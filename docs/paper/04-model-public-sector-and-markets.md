# The model (Section 3): public sector, external sector, market clearing, foreign economy

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

3.3 Government and central bank, 3.4 net foreign assets and the current account, 3.5 market clearing, 3.6 the foreign economy. Equations (58)–(94).

## 3.3 The public sector

**Summary.** The public sector has two agents: a government that buys final goods, collects taxes and borrows, and a central bank that sets the short-term nominal interest rate according to a generalized, expectations-based Taylor-type rule.

### 3.3.1 The government

**Summary.** The government's period budget constraint equates spending plus maturing debt with tax revenue (VAT, labor-income and payroll taxes, taxes on net capital income and dividends, lump-sum taxes) plus newly issued debt. Productivity-adjusted government spending follows an AR(1) process, the VAT rate is close to a random walk, and all other tax rates are constant. Lump-sum taxes react to the gap between the debt-to-GDP ratio and its steady state; with distortionary tax rates fixed outside the model, households are Ricardian, so the choice of financing rule determines the debt path but leaves the rest of the model unchanged.

<!-- kind: eq; id: 58; section: 3.3.1; page: 24; pdf_page: 30 -->
**(58) Government budget constraint**

$$
\begin{aligned}
P_{G,t}G_{t} + B_{t} ={}& \tau_{t}^{C}P_{C,t}C_{t} + \left(\tau_{t}^{N} + \tau_{t}^{W_{h}}\right)\int_{0}^{1}W_{h,t}N_{h,t}dh + \tau^{W_{f}}W_{t}N_{t} \\
&+ \tau_{t}^{K}\left[R_{K,t}u_{t} - \left(\Gamma_{u}\left(u_{t}\right) + \delta\right)P_{I,t}\right]K_{t} + \tau_{t}^{D}D_{t} + T_{t} + R_{t}^{-1}B_{t+1}
\end{aligned}
\tag{58}
$$

Meaning: Government purchases plus maturing bonds are paid for by VAT, household labor and payroll taxes, firm payroll tax, capital-income and dividend taxes, lump-sum taxes and discounted new bond issues.

Note: $\tau^{W_{f}}$ is printed without a time subscript (unlike the other tax rates).

<!-- kind: eq; id: 59; section: 3.3.1; page: 24; pdf_page: 30 -->
**(59) Government spending process (AR(1))**

$$
g_{t} = \left(1-\rho_{G}\right)g + \rho_{G}g_{t-1} + \eta_{t}^{G}
\tag{59}
$$

Meaning: Productivity-adjusted government spending reverts toward its steady-state level $g$ with persistence $\rho_{G}$ and is hit by the innovation $\eta^{G}$.

<!-- kind: inline; id: 59.i1; section: 3.3.1; page: 24; pdf_page: 30 -->
**(59.i1) Stationarized government spending**

$$
g_{t} \equiv G_{t}/z_{t}
$$

Meaning: Government spending is detrended by the labor-augmenting productivity level $z_{t}$.

<!-- kind: eq; id: 60; section: 3.3.1; page: 25; pdf_page: 31 -->
**(60) VAT rate process (near random walk)**

$$
\tau_{t}^{C} = \left(1-0.99\right)\tau^{C} + 0.99\tau_{t-1}^{C} + \eta_{t}^{\tau^{C}}
\tag{60}
$$

Meaning: The VAT rate is an AR(1) with persistence fixed at 0.99 around its steady-state value $\tau^{C}$, driven by the innovation $\eta^{\tau^{C}}$.

<!-- kind: inline; id: 60.i1; section: 3.3.1; page: 25; pdf_page: 31 -->
**(60.i1) Tax rates assumed constant**

$$
\tau_{t}^{N}, \tau_{t}^{W_{h}}, \tau^{W_{f}}, \tau_{t}^{K} \text{ and } \tau_{t}^{D}
$$

Meaning: The income tax, the household and firm social-security taxes, the capital-income tax and the dividend tax are all held constant; only VAT varies over time.

<!-- kind: eq; id: 61; section: 3.3.1; page: 25; pdf_page: 31 -->
**(61) Fiscal financing rule (lump-sum taxes vs. debt)**

$$
s_{T,t} = \phi_{B}\left(s_{B,t+1} - s_{B}\right)
\tag{61}
$$

Meaning: Lump-sum taxes, as a share of GDP, are proportional to the deviation of the debt-to-GDP ratio from its steady-state value $s_{B}$.

<!-- kind: inline; id: 61.i1; section: 3.3.1; page: 25; pdf_page: 31 -->
**(61.i1) Lump-sum taxes as a share of GDP**

$$
s_{T,t} \equiv \frac{T_{t}}{P_{Y,t}Y_{t}}
$$

Meaning: Lump-sum taxes divided by nominal GDP.

<!-- kind: inline; id: 61.i2; section: 3.3.1; page: 25; pdf_page: 31 -->
**(61.i2) Government debt as a share of GDP**

$$
s_{B,t+1} \equiv \frac{B_{t+1}}{P_{Y,t}Y_{t}}
$$

Meaning: Outstanding government debt issued in period $t$ divided by period-$t$ nominal GDP.

<!-- kind: inline; id: 61.i3; section: 3.3.1; page: 25; pdf_page: 31 -->
**(61.i3) Long-run convergence of government debt**

$$
E_{t}\left[s_{B,t+\infty}\right] \rightarrow s_{B}
$$

