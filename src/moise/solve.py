"""Solve a linear rational-expectations system with the QZ (generalized Schur) decomposition.

System:   F_lag y_{t-1} + F_0 y_t + F_lead E_t y_{t+1} + G e_t + c = 0
Solution: y_t = ybar + P (y_{t-1} - ybar) + Q e_t

Method (Klein 2000; Uhlig 1999, companion form). Write X_t = [y_t; y_{t-1}]:

    [F_lead 0] [y_{t+1}]   [-F_0  -F_lag] [y_t    ]
    [0      I] [y_t    ] = [ I     0    ] [y_{t-1}]      i.e.  A E_t X_{t+1} = B X_t

A unique stable solution exists when exactly n generalized eigenvalues of (B, A) lie inside the
unit circle (Blanchard and Kahn 1980) and the y_{t-1} block of the stable deflating subspace is
invertible. Then P = Z11 Z21^{-1} and Q = -(F_lead P + F_0)^{-1} G.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import scipy.linalg as la

from .model import LinearSystem


class SolveError(RuntimeError):
    """No unique stable solution (or a numerical failure)."""

    def __init__(self, message, eigenvalues=None, n_stable=None, n_required=None):
        super().__init__(message)
        self.eigenvalues = eigenvalues
        self.n_stable = n_stable
        self.n_required = n_required


@dataclass
class Solution:
    system: LinearSystem
    P: np.ndarray
    Q: np.ndarray
    ybar: np.ndarray | None        # deterministic steady state of y (None if the constants have none)
    eigenvalues: np.ndarray        # moduli-sorted generalized eigenvalues (inf for infinite)
    n_stable: int
    residual: float                # max |F_lead P^2 + F_0 P + F_lag|
    steady_state_error: str | None = None

    @property
    def variables(self):
        return self.system.variables

    def index(self, name: str) -> int:
        return self.system.variables.index(name)


def steady_state(sys: LinearSystem) -> np.ndarray:
    """Deterministic steady state ybar of the linear system (0 when there are no constants)."""
    if not np.any(sys.c):
        return np.zeros(len(sys.variables))
    M = sys.F_lag + sys.F_0 + sys.F_lead
    ybar, *_ = la.lstsq(M, -sys.c)
    if np.max(np.abs(M @ ybar + sys.c)) > 1e-8 * max(1.0, np.max(np.abs(sys.c))):
        raise SolveError("the constants are inconsistent: no deterministic steady state")
    return ybar


def solve(sys: LinearSystem, qz_criterium: float = 1.0 + 1e-9) -> Solution:
    """Solve the system; raise SolveError if there is no unique stable solution.

    qz_criterium: eigenvalues with modulus below this are stable (Dynare's default is 1+1e-6,
    which also counts exact unit roots as stable).
    """
    n = len(sys.variables)
    I, Z0 = np.eye(n), np.zeros((n, n))
    A = np.block([[sys.F_lead, Z0], [Z0, I]])
    B = np.block([[-sys.F_0, -sys.F_lag], [I, Z0]])

    def stable(alpha, beta):
        return np.abs(alpha) < qz_criterium * np.abs(beta)

    try:
        BB, AA, alpha, beta, Qm, Zm = la.ordqz(B, A, sort=stable, output="complex")
    except (la.LinAlgError, ValueError) as e:
        raise SolveError(f"QZ decomposition failed: {e}") from e
    with np.errstate(divide="ignore", invalid="ignore"):
        lam = np.where(np.abs(beta) > 0, np.abs(alpha) / np.abs(beta), np.inf)
    n_stable = int(np.sum(stable(alpha, beta)))
    eig = np.sort(lam)
    if n_stable != n:
        kind = "indeterminate (too many stable roots)" if n_stable > n else "no stable solution (too few stable roots)"
        raise SolveError(f"Blanchard-Kahn condition fails: {n_stable} stable roots for {n} variables - {kind}",
                         eig, n_stable, n)
    Z11, Z21 = Zm[:n, :n], Zm[n:, :n]
    if np.linalg.cond(Z21) > 1e12:
        raise SolveError("rank condition fails: the stable subspace does not pin down y_t from y_{t-1}",
                         eig, n_stable, n)
    P = np.real_if_close(Z11 @ np.linalg.inv(Z21), tol=1e6)
    if np.iscomplexobj(P):
        if np.max(np.abs(P.imag)) > 1e-8:
            raise SolveError("solution has a non-negligible imaginary part", eig, n_stable, n)
        P = P.real
    M = sys.F_lead @ P + sys.F_0
    if np.linalg.cond(M) > 1e12:
        raise SolveError("F_lead P + F_0 is singular: shock responses are not determined", eig, n_stable, n)
    Q = -np.linalg.solve(M, sys.G)
    residual = float(np.max(np.abs(sys.F_lead @ P @ P + sys.F_0 @ P + sys.F_lag))) if n else 0.0
    if residual > 1e-6:
        raise SolveError(f"solution does not satisfy the model (residual {residual:.2e})", eig, n_stable, n)
    try:
        ybar, ss_error = steady_state(sys), None
    except SolveError as e:          # constants with no steady state: dynamics are still fine
        ybar, ss_error = None, str(e)
    return Solution(sys, P, Q, ybar, eig, n_stable, residual, ss_error)
