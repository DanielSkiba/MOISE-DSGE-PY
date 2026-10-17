"""Solver tests on small models with known analytical solutions."""
import math

import numpy as np
import pytest

from moise import Model, ModelError, SolveError, impulse_response, solve, variance_decomposition
from moise.expr import ExprError, evaluate, parse, parse_equation, to_str


def build(variables, equations, parameters=None, shocks=None, **kw):
    spec = {
        "variables": [v if isinstance(v, dict) else {"name": v} for v in variables],
        "shocks": shocks or [{"name": "e", "std": 1.0}],
        "parameters": [{"name": k, "value": v} for k, v in (parameters or {}).items()],
        "equations": [{"id": str(i), "expr": e} for i, e in enumerate(equations)],
    }
    spec.update(kw)
    return Model(spec)


# ----------------------------------------------------------------------------- parser
def test_parser_precedence_and_keywords():
    assert to_str(parse("a + b*c^2")) == "(a + (b * (c ^ 2)))"
    assert to_str(parse("-x^2")) == "(-(x ^ 2))"
    assert to_str(parse("x^-1")) == "(x ^ (-1))"
    assert to_str(parse("lambda(+1) - lambda")) == "(lambda(+1) - lambda)"
    assert to_str(parse("k(-2)")) == "k(-2)"
    assert evaluate(parse("2^3^2"), lambda n, l: 0) == 512          # right-associative
    assert evaluate(parse("exp(0) + ln(1)"), lambda n, l: 0) == 1
    assert to_str(parse_equation("y = 2*x")) == "(y - (2 * x))"


def test_parser_errors():
    for bad in ("x +", "x(+a)", "(x", "x ? y", "a = b = c"):
        with pytest.raises(ExprError):
            parse_equation(bad)


# ----------------------------------------------------------------------------- solutions
def test_ar1():
    sol = solve(build(["x"], ["x = 0.9*x(-1) + e"]).linear_system())
    assert sol.P[0, 0] == pytest.approx(0.9)
    assert sol.Q[0, 0] == pytest.approx(1.0)
    irf = impulse_response(sol, "e", periods=4)["x"]
    np.testing.assert_allclose(irf, [1, 0.9, 0.81, 0.729])


def test_forward_looking_phillips_curve():
    beta, kappa, rho = 0.99, 0.1, 0.7
    m = build(["pi", "x"], ["pi = beta*pi(+1) + kappa*x", "x = rho*x(-1) + e"],
              {"beta": beta, "kappa": kappa, "rho": rho})
    sol = solve(m.linear_system())
    irf = impulse_response(sol, "e", periods=3)
    a = kappa / (1 - beta * rho)
    np.testing.assert_allclose(irf["pi"], [a, a * rho, a * rho**2], rtol=1e-10)


def test_new_keynesian_determinacy():
    p = {"beta": 0.99, "kappa": 0.1, "sigma": 1.0, "rho": 0.5, "phi": 1.5}
    eqs = ["x = x(+1) - sigma*(i - pi(+1)) + u", "pi = beta*pi(+1) + kappa*x",
           "i = phi*pi", "u = rho*u(-1) + e"]
    sol = solve(build(["x", "pi", "i", "u"], eqs, p).linear_system())
    b_over_a = p["kappa"] / (1 - p["beta"] * p["rho"])
    a = 1 / ((1 - p["rho"]) + p["sigma"] * b_over_a * (p["phi"] - p["rho"]))
    irf = impulse_response(sol, "e", periods=2)
    assert irf["x"][0] == pytest.approx(a, rel=1e-10)
    assert irf["pi"][0] == pytest.approx(a * b_over_a, rel=1e-10)
    # passive policy: indeterminate
    p["phi"] = 0.5
    with pytest.raises(SolveError) as err:
        solve(build(["x", "pi", "i", "u"], eqs, p).linear_system())
    assert err.value.n_stable > err.value.n_required


def test_explosive_has_no_stable_solution():
    with pytest.raises(SolveError) as err:
        solve(build(["x"], ["x = 1.5*x(-1) + e"]).linear_system())
    assert err.value.n_stable < err.value.n_required


def test_predetermined_capital_timing():
    # beginning-of-period stock: k(+1) = a*k + b*z; z = rho*z(-1) + e
    a, b, rho = 0.9, 0.5, 0.8
    m = build([{"name": "k", "predetermined": True}, "z"],
              ["k(+1) = a*k + b*z", "z = rho*z(-1) + e"], {"a": a, "b": b, "rho": rho})
    sol = solve(m.linear_system())
    irf = impulse_response(sol, "e", periods=4)
    np.testing.assert_allclose(irf["k"], [0, b, a * b + b * rho, a * (a * b + b * rho) + b * rho**2])
    np.testing.assert_allclose(irf["z"], [1, rho, rho**2, rho**3])