Meaning: Under rule (61), the debt-to-GDP ratio is expected to return to its steady-state level eventually.

### 3.3.2 The central bank

**Summary.** Monetary policy follows a log-linear, generalized Taylor (1993)-type rule with interest-rate smoothing. The rule's target term combines the forward real interest rate (average expected real rate 5 to 10 years ahead), the time-varying inflation target, the gap between a four-quarter inflation measure (two past quarters, the current one and one expected quarter of CPI inflation) and the target, the output gap relative to a technology-driven trend, and nominal depreciation. The inflation target follows a near random walk to capture the disinflation in the first half of the sample, the forward rate is driven by the highly persistent domestic risk-premium shock $\varepsilon_{t}^{DRP}$ (footnote 18 refers back to section 3.1 and footnote 7), and the policy shock is white noise.

<!-- kind: eq; id: 62; section: 3.3.2; page: 25; pdf_page: 31 -->
**(62) Monetary policy (interest-rate) rule**

$$
\begin{aligned}
\hat{r}_{t} ={}& \left(1-\phi_{R}\right)\left[\widehat{rr}_{t}^{fwd} + \hat{\bar{\pi}}_{t} + \phi_{\Pi}\left(\hat{\pi}_{t}^{CB} - \hat{\bar{\pi}}_{t}\right) + \phi_{y}\hat{y}_{t}^{GAP} + \phi_{\Delta S}\Delta S_{t}\right] \\
&+ \phi_{R}\hat{r}_{t-1} + \eta_{t}^{R}
\end{aligned}
\tag{62}
$$

Meaning: Policy rate = weighted average of its lag and a target (forward real rate + inflation target + responses to the inflation gap, output gap and depreciation), plus a shock.

Note: the inflation target is printed with a wide hat over a full-width bar; encoded as $\hat{\bar{\pi}}_{t}$ (hat over bar over $\pi$) per CONVENTIONS §4.5 — see notes.

<!-- kind: inline; id: 62.i1; section: 3.3.2; page: 25; pdf_page: 31 -->
**(62.i1) Output gap (deviation from technology-driven trend)**

$$
\hat{y}_{t}^{GAP} \equiv \log\frac{Y_{t}}{Z_{t}\varepsilon_{t}} - \log y
$$

Meaning: Log output relative to the product of productivity and the transitory technology shock, measured against its steady-state value $y$.

Note: $Z_{t}$ is printed in upper case here, while productivity is lower-case $z_{t}$ elsewhere (e.g. 59.i1); transcribed as printed — see notes.

<!-- kind: inline; id: 62.i2; section: 3.3.2; page: 25; pdf_page: 31 -->
**(62.i2) Nominal depreciation**

$$
\Delta S_{t} \equiv \Delta\hat{s}_{t} + \hat{\pi}_{Y,t} - \hat{\pi}_{Y,t}^{*}
$$

Meaning: Nominal depreciation equals the change in the real exchange rate plus the gap between domestic and foreign inflation of the $P_{Y}$ prices.

<!-- kind: eq; id: 63; section: 3.3.2; page: 26; pdf_page: 32 -->
**(63) Forward real interest rate (average expected real rate 5 to 10 years ahead)**

$$
\widehat{rr}_{t}^{fwd} = \frac{1}{20}E_{t}\left[\widehat{ri}_{t+21} + \widehat{ri}_{t+22} + \cdots + \widehat{ri}_{t+39} + \widehat{ri}_{t+40}\right]
\tag{63}
$$

Meaning: The forward real rate is the mean of the expected one-quarter real rates from 21 to 40 quarters ahead.

Note: Appendix D eq. (262) (p.118) sums the terms from $t+20$ to $t+39$ instead — see notes.

<!-- kind: inline; id: 63.i1; section: 3.3.2; page: 26; pdf_page: 32 -->
**(63.i1) Real interest rate (log-linearized)**

$$
\widehat{ri}_{t} \equiv \hat{r}_{t} - E_{t}\hat{\pi}_{C,t+1}
$$

Meaning: The real rate is the nominal policy rate minus expected next-quarter CPI inflation.

Note: the hats on $r$ and $\pi$ are printed wide; encoded with \hat (single base letter), consistent with (62) — see notes.

<!-- kind: inline; id: 63.i2; section: 3.3.2; page: 26; pdf_page: 32 -->
**(63.i2) Shock driving the forward real rate**

$$
\varepsilon_{t}^{DRP}
$$

Meaning: The forward real rate is driven by the domestic, highly inertial risk-premium shock (see section 3.1 and footnote 7).

<!-- kind: eq; id: 64; section: 3.3.2; page: 26; pdf_page: 32 -->
**(64) Time-varying inflation target (near random walk)**

$$
\hat{\bar{\pi}}_{t} = 0.99\hat{\bar{\pi}}_{t-1} + \eta_{t}^{\bar{\Pi}}
\tag{64}
$$

Meaning: The inflation target is an AR(1) with persistence fixed at 0.99, driven by the innovation $\eta^{\bar{\Pi}}$.

Note: the target is printed with a wide hat over a full-width bar (as in (62)); the bar over $\Pi$ in the shock superscript is printed full-width. Encoded as \hat{\bar{\pi}} and \bar{\Pi} — see notes.

<!-- kind: eq; id: 65; section: 3.3.2; page: 26; pdf_page: 32 -->
**(65) Inflation measure the central bank reacts to**

