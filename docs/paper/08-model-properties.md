# Model properties: variance decomposition and impulse responses

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

Section 6: forecast-error variance decomposition (Table 7, also `data/table7_variance_decomposition.csv`) and impulse responses (Figures 6–10); Appendix E (Figures 11–18). The plotted impulse responses are digitized in `data/irf/`.

## 6 Model properties

page 68; pdf_page 74 (the heading follows the last paragraph of Section 5 on the same page).

**Summary.** Section 6 shows how the estimated model behaves. Subsection 6.1 reports how the forecast-error variance of ten key variables is divided among the 25 structural shocks at three horizons (Table 7). Subsection 6.2 presents Bayesian impulse responses to five central shocks (Figures 6–10) and explains their transmission. Responses to eight further shocks are in Appendix E (Figures 11–18). The section contains no numbered equations.

### 6.1 Variance decomposition

pages 68–72; pdf_pages 74–78 (Table 7 on pages 69–70, pdf_pages 75–76; footnote 48 on page 71).

**Summary.** Table 7 splits the forecast-error variance of ten variables among the 25 structural shocks at the 1-quarter, 4-quarter and infinite horizons; real variables are stationarized first. CPI inflation is driven mainly by the external risk premium shock and the price-markup shocks, with the oil-price shock gaining weight at longer horizons. Output is driven by demand-type shocks in the short run and by technology shocks in the long run (other real variables differ: see Table 7). The long-run variance of the policy rate is dominated by the nearly unit-root domestic risk premium shock.

<!-- kind: inline; id: 97.i20; section: 6.1; page: 68; pdf_page: 74 -->
**(97.i20) Deflator used to stationarize the real variables of Table 7**

$$
z_{t}
$$

Meaning: Before the decomposition, real variables are made stationary by dividing them by the labour-augmenting productivity level $z_{t}$ (introduced with equation 17).

**Main findings (own words; percentages from Table 7):**

