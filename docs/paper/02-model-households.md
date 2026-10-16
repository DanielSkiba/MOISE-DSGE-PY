# The model (Section 3): overview and households

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

Section 3 opening and 3.1 Households: preferences, budget constraint, consumption and saving, investment and capital utilization, labor supply and wage setting. Equations (1)–(16).

## 3 The model

**Summary.** MOISE is built along the lines of two existing central-bank models, the ECB's NAWM and the Riksbank's RAMSES (a footnote lists comparable models for Norway, Canada, New Zealand and Iceland). Its agents are households, several kinds of firms, a government, and a central bank that pursues an inflation target by setting the nominal interest rate. Production involves monopolistically competitive intermediate-goods makers that hire labor and capital, competitive final-goods makers, importers and exporters. What follows lays out the model's behavioral relationships and the first-order and market-clearing conditions they imply, with extended discussion reserved for the non-standard elements.

### 3.1 Households

**Summary.** A unit continuum of households consumes (with external habits), works, saves in domestic- and foreign-currency bonds, and owns the capital stock, choosing investment and the rate of capital utilization. Households supply differentiated labor and set wages with Calvo-type stickiness and indexation; state-contingent securities make all households choose the same allocations in equilibrium.

#### 3.1.1 Preferences and the budget constraint

**Summary.** Lifetime utility rises with consumption measured against last period's aggregate consumption (external habit) and falls with hours worked; a consumption-demand shock and a labor-supply shock enter preferences. The nominal budget constraint covers VAT-inclusive consumption, investment, an exogenous change in inventories, purchases of domestic and foreign bonds (whose prices include risk-premium shocks and an endogenous external premium), transfers and insurance securities, and income from labor, capital and dividends taxed at separate rates. The inventory share of GDP follows an AR(1), the domestic premium shock is close to a unit root, and the external premium depends on the net-foreign-asset ratio and on depreciation adjusted for the inflation-target differential.

<!-- kind: inline; id: 0.i1; section: 3.1.1; page: 6; pdf_page: 12 -->
**(0.i1) Household index**

$$
h \in [0,1]
$$

Meaning: Households form a continuum indexed on the unit interval.

<!-- kind: eq; id: 1; section: 3.1.1; page: 6; pdf_page: 12 -->
**(1) Lifetime utility of household h**

$$
E_{t}\sum_{k=0}^{\infty}\left[\beta^{k}\left(\varepsilon_{t+k}^{C}\ln\left(C_{h,t+k}-\kappa C_{t+k-1}\right)-\frac{\varepsilon_{t+k}^{N}}{1+\zeta}\left(N_{h,t+k}\right)^{1+\zeta}\right)\right]
\tag{1}
$$

Meaning: Expected discounted sum of log utility from consumption net of external habit (scaled by a demand shock) minus the disutility of hours (scaled by a labor-supply shock).

<!-- kind: inline; id: 1.i1; section: 3.1.1; page: 6; pdf_page: 12 -->
**(1.i1) Example of the log-AR(1) shock process (footnote 4)**

$$
\log\left(\varepsilon_{t}^{C}\right) = \rho^{C}\log\left(\varepsilon_{t-1}^{C}\right)+\eta_{t}^{C}
$$

Meaning: Shocks are generally assumed log-AR(1); for the consumption shock, its log follows an AR(1) with white-noise innovation $\eta_{t}^{C}$.

<!-- kind: eq; id: 2; section: 3.1.1; page: 6; pdf_page: 12 -->
**(2) Period-by-period budget constraint of household h**

$$
\begin{aligned}
&\left(1+w_{\tau^{C}}\tau_{t}^{C}\right)P_{C,t}C_{h,t}+P_{I,t}I_{h,t}+P_{I,t}\Delta INV_{t} \\
&+\left(\varepsilon_{t}^{RP}\varepsilon_{t}^{DRP}R_{t}\right)^{-1}B_{h,t+1}+\left(\varepsilon_{t}^{RP}\Gamma_{B^{*},t}R_{t}^{*}\right)^{-1}S_{t}B_{h,t+1}^{*}+\Xi_{t}+\Upsilon_{h,t} \\
={}&\left(1-\tau_{t}^{N}-\tau_{t}^{W_{h}}\right)W_{h,t}N_{h,t}+\left(1-\tau_{t}^{K}\right)\left[R_{K,t}u_{h,t}-\Gamma_{u}\left(u_{h,t}\right)P_{I,t}\right]K_{h,t} \\
&+\tau_{t}^{K}\delta P_{I,t}K_{h,t}+\left(1-\tau_{t}^{D}\right)D_{h,t}-T_{t}+B_{h,t}+S_{t}B_{h,t}^{*}
\end{aligned}
\tag{2}
$$

