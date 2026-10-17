"""Load a linear rational-expectations model from YAML and build its matrices.

Nothing in this module is specific to MOISE. A model file (see ``docs/equation-spec.md``) has:

* ``variables``      endogenous variables (``predetermined: true`` marks beginning-of-period stocks
                     written as ``x(+1) = f(x, ...)``, which are re-timed as Dynare's
                     ``predetermined_variables`` does)
* ``shocks``         i.i.d. innovations with standard deviations
* ``parameters``     numbers or expressions in earlier parameters
* ``steady_state``   ordered assignments (expressions in parameters and earlier entries)
* ``aliases``        names that stand for another name (e.g. two printed spellings of one variable)
* ``exogenous_zero`` names fixed at zero (variables that do not move in this model)
* ``equations``      ``expr`` strings, linear in the variables, ``printed`` as in the source
* ``decisions``      documented departures from the printed source; each can be switched back
                     to ``printed`` when loading, to test its effect

The equations are evaluated numerically: because they must be linear in the variables, each
coefficient is the change in the residual when one variable is set to 1. Linearity is checked.
"""
from __future__ import annotations

import math
import random
from dataclasses import dataclass, field
from typing import Iterable

import numpy as np
import yaml

from . import expr as ex


class ModelError(ValueError):
    """Raised for problems in the model definition."""


@dataclass
class Equation:
    id: str
    text: str
    node: ex.Node
    block: str
    meta: dict


@dataclass
class LinearSystem:
    """F_lag y_{t-1} + F_0 y_t + F_lead E_t y_{t+1} + G e_t + c = 0."""
    variables: list[str]
    shocks: list[str]
    F_lag: np.ndarray
    F_0: np.ndarray
    F_lead: np.ndarray
    G: np.ndarray
    c: np.ndarray
    equation_ids: list[str]
    shock_std: np.ndarray
    reported: dict[str, tuple[str, int]] = field(default_factory=dict)
    """model variable -> (system variable, shift); predetermined x_t = X_{t-1} has shift 1."""


def _num(v, what):
    if isinstance(v, bool) or v is None:
        raise ModelError(f"{what}: expected a number, got {v!r}")
    return float(v)


