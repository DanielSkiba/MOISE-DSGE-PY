"""Replication tests: impulse responses against the paper's Figures 6-18 and the variance
decomposition against Table 7.

What is compared
----------------
* The figures plot the posterior MEAN of the impulse responses over parameter draws (Bayesian IRFs),
  so the closest single-parameter comparison is the model at the posterior-mean parameters
  (``param_set="posterior_mean"``). The posterior mode is checked more loosely.
* The digitized curves are in docs/paper/data/irf (series "mean"; quarter 1 = impact). Panel units and
  the variable behind each panel are in the ``reporting`` section of model/moise.yaml.
* "Relative RMSE" = RMSE / largest absolute value of the digitized curve.

Known, explained differences (see docs/phase1-report.md)
--------------------------------------------------------
* Figure 6 (interest-rate shock) is about 0.8 times the figure in every panel with near-perfect
  correlation: the shock S.D. is printed as 0.002 (rounded); about 0.0025 reproduces the figure.
* Figure 14 (investment technology) output: rho_I is poorly identified (mode 0.906, mean 0.732), so
  the mean of the responses over draws differs from the response at the mean parameters.
"""
import csv
from pathlib import Path

import numpy as np
import pytest
import yaml

import moise

ROOT = Path(__file__).resolve().parents[1]
SPEC = yaml.safe_load((ROOT / "model" / "moise.yaml").read_text(encoding="utf-8"))
IRF = SPEC["reporting"]["irf"]
VD = SPEC["reporting"]["variance_decomposition"]
IRF_DIR = ROOT / "docs" / "paper" / "data" / "irf"
SHAPE_EXCEPTIONS = {(14, "Output")}


def digitized():
    out = {}
    for f in IRF["figures"]:
        series = {}
        with (IRF_DIR / f["file"]).open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r["series"] == "mean":
                    series.setdefault(r["panel_title"], {})[int(r["quarter"])] = float(r["value"])
        out[f["figure"]] = {p: np.array([v[q] for q in sorted(v)]) for p, v in series.items()}
    return out


FIGS = digitized()


def model_curves(sol):
    panels = IRF["panels"]
    out = {}
    for f in IRF["figures"]:
        irf = moise.impulse_response(sol, f["shock"], periods=IRF["horizon"], variables=[p["variable"] for p in panels])
        out[f["figure"]] = {p["panel"]: irf[p["variable"]] * p["scale"] for p in panels}
    return out


def panel_stats(sol):
    """(figure, panel) -> dict(corr, size, sign, rel_rmse)."""
    model = model_curves(sol)
    stats = {}
    for fig, panels in FIGS.items():
        for panel, data in panels.items():
            m = model[fig][panel]
            peak = int(np.argmax(np.abs(data)))
            scale = np.max(np.abs(data))
            stats[(fig, panel)] = dict(
                corr=float(np.corrcoef(m, data)[0, 1]),
                size=float(np.max(np.abs(m)) / scale),
                sign=bool(np.sign(m[peak]) == np.sign(data[peak])),
                rel_rmse=float(np.sqrt(np.mean((m - data) ** 2)) / scale))
    return stats


def solve(**kw):
    return moise.solve(moise.load(blocks_excluded=("measurement",), **kw).linear_system())


@pytest.fixture(scope="module")
def mean_stats():
    return panel_stats(solve(param_set="posterior_mean"))


def test_all_figures_and_panels_are_compared(mean_stats):
    assert len(FIGS) == 13
    assert all(len(p) == 12 for p in FIGS.values())
    assert len(mean_stats) == 156


def test_irf_signs_match_every_panel(mean_stats):
    wrong = [k for k, s in mean_stats.items() if not s["sign"]]
    assert not wrong, f"sign differs at the peak in {wrong}"


def test_irf_shapes(mean_stats):
    corr = np.array([s["corr"] for s in mean_stats.values()])
    assert np.median(corr) > 0.995
    bad = {k: round(s["corr"], 3) for k, s in mean_stats.items() if s["corr"] < 0.9 and k not in SHAPE_EXCEPTIONS}
    assert not bad, f"low correlation with the figure: {bad}"
    assert all(mean_stats[k]["corr"] > 0.5 for k in SHAPE_EXCEPTIONS)


def test_irf_magnitudes(mean_stats):
    size = np.array([s["size"] for s in mean_stats.values()])
    assert 0.9 < np.median(size) < 1.1
    bad = {k: round(s["size"], 2) for k, s in mean_stats.items() if not 0.65 < s["size"] < 1.35}
    assert not bad, f"peak magnitude off by more than 35%: {bad}"
    rmse = np.array([s["rel_rmse"] for s in mean_stats.values()])
    assert np.median(rmse) < 0.06 and np.mean(rmse) < 0.08


