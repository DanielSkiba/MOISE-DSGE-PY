# Instructions for AI coding agents (Claude, Cursor, etc.)

This file applies to any AI agent working in this repository.

## Project
Independent Python replication of the Bank of Israel MOISE DSGE model (Argov et al., 2012, DP 2012.06). Not affiliated with the Bank of Israel.

## Where the paper is
Work from **`docs/paper/`**, not from the PDF. Start with `docs/paper/README.md`. The log-linearized
model is `docs/paper/10-log-linear-model.md` (each equation has LaTeX and a code form); symbol code
names are in `docs/paper/data/notation_codes.csv`; parameter values in `docs/paper/data/`. Read the
"Known issues" section of that README before implementing anything — the paper has misprints, and
they are transcribed as printed.

## Hard rules
1. **Do not invent equations or parameter values.** Every entry in `model/moise.yaml` must come from the paper (via `docs/paper/`), with `paper_eq` and `page` filled in. Use the code names from `docs/paper/data/notation_codes.csv`. If something is unclear, leave a `TODO` in `notes` instead of guessing.
2. **Never set `verified: true`.** Only humans verify equations.
3. **Keep model and solver separate.** No Israel-specific logic in `src/moise/`; the solver must work on any linear model defined in the YAML format.
4. **Do not simplify or substitute equations** while transcribing, even when algebraically equivalent.
5. **Tests before claims.** Do not state that the model "replicates" the paper unless the replication tests in `tests/` pass.
6. Do not commit the paper PDF (it is git-ignored) or reproduce long passages from it.
7. **Do not "fix" the paper's misprints in `docs/paper/`.** It records the paper as printed. Decide how to handle a misprint in `model/moise.yaml` (with a `notes` entry), not by editing the transcription.
8. After any change to `docs/paper/`, run `python tools/paper/check_paper.py` (and `--fix-code --write-json` if you changed LaTeX in Appendix D).

## Stack
Python ≥ 3.10, NumPy, SciPy, PyYAML, pytest. No Dynare dependency. Code should stay Pyodide-compatible (no compiled extensions beyond NumPy/SciPy).

## Spec
See `docs/equation-spec.md` for the YAML format and `docs/ROADMAP.md` for phases.