$$
\hat{\pi}_{t}^{CB} = E_{t}\left[\hat{\pi}_{C,t-2} + \hat{\pi}_{C,t-1} + \hat{\pi}_{C,t} + \hat{\pi}_{C,t+1}\right]
\tag{65}
$$

Meaning: The central bank's inflation measure sums CPI inflation over two past quarters, the current quarter and the expected next quarter.

Note: printed as a plain sum (no 1/4 factor); Appendix D eq. (265) (p.119) prints 0.25 times the same four terms — see notes.

<!-- kind: inline; id: 65.i1; section: 3.3.2; page: 26; pdf_page: 32 -->
**(65.i1) Policy shock assumption**

$$
\eta_{t}^{R}
$$

Meaning: The monetary policy shock is assumed to be white noise.

## 3.4 Net foreign assets and the current account

**Summary.** The trade balance is export revenue (foreign-currency export price times the exchange rate times exports) minus spending on imports, and the current account adds exogenous foreign transfers. Net foreign assets, held as foreign-currency bonds, accumulate with the current account converted into foreign currency. Foreign transfers, measured as a share of nominal GDP, follow an AR(1) process.

<!-- kind: eq; id: 66; section: 3.4; page: 26; pdf_page: 32 -->
**(66) Trade balance**

$$
TB_{t} = P_{X,t}S_{t}X_{t} - P_{IM,t}IM_{t}
\tag{66}
$$

Meaning: Export revenue in domestic currency minus the value of imports.

<!-- kind: eq; id: 67; section: 3.4; page: 26; pdf_page: 32 -->
**(67) Current account**

$$
CA_{t} = TB_{t} + FTR_{t}
\tag{67}
$$

Meaning: The current account is the trade balance plus exogenous foreign transfers.

<!-- kind: eq; id: 68; section: 3.4; page: 27; pdf_page: 33 -->
**(68) Law of motion of net foreign assets**

$$
(R_{t}^{*})^{-1}B_{t+1}^{*} = B_{t}^{*} + \frac{CA_{t}}{S_{t}}
\tag{68}
$$

Meaning: The discounted value of next period's foreign-currency bond holdings equals current holdings plus the current account expressed in foreign currency.

<!-- kind: inline; id: 68.i1; section: 3.4; page: 27; pdf_page: 33 -->
**(68.i1) Foreign transfers as a share of nominal GDP**

$$
s_{FTR,t} = \frac{FTR_{t}}{P_{Y,t}Y_{t}}
$$

Meaning: Foreign transfers divided by nominal GDP.

<!-- kind: eq; id: 69; section: 3.4; page: 27; pdf_page: 33 -->
**(69) Foreign transfers process (AR(1))**

$$
s_{FTR,t} = \left(1-\rho_{FTR}\right)s_{FTR} + \rho_{FTR}\cdot s_{FTR,t-1} + \eta_{t}^{FTR}
\tag{69}
$$

Meaning: The transfers-to-GDP ratio reverts to its steady-state value with persistence $\rho_{FTR}$ and is driven by the innovation $\eta^{FTR}$.

## 3.5 Market-clearing conditions

**Summary.** This section aggregates the firm- and household-level conditions into market-clearing relations for labor, capital, intermediate goods (domestic and imported) and final goods, derives the aggregate nominal resource constraint (at factor and at market prices), defines real output, and expresses profits as a share of GDP.

### 3.5.1 Clearing of the labor market

**Summary.** Each household's hours equal the total use of its labor by all intermediate-goods firms. Aggregating over households with the labor-demand function links the simple sum of hours to the production-relevant (CES) labor aggregate through a wage-dispersion term, and total payroll equals the aggregate wage times the labor aggregate.

<!-- kind: eq; id: 70; section: 3.5.1; page: 27; pdf_page: 33 -->
**(70) Labor-market clearing for household h**

$$
N_{h,t} = \int_{0}^{1}N_{f,t}^{h}df
\tag{70}
$$

Meaning: Hours supplied by household $h$ equal the sum over firms of the labor of type $h$ they employ.

<!-- kind: inline; id: 70.i1; section: 3.5.1; page: 27; pdf_page: 33 -->
**(70.i1) Household index range**

$$
h \in [0,1]
$$

Meaning: Households form a continuum on the unit interval.

<!-- kind: eq; id: 71; section: 3.5.1; page: 27; pdf_page: 33 -->
**(71) Aggregate hours and the labor aggregate**

$$
\int_{0}^{1}N_{h,t}dh = \int_{0}^{1}\left(\frac{W_{h,t}}{W_{t}}\right)^{-\frac{\varphi_{t}^{W}}{\varphi_{t}^{W}-1}}\cdot N_{t}\cdot dh = \check{s}_{W,t}\cdot N_{t}
\tag{71}
$$

Meaning: Total hours equal the production-relevant labor aggregate scaled by a wage-dispersion factor.

<!-- kind: inline; id: 71.i1; section: 3.5.1; page: 27; pdf_page: 33 -->
**(71.i1) Wage dispersion measure**

$$
\check{s}_{W,t} \equiv \int_{0}^{1}\left(\frac{W_{h,t}}{W_{t}}\right)^{-\frac{\varphi_{t}^{W}}{\varphi_{t}^{W}-1}}\cdot dh
$$

Meaning: Integral over households of relative wages raised to the labor-demand elasticity; it measures wage dispersion.

<!-- kind: inline; id: 71.i2; section: 3.5.1; page: 27; pdf_page: 33 -->
**(71.i2) Production-relevant aggregate of labor services**

