# Overview

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

## About the paper (Sections 1–2)

### 1 Introduction

*Printed pp. 1–4 (PDF pp. 7–10).*

**Summary.** The introduction places MOISE among central-bank New Keynesian DSGE models, names its templates and Israel-specific changes, and previews estimation and fit.

- **Purpose and use.** MOISE is a DSGE model of Israel's small open economy, run by the Research Department at the Bank of Israel. Such models frame a central bank's discussion and analysis, help gauge the economy's present state, and support forecasts. Perhaps most valuably, they quantify alternative policies and scenarios.
- **What it builds on.** The New Keynesian approach of Smets and Wouters (2003), Woodford (2003) and Christiano et al. (2005): optimizing agents in general equilibrium, plus money as unit of account, monopolistic competition and nominal rigidities. Nominal shocks therefore have temporary real effects, and expectations become a policy channel. MOISE follows the Riksbank's RAMSES (Adolfson et al., 2007) and, most closely, the ECB's NAWM (Christoffel et al., 2008). It shares their habits, investment and export adjustment costs, and Calvo (1983) price and wage stickiness with indexation.
- **Israel-specific features.** Imports feed into exports and government consumption goods, since about 70% of goods imports are raw materials for final-goods production. Exports and imports are priced in local currency. A very persistent risk-premium process shifts the long-run real rate, which was non-stationary in the sample. Exogenous inventory investment aligns the resource constraint with the national accounts; fixed capital formation is the observed investment.
- **Estimation.** Full-information Bayesian methods (An and Schorfheide, 2007), using 24 quarterly series for 1992–2009, mostly Israeli (five G4/OECD series and the oil price are included; Appendix A). The first 12 quarters only initialize the Kalman filter (Section 4). Instead of pre-filtering, an "additive hybrid model" in the observation block absorbs trends of individual real series that balanced growth cannot explain. The Kalman filter uses all series jointly. The same device strips out yield-curve term premiums.
- **Fit (previewed).** The likelihood has curvature in most parameters, and posteriors are plausible. Most model moments match the data statistically. Unconditional in-sample forecasts match naive and BVAR models and are best for the interest rate.

### 2 The role of DSGE models in central bank policy formulation

*Printed pp. 4–5 (PDF pp. 10–11).*

**Summary.** The section sets out three ways central banks use DSGE models; these uses guided how MOISE was specified.

- **a. To provide a basis for discussion.** A macro model encodes a view of how the sectors of the economy interact and what drives them. However large, any such model only roughly approximates reality, and its builders and users know this. It still gives a shared frame of reference that eases communication within the central bank and with the public, even when not everyone agrees with it.
- **b. Nowcasting and forecasting.** Many series, notably national-accounts and labor-market data, appear only months after the period they describe. A model can estimate their current values ("nowcasting") and locate the economy in the business cycle. Combined with assumed future paths of exogenous variables, this yields forecasts of the endogenous ones. In practice, model output is blended with outside information and judgment.
- **c. To evaluate alternative policy measures and economic scenarios.** A model grounded in theory and checked against data captures the simultaneous links among sectors. It can therefore trace the consequences of different policies, or of different assumptions about exogenous variables. Under inflation targeting the central bank acts mainly through the interest rate, aiming at its inflation target alongside other goals. Because the model is micro-founded, the bank can assess how alternative rate choices change the future paths of endogenous variables in a way the authors regard as robust to the Lucas (1976) critique. Lacking a model, even the sign of some policy effects would be hard to predict. An estimated model quantifies the effects of policies and shocks and supplies confidence bands and risk assessments for its forecasts.

## The model at a glance

MOISE is built along the lines of two existing central-bank models, the ECB's NAWM and the Riksbank's RAMSES (a footnote lists comparable models for Norway, Canada, New Zealand and Iceland). Its agents are households, several kinds of firms, a government, and a central bank that pursues an inflation target by setting the nominal interest rate. Production involves monopolistically competitive intermediate-goods makers that hire labor and capital, competitive final-goods makers, importers and exporters. What follows lays out the model's behavioral relationships and the first-order and market-clearing conditions they imply, with extended discussion reserved for the non-standard elements.

### Figure 1 (from 3.2): The Structure of the Production Sector (page 13; pdf_page 19)