- **CPI inflation ($\Delta P_{C}$).** Main contributors: the external premium shock, via the exchange rate (33–38% across the three horizons); the domestic and import markup shocks (14–21% and 16–23%); and, at 4 quarters and ∞, the oil price shock (8.7% and 11.5%). These shocks contribute little to output, its main components or hours worked.
- **Output ($\hat{y}$).** At one quarter, demand-type shocks lead: home bias 24%, change in inventories 22%, export share (demand for Israeli exports) 17%, symmetric premium (domestic demand) 11%. At the infinite horizon, technology dominates: transitory technology 36% and investment-specific technology 19%. The latter works both through investment demand and through the capital stock's effect on supply.
- **Imports ($\widehat{im}$).** Demand shocks dominate. At one quarter: home bias 33% (it changes the import intensity of final goods), inventory demand 18% (inventories are volatile and import-intensive), symmetric premium 14%, export share 13%. The symmetric premium shock moves domestic demand, part of which falls on imports, and it also moves import demand through domestic prices and, via the exchange rate, import prices. At the infinite horizon: symmetric premium 22.5%, foreign demand 18%, export share 17%. Higher export demand raises imports for two reasons: exports use imported inputs, and higher net exports appreciate the currency (through the external risk premium), which makes imports cheaper relative to domestic output. Footnote 48 adds that foreign demand also moves import demand through foreign prices, and hence import prices.
- **Real exchange rate ($\hat{s}$).** Its long-run variance reflects its two-way link with trade flows. Five shocks contribute more than 10% at the infinite horizon. Three of them are also the main drivers of exports and imports (symmetric premium, export share, foreign demand). The remaining two are transitory technology (19%; it works through domestic prices $p_{H,t}$ and the nominal exchange rate, see 6.2) and the external premium shock (13%; it moves the nominal exchange rate directly). At one quarter the external premium shock dominates (56%).
- **Labour market ($\hat{w}$, $\hat{N}$), infinite horizon.** Main sources: transitory technology (10.0% / 20.2%), symmetric premium (11.1% / 8.0%), export share (8.2% / 11.2%), foreign demand (10.2% / 9.0%) and wage markup (24.2% / 9.4%). All except the wage markup shift labour demand; the wage markup acts like a shift in labour supply. At one quarter the wage markup explains 66% of the real-wage variance, and transitory technology explains 38% of hours worked.
- **Nominal interest rate ($r^{OB}$).** At the infinite horizon, 75% of its variance is due to the domestic premium shock. This very persistent shock determines the long-run real rate, which varies over time. It dominates because it is assumed to be close to a unit root (AR coefficient 0.99); at short horizons its share is negligible. At one quarter the policy-rule deviation (interest-rate shock, 56%) and the external premium shock (26%, which moves the rate through the rule's reaction to inflation and depreciation) dominate.

#### Table 7: Forecast Error Variance Decompostion (one-quarter, four-quarter and infinite horizon)

- Title as printed (the misspelling "Decompostion" is in the original; part 2 adds "(cont.)").
- The table is printed rotated 90° (landscape). Part 1: page 69, pdf_page 75. Part 2: page 70, pdf_page 76.
- Entries: percentage of each variable's forecast-error variance due to each shock. The horizon columns are 1, 4 and ∞ quarters (printed as "1", "4", "∞"). No units or table note are printed. Every variable–horizon column sums to between 99.7 and 100.1 (rounding).
- Rows: the 25 structural shocks of Section 4.4.2, with the innovation symbol printed in the table. There are no rows for the observation-equation shocks.
- Machine-readable copy: `data/table7_variance_decomposition.csv`, one row per variable × shock, with columns pdf_page, page, variable, variable_symbol, shock, shock_symbol, h1, h4, h_inf.

**Part 1 (page 69; pdf_page 75).** Column groups: Interest rate $r^{OB}$ | Inflation $\Delta P_{C}$ | Real exchange rate $\hat{s}$ | Real wage $\hat{w}$ | Hours worked $\hat{N}$.

| Shock | Symbol | $r^{OB}$ 1 | $r^{OB}$ 4 | $r^{OB}$ $\infty$ | $\Delta P_{C}$ 1 | $\Delta P_{C}$ 4 | $\Delta P_{C}$ $\infty$ | $\hat{s}$ 1 | $\hat{s}$ 4 | $\hat{s}$ $\infty$ | $\hat{w}$ 1 | $\hat{w}$ 4 | $\hat{w}$ $\infty$ | $\hat{N}$ 1 | $\hat{N}$ 4 | $\hat{N}$ $\infty$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Transitory techn. | $\eta$ | 2.6 | 7.2 | 2.1 | 4.1 | 4.1 | 4.1 | 12.1 | 24.9 | 19.0 | 0.3 | 1.5 | 10.0 | 37.9 | 23.8 | 20.2 |
| Permanent techn. | $\eta^{g_{z}}$ | 0.0 | 0.0 | 0.2 | 0.0 | 0.0 | 0.3 | 0.0 | 0.2 | 0.5 | 0.3 | 0.8 | 2.6 | 0.1 | 0.5 | 1.4 |
| Symmetric prem. | $\eta^{RP}$ | 0.7 | 5.5 | 3.7 | 0.5 | 1.2 | 1.1 | 4.0 | 10.1 | 12.6 | 5.9 | 13.6 | 11.1 | 7.3 | 9.3 | 8.0 |
| External prem. | $\eta^{RP^{*}}$ | 25.8 | 42.9 | 7.0 | 37.7 | 35.1 | 33.0 | 55.7 | 24.6 | 13.0 | 8.4 | 7.9 | 5.0 | 1.5 | 3.2 | 2.7 |
| Dom. prem. | $\eta^{DRP}$ | 0.6 | 2.3 | 75.5 | 0.2 | 0.3 | 0.3 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | 0.4 | 0.0 | 0.1 | 0.1 |
| Consumption | $\eta^{C}$ | 0.1 | 0.5 | 0.3 | 0.0 | 0.0 | 0.1 | 0.3 | 0.6 | 0.4 | 0.0 | 0.1 | 1.1 | 2.2 | 3.7 | 3.4 |
| Inv. techn. | $\eta^{I}$ | 0.1 | 0.3 | 0.7 | 0.0 | 0.1 | 2.6 | 0.0 | 0.1 | 8.2 | 0.0 | 0.1 | 6.4 | 2.1 | 2.5 | 4.3 |
| Inventory inv. | $\eta^{\Delta INV}$ | 0.9 | 1.4 | 0.4 | 0.1 | 0.1 | 0.1 | 0.4 | 0.4 | 0.4 | 0.1 | 0.0 | 1.1 | 14.8 | 9.6 | 7.9 |
| Government | $\eta^{G}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.5 | 0.3 | 0.3 |
| Export share | $\eta^{\nu^{*}}$ | 0.0 | 0.0 | 0.3 | 0.2 | 0.5 | 0.8 | 6.3 | 12.3 | 11.8 | 1.6 | 5.3 | 8.2 | 11.0 | 13.1 | 11.2 |
| Home bias | $\eta^{\nu}$ | 0.2 | 0.1 | 0.2 | 0.1 | 0.3 | 0.5 | 2.6 | 5.4 | 5.6 | 1.0 | 2.9 | 4.4 | 15.6 | 11.0 | 9.2 |
| Domestic markup | $\eta^{H}$ | 1.5 | 2.6 | 0.4 | 20.6 | 15.5 | 13.7 | 4.7 | 3.1 | 1.6 | 8.0 | 6.4 | 3.5 | 1.6 | 3.6 | 3.1 |
| Import markup | $\eta^{*}$ | 2.1 | 2.9 | 0.4 | 22.9 | 18.0 | 15.8 | 0.0 | 0.2 | 0.1 | 6.3 | 2.7 | 1.4 | 0.8 | 0.6 | 0.5 |
| Wage markup | $\eta^{W}$ | 0.6 | 2.8 | 0.6 | 4.6 | 5.5 | 4.8 | 3.0 | 6.2 | 3.8 | 66.4 | 49.5 | 24.2 | 0.9 | 6.8 | 9.4 |
| Export markup | $\eta^{X}$ | 0.0 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 | 2.7 | 0.8 | 0.4 | 0.1 | 0.2 | 0.1 | 1.0 | 2.0 | 1.7 |
| Foreign transfers | $\eta^{FTR}$ | 0.1 | 0.6 | 0.4 | 0.2 | 0.3 | 0.4 | 0.4 | 0.9 | 1.4 | 0.2 | 0.8 | 2.7 | 0.0 | 0.0 | 0.2 |
| Interest rate | $\eta^{R}$ | 56.5 | 17.1 | 2.5 | 6.0 | 7.6 | 6.6 | 3.7 | 1.9 | 0.9 | 0.2 | 0.1 | 0.1 | 0.9 | 2.0 | 1.7 |
| Inf. target | $\eta^{\bar{\Pi}}$ | 6.4 | 2.3 | 0.5 | 0.3 | 0.6 | 0.8 | 0.6 | 0.4 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.3 | 0.2 |
| Consumption tax | $\eta^{\tau^{C}}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.8 | 0.0 | 0.0 | 1.3 |
| Foreign demand | $\eta^{Y^{*}}$ | 0.1 | 2.8 | 2.4 | 0.2 | 1.0 | 1.8 | 1.0 | 4.9 | 14.0 | 0.2 | 1.5 | 10.2 | 0.4 | 6.1 | 9.0 |
| Foreign supply | $\eta^{\Pi^{*}}$ | 0.2 | 0.5 | 0.1 | 0.4 | 0.4 | 0.5 | 1.0 | 0.8 | 1.0 | 0.1 | 0.2 | 0.5 | 0.1 | 0.2 | 0.4 |
| Foreign interest rate | $\eta^{R^{*}}$ | 0.2 | 0.3 | 0.2 | 0.3 | 0.3 | 0.4 | 1.0 | 1.8 | 3.2 | 0.2 | 0.7 | 2.0 | 0.0 | 0.3 | 0.9 |
| World trade | $\eta^{WT^{*}}$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.8 | 0.4 | 0.3 |
| Oil price | $\eta^{OIL}$ | 1.1 | 6.6 | 1.3 | 1.5 | 8.7 | 11.5 | 0.0 | 0.2 | 0.5 | 0.6 | 5.0 | 2.9 | 0.1 | 0.5 | 2.2 |
| Foreign LR rate | $\eta^{*,fwd}$ | 0.1 | 0.9 | 0.7 | 0.2 | 0.4 | 0.6 | 0.1 | 0.2 | 1.0 | 0.1 | 0.4 | 1.1 | 0.0 | 0.1 | 0.4 |

**Part 2 (page 70; pdf_page 76).** Column groups: Output $\hat{y}$ | Consumption $\hat{c}$ | Investment $\hat{i}$ | Exports $\hat{x}$ | Imports $\hat{im}$. In this header the imports symbol has a narrow hat centred over "im"; the text on page 71 prints a wide hat, $\widehat{im}$.

| Shock | Symbol | $\hat{y}$ 1 | $\hat{y}$ 4 | $\hat{y}$ $\infty$ | $\hat{c}$ 1 | $\hat{c}$ 4 | $\hat{c}$ $\infty$ | $\hat{i}$ 1 | $\hat{i}$ 4 | $\hat{i}$ $\infty$ | $\hat{x}$ 1 | $\hat{x}$ 4 | $\hat{x}$ $\infty$ | $\hat{im}$ 1 | $\hat{im}$ 4 | $\hat{im}$ $\infty$ |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Transitory techn. | $\eta$ | 6.5 | 28.7 | 36.4 | 1.4 | 3.5 | 9.4 | 1.5 | 2.8 | 7.0 | 0.5 | 3.8 | 6.2 | 0.8 | 1.6 | 2.2 |
| Permanent techn. | $\eta^{g_{z}}$ | 0.0 | 0.1 | 1.1 | 0.2 | 0.3 | 3.3 | 0.5 | 1.1 | 1.8 | 0.0 | 0.0 | 0.2 | 0.0 | 0.1 | 0.2 |
| Symmetric prem. | $\eta^{RP}$ | 11.0 | 9.3 | 5.7 | 55.9 | 55.6 | 34.8 | 33.6 | 28.4 | 20.8 | 0.2 | 1.5 | 4.3 | 14.2 | 23.4 | 22.5 |
| External prem. | $\eta^{RP^{*}}$ | 2.3 | 2.7 | 1.6 | 1.9 | 4.2 | 3.6 | 2.0 | 2.0 | 2.5 | 1.2 | 2.6 | 2.1 | 6.0 | 6.4 | 5.0 |
| Dom. prem. | $\eta^{DRP}$ | 0.0 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Consumption | $\eta^{C}$ | 3.3 | 3.3 | 2.0 | 36.4 | 28.7 | 16.5 | 0.4 | 0.7 | 1.9 | 0.0 | 0.1 | 0.1 | 2.2 | 2.8 | 2.1 |
| Inv. techn. | $\eta^{I}$ | 3.2 | 4.8 | 18.7 | 0.5 | 1.0 | 8.9 | 58.2 | 58.6 | 41.0 | 0.0 | 0.0 | 3.8 | 2.2 | 2.3 | 2.6 |
| Inventory inv. | $\eta^{\Delta INV}$ | 22.4 | 8.5 | 4.4 | 0.4 | 0.9 | 2.0 | 0.4 | 0.7 | 1.6 | 0.0 | 0.0 | 0.1 | 17.9 | 7.4 | 4.7 |
| Government | $\eta^{G}$ | 0.8 | 0.3 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Export share | $\eta^{\nu^{*}}$ | 16.6 | 11.8 | 6.4 | 0.0 | 0.2 | 3.5 | 0.3 | 0.8 | 4.0 | 76.0 | 42.4 | 23.5 | 13.0 | 18.3 | 16.9 |
| Home bias | $\eta^{\nu}$ | 23.6 | 9.9 | 5.1 | 0.0 | 0.1 | 1.7 | 0.1 | 0.4 | 1.9 | 0.1 | 0.9 | 2.1 | 33.3 | 13.7 | 8.3 |
| Domestic markup | $\eta^{H}$ | 2.4 | 3.2 | 1.6 | 0.3 | 0.5 | 0.3 | 0.2 | 0.2 | 0.1 | 0.1 | 0.3 | 0.2 | 0.9 | 0.5 | 0.4 |
| Import markup | $\eta^{*}$ | 1.3 | 0.5 | 0.3 | 0.5 | 0.6 | 0.3 | 0.3 | 0.2 | 0.1 | 0.1 | 0.3 | 0.2 | 5.6 | 3.1 | 1.9 |
| Wage markup | $\eta^{W}$ | 1.4 | 6.2 | 5.2 | 0.1 | 0.5 | 1.0 | 0.2 | 0.4 | 0.7 | 0.1 | 0.9 | 1.0 | 0.4 | 0.7 | 0.7 |
| Export markup | $\eta^{X}$ | 1.6 | 1.8 | 0.9 | 0.0 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | 8.6 | 7.8 | 4.4 | 1.0 | 1.5 | 0.9 |
| Foreign transfers | $\eta^{FTR}$ | 0.0 | 0.0 | 0.6 | 0.3 | 0.7 | 2.7 | 0.5 | 0.9 | 2.7 | 0.0 | 0.2 | 0.6 | 0.2 | 0.8 | 2.1 |
| Interest rate | $\eta^{R}$ | 1.4 | 1.8 | 0.9 | 1.2 | 0.7 | 0.4 | 0.3 | 0.2 | 0.1 | 0.1 | 0.2 | 0.1 | 0.0 | 0.0 | 0.1 |
| Inf. target | $\eta^{\bar{\Pi}}$ | 0.2 | 0.2 | 0.1 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Consumption tax | $\eta^{\tau^{C}}$ | 0.0 | 0.0 | 0.2 | 0.0 | 0.0 | 0.7 | 0.0 | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Foreign demand | $\eta^{Y^{*}}$ | 0.6 | 5.4 | 5.5 | 0.1 | 0.3 | 6.7 | 0.3 | 0.3 | 8.5 | 7.0 | 31.8 | 37.1 | 1.1 | 8.1 | 18.1 |
| Foreign supply | $\eta^{\Pi^{*}}$ | 0.2 | 0.2 | 0.2 | 0.0 | 0.1 | 0.2 | 0.0 | 0.0 | 0.2 | 0.4 | 0.2 | 1.2 | 0.0 | 0.2 | 0.9 |
| Foreign interest rate | $\eta^{R^{*}}$ | 0.0 | 0.2 | 0.6 | 0.0 | 0.0 | 0.9 | 0.0 | 0.0 | 1.0 | 0.2 | 2.2 | 4.4 | 0.3 | 1.7 | 3.7 |
| World trade | $\eta^{WT^{*}}$ | 1.2 | 0.3 | 0.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 4.8 | 0.9 | 0.4 | 0.5 | 0.2 | 0.1 |
| Oil price | $\eta^{OIL}$ | 0.1 | 0.5 | 1.2 | 0.2 | 1.1 | 1.0 | 0.4 | 0.6 | 0.7 | 0.2 | 2.3 | 4.3 | 0.4 | 7.2 | 5.8 |
| Foreign LR rate | $\eta^{*,fwd}$ | 0.0 | 0.1 | 0.8 | 0.3 | 0.7 | 1.9 | 0.7 | 1.5 | 3.1 | 0.2 | 1.6 | 3.5 | 0.1 | 0.1 | 0.7 |

### 6.2 Impulse response functions

pages 73–83; pdf_pages 79–89 (figure pages: 74, 76, 78, 80, 82 = pdf_pages 80, 82, 84, 86, 88; footnote 49 on page 73, footnote 50 on page 83).

**Summary.** Figures 6–10 show Bayesian impulse responses of twelve key variables to five shocks: monetary policy ($\eta^{R}$), external risk premium ($\eta^{RP^{*}}$), symmetric premium ($\eta^{RP}$), foreign demand ($\eta^{Y^{*}}$) and transitory technology ($\eta$). The text explains each transmission mechanism and compares the monetary-policy responses with similar estimated models. Footnote 49 refers to Appendix E for further shocks. Section 6.2 and Appendix E together show impulse responses for 13 of the 25 shocks; the paper shows none for the other 12 ($\eta^{g_{z}}$, $\eta^{DRP}$, $\eta^{C}$, $\eta^{G}$, $\eta^{X}$, $\eta^{FTR}$, $\eta^{\bar{\Pi}}$, $\eta^{\tau^{C}}$, $\eta^{\Pi^{*}}$, $\eta^{R^{*}}$, $\eta^{WT^{*}}$, $\eta^{*,fwd}$).

**How the responses are computed (own words, page 73):**

- The bands are Bayesian. They reflect uncertainty about both the shock's size (its standard deviation) and the model parameters.
- Size uncertainty: instead of a single fixed shock, shock sizes are drawn according to the posterior of each shock's standard deviation.
- Parameter uncertainty: the response distribution follows the posterior simulation draws of the parameters. A response is computed for every draw of the posterior simulation of Section 4.5.
- Each figure plots the mean response over draws, together with the 70% and 90% highest-probability intervals.
- Units: real variables in percent deviation from the model's steady state; inflation measures in percentage-point deviations; interest rates in annualized percentage-point deviations.

**Common format of Figures 6–18.** These points hold for every impulse-response figure in this chunk (6–10 here and 11–18 in Appendix E); each figure section below repeats the essentials. The visible caption is identical on all 13 figure pages.

- **Layout.** One boxed figure with 12 panels in 4 rows × 3 columns, in this order (titles as printed): row 1 Output, Consumption, Fixed investment; row 2 Exports, Imports, Hours worked; row 3 Interest rate, Real wage, Real exchange rate; row 4 CPI inflation, Domestic inflation, Imported inflation.
- **Shock size (caption).** A shock of one standard deviation.
- **Lines (caption wording).** Solid line: "mean of impulse response". Gray area: "70 and 90 percent highest interval of impulse response". There are two nested gray shades, a darker inner band and a lighter outer band. The caption does not say which is which; the nesting implies inner = 70% and outer = 90%. A thin horizontal line marks zero.
- **Units (paraphrasing the caption).** Real variables are in percent deviation from the steady state, inflation rates in percentage-point deviation, and the interest rate in annualized percentage points. The y-axes carry no unit label; each panel has its own y-range (listed below).
- **Horizon.** The x-axis has ticks 0, 10, 20 and no axis title; the text speaks of quarters. The mean line has vertices at x = 1, 2, …, 20 (checked in the PDF vector paths), so **x = 1 is the impact quarter** and 20 quarters are shown.
- **Sign convention (from the text).** A positive real exchange rate is a real depreciation. For example, the policy shock in Figure 6 appreciates the currency and the panel is negative; the external premium shock in Figure 7 depreciates it and the panel is positive.
- In the panel tables below, "Reading" describes the solid mean line. **All numbers in the readings are approximate** (rounded); exact values are left to the chart digitizer. "y-axis (printed)" gives the lowest and highest tick labels printed on the panel.

#### Figure 6: Impulse Response to an Interest Rate Shock

page 74; pdf_page 80. Discussed on pages 73–75 (pdf_pages 79–81).

- **Shock:** monetary policy shock, the one-standard-deviation innovation $\eta^{R}$ to the interest-rate rule (62); in Section 4.4.2 this shock is i.i.d.
- **Stated size:** one standard deviation (caption). The text says it raises the policy rate by about 0.75 percentage points at once.
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).