$$
N_{t} \equiv \int_{0}^{1}N_{f,t}\cdot df = \int_{0}^{1}\left[\left(\int_{0}^{1}\left(N_{f,t}^{h}\right)^{\frac{1}{\varphi_{t}^{W}}}dh\right)^{\varphi_{t}^{W}}\right]df
$$

Meaning: The aggregate labor input sums over firms each firm's CES composite of household-specific labor.

<!-- kind: eq; id: 72; section: 3.5.1; page: 28; pdf_page: 34 -->
**(72) Total payroll**

$$
\int_{0}^{1}N_{h,t}\cdot W_{h,t}\cdot dh = N_{t}\int_{0}^{1}W_{h,t}\left(\frac{W_{h,t}}{W_{t}}\right)^{-\frac{\varphi_{t}^{W}}{\varphi_{t}^{W}-1}}dh = W_{t}N_{t}
\tag{72}
$$

Meaning: Using labor demand and the wage index (22), the economy's wage bill equals the aggregate wage times the labor aggregate.

### 3.5.2 Clearing of the capital market

**Summary.** Firms' total demand for capital services equals the utilized capital stock supplied by households.

<!-- kind: inline; id: 72.i1; section: 3.5.2; page: 28; pdf_page: 34 -->
**(72.i1) Aggregate demand for capital services**

$$
K_{t}^{s} \equiv \int_{0}^{1}K_{f,t}^{s}df
$$

Meaning: Total capital services rented by intermediate-goods firms.

<!-- kind: inline; id: 72.i2; section: 3.5.2; page: 28; pdf_page: 34 -->
**(72.i2) Aggregate utilized capital stock**

$$
u_{t}K_{t} \equiv \int_{0}^{1}u_{h,t}K_{h,t}dh
$$

Meaning: Utilization-weighted capital summed over households.

<!-- kind: eq; id: 73; section: 3.5.2; page: 28; pdf_page: 34 -->
**(73) Capital-market clearing**

$$
u_{t}K_{t} = K_{t}^{s}
\tag{73}
$$

Meaning: Utilized capital supplied by households equals capital services demanded by firms.

### 3.5.3 Intermediate-goods market clearing

**Summary.** Each domestic intermediate-goods firm's output meets the demand from the four final-goods sectors (consumption, investment, government, exports). Aggregating with the CES demand function links the simple sum of firm supplies to the sum of the sectoral production aggregates through a price-dispersion term, and aggregate nominal spending equals the price index times the aggregate. Imported intermediate goods are treated the same way.

#### Domestic intermediate goods

<!-- kind: eq; id: 74; section: 3.5.3; page: 28; pdf_page: 34 -->
**(74) Market clearing for firm f's domestic intermediate good**

$$
H_{f,t}^{s} = H_{f,t}^{C} + H_{f,t}^{I} + H_{f,t}^{G} + H_{f,t}^{X}
\tag{74}
$$

Meaning: Firm $f$'s supply equals the demand for its good from the C, I, G and X final-goods sectors.

<!-- kind: display; id: 74.u1; section: 3.5.3; page: 28; pdf_page: 34 -->
**(74.u1) Aggregated supply of domestic intermediate goods (using (39))**

$$
\int_{0}^{1}H_{f,t}^{s}\cdot df = \int_{0}^{1}\left(\frac{P_{H,f,t}}{P_{H,t}}\right)^{-\frac{\varphi_{t}^{H}}{\varphi_{t}^{H}-1}}\cdot H_{t}\cdot df
$$

Meaning: Summing (74) over firms with the CES demand gives total supply as relative prices raised to the demand elasticity times the aggregate $H_{t}$.

<!-- kind: inline; id: 74.i1; section: 3.5.3; page: 28; pdf_page: 34 -->
**(74.i1) Sum of sectoral aggregates of domestic intermediate goods**

$$
H_{t} \equiv H_{t}^{C} + H_{t}^{I} + H_{t}^{G} + H_{t}^{X}
$$

Meaning: Adds the production-relevant aggregates of domestic intermediate goods used by the four final-goods sectors.

<!-- kind: inline; id: 74.i2; section: 3.5.3; page: 28; pdf_page: 34 -->
**(74.i2) Simple sum of domestic intermediate supply**

$$
H_{t}^{s} \equiv \int_{0}^{1}H_{f,t}^{s}\cdot df
$$

Meaning: Unweighted integral of all firms' output of domestic intermediate goods.

<!-- kind: inline; id: 74.i3; section: 3.5.3; page: 28; pdf_page: 34 -->
**(74.i3) Price dispersion of domestic intermediate goods**

$$
\check{s}_{H,t} \equiv \int_{0}^{1}\left(\frac{P_{H,f,t}}{P_{H,t}}\right)^{-\frac{\varphi_{t}^{H}}{\varphi_{t}^{H}-1}}df
$$

Meaning: Integral of relative firm prices raised to the demand elasticity; it measures domestic price dispersion.

<!-- kind: eq; id: 75; section: 3.5.3; page: 29; pdf_page: 35 -->
**(75) Domestic intermediate supply vs. production aggregate**

$$
H_{t}^{s} = \check{s}_{H,t}H_{t}
\tag{75}
$$

Meaning: Total supply of domestic intermediate goods is the production aggregate scaled by price dispersion.

<!-- kind: eq; id: 76; section: 3.5.3; page: 29; pdf_page: 35 -->
**(76) Aggregate nominal expenditure on domestic intermediate goods**