Meaning: Outlays on taxed consumption, investment, inventories, new bonds, transfers and insurance securities equal after-tax labor, capital and dividend income plus a depreciation allowance, less lump-sum tax, plus maturing bonds.

Note: $B_{h,t}$ and $B^{*}_{h,t}$ are bond holdings at the beginning of period $t$ (p.7).

<!-- kind: inline; id: 2.i1; section: 3.1.1; page: 6; pdf_page: 12 -->
**(2.i1) Nominal consumption expenditure (first term of (2))**

$$
\left(1+w_{\tau^{C}}\tau_{t}^{C}\right)P_{C,t}C_{h,t}
$$

Meaning: Consumption spending including VAT, where $\tau_{t}^{C}$ is the VAT rate, $w_{\tau^{C}}$ the share of goods subject to VAT, and $P_{C,t}$ the pre-tax consumption price.

<!-- kind: inline; id: 2.i2; section: 3.1.1; page: 7; pdf_page: 13 -->
**(2.i2) Change in inventories as a share of GDP**

$$
\Delta inv_{t} = \frac{\Delta INV_{t}}{Y_{t}}
$$

Meaning: The exogenous change in inventories (common to all households) expressed as a ratio to GDP.

<!-- kind: eq; id: 3; section: 3.1.1; page: 7; pdf_page: 13 -->
**(3) AR(1) process for the change in inventories (share of GDP)**

$$
\Delta inv_{t} = \rho_{\Delta INV}\Delta inv_{t-1}+\left(1-\rho_{\Delta INV}\right)\Delta inv+\eta_{t}^{\Delta INV}
\tag{3}
$$

Meaning: The inventory-change share of GDP moves persistently around its steady-state value $\Delta inv$, driven by an innovation.

<!-- kind: inline; id: 3.i1; section: 3.1.1; page: 7; pdf_page: 13 -->
**(3.i1) Market price of the local-currency bond**

$$
\left(\varepsilon_{t}^{RP}\varepsilon_{t}^{DRP}R_{t}\right)^{-1}
$$

Meaning: The domestic bond price is the inverse of the product of the central bank's gross nominal rate $R_{t}$ and the symmetric and domestic premium shocks.

<!-- kind: display; id: 3.u1; section: 3.1.1; page: 8; pdf_page: 14 -->
**(3.u1) Near-unit-root process of the domestic risk-premium shock**

$$
\varepsilon_{t}^{DRP} = 0.99\varepsilon_{t-1}^{DRP}+\left(1-0.99\right)+\eta_{t}^{DRP}
$$

Meaning: The domestic premium shock is highly persistent (coefficient 0.99) around a mean of one, driven by an innovation.

<!-- kind: eq; id: 4; section: 3.1.1; page: 8; pdf_page: 14 -->
**(4) External financial intermediation premium on foreign-currency bonds**

$$
\Gamma_{B^{*}} = \varepsilon_{t}^{RP^{*}}\exp\left[-\gamma_{B^{*}}s_{B^{*},t+1}-\gamma_{S}E_{t}\left(\frac{S_{t+1}}{S_{t}}\frac{\bar{\Pi}_{t+1}^{*}}{\bar{\Pi}_{t+1}}\frac{S_{t}}{S_{t-1}}\frac{\bar{\Pi}_{t}^{*}}{\bar{\Pi}_{t}}-1\right)\right]
\tag{4}
$$

Meaning: The premium is an exogenous shock times the exponential of negative terms in the net-foreign-asset-to-GDP ratio and in expected depreciation (t-1 to t+1) adjusted for inflation-target differentials.

Note: the paper states (p.8) that making the premium depend on the net-foreign-asset ratio ensures a stable non-stochastic steady state with a zero net foreign asset position ($s_{B^{*}} = 0$ in steady state).