**Transmission described in the text (own words):**

- Prices and wages are sticky, so the real rate rises too. Consumption and investment fall, for about two years.
- The higher rate appreciates the currency. Exporters, who have market power, gradually raise their foreign-currency prices, so exports fall, to about 0.2% below steady state.
- Imports face two opposite forces. Weaker domestic demand cuts demand for imported intermediate goods, while the appreciation shifts spending toward imports (expenditure switching). The switching force mostly dominates in the short run.
- Output falls by about 0.2%, because the demand contraction and expenditure switching both lower domestic activity. The trough comes after two quarters; output returns to trend in under two years.
- Inflation drops at once; summed over the first year the decline is about 0.4 pp. Two forces are at work: the appreciation lowers imported inflation directly, and marginal costs (wages and capital rental rates) fall. Marginal costs fall both because activity contracts and because the appreciation moderates wage demands. After weighting each component's response by its CPI weight, domestic and imported inflation contribute about equally to the fall in CPI inflation.
- Comparison with similar models (euro area: Christoffel et al. 2008 and Adolfson et al. 2007; Sweden: Adolfson et al. 2008; New Zealand: Beneš et al. 2009):
  1. MOISE's shock is 1.5–3 times larger, because the estimated standard deviation of its policy shock is larger.
  2. The output effect is smaller, mainly because investment is less sensitive. The inflation effect is larger, because exchange-rate pass-through is faster and import intensity is high.
  3. Output reacts faster and with less of a hump: its strongest effect comes after two quarters in MOISE, versus three to four quarters elsewhere.
  4. The effect lasts about two years, versus about five years elsewhere.

**Panels (mean line; all values approximate):**

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.3 to 0.1 | Falls; ≈ -0.18 on impact, trough ≈ -0.23 at x = 2; close to zero (≈ -0.01) from x ≈ 8 onward. |
| 2 | Consumption | -0.4 to 0 | Falls; trough ≈ -0.19 at x = 2; ≈ -0.05 by x = 6, then slow; ≈ -0.02 at x = 20. |
| 3 | Fixed investment | -0.4 to 0 | Largest fall on impact (≈ -0.20); uneven partial rebound (≈ -0.14 at x = 2, ≈ -0.16 at x = 3), then slow steady recovery; ≈ -0.03 at x = 20. |
| 4 | Exports | -0.4 to 0.4 | Falls; trough ≈ -0.23 at x = 3; crosses zero at x ≈ 8–9; small positive overshoot (≈ +0.02) around x ≈ 10–14; ≈ 0 at x = 20. |
| 5 | Imports | -0.2 to 0.2 | Small initial rise (peak ≈ +0.06 at x = 2), negative from x ≈ 4; trough ≈ -0.07 at x ≈ 6–8; ≈ -0.01 at x = 20. |
| 6 | Hours worked | -0.4 to 0.4 | Falls; trough ≈ -0.27 at x = 2; ≈ 0 by x ≈ 9. |
| 7 | Interest rate | -0.5 to 1 | Jumps to ≈ +0.78 on impact (text: 0.75 pp); ≈ +0.17 at x = 3; ≈ 0 from x ≈ 5 (tiny dip ≈ -0.02 at x ≈ 6). |
| 8 | Real wage | -0.05 to 0.15 | Rises ≈ +0.05 at x = 1–2; crosses zero at x ≈ 4–5; trough ≈ -0.02 at x ≈ 7–8; ≈ -0.01 at x = 20. |
| 9 | Real exchange rate | -0.6 to 0.2 | Appreciates (negative); ≈ -0.43 on impact, trough ≈ -0.44 at x = 2; crosses zero at x ≈ 5–6; small overshoot ≈ +0.04 at x ≈ 7–9; ≈ 0 at x = 20. |
| 10 | CPI inflation | -0.3 to 0.1 | Largest drop on impact (≈ -0.17); ≈ -0.07 at x = 3; ≈ 0 from x ≈ 5. Sum over x = 1–4 ≈ -0.41 (text: about 0.4 pp after one year). |
| 11 | Domestic inflation | -0.15 to 0.05 | Falls; trough ≈ -0.11 at x = 2; ≈ 0 by x ≈ 7–8. |
| 12 | Imported inflation | -0.4 to 0.4 | Largest drop on impact (≈ -0.33); crosses zero between x = 3 and 4; overshoot peak ≈ +0.07 at x = 5; ≈ 0 by x ≈ 9. |

