# Estimation data, filtering and methodology

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

4.1–4.3 data, filtering of the observed data and the estimation method; Appendix A (data) and Appendix B (model-consistent filtering). Equations (95)–(109). The data table is also in `data/appendixA_data.csv`.

<!-- Chunk T05. Part 1: Section 4 opening, 4.1-4.3 (PDF pages 40-47, printed 34-41). Part 2: Appendix A and Appendix B (PDF pages 93-100, printed 87-94). -->
<!-- Part 1 -->

# 4 Estimation of the model

**Summary.** The model is estimated on Israeli quarterly data for 1992:Q1–2009:Q4; the first 12 quarters only initialize the Kalman filter. The sample is full of structural transitions and breaks, so the data are filtered in a model-consistent way (4.2), which makes it possible to fit a cyclical, balanced-growth model. The model is log-linearized and estimated by Bayesian methods (4.3); calibration and priors, results and sensitivity analysis follow in 4.4–4.6, which are outside this chunk.

## 4.1 Data

**Summary.** Twenty-four quarterly series are used; most enter as log differences (94.i2), except interest rates, the VAT rate and the current account (entered as a share of GDP). Hours, employment and the domestic national-accounts aggregates are per capita, and every series is seasonally adjusted apart from interest and exchange rates, tax rates and the oil price. Nominal series (inflation rates, exchange-rate changes, nominal wage growth and interest rates) are detrended by subtracting the inflation target. Model labor is per-capita hours only, with no split into hours per worker and number of workers, so a "semi-theoretical" employment equation (95), following Smets and Wouters (2003) and Christoffel et al. (2008), lets employment data inform the hours gap.

<!-- kind: inline; id: 94.i2; section: 4.1; page: 34; pdf_page: 40 -->
**(94.i2) Default transformation of the observables: log difference**

$$
\Delta X_{t} \equiv \log\left(\frac{X_{t}}{X_{t-1}}\right)
$$

Meaning: Most observables enter as the log of the ratio of the current to the previous quarter's value.

### Observable variables as listed in Section 4.1 — page 35, pdf_page 41

The paper prints these in two columns: the first twelve rows below are the left column, the last twelve the right column.

| Series (as printed) | Symbol (as printed) |
|---|---|
| GDP | $\Delta Y_{t}$ |
| Private consumption | $\Delta C_{t}$ |
| Fixed capital investment | $\Delta I_{t}$ |
| Government consumption | $\Delta G_{t}$ |
| Exports | $\Delta X_{t}$ |
| Imports | $\Delta IM_{t}$ |
| GDP deflator | $\Delta P_{Y,t}^{M}$ |
| Export deflator | $\Delta P_{X,t}^{NIS} = \Delta\left(S_{t} P_{X,t}\right)$ |
| Current account | $s_{CA,t} = CA_{t}/P_{Y,t}^{M} Y_{t}$ |
| CPI | $\Delta P_{C,t}$ |
| Inflation target (annualized) | $4 \cdot \bar{\pi}_{t}$ |
| Nominal exchange rate | $\Delta S_{t}$ |
| Nominal hourly wage | $\Delta W_{t}$ |
| Hours worked | $\Delta N_{t}$ |
| Employment | $\Delta EM_{t}$ |
| Bank of Israel key interest rate | $r_{t}^{OB}$ |
| 5-10 year *fwd* real rate | $rr_{t}^{fwd,OB}$ |
| VAT rate | $\tau_{t}^{C}$ |
| G4 nominal interest rate | $r_{t}^{*,OB}$ |
| G4 CPI | $\Delta P_{Y,t}^{*}$ |
| G4 GDP | $\Delta Y_{t}^{*}$ |
| OECD imports | $\Delta WT_{t}^{*}$ |
| 5-10 year *fwd* G4 nominal interest rate | $r_{t}^{*,fwd,OB}$ |
| Price of oil | $\Delta P_{OIL,t}^{*}$ |

<!-- kind: inline; id: 94.i3; section: 4.1; page: 35; pdf_page: 41 -->
**(94.i3) Export deflator in domestic currency (observable definition)**

$$
\Delta P_{X,t}^{NIS} = \Delta\left(S_{t} P_{X,t}\right)
$$

Meaning: The shekel export-price observable is the log change of the exchange rate times the foreign-currency export price.

<!-- kind: inline; id: 94.i4; section: 4.1; page: 35; pdf_page: 41 -->
**(94.i4) Current account ratio (observable definition)**

$$
s_{CA,t} = CA_{t}/P_{Y,t}^{M} Y_{t}
$$

Meaning: The current-account observable is the current account divided by nominal GDP (market-price GDP deflator times real GDP).
Note: printed here with "$=$"; Appendix A (97.i104) prints the same definition with "$\equiv$".

<!-- kind: inline; id: 94.i5; section: 4.1; page: 35; pdf_page: 41 -->
**(94.i5) Annualized inflation target (observable)**

$$
4 \cdot \bar{\pi}_{t}
$$

Meaning: The inflation target is observed in annualized form, four times the quarterly target.

<!-- kind: eq; id: 95; section: 4.1; page: 36; pdf_page: 42 -->
**(95) Employment equation (employment adjusts gradually toward hours worked)**

