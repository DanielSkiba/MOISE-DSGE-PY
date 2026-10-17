"""Impulse responses, simulation and forecast-error variance decomposition."""
from __future__ import annotations

import numpy as np
import scipy.linalg as la

from .solve import Solution


def _report_index(sol: Solution, name: str) -> tuple[int, int]:
    rep = sol.system.reported
    if name in rep:
        sysname, shift = rep[name]
        return sol.index(sysname), shift
    return sol.index(name), 0


def impulse_response(sol: Solution, shock: str, periods: int = 20, size: float | None = None,
                     variables: list[str] | None = None) -> dict[str, np.ndarray]:
    """Response of each variable to a shock at t = 0, as deviations from steady state.

    size: shock size in units of the innovation; default one standard deviation.
    Predetermined (beginning-of-period) variables are reported with their own timing,
    so they do not move on impact.
    """
    sys = sol.system
    k = sys.shocks.index(shock)
    e = sys.shock_std[k] if size is None else size
    n = len(sys.variables)
    path = np.zeros((periods + 1, n))
    path[0] = sol.Q[:, k] * e
    for t in range(1, periods + 1):
        path[t] = sol.P @ path[t - 1]
    names = variables or list(sys.reported)
    out = {}
    for v in names:
        i, shift = _report_index(sol, v)
        series = np.concatenate([np.zeros(shift), path[:, i]])[:periods]
        out[v] = series
    return out


def simulate(sol: Solution, periods: int, seed: int | None = None,
             variables: list[str] | None = None) -> dict[str, np.ndarray]:
    """Simulate the model with Gaussian innovations (levels include the steady state ybar)."""
    sys = sol.system
    if sol.ybar is None:
        raise ValueError(f"no deterministic steady state to simulate around: {sol.steady_state_error}")
    rng = np.random.default_rng(seed)
    eps = rng.standard_normal((periods, len(sys.shocks))) * sys.shock_std
    y = np.zeros(len(sys.variables))
    out = np.zeros((periods, len(sys.variables)))
    for t in range(periods):
        y = sol.P @ y + sol.Q @ eps[t]
        out[t] = y
    names = variables or list(sys.reported)
    res = {}
    for v in names:
        i, shift = _report_index(sol, v)
        s = out[:, i] + sol.ybar[i]
        res[v] = np.concatenate([np.full(shift, sol.ybar[i]), s])[:periods]
    return res


def unconditional_variance_by_shock(sol: Solution, tol: float = 1e-15, max_iter: int = 64) -> np.ndarray:
    """Unconditional variance of every variable due to each shock: array (n variables, m shocks).

    Only the state block of P (columns that are not identically zero) is iterated:
    x_t = A x_{t-1} + q e_t with A = P[S, S], so Var(x) = sum_j A^j q q' A'^j, summed by doubling
    (X <- X + A X A', A <- A A). Then Var(y) = P[:, S] Var(x) P[:, S]' + q q'.
    """
    sys = sol.system
    P, Q = sol.P, sol.Q * sys.shock_std
    n, m = Q.shape
    S = np.flatnonzero(np.any(P != 0, axis=0))
    if len(S) == 0:
        return Q ** 2
    A = P[np.ix_(S, S)]
    if np.max(np.abs(la.eigvals(A))) >= 1:
        raise ValueError("the solution has a unit or explosive root: unconditional variance is not defined")
    X = np.einsum("ik,jk->kij", Q[S], Q[S])           # (m, s, s): q_k q_k'
    Ak = A
    for _ in range(max_iter):
        X = X + Ak @ X @ Ak.T
        Ak = Ak @ Ak
        if np.max(np.abs(Ak)) < tol:
            break
    else:
        raise ValueError("unconditional variance did not converge")
    B = P[:, S]
    return ((B @ X) * B).sum(axis=2).T + Q ** 2


def variance_decomposition(sol: Solution, horizons=(1, 4, None),
                           variables: list[str] | None = None) -> dict:
    """Share (in %) of each shock in the forecast-error variance of each variable.

    horizons: forecast horizons in periods (1 = one step ahead); None means the unconditional
    variance (infinite horizon). Returns {horizon: {variable: {shock: percent}}}.
    """
    sys = sol.system
    names = variables or list(sys.reported)
    n, m = len(sys.variables), len(sys.shocks)
    finite = [h for h in horizons if h is not None]
    hmax = max(finite) if finite else 0
    # cum[h][:, k] = diag of the h-step forecast-error covariance due to shock k
    cum = {0: np.zeros((n, m))}
    acc = np.zeros((n, m))
    Ph = np.eye(n)
    for h in range(1, hmax + 1):
        acc = acc + (Ph @ (sol.Q * sys.shock_std)) ** 2
        cum[h] = acc.copy()
        Ph = sol.P @ Ph
    if None in horizons:
        unc = unconditional_variance_by_shock(sol)
    out = {}
    for h in horizons:
        res = {}
        for v in names:
            i, shift = _report_index(sol, v)
            row = unc[i] if h is None else cum[max(h - shift, 0)][i]
            tot = row.sum()
            res[v] = {s: (100 * row[k] / tot if tot > 0 else 0.0) for k, s in enumerate(sys.shocks)}
        out[h] = res
    return out