Block diagram (boxes and arrows; no axes, units or horizon). Arrows run from producers to buyers, from the bottom of the figure to the top. Firm types and flows, with the symbols printed in the figure:

- **Domestic Intermediate Goods Firms** (bottom left box)
  - Produce: differentiated domestic intermediate goods $H_{f,t}$ (drawn as three small boxes).
  - Inputs: none shown in the figure.
  - Output goes to: the Domestic Final Goods Firms, including the Export (stage 1) compartment (arrow into a brace that spans the whole final-goods box).
- **Foreign Intermediate Goods Firms** (bottom centre box)
  - Produce: differentiated imported intermediate goods $IM_{f^{*},t}$ (three small boxes).
  - Inputs: none shown in the figure.
  - Output goes to: the Domestic Final Goods Firms, including Export (stage 1) (arrow into the same brace).
- **Domestic Final Goods Firms** (middle box, with a separate compartment labelled **Export (stage 1)**)
  - Produce: $Q_{t}^{C}$, $Q_{t}^{I}$, $Q_{t}^{G}$ in the main part and $Q_{t}^{X}$ in the Export (stage 1) compartment.
  - Inputs: $H_{f,t}$ and $IM_{f^{*},t}$.
  - Output goes to: from the $Q_{t}^{C}, Q_{t}^{I}, Q_{t}^{G}$ part, one arrow into a brace over the three domestic final-use boxes **Consumption** $C_{t}$, **Investment** $I_{t}$, $\Delta INV_{t}$ and **Government** $G_{t}$; from the Export (stage 1) compartment, $Q_{t}^{X}$, an arrow to **Exporters' Brand Naming (Export stage 2)**.
- **Exporters' Brand Naming (Export stage 2)**
  - Produce: differentiated (branded) export goods $X_{f^{x},t}$ (three small boxes; the figure prints a lower-case $x$ on $f$).
  - Inputs: $Q_{t}^{X}$ from Export (stage 1).
  - Output goes to: **Foreign Retail Firms**.
- **Foreign Retail Firms, $X_{t}$ (Export stage 3)**
  - Produce: the homogeneous exported good $X_{t}$.
  - Inputs: the branded goods $X_{f^{x},t}$.
  - Output goes to: **Foreign Demand** $WT_{t}^{*}$.
- Other boxes (final demand, not producers in the domestic production sector):
  - **Foreign Competitors** $X_{t}^{*}$: arrow into Foreign Demand, next to the arrow from Foreign Retail Firms.
  - **Foreign Demand** $WT_{t}^{*}$: top box; receives $X_{t}$ and $X_{t}^{*}$.
  - **Consumption** $C_{t}$, **Investment** $I_{t}$, $\Delta INV_{t}$, **Government** $G_{t}$: domestic final uses supplied by $Q_{t}^{C}, Q_{t}^{I}, Q_{t}^{G}$ (the figure does not pair individual goods with individual uses).

Note: the figure prints the asterisks after the time subscript ("$WT_{t}$*", "$X_{t}$*"); they are written here as superscripts.

## Map of the paper

PDF page = printed page + 6 (the PDF has six front-matter pages). Equation numbers in this edition are the paper's.

