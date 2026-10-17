# Verification log

Record each human check of `model/moise.yaml` against the paper.

| Date | Equation ids | Checked by | Result / notes |
|------|--------------|------------|----------------|

No equation has been human-verified yet.

## How to verify an equation

1. Open the PDF at the page in the entry's `page` (PDF page = page + 6).
2. Compare the printed equation with `printed` in `model/moise.yaml`, symbol by symbol (code names:
   `docs/paper/data/notation_codes.csv`; timing: `x(+1)` = E_t x_{t+1}).
3. If the entry has a `decision`, read it under `decisions` and check that `expr` makes exactly that
   change.
4. Set `verified: true` and `verified_by: <your name>` on the entry, and add a row above.

Decisions are reviewed the same way: set `status: accepted` or `rejected` and fill `reviewed_by`.

## Automated checks (not a substitute for the above)

| Date | What | Result |
|------|------|--------|
| 2026-10-17 | `tests/test_model.py`: every Appendix D equation present, `printed` equal to `docs/paper`, every change tied to a decision, every Table 1–4 value matched by symbol | pass |
| 2026-10-17 | `tests/test_replication.py`: Figures 6–18 and Table 7 at the posterior mean | pass |