class Model:
    """A parsed model. Use :meth:`from_yaml`, then :meth:`linear_system`."""

    def __init__(self, spec: dict, decisions: dict[str, str] | None = None,
                 param_set: str = "value", blocks_excluded: Iterable[str] = (),
                 overrides: dict[str, float] | None = None):
        self.spec = spec
        self.choices = self._decision_choices(decisions or {})
        self.param_set = param_set
        self.blocks_excluded = set(blocks_excluded)
        self.overrides = dict(overrides or {})
        self.values: dict[str, float] = {}
        self._evaluate_parameters()
        self._read_symbols()
        self._read_equations()

    # ------------------------------------------------------------------ construction
    @classmethod
    def from_yaml(cls, path: str, **kwargs) -> "Model":
        with open(path, encoding="utf-8") as f:
            spec = yaml.safe_load(f)
        return cls(spec, **kwargs)

    def _decision_choices(self, decisions):
        known = {d["id"]: d for d in self.spec.get("decisions", []) or []}
        choices = {k: "adopted" for k in known}
        for k, v in decisions.items():
            if k not in known:
                raise ModelError(f"unknown decision {k!r}")
            allowed = ["adopted"] + list(known[k].get("alternatives", []) or [])
            if v not in allowed:
                raise ModelError(f"decision {k}: choice {v!r} not in {allowed}")
            choices[k] = v
        return choices

    def _choice(self, item: dict) -> str:
        d = item.get("decision")
        return self.choices.get(d, "adopted") if d else "adopted"

    def _pick(self, item: dict, what: str, key: str = "expr") -> str:
        """Return the expression to use for an item that may depend on a decision.

        choice 'adopted' -> item[key]; 'printed' -> item['printed']; any other choice c ->
        item['alternatives'][c] (falling back to item[key] if the item has no such alternative,
        so one decision can switch several items, each of which lists only what it changes).
        """
        choice = self._choice(item)
        if choice == "printed":
            if item.get("printed") is None:
                raise ModelError(f"{what}: decision {item['decision']} set to 'printed' but nothing is printed")
            return item["printed"]
        if choice != "adopted" and choice in (item.get("alternatives") or {}):
            return item["alternatives"][choice]
        if item.get(key) is None:
            raise ModelError(f"{what}: missing '{key}'")
        return item[key]

    def _lookup_value(self, name, lag, where):
        if lag != 0:
            raise ModelError(f"{where}: {name}({lag:+d}) - parameters have no time index")
        if name not in self.values:
            raise ModelError(f"{where}: unknown name {name!r}")
        return self.values[name]

    def _evaluate_parameters(self):
        for p in self.spec.get("parameters", []) or []:
            name = p["name"]
            if name in self.overrides:
                self.values[name] = float(self.overrides[name])
                continue
            raw = p.get(self.param_set, p.get("value")) if self.param_set != "value" else p.get("value")
            choice = self._choice(p)
            if choice == "printed" and "printed" in p:
                raw = p["printed"]
            elif choice in (p.get("alternatives") or {}):
                raw = p["alternatives"][choice]
            if raw is None:
                raise ModelError(f"parameter {name}: no value (set one or pass it in overrides)")
            if isinstance(raw, str):
                node = ex.parse(raw)
                try:
                    self.values[name] = ex.evaluate(node, lambda n, l: self._lookup_value(n, l, f"parameter {name}"))
                except (ZeroDivisionError, ValueError, OverflowError) as e:
                    raise ModelError(f"parameter {name}: {e}") from e
            else:
                self.values[name] = _num(raw, f"parameter {name}")
        for s in self.spec.get("steady_state", []) or []:
            name = s["name"]
            if name in self.values:
                raise ModelError(f"steady_state {name}: already defined")
            node = ex.parse(self._pick(s, f"steady_state {name}"))
            try:
                v = ex.evaluate(node, lambda n, l: self._lookup_value(n, l, f"steady_state {name}"))
            except (ZeroDivisionError, ValueError, OverflowError) as e:
                raise ModelError(f"steady_state {name}: {e}") from e
            if not math.isfinite(v):
                raise ModelError(f"steady_state {name}: not finite ({v})")
            self.values[name] = v

    def _read_symbols(self):
        self.var_spec = {}
        for v in self.spec.get("variables", []) or []:
            if v["name"] in self.var_spec:
                raise ModelError(f"variable {v['name']} declared twice")
            self.var_spec[v["name"]] = v
        self.aliases = {a["name"]: a["target"] for a in self.spec.get("aliases", []) or []
                        if not (a.get("decision") and self.choices.get(a["decision"]) == "printed")}
        self.zero = {z["name"] for z in self.spec.get("exogenous_zero", []) or []
                     if not (z.get("decision") and self.choices.get(z["decision"]) == "printed")}
        self.shock_spec = {}
        for s in self.spec.get("shocks", []) or []:
            if s["name"] in self.shock_spec:
                raise ModelError(f"shock {s['name']} declared twice")
            self.shock_spec[s["name"]] = s
        clash = (set(self.var_spec) & set(self.shock_spec)) | (set(self.var_spec) & set(self.values)) \
            | (set(self.shock_spec) & set(self.values))
        if clash:
            raise ModelError(f"names declared in more than one section: {sorted(clash)}")

    def _resolve(self, node: ex.Node) -> ex.Node:
        """Apply aliases and fixed-zero names."""
        if isinstance(node, ex.Var):
            name, seen = node.name, set()
            while name in self.aliases:
                if name in seen:
                    raise ModelError(f"alias cycle at {name}")
                seen.add(name)
                name = self.aliases[name]
            if name in self.zero:
                return ex.Num(0.0)
            return ex.Var(name, node.lag)
        if isinstance(node, ex.Neg):
            return ex.Neg(self._resolve(node.arg))
        if isinstance(node, ex.Func):
            return ex.Func(node.name, self._resolve(node.arg))
        if isinstance(node, ex.Bin):
            return ex.Bin(node.op, self._resolve(node.left), self._resolve(node.right))
        return node

    def _read_equations(self):
        self.equations: list[Equation] = []
        seen = set()
        for e in self.spec.get("equations", []) or []:
            if e.get("block") in self.blocks_excluded:
                continue
            eid = str(e["id"])
            if eid in seen:
                raise ModelError(f"equation id {eid} appears twice")
            seen.add(eid)
            text = self._pick(e, f"equation {eid}")
            try:
                node = self._resolve(ex.parse_equation(text))
            except ex.ExprError as err:
                raise ModelError(f"equation {eid}: {err}") from err
            self.equations.append(Equation(eid, text, node, e.get("block", ""), e))

    # ------------------------------------------------------------------ queries
    def shock_std(self, name: str) -> float:
        """Innovation S.D. for the selected parameter set (``std`` unless the shock has that key)."""
        s = self.shock_spec[name]
        if name in self.overrides:
            return float(self.overrides[name])
        raw = s.get(self.param_set) if self.param_set != "value" and s.get(self.param_set) is not None else s.get("std")
        if isinstance(raw, str):
            return float(ex.evaluate(ex.parse(raw), lambda n, l: self._lookup_value(n, l, f"shock {name}")))
        return _num(raw, f"shock {name} std")

    @property
    def endogenous(self) -> list[str]:
        """Endogenous variables used by the selected equations, in declaration order."""
        used = set()
        for eq in self.equations:
            used |= {n for n, _ in ex.names(eq.node) if n in self.var_spec}
        return [v for v in self.var_spec if v in used]

    def check_names(self) -> list[str]:
        """Names in equations that are not declared anywhere (should be empty)."""
        bad = set()
        for eq in self.equations:
            for n, lag in ex.names(eq.node):
                if n in self.var_spec or n in self.shock_spec:
                    continue
                if n in self.values:
                    if lag != 0:
                        bad.add(f"{n}({lag:+d}) in {eq.id}: parameter with a time index")
                    continue
                bad.add(f"{n} in {eq.id}")
        return sorted(bad)

    # ------------------------------------------------------------------ linearization
    def linear_system(self, check_linearity: bool = True) -> LinearSystem:
        bad = self.check_names()
        if bad:
            raise ModelError("undeclared names: " + "; ".join(bad))
        endo = self.endogenous
        pred = {v for v in endo if self.var_spec[v].get("predetermined")}
        shocks_used = []
        for eq in self.equations:
            for n, lag in ex.names(eq.node):
                if n in self.shock_spec:
                    if lag != 0:
                        raise ModelError(f"equation {eq.id}: shock {n} with a time index")
                    if n not in shocks_used:
                        shocks_used.append(n)
        shocks = [s for s in self.shock_spec if s in shocks_used]

        # re-time predetermined variables: x(k) -> x(k-1) (x now denotes the end-of-period stock)
        def retime(node):
            if isinstance(node, ex.Var) and node.name in pred:
                return ex.Var(node.name, node.lag - 1)
            if isinstance(node, ex.Neg):
                return ex.Neg(retime(node.arg))
            if isinstance(node, ex.Func):
                return ex.Func(node.name, retime(node.arg))
            if isinstance(node, ex.Bin):
                return ex.Bin(node.op, retime(node.left), retime(node.right))
            return node

        rows = [(eq.id, retime(eq.node)) for eq in self.equations]

        # auxiliary variables for leads > 1 and lags < -1
        max_lead, max_lag = {}, {}
        for _, node in rows:
            for n, lag in ex.names(node):
                if n in self.var_spec:
                    max_lead[n] = max(max_lead.get(n, 0), lag)
                    max_lag[n] = min(max_lag.get(n, 0), lag)
        aux_vars, aux_rows = [], []

        def lead_name(n, j):
            return n if j == 0 else f"{n}__lead{j}"

        def lag_name(n, j):
            return n if j == 0 else f"{n}__lag{j}"

        for n in endo:
            for j in range(1, max_lead.get(n, 0)):
                aux_vars.append(lead_name(n, j))
                # n__lead{j}_t = n__lead{j-1}_{t+1}
                aux_rows.append((f"aux:{lead_name(n, j)}",
                                 ex.Bin("-", ex.Var(lead_name(n, j), 0), ex.Var(lead_name(n, j - 1), 1))))
            for j in range(1, -max_lag.get(n, 0)):
                aux_vars.append(lag_name(n, j))
                aux_rows.append((f"aux:{lag_name(n, j)}",
                                 ex.Bin("-", ex.Var(lag_name(n, j), 0), ex.Var(lag_name(n, j - 1), -1))))

        def substitute(node):
            if isinstance(node, ex.Var) and node.name in self.var_spec:
                if node.lag > 1:
                    return ex.Var(lead_name(node.name, node.lag - 1), 1)
                if node.lag < -1:
                    return ex.Var(lag_name(node.name, -node.lag - 1), -1)
                return node
            if isinstance(node, ex.Neg):
                return ex.Neg(substitute(node.arg))
            if isinstance(node, ex.Func):
                return ex.Func(node.name, substitute(node.arg))
            if isinstance(node, ex.Bin):
                return ex.Bin(node.op, substitute(node.left), substitute(node.right))
            return node

        rows = [(i, substitute(nd)) for i, nd in rows] + aux_rows
        allvars = endo + aux_vars
        if len(rows) != len(allvars):
            raise ModelError(f"{len(rows)} equations for {len(allvars)} variables "
                             f"({len(self.equations)} model equations, {len(endo)} endogenous variables)")
        idx = {v: k for k, v in enumerate(allvars)}
        sidx = {s: k for k, s in enumerate(shocks)}
        n, m = len(allvars), len(shocks)
        F = {-1: np.zeros((n, n)), 0: np.zeros((n, n)), 1: np.zeros((n, n))}
        G = np.zeros((n, m))
        c = np.zeros(n)
        rng = random.Random(12345)
        for r, (eid, node) in enumerate(rows):
            terms = sorted({(nm, lag) for nm, lag in ex.names(node) if nm in idx or nm in sidx})
            point = {}

            def look(nm, lag):
                if (nm, lag) in point:
                    return point[(nm, lag)]
                if nm in idx or nm in sidx:
                    return 0.0
                return self.values[nm]

            base = ex.evaluate(node, look)
            c[r] = base
            coefs = {}
            for t in terms:
                point = {t: 1.0}
                coefs[t] = ex.evaluate(node, look) - base
            if check_linearity and terms:
                point = {t: rng.uniform(-2, 2) for t in terms}
                val = ex.evaluate(node, look)
                lin = base + sum(coefs[t] * point[t] for t in terms)
                scale = max(1.0, abs(val), *(abs(coefs[t] * point[t]) for t in terms))
                if abs(val - lin) > 1e-8 * scale:
                    raise ModelError(f"equation {eid} is not linear in the variables "
                                     f"(difference {val - lin:.3g})")
            for (nm, lag), v in coefs.items():
                if nm in sidx:
                    G[r, sidx[nm]] += v
                elif lag in F:
                    F[lag][r, idx[nm]] += v
                else:
                    raise ModelError(f"equation {eid}: {nm}({lag:+d}) after auxiliary substitution")
        std = np.array([self.shock_std(s) for s in shocks])
        reported = {v: (v, 1 if v in pred else 0) for v in endo}
        return LinearSystem(allvars, shocks, F[-1], F[0], F[1], G, c,
                            [i for i, _ in rows], std, reported)
