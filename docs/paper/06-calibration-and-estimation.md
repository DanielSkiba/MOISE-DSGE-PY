# Calibration, shocks, priors and estimation results

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

4.4–4.6: calibrated parameters (Table 1), structural shocks, priors and posteriors (Tables 2–4), sensitivity to the interest-rate rule (Table 5). Every table is also a CSV in `data/`.

<!-- Chunk T06: 4.4 Calibrated parameters, shocks and prior distributions (4.4.1-4.4.3); 4.5 Estimation results; 4.6 Sensitivity analysis. PDF pages 47-67 (printed 41-61). Starts at the 4.4 heading (PDF p.47, below the Bayes-factor display of 4.3); stops before "5 Model evaluation" (PDF p.68). -->

*Printed pp. 41–61 (PDF pp. 47–67).* Machine-readable tables: `data/table1_calibrated.csv`, `table2_structural.csv`, `table3_observation_and_shocks.csv`, `table4_world.csv`, `table5_sensitivity.csv`, `shocks.csv`. All numbers are kept as printed text. In the CSVs, `row_type` = `group_label` marks the italic group-heading rows of Tables 2–5 (kept as their own rows); `data` marks parameter rows; `summary` marks the marginal-likelihood row of Table 5.

## 4.4 Calibrated parameters, shocks and prior distributions

**Summary.** Two kinds of parameters are distinguished. Those that pin down the steady state are calibrated so that the steady state reproduces assumed long-run great ratios (GDP shares), production input weights, or (imbalanced) growth rates. Those that affect only the dynamics are, in general, estimated. Subsection 4.4.1 covers calibration, 4.4.2 lists the structural shocks used in estimation, and 4.4.3 explains how the priors of the estimated parameters were chosen.

### 4.4.1 Calibrated parameters

**Summary.** Table 1 reports the calibrated values. They are chosen so that steady-state ratios match long-horizon data averages or the values the economy is expected to converge to.

- **Great ratios (steady state):** private consumption 55% of GDP, fixed investment 21%, inventory investment ($\Delta inv$) 1%, government consumption ($s_{G}$) 26%, exports 39%, imports 42%. Foreign transfers to GDP ($s_{FTR}$) are set at 3% to finance the steady-state trade deficit.
- **Inflation objective ($\bar{\Pi}$):** 2% per year, the middle of the post-disinflation target range. Table 1 lists the quarterly gross value 1.005.
- **Labor-productivity growth ($g_{z}$):** 1.0% per year, roughly the sample average. Table 1 lists the quarterly gross value 1.0025.
- **Capital weight ($\alpha$):** chosen so that the wage bill is 60% of GDP. Footnote 22 notes that $(1-\alpha)=0.67$ nonetheless, because the cost of working capital is not counted in the wage bill and because of the adjustment to market prices.
- **Depreciation ($\delta$):** 2% per quarter, roughly the long-run average gap between gross and net returns on capital.
- **Discount factor ($\beta$):** set to deliver a 2.9% steady-state real interest rate.
- **Common practice in the literature:**
  - The inverse labor-supply elasticity ($\zeta$) is 2.0.
  - Steady-state markups are 30% for wages, domestic prices and import prices ($\varphi^{W}$, $\varphi^{H}$, $\varphi^{*}$ = 1.3). The export markup ($\varphi^{X}$) is a smaller 10%, because exporters' input price ($P_{t}^{DX}$) already includes the domestic and import markups.
- **Elasticities of substitution (domestic vs. imported intermediates):**
  - Consumption, investment and exports ($\mu^{C}$, $\mu^{I}$, $\mu^{X}$): 1.1. This is below common literature values (footnote 23: a 1.5 prior in Christoffel et al. 2008; a 5.0 calibration in Adolfson et al. 2007) but above the 0.4 estimate for Israel (Friedman and Lavi 2007).
  - Government ($\mu^{G}$): 0.2, because government spending is mostly public-sector wages, which cannot be substituted.
  - Foreign elasticity across import origins ($\mu^{*}$): 1.5, a common value.
- **Home-bias parameters ($\nu^{C}$, $\nu^{I}$, $\nu^{G}$, $\nu^{X}$):** set to give steady-state import intensities of 31% (consumption), 42% (investment), 5% (government) and 32% (exports). Footnote 24 stresses the large import share in exports and notes that several reference models treat exports as pure value added.
- **Taxes, set to finance steady-state government consumption:**
  - Consumption tax $\tau^{C}$ = 16%, levied on 78% of the basket ($w_{\tau^{C}}$). Footnote 25: housing services and fresh fruit and vegetables, 22% of the basket, carry no VAT.
  - Labor-income tax $\tau^{N}$ = 28%.
  - Household payroll tax $\tau^{W_{h}}$ = 9% and firm payroll tax $\tau^{W_{f}}$ = 7%.
  - Capital-income tax $\tau^{K}$ = 50%, far above actual profit or capital-gains rates, to fine-tune the steady-state investment/GDP ratio.
  - Government transfers to GDP ($s_{TR}$) are set to balance the steady-state budget, which does not affect the linearized model.
- **Export demand:** the export competitors' relative price ($p_{X}^{C}$) and relative foreign technology ($\tilde{z}$) are normalized to 1.0. Israel's steady-state weight in world trade ($\nu^{*}$) is 0.5%. None of the three affects the linearized model.
- **Working capital:** the weight of wage-bill loans ($\nu^{F}$) is 0.2, so that the working-capital channel operates.
- Values that appear only in the text (not in Table 1) are collected in `data/calibration_in_text.csv`.
- **Dynamic parameters fixed at zero (inline block 97.i3):** wages are indexed to steady-state rather than actual productivity growth, and final-goods production has no import-intensity adjustment costs. The utilization cost $\gamma_{u,2}$ is set to 10,000, so capital utilization does not vary.
- **Long-run growth rates (non-structural, annual):**
  - Per-capita hours: 0.7%. With productivity growth this gives 1.7% per-capita GDP growth; both are roughly sample averages.
  - Foreign GDP $g_{\Delta Y^{*}}$ 2.2%, world trade $g_{\Delta WT^{*}}$ 5.3%, per-capita consumption $g_{\Delta C}$ 1.7%, investment $g_{\Delta I}$ 1.7%, exports $g_{\Delta X}$ 4.9%, imports $g_{\Delta IM}$ 2.9%. These rest on sample averages plus a judgment that the sample's excess consumption and investment growth is transitory.
  - Implied per-capita government consumption growth $g_{\Delta G}$: −1% per year over the sample (printed "(-1%)").

<!-- kind: inline; id: 97.i2; section: 4.4.1; page: 42; pdf_page: 48 -->
**(97.i2) Labor share implied by the capital weight (footnote 22)**

$$
\left(1-\alpha\right) = 0.67
$$

Meaning: Even with a 60% wage-bill share, one minus the capital weight equals 0.67, owing to unmeasured working-capital cost and the market-price adjustment.

<!-- kind: inline; id: 97.i3; section: 4.4.1; page: 43; pdf_page: 49 -->
**(97.i3) Dynamic parameters fixed at zero: wage indexation to actual productivity growth, final-goods import-intensity adjustment costs**

$$
\chi_{W,g_{z}} = \gamma_{IM^{C}} = \gamma_{IM^{I}} = \gamma_{IM^{G}} = \gamma_{IM^{X}} = 0
$$

Meaning: Wage indexation to actual productivity growth and the import-intensity adjustment costs of the four final-goods sectors are all switched off.

<!-- kind: inline; id: 97.i4; section: 4.4.1; page: 43; pdf_page: 49 -->
**(97.i4) Utilization-cost parameter and its calibrated value (printed in words: "setting the cost of variation ($\gamma_{u,2}$) to $10,000$")**

$$
\gamma_{u,2}
$$

Meaning: The capital-utilization cost parameter, set to 10,000 (printed with a thousands comma) so that capital utilization effectively cannot vary.

#### Table 1: Calibrated Parameters (printed p. 44, pdf_page 50)

The table is printed as two side-by-side panels (each with Parameter, symbol and Value columns). The CSV keeps one record per entry, with `side` = left/right and `printed_row` = the line within its panel. The left panel has 17 lines; the right has 16 (line 17 is blank).