#### Figure 7: Impulse Response to an External Risk Premium Shock

page 76; pdf_page 82. Discussed on pages 75–77 (pdf_pages 81–83).

- **Shock:** external risk premium shock, innovation $\eta_{t}^{RP^{*}}$. The text notes that it is usually called an exchange-rate (UIP) shock (Section 3.1).
- **Stated size:** one standard deviation (caption). According to the text it causes an immediate nominal depreciation of 2.3% (the nominal exchange rate is not plotted) and a policy-rate rise of 0.5 pp on impact.
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).

**Transmission described in the text (own words):**

- A higher external premium makes domestic-currency bonds less attractive than foreign-currency bonds. Equal expected returns are restored by an immediate nominal depreciation (2.3%) together with a higher domestic interest rate.
- The depreciation pushes up CPI inflation directly, via the cost of imported intermediate inputs; on impact the CPI responds to the depreciation with an elasticity of 0.18.
- The real depreciation improves the current account: exports rise (text: by roughly 0.5%) and imports fall. In other words, expenditure switching is stronger than the direct effect that the depreciation itself has on the current account.
- Domestic demand components fall, because of the higher real rate and dearer imports. Output nevertheless rises, by about 0.3%, because of expenditure switching.
- Higher inflation, higher output and the depreciation lead to a rate hike: +0.5 pp on impact, rising to 1.0 pp within three quarters (text).
- The depreciation is short-lived; the real exchange rate is back at its initial level within two years.
- Domestic inflation also rises, much less than imported inflation, because marginal cost rises. The text gives four reasons:
  1. Higher activity changes marginal productivity and input costs.
  2. The depreciation raises wage and rental demands: measured against the CPI (which contains import prices), wages and rental rates first drop.
  3. Lower investment creates a capital shortage, which raises the rental rate further.
  4. The higher nominal rate raises wage-bill costs through the working-capital channel (Section 3.2.1).

**Panels (mean line; all values approximate):**

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.2 to 0.6 | Expands; ≈ +0.22 on impact, peak ≈ +0.32 at x = 2 (text: about 0.3%); ≈ 0 at x = 5; mild undershoot ≈ -0.06 at x ≈ 7–8; ≈ 0 by x ≈ 18. |
| 2 | Consumption | -1 to 0.5 | Falls; trough ≈ -0.48 at x = 3; crosses zero at x ≈ 8; positive hump ≈ +0.15 at x ≈ 12–15; ≈ +0.11 at x = 20. |
| 3 | Fixed investment | -2 to 1 | Falls; trough ≈ -0.68 at x = 3; crosses zero at x ≈ 7–8; rises to ≈ +0.49 at x ≈ 15–17; ≈ +0.45 at x = 20. |
| 4 | Exports | -0.5 to 1.5 | Rises; ≈ +0.39 on impact, peak ≈ +0.79 at x = 3 (text: approximately 0.5%); crosses zero at x ≈ 7–8; undershoot ≈ -0.24 at x ≈ 13–15; ≈ -0.18 at x = 20. |
| 5 | Imports | -1.5 to 0.5 | Falls; trough ≈ -0.98 at x = 2; crosses zero at x ≈ 6–7; positive ≈ +0.28 at x ≈ 13–14; ≈ +0.21 at x = 20. |
| 6 | Hours worked | -0.2 to 0.6 | Rises; peak ≈ +0.37 at x = 2; crosses zero at x ≈ 5–6; small undershoot ≈ -0.04 at x = 7; ≈ -0.01 afterwards. |
| 7 | Interest rate | -0.5 to 1.5 | Rises to ≈ +0.51 on impact (text: 0.5 pp); peak ≈ +0.85 at x = 3 (text: up to 1.0 pp within three quarters); crosses zero at x ≈ 7–8; small undershoot ≈ -0.07 at x ≈ 10–13; ≈ -0.04 at x = 20. |
| 8 | Real wage | -0.6 to 0.2 | Falls; trough ≈ -0.41 at x = 2; crosses zero at x ≈ 6–7; positive plateau ≈ +0.09 over x ≈ 11–17; ≈ +0.07 at x = 20. |
| 9 | Real exchange rate | -1 to 2 | Sharp depreciation on impact (≈ +1.66, the maximum), then a fast decline; crosses zero at x ≈ 5–6; undershoot ≈ -0.25 at x ≈ 12–13; ≈ -0.15 at x = 20. |
| 10 | CPI inflation | -0.2 to 0.6 | Jumps to ≈ +0.43 on impact; ≈ 0 at x = 3; undershoot ≈ -0.10 at x ≈ 4–5; ≈ 0 by x ≈ 10. |
| 11 | Domestic inflation | -0.1 to 0.3 | Rises; ≈ +0.10 on impact, peak ≈ +0.13 at x = 2; ≈ 0 by x ≈ 6; ≈ -0.01 over x ≈ 15–20. |
| 12 | Imported inflation | -0.5 to 1.5 | Jumps to ≈ +1.0 on impact; crosses zero between x = 2 and 3; trough ≈ -0.37 at x = 4; ≈ 0 by x ≈ 12. |

#### Figure 8: Impulse Response to a Symmetric Premium Shock

page 78; pdf_page 84. Discussed on pages 77–79 (pdf_pages 83–85).

- **Shock:** symmetric risk premium shock, innovation $\eta^{RP}$ (positive shock).
- **Stated size:** one standard deviation (caption). The text gives no impact size for the premium itself.
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).

**Transmission described in the text (own words):**

- A positive shock makes risk-free financial assets (both domestic- and foreign-currency bonds) more attractive relative to real spending, so it acts as a domestic demand shock.
- Consumption and fixed investment fall on impact, by about 1% and 2%.
- Lower domestic final uses cut demand for domestic output (about -0.5%) and for imports (about -1.5%). Imports fall more because of expenditure switching.
- The resulting slack lowers domestic costs and inflation (by 0.2 pp over the first year).
- Facing lower inflation and output, the central bank cuts the policy rate gradually. The resulting depreciation causes expenditure switching, which explains why imports bear more of the contraction, and a gradual rise in exports of up to 0.7%.
- The effects last about ten quarters.

**Panels (mean line; all values approximate):**

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.8 to 0 | Largest fall on impact (≈ -0.48; text: about 0.5%); recovers to ≈ -0.13 by x ≈ 8 and stays near there to x ≈ 14; ≈ -0.08 at x = 20 (not back to zero within the window). |
| 2 | Consumption | -2 to 1 | Falls ≈ -1.1 on impact (text: about 1%), trough ≈ -1.44 at x = 2–3; crosses zero at x ≈ 11–12; overshoot ≈ +0.19 at x ≈ 18; ≈ +0.18 at x = 20. |
| 3 | Fixed investment | -4 to 2 | Falls ≈ -1.9 on impact (text: about 2%), trough ≈ -2.35 at x = 3; crosses zero at x ≈ 12–13; still rising at x = 20 (≈ +0.96). |
| 4 | Exports | -1 to 2 | Gradual rise, peak ≈ +0.70 at x = 5 (text: up to 0.7%); crosses zero at x ≈ 10–11; undershoot ≈ -0.50 at x ≈ 18–19. |
| 5 | Imports | -3 to 1 | Falls; trough ≈ -1.64 at x = 3 (text: about 1.5%); crosses zero at x ≈ 10–11; overshoot ≈ +0.49 at x ≈ 18–19. |
| 6 | Hours worked | -1 to 0.5 | Largest fall on impact (≈ -0.55); ≈ 0 from x ≈ 8. |
| 7 | Interest rate | -0.8 to 0 | Gradual cut: ≈ -0.09 on impact, trough ≈ -0.37 at x = 5; slow return, ≈ -0.11 at x = 20. |
| 8 | Real wage | -1 to 0.5 | Falls; trough ≈ -0.48 at x = 3; crosses zero at x ≈ 10–11; ≈ +0.13 over x ≈ 17–20. |
| 9 | Real exchange rate | -1 to 2 | Depreciates; peak ≈ +0.92 at x = 3–4; crosses zero at x ≈ 9–10; appreciation ≈ -0.51 at x ≈ 16–18; ≈ -0.47 at x = 20. |
| 10 | CPI inflation | -0.1 to 0.1 | Small fall; trough ≈ -0.055 at x = 2; ≈ 0 by x ≈ 7, tiny positive (≈ +0.003) afterwards. Sum over x = 1–4 ≈ -0.17 (text: 0.2 pp during the first year). |
| 11 | Domestic inflation | -0.4 to 0.4 | Falls ≈ -0.18 at x = 1–2; crosses zero at x ≈ 4–5; positive hump ≈ +0.07 at x ≈ 7–9; ≈ 0 by x ≈ 17. |
| 12 | Imported inflation | -0.2 to 0.6 | Rises to ≈ +0.20 on impact; crosses zero at x ≈ 3–4; trough ≈ -0.14 at x ≈ 7–8; ≈ 0 by x ≈ 17; ≈ +0.02 at x = 20. |