Note: The left-hand side is printed $\Gamma_{B^{*}}$ without a time subscript, whereas (2) and (7) write $\Gamma_{B^{*},t}$; transcribed as printed (see [transcription notes](transcription-notes/T01.md)).

<!-- kind: inline; id: 4.i1; section: 3.1.1; page: 8; pdf_page: 14 -->
**(4.i1) Net foreign assets to nominal GDP ratio**

$$
s_{B^{*},t+1} \equiv \left(S_{t}B_{t+1}^{*}\right)/\left(P_{Y,t}Y_{t}\right)
$$

Meaning: Total net foreign assets valued in domestic currency, divided by nominal GDP.

<!-- kind: inline; id: 4.i2; section: 3.1.1; page: 8; pdf_page: 14 -->
**(4.i2) Inflation-target differential**

$$
\bar{\Pi}_{t}^{*}/\bar{\Pi}_{t}
$$

Meaning: Ratio of the foreign to the domestic inflation target, used to adjust depreciation in the premium (4).

#### 3.1.2 The consumption and saving decision

**Summary.** Attaching a multiplier to the budget constraint, the household's first-order conditions deliver the marginal utility of consumption, net of habit and divided by the VAT wedge. Two Euler equations follow: one for domestic-currency bonds, which carries both premium shocks, and one for foreign-currency bonds, which carries the symmetric premium shock, the external premium and expected exchange-rate changes.

<!-- kind: inline; id: 4.i3; section: 3.1.2; page: 9; pdf_page: 15 -->
**(4.i3) Lagrange multiplier on the budget constraint (2)**

$$
\beta^{k}\cdot\Lambda_{h,t+k}/P_{C,t+k} \quad (\text{for } k\geq 0)
$$

Meaning: Defines $\Lambda_{h,t}$ through the discounted multiplier on the nominal budget constraint, measured relative to the consumption price.

<!-- kind: eq; id: 5; section: 3.1.2; page: 9; pdf_page: 15 -->
**(5) Marginal utility of consumption (Lagrange multiplier)**

$$
\Lambda_{h,t} = \varepsilon_{t}^{C}\frac{\left(C_{h,t}-\kappa C_{t-1}\right)^{-1}}{1+w_{\tau^{C}}\tau_{t}^{C}}
\tag{5}
$$

Meaning: The multiplier equals demand-shocked marginal utility of habit-adjusted consumption, divided by the VAT wedge on consumption.

<!-- kind: eq; id: 6; section: 3.1.2; page: 9; pdf_page: 15 -->
**(6) Euler equation for domestic-currency bonds**

$$
\beta\varepsilon_{t}^{DRP}\varepsilon_{t}^{RP}R_{t}E_{t}\left[\frac{\Lambda_{h,t+1}}{\Lambda_{h,t}}\frac{P_{C,t}}{P_{C,t+1}}\right] = 1
\tag{6}
$$

Meaning: The premium-adjusted domestic nominal rate times the expected nominal stochastic discount factor (marginal-utility ratio divided by gross CPI inflation) equals one.

<!-- kind: eq; id: 7; section: 3.1.2; page: 9; pdf_page: 15 -->
**(7) Euler equation for foreign-currency bonds**

$$
\beta\varepsilon_{t}^{RP}\Gamma_{B^{*},t}R_{t}^{*}E_{t}\left[\frac{\Lambda_{h,t+1}}{\Lambda_{h,t}}\frac{P_{C,t}}{P_{C,t+1}}\frac{S_{t+1}}{S_{t}}\right] = 1
\tag{7}
$$

Meaning: The premium-adjusted foreign nominal rate times the expectation of the nominal discount factor multiplied by the depreciation rate $S_{t+1}/S_{t}$ equals one.

#### 3.1.3 Investment and capital utilization

**Summary.** Varying the utilization rate costs a convex function of its deviation from one. Capital accumulates from undepreciated capital plus investment, scaled by an investment-specific technology shock and reduced by an adjustment cost. That cost depends on an investment-growth index built from two lags of investment, compared with long-run productivity growth. With Tobin's Q as the shadow price of installed capital, the first-order conditions for investment, next-period capital and utilization are derived.

<!-- kind: eq; id: 8; section: 3.1.3; page: 9; pdf_page: 15 -->
**(8) Cost of capital utilization**