$$
\int_{0}^{1}P_{H,f,t}H_{f,t}^{s}df = H_{t}\int_{0}^{1}P_{H,f,t}\left(\frac{P_{H,f,t}}{P_{H,t}}\right)^{-\frac{\varphi_{t}^{H}}{\varphi_{t}^{H}-1}}df = P_{H,t}H_{t}
\tag{76}
$$

Meaning: Using (74), demand (39) and the price index (41), total spending on domestic intermediates equals the price index times the aggregate.

#### Imported intermediate goods

<!-- kind: inline; id: 76.i1; section: 3.5.3; page: 29; pdf_page: 35 -->
**(76.i1) Price dispersion of imported intermediate goods**

$$
\check{s}_{IM,t} \equiv \int_{0}^{1}\left(\frac{P_{IM,f^{*},t}}{P_{IM,t}}\right)^{-\frac{\varphi_{t}^{*}}{\varphi_{t}^{*}-1}}df^{*}
$$

Meaning: Integral of relative import prices raised to the import-demand elasticity; it measures import price dispersion.

<!-- kind: inline; id: 76.i2; section: 3.5.3; page: 29; pdf_page: 35 -->
**(76.i2) Simple sum of imported intermediate goods**

$$
IM_{t}^{s} \equiv \int_{0}^{1}IM_{f^{*},t}df^{*}
$$

Meaning: Unweighted integral of the imported goods supplied by all foreign intermediate-goods firms.

<!-- kind: eq; id: 77; section: 3.5.3; page: 29; pdf_page: 35 -->
**(77) Market clearing for foreign firm f*'s imported good**

$$
IM_{f^{*},t} = IM_{f^{*},t}^{C} + IM_{f^{*},t}^{I} + IM_{f^{*},t}^{G} + IM_{f^{*},t}^{X}
\tag{77}
$$

Meaning: Each imported variety's supply equals the demand for it from the C, I, G and X final-goods sectors.

<!-- kind: eq; id: 78; section: 3.5.3; page: 29; pdf_page: 35 -->
**(78) Imported supply vs. production aggregate**

$$
IM_{t}^{s} = \check{s}_{IM,t}IM_{t}
\tag{78}
$$

Meaning: Total imported supply is the import aggregate scaled by import price dispersion.

<!-- kind: eq; id: 79; section: 3.5.3; page: 29; pdf_page: 35 -->
**(79) Aggregate nominal expenditure on imported intermediate goods**

$$
\int_{0}^{1}P_{IM,f^{*},t}IM_{f^{*},t}df^{*} = P_{IM,t}IM_{t}
\tag{79}
$$

Meaning: Total spending on imported varieties equals the import price index times the import aggregate.

<!-- kind: inline; id: 79.i1; section: 3.5.3; page: 29; pdf_page: 35 -->
**(79.i1) Sum of sectoral import aggregates**

$$
IM_{t} \equiv IM_{t}^{C} + IM_{t}^{I} + IM_{t}^{G} + IM_{t}^{X}
$$

Meaning: Adds the import aggregates used by the four final-goods sectors.

### 3.5.4 Clearing of the final goods markets

**Summary.** Consumption-goods output equals consumption, investment-goods output covers fixed investment, capital-utilization costs and the change in inventories, and government-goods output equals government purchases. In the export sector, the homogeneous export good bought by exporters equals their differentiated output plus the fixed brand-naming cost; using the demand for exporters' goods and an export price-dispersion term links export-goods production to the utility-based export aggregate.

<!-- kind: eq; id: 80; section: 3.5.4; page: 30; pdf_page: 36 -->
**(80) Consumption-goods market clearing**

$$
Q_{t}^{C} = C_{t}
\tag{80}
$$

Meaning: Output of final consumption goods equals aggregate consumption.

<!-- kind: eq; id: 81; section: 3.5.4; page: 30; pdf_page: 36 -->
**(81) Investment-goods market clearing**

$$
Q_{t}^{I} = I_{t} + \Gamma_{u}\left(u_{h,t}\right)\cdot K_{t} + \Delta INV_{t}
\tag{81}
$$

Meaning: Output of investment goods covers fixed investment, the resource cost of capital utilization and the change in inventories.

<!-- kind: eq; id: 82; section: 3.5.4; page: 30; pdf_page: 36 -->
**(82) Government-goods market clearing**

$$
Q_{t}^{G} = G_{t}
\tag{82}
$$

Meaning: Output of government-consumption goods equals government purchases.

<!-- kind: display; id: 82.u1; section: 3.5.4; page: 30; pdf_page: 36 -->
**(82.u1) Export-sector market clearing**

$$
Q_{t}^{X} = \int_{0}^{1}Q_{f^{X},t}\cdot df^{X} = \int_{0}^{1}X_{f^{X},t}\cdot df^{X} + \int_{0}^{1}\psi^{X}\cdot z_{t}\cdot df^{X}
$$

Meaning: The homogeneous export good is fully bought by exporters; by production function (46) this equals their differentiated output plus the fixed cost $\psi^{X}z_{t}$.

<!-- kind: inline; id: 82.i1; section: 3.5.4; page: 30; pdf_page: 36 -->
**(82.i1) Price dispersion in the export sector**

$$
\check{s}_{X,t} \equiv \int_{0}^{1}\left(\frac{P_{X,f^{X},t}}{P_{X,t}}\right)^{-\frac{\varphi_{t}^{X}}{\varphi_{t}^{X}-1}}\cdot df^{X}
$$