#### Figure 9: Impulse Response to a Foreign Demand Shock

page 80; pdf_page 86. Discussed on pages 79–81 (pdf_pages 85–87).

- **Shock:** foreign demand shock, innovation $\eta^{Y^{*}}$ (positive shock).
- **Stated size:** one standard deviation (caption). According to the text it raises foreign output by 0.6% and world trade by 2% (neither is plotted).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).

**Transmission described in the text (own words):**

- A positive shock moves the foreign IS curve (equation 89) up, so foreign output rises by 0.6%. The variance decomposition shows it is the foreign shock that matters most for the domestic real economy.
- There are three channels:
  1. World trade expands by 2% (equation 91), raising demand for exports; the text puts the export rise at roughly 2%.
  2. Higher foreign output creates foreign inflation (equation 92), which raises importers' marginal costs (equation 30).
  3. Foreign output and inflation trigger a foreign interest-rate rise of 0.5 pp within a year (equation 94).
- The initially wider gap between foreign and domestic rates pushes toward depreciation. Yet the real exchange rate appreciates, because the current-account surplus raises net foreign assets and lowers the external risk premium.
- Net effect: domestic output rises (peak about 0.4%), inflation rises (0.2 pp in the first year), and policy tightens (the rate goes up by about 0.3 pp within a year).
- The tightening first lowers consumption and investment. After about two years a positive income effect dominates and both rise above their steady-state levels.

**Panels (mean line; all values approximate):**

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.2 to 0.6 | Rises; peak ≈ +0.40 at x = 3–4 (text: about 0.4% at the peak); crosses zero at x ≈ 10–11; mild undershoot ≈ -0.06 at x ≈ 13–15; ≈ 0 at x = 20. |
| 2 | Consumption | -0.5 to 0.5 | Initial dip, trough ≈ -0.14 at x ≈ 4–5; crosses zero at x ≈ 8–9; rises to ≈ +0.33 at x ≈ 17–18; ≈ +0.31 at x = 20. |
| 3 | Fixed investment | -1 to 2 | Initial fall, trough ≈ -0.30 at x = 3; crosses zero at x ≈ 7–8; rises to ≈ +1.06 at x ≈ 17–18; ≈ +1.0 at x = 20. |
| 4 | Exports | -2 to 4 | Strong rise; ≈ +0.9 on impact, peak ≈ +2.8 at x = 4 (text: approximately 2%); crosses zero at x ≈ 11–12; undershoot ≈ -0.77 at x ≈ 17. |
| 5 | Imports | 0 to 2 | Rises; peak ≈ +1.16 at x = 5; slow decline; still ≈ +0.35 at x = 20 (positive throughout). |
| 6 | Hours worked | -0.2 to 0.6 | Rises; peak ≈ +0.46 at x = 3–4; crosses zero at x ≈ 10–11; undershoot ≈ -0.10 at x ≈ 15–16. |
| 7 | Interest rate | -0.2 to 0.6 | Gradual rise; peak ≈ +0.32 at x = 5–6 (text: about 0.3 pp within a year); crosses zero at x ≈ 12–13; ≈ -0.14 over x ≈ 18–20. |
| 8 | Real wage | 0 to 0.4 | Rises gradually; peak ≈ +0.25 at x ≈ 8–9; slow decline; ≈ +0.17 at x = 20. |
| 9 | Real exchange rate | -1.5 to 0 | Appreciates; trough ≈ -0.88 at x ≈ 6–7; slow return; ≈ -0.23 at x = 20. |
| 10 | CPI inflation | -0.05 to 0.15 | Rises; peak ≈ +0.05 at x = 2–3; crosses zero at x ≈ 6–7; undershoot ≈ -0.022 at x ≈ 11–12; ≈ -0.012 at x = 20. Sum over x = 1–4 ≈ +0.17 (text: 0.2 pp in the first year). |
| 11 | Domestic inflation | -0.1 to 0.3 | Rises; peak ≈ +0.12 at x = 2; crosses zero at x ≈ 7; undershoot ≈ -0.04 over x ≈ 10–15; ≈ -0.02 at x = 20. |
| 12 | Imported inflation | -0.2 to 0.2 | Falls to ≈ -0.08 at x = 1–2; ≈ 0 by x ≈ 8–9; tiny positive (≈ +0.01) afterwards. |

#### Figure 10: Impulse Response to a Transitory Technology Shock

page 82; pdf_page 88. Discussed on pages 81–83 (pdf_pages 87–89).

- **Shock:** transitory technology shock: a temporary increase in total factor productivity $\varepsilon_{t}$ (equation 17), driven by the innovation $\eta$.
- **Stated size:** one standard deviation (caption). According to the text the shock peaks on impact and then decays, with persistence 0.86.
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).

**Transmission described in the text (own words):**

- The text splits the response into a short run with excess supply and a medium run with excess demand.
- **Short run, supply side.** Given inputs can now produce more output. But with nominal frictions and a central bank that operates in the credit market, output is determined by demand. Demand rises, but by less than the direct supply effect. Because capital is predetermined, the capital rental cost and hours worked fall: technology replaces labour.
- **Short run, costs and inflation.** Marginal cost falls for three reasons: the direct productivity effect, the lower rental cost, and higher marginal labour productivity as hours fall. Together these outweigh the rise in the real wage, driven by households' income effect on how much they want to work and by sticky nominal wages. Lower marginal cost lowers DPI (domestic) inflation and then CPI inflation (by 0.3 pp in the first year).
- **Short run, exchange rate.** The result is a real depreciation, reinforced by a nominal depreciation as monetary policy eases; the peak real depreciation is 1.4%. Expenditure switching helps bring demand for domestic output in line with supply.
- **Short run, consumption and investment.** Consumption rises through the income effect and a lower real interest rate. Footnote 50: the real rate rises at first, because expected inflation falls by more than policy eases, but it declines from the second quarter on. Investment is forward-looking (adjustment costs, time to build capital). So although the real rate rises and the rental cost falls in the very short run, Tobin's Q rises immediately, reflecting expected lower real rates and higher rental costs later.
- **First few quarters overall.** Supply grows faster than domestic demand. This excess domestic supply shows up as higher exports and lower imports.
- **Medium run.** The shock fades while demand stays high, so production costs and DPI inflation rise. But the accumulated current-account surpluses cause a nominal appreciation that lowers imported inflation, so CPI inflation stays low for a while. Excess demand then raises imports, financed by the earlier surpluses.
- **Medium run (continued).** Market forces and policy together raise utility (higher consumption and leisure) long after the shock has faded. The current account cushions the gap between output's quick return and the long-lasting utility gain. Together with the relatively high persistence (0.86), these mechanisms keep the expansion going for more than five years in some variables.

