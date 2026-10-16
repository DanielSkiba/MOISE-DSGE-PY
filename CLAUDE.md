# Instructions for AI coding agents (Claude, Cursor, etc.)

This file applies to any AI agent working in this repository.

## Project
Independent Python replication of the Bank of Israel MOISE DSGE model (Argov et al., 2012, DP 2012.06). Not affiliated with the Bank of Israel.

## Hard rules
1. **Do not invent equations or parameter values.** Every entry in `model/moise.yaml` must come from the paper, with `paper_eq` and `page` filled in. If you cannot read it clearly, leave a `TODO` in `notes` instead of guessing.
2. **Never set `verified: true`.** Only humans verify equations.
3. **Keep model and solver separate.** No Israel-specific logic in `src/moise/`; the solver must work on any linear model defined in the YAML format.
4. **Do not simplify or substitute equations** while transcribing, even when algebraically equivalent.
5. **Tests before claims.** Do not state that the model "replicates" the paper unless the replication tests in `tests/` pass.
6. Do not commit the paper PDF (it is git-ignored) or reproduce long passages from it.

## Stack
Python ≥ 3.10, NumPy, SciPy, PyYAML, pytest. No Dynare dependency. Code should stay Pyodide-compatible (no compiled extensions beyond NumPy/SciPy).

## Spec
See `docs/equation-spec.md` for the YAML format and `docs/ROADMAP.md` for phases.