| Section | Title | Printed page | PDF page | File here |
|---|---|---|---|---|
| 1 | Introduction | 1 | 7 | [00-overview.md](00-overview.md) |
| 2 | The role of DSGE models in central bank policy formulation | 4 | 10 | [00-overview.md](00-overview.md) |
| 3 | The model | 5 | 11 | [02-model-households.md](02-model-households.md) |
| 3.1 | Households | 6 | 12 | [02-model-households.md](02-model-households.md) |
| 3.1.1 | Preferences and the budget constraint | 6 | 12 | [02-model-households.md](02-model-households.md) |
| 3.1.2 | The consumption and saving decision | 9 | 15 | [02-model-households.md](02-model-households.md) |
| 3.1.3 | Investment and capital utilization | 9 | 15 | [02-model-households.md](02-model-households.md) |
| 3.1.4 | Labor supply and wage setting | 11 | 17 | [02-model-households.md](02-model-households.md) |
| 3.2 | Firms | 12 | 18 | [03-model-firms.md](03-model-firms.md) |
| 3.2.1 | Domestic intermediate goods firms | 13 | 19 | [03-model-firms.md](03-model-firms.md) |
| 3.2.2 | Foreign intermediate goods firms | 16 | 22 | [03-model-firms.md](03-model-firms.md) |
| 3.2.3 | Domestic final goods firms | 18 | 24 | [03-model-firms.md](03-model-firms.md) |
| 3.2.4 | Exporters | 21 | 27 | [03-model-firms.md](03-model-firms.md) |
| 3.2.5 | Foreign retail firms | 23 | 29 | [03-model-firms.md](03-model-firms.md) |
| 3.3 | The public sector | 24 | 30 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.3.1 | The government | 24 | 30 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.3.2 | The central bank | 25 | 31 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.4 | Net foreign assets and the current account | 26 | 32 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5 | Market-clearing conditions | 27 | 33 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.1 | Clearing of the labor market | 27 | 33 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.2 | Clearing of the capital market | 28 | 34 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.3 | Intermediate-goods market clearing | 28 | 34 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.4 | Clearing of the final goods markets | 30 | 36 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.5 | Aggregate resource constraints | 31 | 37 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.5.6 | The share of profits | 32 | 38 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 3.6 | The foreign economy | 32 | 38 | [04-model-public-sector-and-markets.md](04-model-public-sector-and-markets.md) |
| 4 | Estimation of the model | 34 | 40 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| 4.1 | Data | 34 | 40 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| 4.2 | Filtering the observed data | 36 | 42 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| 4.3 | Methodology | 40 | 46 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| 4.4 | Calibrated parameters, shocks and prior distributions | 41 | 47 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 4.4.1 | Calibrated parameters | 41 | 47 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 4.4.2 | Structural shocks | 45 | 51 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 4.4.3 | Prior distributions | 46 | 52 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 4.5 | Estimation results | 49 | 55 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 4.6 | Sensitivity analysis | 58 | 64 | [06-calibration-and-estimation.md](06-calibration-and-estimation.md) |
| 5 | Model evaluation | 62 | 68 | [07-evaluation.md](07-evaluation.md) |
| 5.1 | Moment goodness-of-fit tests | 62 | 68 | [07-evaluation.md](07-evaluation.md) |
| 5.2 | Forecast quality | 66 | 72 | [07-evaluation.md](07-evaluation.md) |
| 6 | Model properties | 68 | 74 | [08-model-properties.md](08-model-properties.md) |
| 6.1 | Variance decomposition | 68 | 74 | [08-model-properties.md](08-model-properties.md) |
| 6.2 | Impulse response functions | 73 | 79 | [08-model-properties.md](08-model-properties.md) |
| 7 | Concluding remarks | 84 | 90 | [07-evaluation.md](07-evaluation.md) |
| Appendix A | The data | 87 | 93 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| Appendix B | Model-consistent filtering | 91 | 97 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| B.1 | Detrending employment variables | 91 | 97 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| B.2 | Detrending aggregate quantities of goods | 92 | 98 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| B.3 | Detrending relative prices | 93 | 99 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| B.4 | Smoothing of forward interest rates | 94 | 100 | [05-data-and-filtering.md](05-data-and-filtering.md) |
| Appendix C | The steady state | 95 | 101 | [09-steady-state.md](09-steady-state.md) |
| C.1 | The non-linear steady-state model | 96 | 102 | [09-steady-state.md](09-steady-state.md) |
| C.1.1 | Households | 96 | 102 | [09-steady-state.md](09-steady-state.md) |
| C.1.2 | Domestic intermediate goods firms | 98 | 104 | [09-steady-state.md](09-steady-state.md) |
| C.1.3 | Foreign intermediate goods firms | 98 | 104 | [09-steady-state.md](09-steady-state.md) |
| C.1.4 | Domestic final goods firms | 99 | 105 | [09-steady-state.md](09-steady-state.md) |
| C.1.5 | Exporters | 100 | 106 | [09-steady-state.md](09-steady-state.md) |
| C.1.6 | Foreign retail firms | 100 | 106 | [09-steady-state.md](09-steady-state.md) |
| C.1.7 | Government | 100 | 106 | [09-steady-state.md](09-steady-state.md) |
| C.1.8 | Net foreign assets and the current account | 101 | 107 | [09-steady-state.md](09-steady-state.md) |
| C.1.9 | Market-clearing conditions | 101 | 107 | [09-steady-state.md](09-steady-state.md) |
| C.2 | The recursive steady-state solution | 103 | 109 | [09-steady-state.md](09-steady-state.md) |
| C.2.1 | Solving for prices | 104 | 110 | [09-steady-state.md](09-steady-state.md) |
| C.2.2 | Solving for input prices and the trade balance | 106 | 112 | [09-steady-state.md](09-steady-state.md) |
| C.2.3 | Solving for quantities per working hours | 107 | 113 | [09-steady-state.md](09-steady-state.md) |
| C.2.4 | Solving for hours worked (N ) | 108 | 114 | [09-steady-state.md](09-steady-state.md) |
| C.2.5 | Returning to levels | 108 | 114 | [09-steady-state.md](09-steady-state.md) |
| C.2.6 | Solving for sector-specific intermediate goods, imports and exports | 109 | 115 | [09-steady-state.md](09-steady-state.md) |
| C.2.7 | Solving for government debt | 110 | 116 | [09-steady-state.md](09-steady-state.md) |
| C.2.8 | Solving for fixed costs | 111 | 117 | [09-steady-state.md](09-steady-state.md) |
| C.2.9 | Solving for additional variables | 111 | 117 | [09-steady-state.md](09-steady-state.md) |
| Appendix D | The log-linearized model | 111 | 117 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.1 | Households'Choice of Allocations | 111 | 117 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.2 | Labor Supply and Wage Setting | 112 | 118 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.3 | Intermediate-good Firms Resource Allocation | 113 | 119 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.4 | Intermediate-good Firms Price Setting (Phillips Curves) | 113 | 119 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5 | Final-Good Firms: Technology, Inputs and Prices | 114 | 120 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5.1 | Final private consumption good | 114 | 120 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5.2 | Final investment good | 115 | 121 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5.3 | Final public consumption good | 116 | 122 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5.4 | Final exports good | 116 | 122 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.5.5 | Exports to foreign markets (monopolistic firms) | 117 | 123 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.6 | The Fiscal and Monetary Authorities | 117 | 123 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.7 | Net Foreign Assets and the Current Account | 119 | 125 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.8 | Market Clearing Conditions | 120 | 126 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.9 | The Foreign Economy: | 122 | 128 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.10 | Observation Equations | 122 | 128 | [10-log-linear-model.md](10-log-linear-model.md) |
| D.11 | AR(1) processes of the idiosyncratic trend shocks | 126 | 132 | [10-log-linear-model.md](10-log-linear-model.md) |
| Appendix E | Bayesian impulse responses | 127 | 133 | [08-model-properties.md](08-model-properties.md) |
| References |  | 135 | 141 | (Key references below) |