**Panels (mean line; all values approximate):**

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | 0 to 1.5 | Rises; peak ≈ +0.91 at x = 4; slow decline; still ≈ +0.23 at x = 20. |
| 2 | Consumption | 0 to 0.8 | Rises; peak ≈ +0.45 at x ≈ 4–5; very persistent; ≈ +0.25 at x = 20. |
| 3 | Fixed investment | 0 to 1.5 | Rises; broad hump peaking ≈ +0.88 at x ≈ 8–9; ≈ +0.53 at x = 20. |
| 4 | Exports | -0.5 to 1.5 | Rises; peak ≈ +1.08 at x = 5; ≈ +0.15 at x = 20. |
| 5 | Imports | -1 to 0.5 | Falls; trough ≈ -0.43 at x = 2–3; crosses zero at x ≈ 6–7; positive ≈ +0.24 at x ≈ 12–13; ≈ +0.17 at x = 20. |
| 6 | Hours worked | -1.5 to 0.5 | Large fall on impact (≈ -1.28), fast recovery; crosses zero at x ≈ 4–5; small positive ≈ +0.08 at x = 6; slightly negative (≈ -0.03) after x ≈ 12. |
| 7 | Interest rate | -0.8 to 0 | Cut; ≈ -0.17 on impact, trough ≈ -0.34 at x = 3; slow return; ≈ -0.07 at x = 20. |
| 8 | Real wage | -0.2 to 0.6 | Rises gradually; peak ≈ +0.27 at x ≈ 7–10; ≈ +0.17 at x = 20. |
| 9 | Real exchange rate | -1 to 2 | Depreciates; peak ≈ +1.39 at x = 3 (text: 1.4%); slow decline; ≈ +0.12 at x = 20. |
| 10 | CPI inflation | -0.3 to 0.1 | Largest drop on impact (≈ -0.14); ≈ 0 by x ≈ 4, then ≈ -0.01 to x = 20. Sum over x = 1–4 ≈ -0.27 (text: 0.3 pp in the first year). |
| 11 | Domestic inflation | -0.6 to 0.2 | Large drop on impact (≈ -0.38); crosses zero at x ≈ 3–4; positive hump ≈ +0.07 at x ≈ 6; ≈ 0 from x ≈ 13. |
| 12 | Imported inflation | -0.2 to 0.6 | Rises to ≈ +0.30 on impact; crosses zero at x ≈ 3–4; trough ≈ -0.14 at x ≈ 6–7; slow return; ≈ -0.02 at x = 20. |

## Appendix E Bayesian impulse responses

pages 127–134; pdf_pages 133–140 (the appendix heading is on page 127 above Figure 11; References begin on page 135, pdf_page 141).

**Summary.** Appendix E has no text, only the heading and eight figures. Figures 11–18 show Bayesian impulse responses, in the same format as Figures 6–10, to eight further shocks that Section 6.2 does not discuss (footnote 49; 12 of the 25 shocks have no impulse responses anywhere in the paper): domestic price markup, import price markup, oil price, investment-specific technology, export share, home bias, wage markup, and inventory investment demand. Layout, caption, units, horizon and line types are as described under "Common format of Figures 6–18" in Section 6.2 and are repeated in each figure section. The shock symbols below are the innovation symbols of Table 7; the figures themselves print no symbols. The figures do not state the sign of the shock; the responses are consistent with a positive one-standard-deviation innovation.

#### Figure 11: Impulse Response to a Domestic Price Markup Shock

page 127; pdf_page 133. No text discussion.

- **Shock:** domestic price markup shock, innovation $\eta^{H}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Layout note:** printed at a reduced size (panel frames about 72 pt wide instead of about 107 pt) on the page that carries the appendix heading; the caption differs from the others only in line breaks and dash spacing.
- **Overall (from the panels):** domestic and CPI inflation jump on impact and the policy rate rises, while activity, the real wage and the real exchange rate (appreciation) fall briefly.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.6 to 0.2 | Falls; trough ≈ -0.29 at x = 2; ≈ 0 by x ≈ 7; small positive (≈ +0.02) over x ≈ 8–11; ≈ -0.01 at x = 20. |
| 2 | Consumption | -0.4 to 0 | Falls; trough ≈ -0.15 at x = 3; ≈ -0.03 by x ≈ 8; small negative tail (≈ -0.02). |
| 3 | Fixed investment | -0.4 to 0 | Falls; trough ≈ -0.17 at x = 3; slow steady recovery; ≈ -0.02 at x = 20. |
| 4 | Exports | -0.6 to 0.2 | Falls; trough ≈ -0.25 at x = 3; crosses zero at x ≈ 7–8; small overshoot ≈ +0.06 at x ≈ 10–11; ≈ 0 at x = 20. |
| 5 | Imports | -0.2 to 0.6 | Rises ≈ +0.26 at x = 1–2; crosses zero at x ≈ 4–5; trough ≈ -0.11 at x = 7; ≈ -0.01 at x = 20. |
| 6 | Hours worked | -0.6 to 0.2 | Falls; trough ≈ -0.33 at x = 2; crosses zero at x ≈ 7; small positive ≈ +0.04 at x ≈ 9–10. |
| 7 | Interest rate | -0.2 to 0.6 | Rises; peak ≈ +0.22 at x = 3; ≈ 0 by x ≈ 6; tiny undershoot ≈ -0.03 at x = 7. |
| 8 | Real wage | -0.8 to 0 | Largest fall on impact (≈ -0.35); smooth recovery; ≈ -0.01 at x = 20. |
| 9 | Real exchange rate | -1 to 0.5 | Appreciates; trough ≈ -0.53 at x = 2; crosses zero at x ≈ 5–6; overshoot ≈ +0.11 at x = 8; ≈ 0 by x ≈ 17. |
| 10 | CPI inflation | -0.2 to 0.6 | Jumps to ≈ +0.30 on impact; ≈ +0.05 at x = 2; small undershoot ≈ -0.06 at x ≈ 3–4; ≈ 0 by x ≈ 7. |
| 11 | Domestic inflation | -0.5 to 1 | Jumps to ≈ +0.47 on impact; ≈ +0.07 at x = 2; undershoot ≈ -0.13 at x = 4; ≈ 0 by x ≈ 8. |
| 12 | Imported inflation | -0.1 to 0.3 | Slightly negative on impact (≈ -0.03); hump ≈ +0.08 at x = 5; ≈ 0 by x ≈ 9. |

#### Figure 12: Impulse Response to an Import Price Markup Shock

page 128; pdf_page 134. No text discussion.

- **Shock:** import price markup shock, innovation $\eta^{*}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** imported and CPI inflation spike on impact and imports drop. The policy rate rises briefly, and domestic demand and the real wage fall.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.1 to 0.3 | Rises to ≈ +0.16 on impact (maximum); crosses zero at x ≈ 2–3; trough ≈ -0.07 at x = 4; ≈ 0 by x ≈ 7–8 (≈ -0.01 later). |
| 2 | Consumption | -0.4 to 0 | Falls; trough ≈ -0.16 at x = 2–3; ≈ -0.03 by x ≈ 7; small negative tail (≈ -0.02). |
| 3 | Fixed investment | -0.4 to 0 | Falls; trough ≈ -0.20 at x = 3; slow steady recovery; ≈ -0.02 at x = 20. |
| 4 | Exports | -0.4 to 0.4 | Falls; trough ≈ -0.24 at x = 3; crosses zero at x ≈ 7–8; small overshoot ≈ +0.03 over x ≈ 9–12; ≈ 0 at x = 20. |
| 5 | Imports | -1 to 0 | Largest fall on impact (≈ -0.70); quick partial recovery (≈ -0.25 at x = 4), then gradual; ≈ -0.01 at x = 20. |
| 6 | Hours worked | -0.2 to 0.6 | Rises to ≈ +0.18 on impact; crosses zero at x ≈ 2–3; trough ≈ -0.07 at x = 4; ≈ 0 from x ≈ 7. |
| 7 | Interest rate | -0.2 to 0.6 | Rises; peak ≈ +0.23 at x = 3; ≈ 0 at x = 5; small undershoot ≈ -0.03 at x ≈ 6–7. |
| 8 | Real wage | -0.8 to 0 | Largest fall on impact (≈ -0.31); rapid recovery to ≈ -0.05 by x = 4, then slow; ≈ -0.01 at x = 20. |
| 9 | Real exchange rate | -0.4 to 0.4 | Appreciates; trough ≈ -0.14 at x = 3; crosses zero at x ≈ 4–5; overshoot ≈ +0.08 at x = 7; ≈ 0 by x ≈ 17. |
| 10 | CPI inflation | -0.2 to 0.6 | Jumps to ≈ +0.32 on impact; negative from x = 2, trough ≈ -0.10 at x = 3; ≈ 0 by x ≈ 6. |
| 11 | Domestic inflation | -0.02 to 0.06 | Very small: ≈ +0.03 at x = 1–2; ≈ 0 at x ≈ 4–5; second small hump ≈ +0.01 at x ≈ 8; ≈ +0.002 at x = 20. |
| 12 | Imported inflation | -0.5 to 1.5 | Jumps to ≈ +0.87 on impact; negative from x = 2, trough ≈ -0.32 at x = 3; ≈ 0 by x ≈ 6. |

#### Figure 13: Impulse Response to an Oil Price Shock

page 129; pdf_page 135. No text discussion.

