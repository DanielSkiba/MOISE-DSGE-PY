# Model evaluation and concluding remarks

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

Section 5 (moment fit, Table 6; in-sample forecast quality) and Section 7 (concluding remarks).

## 5 Model evaluation

*Printed pp. 62–68 (PDF pp. 68–74). The last paragraphs of 5.2 are on PDF p. 74, above the Section 6 heading.*

**Summary.** Section 5 tests the estimated model against the data in two ways. Section 5.1 checks whether moments simulated from the model bracket the observed ones: auto- and cross-correlations of six key variables (Figure 4), and means and standard deviations of eleven observables (Table 6). Section 5.2 compares the model's unconditional in-sample forecast errors with those of steady-state, random-walk and BVAR benchmarks (Figure 5).

### 5.1 Moment goodness-of-fit tests

**Summary.** Simulation gives the model's distribution of each sample moment, and the observed moment is compared with it. Most observed moments fall inside the model's 90% intervals; the exceptions are listed below.

How the test is built:

- Six key variables (inline block below): the policy rate, CPI inflation, the change in the nominal effective exchange rate, and growth in hourly nominal wages, output per head and exports per head.
- Data moments use the 72 quarterly observations of the estimation sample, 1992:Q1–2009:Q4.
- Model intervals come from 1,000 simulated samples of 72 periods each; for each moment, the band is the central 90% of its 1,000 simulated values. Parameters are fixed at their posterior means, so the bands reflect only randomness in the shocks, not parameter uncertainty (footnote 40). The simulated model includes its built-in filtering block (Section 4.2), so simulated series contain both the model's business-cycle dynamics and the imbalanced growth seen in the data.

<!-- kind: inline; id: 97.i11; section: 5.1; page: 62; pdf_page: 68 -->
**(97.i11) Notation for the six key variables of the correlation tests**

$$
r_{t}^{OB}, \Delta P_{c,t}, \Delta S_{t}, \Delta W_{t}, \Delta Y_{t} \text{ and } \Delta X_{t}
$$

Meaning: Symbols for the six tested series: policy rate, CPI inflation, exchange-rate depreciation, and growth in hourly nominal wages, output per head and exports per head.

#### Figure 4: Cross-Correlations: Observed vs. Model-Based Confidence Intervals (page 63, pdf_page 69)

- **Layout.** The figure is printed sideways; it is described here with the page turned 90° clockwise, so that panel titles read upright and the caption runs down the right edge. It is a 6 × 6 grid of panels. Rows and columns both run over the six variables in the order $r^{OB}$, $\Delta P_{C}$, $\Delta S$, $\Delta W$, $\Delta Y$, $\Delta X$. The panel in row $a$, column $b$ shows the correlation of $a$ at $t$ with $b$ at $t-k$; panel titles read like "$r_{t}^{OB}$ & $\Delta P_{C,t-k}$". The diagonal panels are therefore auto-correlations. Panel titles use an upper-case $C$ in $\Delta P_{C}$; the Section 5.1 text and Table 6 use a lower-case $c$.
- **Axes and lines.** The x-axis is the lag $k = 0, \dots, 5$ (quarters) and the y-axis the correlation, from −1 to 1. The solid blue line is the correlation in the data; the gray band is the model-based 90% interval from the simulations above.
- **Auto-correlations (diagonal), approximate readings.**
  - $r^{OB}$: the data fall smoothly from 1 to about 0.3 at $k = 5$, inside a wide band (about −0.3 to 0.5 at $k = 5$).
  - $\Delta P_{C}$: about 0.3 at $k = 1$, near the lower edge of the band (about 0.25–0.55); near zero at $k = 2$–3; about 0.2 at $k = 4$, slightly above the band.
  - $\Delta X$: about 0.25 at $k = 1$, near the lower edge of a band of about 0.2–0.6, then declining toward zero inside the band.
  - $\Delta Y$: about 0.37 at $k = 1$ and 0.3 at $k = 2$, above the band (upper edges about 0.32 and 0.2). This is the output-growth persistence the model misses.
  - $\Delta S$: about 0.1 at $k = 1$, then near zero, inside a band that straddles zero.
  - $\Delta W$: the data zig-zag (about −0.25 at $k = 1$, +0.3 at $k = 3$, −0.3 at $k = 4$) and lie outside a zero-straddling band at those lags, only marginally at $k = 4$.