| Parameter | Symbol | Value | Parameter | Symbol | Value |
|---|---|---|---|---|---|
| Discount factor | $\beta$ | 0.995 | Wage markup | $\varphi^{W}$ | 1.3 |
| Inverse of labor EoS | $\zeta$ | 2.0 | Dom. price markup | $\varphi^{H}$ | 1.3 |
| Capital share in prod. | $\alpha$ | 0.33 | Imp. price markup | $\varphi^{*}$ | 1.3 |
| LR productivity growth | $g_{z}$ | 1.0025 | Exp. price markup | $\varphi^{X}$ | 1.1 |
| Depreciation rate | $\delta$ | 0.02 | Home bias - C | $\nu^{C}$ | 0.65 |
| EoS in consumption | $\mu^{C}$ | 1.1 | Home bias - I | $\nu^{I}$ | 0.60 |
| EoS in investment | $\mu^{I}$ | 1.1 | Home bias - G | $\nu^{G}$ | 0.95 |
| EoS in government | $\mu^{G}$ | 0.2 | Home bias - X | $\nu^{X}$ | 0.68 |
| EoS in exports | $\mu^{X}$ | 1.1 | Gov. to GDP | $s_{G}$ | 0.26 |
| Foreign EoS | $\mu^{*}$ | 1.5 | Consumption tax | $\tau^{C}$ | 0.16 |
| X's competitors price | $p_{X}^{C}$ | 1.0 | Capital tax | $\tau^{K}$ | 0.50 |
| Relative technology | $\tilde{z}$ | 1.0 | Labor income tax | $\tau^{N}$ | 0.28 |
| X's weight in $IM^{*}$ | $\nu^{*}$ | 0.005 | Payroll tax - $h$ | $\tau^{W_{h}}$ | 0.09 |
| Working capital weight | $\nu^{F}$ | 0.2 | Payroll tax - $f$ | $\tau^{W_{f}}$ | 0.07 |
| Foreign transfers to GDP | $s_{FTR}$ | 0.03 | Gov. transfers to GDP | $s_{TR}$ | 0.15 |
| LR inflation rate | $\bar{\Pi}$ | 1.005 | $\Delta$ Inventories in GDP | $\Delta inv$ | 0.01 |
| Share of taxed goods | $w_{\tau^{C}}$ | 0.78 | | | |

Notes on Table 1:
- $g_{z}$ = 1.0025 and $\bar{\Pi}$ = 1.005 are quarterly gross rates (≈1.0% and 2% per year in the text).
- $\nu^{*}$ = 0.005 is the 0.5% weight of Israel's exports in world trade described in the text.
- The text does not give a numerical $s_{TR}$; the table's 0.15 is the value chosen to balance the budget.

### 4.4.2 Structural shocks

**Summary.** The estimation uses 24 observed series. It involves 25 structural shocks, plus the 14 observation-equation shocks of Appendix B. All structural shocks are AR(1) (footnote 26 refers to footnote 4: in general, log-AR(1)), except the interest-rate (Taylor-rule) shock, which is i.i.d. For each shock the paper lists, in parentheses, the shock symbol, its AR coefficient and its i.i.d. innovation. Four entries list only an innovation: the interest rate, the inflation target, the VAT rate and the world LR rate.

Several shocks are excluded or restricted:
- The labor-supply shock $\varepsilon_{t}^{N}$ is dropped because it is observationally equivalent to the wage-markup shock $\varphi_{t}^{W}$.
- The home-bias variables of all final-good sectors ($\nu_{t}^{C}$, $\nu_{t}^{G}$, $\nu_{t}^{I}$, $\nu_{t}^{X}$) share one innovation $\eta_{t}^{\nu}$ and one AR coefficient $\rho_{\nu}$. This cuts the number of under-identified free parameters, and $\eta_{t}^{\nu}$ acts as a general negative import-demand shock.
- The alternative import-demand shock $\varepsilon_{t}^{IM}$ is therefore not used. It would move final-goods prices directly through the import-intensity adjustment-cost term, which the authors find hard to interpret. Footnote 27: unlike adjustment costs, the effect of $\nu_{t}$ drops out of the log-linearized final-goods price equations (e.g. (45)) when domestic and imported intermediate prices are equal in steady state.
- The export competitors' relative foreign price $p_{X,t}^{c,*}$ is held constant (inline block 97.i5).
- Neither variation in competitors' relative export prices nor the export-demand shock $\varepsilon_{t}^{X}$ is used: in the linearized model (fn. 28) both are observationally equivalent to the time-varying export share $\nu_{t}^{*}$. Footnote 29 adds that competitors' prices are not used because the data cannot separate them from foreign prices in general.
- Owing to data limitations, the social-security tax rates ($\tau_{t}^{W_{h}}$ and $\tau^{W_{f}}$), the capital-income tax ($\tau_{t}^{K}$) and the dividend tax ($\tau_{t}^{D}$) are held constant.
- Estimation with the direct income-tax rate $\tau_{t}^{N}$ gave unsatisfactory results, probably because of its strong downward trend over the sample.

<!-- kind: inline; id: 97.i5; section: 4.4.2; page: 46; pdf_page: 52 -->
**(97.i5) Relative foreign price of export competitors (assumed not to vary)**

$$
p_{X,t}^{c,*} = P_{X,t}^{c,*}/P_{t}^{*}
$$

Meaning: The competitors' export price relative to the foreign price level; the estimation assumes it stays constant.

Note: Section 3.6 (PDF p.40, outside this chunk) prints the same assumption as $p_{X,t}^{c,*} \equiv P_{X,t}^{c,*}/P_{Y,t}^{*} = 1$, with $P_{Y,t}^{*}$ in the denominator. Here the denominator is printed $P_{t}^{*}$ and Table 1 writes $p_{X}^{C}$ (capital C).

#### Structural shocks listed in 4.4.2 (printed p. 45, pdf_page 51)

The order follows the printed two-column list: the left column top to bottom, then the right column. Symbols are as printed in the list. Where the tables label the same item differently, the CSV column `enters_or_remarks` records it. "—" means nothing is printed in the list.

| # | Shock | Shock symbol | AR coefficient | Innovation | Specification / remarks as stated |
|---|---|---|---|---|---|
| 1 | Transitory technology | $\varepsilon_{t}$ | $\rho$ | $\eta_{t}$ | AR(1) |
| 2 | Permanent labor-productivity | $g_{z,t}$ | $\rho_{g_{z}}$ | $\eta_{t}^{g_{z}}$ | AR(1) |
| 3 | Symmetric premium | $\varepsilon_{t}^{RP}$ | $\rho_{RP}$ | $\eta_{t}^{RP}$ | AR(1) |
| 4 | External premium | $\varepsilon_{t}^{RP^{*}}$ | $\rho_{RP^{*}}$ | $\eta_{t}^{RP^{*}}$ | AR(1) |
| 5 | Domestic premium | $\varepsilon_{t}^{DRP}$ | $\rho_{DRP}$ | $\eta_{t}^{DRP}$ | AR(1); no $\rho_{DRP}$ estimate is reported in Tables 2–4 |
| 6 | Consumption demand | $\varepsilon_{t}^{C}$ | $\rho_{C}$ | $\eta_{t}^{C}$ | AR(1) |
| 7 | Investment technology | $\varepsilon_{t}^{I}$ | $\rho_{I}$ | $\eta_{t}^{I}$ | AR(1) |
| 8 | Inventory investment | $\Delta inv_{t}$ | $\rho_{\Delta inv}$ | $\eta_{t}^{\Delta inv}$ | AR(1); the tables print $\rho_{\Delta INV}$, $\eta^{\Delta INV}$ |
| 9 | Government consumption | $\varepsilon_{t}^{G}$ | $\rho_{G}$ | $\eta_{t}^{G}$ | AR(1) |
| 10 | Time-varying export share | $\nu_{t}^{*}$ | $\rho_{\nu^{*}}$ | $\eta_{t}^{\nu^{*}}$ | AR(1); replaces export-demand shock $\varepsilon_{t}^{X}$ |
| 11 | Time-varying home bias | $\nu_{t}$ | $\rho_{\nu}$ | $\eta_{t}^{\nu}$ | AR(1); one process common to $\nu_{t}^{C}$, $\nu_{t}^{G}$, $\nu_{t}^{I}$, $\nu_{t}^{X}$ |
| 12 | Domestic price markup | $\varphi_{t}^{H}$ | $\rho_{H}$ | $\eta_{t}^{H}$ | AR(1); Table 2 labels the AR coefficient $\rho_{\varphi^{H}}$ |
| 13 | Import price markup | $\varphi_{t}^{*}$ | $\rho^{*}$ | $\eta_{t}^{*}$ | AR(1); Table 2 labels the AR coefficient $\rho_{\varphi^{*}}$ |
| 14 | Wage markup | $\varphi_{t}^{W}$ | $\rho_{W}$ | $\eta_{t}^{W}$ | AR(1); stands in for labor supply shock $\varepsilon_{t}^{N}$; Table 2: $\rho_{\varphi^{W}}$ |
| 15 | Export price markup | $\varphi_{t}^{X}$ | $\rho_{X}$ | $\eta_{t}^{X}$ | AR(1); Table 2 labels the AR coefficient $\rho_{\varphi^{X}}$ |
| 16 | Foreign transfers | $s_{FTR,t}$ | $\rho_{FTR}$ | $\eta_{t}^{FTR}$ | AR(1) |
| 17 | Interest rate | — | — | $\eta_{t}^{R}$ | i.i.d. (the stated exception) |
| 18 | Inflation target | — | — | $\eta_{t}^{\bar{\Pi}}$ | only the innovation is listed |
| 19 | VAT rate | — | — | $\eta_{t}^{\tau^{C}}$ | only the innovation is listed |
| 20 | World demand | $\varepsilon_{t}^{Y^{*}}$ | $\rho_{Y^{*}}$ | $\eta_{t}^{Y^{*}}$ | AR(1) |
| 21 | World cost push | $\varepsilon_{t}^{\Pi^{*}}$ | $\rho_{\Pi^{*}}$ | $\eta_{t}^{\Pi^{*}}$ | AR(1) |
| 22 | World interest rate | $\varepsilon_{t}^{R^{*}}$ | $\rho_{R^{*}}$ | $\eta_{t}^{R^{*}}$ | AR(1) |
| 23 | World trade | $\varepsilon_{t}^{WT^{*}}$ | $\rho_{WT^{*}}$ | $\eta_{t}^{WT^{*}}$ | AR(1); no $\rho_{WT^{*}}$ estimate is reported in Tables 2–4 |
| 24 | Oil price | $\varepsilon_{t}^{OIL}$ | $\rho_{OIL}$ | $\eta_{t}^{OIL}$ | AR(1); no $\rho_{OIL}$ estimate is reported in Tables 2–4 |
| 25 | World LR rate | — | — | $\eta_{t}^{*,fwd}$ | only the innovation is listed |