- **Shock:** oil price shock, innovation $\eta^{OIL}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** imported and CPI inflation peak at x = 2 and the policy rate rises. Activity contracts with a delay (troughs around x = 4–5), followed by damped oscillations in several variables.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.4 to 0.4 | Small rise (peak ≈ +0.12 at x = 2), then contraction; trough ≈ -0.23 at x = 5–6; crosses zero at x ≈ 9; small positive ≈ +0.05 at x ≈ 11; ≈ -0.02 at x = 20. |
| 2 | Consumption | -0.4 to 0.4 | Falls; trough ≈ -0.24 at x = 3–4; back near zero (≈ -0.01) at x ≈ 8–9, then a second dip to ≈ -0.09 at x ≈ 13–16; ≈ -0.07 at x = 20. |
| 3 | Fixed investment | -0.8 to 0 | Falls; trough ≈ -0.35 at x = 3; partial recovery to ≈ -0.18 at x ≈ 7–8, second trough ≈ -0.25 at x ≈ 12–14; ≈ -0.15 at x = 20. |
| 4 | Exports | -2 to 1 | Slightly positive on impact (≈ +0.14), then a large fall; trough ≈ -1.15 at x = 5; crosses zero at x ≈ 9; overshoot ≈ +0.31 at x ≈ 12–13; ≈ +0.10 at x = 20. |
| 5 | Imports | -1.5 to 0.5 | Falls; trough ≈ -1.03 at x = 3–4; ≈ -0.1 by x ≈ 10; ≈ -0.03 at x = 20. |
| 6 | Hours worked | -0.4 to 0.4 | Small rise (≈ +0.15 at x = 2), then fall; trough ≈ -0.25 at x = 5; crosses zero at x ≈ 8–9; small positive ≈ +0.09 at x = 11; ≈ +0.01 at x = 20. |
| 7 | Interest rate | -0.5 to 0.5 | Rises; peak ≈ +0.35 at x = 3; crosses zero at x ≈ 6; trough ≈ -0.17 at x = 8; ≈ 0 at x ≈ 11, then slightly positive (≈ +0.06 at x ≈ 13–14). |
| 8 | Real wage | -0.6 to 0.2 | Falls; trough ≈ -0.32 at x = 3; ≈ -0.06 by x ≈ 7, then slow; ≈ -0.03 at x = 20. |
| 9 | Real exchange rate | -0.4 to 0.4 | Appreciates; trough ≈ -0.17 at x = 4; crosses zero at x ≈ 6; depreciation peak ≈ +0.21 at x ≈ 9; ≈ 0 by x ≈ 16. |
| 10 | CPI inflation | -0.2 to 0.6 | Rises; peak ≈ +0.21 at x = 2; negative over x ≈ 4–7 (trough ≈ -0.13 at x = 5); small positive ≈ +0.03 over x ≈ 9–11; ≈ 0 by x ≈ 14. |
| 11 | Domestic inflation | -0.05 to 0.05 | Very small: ≈ +0.01 at x = 1–2; trough ≈ -0.017 at x = 5; hump ≈ +0.03 at x = 10; ≈ +0.004 at x = 20. |
| 12 | Imported inflation | -0.5 to 1 | Rises; peak ≈ +0.57 at x = 2; crosses zero at x ≈ 3–4; trough ≈ -0.33 at x = 5; small oscillations around zero after x ≈ 8. |

#### Figure 14: Impulse Response to an Investment Specific Technology Shock

page 130; pdf_page 136 (title printed with the "fi" ligature: "Speciﬁc"). No text discussion.

- **Shock:** investment-specific technology shock, innovation $\eta^{I}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** a large, persistent investment boom. Output, exports, the real wage and the real exchange rate (depreciation) rise slowly and persistently, consumption is crowded out for about 15 quarters, and inflation falls slightly; the bands are wide.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | 0 to 1 | Rises to ≈ +0.26 on impact and keeps rising; broad peak ≈ +0.49 at x ≈ 11; ≈ +0.41 at x = 20 (very persistent). |
| 2 | Consumption | -1 to 0.5 | Falls; trough ≈ -0.32 at x ≈ 4–5; slow recovery, crossing zero at x ≈ 15–16; ≈ +0.15 at x = 20. |
| 3 | Fixed investment | -2 to 6 | Large rise, ≈ +2.3 on impact; peak ≈ +3.2 at x ≈ 3–5; steady decline to ≈ +0.2 at x = 20. |
| 4 | Exports | -0.5 to 1.5 | Starts ≈ 0 and rises steadily; peak ≈ +0.65 at x ≈ 16–18; ≈ +0.63 at x = 20. |
| 5 | Imports | -0.5 to 1 | Rises to ≈ +0.41 on impact, peak ≈ +0.48 at x = 3; then declines, crossing zero at x ≈ 12–13; ≈ -0.14 at x = 20. |
| 6 | Hours worked | -0.2 to 0.6 | Rises to ≈ +0.29 on impact (maximum); uneven slow decline; crosses zero at x ≈ 16; ≈ -0.05 at x = 20. |
| 7 | Interest rate | -0.2 to 0.2 | Small rise; peak ≈ +0.06 at x ≈ 3–5; crosses zero at x ≈ 14–15; ≈ -0.04 at x = 20. |
| 8 | Real wage | -0.1 to 0.3 | ≈ 0 on impact; rises almost linearly to ≈ +0.14 at x = 20 (still rising). |
| 9 | Real exchange rate | -0.5 to 1.5 | ≈ 0 on impact; gradual depreciation to ≈ +0.63 at x ≈ 15–17; ≈ +0.59 at x = 20. |
| 10 | CPI inflation | -0.1 to 0.1 | Small, persistent fall: ≈ 0 on impact, ≈ -0.03 by x ≈ 5, ≈ -0.036 over x ≈ 11–14; ≈ -0.033 at x = 20. |
| 11 | Domestic inflation | -0.1 to 0.1 | Falls; trough ≈ -0.057 at x ≈ 6–7; slow return; ≈ -0.03 at x = 20. |
| 12 | Imported inflation | -0.1 to 0.1 | Small rise, peak ≈ +0.017 at x = 5; crosses zero at x ≈ 9–10; still falling at x = 20 (≈ -0.044). |

#### Figure 15: Impulse Response to an Export Share Shock

page 131; pdf_page 137. No text discussion.

- **Shock:** export share shock, innovation $\eta^{\nu^{*}}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** exports, imports, output and hours jump on impact. The real exchange rate appreciates persistently, and imported and CPI inflation fall; consumption and investment build up gradually.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.5 to 1 | Largest rise on impact (≈ +0.61); falls to ≈ +0.01 by x ≈ 8; then creeps up to ≈ +0.07 at x = 20 (stays positive). |
| 2 | Consumption | -0.2 to 0.6 | Gradual rise; peak ≈ +0.23 over x ≈ 8–12; ≈ +0.17 at x = 20. |
| 3 | Fixed investment | 0 to 1.5 | Rises; peak ≈ +0.76 at x ≈ 10; ≈ +0.45 at x = 20. |
| 4 | Exports | -2 to 4 | Jumps to ≈ +2.8 on impact, peak ≈ +3.0 at x = 2; ≈ 0 by x ≈ 9; small undershoot ≈ -0.13 over x ≈ 12–14; ≈ -0.06 at x = 20. |
| 5 | Imports | 0 to 2 | Rises to ≈ +1.1 on impact, peak ≈ +1.4 at x = 2–3; slow decline; ≈ +0.24 at x = 20. |
| 6 | Hours worked | -0.5 to 1 | Largest rise on impact (≈ +0.70); ≈ 0 by x ≈ 7; ≈ -0.03 afterwards. |
| 7 | Interest rate | -0.2 to 0.2 | Tiny rise (≈ +0.03 at x = 2), negative from x ≈ 4; trough ≈ -0.08 over x ≈ 8–12; ≈ -0.05 at x = 20. |
| 8 | Real wage | 0 to 0.8 | Rises; peak ≈ +0.32 at x ≈ 4–5; slow decline; ≈ +0.12 at x = 20. |
| 9 | Real exchange rate | -1.5 to 0 | Appreciates; trough ≈ -1.0 at x ≈ 3–4; slow return; ≈ -0.12 at x = 20. |
| 10 | CPI inflation | -0.08 to 0 | Small fall; trough ≈ -0.035 at x = 1–2; ≈ -0.009 from x ≈ 10 to x = 20. |
| 11 | Domestic inflation | -0.1 to 0.3 | Rises to ≈ +0.10 on impact (maximum); crosses zero at x ≈ 3–4; trough ≈ -0.05 at x ≈ 7; ≈ -0.02 at x = 20. |
| 12 | Imported inflation | -0.6 to 0.2 | Falls to ≈ -0.28 on impact (minimum); ≈ 0 at x ≈ 5; small positive ≈ +0.05 at x ≈ 8; ≈ +0.01 at x = 20. |

#### Figure 16: Impulse Response to a Home Bias Shock

page 132; pdf_page 138. No text discussion.