- **Cross-correlations (off-diagonal), approximate readings.**
  - $r_{t}^{OB}$ & $\Delta P_{C,t-k}$: the model band is positive (about 0.2–0.65 for $k = 1$–3), while the data are negative at every lag (about −0.12 to −0.25). The data therefore lie below the band at every lag, only marginally at $k = 5$. This is the main failure.
  - $\Delta P_{C,t}$ & $r_{t-k}^{OB}$: the data are negative: about −0.25 at $k = 0$, a trough near −0.5 at $k = 1$, about −0.27 at $k = 5$. The band also lies mostly below zero for $k \ge 1$ and contains the data from $k = 2$ onward; at $k = 0$–1 the data sit somewhat below it.
  - $\Delta P_{C,t}$ & $\Delta S_{t-k}$: about 0.35 at $k = 0$ and 0.2 at $k = 1$, then near zero, inside the band.
  - $\Delta Y_{t}$ & $\Delta X_{t-k}$ and $\Delta X_{t}$ & $\Delta Y_{t-k}$: about 0.56 at $k = 0$, inside a band of about 0.3–0.65, then decaying. At $k = 1$ (and at $k = 2$ for $\Delta Y_{t}$ & $\Delta X_{t-k}$) the data are at or slightly above the upper edge.
  - Other pairs: the data mostly stay within about ±0.3 and inside bands that straddle zero. Many panels, however, have one or two lags at or just past a band edge. The clearest cases are $\Delta Y_{t}$ & $\Delta S_{t-k}$ at $k = 1$ (data about −0.4, lower edge about −0.05), $\Delta X_{t}$ & $\Delta S_{t-k}$ at $k = 1$ (about −0.25 against about −0.1), $\Delta Y_{t}$ & $\Delta P_{C,t-k}$ at $k = 2$ (about +0.25 against about +0.08), and $\Delta W_{t}$ & $\Delta Y_{t-k}$ at $k = 2$ (about 0.42 against about 0.33). A few k = 0 bands do not straddle zero, so "inside bands that straddle zero" holds only mostly.

Findings stated in the text:

- The model implies significant first-order auto-correlation for $r^{OB}$, $\Delta P_{c}$ and $\Delta X$, and the data agree. The observed persistence of $\Delta Y$ is not captured. For $\Delta S$ and $\Delta W$, neither the model nor the data shows significant auto-correlation.
- Most observed cross-correlations lie inside the model intervals. The notable exception is the correlation of the policy rate with current and past inflation (inline block below): the model makes it significantly positive, but the data show no positive value. Sub-samples show none either. Footnote 41: two alternative observables brought no improvement either. One measured the policy rate as a gap to the long-run forward rate; the other kept housing in CPI inflation over the full sample.
- This moment depends mainly on the policy rule and its response to inflation. The rule is the model's only behavioral equation without micro-foundations, so the authors re-estimated the model under alternative rules. Some of these lowered the model correlation between $r_{t}^{OB}$ and lagged inflation but worsened other moments, so rule (62) was kept. Footnote 42 points to the sensitivity analysis in Section 4.6.
- In the reverse direction, current inflation against the lagged policy rate (second inline block below), the model reproduces the data's negative correlation fairly well. The authors read this as support for how the model transmits monetary policy to inflation.
- The correlation of inflation with current and lagged depreciation is also matched, which suggests that the model's exchange-rate pass-through to prices is reasonable.
- Many cross-correlations are not significantly different from zero in the model; Figure 4 indicates the same is true of the data.