def test_long_leads_and_lags():
    rho = 0.6
    m = build(["y", "w", "z"], ["y = z(+3)", "w = z(-2)", "z = rho*z(-1) + e"], {"rho": rho})
    sol = solve(m.linear_system())
    irf = impulse_response(sol, "e", periods=5)
    np.testing.assert_allclose(irf["y"], rho**3 * rho ** np.arange(5))
    np.testing.assert_allclose(irf["w"], [0, 0, 1, rho, rho**2])


def test_constants_give_steady_state():
    sol = solve(build(["x"], ["x = 0.5 + 0.9*x(-1) + e"]).linear_system())
    assert sol.ybar[0] == pytest.approx(5.0)


def test_nonlinear_equation_is_rejected():
    with pytest.raises(ModelError, match="not linear"):
        build(["x", "y"], ["x = 0.9*x(-1) + e", "y = x*x"]).linear_system()


def test_undeclared_name_is_rejected():
    with pytest.raises(ModelError, match="undeclared"):
        build(["x"], ["x = rho*x(-1) + e"]).linear_system()


def test_equation_count_must_match():
    with pytest.raises(ModelError, match="equations for"):
        build(["x", "y"], ["x = 0.9*x(-1) + e + y"]).linear_system()


def test_aliases_zero_and_decisions():
    spec = {
        "variables": [{"name": "x"}, {"name": "y"}],
        "shocks": [{"name": "e", "std": 2.0}],
        "parameters": [{"name": "rho", "value": 0.5}, {"name": "c", "value": "2*rho"}],
        "aliases": [{"name": "x_printed", "target": "x"}],
        "exogenous_zero": [{"name": "unused"}],
        "decisions": [{"id": "D1", "alternatives": ["printed"]}],
        "equations": [
            {"id": "1", "expr": "x = rho*x_printed(-1) + e + unused"},
            {"id": "2", "printed": "y = 3*x", "expr": "y = c*x", "decision": "D1"},
        ],
    }
    sol = solve(Model(spec).linear_system())
    irf = impulse_response(sol, "e", periods=2)
    np.testing.assert_allclose(irf["x"], [2, 1])
    np.testing.assert_allclose(irf["y"], [2, 1])           # c = 2*rho = 1
    sol2 = solve(Model(spec, decisions={"D1": "printed"}).linear_system())
    np.testing.assert_allclose(impulse_response(sol2, "e", periods=1)["y"], [6])
    with pytest.raises(ModelError):
        Model(spec, decisions={"D1": "other"})


def test_variance_decomposition_sums_to_100():
    m = build(["x", "y"], ["x = 0.5*x(-1) + e1", "y = 0.8*y(-1) + x + e2"],
              shocks=[{"name": "e1", "std": 1.0}, {"name": "e2", "std": 0.5}])
    sol = solve(m.linear_system())
    vd = variance_decomposition(sol, horizons=(1, 4, None))
    for h in vd:
        for v in ("x", "y"):
            assert sum(vd[h][v].values()) == pytest.approx(100)
    assert vd[1]["x"]["e1"] == pytest.approx(100)
    assert vd[1]["y"]["e1"] == pytest.approx(100 * 1 / (1 + 0.25))
    # unconditional variance of x: 1/(1-0.25)
    assert vd[None]["x"]["e1"] == pytest.approx(100)


def test_saddle_path_matches_closed_form():
    """Two-variable saddle path with a known stable root."""
    # c(+1) = c - s*k ; k(+1) = k/beta - c + z   (k predetermined, z i.i.d.).
    # Roots solve lam^2 - (1 + 1/beta) lam + (1/beta - s) = 0; one is inside the unit circle.
    beta, s = 0.95, 0.2
    m = build(["c", {"name": "k", "predetermined": True}, "z"],
              ["c(+1) = c - s*k", "k(+1) = k/beta - c + z", "z = 0*z(-1) + e"],
              {"beta": beta, "s": s})
    sol = solve(m.linear_system())
    b, d = 1 + 1 / beta, 1 / beta - s
    lam = (b - math.sqrt(b * b - 4 * d)) / 2
    assert 0 < lam < 1 < (b + math.sqrt(b * b - 4 * d)) / 2
    irf = impulse_response(sol, "e", periods=6)
    k = irf["k"]
    theta = s / (1 - lam)                      # saddle path c = theta * k
    c0 = theta / (1 + theta)                   # c_1 = c_0 = theta * (1 - c_0)
    assert irf["c"][0] == pytest.approx(c0, rel=1e-9)
    assert k[0] == 0 and k[1] == pytest.approx(1 - c0, rel=1e-9)
    assert k[3] / k[2] == pytest.approx(lam, rel=1e-9)
    # the explosive version has no saddle path
    m2 = build(["c", {"name": "k", "predetermined": True}, "z"],
               ["c(+1) = c + s*k", "k(+1) = k/beta - c + z", "z = 0*z(-1) + e"],
               {"beta": beta, "s": s})
    with pytest.raises(SolveError):
        solve(m2.linear_system())