Where the estimates are reported: AR coefficients for rows 1–4, 6–16 are in Table 2 (and Table 5); innovation S.D.s for rows 1–19 are in Table 3. For rows 20–25, Table 4 reports $\rho_{Y^{*}}$, $\rho_{\Pi^{*}}$, $\rho_{R^{*}}$ and the six S.D.s (Demand, Supply, Interest rate, World trade, Oil price, LR rate).

Cross-references (outside this chunk, for context only): the main-text equations give fixed coefficients 0.99 for the domestic premium (p.14, Section 3.1), the VAT rate (eq. 60), the inflation target (eq. 64) and the foreign forward real rate (eq. 90). This is consistent with no AR estimate being reported for these. In eq. (90) the innovation is printed $\varepsilon_{t}^{*,fwd}$, not $\eta^{*,fwd}$. The oil price follows an AR(2) process (eq. 93) with coefficients $c_{oil,-}$ and $c_{oil,\Delta}$ (Table 4), not an AR(1) with $\rho_{OIL}$; world trade follows eq. (91) with coefficients $c_{wt,\cdot}$.

### 4.4.3 Prior distributions

**Summary.** Table 2 lists the priors with the estimates. Footnote 30 notes that observation-equation parameters and shock S.D.s are in Table 3, and world-model parameters in Table 4.
- **Prior shape follows the parameter's admissible support:**
  - beta for parameters in (0,1): Calvo probabilities, AR coefficients, various weights;
  - gamma for parameters that must be positive, such as adjustment costs;
  - normal for unbounded parameters;
  - inverse gamma for shock standard errors.
- **Prior means** draw on estimates for similar foreign models and on pre-estimation calibration exercises. Those exercises judged model properties mainly through impulse responses, model-implied moments and historical shock decompositions. The main reference models are NAWM (euro area), RAMSES (euro area and Sweden), NEMO (Norway) and TOTEM (Canada). All are New Keynesian small-open-economy DSGE models with price and wage rigidities, incomplete exchange-rate pass-through, endogenous investment and an interest-rate policy instrument.

Specific prior choices:
- **Habit formation $\kappa$:** mean 0.7, mid-range of the reference models' estimates (0.57–0.88).
- **Indexation (all $\chi$):** mean 0.4. This lies between NAWM (0.5) and RAMSES (0.2) and is near Binyamini's (2007) estimate for Israeli prices.
- **Calvo probabilities (all $\xi$):** mean 0.6, i.e. a 2.5-quarter optimized price duration. This is somewhat shorter than the 3–4 quarters usual in macro studies, which the authors justify by Israel's relatively volatile inflation; it is also in line with Ribon (2004) and Binyamini (2007).
- **Adjustment costs ($\gamma_{I}$, $\omega_{\Gamma_{I}}$, $\gamma^{*}$):** taken from the pre-estimation calibration exercises.
- **External intermediation premium:**
  - $\gamma_{B}$ (on net foreign assets) follows the NAWM result. The text says 0.1, while Table 2 prints a prior mean of 0.01 (see [transcription notes](transcription-notes/T06.md)).
  - $\gamma_{S}$ (on the exchange rate) is 0.45, a little below RAMSES-Sweden's 0.6 and based on the calibration exercise.
- **Oil import share ($\omega^{*}$):** prior 0.15, roughly the fuel share in Israel's goods imports.
- **Policy rule:** standard literature values, close to other Israeli studies.
  - Smoothing $\phi_{R}$ 0.7, inflation response $\phi_{\Pi}$ 2.5, output-gap response $\phi_{y}$ 0.2.
  - These responses exceed Taylor's original (1.5, 0.125). Footnote 36: Taylor's 0.5 output coefficient refers to annualized rates, which is 0.125 for a quarterly rate. Because the rule includes smoothing, the short-run elasticities are actually smaller than the response parameters.
  - The depreciation response $\phi_{\Delta S}$ prior of 0.2 is not a standard literature value; it rests partly on earlier Israeli rule estimates (e.g. Argov and Elkayam 2010).
- **AR coefficients ($\rho$):** generally 0.7 (NAWM 0.75, RAMSES 0.85). The exception the text names is the four markup shocks, set to 0.3, reflecting the prior view that markup shocks (inflation-equation residuals) are unpredictable; Tables 3–4 show other exceptions ($\rho_{R^{*}}$ prior mean 0.25, $\rho_{EX}^{P_{OIL}^{*}}$ prior mean 0.50).
- **Prior standard deviations** express confidence in the means. Priors were kept wide in general, but tight enough to give a single posterior mode, i.e. enough curvature.

## 4.5 Estimation results

**Summary.** Tables 2–4 report the Bayesian estimates:
- Table 2: structural parameters and shock AR coefficients;
- Table 3: observation-equation parameters (section 4.2, Appendix B) and shock S.D.s;
- Table 4: the foreign-economy block (section 3.6).

In each table the middle panel gives the prior (shape, mean, std) and the right panel the posterior. Two methods supply the posterior figures:
- The **mode** comes from standard numerical optimization; its **std** is approximated from the inverse Hessian.
- The posterior **mean** and **5% / 95% percentiles** come from 4 Metropolis-Hastings chains of 700,000 draws, half discarded as burn-in. The scale is tuned for an acceptance rate of about 0.3, and convergence is monitored with Brooks and Gelman (1998).

