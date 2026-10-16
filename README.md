# MOISE-DSGE-PY

An independent, open-source Python replication of **MOISE** (MOdel for the ISraeli Economy), the medium-scale New Keynesian DSGE model developed by the Bank of Israel Research Department.

> **Disclaimer.** This project is not affiliated with, endorsed by, or reviewed by the Bank of Israel. It is an independent reconstruction based solely on the publicly available discussion paper cited below. Results may differ from the Bank's internal model, which has been updated since 2012. Nothing here is a forecast or statement of the Bank of Israel.

## Original paper

Argov, E., Barnea, E., Binyamini, A., Borenstein, E., Elkayam, D., & Rozenshtrom, I. (2012).
*MOISE: A DSGE Model for the Israeli Economy.* Bank of Israel Research Department, Discussion Paper No. 2012.06.
[PDF](https://boi.org.il/media/ybvpydng/dp12065e.pdf) · [Abstract page](https://boi.org.il/en/economic-roles/research-and-publications/discussion-paper-series-research-department/moise-a-dsge-model-for-the-israeli-economy)

```bibtex
@techreport{argov2012moise,
  author      = {Argov, Eyal and Barnea, Emanuel and Binyamini, Alon and Borenstein, Eliezer and Elkayam, David and Rozenshtrom, Irit},
  title       = {{MOISE}: A {DSGE} Model for the {I}sraeli Economy},
  institution = {Bank of Israel, Research Department},
  type        = {Discussion Paper},
  number      = {2012.06},
  year        = {2012},
  url         = {https://boi.org.il/media/ybvpydng/dp12065e.pdf}
}
```

If you use this code, please cite both the original paper and this repository (see `CITATION.cff`).

## Goals

1. **Faithful replication** of the log-linearized model (paper Appendix D) and steady state (Appendix C), calibrated at the paper's reported parameter estimates.
2. **Verification** against the paper's impulse responses and variance decompositions. A result is not trusted until it matches.
3. **Interactive playground** for the web: choose a shock, change policy-rule coefficients, compare paths.
4. **Later:** data pipeline from Bank of Israel / CBS series and Bayesian re-estimation on recent data.

See [`docs/ROADMAP.md`](docs/ROADMAP.md) for the phased plan.

## Design principles

- **Equations are data, not code.** The model lives in `model/moise.yaml`, with each equation tagged by its equation number and page in the paper. The solver is generic and knows nothing about Israel.
- **Pure Python, no Dynare dependency.** Linear rational-expectations solution via QZ decomposition (NumPy / SciPy), small enough to also run in the browser via Pyodide.
- **Every equation is human-verified** against the PDF before it is marked `verified: true`. See [`docs/equation-spec.md`](docs/equation-spec.md).

## The paper, in a form agents can read

[`docs/paper/`](docs/paper/README.md) is an AI-readable edition of the paper: all 331 numbered
equations (plus every unnumbered display and inline definition) in clean LaTeX with the paper's
numbering and page references, a plain code form for the log-linearized equations (all but one that the paper prints with "…"), a notation
table with code names, every table as CSV, and the impulse-response charts digitized as data.
Each section was transcribed from page images and checked by an independent second pass.
Explanations are paraphrased; it is not a substitute for the paper.

## Repository layout

```
docs/paper/     AI-readable edition of the paper (equations, notation, tables, IRF data)
model/          Model definition (equations, parameters, shocks) in YAML
src/moise/      Python package: parser, solver, IRFs, simulation
tests/          Tests, including replication checks against the paper
tools/paper/    Checks for docs/paper (ids, completeness, LaTeX, code-form sync)
docs/           Roadmap, equation-file spec, verification log
web/            Browser playground (Phase 2)
```

## Status

🚧 **Phase 0 done** (repository setup) and the **agent edition of the paper** is in `docs/paper/`.
Next: Phase 1, transcribing the log-linearized model into `model/moise.yaml` and writing the solver.

## Contributing

Contributions are welcome, especially help verifying transcribed equations against the paper. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Code is released under the [MIT License](LICENSE). The original paper and its content remain the property of the Bank of Israel and its authors; this repository does not redistribute the paper.