<!-- kind: inline; id: 97.i12; section: 5.1; page: 64; pdf_page: 70 -->
**(97.i12) Lagged inflation and the range of lags in the policy-rate/inflation moment**

$$
\Delta P_{c,t-k}, k \in \{0, ..., 5\}
$$

Meaning: Inflation lagged k quarters, k from 0 to 5; its correlation with the current policy rate is the moment the model fails to reproduce.

<!-- kind: inline; id: 97.i13; section: 5.1; page: 64; pdf_page: 70 -->
**(97.i13) Lagged policy rate**

$$
r_{t-k}^{OB}
$$

Meaning: Policy rate lagged k quarters; current inflation's negative correlation with it, seen in the data, is matched fairly well by the model.

#### Table 6: Selected Means and Standard Deviations — Model-Based Intervals vs. the Data (page 65, pdf_page 71)

For each variable, the table gives the median and the 5th and 95th percentiles of the model-simulated distribution of the sample mean and of the sample standard deviation, plus the value in the data. The table does not state units or transformations. The row symbols correspond to observables defined in Appendix A (PDF pp. 93–96). The table is also in `data/table6_moments.csv`.

| Variable | Mean: Median | Mean: 5% | Mean: 95% | Mean: data | Standard Deviation: Median | Standard Deviation: 5% | Standard Deviation: 95% | Standard Deviation: data |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $\Delta C$ | 0.42 | 0.17 | 0.72 | 0.44 | 1.87 | 1.55 | 2.26 | 1.22 |
| $\Delta X$ | 1.21 | 0.78 | 1.67 | 1.22 | 4.37 | 3.59 | 5.17 | 3.62 |
| $\Delta I$ | 0.43 | -0.18 | 1.05 | 0.06 | 3.54 | 2.96 | 4.25 | 3.13 |
| $\Delta IM$ | 0.71 | 0.34 | 1.07 | 0.56 | 3.59 | 3.05 | 4.21 | 3.49 |
| $\Delta Y$ | 0.43 | 0.24 | 0.61 | 0.39 | 1.80 | 1.51 | 2.09 | 1.00 |
| $\Delta P_{c}$ | 0.51 | 0.14 | 0.87 | 0.37 | 0.88 | 0.73 | 1.04 | 0.82 |
| $\Delta S$ | 0.01 | -0.51 | 0.53 | -0.21 | 3.33 | 2.84 | 3.89 | 3.33 |
| $r^{OB}$ | 6.35 | -2.15 | 12.89 | 5.51 | 2.57 | 1.85 | 3.48 | 2.49 |
| $\Delta W$ | 0.75 | 0.25 | 1.23 | 0.61 | 1.82 | 1.56 | 2.12 | 1.68 |
| $\Delta N$ | 0.17 | 0.02 | 0.32 | 0.14 | 2.46 | 2.10 | 2.83 | 1.38 |
| $s_{CA}$ | -0.02 | -1.28 | 1.35 | 0.40 | 4.03 | 2.99 | 5.56 | 3.00 |

Table note (paraphrased): the model intervals come from 1,000 simulated samples, each 72 periods long.

Findings stated in the text:

- Every observed mean lies well inside its model interval.
- Most observed standard deviations do too; where they do not, the observed value is below the interval. The text singles out output growth and hours-worked growth (inline block below). In the table, $\Delta C$ (1.22 against a 5% bound of 1.55) is also below its interval.
- The authors attribute part of the excess model volatility of $\Delta Y$ and $\Delta N$ to the exogenous law of motion for the change in inventories (equation (3)). In reality, inventory changes cushion output, which is demand-determined. Made exogenous, they instead add volatility, mainly to output and production. Footnote 43: dropping the inventory-change shock from the simulations shifts both standard-deviation intervals down and barely changes other moments, but the observed values stay below the new lower bounds.
- The interval for the mean of $r^{OB}$ is exceptionally wide (−2.15 to 12.89). This happens because the forward-real-rate shock (inline block below) follows a near-unit-root process (AR(1) with coefficient 0.99; Section 3.1, display 3.u1), which also shows up in the variance decomposition of Table 7 (Section 6). The authors note that this fits the trend in the observed interest rate over the sample. Footnote 44: without this shock, the interval narrows to 3.04–6.82, and other simulated moments change little.

