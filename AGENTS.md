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

## Current state (2026-10-31; update or delete this section once PRs #1 and #2 are merged)
- Phase 1 is drafted but **not on `main`**. It is in two stacked PRs waiting for Daniel's review, and #1 must be merged first:
  - **#1** `phase1-solver` → `main`: the generic solver (`src/moise/`: `expr.py`, `model.py`, `solve.py`, `irf.py`) and `tests/test_solver.py`.
  - **#2** `phase1-model` → `phase1-solver`: the full `model/moise.yaml`, `tests/test_model.py`, `tests/test_replication.py`, the report `docs/phase1/README.md` and `tools/replication/plot_irfs.py`. It also rewrites hard rules 2, 5 and 7 above.
- Don't rebuild the solver or the model on `main`. Branch from `phase1-model` (it contains both PRs), or from `phase1-solver` for solver-only work. Ask before pushing to either PR branch.
- In PR #2, `model/moise.yaml` starts with `decisions:` D01–D37, all `status: proposed`. As with `verified` and `verified_by`, only Daniel sets a decision's `status` and `reviewed_by`. Phase 1 is done only after Daniel has reviewed the decisions and verified the equations.

## Commands
Run from the repo root.

```bash
pip install -e ".[dev]"                       # the package, plus pytest and matplotlib
python -m pytest -q                           # all tests; about 20 s with PR #2
python -m pytest tests/<file>.py -k <name>    # a subset
python tools/paper/check_paper.py             # docs/paper consistency; must end with "RESULT: OK"
```

- CI (`.github/workflows/ci.yml`) runs the install, `pytest -q` and `check_paper.py` on Python 3.10 and 3.12. Run the last two before every commit.
- After changing LaTeX anywhere in `docs/paper/`, run `python tools/paper/check_paper.py --fix-code --write-json`, then `python tools/paper/check_paper.py --compile`, and log the change in `docs/verification-log.md`. `--write-json` rebuilds `docs/paper/equations.json`. Nothing checks that file, so a stale copy still passes CI.
- `docs/paper/MOISE_agent_edition.md` is files `00`–`10` joined together. Edit those, not it. PR #1 adds `--write-combined` to rebuild it.
- With PR #2: `python tools/replication/plot_irfs.py` redraws `docs/phase1/figures/` (`--param-set value` for the posterior mode, `--decision D13=printed`, `--out DIR`).
- There is no separate build step, and no linter or formatter is configured or run in CI.
- The editable install points `import moise` at the checkout it was run in. In another worktree, run it again there or set `PYTHONPATH=src`.
- To test on Python 3.10, the oldest version CI uses: `uv venv --clear --python 3.10 /tmp/py310 && uv pip install --python /tmp/py310/bin/python -e ".[dev]" && /tmp/py310/bin/python -m pytest -q`.

### In a Claude Code cloud session
- The container has Python 3.13 and no SciPy or pytest. Run the install first.
- Use `python -m pytest`, not `pytest`. The `pytest` on `PATH` is an isolated uv tool, and it cannot import the package.
- There is no `pdflatex`. Without it, `check_paper.py --compile` prints `RESULT: OK` without compiling anything, so don't report the LaTeX as compiled.

## Code style
- Nothing is auto-formatted, and `ruff format` would change most files. Don't reformat code you aren't otherwise changing; match the file you are in.
- Code must run on Python 3.10. Don't use `tomllib`, `typing.Self`, `except*`, `type` statements, or f-strings that reuse their outer quotes.
- `src/moise/` imports only the standard library, NumPy, SciPy and PyYAML, so that it runs under Pyodide. Plotting and PDF code stay in `tools/` and `docs/paper/data/irf/scripts/`. Ask before adding a dependency.
- New modules follow `src/moise/` from PR #1: a module docstring that says what the module does, `from __future__ import annotations`, type hints on public functions, dataclasses for records, imports grouped as standard library / third-party / local, and lines under about 120 characters.
- Be strict. If the input is something you don't understand, raise the module's error (`ModelError`, `SolveError`, `ExprError`, `ConvertError`) with a message that names the equation or symbol. Never guess or skip silently.
- Scripts in `tools/` run from the repo root, give their usage in the module docstring and exit with status 1 on failure.
- Tests are plain pytest functions named for what they check (`test_model_has_a_unique_stable_solution`), using `pytest.approx`, explicit tolerances and `parametrize`. The module docstring says what is compared and why the tolerances are what they are.

## Git and pull requests
- Never commit to `main`, and never merge a PR: only Daniel merges. Work on a branch. PRs go against `main`, unless they are stacked.
- Keep model changes (`model/moise.yaml`) and code changes (`src/`) in separate PRs (`CONTRIBUTING.md`). If one needs the other, stack them and say so in the description.
- Commit subjects are in the imperative and in sentence case, with no trailing period, e.g. "Add a generic solver for linear rational-expectations models". The body says what changed and why, wrapped at about 72 columns.
- PR descriptions follow #1 and #2: what is in it, how to check it (commands and the expected output), and what Daniel needs to do.
- Cite the paper by equation number and printed page, e.g. "(229), p. 114". The PDF page is the printed page + 6.

## The Bank of Israel and its paper
- Keep the "not affiliated with the Bank of Israel" wording wherever the Bank is named. Never use the Bank's logo, and never present results as a Bank of Israel forecast or position.
- Ask Daniel before adding more of the paper's own text, tables or figures to the repository, and before moving or deleting `docs/paper/`.

## ClickUp
- Work on this repo is tracked in ClickUp, which Claude sessions reach through the ClickUp connector: space **ShekelTech**, list **MOISE-DSGE-PY** (list id `1100330000114974`). Check it for open work before starting something new. The space's other lists belong to other projects. Don't add tasks to **Claude reviews**: an automation runs every task put there.
- Tags: `human-only` means only Daniel can do it; `ai-can-do` means any AI agent may pick it up. Don't do a `human-only` task, but you may prepare material for one when asked.
- Statuses: `to do`, `in progress`, `needs your review`, `blocked`, `complete`.
- The list's own rules: AI agents never set the verified or reviewed fields in `model/moise.yaml`, and never merge PRs.
- End a task you create with a `Source:` line that links the session it came from.