$$
\begin{aligned}
\widehat{EM}_{t} ={}& \frac{\beta}{1+\beta \chi_{EM}} E_{t}\left[\widehat{EM}_{t+1}\right] + \frac{\chi_{EM}}{1+\beta \chi_{EM}} \widehat{EM}_{t-1} \\
&+ \frac{\left(1-\beta \xi_{EM}\right)\left(1-\xi_{EM}\right)}{\xi_{EM}\left(1+\beta \chi_{EM}\right)}\left(\hat{N}_{t} - \widehat{EM}_{t}\right) + \varepsilon_{t}^{EM}
\end{aligned}
\tag{95}
$$

Meaning: The employment deviation depends on its expected and lagged values and closes the gap to hours worked gradually, at a Calvo-like speed set by $\xi_{EM}$, plus a shock.
Note: the hat on $N$ is printed wide here and in the sentence below (95). It is written $\hat{N}$ under the single-letter rule and is the same variable as $\hat{N}_{t}$ in (99).

Hats denote log deviations from steady state. Employment is assumed to adjust slowly, while hours are flexible. A larger $\xi_{EM}$ means employment reacts less to hours, and $\chi_{EM}$ makes employment persistent. Footnote 20 says $\chi_{EM}$ is the authors' addition, absent from Smets and Wouters (2003) and Christoffel et al. (2008), meant to loosen the link between hours and employment. $\varepsilon_{t}^{EM}$ is not a structural shock and does not feed back into the rest of the model. The equation also serves to forecast employment from predicted hours, and footnote 21 calls it a form of "additive hybrid model".

## 4.2 Filtering the observed data

**Summary.** The sample spans many structural transitions (disinflation, capital-flow and exchange-rate liberalization, shifting pass-through, mass immigration, a changing export mix, a swing from current-account deficits to surpluses, a smaller government-spending share, growing openness), so many real aggregates trend at rates different from output (Figure 2). The model has a single balanced growth path set by productivity growth $g_{z}$; fitting raw data would force its transitory shocks to absorb the uneven trends, and univariate pre-filtering would discard information. Instead, excess trends are estimated jointly with the parameters and shocks ("additive hybrid models", Schorfheide 2011; Canova 2009), with the multivariate Kalman smoother removing only what the model's cyclical dynamics cannot explain. In a typical real-variable observation equation (95.u1) the shared trend splits into technology growth $\hat{g}_{z,t}$ and an AR trend in hours growth $GR_{t}^{N}$ (identified from hours and employment), plus an AR(1) idiosyncratic trend shock $EX_{t}$. Interest rates look non-stationary and are handled like trending variables, the two forward rates getting observation equations with unobserved time-varying term premia; Appendix B lists every observation equation.

**Figure 2: Observable Trending Variables (solid line) and Trends (dashed line).** (page 38, pdf_page 44)

- **Layout:** fifteen panels in a 5 × 3 grid. The x-axis ticks are at 1995, 2000, 2005 and 2010, and each series spans the sample.
  - Row 1: $N$, $EM$, $Y$.
  - Row 2: $C/Y$, $I/Y$, $G/Y$.
  - Row 3: $X/Y$, $IM/Y$, $Y^{*}$.
  - Row 4: $WT^{*}$, $S$, $W/P_{C}$.
  - Row 5: $P_{OIL}^{*}/P_{Y}^{*}$, "$rr^{fwd,OB}$ and $rr^{fwd}$", "$r^{*,fwd,OB}$ and $rr^{*,fwd}$".
- **Lines:** the solid line is the observed trending variable and the dashed line its estimated trend. In the two forward-rate panels the dashed line is the smoothed expected short real rate 5–10 years ahead (see B.4).
- **Figure note:** the trends come from the stochastic growth rate $g_{z}$ and the additive components of Section 4.2, and interest rates are annualized.
- **Scales:** each panel has its own y-axis scale; no units are stated.
- **Approximate reading:** in both forward-rate panels the observed rate lies above the smoothed expected real rate over the whole sample.

<!-- kind: display; id: 95.u1; section: 4.2; page: 39; pdf_page: 45 -->
**(95.u1) Typical observation equation for a real variable**

$$
\Delta X_{t} = \hat{x}_{t} - \hat{x}_{t-1} + J^{g} \cdot \left(\hat{g}_{z,t} + g_{z}\right) + J^{N} \cdot GR_{t}^{N} + EX_{t}
$$

Meaning: Observed growth equals the change in the model counterpart plus, via 0/1 selection indicators, technology growth and hours-trend growth, plus an AR(1) idiosyncratic trend shock $EX_{t}$.
Note: the hat on $g$ is printed wide, here and in the text below; it is written $\hat{g}_{z,t}$. This generic form has $\left(\hat{g}_{z,t} + g_{z}\right)$ with no $-1$, whereas (101) and (104) have $\hat{g}_{z,t} + \left(g_{z}-1\right)$. Transcribed as printed (see [transcription notes](transcription-notes/T05.md)).

## 4.3 Methodology