Meaning: Integral of exporters' relative prices raised to the demand elasticity; it measures export price dispersion.

<!-- kind: eq; id: 83; section: 3.5.4; page: 30; pdf_page: 36 -->
**(83) Export-goods production vs. export aggregate**

$$
Q_{t}^{X} = \check{s}_{X,t}\cdot X_{t} + \psi^{X}\cdot z_{t}
\tag{83}
$$

Meaning: Production of export goods equals the utility-based export aggregate scaled by price dispersion, plus exporters' fixed cost.

### 3.5.5 Aggregate resource constraints

**Summary.** Nominal GDP is the economy's value added: the value of domestic intermediate output plus exporters' value added, since perfectly competitive firms add no value. Using zero-profit conditions and market clearing gives the expenditure-side nominal resource constraint, in which each sector's imports are scaled by its import-intensity adjustment-cost terms; adding VAT gives the version at market prices used for estimation. Real output is defined as the output of domestic intermediate-goods firms; footnote 19 explains that this split of nominal output into real output and a deflator is needed to map the model to the data and to define the output gap in rule (62), and that real output excludes exporters' monopoly profits although nominal output (84) includes them.

<!-- kind: inline; id: 83.i1; section: 3.5.5; page: 31; pdf_page: 37 -->
**(83.i1) Nominal GDP**

$$
P_{Y,t}Y_{t}
$$

Meaning: Defines nominal GDP as the total value added produced in the domestic economy.

<!-- kind: eq; id: 84; section: 3.5.5; page: 31; pdf_page: 37 -->
**(84) Nominal GDP as value added**

$$
P_{Y,t}Y_{t} = P_{H,t}H_{t}^{s} + S_{t}P_{X,t}X_{t} - P_{DX,t}Q_{t}^{X}
\tag{84}
$$

Meaning: Nominal GDP equals the value of domestic intermediate output plus exporters' revenue minus their cost of the homogeneous export good.

<!-- kind: eq; id: 85; section: 3.5.5; page: 31; pdf_page: 37 -->
**(85) Aggregate nominal resource constraint**

$$
\begin{aligned}
P_{Y,t}Y_{t} ={}& P_{C,t}C_{t} + P_{I,t}\left(I_{t} + \Gamma_{u}\left(u_{h,t}\right)K_{t} + \Delta INV_{t}\right) + P_{G,t}G_{t} + S_{t}P_{X,t}X_{t} \\
&- P_{IM,t}\left(IM_{t}^{C}\frac{1-\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{C}}^{\dagger}\left(IM_{t}^{C}/Q_{t}^{C};\epsilon_{t}^{IM}\right)} + IM_{t}^{I}\frac{1-\Gamma_{IM^{I}}\left(IM_{t}^{I}/Q_{t}^{I};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{I}}^{\dagger}\left(IM_{t}^{I}/Q_{t}^{I};\epsilon_{t}^{IM}\right)}\right) \\
&- P_{IM,t}\left(IM_{t}^{G}\frac{1-\Gamma_{IM^{G}}\left(IM_{t}^{G}/Q_{t}^{G};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{G}}^{\dagger}\left(IM_{t}^{G}/Q_{t}^{G};\epsilon_{t}^{IM}\right)} + IM_{t}^{X}\frac{1-\Gamma_{IM^{X}}\left(IM_{t}^{X}/Q_{t}^{X};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{X}}^{\dagger}\left(IM_{t}^{X}/Q_{t}^{X};\epsilon_{t}^{IM}\right)}\right)
\end{aligned}
\tag{85}
$$

Meaning: Nominal GDP equals consumption, investment (incl. utilization costs and inventories), government and export spending, minus imports in each sector adjusted by that sector's import-intensity adjustment-cost terms.

Note: the import shock is printed here as lunate $\epsilon_{t}^{IM}$ (in (38) it is $\varepsilon_{t}^{IM}$) — transcribed as printed; see notes.

<!-- kind: eq; id: 86; section: 3.5.5; page: 31; pdf_page: 37 -->
**(86) Aggregate resource constraint at market prices (including VAT)**

$$
\begin{aligned}
P_{Y,t}^{M}Y_{t} ={}& \left(1+\tau_{t}^{C}\right)P_{C,t}C_{t} + P_{I,t}\left(I_{t} + \Gamma_{u}\left(u_{h,t}\right)K_{t} + \Delta INV_{t}\right) + P_{G,t}G_{t} + S_{t}P_{X,t}X_{t} \\
&- P_{IM,t}\left(IM_{t}^{C}\frac{1-\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{C}}^{\dagger}\left(IM_{t}^{C}/Q_{t}^{C};\epsilon_{t}^{IM}\right)} + IM_{t}^{I}\frac{1-\Gamma_{IM^{I}}\left(IM_{t}^{I}/Q_{t}^{I};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{I}}^{\dagger}\left(IM_{t}^{I}/Q_{t}^{I};\epsilon_{t}^{IM}\right)}\right) \\
&- P_{IM,t}\left(IM_{t}^{G}\frac{1-\Gamma_{IM^{G}}\left(IM_{t}^{G}/Q_{t}^{G};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{G}}^{\dagger}\left(IM_{t}^{G}/Q_{t}^{G};\epsilon_{t}^{IM}\right)} + IM_{t}^{X}\frac{1-\Gamma_{IM^{X}}\left(IM_{t}^{X}/Q_{t}^{X};\epsilon_{t}^{IM}\right)}{\Gamma_{IM^{X}}^{\dagger}\left(IM_{t}^{X}/Q_{t}^{X};\epsilon_{t}^{IM}\right)}\right)
\end{aligned}
\tag{86}
$$