$$
\Gamma_{u}\left(u_{h,t}\right) = \gamma_{u,1}\left(u_{h,t}-1\right)+\frac{\gamma_{u,2}}{2}\left(u_{h,t}-1\right)^{2}
\tag{8}
$$

Meaning: Utilization costs are linear plus quadratic in the deviation of the utilization rate from one.

<!-- kind: inline; id: 8.i1; section: 3.1.3; page: 9; pdf_page: 15 -->
**(8.i1) Parameter restriction on utilization-cost coefficients**

$$
\gamma_{u,1},\gamma_{u,2} > 0
$$

Meaning: Both coefficients of the utilization cost function are strictly positive.

<!-- kind: eq; id: 9; section: 3.1.3; page: 10; pdf_page: 16 -->
**(9) Law of motion of physical capital**

$$
K_{h,t+1} = \left(1-\delta\right)K_{h,t}+\varepsilon_{t}^{I}\left[1-\Gamma_{I}\left(\tilde{I}_{h,t}\right)\right]I_{h,t}
\tag{9}
$$

Meaning: Next period's capital is undepreciated capital plus investment net of adjustment costs, scaled by the investment-specific technology shock.

<!-- kind: eq; id: 10; section: 3.1.3; page: 10; pdf_page: 16 -->
**(10) Investment adjustment cost function**

$$
\Gamma_{I}\left(\tilde{I}_{h,t}\right) = \frac{\gamma_{I}}{2}\left(\tilde{I}_{h,t}-g_{z}^{\left(1+\omega_{\Gamma_{I}}\right)}\right)^{2}
\tag{10}
$$

Meaning: Adjustment costs are quadratic in the gap between the investment-growth index and long-run productivity growth raised to the power one plus the lag weight.

<!-- kind: display; id: 10.u1; section: 3.1.3; page: 10; pdf_page: 16 -->
**(10.u1) Investment-growth index with two lags**

$$
\tilde{I}_{h,t} \equiv \frac{I_{h,t}}{I_{h,t-1}}\left(\frac{I_{h,t-1}}{I_{h,t-2}}\right)^{\omega_{\Gamma_{I}}}
$$

Meaning: Current investment growth multiplied by lagged investment growth raised to the weight $\omega_{\Gamma_{I}}$.

<!-- kind: inline; id: 10.i1; section: 3.1.3; page: 10; pdf_page: 16 -->
**(10.i1) Standard specification as a special case (footnote 9)**

$$
\omega_{\Gamma_{I}} = 0
$$

Meaning: Setting the lag weight to zero recovers the usual one-lag adjustment cost.

<!-- kind: inline; id: 10.i2; section: 3.1.3; page: 10; pdf_page: 16 -->
**(10.i2) Lagrange multiplier on capital accumulation (9)**

$$
\beta^{k}\Lambda_{h,t+k}Q_{h,t+k} \quad (\text{for } k\geq 0)
$$

Meaning: Defines Tobin's Q, $Q_{h,t}$, the price of installed capital in consumption units, through the multiplier on (9).

<!-- kind: eq; id: 11; section: 3.1.3; page: 10; pdf_page: 16 -->
**(11) First-order condition for investment**