**Summary.** Estimation is full-information, likelihood-based and Bayesian (An and Schorfheide 2007), the standard approach for medium-scale policy DSGE models, and is run in Dynare 4 under Matlab. The posterior of model $M_{i}$'s parameters $\theta_{i}$ given data $y$ is likelihood (from the Kalman filter) times prior over the marginal data density (96); since that denominator does not involve $\theta_{i}$, the posterior is proportional to the kernel $K$ (97). With no analytical form available, the posterior mode is found by numerical optimization, and random-walk Metropolis–Hastings draws then give the posterior mean and selected intervals. Models are compared by Bayes factors, which under equal prior model probabilities equal the ratio of marginal data densities, each the kernel integrated over the parameters (97.u1).

<!-- kind: eq; id: 96; section: 4.3; page: 40; pdf_page: 46 -->
**(96) Posterior distribution of the parameters (Bayes' rule)**

$$
p\left(\theta_{i} \mid y, M_{i}\right) = \frac{p\left(y \mid \theta_{i}, M_{i}\right) p\left(\theta_{i} \mid M_{i}\right)}{p\left(y \mid M_{i}\right)}
\tag{96}
$$

Meaning: The posterior of model i's parameters given the data equals the likelihood times the prior, divided by the marginal density of the data under model i.

<!-- kind: inline; id: 96.i1; section: 4.3; page: 40; pdf_page: 46 -->
**(96.i1) Likelihood function**

$$
p\left(y \mid \theta_{i}, M_{i}\right)
$$

Meaning: The likelihood of the data given model i and its parameters; the paper evaluates it with the Kalman filter.

<!-- kind: inline; id: 96.i2; section: 4.3; page: 40; pdf_page: 46 -->
**(96.i2) Prior distribution**

$$
p\left(\theta_{i} \mid M_{i}\right)
$$

Meaning: The prior on model i's parameters, expressing the researcher's beliefs before seeing the data.

<!-- kind: eq; id: 97; section: 4.3; page: 40; pdf_page: 46 -->
**(97) Posterior kernel**

$$
p\left(\theta_{i} \mid y, M_{i}\right) \propto p\left(y \mid \theta_{i}, M_{i}\right) p\left(\theta_{i} \mid M_{i}\right) = K\left(\theta_{i} \mid y, M_{i}\right)
\tag{97}
$$

Meaning: Without the parameter-free denominator, the posterior is proportional to likelihood times prior, a product denoted by the kernel $K$.

<!-- kind: inline; id: 97.i1; section: 4.3; page: 40; pdf_page: 46 -->
**(97.i1) Posterior probability of model i (what the Bayes factor compares)**

$$
p\left(M_{i} \mid y\right)
$$

Meaning: Probability of model i given the data. The text says the Bayes factor $BF_{ij}$ compares these across models and calls them the models' "marginal likelihoods".

<!-- kind: display; id: 97.u1; section: 4.3; page: 41; pdf_page: 47 -->
**(97.u1) Bayes factor between models i and j**

$$
BF_{ij} = \frac{p\left(M_{i} \mid y\right)}{p\left(M_{j} \mid y\right)} = \frac{p\left(y \mid M_{i}\right)}{p\left(y \mid M_{j}\right)} = \frac{\int p\left(y \mid \theta_{i}, M_{i}\right) p\left(\theta_{i} \mid M_{i}\right) d\theta_{i}}{\int p\left(y \mid \theta_{j}, M_{j}\right) p\left(\theta_{j} \mid M_{j}\right) d\theta_{j}} = \frac{\int K\left(\theta_{i} \mid y, M_{i}\right) d\theta_{i}}{\int K\left(\theta_{j} \mid y, M_{j}\right) d\theta_{j}}
$$

Meaning: The Bayes factor is the ratio of posterior model probabilities. With equal prior model probabilities it equals the ratio of marginal data densities, which are the integrated kernels.

The text explains each equality in turn: the second applies Bayes' rule under equal prior probabilities of the two models, the third integrates out each model's parameters, and the last uses the kernel defined in (97).

<!-- Part 2 -->

# Appendices

## Appendix A The data

**Summary.** The estimation data are 24 quarterly series for 1992:Q1–2009:Q4. Unless a series is said to be treated differently, it enters as a one-quarter log difference (97.i101). Everything except interest and exchange rates, tax rates and the oil price is seasonally adjusted, and per-capita series are divided by the working-age population. The table below lists the series by the paper's six categories; defining expressions printed inside the list follow it as separate math blocks.

<!-- kind: inline; id: 97.i101; section: A; page: 87; pdf_page: 93 -->
**(97.i101) Default transformation of the observed series: log difference**

$$
\Delta X_{t} \equiv \log\left(x_{t}/x_{t-1}\right)
$$

Meaning: Unless stated otherwise, each observable is the log of the ratio of its current to its previous quarterly value.
Note: printed with upper-case $X_{t}$ on the left and lower-case $x_{t}$, $x_{t-1}$ inside the log. The Section 4.1 version (94.i2) is upper case throughout and uses a stacked fraction. Transcribed as printed (see [transcription notes](transcription-notes/T05.md)).

### Appendix A data series (a list in the paper, not a numbered table) — pages 87–90, pdf_pages 93–96

The "Definition" column is as printed, except where it is marked as condensed. The "Transformation / adjustment" column paraphrases what the paper says about each series or its group. The same rows are in `data/appendixA_data.csv`.

| Category | Series | Symbol | Definition (as printed) | Transformation / adjustment | Source |
|---|---|---|---|---|---|
| Real National Accounts data | Output | $\Delta Y_{t}$ | gross domestic product. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Real National Accounts data | Private consumption | $\Delta C_{t}$ | private consumption expenditure. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Real National Accounts data | Investment | $\Delta I_{t}$ | gross fixed capital formation excluding ships and aircraft. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Real National Accounts data | Government consumption | $\Delta G_{t}$ | general government consumption, excluding defence imports. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Real National Accounts data | Exports | $\Delta X_{t}$ | exports of goods and services, excluding diamonds and start-up companies. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Real National Accounts data | Imports | $\Delta IM_{t}$ | imports of goods and services, excluding defence imports, ships, aircraft and diamonds. | log difference; per capita, constant prices; seasonally adjusted by the CBS | Central Bureau of Statistics (CBS) |
| Prices and Inflation | CPI | $\Delta P_{C,t}$ | Consumer Price Index. (Condensed: fruit and vegetables, about 3% of the CPI, excluded throughout; housing also excluded from 1992 until 2006; from 2007 only fruit and vegetables excluded.) | log difference; changes in the VAT rate deducted, with a time-varying weight (footnote 51); inflation target subtracted, then seasonally adjusted | CBS |
| Prices and Inflation | Output price | $\Delta P_{Y,t}^{M}$ | GDP deflator in market prices. | log difference; inflation target subtracted, then seasonally adjusted; its observation equation includes a measurement error (footnote 52) | CBS national accounts data |
| Prices and Inflation | Export price in domestic currency | $\Delta P_{X,t}^{NIS} = \Delta\left(S_{t} P_{X,t}\right)$ | Deflator of exports excluding diamonds and start-up companies (in market prices). | log difference; inflation target subtracted, then seasonally adjusted | CBS National Accounts data |
| Prices and Inflation | Annualized inflation target | $4 \cdot \bar{\pi}_{t}$ | (no further description printed) | four times the quarterly target, as the symbol shows | Bank of Israel |
| Interest rates and the exchange rate | Nominal interest rate | $r_{t}^{OB}$ | Annualized key nominal interest rate set by the Bank of Israel. | level, not log-differenced (main-text data section); not seasonally adjusted; inflation target subtracted | Bank of Israel |
| Interest rates and the exchange rate | 5-10 year forward real interest rate | $rr_{t}^{fwd,OB}$ | The 5-10 years forward real interest rates, which are derived from indexed government bond yields. | level, not log-differenced (main-text data section); not seasonally adjusted | Bank of Israel |
| Interest rates and the exchange rate | Nominal exchange rate | $\Delta S_{t}$ | Israel's weighted nominal effective exchange rate against the currencies of its four major trading partners. (Condensed: weights US dollar 49%, Euro 32%, Sterling 13%, Yen 6%, taken from an OLS regression of a broader effective rate of more than 20 currencies on the four; an increase is a depreciation.) | log difference; not seasonally adjusted; inflation target subtracted from the change | Bank of Israel |
| Labor market data | Nominal hourly wage | $\Delta W_{t}$ | total wages divided by total hours worked. | log difference; inflation target subtracted; seasonally adjusted by the CBS | CBS and the National Insurance Institute |
| Labor market data | Hours worked | $\Delta N_{t}$ | Total hours worked per working-age population. | log difference; seasonally adjusted by the CBS | CBS and the National Insurance Institute |
| Labor market data | Employment | $\Delta EM_{t}$ | Total employees per working-age population. | log difference; seasonally adjusted by the CBS | CBS and the National Insurance Institute |
| Foreign data | G4 nominal interest rate | $r_{t}^{*,OB}$ | Weighted average of the nominal central bank key interest rates of the G4 countries. | level, not log-differenced (main-text data section); not seasonally adjusted; G4 aggregate; the paper prints one weight set after the foreign-data list (USA 49%, Euro area 32%, Britain 13%, Japan 6%) without saying which series it covers | Bloomberg |
| Foreign data | G4 CPI | $\Delta P_{Y,t}^{*}$ | Seasonally adjusted weighted average of the consumer price indices of the G4 countries. | log difference; seasonally adjusted; G4 aggregate; the paper prints one weight set after the foreign-data list (USA 49%, Euro area 32%, Britain 13%, Japan 6%) without saying which series it covers | OECD database |
| Foreign data | G4 GDP | $\Delta Y_{t}^{*}$ | Weighted average of the gross domestic product of the G4 countries, in fixed prices; seasonally adjusted by G4 agencies. | log difference; seasonally adjusted; G4 aggregate; the paper prints one weight set after the foreign-data list (USA 49%, Euro area 32%, Britain 13%, Japan 6%) without saying which series it covers | OECD database |
| Foreign data | OECD imports | $\Delta WT_{t}^{*}$ | Weighted average of the volume of OECD imports of goods and services; seasonally adjusted. | log difference; seasonally adjusted | OECD database |
| Foreign data | 5-10 year forward G4 nominal interest rate | $r_{t}^{*,fwd,OB}$ | The 5-10 years forward nominal interest rates, extracted from non-indexed government bond yields. | level, not log-differenced (main-text data section); not seasonally adjusted; G4 aggregate; the paper prints one weight set after the foreign-data list (USA 49%, Euro area 32%, Britain 13%, Japan 6%) without saying which series it covers | Bloomberg |
| Miscellaneous data | VAT rate | $\tau_{t}^{C}$ | VAT rate. | level, not log-differenced (main-text data section); not seasonally adjusted (tax rate) | Ministry of Finance |
| Miscellaneous data | Current account surplus | $s_{CA,t} \equiv CA_{t}/P_{Y,t}^{M} Y_{t}$ | Seasonally adjusted ratio of the current account surplus to nominal GDP. | share of GDP, not log-differenced; seasonally adjusted | CBS |
| Miscellaneous data | Oil price | $\Delta P_{OIL,t}^{*}$ | Price per barrel of Brent crude oil in terms of the effective exchange rate. | log difference; not seasonally adjusted | Bloomberg |

Note on the foreign weights: the paper says the foreign-data weights are the same as those of the nominal exchange rate, namely USA (49%), Euro area (32%), Britain (13%) and Japan (6%). It states them once, after the list of foreign series. The OECD source is printed as "Source OECD database" (no colon) for OECD imports.

### Real National Accounts data

**Summary.** These are six national-accounts aggregates, all per capita and at constant prices. Volatile, low-value-added subcomponents unrelated to the business cycle are left out (ships and aircraft, diamonds, start-ups, defence imports). Data on the SNA93 standard start only in 1995:Q1, so earlier quarters follow the previous standard. The CBS supplies all six series already seasonally adjusted.

### Prices and Inflation

**Summary.** Fruit and vegetables are removed from the CPI. Housing is also removed for 1992–2006, when most rental contracts were in dollars. Model CPI inflation ($\hat{\pi}_{C,t}$) is measured before indirect taxes, so VAT-rate changes are subtracted from observed CPI inflation, with a time-varying weight because rents carry no VAT (footnote 51). The GDP-deflator observation equation includes a measurement error (footnote 52). For these nominal price series, the inflation target is subtracted first and seasonal adjustment is done afterwards.

<!-- kind: inline; id: 97.i102; section: A; page: 88; pdf_page: 94 -->
**(97.i102) Export price in domestic currency (observable definition)**

$$
\Delta P_{X,t}^{NIS} = \Delta\left(S_{t} P_{X,t}\right)
$$

Meaning: The shekel export-price observable is the log change of the exchange rate times the foreign-currency export price.

<!-- kind: inline; id: 97.i103; section: A; page: 88; pdf_page: 94 -->
**(97.i103) Annualized inflation target (observable)**

$$
4 \cdot \bar{\pi}_{t}
$$

Meaning: The inflation-target observable is four times the quarterly target (annualized).

### Interest rates and the exchange rate

**Summary.** The policy rate is the Bank of Israel's annualized key rate, and the forward real rate comes from indexed government bond yields. The exchange rate is a four-currency effective rate (a rise is a depreciation), with weights from regressing a broader effective rate on those four currencies. None of these series is seasonally adjusted, and the inflation target is subtracted from the nominal rate and from the exchange-rate change.

### Labor market data

**Summary.** The hourly wage is the total wage bill over total hours, net of the inflation target. Hours and employment are both per working-age person. The data come from the National Insurance Institute and the CBS, and the CBS does the seasonal adjustment.

### Foreign data

**Summary.** The foreign variables are G4 aggregates (policy rate, CPI, GDP), OECD import volumes, and a G4 5–10 year forward nominal rate from non-indexed bonds. The weights are the exchange-rate weights: USA 49%, Euro area 32%, Britain 13%, Japan 6%.

### Miscellaneous data

**Summary.** This group contains the VAT rate (Ministry of Finance) and the current-account surplus as a share of nominal GDP (CBS). It also contains the Brent crude price per barrel in effective-exchange-rate terms (Bloomberg).

<!-- kind: inline; id: 97.i104; section: A; page: 90; pdf_page: 96 -->
**(97.i104) Current account surplus ratio (observable definition)**

$$
s_{CA,t} \equiv CA_{t}/P_{Y,t}^{M} Y_{t}
$$

Meaning: The current-account observable is the current-account surplus divided by nominal GDP (market-price deflator times real output).
Note: printed with "$\equiv$" here and with "$=$" in Section 4.1 (94.i4).

## Appendix B Model-consistent filtering

**Summary.** In the model, all real variables grow at one common rate, the labor-augmenting technology growth $\hat{g}_{z,t}$ (equation (18)). In the data, different aggregates trend at different speeds. Each observable therefore gets an explicitly modelled "excess trend", estimated together with the model; this appendix gives those trend processes and the observation equations built on them.

### B.1 Detrending employment variables

**Summary.** One secular growth component for per-capita hours, $GR_{t}^{N}$, follows an AR(1) process. It removes the excess trend from hours and employment and, through output, from the real domestic variables. Footnote 53 says the long-run growth of per-capita hours must strictly be zero. The AR means are treated as long-run growth rates only within the sample. The three observation equations below tie the observed growth rates of hours, employment and output per capita to model deviations from steady state.

<!-- kind: eq; id: 98; section: B.1; page: 91; pdf_page: 97 -->
**(98) Secular growth component of hours worked (AR(1))**

$$
GR_{t}^{N} = \left(1-\rho_{GR}^{N}\right) g_{\Delta N} + \rho_{GR}^{N} GR_{t-1}^{N} + \eta_{GR,t}^{N}
\tag{98}
$$

Meaning: Trend growth of per-capita hours is AR(1) around the long-run rate $g_{\Delta N}$, with estimated persistence $\rho_{GR}^{N}$ and an i.i.d. innovation $\eta_{GR,t}^{N}$.

<!-- kind: inline; id: 98.i1; section: B.1; page: 91; pdf_page: 97 -->
**(98.i1) Footnote 54: log deviation of stationarized output**

$$
\hat{y}_{t} = y_{t} - y
$$

Meaning: Hatted output is the deviation of stationarized log output from its steady-state value $y$.

<!-- kind: inline; id: 98.i2; section: B.1; page: 91; pdf_page: 97 -->
**(98.i2) Footnote 54: stationarized log output**

$$
y_{t} = \log\left(Y_{t}/z_{t}\right)
$$

Meaning: Real domestic variables are made stationary by dividing by the permanent technology level $z_{t}$; for output this gives the log of $Y_{t}/z_{t}$.
Note: the footnote calls $y$ "the steady state value of $Y_{t}/z_{t}$". Because $y_{t}$ is a log, $y$ should be the steady state of $y_{t}$, i.e. of the log ratio. The wording is kept as printed (see [transcription notes](transcription-notes/T05.md)).

<!-- kind: eq; id: 99; section: B.1; page: 91; pdf_page: 97 -->
**(99) Observation equation: hours worked**

$$
\Delta N_{t}^{OB} = \hat{N}_{t} - \hat{N}_{t-1} + GR_{t}^{N}
\tag{99}
$$

Meaning: Observed growth of per-capita hours equals the change in the hours deviation plus the secular hours-growth component.

<!-- kind: eq; id: 100; section: B.1; page: 92; pdf_page: 98 -->
**(100) Observation equation: employment**

$$
\Delta EM_{t}^{OB} = \widehat{EM}_{t} - \widehat{EM}_{t-1} + GR_{t}^{N}
\tag{100}
$$

Meaning: Observed employment-rate growth equals the change in the employment deviation plus the same secular hours-growth component.

<!-- kind: eq; id: 101; section: B.1; page: 92; pdf_page: 98 -->
**(101) Observation equation: per capita output (GDP)**

$$
\Delta Y_{t}^{OB} = \hat{y}_{t} - \hat{y}_{t-1} + \hat{g}_{z,t} + \left(g_{z}-1\right) + GR_{t}^{N}
\tag{101}
$$

Meaning: Observed per-capita GDP growth equals the change in stationarized output, plus technology growth ($\hat{g}_{z,t}$ plus the net steady-state rate $g_{z}-1$), plus secular hours growth.

The superscript $OB$ marks the observed variables, which still contain the excess trends, as distinct from their model counterparts.

### B.2 Detrending aggregate quantities of goods

**Summary.** Private consumption, investment, exports, imports, foreign GDP and world trade each have an AR(1) excess trend $EX_{t}^{J}$. Its mean is the component's long-run growth less technology growth and, for domestic components only, less hours growth; an indicator $j^{H}$ switches the hours term on. Government consumption has no AR process of its own: its excess trend follows from a share-weighted condition that keeps the long-run resource constraint satisfied. One observation equation, (104), then covers all seven real components. Footnote 55 says foreign excess growth is measured relative to $g_{z}$, and domestic excess growth relative to the long-run growth of observed GDP.

<!-- kind: inline; id: 101.i1; section: B.2; page: 92; pdf_page: 98 -->
**(101.i1) Components that have an AR excess-trend process**

$$
J \in \left\{C, I, X, IM, Y^{*}, WT^{*}\right\}
$$

Meaning: The AR excess-trend process (102) is specified for consumption, investment, exports, imports, foreign GDP and world trade (not government consumption).

<!-- kind: eq; id: 102; section: B.2; page: 92; pdf_page: 98 -->
**(102) Excess trend of component J (AR(1))**

$$
EX_{t}^{J} = \left(1-\rho_{EX}^{J}\right)\left(g_{\Delta J} - g_{z} - j^{H}\left(J\right) \cdot g_{\Delta N}\right) + \rho_{EX}^{J} EX_{t-1}^{J} + \eta_{EX,t}^{J}
\tag{102}
$$

Meaning: Each component's excess trend is AR(1) around its long-run excess growth, with estimated persistence $\rho_{EX}^{J}$ and an i.i.d. innovation $\eta_{EX,t}^{J}$.

<!-- kind: display; id: 102.u1; section: B.2; page: 92; pdf_page: 98 -->
**(102.u1) Domestic-component indicator function**

$$
j^{H}\left(J\right) = \left\{ \begin{array}{lll} 1 & if & J \in \left\{C, I, X, IM\right\} \\ 0 & if & J \in \left\{Y^{*}, WT^{*}\right\} \end{array} \right.
$$

Meaning: The indicator is one for domestic components, which carry the secular hours growth, and zero for foreign GDP and world trade.

<!-- kind: inline; id: 102.i1; section: B.2; page: 92; pdf_page: 98 -->
**(102.i1) Long-run (idiosyncratic) excess growth of component J**

$$
g_{\Delta J} - g_{z} - j^{H}\left(J\right) \cdot g_{\Delta N}
$$

Meaning: The assumed long-run growth $g_{\Delta J}$ of component J, less technology growth and, for domestic components, less hours growth.

<!-- kind: inline; id: 102.i2; section: B.2; page: 92; pdf_page: 98 -->
**(102.i2) Footnote 55: long-run growth rate of observed GDP**

$$
g_{z} + g_{\Delta N} - 1
$$

Meaning: Domestic components' excess growth is measured against this, the long-run growth of observed GDP; foreign variables' excess growth is measured against $g_{z}$.

<!-- kind: eq; id: 103; section: B.2; page: 93; pdf_page: 99 -->
**(103) Long-run resource-constraint condition on excess trends (determines government consumption)**

$$
s_{C} EX_{t}^{C} + s_{I} EX_{t}^{I} + s_{G} EX_{t}^{G} + s_{X} EX_{t}^{X} - s_{IM} EX_{t}^{IM} = 0
\tag{103}
$$

Meaning: The GDP-share-weighted excess trends of the expenditure components, with imports subtracted, sum to zero; this determines government consumption's excess trend $EX_{t}^{G}$.

<!-- kind: inline; id: 103.i1; section: B.2; page: 93; pdf_page: 99 -->
**(103.i1) Real components covered by the observation equation (104)**

$$
J \in \left\{C, I, G, X, IM, Y^{*}, WT^{*}\right\}
$$

Meaning: Observation equation (104) applies to all seven real components, including government consumption.

<!-- kind: inline; id: 103.i2; section: B.2; page: 93; pdf_page: 99 -->
**(103.i2) Stationarized component J (its log deviation from steady state is denoted $\hat{\jmath}_{t}$)**

$$
J_{t}/z_{t}
$$

Meaning: Each real component is scaled by technology $z_{t}$; $\hat{\jmath}_{t}$ is the log deviation of this ratio from its steady state.

<!-- kind: eq; id: 104; section: B.2; page: 93; pdf_page: 99 -->
**(104) Observation equation: real component J**

$$
\Delta J_{t}^{OB} = \hat{\jmath}_{t} - \hat{\jmath}_{t-1} + \hat{g}_{z,t} + \left(g_{z}-1\right) + j^{H} \cdot GR_{t}^{N} + EX_{t}^{J}
\tag{104}
$$

Meaning: Observed growth of component J equals the change in its stationarized deviation, plus technology growth, secular hours growth (domestic components only) and its own excess trend.
Note: $j^{H}$ is printed here without its argument $\left(J\right)$, unlike (102) and 102.u1.

### B.3 Detrending relative prices

**Summary.** Three relative prices also get model-consistent excess trends: the real exchange rate, the real hourly wage and the oil price relative to foreign prices. The exchange-rate and wage equations subtract the inflation-target deviation $\hat{\bar{\pi}}_{t}$, mirroring the target subtraction applied to the nominal data (Section 4.1). $EX_{t}^{S}$ and $EX_{t}^{W}$ are i.i.d. rather than AR, which avoids long-lived gaps between observed and model exchange-rate changes and treats the wage term as noise. The oil excess trend $EX_{t}^{P_{OIL}^{*}}$ is AR(1), zero in steady state, with persistence $\rho_{EX}^{P_{OIL}^{*}}$ (as in (102)), and can represent permanent relative-price shifts or simply observation error.

<!-- kind: eq; id: 105; section: B.3; page: 93; pdf_page: 99 -->
**(105) Observation equation: nominal exchange rate (depreciation)**

$$
\Delta S_{t}^{OB} = \hat{s}_{t} - \hat{s}_{t-1} + \left(\hat{\pi}_{Y,t} + \bar{\Pi} - 1\right) - \left(\hat{\pi}_{Y,t}^{*} + \bar{\Pi}^{*} - 1\right) - \hat{\bar{\pi}}_{t} + EX_{t}^{S}
\tag{105}
$$

Meaning: Observed depreciation equals the change in the real exchange rate, plus domestic minus foreign inflation (each deviation plus steady state), minus the target deviation, plus an i.i.d. term.
Note: the accent on $\pi$ is printed as a wide hat over a bar (here, in (106) and in (109)). It is written $\hat{\bar{\pi}}$, the notation EXAMPLE.md uses for the same variable.

<!-- kind: eq; id: 106; section: B.3; page: 93; pdf_page: 99 -->
**(106) Observation equation: nominal hourly wage**

$$
\Delta W_{t}^{OB} = \hat{w}_{t} + \hat{w}_{t-1} + \left(\hat{\pi}_{C,t} + \bar{\Pi} - 1\right) + \left(\hat{g}_{z,t} + g_{z} - 1\right) - \hat{\bar{\pi}}_{t} + EX_{t}^{W}
\tag{106}
$$

Meaning: Observed nominal wage growth links to the scaled real-wage terms, CPI inflation (deviation plus steady state) and technology growth, less the target deviation, plus i.i.d. noise.
Note: printed "$+\hat{w}_{t-1}$". Equations (99)–(105) and (107) all use the change $\hat{x}_{t}-\hat{x}_{t-1}$, and the text says (106) ties wage growth to the real-wage deviation, so "$-$" is probably intended. Transcribed as printed (see [transcription notes](transcription-notes/T05.md)).

<!-- kind: eq; id: 107; section: B.3; page: 93; pdf_page: 99 -->
**(107) Observation equation: oil price (foreign currency)**

$$
\Delta P_{OIL,t}^{*,OB} = \hat{p}_{OIL,t}^{*} - \hat{p}_{OIL,t-1}^{*} + \Delta P_{Y,t}^{*} + EX_{t}^{P_{OIL}^{*}}
\tag{107}
$$

Meaning: Observed quarterly oil-price growth equals the change in the relative oil price, plus foreign price inflation, plus an AR(1) excess-trend term.
Note: the foreign-inflation term is written $\Delta P_{Y,t}^{*}$, the symbol of the observed G4 CPI series, not a model term such as the $\hat{\pi}_{Y,t}^{*} + \bar{\Pi}^{*} - 1$ used in (105). Transcribed as printed.

<!-- kind: inline; id: 107.i1; section: B.3; page: 93; pdf_page: 99 -->
**(107.i1) Real exchange rate (level definition)**

$$
s_{t} = S_{t} \cdot P_{Y,t}^{*}/P_{Y,t}
$$

Meaning: The real exchange rate is the nominal rate times the foreign price level, divided by the domestic output price. $\hat{s}_{t}$ is its deviation from steady state.

<!-- kind: inline; id: 107.i2; section: B.3; page: 94; pdf_page: 100 -->
**(107.i2) Scaled real wage**

$$
w_{t} = \frac{W_{t}}{P_{C,t} z_{t}}
$$

Meaning: The nominal hourly wage, deflated by the CPI and scaled by technology. $\hat{w}_{t}$ is its log deviation from steady state.

<!-- kind: inline; id: 107.i3; section: B.3; page: 94; pdf_page: 100 -->
**(107.i3) Relative price of oil**

$$
p_{OIL.t}^{*} = P_{OIL,t}^{*}/P_{Y,t}^{*}
$$

Meaning: The relative oil price is the foreign-currency oil price divided by the foreign price level. $\hat{p}_{OIL,t}^{*}$ is its deviation from steady state.
Note: the left-hand subscript is printed "$OIL.t$", with a period, both here and in the $\hat{p}_{OIL.t}^{*}$ just before it; everywhere else it is "$OIL,t$". It is probably a typo for a comma. Transcribed as printed (see [transcription notes](transcription-notes/T05.md)).

### B.4 Smoothing of forward interest rates

**Summary.** The observed 5–10 year forward rates are tied to the short rates the model expects 5–10 years ahead; the domestic forward rate is real, the foreign one nominal, and the bracketed terms are multiplied by 4 because the data are annualized. Each equation adds a constant term premium ($tp$, $tp^{*}$, both estimated) to account for yield curves that normally slope upward, plus a serially correlated observation error that may also capture time variation in the premium. For the foreign rate, agents are assumed to expect average foreign inflation 5–10 years ahead to sit at its target ($\hat{\bar{\pi}}_{t}^{*}$). The appendix ends at the top of PDF p.101, noting that Figure 2 plots the observed forward rates against the smoothed expected real rates $\widehat{rr}_{t}^{fwd}$ and $\widehat{rr}_{t}^{*,fwd}$.

<!-- kind: eq; id: 108; section: B.4; page: 94; pdf_page: 100 -->
**(108) Observation equation: domestic 5-10 year forward real interest rate**

$$
rr_{t}^{fwd,OB} = 4 \cdot \left(\frac{g_{z}}{\beta} - 1 + \widehat{rr}_{t}^{fwd}\right) + tp + \varepsilon_{t}^{fwd,OB}
\tag{108}
$$

Meaning: The observed annualized forward real rate is four times the steady-state net real rate plus the expected real-rate deviation, plus a constant term premium and an observation error.

<!-- kind: eq; id: 109; section: B.4; page: 94; pdf_page: 100 -->
**(109) Observation equation: foreign 5-10 year forward nominal interest rate**

$$
r_{t}^{*,fwd,OB} = 4 \cdot \left(\frac{g_{z}}{\beta} \bar{\Pi}^{*} - 1 + \widehat{rr}_{t}^{*,fwd} + \hat{\bar{\pi}}_{t}^{*}\right) + tp^{*} + \varepsilon_{t}^{*,fwd,OB}
\tag{109}
$$

Meaning: The observed annualized foreign forward nominal rate is four times the steady-state net nominal rate plus expected real-rate and target-inflation deviations, plus a term premium and an error.

<!-- kind: inline; id: 109.i1; section: B.4; page: 94; pdf_page: 100 -->
**(109.i1) Steady-state (gross) real interest rate**

$$
g_{z}/\beta
$$

Meaning: Productivity growth divided by the discount factor gives the steady-state gross real interest rate used in (108) and (109).