<!-- kind: inline; id: 97.i14; section: 5.1; page: 65; pdf_page: 71 -->
**(97.i14) Output and hours-worked growth**

$$
\Delta Y \text{ and } \Delta N
$$

Meaning: Growth rates of output and of hours worked, whose observed standard deviations fall below the model's simulated intervals.

<!-- kind: inline; id: 97.i15; section: 5.1; page: 66; pdf_page: 72 -->
**(97.i15) Forward real interest rate shock**

$$
\varepsilon_{t}^{DRP}
$$

Meaning: Shock that moves the forward real rate; it is a near-unit-root AR(1) (coefficient 0.99), which makes the model interval for the mean policy rate very wide.

### 5.2 Forecast quality

**Summary.** The model's unconditional in-sample forecasts, up to eight quarters ahead, are compared with three simple benchmarks by root mean squared error. For most variables the model does no worse than the benchmarks, and it is the best forecaster of the policy rate. The authors expect conditioning on outside information to improve the forecasts in practice. They also name two shocks whose advance knowledge would sharply cut forecast errors.

How the comparison is built:

- Eight variables. For the Bank of Israel rate $r^{OB}$, the error is that of the rate forecast itself. For seven level variables (output, consumption, exports, the CPI, the nominal effective exchange rate, hourly nominal wages and hours worked), the RMSE is that of the cumulated growth-rate forecasts (inline block below).
- Benchmarks: steady state (SS; labelled "Model Based SS" in the figure legend), random walk (RW) and a third-order Bayesian VAR (BVAR). The BVAR uses Minnesota-style priors centred at 0.5; other prior means gave it larger RMSEs (footnote 45). It contains the eight variables of Figure 5. Adding employment growth (second inline block below) pushed the BVAR's RMSEs for $\Delta W$ and $\Delta C$ below those of MOISE, but raised them markedly for the other variables (footnote 46).

<!-- kind: inline; id: 97.i16; section: 5.2; page: 66; pdf_page: 72 -->
**(97.i16) Growth rates whose cumulated forecast errors are reported**

$$
\Delta P_{C}, \Delta Y, \Delta C, \Delta S, \Delta X, \Delta W \text{ and } \Delta N
$$

Meaning: Growth rates whose cumulated forecasts give level forecast errors for the CPI, output, consumption, exchange rate, exports, nominal hourly wage and hours worked.

<!-- kind: inline; id: 97.i17; section: 5.2; page: 66; pdf_page: 72 -->
**(97.i17) Employment growth (footnote 46)**

$$
\Delta EM
$$

Meaning: Rate of change in employment; adding it to the BVAR benchmark lowered that model's errors for wages and consumption but raised them for the remaining variables.

#### Figure 5: In-Sample Forecast Root Mean Square Errors (RMSE) (page 67, pdf_page 73)

- **Layout.** The figure is printed sideways; it is described here with the page turned 90° clockwise (caption down the right edge), giving four rows of two panels (as printed, with the caption on top, it is two rows of four): "Forecast RMSE of $r^{OB}$" and "Cumulated Forecast RMSE of $\Delta P_{C}$"; then $\Delta Y$ and $\Delta C$; $\Delta S$ and $\Delta X$; $\Delta W$ and $\Delta N$ (all titled "Cumulated Forecast RMSE of …").
- **Axes and lines.** x-axis: forecast horizon, 1 to 8 quarters. y-axis: RMSE in %. There are four lines: DSGE (MOISE; solid black), Model Based SS (blue dashed with circles), RW (red dotted with asterisks) and BVAR(3) (magenta dashed). The legend is in the $r^{OB}$ panel.
- **Approximate readings.** Values are read off the chart at horizon 1 → horizon 8; they are not printed in the paper.

