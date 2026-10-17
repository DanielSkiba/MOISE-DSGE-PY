# Model file specification (`model/moise.yaml`)

The model is defined entirely in YAML so that it can be checked line by line against the paper
without reading any solver code. The solver (`src/moise/`) reads any file in this format; nothing in
it is specific to MOISE.

## Source

Transcribe from `docs/paper/10-log-linear-model.md`. Each Appendix D equation there has a code form
that already follows the timing convention below, with variable and parameter names from
`docs/paper/data/notation_codes.csv`. The YAML keeps that code form verbatim in `printed`. The
solver uses `expr`, which may differ from `printed` only where a documented decision applies.

## Conventions

- Hatted variables are **log deviations from the steady state** (as in Appendix D). Shares and tax
  rates (`s_X`, `s_IM`, `s_TB`, `CA_over_Y`, `dinv`, `tau_*`) are level deviations.
- Timing: `x` = x_t, `x(+1)` = E_t x_{t+1}, `x(-1)` = x_{t-1}; any integer lead or lag is allowed
  (the solver adds auxiliary variables for leads above 1 and lags below −1).
- Each equation is `lhs = rhs`, linear in the variables (checked numerically). Parameters may enter
  nonlinearly. Constants are allowed (they define the deterministic steady state of the observables).
- Operators `+ - * / ^` and parentheses; functions `exp`, `log`, `ln`, `sqrt`. `^` is a power.

## Sections

```yaml
meta: {...}                 # free-form description

decisions:                  # every departure from (or interpretation of) the printed paper
  - id: D13
    title: '(217): (1-γ_S) on the expected inflation differential'
    status: proposed        # proposed (drafted, waiting for review) | accepted | rejected  - set by a person
    applies_to: ['(217)']
    printed: 'what the paper prints'
    adopted: 'what the model uses'
    alternatives: [printed] # choices that can be selected instead of the adopted one when loading
    rationale: 'why'
    evidence: 'test results, if any'
    reviewed_by: null

variables:                  # endogenous variables
  - name: k
    paper_symbol: '\hat{k}'
    description: '...'
    block: households
    predetermined: true     # beginning-of-period stock written as k(+1) = f(k, ...) in the paper

shocks:                     # i.i.d. innovations
  - name: eta_R
    paper_symbol: '\eta^{R}'
    std: 0.002              # posterior mode (number or expression)
    posterior_mean: 0.002   # optional; used when loading with param_set="posterior_mean"
    prior: {dist: inv_gamma, mean: 0.01, std: Inf}
    source: 'Table 3'
    page: 51

parameters:                 # evaluated in order; values may be numbers or expressions in earlier names
  - name: kappa
    paper_symbol: '\kappa'
    kind: estimated         # calibrated | fixed | estimated | derived | assumed
    value: 0.616            # posterior mode for estimated parameters
    posterior_mean: 0.706
    prior: {dist: beta, mean: 0.70, std: 0.15}
    source: 'Table 2'
    page: 50
  - name: gamma_u_1
    kind: derived
    value: '(g_z_ss/beta - (1 - delta + tau_K_ss*delta))*(1 - tau_K_ss)^(-1)'
    printed: '(beta/g_z_ss - ...)'   # the paper's version, used when the decision is set to 'printed'
    decision: D32

steady_state:               # ordered assignments after the parameters (Appendix C.2)
  - name: R_ss
    expr: 'g_z_ss*pi_ss/beta'
    paper_eq: '(168)'
    page: 106

aliases:                    # one name standing for another (two printed spellings of one variable)
  - {name: pibar_nohat, target: pibar, decision: D01}

exogenous_zero:             # names fixed at zero (variables that never move in this model)
  - {name: ztilde, decision: D23}

equations:
  - id: '217'
    paper_eq: '(217)'
    page: 112
    section: 'D.1'          # 'added' for equations not printed in Appendix D
    block: households       # used to select or exclude blocks, e.g. blocks_excluded=["measurement"]
    title: '...'
    printed: '...'          # verbatim code form from docs/paper (null if not printed or printed with "...")
    expr: '...'             # what the solver uses
    decision: D13           # required whenever expr differs from printed
    alternatives:           # optional: expressions for decision choices other than adopted/printed
      main_text: '...'
    see: [D10]              # optional: related decisions that do not change this entry
    notes: '...'
    verified: false         # set true only by a person who compared the entry with the PDF
    verified_by: null

reporting: {...}            # how the paper reports results (figure panels, Table 7); not part of the model
```

## Loading with decisions switched

```python
import moise
m = moise.load()                                   # adopted choices, posterior-mode parameters
m = moise.load(param_set="posterior_mean")         # use each entry's posterior_mean where given
m = moise.load(decisions={"D13": "printed"})       # the paper's printed (217)
m = moise.load(blocks_excluded=["measurement"])    # structural model only
sol = moise.solve(m.linear_system())
```

For an item tied to a decision, choice `adopted` uses `expr` (or `value`), `printed` uses `printed`,
and any other choice uses `alternatives[choice]` (falling back to `expr` when the item does not list
that choice, so one decision can switch several items). Aliases and fixed-zero names tied to a
decision are switched off when that decision is set to `printed`.

## Rules

1. **Never mark `verified: true` unless a person has compared the entry with the PDF.** AI agents may
   draft entries but may not verify them, and may not change a decision's `status`.
2. One equation per entry. Do not merge or simplify equations, even if they are algebraically
   equivalent.
3. Keep the paper's version in `printed`. Every difference between `expr` and `printed` must name a
   decision, and every decision must say what is printed, what is adopted and why
   (`tests/test_model.py` checks this).
4. Parameter values cite their table or equation and page. A value the paper does not give is
   `kind: assumed`, tied to a decision, with a `TODO` in `notes`.
