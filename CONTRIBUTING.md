# Contributing

Thanks for helping. The most valuable contribution right now is **verifying transcribed equations** against the paper.

## Workflow
1. Open an issue describing what you plan to change.
2. Work on a branch and open a pull request against `main`.
3. Keep model changes (`model/moise.yaml`) and code changes (`src/`) in separate pull requests.
4. `pytest` must pass.

## Verifying the paper edition (`docs/paper/`)
The edition was checked by machine. Human checks are very welcome: pick an equation, compare it with
the PDF at the printed page given in its metadata line, and record the result in
`docs/verification-log.md`. If you find a transcription error, fix the LaTeX and run
`python tools/paper/check_paper.py --fix-code --write-json`. Misprints in the paper itself are kept
as printed and recorded as `Note:` lines.

## Verifying equations
- Open the [paper PDF](https://boi.org.il/media/ybvpydng/dp12065e.pdf) at the page listed in the entry.
- Compare symbol by symbol, including timing and signs.
- If it matches, set `verified: true` and `verified_by: <your GitHub handle>`, and add a row to `docs/verification-log.md`.
- If not, fix it or open an issue.

## Ground rules
- Do not commit the paper PDF or copy large passages from it. Link and cite instead.
- Do not describe outputs as Bank of Israel forecasts or positions.