- **Shock:** home bias shock, innovation $\eta^{\nu}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** imports drop and output and hours jump on impact. The real exchange rate appreciates and exports fall for several years, while consumption, investment and the real wage rise gradually.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.5 to 1 | Largest rise on impact (≈ +0.71); fast decline to ≈ +0.01 by x ≈ 8; ≈ +0.05 at x = 20 (stays slightly positive). |
| 2 | Consumption | -0.1 to 0.3 | Gradual rise; peak ≈ +0.16 at x ≈ 9–10; ≈ +0.12 at x = 20. |
| 3 | Fixed investment | 0 to 0.8 | Rises; peak ≈ +0.51 at x ≈ 9–11; ≈ +0.32 at x = 20. |
| 4 | Exports | -1 to 0 | Falls; trough ≈ -0.59 at x ≈ 5–6; slow recovery; ≈ -0.13 at x = 20. |
| 5 | Imports | -2 to 1 | Largest fall on impact (≈ -1.7); fast recovery, crossing zero at x ≈ 8–9; small positive ≈ +0.11 over x ≈ 14–18; ≈ +0.10 at x = 20. |
| 6 | Hours worked | -0.5 to 1 | Largest rise on impact (≈ +0.82); ≈ 0 by x ≈ 7; ≈ -0.01 to -0.02 afterwards. |
| 7 | Interest rate | -0.1 to 0.1 | Rises ≈ +0.05 at x = 1–2; crosses zero at x ≈ 3–4; trough ≈ -0.055 at x ≈ 8–9; ≈ -0.036 at x = 20. |
| 8 | Real wage | 0 to 0.4 | Rises; peak ≈ +0.23 at x ≈ 3–4; slow decline; ≈ +0.09 at x = 20. |
| 9 | Real exchange rate | -1.5 to 0 | Appreciates; trough ≈ -0.69 at x = 4; slow return; ≈ -0.10 at x = 20. |
| 10 | CPI inflation | -0.06 to 0.02 | Small fall; trough ≈ -0.030 at x = 2; settles at ≈ -0.006 from x ≈ 10. |
| 11 | Domestic inflation | -0.05 to 0.15 | Rises to ≈ +0.09 on impact (maximum); crosses zero at x ≈ 3–4; trough ≈ -0.03 at x ≈ 6–7; ≈ -0.01 at x = 20. |
| 12 | Imported inflation | -0.4 to 0.4 | Falls to ≈ -0.22 on impact (minimum); ≈ 0 by x ≈ 5; small positive ≈ +0.03 over x ≈ 7–10; ≈ +0.01 at x = 20. |

#### Figure 17: Impulse Response to a Wage Markup Shock

page 133; pdf_page 139. No text discussion.

- **Shock:** wage markup shock, innovation $\eta^{W}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** the real wage jumps and domestic and CPI inflation rise on impact. Hours, output and demand components fall with troughs around x = 3–5, the policy rate rises, and the currency appreciates.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.8 to 0 | Falls; trough ≈ -0.38 at x ≈ 3–4; recovers to ≈ -0.05 by x ≈ 12; ≈ -0.03 at x = 20. |
| 2 | Consumption | -0.4 to 0 | Falls; trough ≈ -0.16 at x = 4; slow recovery; ≈ -0.05 at x = 20. |
| 3 | Fixed investment | -0.8 to 0 | Falls; broad trough ≈ -0.27 over x ≈ 5–7; slow recovery; ≈ -0.12 at x = 20. |
| 4 | Exports | -1 to 0.5 | Falls; trough ≈ -0.45 at x ≈ 4–5; crosses zero at x ≈ 12–13; ≈ +0.03 over x ≈ 15–19. |
| 5 | Imports | -0.2 to 0.6 | Rises; peak ≈ +0.27 at x = 2; crosses zero at x ≈ 6–7; trough ≈ -0.12 at x ≈ 10–11; ≈ -0.06 at x = 20. |
| 6 | Hours worked | -0.6 to 0.2 | Falls; trough ≈ -0.43 at x ≈ 3–4; ≈ 0 by x ≈ 15. |
| 7 | Interest rate | 0 to 0.4 | Rises; peak ≈ +0.21 at x ≈ 3–4; ≈ +0.03 by x ≈ 9; ≈ +0.02 at x = 20 (stays slightly positive). |
| 8 | Real wage | -0.5 to 1.5 | Largest rise on impact (≈ +1.0); fast decline; crosses zero at x ≈ 9–10; ≈ -0.03 afterwards. |
| 9 | Real exchange rate | -1 to 0.5 | Appreciates; trough ≈ -0.66 at x = 3; crosses zero at x ≈ 10; ≈ +0.04 over x ≈ 12–16; ≈ +0.02 at x = 20. |
| 10 | CPI inflation | -0.1 to 0.3 | Rises to ≈ +0.14 on impact (maximum); ≈ 0 by x ≈ 5; ≈ +0.005 afterwards. |
| 11 | Domestic inflation | -0.2 to 0.6 | Rises to ≈ +0.27 on impact (maximum); crosses zero at x ≈ 3–4; trough ≈ -0.05 over x ≈ 5–7; ≈ 0 by x ≈ 11. |
| 12 | Imported inflation | -0.2 to 0.2 | Falls to ≈ -0.08 on impact; crosses zero at x ≈ 3; peak ≈ +0.10 at x = 6; ≈ 0 by x ≈ 14. |

#### Figure 18: Impulse Response to an Inventories Investment Demand Shock

page 134; pdf_page 140. No text discussion.

- **Shock:** inventory investment demand shock, innovation $\eta^{\Delta INV}$; size: one standard deviation (caption).
- **Line types (caption wording):** solid line – "mean of impulse response"; gray area – "70 and 90 percent highest interval of impulse response" (darker inner shade and lighter outer shade; the caption does not say which is which).
- **Units:** as for all IRF figures (see "Units" under the common format in 6.2).
- **Horizon:** 20 quarters; the mean line is plotted at x = 1 (impact) … 20; x-axis ticks 0, 10, 20, no axis title.
- **Panels (in order):** Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Interest rate, Real wage, Real exchange rate, CPI inflation, Domestic inflation, Imported inflation (4 rows × 3 columns).
- **Overall (from the panels):** output, imports and hours jump on impact and return quickly. Consumption and fixed investment fall persistently, and the policy rate rises modestly and persistently.

| # | Panel | y-axis (printed) | Reading |
|---|---|---|---|
| 1 | Output | -0.5 to 1 | Largest rise on impact (≈ +0.69); fast decline; crosses zero at x ≈ 6; slightly negative (≈ -0.04) over x ≈ 15–20. |
| 2 | Consumption | -0.4 to 0 | Falls; trough ≈ -0.23 at x ≈ 4–5; very slow recovery; ≈ -0.11 at x = 20. |
| 3 | Fixed investment | -1 to 0 | Falls; broad trough ≈ -0.51 over x ≈ 7–9; ≈ -0.25 at x = 20. |
| 4 | Exports | -0.2 to 0.2 | Falls; trough ≈ -0.11 at x ≈ 3–4; crosses zero at x ≈ 7–8; positive ≈ +0.09 over x ≈ 12–14; ≈ +0.04 at x = 20. |
| 5 | Imports | -0.5 to 1.5 | Largest rise on impact (≈ +1.26); crosses zero at x ≈ 6–7; undershoot ≈ -0.16 at x ≈ 11–12; ≈ -0.10 at x = 20. |
| 6 | Hours worked | -0.5 to 1 | Largest rise on impact (≈ +0.79); ≈ +0.01 by x ≈ 6; ≈ +0.02 afterwards. |
| 7 | Interest rate | 0 to 0.2 | Rises to ≈ +0.10 on impact, peak ≈ +0.145 at x = 3; slow decline; ≈ +0.03 at x = 20. |
| 8 | Real wage | -0.2 to 0.2 | Small rise ≈ +0.03 at x = 1–2; crosses zero at x ≈ 4; trough ≈ -0.08 over x ≈ 10–13; ≈ -0.06 at x = 20. |
| 9 | Real exchange rate | -0.4 to 0.4 | Appreciates; trough ≈ -0.20 at x = 2; crosses zero at x ≈ 6–7; depreciation ≈ +0.10 over x ≈ 10–12; ≈ +0.03 at x = 20. |
| 10 | CPI inflation | -0.02 to 0.04 | Small rise to ≈ +0.017 on impact (maximum); negative over x ≈ 3–6 (trough ≈ -0.007 at x = 4); ≈ +0.005 from x ≈ 9. |
| 11 | Domestic inflation | -0.05 to 0.15 | Rises to ≈ +0.06 on impact (maximum); crosses zero at x ≈ 2–3; trough ≈ -0.027 at x = 5; positive again from x ≈ 10; ≈ +0.009 at x = 20. |
| 12 | Imported inflation | -0.1 to 0.1 | Falls to ≈ -0.06 on impact (minimum); crosses zero at x ≈ 3–4; peak ≈ +0.04 at x ≈ 5–6; ≈ 0 by x ≈ 13. |