$$
\begin{aligned}
\frac{P_{I,t}}{P_{C,t}} ={}& Q_{h,t}\varepsilon_{t}^{I}\left[1-\Gamma_{I}\left(\tilde{I}_{h,t}\right)-\Gamma'_{I}\left(\tilde{I}_{h,t}\right)\tilde{I}_{h,t}\right] \\
&+\left(1-\omega_{\Gamma_{I}}\right)\beta E_{t}\left[\frac{\Lambda_{h,t+1}}{\Lambda_{h,t}}Q_{h,t+1}\varepsilon_{t+1}^{I}\Gamma'_{I}\left(\tilde{I}_{h,t+1}\right)\tilde{I}_{h,t+1}\frac{I_{h,t+1}}{I_{h,t}}\right] \\
&+\omega_{\Gamma_{I}}\beta^{2}E_{t}\left[\frac{\Lambda_{h,t+2}}{\Lambda_{h,t+1}}\frac{\Lambda_{h,t+1}}{\Lambda_{h,t}}Q_{h,t+2}\varepsilon_{t+2}^{I}\Gamma'_{I}\left(\tilde{I}_{h,t+2}\right)\tilde{I}_{h,t+2}\frac{I_{h,t+2}}{I_{h,t}}\right]
\end{aligned}
\tag{11}
$$

Meaning: The relative price of investment equals the marginal value of new capital net of current adjustment costs, plus discounted adjustment-cost effects one and two periods ahead.

<!-- kind: eq; id: 12; section: 3.1.3; page: 10; pdf_page: 16 -->
**(12) First-order condition for capital (Tobin's Q)**

$$
Q_{h,t} = \beta E_{t}\left[\frac{\Lambda_{h,t+1}}{\Lambda_{h,t}}\left(\begin{aligned}&\left(1-\tau_{t+1}^{K}\right)\left[\frac{R_{K,t+1}}{P_{C,t+1}}u_{h,t+1}-\Gamma_{u}\left(u_{h,t+1}\right)\frac{P_{I,t+1}}{P_{C,t+1}}\right] \\ &+\tau_{t+1}^{K}\delta\frac{P_{I,t+1}}{P_{C,t+1}}+\left(1-\delta\right)Q_{h,t+1}\end{aligned}\right)\right]
\tag{12}
$$

Meaning: Today's Q is the discounted expected after-tax real net return on capital services, plus the depreciation tax allowance, plus the undepreciated value of capital next period.

Note: The paper breaks the content of the large parenthesis into two centred rows (with small inline fractions); the nested `aligned` keeps that line break. The two rows are one sum.

<!-- kind: eq; id: 13; section: 3.1.3; page: 11; pdf_page: 17 -->
**(13) First-order condition for capital utilization**

$$
R_{K,t} = \Gamma'_{u}\left(u_{h,t}\right)P_{I,t}
\tag{13}
$$

Meaning: The rental price of capital services equals the marginal utilization cost valued at the investment price.

#### 3.1.4 Labor supply and wage setting

**Summary.** Each household is a monopolistic supplier of its own labor type, and wages are reset under Calvo frictions. Households that cannot reoptimize index their wage to a geometric mix of lagged and long-run productivity growth and to a geometric mix of lagged CPI inflation and the inflation target. Reoptimizing households all set the same wage, determined by a forward-looking first-order condition, and the aggregate wage index combines indexed and newly set wages.

<!-- kind: inline; id: 13.i1; section: 3.1.4; page: 11; pdf_page: 17 -->
**(13.i1) Calvo probability of wage reoptimization**

$$
\left(1-\xi_{W}\right) \in (0,1)
$$

Meaning: Each period a household gets the signal to reset its wage with probability $1-\xi_{W}$; with probability $\xi_{W}$ it indexes instead.

<!-- kind: eq; id: 14; section: 3.1.4; page: 11; pdf_page: 17 -->
**(14) Wage indexation scheme for non-reoptimizing households**

$$
W_{h,t} = \left(g_{z,t-1}\right)^{\chi_{W,g_{z}}}\left(g_{z}\right)^{\left(1-\chi_{W,g_{z}}\right)}\Pi_{C,t}^{\dagger}W_{h,t-1}
\tag{14}
$$

Meaning: A non-reoptimized wage grows with a weighted geometric average of lagged and long-run productivity growth, times the indexation inflation factor.

<!-- kind: inline; id: 14.i1; section: 3.1.4; page: 11; pdf_page: 17 -->
**(14.i1) Inflation indexation factor for wages**

$$
\Pi_{C,t}^{\dagger} \equiv \left(\Pi_{C,t-1}\right)^{\chi_{W}}\left(\bar{\Pi}_{t}\right)^{\left(1-\chi_{W}\right)}
$$

Meaning: A geometric mix of last period's CPI inflation and the current inflation target, weighted by $\chi_{W}$.

<!-- kind: inline; id: 14.i2; section: 3.1.4; page: 11; pdf_page: 17 -->
**(14.i2) Gross CPI inflation**

$$
\Pi_{C,t} \equiv P_{C,t}/P_{C,t-1}
$$

Meaning: Gross inflation of the consumption price index; $\bar{\Pi}_{t}$ denotes the gross inflation target.

<!-- kind: eq; id: 15; section: 3.1.4; page: 11; pdf_page: 17 -->
**(15) First-order condition for the optimal reset wage**

$$
\begin{aligned}
E_{t}\sum_{k=0}^{\infty}\Bigg\{\left(\xi_{W}\beta\right)^{k}\Bigg[&\Lambda_{t+k}\left(1-\tau_{t+k}^{N}-\tau_{t+k}^{W_{h}}\right)\left(g_{z;t-1,t+k-1}\right)^{\chi_{W,g_{z}}}\left[\left(g_{z}\right)^{1-\chi_{W,g_{z}}}\right]^{k}\frac{\Pi_{C;t,t+k}^{\dagger}}{\Pi_{C;t,t+k}}\frac{\tilde{W}_{t}}{P_{C,t}} \\
&-\varphi_{t+k}^{W}\varepsilon_{t+k}^{N}\left(N_{h,t+k}\right)^{\zeta}\Bigg]N_{h,t+k}\Bigg\} = 0
\end{aligned}
\tag{15}
$$

Meaning: The expected discounted, hours-weighted gap between the utility value of the after-tax indexed real wage and the markup-scaled marginal disutility of work, summed over the wage's lifetime, is zero.

Note: The multiplier is printed $\Lambda_{t+k}$, without the household subscript $h$ used in (5)-(7) and (11)-(12); transcribed as printed (see [transcription notes](transcription-notes/T01.md)).

<!-- kind: inline; id: 15.i1; section: 3.1.4; page: 12; pdf_page: 18 -->
**(15.i1) Accumulated productivity growth for indexation (for every k ≥ 1)**

$$
g_{z;t,t+k} \equiv \prod_{s=1}^{k}g_{z,t+s} \quad \text{for every } k\geq 1
$$

Meaning: Cumulative gross labor-productivity growth over periods $t+1$ to $t+k$, used in wage indexation; defined for $k\geq 1$.

<!-- kind: inline; id: 15.i2; section: 3.1.4; page: 12; pdf_page: 18 -->
**(15.i2) Accumulated indexation inflation (for every k ≥ 1)**

$$
\Pi_{C;t,t+k}^{\dagger} \equiv \prod_{s=1}^{k}\Pi_{C,t+s-1}^{\chi_{W}}\bar{\Pi}_{t+s}^{1-\chi_{W}} \quad \text{for every } k\geq 1
$$

Meaning: Cumulative product over $k$ periods of the indexation inflation factors (lagged CPI inflation and target, weighted by $\chi_{W}$); defined for $k\geq 1$.

<!-- kind: inline; id: 15.i3; section: 3.1.4; page: 12; pdf_page: 18 -->
**(15.i3) Accumulated CPI inflation (for every k ≥ 1)**

$$
\Pi_{C;t,t+k} \equiv \prod_{s=1}^{k}\Pi_{C,t+s} \quad \text{for every } k\geq 1
$$

Meaning: Cumulative gross CPI inflation between $t$ and $t+k$; defined for $k\geq 1$.

<!-- kind: inline; id: 15.i4; section: 3.1.4; page: 12; pdf_page: 18 -->
**(15.i4) Accumulated terms for k = 0**

$$
g_{z;t,t} = \Pi_{C;t,t}^{\dagger} = \Pi_{C;t,t} \equiv 1
$$

Meaning: For $k=0$ the accumulated growth and inflation terms are all set to one.

<!-- kind: eq; id: 16; section: 3.1.4; page: 12; pdf_page: 18 -->
**(16) Dynamics of the aggregate wage composite**

$$
W_{t} = \left(\xi_{W}\left[\left(g_{z,t-1}\right)^{\chi_{W,g_{z}}}\left(g_{z}\right)^{1-\chi_{W,g_{z}}}\Pi_{C,t}^{\dagger}W_{h,t-1}\right]^{\frac{1}{1-\varphi_{t}^{W}}}+\left(1-\xi_{W}\right)\left(\tilde{W}_{t}\right)^{\frac{1}{1-\varphi_{t}^{W}}}\right)^{1-\varphi_{t}^{W}}
\tag{16}
$$

Meaning: The aggregate wage is a CES-type average of indexed previous wages (weight $\xi_{W}$) and the newly reset wage (weight $1-\xi_{W}$), with the wage markup governing the exponents.

Note: Inside the bracket the paper prints $W_{h,t-1}$ (household wage) rather than the aggregate $W_{t-1}$; transcribed as printed (suspected typo, see notes).