**Identification (Figure 3).** Most, but not all, parameters are identified. Weakly identified ones, whose posterior largely reproduces the prior, are mainly the persistence parameters $\rho_{g_{z}}$, $\rho_{G}$, $\rho_{\nu^{*}}$, $\rho^{*}$ and the indexation parameters ($\chi$'s).

**Main findings.**
- **Nominal rigidity** is fairly low compared with other countries.
  - Imports are the most flexible: the estimate implies an average optimized price duration of 1.8 quarters, i.e. fast pass-through from the exchange rate and foreign prices to import prices.
  - Wage stickiness implies 2.2 quarters, below the prior (2.5) and below domestic prices (2.8). This may partly reflect volatile aggregate wage data rather than truly flexible wages.
- **Habit persistence** is consistent with the 0.7 prior.
- **Adjustment costs:**
  - Investment adjustment costs ($\gamma_{I}$) exceed the prior; the posterior mean is 3.3, still below NAWM (5.2) and RAMSES (8.7).
  - The data do not support an adjustment cost on the composition of world imports ($\gamma^{*}$); its posterior mean (0.65) is half the prior mean.
- **Modified UIP:** the data support the modification through $\gamma_{S}$ (see eq. (4)), but its posterior mean (0.36) is below the prior (0.45) and below the 0.61 posterior median for Sweden (Adolfson et al. 2008).
- **Policy rule:** mostly well identified.
  - Smoothing is strongly supported: mean $\phi_{R}$ 0.83, typical for extended Taylor rules.
  - The output-gap prior of 0.2 gets some support, with a posterior narrower than the prior.
  - The depreciation response is below the prior (mean 0.12 vs 0.2).
  - The data are uninformative about $\phi_{\Pi}$: the posterior roughly reproduces the prior (mean 2.5). The estimate is nonetheless broadly in line with other countries and earlier Israeli work.
- **Shock persistence:**
  - Technology shocks are relatively persistent: modes of about 0.9 for the transitory-technology ($\rho$) and investment-specific ($\rho_{I}$) AR coefficients. This suggests a sizable role for supply factors in Israel's cycle over the sample.
  - The four markup shocks have the lowest posterior modes (0.1–0.2). This mainly reflects their low priors, but the posteriors fall below the priors, so the data contribute too.
  - The external-premium persistence $\rho_{RP^{*}}$ (posterior mean 0.55, prior 0.7) agrees with Adolfson et al. (2008), who find that modifying UIP lowers this persistence; lower persistence means less predictable UIP deviations. Footnote 37: Adolfson et al. report a posterior median of 0.68 (prior mean 0.85) with modified UIP vs 0.93 without, and Christoffel et al. (2008) a mean of 0.88 (prior 0.75) with unmodified UIP.


#### Table 2: Prior and Posterior Distributions of the Main Structural Parameters (printed p. 50, pdf_page 56)

| Parameter | Symbol | Prior type | Prior mean | Prior std | Post. mode | Post. std | Post. mean | 5% | 95% |
|---|---|---|---|---|---|---|---|---|---|
| Habit formation | $\kappa$ | beta | 0.70 | 0.15 | 0.616 | 0.064 | 0.706 | 0.568 | 0.861 |
| *Indexation parameters* |  |  |  |  |  |  |  |  |  |
| Employment | $\chi_{E}$ | beta | 0.40 | 0.10 | 0.494 | 0.102 | 0.485 | 0.316 | 0.648 |
| Dom. prices | $\chi_{H}$ | beta | 0.40 | 0.10 | 0.365 | 0.097 | 0.355 | 0.201 | 0.504 |
| Import prices | $\chi_{IM}$ | beta | 0.40 | 0.10 | 0.300 | 0.089 | 0.322 | 0.179 | 0.462 |
| Wages | $\chi_{W}$ | beta | 0.40 | 0.10 | 0.377 | 0.100 | 0.377 | 0.217 | 0.531 |
| Exports | $\chi_{X}$ | beta | 0.40 | 0.10 | 0.281 | 0.085 | 0.294 | 0.158 | 0.429 |
| *Calvo parameters* |  |  |  |  |  |  |  |  |  |
| Employment | $\xi_{E}$ | beta | 0.60 | 0.10 | 0.614 | 0.040 | 0.646 | 0.552 | 0.743 |
| Dom. prices | $\xi_{H}$ | beta | 0.60 | 0.10 | 0.606 | 0.053 | 0.648 | 0.552 | 0.746 |
| Import prices | $\xi_{IM}$ | beta | 0.60 | 0.10 | 0.428 | 0.048 | 0.443 | 0.361 | 0.526 |
| Wages | $\xi_{W}$ | beta | 0.60 | 0.10 | 0.456 | 0.057 | 0.543 | 0.421 | 0.664 |
| Exports | $\xi_{X}$ | beta | 0.60 | 0.10 | 0.588 | 0.047 | 0.596 | 0.510 | 0.679 |
| Adj. cost inv. | $\gamma_{I}$ | gamma | 2.00 | 1.00 | 2.816 | 0.709 | 3.305 | 1.919 | 4.680 |
| Adj. cost inv. lag | $\omega_{\Gamma_{I}}$ | beta | 0.50 | 0.15 | 0.554 | 0.082 | 0.536 | 0.394 | 0.681 |
| Adj. cost export | $\gamma^{*}$ | gamma | 1.20 | 0.50 | 0.295 | 0.125 | 0.645 | 0.154 | 1.176 |
| FX premium - B* | $\gamma_{B}$ | gamma | 0.01 | 0.01 | 0.012 | 0.003 | 0.012 | 0.006 | 0.017 |
| FX premium - S | $\gamma_{S}$ | beta | 0.45 | 0.20 | 0.325 | 0.077 | 0.358 | 0.229 | 0.487 |
| Oil import share | $\omega^{*}$ | beta | 0.15 | 0.05 | 0.118 | 0.024 | 0.133 | 0.086 | 0.177 |
| *Monetary policy* |  |  |  |  |  |  |  |  |  |
| Smoothing | $\phi_{R}$ | beta | 0.70 | 0.10 | 0.814 | 0.035 | 0.833 | 0.780 | 0.887 |
| Resp. to inflation | $\phi_{\Pi}$ | gamma | 2.50 | 0.50 | 2.538 | 0.400 | 2.656 | 1.942 | 3.361 |
| Resp. to output | $\phi_{y}$ | gamma | 0.20 | 0.10 | 0.204 | 0.057 | 0.205 | 0.100 | 0.311 |
| Resp. to depreciation | $\phi_{\Delta S}$ | gamma | 0.20 | 0.10 | 0.090 | 0.043 | 0.124 | 0.037 | 0.206 |
| *Autoregressive coeff.* |  |  |  |  |  |  |  |  |  |
| Transitory techn. | $\rho$ | beta | 0.70 | 0.15 | 0.920 | 0.039 | 0.859 | 0.760 | 0.959 |
| Permanent techn. | $\rho_{g_{z}}$ | beta | 0.70 | 0.15 | 0.693 | 0.161 | 0.668 | 0.454 | 0.900 |
| Symmetric prem. | $\rho_{RP}$ | beta | 0.70 | 0.15 | 0.767 | 0.065 | 0.737 | 0.575 | 0.877 |
| External prem. | $\rho_{RP^{*}}$ | beta | 0.70 | 0.15 | 0.582 | 0.105 | 0.550 | 0.375 | 0.727 |
| Consumption | $\rho_{C}$ | beta | 0.70 | 0.15 | 0.782 | 0.241 | 0.584 | 0.275 | 0.938 |
| Inv. techn. | $\rho_{I}$ | beta | 0.70 | 0.15 | 0.906 | 0.035 | 0.732 | 0.482 | 0.944 |
| Inventory inv. | $\rho_{\Delta INV}$ | beta | 0.70 | 0.15 | 0.708 | 0.109 | 0.678 | 0.513 | 0.852 |
| Government | $\rho_{G}$ | beta | 0.70 | 0.15 | 0.679 | 0.218 | 0.672 | 0.416 | 0.935 |
| Export share | $\rho_{\nu^{*}}$ | beta | 0.70 | 0.15 | 0.839 | 0.094 | 0.664 | 0.377 | 0.921 |
| Home bias | $\rho_{\nu}$ | beta | 0.70 | 0.15 | 0.802 | 0.091 | 0.770 | 0.627 | 0.915 |
| Domestic markup | $\rho_{\varphi^{H}}$ | beta | 0.30 | 0.15 | 0.196 | 0.131 | 0.241 | 0.039 | 0.429 |
| Import markup | $\rho_{\varphi^{*}}$ | beta | 0.30 | 0.15 | 0.203 | 0.135 | 0.258 | 0.048 | 0.461 |
| Wage markup | $\rho_{\varphi^{W}}$ | beta | 0.30 | 0.15 | 0.109 | 0.079 | 0.187 | 0.025 | 0.343 |
| Export markup | $\rho_{\varphi^{X}}$ | beta | 0.30 | 0.15 | 0.102 | 0.078 | 0.142 | 0.017 | 0.261 |
| Foreign transfers | $\rho_{FTR}$ | beta | 0.70 | 0.15 | 0.431 | 0.183 | 0.441 | 0.201 | 0.681 |

- **$\gamma_{B}$ prior (FX premium, B\*):** the text gives a prior mean of 0.1, the table 0.01. Figure 3's prior curve for $\gamma_{B}$ (PDF p.60) is hump-shaped with its mode near 0.0073, which fits gamma(mean 0.01, std ≈ 0.005) and rules out mean 0.1. Gamma(0.01, 0.01) as printed would be an exponential with its mode at 0, so the printed std "0.01" is most likely 0.005 rounded. Do not use gamma(0.01, 0.01) as is (evidence from digitizing Figure 3 in the independent check).

Notes on Table 2:
- Rows are printed in groups headed by italic labels (*Indexation parameters*, *Calvo parameters*, *Monetary policy*, *Autoregressive coeff.*). An unlabelled block (adjustment costs, FX premium, oil share) follows a blank spacer line after the Calvo group. In the CSV these rows have an empty `group`.
- "Employment" under Indexation/Calvo is printed with subscript $E$ ($\chi_{E}$, $\xi_{E}$), whereas the employment equation (95) in 4.1 writes $\chi_{EM}$, $\xi_{EM}$.
- The markup AR coefficients are printed $\rho_{\varphi^{H}}$, $\rho_{\varphi^{*}}$, $\rho_{\varphi^{W}}$, $\rho_{\varphi^{X}}$ here, but $\rho_{H}$, $\rho^{*}$, $\rho_{W}$, $\rho_{X}$ in 4.4.2, Table 5 and Figure 3. The values agree with Table 5's baseline.
- "FX premium - B*" ($\gamma_{B}$) has a prior mean of 0.01, while the text of 4.4.3 says the NAWM value 0.1 (see [transcription notes](transcription-notes/T06.md)).


#### Table 3: Prior and Posterior Distributions of Observation Parameters and Shock Standard Deviations (printed p. 51, pdf_page 57)

| Parameter | Symbol | Prior type | Prior mean | Prior std | Post. mode | Post. std | Post. mean | 5% | 95% |
|---|---|---|---|---|---|---|---|---|---|
| *Observation parameters* |  |  |  |  |  |  |  |  |  |
| Obs. error output def. | $\rho_{OB,\Delta Y}$ | normal | 0.00 | 0.25 | -0.185 | 0.136 | -0.189 | -0.421 | 0.032 |
| Employment | $\rho_{OB,E}$ | beta | 0.70 | 0.15 | 0.907 | 0.044 | 0.837 | 0.718 | 0.959 |
| Constant | $tp$ | normal | 0.01 | 0.01 | 0.012 | 0.004 | 0.011 | 0.004 | 0.018 |
| Obs. error | $\rho_{OB,fwd}$ | beta | 0.70 | 0.15 | 0.740 | 0.169 | 0.716 | 0.510 | 0.938 |
| Constant | $tp^{*}$ | normal | 0.02 | 0.01 | 0.018 | 0.004 | 0.018 | 0.011 | 0.025 |
| Obs. error | $\rho_{OB,fwd^{*}}$ | beta | 0.70 | 0.15 | 0.832 | 0.104 | 0.791 | 0.631 | 0.958 |
| Hours | $\rho_{EX}^{N}$ | beta | 0.70 | 0.15 | 0.933 | 0.038 | 0.792 | 0.569 | 0.979 |
| Consumption | $\rho_{EX}^{C}$ | beta | 0.70 | 0.15 | 0.546 | 0.179 | 0.600 | 0.365 | 0.842 |
| Investment | $\rho_{EX}^{I}$ | beta | 0.70 | 0.15 | 0.735 | 0.189 | 0.737 | 0.515 | 0.948 |
| Export | $\rho_{EX}^{X}$ | beta | 0.70 | 0.15 | 0.602 | 0.169 | 0.580 | 0.332 | 0.824 |
| Import | $\rho_{EX}^{IM}$ | beta | 0.70 | 0.15 | 0.675 | 0.160 | 0.615 | 0.377 | 0.855 |
| Foreign GDP | $\rho_{EX}^{Y^{*}}$ | beta | 0.70 | 0.15 | 0.655 | 0.143 | 0.645 | 0.432 | 0.866 |
| World trade | $\rho_{EX}^{WT^{*}}$ | beta | 0.70 | 0.15 | 0.849 | 0.077 | 0.800 | 0.654 | 0.950 |
| Oil price | $\rho_{EX}^{P_{OIL}^{*}}$ | beta | 0.50 | 0.07 | 0.566 | 0.067 | 0.552 | 0.443 | 0.660 |
| *Shocks' standard deviations* |  |  |  |  |  |  |  |  |  |
| Obs. error output def. | S.D.($\eta^{\Delta P_{Y}^{M}}$) | inv. gamma | 0.01 | Inf | 0.007 | 0.001 | 0.007 | 0.006 | 0.009 |
| Employment | S.D.($\eta^{OB,E}$) | inv. gamma | 0.01 | Inf | 0.003 | 0.000 | 0.003 | 0.002 | 0.003 |
| Dom. term prem. | S.D.($\eta^{fwd,OB}$) | inv. gamma | 0.01 | Inf | 0.002 | 0.001 | 0.002 | 0.002 | 0.003 |
| Foreign term prem. | S.D.($\eta^{*,fwd,OB}$) | inv. gamma | 0.01 | Inf | 0.002 | 0.000 | 0.002 | 0.001 | 0.002 |
| Hours worked | S.D.($\eta_{EX}^{N}$) | inv. gamma | 0.00 | 0.00 | 0.001 | 0.000 | 0.001 | 0.000 | 0.001 |
| Consumption | S.D.($\eta_{EX}^{C}$) | inv. gamma | 0.01 | 0.00 | 0.003 | 0.000 | 0.003 | 0.002 | 0.004 |
| Investment | S.D.($\eta_{EX}^{I}$) | inv. gamma | 0.01 | 0.00 | 0.004 | 0.001 | 0.004 | 0.003 | 0.006 |
| Export | S.D.($\eta_{EX}^{X}$) | inv. gamma | 0.01 | 0.00 | 0.003 | 0.001 | 0.003 | 0.002 | 0.005 |
| Import | S.D.($\eta_{EX}^{IM}$) | inv. gamma | 0.01 | 0.00 | 0.003 | 0.001 | 0.003 | 0.002 | 0.004 |
| Wages | S.D.($\eta_{EX}^{W}$) | inv. gamma | 0.01 | 0.00 | 0.010 | 0.002 | 0.011 | 0.007 | 0.016 |
| Foreign GDP | S.D.($\eta_{EX}^{Y^{*}}$) | inv. gamma | 0.01 | 0.00 | 0.003 | 0.000 | 0.003 | 0.002 | 0.003 |
| World trade | S.D.($\eta_{EX}^{WT^{*}}$) | inv. gamma | 0.01 | 0.00 | 0.004 | 0.001 | 0.004 | 0.003 | 0.006 |
| Oil price | S.D.($\eta_{EX}^{P_{OIL}^{*}}$) | inv. gamma | 0.03 | 0.01 | 0.032 | 0.007 | 0.038 | 0.023 | 0.052 |
| Exchange rate | S.D.($\eta_{EX}^{S}$) | inv. gamma | 0.01 | 0.01 | 0.013 | 0.002 | 0.014 | 0.010 | 0.018 |
| Transitory techn. | S.D.($\eta$) | inv. gamma | 0.03 | Inf | 0.011 | 0.001 | 0.012 | 0.010 | 0.013 |
| Permanent techn. | S.D.($\eta^{g_{z}}$) | inv. gamma | 0.01 | Inf | 0.002 | 0.000 | 0.002 | 0.001 | 0.002 |
| Symmetric prem. | S.D.($\eta^{RP}$) | inv. gamma | 0.03 | Inf | 0.010 | 0.003 | 0.013 | 0.006 | 0.022 |
| External prem. | S.D.($\eta^{RP^{*}}$) | inv. gamma | 0.03 | Inf | 0.011 | 0.002 | 0.011 | 0.008 | 0.014 |
| Dom. prem. | S.D.($\eta^{DRP}$) | inv. gamma | 0.00 | Inf | 0.000 | 0.000 | 0.001 | 0.000 | 0.001 |
| Consumption | S.D.($\eta^{C}$) | inv. gamma | 0.03 | Inf | 0.012 | 0.006 | 0.035 | 0.007 | 0.067 |
| Inv. techn. | S.D.($\eta^{I}$) | inv. gamma | 0.05 | Inf | 0.042 | 0.009 | 0.052 | 0.020 | 0.081 |
| Inventory inv. | S.D.($\eta^{\Delta INV}$) | inv. gamma | 0.01 | Inf | 0.013 | 0.001 | 0.013 | 0.011 | 0.015 |
| Government | S.D.($\eta^{G}$) | inv. gamma | 0.01 | Inf | 0.006 | 0.001 | 0.006 | 0.004 | 0.008 |
| Export share | S.D.($\eta^{\nu^{*}}$) | inv. gamma | 0.05 | Inf | 0.042 | 0.007 | 0.058 | 0.035 | 0.082 |
| Home bias | S.D.($\eta^{\nu}$) | inv. gamma | 0.01 | Inf | 0.008 | 0.001 | 0.008 | 0.007 | 0.010 |
| Domestic markup | S.D.($\eta^{\varphi^{H}}$) | inv. gamma | 0.05 | Inf | 0.028 | 0.009 | 0.038 | 0.016 | 0.059 |
| Import markup | S.D.($\eta^{\varphi^{*}}$) | inv. gamma | 0.03 | Inf | 0.026 | 0.007 | 0.029 | 0.015 | 0.043 |
| Wage markup | S.D.($\eta^{\varphi^{W}}$) | inv. gamma | 0.50 | Inf | 0.238 | 0.068 | 0.335 | 0.141 | 0.519 |
| Export markup | S.D.($\eta^{\varphi^{X}}$) | inv. gamma | 0.10 | Inf | 0.066 | 0.017 | 0.076 | 0.042 | 0.107 |
| Foreign transfers | S.D.($\eta^{FTR}$) | inv. gamma | 0.01 | Inf | 0.016 | 0.002 | 0.016 | 0.013 | 0.019 |
| Interest rate | S.D.($\eta^{R}$) | inv. gamma | 0.01 | Inf | 0.002 | 0.000 | 0.002 | 0.002 | 0.003 |
| Inf. target | S.D.($\eta^{\bar{\Pi}}$) | inv. gamma | 0.00 | Inf | 0.001 | 0.000 | 0.001 | 0.001 | 0.001 |
| Consumption tax | S.D.($\eta^{\tau^{C}}$) | inv. gamma | 0.00 | Inf | 0.002 | 0.000 | 0.002 | 0.002 | 0.003 |

Notes on Table 3:
- Observation parameters map to Appendix B: $\rho_{EX}^{J}$ are the AR coefficients of the excess-trend processes (eq. 102 for $J \in \{C, I, X, IM, Y^{*}, WT^{*}\}$). The hours row $\rho_{EX}^{N}$ is the persistence of the hours trend $GR_{t}^{N}$ in eq. 98 (written $\rho_{GR}^{N}$ there; Appendix D (322) uses the table's label), and the oil persistence is stated in the text after eq. 107 and in Appendix D (331). $\rho_{OB,fwd}$ and $\rho_{OB,fwd^{*}}$ are the AR coefficients of the forward-rate observation errors. $tp$ and $tp^{*}$ are the constant term premiums (eqs. 108–109). $\rho_{OB,\Delta Y}$ and $\rho_{OB,E}$ are presumably the AR(1) coefficients of the output-deflator and employment observation errors; the paper does not print a process for these errors.
- S.D. rows: $\eta^{\Delta P_{Y}^{M}}$ (output deflator), $\eta^{OB,E}$, $\eta^{fwd,OB}$ (domestic term premium), $\eta^{*,fwd,OB}$ (foreign term premium), $\eta_{EX}^{J}$ (excess-trend innovations), then the 19 domestic structural innovations of 4.4.2.
- "0.00" prior cells are two-decimal roundings and cannot be used as parameter values; source the true values elsewhere rather than inventing them. Prior **std** "0.00" appears in 8 rows of Table 3 (Hours worked, Consumption, Investment, Export, Import, Wages, Foreign GDP, World trade excess trends). Prior **mean** "0.00" appears in 6 rows: Table 3 Hours worked, Dom. prem. ($\eta^{DRP}$), Inf. target ($\eta^{\bar{\Pi}}$), Consumption tax ($\eta^{\tau^{C}}$), and Table 4 Interest rate ($\eta^{R^{*}}$) and LR rate ($\eta^{*,fwd}$). Prior std "Inf" is printed as text and is not defined in the paper. All cells are kept exactly as printed.
- $\rho_{OB,\Delta Y}$ (normal prior) is the only negative estimate in this table: mode -0.185, mean -0.189, 5% -0.421, 95% 0.032.
- 14 observation-type S.D.s are listed (rows 1–14 of the S.D. block, Obs. error output def. to Exchange rate). This matches the "14 observation equation shocks" of 4.4.2.


#### Table 4: Prior and Posterior Distributions of the World Model's Parameters (printed p. 52, pdf_page 58)

| Parameter | Symbol | Prior type | Prior mean | Prior std | Post. mode | Post. std | Post. mean | 5% | 95% |
|---|---|---|---|---|---|---|---|---|---|
| *Output equation* |  |  |  |  |  |  |  |  |  |
| Expectations | $c_{y^{*},+}$ | beta | 0.50 | 0.10 | 0.227 | 0.048 | 0.225 | 0.146 | 0.302 |
| Real rate | $c_{y^{*},r}$ | gamma | 0.20 | 0.05 | 0.156 | 0.030 | 0.157 | 0.107 | 0.205 |
| AR in shock | $\rho_{Y^{*}}$ | beta | 0.70 | 0.07 | 0.643 | 0.063 | 0.636 | 0.535 | 0.738 |
| *Inflation equation* |  |  |  |  |  |  |  |  |  |
| Expectations | $c_{\pi^{*},+}$ | beta | 0.70 | 0.15 | 0.966 | 0.026 | 0.953 | 0.915 | 0.993 |
| Output | $c_{\pi^{*},y}$ | gamma | 0.10 | 0.03 | 0.071 | 0.017 | 0.076 | 0.046 | 0.105 |
| Oil - level | $c_{\pi^{*},OIL}$ | gamma | 0.05 | 0.03 | 0.025 | 0.007 | 0.028 | 0.015 | 0.041 |
| Oil - change | $c_{\pi^{*},\Delta OIL}$ | gamma | 0.05 | 0.03 | 0.016 | 0.005 | 0.017 | 0.008 | 0.026 |
| AR in shock | $\rho_{\Pi^{*}}$ | beta | 0.70 | 0.15 | 0.247 | 0.084 | 0.261 | 0.125 | 0.391 |
| *Monetary policy equation* |  |  |  |  |  |  |  |  |  |
| Smoothing | $c_{r^{*},-}$ | beta | 0.75 | 0.10 | 0.832 | 0.033 | 0.831 | 0.778 | 0.885 |
| Resp. to inflation | $c_{r^{*},\pi}$ | gamma | 2.50 | 0.50 | 2.087 | 0.429 | 2.211 | 1.487 | 2.908 |
| Resp. to output | $c_{r^{*},y}$ | gamma | 0.50 | 0.05 | 0.516 | 0.051 | 0.523 | 0.437 | 0.606 |
| AR in shock | $\rho_{R^{*}}$ | beta | 0.25 | 0.05 | 0.302 | 0.053 | 0.301 | 0.215 | 0.385 |
| *World trade equation* |  |  |  |  |  |  |  |  |  |
| Output | $c_{wt,y}$ | normal | 2.50 | 0.50 | 2.336 | 0.371 | 2.331 | 1.719 | 2.961 |
| Lagged output | $c_{wt,y-}$ | normal | 0.00 | 1.00 | 1.509 | 0.746 | 1.380 | 0.165 | 2.626 |
| Lagged world trade | $c_{wt,-}$ | normal | 0.00 | 0.50 | 0.176 | 0.149 | 0.215 | -0.029 | 0.468 |
| *Oil price inflation* |  |  |  |  |  |  |  |  |  |
| Lag | $c_{oil,-}$ | beta | 0.70 | 0.15 | 0.667 | 0.078 | 0.635 | 0.505 | 0.771 |
| Lagged change | $c_{oil,\Delta}$ | normal | 0.00 | 0.50 | -0.415 | 0.096 | -0.411 | -0.576 | -0.250 |
| *Shocks' standard deviations* |  |  |  |  |  |  |  |  |  |
| Demand | S.D.($\eta^{Y^{*}}$) | inv. gamma | 0.01 | Inf | 0.002 | 0.000 | 0.002 | 0.002 | 0.003 |
| Supply | S.D.($\eta^{\Pi^{*}}$) | inv. gamma | 0.01 | Inf | 0.007 | 0.001 | 0.007 | 0.006 | 0.009 |
| Interest rate | S.D.($\eta^{R^{*}}$) | inv. gamma | 0.00 | Inf | 0.002 | 0.000 | 0.002 | 0.002 | 0.003 |
| World trade | S.D.($\eta^{WT^{*}}$) | inv. gamma | 0.03 | Inf | 0.007 | 0.001 | 0.007 | 0.005 | 0.009 |
| Oil price | S.D.($\eta^{OIL}$) | inv. gamma | 0.10 | Inf | 0.124 | 0.012 | 0.124 | 0.101 | 0.146 |
| LR rate | S.D.($\eta^{*,fwd}$) | inv. gamma | 0.00 | Inf | 0.001 | 0.000 | 0.001 | 0.000 | 0.001 |

Notes on Table 4:
- The coefficient names match the foreign-economy equations (89)–(94) of section 3.6, with one exception: equation (91) writes the lagged-output coefficient $c_{wt,y\_lag}$, where the table writes $c_{wt,y-}$. Appendix D (289) prints $c_{wt,y-}$ (as in the table) and the lagged-world-trade coefficient with a star, $c_{wt,-}^{*}$.
- The oil-price block follows the AR(2) process (93) with $c_{oil,-}$ and $c_{oil,\Delta}$; there is no separate $\rho_{OIL}$ estimate. **Sign conflict:** (93) adds $+c_{oil,\Delta}(\hat{p}_{OIL,t-1}^{*}-\hat{p}_{OIL,t-2}^{*})$ while Appendix D (290) subtracts it; the estimate is negative (mode −0.415), so the convention decides the direction of the effect. Check which form the estimation used before implementing.
- Negative values: Lagged world trade 5% = -0.029; Lagged change $c_{oil,\Delta}$ mode -0.415, mean -0.411, 5% -0.576, 95% -0.250.
- Shock S.D. labels: Demand = $\eta^{Y^{*}}$, Supply = $\eta^{\Pi^{*}}$, Interest rate = $\eta^{R^{*}}$, World trade = $\eta^{WT^{*}}$, Oil price = $\eta^{OIL}$, LR rate = $\eta^{*,fwd}$. These are the innovations of the world shocks in 4.4.2.

#### Figure 3: Prior and Posterior Distributions of the Structural Parameters (printed pp. 53–56, pdf_pages 59–62)

The figure is printed in landscape orientation (rotated 90° on the page), over four pages titled "Figure 3: … (cont.)" after the first. Each page has nine panels in a 3 × 3 grid. The legend note is the same on every page: the dashed line (green in the PDF) marks the conditional posterior mode, the black line the posterior and the gray line the prior. The 36 panels are exactly the 36 parameters of Table 2, in the same order. Read with the page turned to landscape, row by row:

| pdf_page (printed) | Parameters plotted |
|---|---|
| 59 (53) | $\kappa$, $\chi_{E}$, $\chi_{H}$; $\chi_{IM}$, $\chi_{W}$, $\chi_{X}$; $\xi_{E}$, $\xi_{H}$, $\xi_{IM}$ |
| 60 (54) | $\xi_{W}$, $\xi_{X}$, $\gamma_{I}$; $\omega_{\Gamma_{I}}$, $\gamma^{*}$, $\gamma_{B}$; $\gamma_{S}$, $\omega^{*}$, $\phi_{R}$ |
| 61 (55) | $\phi_{\Pi}$, $\phi_{y}$, $\phi_{\Delta S}$; $\rho$, $\rho_{g_{z}}$, $\rho_{RP}$; $\rho_{RP^{*}}$, $\rho_{C}$, $\rho_{I}$ |
| 62 (56) | $\rho_{\Delta INV}$, $\rho_{G}$, $\rho_{\nu^{*}}$; $\rho_{\nu}$, $\rho_{H}$, $\rho^{*}$; $\rho_{W}$, $\rho_{X}$, $\rho_{FTR}$ |

Panel labels are printed as in Table 2, except for the four markup AR coefficients on p.62, which are labelled $\rho_{H}$, $\rho^{*}$, $\rho_{W}$, $\rho_{X}$ (as in Table 5), not $\rho_{\varphi^{H}}$ etc. Shock S.D.s, observation parameters and world-model parameters (Tables 3–4) are not plotted. No readings were taken (not requested).

## 4.6 Sensitivity analysis

**Summary.** This section re-estimates the model's posterior mode under five alternative versions of the interest-rate rule (62). The rule is chosen because it is the only ad hoc behavioral equation; the other behavioral equations come from agents' optimization. Each version is judged by how the parameter estimates change and by the marginal likelihood. Only the posterior mode is computed, because Metropolis-Hastings runs are very time-consuming.

The five alternatives:
- **Alternatives 1–2 (smoothing of rate changes):** add the lagged rate change $\Delta R_{t-1}$ with coefficient $\phi_{\Delta R}$, with a Gamma prior of mean 1.0. The motivation is optimal policy under commitment with a policymaker averse to rate volatility. Footnote 38 (Woodford 2003, Ch. 8.3): such rules contain $\Delta R_{t-1}$ with coefficient $\beta^{-1}$, slightly above one. Alternative 1 uses prior std 0.5; alternative 2 a tight prior with std 0.05.
- **Alternatives 3–4 (output growth):** add the lagged output growth rate (97.i7) with coefficient $\phi_{\Delta Y}$, inside the square brackets of (62), so its overall coefficient is $(1-\phi_{R})\phi_{\Delta Y}$ (97.i8). The prior is Gamma with mean 0.1 and std 0.05. Alternative 3 replaces the output-gap response ($\phi_{y}=0$); alternative 4 keeps both.
- **Alternative 5 (forward-looking):** the policy inflation measure (65), which mixes lagged and expected inflation, is replaced by the purely forward-looking measure 97.u2.

**Results (Table 5).** Estimates change little across specifications.
- **Alternatives 1–2:** the smoothing term affects the marginal likelihood.
  - A tight prior around one (alternative 2) worsens the fit (4429.7 vs 4444.6).
  - With the wider prior (alternative 1) the mode of $\phi_{\Delta R}$ is only 0.234, and the other parameters and the overall fit stay close to the baseline.
- **Alternative 3:** replacing the gap with growth does not raise the likelihood. The growth coefficient is 0.172, close to the gap coefficient, and smoothing rises slightly, probably because growth is more volatile than the gap.
- **Alternative 4:** including both gives a small gain (marginal likelihood 4444.6 → 4447.5). The gap coefficient stays about 0.2, the growth response is 0.15, and the other parameters are close to baseline.
- **Alternative 5:** the forward-looking rule barely changes the policy parameters but lowers the marginal likelihood somewhat. The authors find this at odds with the Bank of Israel's emphasis on (market-based) inflation expectations and with the good performance of single-equation Taylor rules using market expectations (fn. 39). They reconcile the two by noting that market expectations may differ from model-consistent ones.

Overall, the results are not very sensitive to the policy-rule specification; section 5 discusses the alternatives further.

<!-- kind: inline; id: 97.i6; section: 4.6; page: 58; pdf_page: 64 -->
**(97.i6) Additional smoothing term in alternatives 1 and 2**

$$
\Delta R_{t-1}
$$

Meaning: The lagged change in the policy rate, added to the rule with coefficient $\phi_{\Delta R}$ (prior Gamma, mean 1.0).

<!-- kind: inline; id: 97.i7; section: 4.6; page: 59; pdf_page: 65 -->
**(97.i7) Lagged output growth term in alternatives 3 and 4 (coefficient $\phi_{\Delta Y}$)**

$$
\hat{y}_{t-1} - \hat{y}_{t-2} + \hat{g}_{z,t-1}
$$

Meaning: Lagged growth of output, i.e. the change in detrended output plus the lagged technology growth rate, entering the rule with coefficient $\phi_{\Delta Y}$.

<!-- kind: inline; id: 97.i8; section: 4.6; page: 59; pdf_page: 65 -->
**(97.i8) Overall coefficient on output growth (term placed inside the brackets of (62))**

$$
\left(1-\phi_{R}\right) \phi_{\Delta Y}
$$

Meaning: Because the growth term sits inside the smoothed bracket of rule (62), its effective coefficient is scaled by one minus the smoothing parameter.

<!-- kind: inline; id: 97.i9; section: 4.6; page: 59; pdf_page: 65 -->
**(97.i9) Output-gap response switched off in alternative 3**

$$
\phi_{y} = 0
$$

Meaning: In alternative 3 the response to output growth replaces the response to the output gap.

<!-- kind: inline; id: 97.i10; section: 4.6; page: 59; pdf_page: 65 -->
**(97.i10) Coefficient on the lagged rate change under commitment (footnote 38)**

$$
\beta^{-1}
$$

Meaning: Under optimal commitment policy the coefficient on $\Delta R_{t-1}$ equals the inverse discount factor, slightly above one.

<!-- kind: display; id: 97.u2; section: 4.6; page: 59; pdf_page: 65 -->
**(97.u2) Inflation measure of the fully forward-looking rule (alternative 5), replacing (65)**

$$
\hat{\pi}_{t}^{CB} = E_{t}\left[\hat{\pi}_{C,t} + \hat{\pi}_{C,t+1} + \hat{\pi}_{C,t+2} + \hat{\pi}_{C,t+3}\right]
$$

Meaning: In alternative 5 the central bank responds to expected CPI inflation summed over the current and next three quarters, instead of the mix of lagged and expected inflation in (65).

Note: Equation (65), printed on PDF p.32 (outside this chunk), is $\hat{\pi}_{t}^{CB} = E_{t}\left[\hat{\pi}_{C,t-2} + \hat{\pi}_{C,t-1} + \hat{\pi}_{C,t} + \hat{\pi}_{C,t+1}\right]$, shown here only for comparison; it is not transcribed as a block of this chunk.


#### Table 5: Posterior Mode Sensitivity to Different Interest Rate Rules (printed p. 60, pdf_page 66)

| Parameter | Symbol | Baseline | 1: $\phi_{\Delta R}$ | 2: $\phi_{\Delta R}=1$ | 3: $\phi_{\Delta Y}$, $\phi_{y}=0$ | 4: $\phi_{\Delta Y}$ | 5: fwd looking |
|---|---|---|---|---|---|---|---|
| Habit formation | $\kappa$ | 0.616 | 0.620 | 0.625 | 0.619 | 0.611 | 0.607 |
| *Indexation parameters* |  |  |  |  |  |  |  |
| Employment | $\chi_{E}$ | 0.494 | 0.490 | 0.476 | 0.502 | 0.494 | 0.499 |
| Dom. prices | $\chi_{H}$ | 0.365 | 0.368 | 0.364 | 0.375 | 0.364 | 0.339 |
| Import prices | $\chi_{IM}$ | 0.300 | 0.305 | 0.318 | 0.310 | 0.298 | 0.285 |
| Wages | $\chi_{W}$ | 0.377 | 0.378 | 0.377 | 0.379 | 0.376 | 0.387 |
| Exports | $\chi_{X}$ | 0.281 | 0.279 | 0.273 | 0.284 | 0.279 | 0.275 |
| *Calvo parameters* |  |  |  |  |  |  |  |
| Employment | $\xi_{E}$ | 0.614 | 0.615 | 0.621 | 0.614 | 0.614 | 0.618 |
| Dom. prices | $\xi_{H}$ | 0.606 | 0.602 | 0.601 | 0.608 | 0.609 | 0.676 |
| Import prices | $\xi_{IM}$ | 0.428 | 0.423 | 0.396 | 0.430 | 0.429 | 0.473 |
| Wages | $\xi_{W}$ | 0.456 | 0.459 | 0.476 | 0.447 | 0.459 | 0.474 |
| Exports | $\xi_{X}$ | 0.588 | 0.590 | 0.594 | 0.589 | 0.588 | 0.593 |
| Adj. cost inv. | $\gamma_{I}$ | 2.816 | 2.788 | 2.528 | 3.056 | 2.786 | 2.541 |
| Adj. cost inv. lag | $\omega_{\Gamma_{I}}$ | 0.554 | 0.554 | 0.558 | 0.554 | 0.556 | 0.549 |
| Adj. cost export | $\gamma^{*}$ | 0.295 | 0.304 | 0.322 | 0.316 | 0.295 | 0.287 |
| FX premium - B* | $\gamma_{B}$ | 0.012 | 0.012 | 0.012 | 0.013 | 0.012 | 0.011 |
| FX premium - S | $\gamma_{S}$ | 0.325 | 0.352 | 0.412 | 0.326 | 0.334 | 0.326 |
| Oil import share | $\omega^{*}$ | 0.118 | 0.120 | 0.122 | 0.122 | 0.118 | 0.118 |
| *Monetary policy* |  |  |  |  |  |  |  |
| Smoothing | $\phi_{R}$ | 0.814 | 0.805 | 0.743 | 0.858 | 0.813 | 0.837 |
| Resp. to inflation | $\phi_{\Pi}$ | 2.538 | 2.273 | 1.801 | 2.681 | 2.515 | 2.733 |
| Resp. to output | $\phi_{y}$ | 0.204 | 0.209 | 0.296 | - | 0.194 | 0.233 |
| Resp. to depreciation | $\phi_{\Delta S}$ | 0.090 | 0.112 | 0.228 | 0.116 | 0.095 | 0.085 |
| Resp. to R change | $\phi_{\Delta R}$ | - | 0.234 | 0.924 | - | - | - |
| Resp. to output growth | $\phi_{\Delta Y}$ | - | - | - | 0.172 | 0.149 | - |
| *Autoregressive coeff.* |  |  |  |  |  |  |  |
| Transitory techn. | $\rho$ | 0.920 | 0.913 | 0.875 | 0.926 | 0.917 | 0.911 |
| Permanent techn. | $\rho_{g_{z}}$ | 0.693 | 0.684 | 0.673 | 0.796 | 0.697 | 0.775 |
| Symmetric prem. | $\rho_{RP}$ | 0.767 | 0.768 | 0.788 | 0.622 | 0.766 | 0.734 |
| External prem. | $\rho_{RP^{*}}$ | 0.582 | 0.543 | 0.427 | 0.609 | 0.574 | 0.587 |
| Consumption | $\rho_{C}$ | 0.782 | 0.778 | 0.743 | 0.758 | 0.780 | 0.746 |
| Inv. techn. | $\rho_{I}$ | 0.906 | 0.904 | 0.899 | 0.913 | 0.904 | 0.914 |
| Inventory inv. | $\rho_{\Delta INV}$ | 0.708 | 0.704 | 0.695 | 0.689 | 0.707 | 0.697 |
| Government | $\rho_{G}$ | 0.679 | 0.680 | 0.677 | 0.677 | 0.680 | 0.684 |
| Export share | $\rho_{\nu^{*}}$ | 0.839 | 0.830 | 0.810 | 0.828 | 0.839 | 0.861 |
| Home bias | $\rho_{\nu}$ | 0.802 | 0.798 | 0.788 | 0.763 | 0.804 | 0.779 |
| Domestic markup | $\rho_{H}$ | 0.196 | 0.202 | 0.204 | 0.179 | 0.195 | 0.191 |
| Import markup | $\rho^{*}$ | 0.203 | 0.211 | 0.232 | 0.207 | 0.198 | 0.196 |
| Wage markup | $\rho_{W}$ | 0.109 | 0.113 | 0.120 | 0.098 | 0.109 | 0.109 |
| Export markup | $\rho_{X}$ | 0.102 | 0.100 | 0.090 | 0.108 | 0.102 | 0.104 |
| Foreign transfers | $\rho_{FTR}$ | 0.431 | 0.420 | 0.379 | 0.435 | 0.432 | 0.439 |
| **Marginal likelihood** |  | 4444.6 | 4444.8 | 4429.7 | 4443.9 | 4447.5 | 4439.5 |

Notes on Table 5:
- Column headers as printed: "Baseline", "1" ($\phi_{\Delta R}$), "2" ($\phi_{\Delta R}=1$), "3" ($\phi_{\Delta Y}$ over $\phi_{y}=0$), "4" ($\phi_{\Delta Y}$), "5" ($fwd$ over "looking"). The CSV column names (`alt1_phi_DeltaR`, …) are descriptive, not printed text.
- "-" cells mean the coefficient is not part of that specification. They are kept as the printed text "-".
- The baseline column equals the posterior modes of Table 2, entry for entry.
- The markup AR coefficients are labelled $\rho_{H}$, $\rho^{*}$, $\rho_{W}$, $\rho_{X}$ here (Table 2 uses $\rho_{\varphi^{H}}$ etc.).
- The two policy rows absent from Table 2 are "Resp. to R change" ($\phi_{\Delta R}$) and "Resp. to output growth" ($\phi_{\Delta Y}$).
- The "Marginal likelihood" row is a summary row (`row_type` = `summary`). The text treats a higher value as a better fit: it says alternative 2 reduces the fit (4429.7) and calls alternative 4 an improvement (4444.6 → 4447.5).