| Panel | DSGE | Model Based SS | RW | BVAR(3) |
|---|---|---|---|---|
| $r^{OB}$ | ≈0.95 → ≈1.8 | ≈2.35 → ≈2.1 | ≈1.1 → ≈2.5 | ≈1.1 → ≈2.4 |
| $\Delta P_{C}$ | ≈0.85 → ≈2.5 | ≈0.8 → ≈3.2 | ≈1.1 → ≈7.0 | ≈0.9 → ≈5.2 |
| $\Delta Y$ | ≈1.2 → ≈3.9 | ≈1.0 → ≈4.1 | ≈1.25 → ≈9.3 | ≈1.1 → ≈5.0 |
| $\Delta C$ | ≈1.5 → ≈4.3 | ≈1.2 → ≈3.3 | ≈1.9 → ≈11.4 | ≈1.4 → ≈5.1 |
| $\Delta S$ | ≈3.2 → ≈7.3 | ≈3.3 → ≈9.5 | ≈4.8 → ≈28 | ≈3.7 → ≈16.8 |
| $\Delta X$ | ≈3.6 → ≈10.5 | ≈3.3 → ≈12.2 | ≈4.7 → ≈30 | ≈3.2 → ≈12.7 |
| $\Delta W$ | ≈1.8 → ≈4.2 | ≈1.7 → ≈4.5 | ≈2.7 → ≈15 | ≈1.7 → ≈6.5 |
| $\Delta N$ | ≈1.9 → ≈4.5 | ≈1.5 → ≈3.6 | ≈2.4 → ≈13.3 | ≈1.5 → ≈3.35 |

- **Main visible pattern.**
  - RW has by far the largest cumulated errors for every level variable, and they grow roughly linearly with the horizon.
  - $r^{OB}$: DSGE is lowest at every horizon. SS is nearly flat, and RW and BVAR almost coincide.
  - $\Delta P_{C}$: DSGE and SS are about equal up to horizon 4; after that DSGE is lowest.
  - $\Delta Y$: SS lies below DSGE up to about horizon 4 (e.g. ≈1.0 vs ≈1.3 at horizon 1) and the two are close afterwards. $\Delta W$: DSGE and SS nearly coincide. BVAR lies above both beyond the first few quarters.
  - $\Delta C$: SS is lowest throughout. DSGE is slightly above BVAR up to horizon 4; the two cross near horizon 5, after which DSGE is lower.
  - $\Delta S$: DSGE is lowest at all horizons.
  - $\Delta X$: DSGE, SS and BVAR stay close up to about horizon 5, with DSGE slightly above the other two at the shortest horizons; after that DSGE is lowest.
  - $\Delta N$: SS and BVAR are below DSGE at all horizons.

Findings stated in the text:

- For most variables the unconditional MOISE forecasts appear no worse than the benchmarks. For the interest rate, its RMSEs are below all the alternatives, which the authors take to mean the model predicts this variable better.
- According to the text, MOISE does not beat the SS benchmark for the CPI and output, unlike the interest rate. The authors relate this to flexible inflation targeting: it is chiefly the policy rate that departs from steady state, absorbing shocks so that other variables stay close to theirs.
- The authors call the result encouraging. In actual use, the forecasts are conditioned on much information from outside the model, which should improve them further (PDF p. 74). Footnote 47 adds that, according to Maih (2010), such conditioning can raise RMSEs, because models are inevitably misspecified. Conditioning is fairly easy in the DSGE model, hard in a BVAR and impossible with SS or RW.
- Two shocks would have improved the forecasts substantially had they been known in advance:
  - $\varepsilon_{t}^{RP^{*}}$, which hits the modified UIP condition (7); its standard deviation is large and its effects propagate strongly.
  - $\varepsilon_{t}^{RP}$, the very persistent risk-premium shock on bonds that enters the households' budget constraint (2).

  Forecasting with advance knowledge of these two shocks would cut the RMSEs considerably. Both symbols are given as inline blocks below; Section 3.1 defines them.

