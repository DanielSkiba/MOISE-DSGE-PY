# Roadmap

## Phase 0 — Repository setup ✅
License, citation, project structure, CI, contributor and agent guidelines.

## Phase 0.5 — Agent edition of the paper ✅
`docs/paper/`: every equation in LaTeX with the paper's numbering and pages, code forms for
Appendix D, notation with code names, Tables 1–7 as CSV, digitized impulse responses (Figures 6–18).
Transcribed from page images and checked by an independent second pass (machine-verified only).

## Phase 1 — Core model
1. Transcribe the log-linearized equations (paper Appendix D) into `model/moise.yaml`, one equation per entry, tagged with equation number and page. Start from the code forms in `docs/paper/10-log-linear-model.md` and decide, with a `notes` entry, how to treat each known misprint listed in `docs/paper/README.md`.
2. Transcribe parameter values (calibrated + posterior estimates from Section 4) and shock definitions.
3. Human-verify every equation against the PDF; record it in `docs/verification-log.md`.
4. Write the generic pieces in `src/moise/`: YAML parser → symbolic system → matrices; QZ-based linear RE solver with Blanchard–Kahn checks; IRF and simulation utilities.
5. **Replication tests:** compare our impulse responses with the digitized ones in `docs/paper/data/irf/` (sign, peak timing, magnitude; note the paper plots posterior means over parameter draws, not the posterior mode) and the variance decomposition with `docs/paper/data/table7_variance_decomposition.csv`.

**Definition of done:** model solves uniquely, all equations verified, IRFs match the paper's figures.

## Phase 2 — Web playground
- Run the solver in the browser via Pyodide (no server cost), or a small API endpoint as fallback.
- Controls: shock selection and size, policy-rule coefficients, rule swap (MOISE rule / Taylor 1993 / custom).
- Side-by-side comparison of paths; export to CSV.
- Embed on shekeltech.co.il.

## Phase 3 — Data and estimation
- Automated pull of the observables from Bank of Israel and CBS series.
- Bayesian re-estimation (e.g. PyMC or an MCMC sampler) on data extended past 2009.
- Compare re-estimated parameters to the 2012 posterior.