## Key references

Entries are taken from the reference list (printed pp. 135–138, PDF pp. 141–144). A note after each entry gives why it is listed and where the paper cites it.

**Central-bank models MOISE is based on** (Sections 1 and 3, PDF pp. 7–8 and 11)

- Christoffel, K., G. Coenen, and A. Warne (2008). The New Area-Wide Model of the Euro Area: A Micro-Founded Open-Economy Model for Forecasting and Policy Analysis. *European Central Bank, Working Paper Series 944*. Note: the ECB's NAWM, the model MOISE follows most closely; also the source of the explicit oil-price role in import prices (PDF p. 23).
- Adolfson, M., S. Laséen, J. Lindé, and M. Villani (2007). Bayesian Estimation of an Open Economy DSGE Model with Incomplete Pass-Through. *Journal of International Economics 72*(2), 481–511. Note: the Riksbank's RAMSES, the second template; also the source of the working-capital channel (PDF p. 21).

**New Keynesian foundations named in Section 1** (PDF pp. 7–8)

- Woodford, M. (2003). *Interest and Prices: Foundations of a Theory of Monetary Policy*. Princeton Univ Press. Note: NK framework.
- Christiano, L., M. Eichenbaum, and C. Evans (2005). Nominal Rigidities and the Dynamic Effects of a Shock to Monetary Policy. *Journal of Political Economy 113*(1), 1–45. Note: NK framework; also followed for the state-contingent securities in the household problem (PDF p. 14).
- Smets, F. and R. Wouters (2003). An Estimated Dynamic Stochastic General Equilibrium Model of the Euro Area. *Journal of the European Economic Association 1*(5), 1123–1175. Note: NK framework and Bayesian estimation practice (PDF p. 40); basis of the employment equation (95) (PDF p. 42).
- Calvo, G. (1983). Staggered Prices in a Utility-Maximizing Framework. *Journal of monetary Economics 12*(3), 383–398. Note: the price- and wage-setting friction used in MOISE.

