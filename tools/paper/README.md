# tools/paper — maintenance tools for `docs/paper/`

`docs/paper/` is the AI-readable edition of the MOISE paper. These scripts keep it consistent.

| File | What it does |
|---|---|
| `blocks.py` | Parses the math blocks (`<!-- kind: …; id: …; … -->` + `$$ … $$`) out of the Markdown files. |
| `latex2code.py` | Strict converter from the edition's LaTeX to the plain code form (`pi_IM(+1)`, explicit `*`, `E_t` dropped). Raises an error instead of guessing on anything it does not understand. |
| `check_paper.py` | Checks metadata, unique ids, that equations (1)–(331) are all present once, and that every code form in `10-log-linear-model.md` still matches its LaTeX. `--compile` also compiles every block with pdflatex; `--fix-code` rewrites stale code forms; `--write-json` regenerates `equations.json`. |

## Workflow when you correct an equation

1. Fix the LaTeX in the relevant `docs/paper/NN-*.md` file (keep it exactly as printed in the paper; record suspected paper typos as `Note:` lines instead of correcting them).
2. If the equation introduces a symbol that has no code name yet, add a row to `docs/paper/data/notation_codes.csv`.
3. Run `python tools/paper/check_paper.py --fix-code --write-json`, then `python tools/paper/check_paper.py --compile`.
4. Log the change in `docs/verification-log.md`.

Requires Python ≥ 3.10; `--compile` additionally needs `pdflatex` with `amsmath`/`amssymb`.