<!-- kind: inline; id: 97.i18; section: 5.2; page: 68; pdf_page: 74 -->
**(97.i18) Shock in the modified UIP condition (7)**

$$
\varepsilon_{t}^{RP^{*}}
$$

Meaning: Shock in the modified UIP condition (7); large and strongly transmitted, so knowing it in advance would have reduced forecast errors substantially.

<!-- kind: inline; id: 97.i19; section: 5.2; page: 68; pdf_page: 74 -->
**(97.i19) Bond risk-premium shock (budget constraint (2))**

$$
\varepsilon_{t}^{RP}
$$

Meaning: Very persistent bond risk-premium shock in the households' budget constraint (2); advance knowledge of it would also have cut forecast errors substantially.

Note: the paper prints $\varepsilon_{t}^{RP}$ here and calls it highly inertial, but elsewhere it uses that description for the domestic premium shock $\varepsilon^{DRP}$ (AR coefficient 0.99), while $\rho_{RP}$ is estimated at about 0.77 (Table 2). The sentence may refer to $\varepsilon^{DRP}$; transcribed as printed.

## 7 Concluding remarks

*Printed pp. 84–86 (PDF pp. 90–92).*

**Summary.** The conclusions restate what MOISE is and how it was estimated. They list its main modifications and their costs, highlight its distinctive properties, and outline further work.

- **Model and overall assessment.** MOISE is a micro-founded DSGE model of medium size, a type central banks use widely. It was built to help the Bank of Israel design monetary policy and assess risks. Standard Bayesian methods were applied to quarterly Israeli data, 1992–2009. The authors judge the outcome largely satisfactory: the data identify most parameters well, the simulated model matches most observed moments of key macro series, and its unconditional in-sample forecasts are on a par with naive and statistical benchmarks.
- **Modifications to the borrowed framework.** The changes, made to fit Israeli features and practical use, include among others (the paper's list ends with "etc."; Section 1 also mentions imports in government consumption and local-currency pricing of trade):
  - imports as an intermediate input to exports;
  - extensions for the time-varying long-term real rate;
  - allowance for the disinflation of the early sample years;
  - inventories, so that the aggregate resource constraint satisfies national-accounts identities;
  - stochastic terms in the observation equations that absorb imbalanced growth. This avoids pre-filtering and keeps the information in how the series move together.
- **Stated limitations.** Most modifications are very simple. They still improve the overall fit and the usefulness for policy, but simplicity has a price: some moments remain poorly matched. Neither the persistence nor the volatility of output growth is reproduced, partly because inventory investment is exogenous. Section 5 showed that output growth is more persistent and less volatile in the data than in the model. The model also fails to reproduce the data's negative correlation of the policy rate with past inflation, and the authors have no good explanation. An ad hoc, possibly misspecified policy rule is one suspect. Even so, the model forecasts the rate well, and the other structural estimates are robust to alternative rule specifications.
- **Distinctive properties.**
  - Different shocks drive real and nominal variables; the variance decomposition makes this duality plain.
  - In comparable models for other countries, monetary policy reaches inflation more through domestic prices than through import prices, with both channels pushing the same way. In MOISE the two channels are about equally strong.
  - Transmission is fast: after a policy shock, inflation responds most in the same quarter and output one quarter later. The effects also fade quickly by international standards, partly reflecting the weak real and nominal frictions estimated for Israel.
  - Prices are re-optimized on average every 1.8–2.8 quarters across sectors, against a typical 3–4 quarters elsewhere.
- **Planned extensions.** The authors hope to present applications and extensions of the model in future work. Beyond forecasting and risk assessment, the model already serves research questions, notably counterfactual and other simulations assessing how monetary policy was actually conducted. The authors are also considering richer labor and financial markets, as other central banks have done after the recent global economic events.
