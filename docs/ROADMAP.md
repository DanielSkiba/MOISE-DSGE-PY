# Roadmap

## Phase 0 — Repository setup ✅
License, citation, project structure, CI, contributor and agent guidelines.

## Phase 1 — Core model
1. Transcribe the log-linearized equations (paper Appendix D) into `model/moise.yaml`, one equation per entry, tagged with equation number and page.
2. Transcribe parameter values (calibrated + posterior estimates from Section 4) and shock definitions.
3. Human-verify every equation against the PDF; record it in `docs/verification-log.md`.
4. Write the generic pieces in `src/moise/`: YAML parser → symbolic system → matrices; QZ-based linear RE solver with Blanchard–Kahn checks; IRF and simulation utilities.
5. **Replication tests:** digitize key IRFs from the paper (Section 6) and assert that our responses match in sign, peak timing and approximate magnitude.

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