Meaning: Same constraint as (85) but with consumption valued including VAT, giving nominal GDP at market prices $P_{Y,t}^{M}Y_{t}$.

Note: as in (85), the import shock is printed as lunate $\epsilon_{t}^{IM}$.

<!-- kind: eq; id: 87; section: 3.5.5; page: 32; pdf_page: 38 -->
**(87) Definition of real output**

$$
Y_{t} = H_{t}^{s}
\tag{87}
$$

Meaning: Real output is defined as total output of the domestic intermediate-goods firms (produced with domestic labor and capital).

### 3.5.6 The share of profits

**Summary.** Profits of domestic intermediate-goods firms and exporters are revenue minus marginal cost times (output plus fixed cost); aggregating with the dispersion terms and using (84) expresses total profits as a share of nominal GDP.

<!-- kind: eq; id: 88; section: 3.5.6; page: 32; pdf_page: 38 -->
**(88) Aggregate profits of domestic intermediate-goods firms and exporters**

$$
\begin{aligned}
D_{t} \equiv{}& \int_{0}^{1}D_{H,f,t}df + \int_{0}^{1}D_{X,f^{X},t}df^{X} = \\
={}& \int_{0}^{1}\left[P_{H,f,t}H_{f,t}^{s} - MC_{t}\left(H_{f,t} + \psi z_{t}\right)\right]df + \int_{0}^{1}\left[S_{t}P_{X,f^{X},t}X_{f^{X},t} - MC_{t}^{X}\left(X_{f^{X},t} + \psi^{X}z_{t}\right)\right]df^{X} \\
={}& P_{H,t}H_{t}^{s} - MC_{t}\left(\check{s}_{H,t}H_{t} + \psi z_{t}\right) + S_{t}P_{X,t}X_{t} - P_{DX,t}\left(\check{s}_{X,t}X_{t} + \psi^{X}z_{t}\right)
\end{aligned}
\tag{88}
$$

Meaning: Total profits sum firms' revenues minus marginal cost times (output plus fixed cost); aggregated, they use price dispersion and $MC_{t}^{X}=P_{DX,t}$.

Note: the first line ends with "=" and the second begins with "=", as printed.

<!-- kind: display; id: 88.u1; section: 3.5.6; page: 32; pdf_page: 38 -->
**(88.u1) Profit share of nominal GDP**

$$
s_{D,t} \equiv \frac{D_{t}}{P_{Y,t}Y_{t}} = \frac{P_{Y,t}Y_{t} - MC_{t}\left(\check{s}_{H,t}H_{t} + \psi z_{t}\right)}{P_{Y,t}Y_{t}} = 1 - \frac{MC_{t}}{P_{Y,t}}\frac{\left(\check{s}_{H,t}H_{t} + \psi z_{t}\right)}{Y_{t}}
$$

Meaning: Using (84), the profit share equals one minus real marginal cost ($MC_{t}/P_{Y,t}$) times dispersion-weighted domestic output plus fixed cost, per unit of real output.

## 3.6 The foreign economy

**Summary.** Five foreign variables affect the domestic economy: the foreign interest rate $R_{t}^{*}$, the price of foreign intermediate goods $P_{Y,t}^{*}$, the oil price $P_{OIL,t}^{*}$, competing exporters' prices $P_{X,t}^{c,*}$ and world trade $WT_{t}^{*}$. Because SVAR and univariate AR specifications gave poor impulse responses, the foreign economy is a small log-linear closed-economy New Keynesian model, exogenous to Israel: a hybrid IS curve using the foreign forward rate (a near random walk) as the natural-rate proxy, a world-trade equation linked to foreign output, a hybrid Phillips curve with oil-price terms, an AR(2) relative oil price and an extended Taylor rule. In this block a hat on a lower-case letter marks a log deviation from the deterministic steady state, and the ε terms are shocks; competitors' relative export prices are held fixed at one.

<!-- kind: inline; id: 88.i1; section: 3.6; page: 32; pdf_page: 38 -->
**(88.i1) Foreign variables affecting the domestic economy**

$$
R_{t}^{*}, P_{Y,t}^{*}, P_{OIL,t}^{*}, P_{X,t}^{c,*} \text{ and } WT_{t}^{*}
$$

Meaning: The foreign interest rate, foreign intermediate-goods prices, oil prices, competing exporters' prices and world trade transmit global conditions.

<!-- kind: eq; id: 89; section: 3.6; page: 33; pdf_page: 39 -->
**(89) Foreign output: hybrid IS curve**

$$
\hat{y}_{t}^{*} = c_{y^{*},+}E_{t}\left[\hat{y}_{t+1}^{*}\right] + \left(1-c_{y^{*},+}\right)_{t}\hat{y}_{t-1}^{*} - c_{y^{*},r}\cdot 4\cdot\left(\hat{r}_{t}^{*} - E_{t}\left[\hat{\pi}_{Y,t+1}^{*}\right] - \widehat{rr}_{t}^{*,fwd}\right) + \varepsilon_{t}^{Y^{*}}
\tag{89}
$$

