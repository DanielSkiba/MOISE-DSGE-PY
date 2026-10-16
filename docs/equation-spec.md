# Equation file specification (`model/moise.yaml`)

The model is defined entirely in YAML so that it can be checked line by line against the paper without reading any solver code.

## Source

Transcribe from `docs/paper/10-log-linear-model.md`. Each equation there has a code form that
already follows the timing convention below; variable and parameter names come from
`docs/paper/data/notation_codes.csv`. The YAML `expr` should match that code form unless a
documented decision (in `notes`) changes it, e.g. to correct a known misprint.

## Conventions
- All variables are **log-deviations from steady state** (as in paper Appendix D) unless stated otherwise.
- Timing: `x` = x_t, `x(+1)` = E_t x_{t+1}, `x(-1)` = x_{t-1}.
- Each equation is written as `lhs = rhs`.
- Notation follows the paper as closely as possible. Where a symbol must be renamed (Greek letters, hats, primes), record the original in `paper_symbol`.

## Sections

```yaml
meta:
  source: "Argov et al. (2012), BoI DP 2012.06"

variables:            # endogenous variables
  - name: pi_c
    paper_symbol: "π^c_t"
    description: "CPI inflation"

shocks:               # exogenous innovations
  - name: eps_r
    paper_symbol: "ε^R_t"
    description: "Monetary policy shock"

parameters:
  - name: beta
    paper_symbol: "β"
    value: null        # filled from the paper's tables
    source: "Table X, p. Y"   # mode / calibrated value location
    kind: calibrated   # calibrated | estimated_mode | estimated_mean

equations:
  - id: D.1
    paper_eq: "(D.1)"
    page: 111
    block: households  # households | firms | wages | open_economy | policy | exogenous | ...
    expr: "lhs = rhs"
    verified: false    # set true only after a human checks it against the PDF
    verified_by: null
    notes: ""
```

## Rules
1. **Never mark `verified: true` unless a person has compared the entry to the PDF.** AI agents may draft entries but may not verify them.
2. One equation per entry. Do not merge or simplify equations, even if they are algebraically equivalent.
3. If the paper is ambiguous or appears to contain a typo, keep the paper's version, set `notes`, and open an issue.
4. Parameter values must cite their table and page.