**Methodology needed for replication** (estimation and filtering)

- An, S. and F. Schorfheide (2007). Bayesian Analysis of DSGE Models. *Econometric Reviews 26*(2-4), 113–172. Note: the full-information Bayesian estimation approach (PDF pp. 9, 46).
- Schorfheide, F. (2011). Estimation and Evaluation of DSGE Models: Progress and Challenges. *Federal Reserve Bank of Philadelphia, Research Department Working Paper 11-7*. Note: "additive hybrid models" behind the model-consistent filtering of trends (PDF p. 43).
- Canova, F. (2009). Bridging Cyclical DSGE Models and the Raw Data. Manuscript, Centre de Recerca en Economia Internacional. Note: same purpose as Schorfheide (2011) (PDF p. 43).
- Juillard, M. (1996). Dynare: A Program for the Resolution and Simulation of Dynamic Models with Forward Variables Through the Use of a Relaxation Algorithm. *CEPREMAP Working Papers* (9602). Note: Dynare, the software used for estimation (PDF p. 46).
- Adjemian, S., H. Bastani, M. Juillard, F. Mihoubi, G. Perendia, M. Ratto, and S. Villemot (2011). Dynare: Reference Manual, Version 4. *Dynare Working Papers*. Note: Dynare 4 manual (PDF p. 46).
- Brooks, S. and A. Gelman (1998). General Methods for Monitoring Convergence of Iterative Simulations. *Journal of Computational and Graphical Statistics 7*(4), 434–455. Note: convergence check for the Metropolis-Hastings chains (PDF p. 55).

**Specific model components that Section 3 says follow other work** (cited after PDF p. 12)

- Adolfson, M., S. Laséen, J. Lindé, and M. Villani (2008). Evaluating an Estimated New Keynesian Small Open Economy Model. *Journal of Economic Dynamics and Control 32*(8), 2690–2721. Note: the external risk premium depends on expected depreciation (PDF p. 14).
- Schmitt-Grohe, S. and M. Uribe (2003). Closing Small Open Economy Models. *Journal of International Economics 61*(1), 163–185. Note: a premium that depends on net foreign assets, which gives a stable steady state (footnote 8, PDF p. 14).
- Greenwood, J., Z. Hercowitz, and P. Krusell (1997). Long-Run Implications of Investment-Specific Technological Change. *The American Economic Review 87*(3), 342–362. Note: investment-specific technology shock (PDF p. 16).
- Dixit, A. and J. Stiglitz (1977). Monopolistic Competition and Optimum Product Diversity. *The American Economic Review 67*(3), 297–308. Note: cited for the CES composite of household labor inputs (PDF p. 20) and for the foreign retailers' demand for differentiated exports, (53) (PDF p. 29).
- Taylor, J. (1993). Discretion versus Policy Rules in Practice. In *Carnegie-Rochester conference series on public policy*, Volume 39, pp. 195–214. Elsevier. Note: the domestic and foreign policy rules generalize a Taylor-type rule (PDF pp. 31, 39).
- Argov, E. and D. Elkayam (2010). An Estimated New Keynesian Model for Israel. *Israel Economic Review 7*(2), 1–40. Note: its findings motivate the policy rule's response to depreciation and to past and expected inflation (PDF p. 32).

Not listed: footnote 3 (PDF p. 11) cites similar central-bank models for Norway, Canada, New Zealand and Iceland, but the paper does not say MOISE is based on them. Kydland and Prescott (1982) and Lucas (1976) appear only as background. Section 4 sources used only for calibration or priors (e.g. Ribon 2004, Binyamini 2007, Friedman and Lavi 2007) are also left out.