Meaning: Foreign output depends on its expected and lagged values and falls when the annualized real rate exceeds the forward-rate proxy for the natural rate; plus a demand shock.

Note: a stray subscript $t$ is printed after $\left(1-c_{y^{*},+}\right)$; transcribed as printed (probable typo) — see notes.

<!-- kind: eq; id: 90; section: 3.6; page: 33; pdf_page: 39 -->
**(90) Foreign forward ("natural") interest rate: near random walk**

$$
\widehat{rr}_{t}^{*,fwd} = 0.99\cdot\widehat{rr}_{t-1}^{*,fwd} + \varepsilon_{t}^{*,fwd}
\tag{90}
$$

Meaning: The foreign forward rate follows an AR(1) with persistence fixed at 0.99; it is identified from the observed forward nominal rate.

<!-- kind: eq; id: 91; section: 3.6; page: 33; pdf_page: 39 -->
**(91) World trade process**

$$
\widehat{wt}_{t}^{*} = c_{wt,y}\hat{y}_{t}^{*} + c_{wt,y\_lag}\hat{y}_{t-1}^{*} + c_{wt,-}\widehat{wt}_{t-1}^{*} + \varepsilon_{t}^{WT^{*}}
\tag{91}
$$

Meaning: World trade, which drives Israeli export demand (55), depends on current and lagged foreign output and its own lag, plus a shock.

<!-- kind: eq; id: 92; section: 3.6; page: 33; pdf_page: 39 -->
**(92) World inflation: hybrid New Keynesian Phillips curve**

$$
\begin{aligned}
4\cdot\hat{\pi}_{Y,t}^{*} ={}& c_{\pi^{*},+}\cdot 4\cdot E_{t}\left[\hat{\pi}_{Y,t+1}^{*}\right] + \left(1-c_{\pi^{*},+}\right)\cdot 4\cdot\hat{\pi}_{Y,t-1}^{*} \\
&+ c_{\pi^{*},y}\frac{\hat{y}_{t}^{*}+\hat{y}_{t-1}^{*}}{2} + c_{\pi^{*},OIL}\hat{p}_{OIL,t}^{*} + c_{\pi^{*},\Delta OIL}\left(\hat{p}_{OIL,t}^{*} - \hat{p}_{OIL,t-2}^{*}\right) + \varepsilon_{t}^{\Pi^{*}}
\end{aligned}
\tag{92}
$$

Meaning: Annualized world inflation mixes expected and lagged inflation and responds to average foreign output, the relative oil price and its two-quarter change, plus a shock.

<!-- kind: inline; id: 92.i1; section: 3.6; page: 33; pdf_page: 39 -->
**(92.i1) Relative price of oil**

$$
p_{OIL,t}^{*} \equiv P_{OIL,t}^{*}/P_{Y,t}^{*}
$$

Meaning: The global oil price relative to the global price of foreign intermediate goods.

<!-- kind: eq; id: 93; section: 3.6; page: 33; pdf_page: 39 -->
**(93) Relative oil price: AR(2) process**

$$
\hat{p}_{OIL,t}^{*} = c_{oil,-}\hat{p}_{OIL,t-1}^{*} + c_{oil,\Delta}\left(\hat{p}_{OIL,t-1}^{*} - \hat{p}_{OIL,t-2}^{*}\right) + \varepsilon_{t}^{OIL}
\tag{93}
$$

Meaning: The relative oil price depends on its lag and its lagged change (an AR(2) in levels), plus an oil shock.

<!-- kind: eq; id: 94; section: 3.6; page: 33; pdf_page: 39 -->
**(94) Foreign interest-rate rule (extended Taylor rule)**

$$
\begin{aligned}
4\cdot\hat{r}_{t}^{*} ={}& \left(1-c_{r^{*},-}\right)[4\cdot\left(\widehat{rr}_{t}^{*,fwd} + \hat{\bar{\pi}}_{t}^{*}\right) \\
&+ c_{r^{*},\pi}4\cdot\left(\frac{\hat{\pi}_{Y,t-1}^{*} + \hat{\pi}_{Y,t}^{*} + \hat{\pi}_{Y,t+1}^{*} + \hat{\pi}_{Y,t+2}^{*} + \hat{\pi}_{Y,t+3}^{*}}{5} - \hat{\bar{\pi}}_{t}^{*}\right) \\
&+ c_{r^{*},y}\hat{y}_{t}^{*}] + c_{r^{*},-}\cdot 4\cdot\hat{r}_{t-1}^{*} + \varepsilon_{t}^{R^{*}}
\end{aligned}
\tag{94}
$$

Meaning: The annualized foreign rate smooths toward a target of the forward rate plus inflation target, a five-quarter average inflation gap and foreign output, plus a policy shock.

Note: the square bracket opens on the first line and closes on the third, as printed; plain [ ] are used so the bracket can span the line breaks. The foreign target $\hat{\bar{\pi}}_{t}^{*}$ is printed with a wide hat over a full-width bar (encoded as in (62)).

<!-- kind: inline; id: 94.i1; section: 3.6; page: 34; pdf_page: 40 -->
**(94.i1) Competitors' relative export price fixed**

$$
p_{X,t}^{c,*} \equiv P_{X,t}^{c,*}/P_{Y,t}^{*} = 1
$$

Meaning: Variations in competing exporters' prices relative to foreign intermediate-goods prices are ruled out; the ratio is fixed at one.

Note: this sentence ends Section 3 on PDF p.40 (printed 34), above the heading "4 Estimation of the model".