def test_irfs_lie_inside_the_papers_credible_bands():
    """At least 99% of the 3,120 points (13 figures x 12 panels x 20 quarters) are inside the 90% band."""
    bands = {}
    for f in IRF["figures"]:
        with (IRF_DIR / f["file"]).open(encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                bands.setdefault((f["figure"], r["panel_title"], r["series"]), {})[int(r["quarter"])] = float(r["value"])
    model = model_curves(solve(param_set="posterior_mean"))
    inside = total = 0
    for fig, panels in model.items():
        for panel, m in panels.items():
            lo = np.array([bands[(fig, panel, "hpd90_lower")][q] for q in range(1, IRF["horizon"] + 1)])
            hi = np.array([bands[(fig, panel, "hpd90_upper")][q] for q in range(1, IRF["horizon"] + 1)])
            inside += int(np.sum((m >= np.minimum(lo, hi) - 1e-9) & (m <= np.maximum(lo, hi) + 1e-9)))
            total += len(m)
    assert total == 3120
    assert inside / total > 0.99, f"{inside}/{total} points inside the 90% bands"


def test_figure6_differs_only_by_scale(mean_stats):
    """The interest-rate shock responses have the right shape but are ~0.8 of the figure (rounded S.D.)."""
    fig6 = [s for (f, _), s in mean_stats.items() if f == 6]
    assert min(s["corr"] for s in fig6) > 0.99
    sizes = np.array([s["size"] for s in fig6])
    assert 0.7 < sizes.min() and sizes.max() < 1.05


def test_posterior_mode_is_close_too():
    stats = panel_stats(solve(param_set="value"))
    assert all(s["sign"] for s in stats.values())
    assert np.median([s["corr"] for s in stats.values()]) > 0.98
    assert np.median([s["rel_rmse"] for s in stats.values()]) < 0.12


def _mean_rmse(**kw):
    return np.mean([s["rel_rmse"] for s in panel_stats(solve(param_set="posterior_mean", **kw)).values()])


@pytest.mark.parametrize("decision,alternative", [("D05", "printed"), ("D07", "main_text"), ("D09", "main_text"),
                                                  ("D13", "printed"), ("D18", "printed")])
def test_figures_support_the_adopted_choice(decision, alternative):
    """Evidence recorded in the decisions of moise.yaml: the adopted form fits Figures 6-18 better."""
    adopted = _mean_rmse()
    other = _mean_rmse(decisions={decision: alternative})
    assert adopted < other - 0.01, f"{decision}: adopted {adopted:.3f} vs {alternative} {other:.3f}"


# ----------------------------------------------------------------------------- Table 6
TABLE6 = {r"$\Delta C$": "Delta_C", r"$\Delta X$": "Delta_X", r"$\Delta I$": "Delta_I_NI", r"$\Delta IM$": "Delta_IM",
          r"$\Delta Y$": "Delta_Y", r"$\Delta P_{c}$": "Delta_P_C", r"$\Delta S$": "Delta_S", r"$r^{OB}$": "r_OB",
          r"$\Delta W$": "Delta_W", r"$\Delta N$": "Delta_N", r"$s_{CA}$": "S_CA"}


def test_observable_moments_match_table6():
    """Means and S.D.s of the 11 observables of Table 6 (percent), at the posterior mean.

    Table 6 reports the median over simulated 72-quarter samples. For the growth rates this is close
    to the population moment. The policy rate (r_OB) and the current account are persistent, so their
    small-sample S.D. is below the population one, and the sample mean of r_OB depends on where the
    simulations start (its 90% interval is -2.15 to 12.89); for r_OB only the interval is checked.
    """
    sol = moise.solve(moise.load(param_set="posterior_mean").linear_system())
    var = moise.irf.unconditional_variance_by_shock(sol).sum(axis=1)
    with (ROOT / "docs/paper/data/table6_moments.csv").open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 11
    for r in rows:
        v = TABLE6[r["Variable"]]
        i = sol.index(v)
        mean, sd = 100 * sol.ybar[i], 100 * np.sqrt(var[i])
        if v == "r_OB":
            assert float(r["Mean 5%"]) < mean < float(r["Mean 95%"])
            assert sd > float(r["Standard Deviation Median"])
            continue
        assert mean == pytest.approx(float(r["Mean Median"]), abs=0.03), v
        tol = 0.10 if v == "S_CA" else 0.05
        assert sd == pytest.approx(float(r["Standard Deviation Median"]), rel=tol), v


# ----------------------------------------------------------------------------- Table 7
def table7():
    var = {v["table"]: v["variable"] for v in VD["variables"]}
    shock = {s["table"]: s["shock"] for s in VD["shocks"]}
    out = {}
    with (ROOT / "docs/paper/data/table7_variance_decomposition.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for h, col in ((1, "h1"), (4, "h4"), (None, "h_inf")):
                out.setdefault(h, {}).setdefault(var[r["variable"]], {})[shock[r["shock"]]] = float(r[col])
    return out


def test_variance_decomposition_matches_table7():
    t7 = table7()
    sol = moise.solve(moise.load(param_set="posterior_mean").linear_system())   # full model: r_OB, Delta_P_C
    shocks = [s["shock"] for s in VD["shocks"]]
    vd = moise.variance_decomposition(sol, horizons=(1, 4, None), variables=list(t7[1]))
    diffs, top_ok, n = [], 0, 0
    for h in (1, 4, None):
        for v, row in t7[h].items():
            total = sum(vd[h][v][s] for s in shocks)          # the table covers the 25 structural shocks
            model = {s: 100 * vd[h][v][s] / total for s in shocks}
            diffs += [abs(model[s] - row[s]) for s in shocks]
            # the table's largest contributor is among the model's two largest
            top = max(row, key=row.get)
            top_ok += top in sorted(model, key=model.get)[-2:]
            n += 1
    diffs = np.array(diffs)
    assert diffs.mean() < 0.6, f"mean |difference| {diffs.mean():.2f} pp"
    assert np.median(diffs) < 0.15
    assert np.percentile(diffs, 95) < 2.5
    assert top_ok / n > 0.9, f"largest contributor matches in {top_ok}/{n} columns"
