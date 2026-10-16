# The steady state (Appendix C)

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

C.1 the non-linear steady-state model and C.2 the recursive steady-state solution. Equations (110)–(211).

## Appendix C The steady state

**Summary.** This appendix derives the deterministic steady state: C.1 restates the optimality and market-clearing conditions at the steady state (48 non-linear equations in 48 unknowns), and C.2 solves them recursively in terms of the parameters. Because productivity has a unit root and prices are non-stationary, variables with a real trend are divided by productivity $z_{t}$ and those with a nominal trend by the CPI $P_{C,t}$; lower-case letters denote the resulting stationary variables. Along the balanced growth path every real variable, world output included, grows at $g_{z}$, and every steady-state inflation rate is in line with the inflation target. Three features of the steady state are imposed: capital is fully utilized, net foreign assets are zero, and indexation makes the outcome equivalent to fully flexible prices and wages (all Calvo parameters set to zero).

<!-- kind: inline; id: 109.i2; section: C; page: 95; pdf_page: 101 -->
**(109.i2) Normalizer of real trending variables: productivity level**

$$
z_{t}
$$

Meaning: The productivity level, which divides variables with a real stochastic trend to make them stationary.

<!-- kind: inline; id: 109.i3; section: C; page: 95; pdf_page: 101 -->
**(109.i3) Normalizer of nominal trending variables: the CPI**

$$
P_{C,t}
$$

Meaning: The consumer price index, which divides variables with a nominal trend to make them stationary.

<!-- kind: inline; id: 109.i4; section: C; page: 95; pdf_page: 101 -->
**(109.i4) Example of a stationarized real variable**

$$
c_{t} \equiv C_{t}/z_{t}
$$

Meaning: Example of the lower-case convention: stationary consumption is aggregate consumption divided by productivity.

<!-- kind: inline; id: 109.i5; section: C; page: 95; pdf_page: 101 -->
**(109.i5) Example of a stationarized price**

$$
p_{H,t} \equiv P_{H,t}/P_{C,t}
$$

Meaning: Example of the lower-case convention: the price of domestic intermediate goods measured relative to the CPI.

<!-- kind: inline; id: 109.i6; section: C; page: 95; pdf_page: 101 -->
**(109.i6) Common steady-state growth rate**

$$
g_{z}
$$

Meaning: On the balanced growth path all real variables, including world output, grow at this one gross rate.

<!-- kind: inline; id: 109.i7; section: C; page: 95; pdf_page: 101 -->
**(109.i7) Inflation target**

$$
\bar{\pi}
$$

Meaning: The inflation target. All steady-state inflation rates are consistent with it.

<!-- kind: inline; id: 109.i8; section: C; page: 95; pdf_page: 101 -->
**(109.i8) Assumption 1: full capital utilization in steady state**

$$
u = 1
$$

Meaning: Assumed: capital is used at full capacity ($u = 1$) in the deterministic steady state; the cost of varying utilization is what delivers this.

<!-- kind: inline; id: 109.i9; section: C; page: 96; pdf_page: 102 -->
**(109.i9) Assumption 2: zero steady-state net foreign assets**

$$
B^{*} = 0
$$

Meaning: The external risk premium, which depends on net foreign assets, pushes them to zero in steady state, so the current account is balanced.

<!-- kind: inline; id: 109.i10; section: C; page: 96; pdf_page: 102 -->
**(109.i10) Assumption 3: Calvo parameters set to zero**

$$
\xi's
$$

Meaning: Indexation updates all prices (and wages) by the target in steady state, so the solution matches flexible prices and all Calvo parameters ξ are set to zero.

## C.1 The non-linear steady-state model

**Summary.** The non-linear equilibrium conditions are evaluated at the deterministic steady state. Shocks are switched off (for most of them this means setting them to one), time subscripts are removed, and, since all households and all firms behave identically there, their indices are removed as well. The resulting conditions are listed by sector in C.1.1–C.1.9.

### C.1.1 Households

**Summary.** Steady-state household conditions: the consumption first-order condition gives the normalized marginal utility of income, and the two bond conditions tie the domestic and foreign nominal rates to growth, discounting and inflation (foreign inflation is assumed equal to domestic inflation). The capital accumulation law and the investment, capital and utilization conditions, with $u=1$ substituted, determine investment, Tobin's Q and the rental rate of capital. Full utilization is consistent with these conditions only under a restriction on the utilization-cost coefficient $\gamma_{u,1}$. Wage setting, once indexation is taken into account, makes the real wage a markup over the ratio of the marginal disutility of hours to the marginal utility of income, grossed up for household labor taxes.

<!-- kind: eq; id: 110; section: C.1.1; page: 96; pdf_page: 102 -->
**(110) Steady-state FOC with respect to consumption (marginal utility of income)**

$$
\lambda = \frac{\left(1 - \kappa/g_{z}\right)^{-1}}{1 + w_{\tau^{C}} \tau^{C}} \frac{1}{c}
\tag{110}
$$

Meaning: Normalized marginal utility of income equals the habit-adjusted inverse of consumption, divided by one plus the effective VAT rate.

<!-- kind: inline; id: 110.i1; section: C.1.1; page: 96; pdf_page: 102 -->
**(110.i1) Normalized marginal utility of income**

$$
\lambda_{t} = \left(\Lambda_{t} \cdot z_{t}\right)
$$

Meaning: The multiplier Λ_t times productivity z_t, a stationary version of the marginal utility of income.

<!-- kind: eq; id: 111; section: C.1.1; page: 96; pdf_page: 102 -->
**(111) Steady-state FOC with respect to domestic bonds**

$$
\frac{\beta}{g_{z} \Pi} R = 1
\tag{111}
$$

Meaning: Domestic bond Euler equation at the steady state. The discount factor times the gross nominal rate, divided by growth times inflation, equals one.

<!-- kind: eq; id: 112; section: C.1.1; page: 96; pdf_page: 102 -->
**(112) Steady-state FOC with respect to foreign-currency bonds**

$$
\frac{\beta}{g_{z} \Pi^{*}} R^{*} = 1
\tag{112}
$$

Meaning: Foreign-currency bond Euler equation at the steady state. It ties the foreign nominal rate to growth, discounting and foreign inflation.

<!-- kind: inline; id: 112.i1; section: C.1.1; page: 96; pdf_page: 102 -->
**(112.i1) Assumption: equal foreign and domestic steady-state inflation**

$$
\Pi^{*} = \Pi
$$

Meaning: Steady-state foreign inflation is assumed equal to domestic steady-state inflation.

<!-- kind: eq; id: 113; section: C.1.1; page: 97; pdf_page: 103 -->
**(113) Steady-state capital accumulation (physical capital production function)**

$$
i = \left(1 - \frac{1-\delta}{g_{z}}\right) k
\tag{113}
$$

Meaning: Normalized investment covers depreciation and growth of the normalized capital stock.

<!-- kind: inline; id: 113.i1; section: C.1.1; page: 97; pdf_page: 103 -->
**(113.i1) Definition of normalized capital**

$$
k_{t} \equiv K_{t+1}/z_{t}
$$

Meaning: Normalized capital is end-of-period capital K_{t+1} divided by current productivity z_t.

<!-- kind: eq; id: 114; section: C.1.1; page: 97; pdf_page: 103 -->
**(114) Steady-state FOC with respect to investment**

$$
p_{I} = Q
\tag{114}
$$

Meaning: In steady state the relative price of investment goods equals Tobin's Q.

<!-- kind: display; id: 114.u1; section: C.1.1; page: 97; pdf_page: 103 -->
**(114.u1) Steady-state FOC with respect to next-period capital (with u = 1)**

$$
Q = \frac{\left(1-\tau^{K}\right) r_{K} + \tau^{K} \delta p_{I}}{g_{z}/\beta - \left(1-\delta\right)}
$$

Meaning: With full utilization, Q equals the after-tax rental return plus the depreciation allowance, divided by the growth-adjusted real rate less undepreciated capital.

<!-- kind: eq; id: 115; section: C.1.1; page: 97; pdf_page: 103 -->
**(115) Capital FOC combined with the investment FOC (114)**

$$
\left[\frac{\beta}{g_{z}} - \left(1 - \delta + \tau^{K} \delta\right)\right] p_{I} = \left(1 - \tau^{K}\right) r_{K}
\tag{115}
$$

Meaning: Substituting p_I = Q into the capital condition gives a link between the investment price and the after-tax rental rate of capital.

Note: Printed with β/g_z as the first term in the bracket. Combining 114.u1 with (114) gives g_z/β in that position, so this is a suspected typo (see [transcription notes](transcription-notes/T09.md)).

<!-- kind: display; id: 115.u1; section: C.1.1; page: 97; pdf_page: 103 -->
**(115.u1) Steady-state FOC with respect to utilization (with u = 1)**

$$
r_{K} = \gamma_{u,1} p_{I}
$$

Meaning: At full utilization the real rental rate equals the slope of the utilization cost times the relative investment price.

<!-- kind: display; id: 115.u2; section: C.1.1; page: 97; pdf_page: 103 -->
**(115.u2) Parameter restriction on the utilization-cost coefficient**

$$
\gamma_{u,1} = \left[\frac{\beta}{g_{z}} - \left(1 - \delta + \tau^{K} \delta\right)\right] \left(1 - \tau^{K}\right)^{-1}
$$

Meaning: The value the linear utilization-cost coefficient must take for 115.u1 and (115) to hold together at full utilization.

Note: Printed with β/g_z, like (115). Derived from 114.u1 it would read g_z/β, so this is a suspected typo (see [transcription notes](transcription-notes/T09.md)).

<!-- kind: eq; id: 116; section: C.1.1; page: 97; pdf_page: 103 -->
**(116) Full capital utilization**

$$
u = 1
\tag{116}
$$

Meaning: Capital utilization equals one in steady state. The paper says this fails unless the restriction 115.u2 holds.

<!-- kind: eq; id: 117; section: C.1.1; page: 97; pdf_page: 103 -->
**(117) Steady-state optimal wage setting**

$$
w = \frac{\varphi^{W}}{\left(1 - \tau^{N} - \tau^{W_{h}}\right)} \frac{N^{\zeta}}{\lambda}
\tag{117}
$$

Meaning: The real wage equals the wage markup times the marginal disutility of hours over the marginal utility of income, grossed up for household labor taxes.

<!-- kind: inline; id: 117.i1; section: C.1.1; page: 97; pdf_page: 103 -->
**(117.i1) Definition of the normalized real wage**

$$
w_{t} = \frac{W_{t}}{P_{C,t} z_{t}}
$$

Meaning: The stationary real wage is the nominal wage divided by the CPI and by productivity.

### C.1.2 Domestic intermediate goods firms

**Summary.** These are the steady-state conditions of domestic intermediate-goods producers. They cover the production function, the interest factor on working capital, the cost-minimizing ratio of capital to hours, and real marginal cost in consumer-price terms. With flexible steady-state prices, the relative domestic price is a fixed markup over marginal cost.

<!-- kind: eq; id: 118; section: C.1.2; page: 98; pdf_page: 104 -->
**(118) Steady-state production function of domestic intermediate goods**

$$
h^{s} = \left(g_{z}\right)^{-\alpha} \left(k^{s}\right)^{\alpha} N^{1-\alpha} - \psi
\tag{118}
$$

Meaning: Normalized supply of domestic intermediate goods is Cobb-Douglas in growth-deflated capital services and hours, minus the fixed cost.

<!-- kind: eq; id: 119; section: C.1.2; page: 98; pdf_page: 104 -->
**(119) Steady-state working-capital interest factor**

$$
R^{F} = 1 + \nu^{F} \left(R - 1\right)
\tag{119}
$$

Meaning: The gross financing cost of the wage bill is one plus the borrowed fraction times the net nominal interest rate.

<!-- kind: eq; id: 120; section: C.1.2; page: 98; pdf_page: 104 -->
**(120) Steady-state cost minimization (capital-labor ratio)**

$$
\frac{k^{s}}{N} = \frac{\alpha}{\left(1-\alpha\right)} g_{z} \frac{\left(1 + \tau^{W_{f}}\right) R^{F} w}{r_{K}}
\tag{120}
$$

Meaning: Capital services per hour rise with the effective labor cost (wage with payroll tax and working-capital financing) relative to the rental rate.

<!-- kind: eq; id: 121; section: C.1.2; page: 98; pdf_page: 104 -->
**(121) Steady-state real marginal cost of domestic intermediate firms (CPI terms)**

$$
mc = \frac{1}{\alpha^{\alpha} \left(1-\alpha\right)^{1-\alpha}} \left(r_{K}\right)^{\alpha} \left[\left(1 + \tau^{W_{f}}\right) R^{F} w\right]^{1-\alpha}
\tag{121}
$$

Meaning: Real marginal cost is a Cobb-Douglas combination of the rental rate and the effective cost of labor.

<!-- kind: eq; id: 122; section: C.1.2; page: 98; pdf_page: 104 -->
**(122) Steady-state optimal price setting of domestic intermediate firms**

$$
\frac{mc}{p_{H}} = \frac{1}{\varphi^{H}}
\tag{122}
$$

Meaning: The domestic intermediate-goods price is the markup times real marginal cost.

### C.1.3 Foreign intermediate goods firms

**Summary.** The importers' marginal cost is substituted into their price-setting condition. In steady state the relative import price becomes a constant markup over a cost that depends on the real exchange rate, the relative GDP deflator and the real oil price, raised to the oil share.

<!-- kind: eq; id: 123; section: C.1.3; page: 98; pdf_page: 104 -->
**(123) Steady-state optimal price setting of foreign intermediate (import) firms**

$$
\frac{s \cdot p_{Y} \left(p_{OIL}^{*}\right)^{\omega^{*}}}{p_{IM}} = \frac{1}{\varphi^{*}}
\tag{123}
$$

Meaning: Importers' marginal cost (real exchange rate times relative price times oil price to the oil share) over the import price equals the inverse markup.

<!-- kind: inline; id: 123.i1; section: C.1.3; page: 98; pdf_page: 104 -->
**(123.i1) Definition of the real exchange rate**

$$
s_{t} \equiv P_{Y,t}^{*} S_{t}/P_{Y,t}
$$

Meaning: The real exchange rate is the foreign intermediate-goods price converted into domestic currency, relative to the domestic GDP deflator.

### C.1.4 Domestic final goods firms

**Summary.** For each of the four final-goods sectors (consumption $C$, investment $I$, government $G$, exports $X$), the steady state gives CES demands for domestic and imported intermediate inputs, and the sector's CES price index. The CPI is the numeraire, so the consumption-sector price index is written as one equal to the CES aggregate, and the consumption-sector demands use $p_{H}$ and $p_{IM}$ directly.

<!-- kind: eq; id: 124; section: C.1.4; page: 99; pdf_page: 105 -->
**(124) Demand for domestic intermediate goods: consumption sector**

$$
h^{C} = \nu_{C} \left(p_{H}\right)^{-\mu_{C}} q^{C}
\tag{124}
$$

Meaning: Consumption-goods producers buy domestic inputs in proportion to their output, scaled by home bias and the relative domestic price raised to minus the elasticity.

<!-- kind: eq; id: 125; section: C.1.4; page: 99; pdf_page: 105 -->
**(125) Demand for domestic intermediate goods: investment sector**

$$
h^{I} = \nu_{I} \left(\frac{p_{H}}{p_{I}}\right)^{-\mu_{I}} q^{I}
\tag{125}
$$

Meaning: Investment-goods producers' demand for domestic inputs depends on their output and the domestic-input price relative to the investment-goods price.

<!-- kind: eq; id: 126; section: C.1.4; page: 99; pdf_page: 105 -->
**(126) Demand for domestic intermediate goods: government-consumption sector**

$$
h^{G} = \nu_{G} \left(\frac{p_{H}}{p_{G}}\right)^{-\mu_{G}} q^{G}
\tag{126}
$$

Meaning: Government-goods producers' demand for domestic inputs depends on their output and the domestic-input price relative to the government-goods price.

<!-- kind: eq; id: 127; section: C.1.4; page: 99; pdf_page: 105 -->
**(127) Demand for domestic intermediate goods: export sector**

$$
h^{X} = \nu_{X} \left(\frac{p_{H}}{p_{DX}}\right)^{-\mu_{X}} q^{X}
\tag{127}
$$

Meaning: Export-goods producers' demand for domestic inputs depends on their output and the domestic-input price relative to the domestic export-good price.

<!-- kind: eq; id: 128; section: C.1.4; page: 99; pdf_page: 105 -->
**(128) Demand for imported intermediate goods: consumption sector**

$$
im^{C} = \left(1 - \nu_{C}\right) \left(p_{IM}\right)^{-\mu_{C}} q^{C}
\tag{128}
$$

Meaning: Consumption-goods producers buy imported inputs in proportion to output, scaled by the import weight and the relative import price raised to minus the elasticity.

<!-- kind: eq; id: 129; section: C.1.4; page: 99; pdf_page: 105 -->
**(129) Demand for imported intermediate goods: investment sector**

$$
im^{I} = \left(1 - \nu_{I}\right) \left(\frac{p_{IM}}{p_{I}}\right)^{-\mu_{I}} q^{I}
\tag{129}
$$

Meaning: Investment-goods producers' demand for imported inputs depends on their output and the import price relative to the investment-goods price.

<!-- kind: eq; id: 130; section: C.1.4; page: 99; pdf_page: 105 -->
**(130) Demand for imported intermediate goods: government-consumption sector**

$$
im^{G} = \left(1 - \nu_{G}\right) \left(\frac{p_{IM}}{p_{G}}\right)^{-\mu_{G}} q^{G}
\tag{130}
$$

Meaning: Government-goods producers' demand for imported inputs depends on their output and the import price relative to the government-goods price.

<!-- kind: eq; id: 131; section: C.1.4; page: 99; pdf_page: 105 -->
**(131) Demand for imported intermediate goods: export sector**

$$
im^{X} = \left(1 - \nu_{X}\right) \left(\frac{p_{IM}}{p_{DX}}\right)^{-\mu_{G}} q^{X}
\tag{131}
$$

Meaning: Export-goods producers' demand for imported inputs depends on their output and the import price relative to the domestic export-good price.

Note: The exponent is printed as −μ_G. The X-sector analogues (127) and (135) use μ_X, so −μ_X would be expected. Suspected typo; C.2's (200) repeats it (see [transcription notes](transcription-notes/T09.md)).

<!-- kind: eq; id: 132; section: C.1.4; page: 99; pdf_page: 105 -->
**(132) Steady-state competitive price: consumption goods (CPI normalized to one)**

$$
1 = \left[\nu_{C} \left(p_{H}\right)^{1-\mu_{C}} + \left(1 - \nu_{C}\right) \left(p_{IM}\right)^{1-\mu_{C}}\right]^{\frac{1}{1-\mu_{C}}}
\tag{132}
$$

Meaning: The CES aggregate of relative domestic and import prices with consumption-sector weights equals one, the relative CPI.

<!-- kind: eq; id: 133; section: C.1.4; page: 100; pdf_page: 106 -->
**(133) Steady-state competitive price: investment goods**

$$
p_{I} = \left[\nu_{I} \left(p_{H}\right)^{1-\mu_{I}} + \left(1 - \nu_{I}\right) \left(p_{IM}\right)^{1-\mu_{I}}\right]^{\frac{1}{1-\mu_{I}}}
\tag{133}
$$

Meaning: The relative investment-goods price is a CES aggregate of the domestic and imported input prices.

<!-- kind: eq; id: 134; section: C.1.4; page: 100; pdf_page: 106 -->
**(134) Steady-state competitive price: government-consumption goods**

$$
p_{G} = \left[\nu_{G} \left(p_{H}\right)^{1-\mu_{G}} + \left(1 - \nu_{G}\right) \left(p_{IM}\right)^{1-\mu_{G}}\right]^{\frac{1}{1-\mu_{G}}}
\tag{134}
$$

Meaning: The relative government-goods price is a CES aggregate of the domestic and imported input prices.

<!-- kind: eq; id: 135; section: C.1.4; page: 100; pdf_page: 106 -->
**(135) Steady-state competitive price: domestic export good**

$$
p_{DX} = \left[\nu_{X} \left(p_{H}\right)^{1-\mu_{X}} + \left(1 - \nu_{X}\right) \left(p_{IM}\right)^{1-\mu_{X}}\right]^{\frac{1}{1-\mu_{X}}}
\tag{135}
$$

Meaning: The relative price of the homogeneous domestic export good is a CES aggregate of the domestic and imported input prices.

### C.1.5 Exporters

**Summary.** The exporters' price-setting condition reduces, in steady state, to a fixed markup. The domestic-currency value of their foreign-currency selling price is a markup over the price of the homogeneous domestic export good that they buy.

<!-- kind: eq; id: 136; section: C.1.5; page: 100; pdf_page: 106 -->
**(136) Steady-state optimal price setting of exporters**

$$
\frac{p_{DX}}{s p_{x} p_{Y}} = \frac{1}{\varphi^{X}}
\tag{136}
$$

Meaning: The domestic export-good price, relative to the domestic-currency value of the export price, equals the inverse of the export markup.

Note: The export price in the denominator is printed with a lowercase subscript, p_x. Elsewhere, e.g. (137), (142) and (152), it is p_X. Suspected typo (see [transcription notes](transcription-notes/T09.md)).

### C.1.6 Foreign retail firms

**Summary.** Foreign demand for the home country's exports in steady state. It depends on the export price relative to the price of world trade, on world trade scaled by foreign productivity, and on foreign technology relative to domestic technology.

<!-- kind: eq; id: 137; section: C.1.6; page: 100; pdf_page: 106 -->
**(137) Steady-state foreign demand for exports**

$$
x = \nu^{*} \left(\frac{p_{X}}{p_{X}^{c,*}}\right)^{-\mu^{*}} wt^{*} \tilde{z}
\tag{137}
$$

Meaning: Exports equal a demand scale times the relative export price raised to minus the export price elasticity, times scaled world trade and relative technology.

<!-- kind: inline; id: 137.i1; section: C.1.6; page: 100; pdf_page: 106 -->
**(137.i1) Definition of scaled world trade**

$$
wt_{t}^{*} = WT_{t}^{*}/z_{t}^{*}
$$

Meaning: Scaled world trade is the level of world trade divided by foreign productivity.

<!-- kind: inline; id: 137.i2; section: C.1.6; page: 100; pdf_page: 106 -->
**(137.i2) Definition of the relative level of technology**

$$
\tilde{z}_{t} = z_{t}^{*}/z_{t}
$$

Meaning: Relative technology is the foreign productivity level divided by domestic productivity.

### C.1.7 Government

**Summary.** The government spending share of GDP and all tax rates are exogenous and treated as parameters. The government budget constraint is written in shares of nominal GDP, with inherited debt deflated by nominal growth. By the fiscal rule (61), lump-sum taxes respond only to the gap between debt and its steady-state level, so they are zero in steady state. Real government consumption follows from its share in GDP.

<!-- kind: inline; id: 137.i3; section: C.1.7; page: 100; pdf_page: 106 -->
**(137.i3) Government expenditure share of GDP (treated as a parameter)**

$$
s_{G}
$$

Meaning: The share of government expenditure in GDP. The government sets it exogenously, so it is a parameter of the steady state.

<!-- kind: inline; id: 137.i4; section: C.1.7; page: 100; pdf_page: 106 -->
**(137.i4) Tax rates (treated as parameters)**

$$
\tau^{C}, \tau^{D}, \tau^{K}, \tau^{N}, \tau^{W_{h}} \text{ and } \tau^{W_{f}}
$$

Meaning: The VAT, dividend, capital, labor-income and household and firm social-security tax rates are exogenous and treated as parameters.

<!-- kind: eq; id: 138; section: C.1.7; page: 100; pdf_page: 106 -->
**(138) Steady-state government budget constraint (shares of GDP)**

$$
\begin{aligned}
s_{G} + \left(\Pi g_{z}\right)^{-1} s_{B} ={}& w_{\tau^{C}} \tau^{C} \frac{c}{p_{Y} y} + \left(\tau^{N} + \tau^{W_{h}} + \tau^{W_{f}}\right) \frac{w N}{p_{Y} y} \\
&+ \frac{\tau^{K}}{g_{z}} \frac{r_{K} k}{p_{Y} y} - \frac{\tau^{K} \delta}{g_{z}} \frac{p_{I} k}{p_{Y} y} + \tau^{D} s_{D} + s_{T} + \frac{s_{B}}{R}
\end{aligned}
\tag{138}
$$

Meaning: Spending plus inherited debt (deflated by nominal growth) equals VAT, labor-tax and capital-tax revenue (net of the depreciation allowance), dividend tax, lump-sum taxes and new debt valued at 1/R.

<!-- kind: eq; id: 139; section: C.1.7; page: 101; pdf_page: 107 -->
**(139) Steady-state lump-sum taxes**

$$
s_{T} = 0
\tag{139}
$$

Meaning: Zero in steady state: by rule (61) lump-sum taxes respond only to the gap between debt and its steady-state level, which is zero there.

<!-- kind: eq; id: 140; section: C.1.7; page: 101; pdf_page: 107 -->
**(140) Real government consumption**

$$
g = \frac{p_{Y} y}{p_{G}} s_{G}
\tag{140}
$$

Meaning: Real government consumption is the spending share times nominal GDP, divided by the relative price of government goods.

### C.1.8 Net foreign assets and the current account

**Summary.** The trade balance, export and import shares of GDP are defined. The external intermediation premium drives steady-state net foreign assets to zero, so the current account balances. The trade-balance share therefore equals minus the exogenous foreign-transfer share.

<!-- kind: eq; id: 141; section: C.1.8; page: 101; pdf_page: 107 -->
**(141) Trade balance as a share of GDP**

$$
s_{TB} = s_{X} - s_{IM}
\tag{141}
$$

Meaning: The trade-balance share of GDP is the export share minus the import share.

<!-- kind: eq; id: 142; section: C.1.8; page: 101; pdf_page: 107 -->
**(142) Export share of GDP**

$$
s_{X} = \frac{s \cdot p_{X} x}{y}
\tag{142}
$$

Meaning: The export share is the real exchange rate times the relative export price times exports, divided by output.

<!-- kind: eq; id: 143; section: C.1.8; page: 101; pdf_page: 107 -->
**(143) Import share of GDP**

$$
s_{IM} = \frac{p_{IM} im}{p_{Y} y}
\tag{143}
$$

Meaning: The import share is the value of imports at the relative import price, divided by nominal GDP.

<!-- kind: inline; id: 143.i1; section: C.1.8; page: 101; pdf_page: 107 -->
**(143.i1) Zero steady-state net foreign assets (restated)**

$$
B^{*} = 0
$$

Meaning: Because of the external intermediation premium, the steady-state net foreign asset position is zero.

<!-- kind: eq; id: 144; section: C.1.8; page: 101; pdf_page: 107 -->
**(144) Balanced current account in steady state**

$$
s_{TB} = -s_{FTR}
\tag{144}
$$

Meaning: With a balanced current account, the trade-balance share of GDP equals minus the share of foreign transfers.

<!-- kind: inline; id: 144.i1; section: C.1.8; page: 101; pdf_page: 107 -->
**(144.i1) Foreign transfers share of GDP**

$$
s_{FTR}
$$

Meaning: The exogenous weight of foreign transfers in GDP.

### C.1.9 Market-clearing conditions

**Summary.** These are the steady-state market-clearing conditions: capital, domestic and imported intermediate goods, and the four final-goods markets (investment goods also cover inventory investment, export goods also cover the exporters' fixed cost). They are followed by nominal GDP, the aggregate nominal resource constraint (also at market prices, with VAT on consumption) and the definition of real output. The section ends with the profit shares of the export sector and of the whole economy. No adding-up equation for $h$ (the analogue of (147) for imports) is listed, because the paper states it is implied by the price, final-goods, import, GDP and resource equations.

<!-- kind: eq; id: 145; section: C.1.9; page: 101; pdf_page: 107 -->
**(145) Capital-market clearing**

$$
k = k^{s}
\tag{145}
$$

Meaning: Capital services used in production equal the normalized capital stock.

<!-- kind: eq; id: 146; section: C.1.9; page: 102; pdf_page: 108 -->
**(146) Domestic intermediate goods market clearing**

$$
h^{s} = h
\tag{146}
$$

Meaning: Supply of domestic intermediate goods equals total demand for them.

<!-- kind: eq; id: 147; section: C.1.9; page: 102; pdf_page: 108 -->
**(147) Imported intermediate goods market clearing**

$$
im = im^{C} + im^{I} + im^{G} + im^{X}
\tag{147}
$$

Meaning: Total imports equal the sum of imported inputs used by the four final-goods sectors.

<!-- kind: eq; id: 148; section: C.1.9; page: 102; pdf_page: 108 -->
**(148) Final consumption goods market clearing**

$$
q^{C} = c
\tag{148}
$$

Meaning: Output of final consumption goods equals consumption.

<!-- kind: eq; id: 149; section: C.1.9; page: 102; pdf_page: 108 -->
**(149) Final investment goods market clearing**

$$
q^{I} = i + \Delta inv \cdot y
\tag{149}
$$

Meaning: Output of investment goods covers fixed investment plus inventory investment, which is its GDP weight times output.

<!-- kind: inline; id: 149.i1; section: C.1.9; page: 102; pdf_page: 108 -->
**(149.i1) Steady-state weight of inventory investment in GDP**

$$
\Delta inv
$$

Meaning: Inventory investment as a share of GDP in steady state, set outside the model (a given input).

<!-- kind: eq; id: 150; section: C.1.9; page: 102; pdf_page: 108 -->
**(150) Final government-consumption goods market clearing**

$$
q^{G} = g
\tag{150}
$$

Meaning: Output of government-consumption goods equals real government consumption.

<!-- kind: eq; id: 151; section: C.1.9; page: 102; pdf_page: 108 -->
**(151) Final export goods market clearing**

$$
q^{X} = x + \psi^{X}
\tag{151}
$$

Meaning: Output of the homogeneous export good covers exports plus the exporters' fixed cost.

<!-- kind: eq; id: 152; section: C.1.9; page: 102; pdf_page: 108 -->
**(152) Steady-state nominal GDP (value added)**

$$
p_{Y} y = p_{H} h + s \cdot p_{X} p_{Y} x - p_{DX} q^{X}
\tag{152}
$$

Meaning: Nominal GDP is the value of domestic intermediate goods plus the domestic-currency value of exports, minus exporters' purchases of the homogeneous export good.

<!-- kind: eq; id: 153; section: C.1.9; page: 102; pdf_page: 108 -->
**(153) Steady-state aggregate nominal resource constraint**

$$
p_{Y} y = c + p_{I} i + \Delta inv \cdot p_{I} y + p_{G} g + s \cdot p_{X} p_{Y} x - p_{IM} im
\tag{153}
$$

Meaning: Nominal GDP equals consumption, fixed and inventory investment, government consumption and exports, minus imports, all at relative prices.

<!-- kind: eq; id: 154; section: C.1.9; page: 102; pdf_page: 108 -->
**(154) Steady-state aggregate resource constraint at market prices**

$$
p_{Y}^{M} y = \left(1 + w_{\tau^{C}} \tau^{C}\right) c + p_{I} i + \Delta inv \cdot p_{I} y + p_{G} g + s \cdot p_{X} p_{Y} x - p_{IM} im
\tag{154}
$$

Meaning: The same resource constraint with consumption valued including VAT, which defines GDP at market prices.

<!-- kind: eq; id: 155; section: C.1.9; page: 103; pdf_page: 109 -->
**(155) Steady-state real output**

$$
y = h^{s}
\tag{155}
$$

Meaning: Real output equals the supply of domestic intermediate goods.

<!-- kind: eq; id: 156; section: C.1.9; page: 103; pdf_page: 109 -->
**(156) Steady-state share of profits in the export sector**

$$
s_{DX} = s \cdot p_{X} \frac{x}{y} - \frac{p_{DX} \left(x + \psi^{X}\right)}{p_{Y} y}
\tag{156}
$$

Meaning: Export-sector profits as a share of GDP are export revenue over output minus the cost of the export good used (exports plus fixed cost) over nominal GDP.

<!-- kind: eq; id: 157; section: C.1.9; page: 103; pdf_page: 109 -->
**(157) Steady-state total share of profits in the economy**

$$
s_{D} = 1 - \frac{mc}{p_{Y}} \left(\frac{h^{s}}{y} + \frac{\psi}{y}\right)
\tag{157}
$$

Meaning: The economy-wide profit share is one minus real marginal cost (relative to the GDP deflator) times intermediate output plus the fixed cost, both per unit of output.

## C.2 The recursive steady-state solution

**Summary.** The 48 steady-state conditions (110)–(157) are solved one unknown at a time (a recursive rather than fully explicit solution), so that the system stays easy to modify. Two choices start the recursion. First, the real exchange rate is normalized to $s=1$ and taken as given, and scaled world trade $wt^{*}$ becomes an unknown in its place. Second, steady-state dividends are set to zero ($s_{D}=s_{DX}=0$) and taken as given, and the fixed production costs $\psi$ and $\psi^{X}$ (of technologies (17) and (46)) become unknowns instead; the paper lists the 48 unknowns and the parameters that enter, and the next step, after these normalizations, imposes full capital utilization $u=1$ from (116).

<!-- kind: inline; id: 157.i1; section: C.2; page: 103; pdf_page: 109 -->
**Inline 157.i1: Normalization of the steady-state real exchange rate**

$$
s = 1
$$

Meaning: The steady-state real exchange rate is fixed at one and treated as a given input of the steady-state solution.

<!-- kind: inline; id: 157.i2; section: C.2; page: 103; pdf_page: 109 -->
**Inline 157.i2: Zero steady-state profit (dividend) shares**

$$
s_{D} = s_{DX} = 0
$$

Meaning: Both the economy-wide profit share and the export-sector profit share of GDP are set to zero and treated as given.

<!-- kind: display; id: 157.u1; section: C.2; page: 104; pdf_page: 110 -->
**Display 157.u1: The 48 steady-state unknowns of the recursive solution**

$$
\begin{aligned}
& wt^{*}, \psi, \psi^{X}, p_{Y}, p_{Y}^{M}, p_{X}, p_{I}, p_{G}, p_{DX}, p_{H}, p_{IM}, mc, r_{K}, w, R^{F}, N, u, k, k^{s}, \lambda, Q, y, c, i, g, x, \\
& q^{C}, q^{I}, q^{G}, q^{X}, h, h^{s}, h^{C}, h^{I}, h^{G}, h^{X}, im^{C}, im^{I}, im^{G}, im^{X}, s_{T}, s_{B}, s_{X}, s_{IM}, s_{TB}, p_{DX}, R, R^{*}
\end{aligned}
$$

Meaning: The steady-state variables determined by the recursion; world trade and the two fixed costs take the place of the real exchange rate and the profit shares.

Note: $p_{DX}$ is printed twice (first and second line) and total imports $im$, solved in (201), is not listed; transcribed as printed (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: display; id: 157.u2; section: C.2; page: 104; pdf_page: 110 -->
**Display 157.u2: Parameters that affect the steady-state solution**

$$
\begin{aligned}
& s, s_{D}, s_{DX}, \alpha, \beta, \zeta, \delta, g_{z}, \kappa, \mu^{C}, \mu^{I}, \mu^{G}, \mu^{X}, \mu^{*}, \nu_{C}, \nu_{I}, \nu_{G}, \nu_{X}, \nu^{*}, \nu^{F}, p_{X}^{C}, \Pi, s_{G}, \\
& \tau^{C}, \tau^{D}, \tau^{K}, \tau^{N}, \tau^{W_{h}}, \tau^{W_{f}}, \varphi^{W}, \varphi^{*}, \varphi^{H}, \varphi^{X}, \tilde{z}, s_{FTR}, p_{OIL}^{*}, \omega^{*}, \Delta inv
\end{aligned}
$$

Meaning: The subset of parameters, including the normalized $s$, $s_{D}$ and $s_{DX}$, on which the steady-state values depend.

Note: the elasticities are printed with superscripts here ($\mu^{C}$, …) but with subscripts ($\mu_{C}$, …) in the equations; the competitors' export price is $p_{X}^{C}$ here but $p_{X}^{c,*}$ in (205); $w_{\tau^{C}}$, which enters 179.u1, (180), (207), (210) and (211), is not listed (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: eq; id: 158; section: C.2; page: 104; pdf_page: 110 -->
**(158) Full capital utilization in steady state**

$$
u = 1
\tag{158}
$$

Meaning: The next step of the recursion, after the normalizations: steady-state capital utilization equals one, taken from the full-utilization assumption (116).

### C.2.1 Solving for prices

**Summary.** Relative prices are solved first, taking as given $s$, $s_{DX}$, $\varphi^{*}$, $\omega^{*}$, $\varphi^{H}$, $\varphi^{X}$, the oil price $p_{OIL}^{*}$ (calibrated at the end of this step) and the home-bias weights and elasticities $\nu_{C},\nu_{I},\nu_{G},\nu_{X}$, $\mu_{C},\mu_{I},\mu_{G},\mu_{X}$. Substituting (151) and (156) into nominal GDP (152) and using (155) links $p_{Y}$ to $p_{H}$; inserting this into the import-pricing condition (123) gives the import-to-domestic price ratio $p_{IM\_H}$ (159), and the consumption-good price index (132) then gives $p_{H}$ through the composite $A_{C}$ (160), hence $p_{Y}$ (161), $p_{IM}$ (162) and, via (122), $mc$ (163). The investment, government and export final-good price indices (133)–(135) give $p_{I}$ (164), $p_{G}$ (165) and $p_{DX}$ (166) through the composites $A_{I}$, $A_{G}$, $A_{X}$, and the exporters' pricing condition (136) gives the foreign-market export price (167). Finally, $p_{OIL}^{*}$ is calibrated so that $p_{IM\_H}=1$ (167.u1); with $s=1$ and $s_{DX}=0$ this gives $p_{Y}=p_{I}=p_{G}=p_{H}=p_{IM}=p_{DX}=1$, $mc=1/\varphi^{H}$ and $p_{X}=\varphi^{X}$, so the steady state does not depend on the substitution elasticities.

<!-- kind: display; id: 158.u1; section: C.2.1; page: 104; pdf_page: 110 -->
**Display 158.u1: Nominal GDP with the export profit share substituted**

$$
p_{Y} y = p_{H} h + p_{Y} y s_{DX}
$$

Meaning: Nominal GDP equals the value of domestic intermediate output plus export-sector profits, the latter written as their share of nominal GDP.

<!-- kind: display; id: 158.u2; section: C.2.1; page: 104; pdf_page: 110 -->
**Display 158.u2: Output deflator in terms of the domestic intermediate price**

$$
p_{Y} = \left(1 - s_{DX}\right)^{-1} p_{H}
$$

Meaning: The output deflator equals the domestic intermediate-goods price scaled up by one over one minus the export profit share.

<!-- kind: eq; id: 159; section: C.2.1; page: 104; pdf_page: 110 -->
**(159) Ratio of the import price to the domestic intermediate price**

$$
p_{IM\_H} \left(= \frac{p_{IM}}{p_{H}}\right) = \varphi^{*} \left(p_{OIL}^{*}\right)^{\omega^{*}} s \left(1 - s_{DX}\right)^{-1}
\tag{159}
$$

Meaning: Defines $p_{IM\_H}$ as $p_{IM}/p_{H}$ and expresses it through the import markup, the oil price raised to the oil share, the real exchange rate and the export profit share.

<!-- kind: display; id: 159.u1; section: C.2.1; page: 105; pdf_page: 111 -->
**Display 159.u1: Consumption-good price index (132) rewritten to solve for $p_{H}$**

$$
\frac{1}{p_{H}} = \left[\nu_{C} + \left(1 - \nu_{C}\right) \left(\frac{p_{IM}}{p_{H}}\right)^{1-\mu_{C}}\right]^{\frac{1}{1-\mu_{C}}}
$$

Meaning: With the consumption good as numeraire, the inverse domestic intermediate price is a CES aggregate of one and the import-to-domestic price ratio.

<!-- kind: eq; id: 160; section: C.2.1; page: 105; pdf_page: 111 -->
**(160) Domestic intermediate-goods price and the composite $A_{C}$**

$$
p_{H} = \left(A_{C}\right)^{-1} \quad \text{with} \quad A_{C} = \left[\nu_{C} + \left(1 - \nu_{C}\right) \left(p_{IM\_H}\right)^{1-\mu_{C}}\right]^{\frac{1}{1-\mu_{C}}}
\tag{160}
$$

Meaning: The relative domestic intermediate price is the inverse of a consumption-sector CES composite of one and the import-to-domestic price ratio.

<!-- kind: eq; id: 161; section: C.2.1; page: 105; pdf_page: 111 -->
**(161) Output deflator**

$$
p_{Y} = \left(1 - s_{DX}\right)^{-1} \left(A_{C}\right)^{-1}
\tag{161}
$$

Meaning: The output deflator is the domestic intermediate price from (160) scaled by the export profit-share term.

<!-- kind: eq; id: 162; section: C.2.1; page: 105; pdf_page: 111 -->
**(162) Price of imported intermediate goods**

$$
p_{IM} = \varphi^{*} \left(p_{OIL}^{*}\right)^{\omega^{*}} s \cdot \left(1 - s_{DX}\right)^{-1} \left(A_{C}\right)^{-1}
\tag{162}
$$

Meaning: The relative import price equals the import-to-domestic price ratio (159) times the domestic intermediate price (160).

<!-- kind: eq; id: 163; section: C.2.1; page: 105; pdf_page: 111 -->
**(163) Real marginal cost of domestic intermediate-goods firms**

$$
mc = \frac{1}{\varphi^{H}} \left(A_{C}\right)^{-1}
\tag{163}
$$

Meaning: Domestic firms' real marginal cost equals the domestic intermediate price divided by the domestic price markup.

<!-- kind: display; id: 163.u1; section: C.2.1; page: 105; pdf_page: 111 -->
**Display 163.u1: Investment-good price index (133) with $p_{H}$ factored out**

$$
p_{I} = p_{H} \left[\nu_{I} + \left(1 - \nu_{I}\right) \left(\frac{p_{IM}}{p_{H}}\right)^{1-\mu_{I}}\right]^{\frac{1}{1-\mu_{I}}}
$$

Meaning: The investment-good price is the domestic intermediate price times a CES aggregate of one and the import-to-domestic price ratio.

<!-- kind: eq; id: 164; section: C.2.1; page: 105; pdf_page: 111 -->
**(164) Investment-good price and the composite $A_{I}$**

$$
p_{I} = \left(A_{C}\right)^{-1} A_{I} \quad \text{with} \quad A_{I} = \left[\nu_{I} + \left(1 - \nu_{I}\right) \left(p_{IM\_H}\right)^{1-\mu_{I}}\right]^{\frac{1}{1-\mu_{I}}}
\tag{164}
$$

Meaning: The relative investment-good price equals the investment-sector CES composite of the price ratio divided by the consumption composite $A_{C}$.

<!-- kind: display; id: 164.u1; section: C.2.1; page: 105; pdf_page: 111 -->
**Display 164.u1: Government-consumption-good price index (134) with $p_{H}$ factored out**

$$
p_{G} = p_{H} \left[\nu_{G} + \left(1 - \nu_{G}\right) \left(\frac{p_{IM}}{p_{H}}\right)^{1-\mu_{G}}\right]^{\frac{1}{1-\mu_{G}}}
$$

Meaning: The government-good price is the domestic intermediate price times a CES aggregate of one and the import-to-domestic price ratio.

<!-- kind: eq; id: 165; section: C.2.1; page: 105; pdf_page: 111 -->
**(165) Government-consumption-good price and the composite $A_{G}$**

$$
p_{G} = \left(A_{C}\right)^{-1} A_{G} \quad \text{with} \quad A_{G} = \left[\nu_{G} + \left(1 - \nu_{G}\right) \left(p_{IM\_H}\right)^{1-\mu_{G}}\right]^{\frac{1}{1-\mu_{G}}}
\tag{165}
$$

Meaning: The relative government-good price equals the government-sector CES composite of the price ratio divided by the consumption composite $A_{C}$.

<!-- kind: display; id: 165.u1; section: C.2.1; page: 105; pdf_page: 111 -->
**Display 165.u1: Export-good price index (135) with $p_{H}$ factored out**

$$
p_{DX} = p_{H} \left[\nu_{X} + \left(1 - \nu_{X}\right) \left(\frac{p_{IM}}{p_{H}}\right)^{1-\mu_{X}}\right]^{\frac{1}{1-\mu_{X}}}
$$

Meaning: The final export good's price is the domestic intermediate price times a CES aggregate of one and the import-to-domestic price ratio.

<!-- kind: eq; id: 166; section: C.2.1; page: 106; pdf_page: 112 -->
**(166) Final export-good price and the composite $A_{X}$**

$$
p_{DX} = \left(A_{C}\right)^{-1} A_{X} \quad \text{with} \quad A_{X} = \left[\nu_{X} + \left(1 - \nu_{X}\right) \left(p_{IM\_H}\right)^{1-\mu_{X}}\right]^{\frac{1}{1-\mu_{X}}}
\tag{166}
$$

Meaning: The relative price of the final export good equals the export-sector CES composite of the price ratio divided by the consumption composite $A_{C}$.

<!-- kind: eq; id: 167; section: C.2.1; page: 106; pdf_page: 112 -->
**(167) Export price in foreign markets**

$$
p_{x} = \frac{\varphi^{X} p_{DX}}{s \cdot p_{Y}}
\tag{167}
$$

Meaning: The export price abroad equals the export markup times the final export-good price, divided by the real exchange rate times the output deflator.

Note: the subscript is printed lowercase ($p_{x}$) here, as in (136), while the export price is written $p_{X}$ elsewhere in C.2 (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: display; id: 167.u1; section: C.2.1; page: 106; pdf_page: 112 -->
**Display 167.u1: Calibration condition that pins down the steady-state oil price**

$$
\varphi^{*} \left(p_{OIL}^{*}\right)^{\omega^{*}} s \left(1 - s_{DX}\right)^{-1} = 1
$$

Meaning: The oil price is chosen so that the import-to-domestic price ratio (159) equals one, so home-bias shocks have no direct effect on final-good prices.

<!-- kind: inline; id: 167.i1; section: C.2.1; page: 106; pdf_page: 112 -->
**Inline 167.i1: Relative prices implied by the oil-price calibration**

$$
p_{Y} = p_{I} = p_{G} = p_{H} = p_{IM} = p_{DX} = 1
$$

Meaning: Under the oil-price condition (with $s_{DX} = 0$ already imposed), the output deflator and the intermediate and final-good relative prices all equal one.

<!-- kind: inline; id: 167.i2; section: C.2.1; page: 106; pdf_page: 112 -->
**Inline 167.i2: Real marginal cost implied by the oil-price calibration**

$$
mc = 1/\varphi^{H}
$$

Meaning: Under the oil-price condition, domestic firms' real marginal cost equals the inverse of the domestic price markup.

<!-- kind: inline; id: 167.i3; section: C.2.1; page: 106; pdf_page: 112 -->
**Inline 167.i3: Export price implied by the oil-price calibration**

$$
p_{X} = \varphi^{X}
$$

Meaning: Under the oil-price condition, given $s = 1$ and $s_{DX} = 0$, the export price in foreign markets equals the export price markup.

### C.2.2 Solving for input prices and the trade balance

**Summary.** Given $g_{z}$, $\Pi$, $\beta$ and $\nu^{F}$, the Euler conditions (111) and (112), the working-capital cost (119) and the investment FOC (114) give $R$ (168), $R^{*}$ (169), $R^{F}$ (170) and $Q=p_{I}$ (171); footnote 56 (no math) adds the assumption that home and foreign long-run inflation targets coincide. The capital FOC (115) gives the rental rate $r_{K}$ (172), with $\gamma_{u,1}$ fixed by a restriction on $\beta$, $g_{z}$, $\delta$ and $\tau^{K}$ (172.u1). The marginal-cost condition (121) is inverted for the real wage $w$ (173), given $\alpha$, $\tau^{W_{f}}$ and the already solved $mc$, $r_{K}$, $R^{F}$, and a balanced current account with (144) sets the trade-balance share $s_{TB}$ from the given foreign-transfer share $s_{FTR}$ (174).

<!-- kind: eq; id: 168; section: C.2.2; page: 106; pdf_page: 112 -->
**(168) Domestic nominal interest rate**

$$
R = \frac{g_{z} \Pi}{\beta}
\tag{168}
$$

Meaning: The steady-state gross domestic interest rate equals trend productivity growth times the inflation target, divided by the discount factor.

<!-- kind: eq; id: 169; section: C.2.2; page: 106; pdf_page: 112 -->
**(169) Foreign nominal interest rate**

$$
R^{*} = \frac{g_{z} \Pi}{\beta}
\tag{169}
$$

Meaning: The steady-state gross foreign interest rate takes the same value as the domestic one.

<!-- kind: eq; id: 170; section: C.2.2; page: 106; pdf_page: 112 -->
**(170) Gross cost of working-capital financing**

$$
R^{F} = 1 + \nu^{F} \left(R - 1\right)
\tag{170}
$$

Meaning: The working-capital cost factor is one plus the net interest rate paid on the fraction $\nu^{F}$ of the wage bill borrowed.

<!-- kind: eq; id: 171; section: C.2.2; page: 106; pdf_page: 112 -->
**(171) Tobin's Q**

$$
Q = p_{I}
\tag{171}
$$

Meaning: In steady state the value of installed capital equals the relative price of investment goods.

<!-- kind: eq; id: 172; section: C.2.2; page: 107; pdf_page: 113 -->
**(172) Real rental rate of capital**

$$
r_{K} = \gamma_{u,1} p_{I}
\tag{172}
$$

Meaning: The real rental rate of capital equals the utilization-cost parameter $\gamma_{u,1}$ times the investment-good price.

<!-- kind: display; id: 172.u1; section: C.2.2; page: 107; pdf_page: 113 -->
**Display 172.u1: Definition of $\gamma_{u,1}$ (parameter restriction)**

$$
\gamma_{u,1} = \left[\frac{\beta}{g_{z}} - \left(1 - \delta + \tau^{K} \delta\right)\right] \left(1 - \tau^{K}\right)^{-1}
$$

Meaning: The utilization-cost parameter is tied to the discount factor, trend growth, depreciation and the capital tax rate, consistent with full utilization.

Note: printed $\beta/g_{z}$ here, in (115) and in the C.1 restriction; the C.1 expression for $Q$ (denominator $g_{z}/\beta - (1-\delta)$) combined with (114) implies $g_{z}/\beta$. Suspected typo, transcribed as printed (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: eq; id: 173; section: C.2.2; page: 107; pdf_page: 113 -->
**(173) Real wage**

$$
w = \left[\frac{\alpha^{\alpha} \left(1 - \alpha\right)^{1-\alpha}}{\left(1 + \tau^{W_{f}}\right)^{1-\alpha}} mc \left(r_{K}\right)^{-\alpha} \left(R^{F}\right)^{-\left(1-\alpha\right)}\right]^{\frac{1}{1-\alpha}}
\tag{173}
$$

Meaning: The Cobb-Douglas marginal-cost condition inverted for the real wage, given marginal cost, the rental rate, the working-capital cost and the firms' payroll tax.

<!-- kind: eq; id: 174; section: C.2.2; page: 107; pdf_page: 113 -->
**(174) Trade-balance share of GDP**

$$
s_{TB} = -s_{FTR}
\tag{174}
$$

Meaning: With a balanced current account, the trade-balance share of GDP is minus the foreign-transfer share of GDP.

### C.2.3 Solving for quantities per working hours

**Summary.** Quantities are first expressed per hour worked, using the prices from C.2.1–C.2.2 and the given $\alpha$, $g_{z}$, $\delta$, $\tau^{W_{f}}$, $s_{D}$ and $s_{G}$. Capital-market clearing (145) gives $k^{s}=k$, cost minimization (120) gives $k/N$ (175) and capital accumulation (113) gives $i/N$ (176). The profit-share definition (157) gives $h^{s}+\psi$, which is substituted into the production function (118) to obtain $y/N$ (177) without $\psi$, and the definition of real government consumption (140), divided by $N$, gives $g/N$ (178).

<!-- kind: inline; id: 174.i1; section: C.2.3; page: 107; pdf_page: 113 -->
**Inline 174.i1: Capital services equal the capital stock**

$$
k^{s} = k
$$

Meaning: By capital-market clearing (145), capital services used in production equal the normalized capital stock.

<!-- kind: eq; id: 175; section: C.2.3; page: 107; pdf_page: 113 -->
**(175) Capital per hour worked**

$$
\left(\frac{k}{N}\right) = \frac{\alpha}{\left(1 - \alpha\right)} g_{z} \frac{\left(1 + \tau^{W_{f}}\right) R^{F} w}{r_{K}}
\tag{175}
$$

Meaning: The capital-hours ratio is proportional to the payroll-tax- and financing-inclusive wage relative to the rental rate, scaled by $\alpha/(1-\alpha)$ and trend growth.

<!-- kind: eq; id: 176; section: C.2.3; page: 107; pdf_page: 113 -->
**(176) Investment per hour worked**

$$
\left(\frac{i}{N}\right) = \frac{i}{k} \left(\frac{k}{N}\right) = \left(1 - \frac{1 - \delta}{g_{z}}\right) \left(\frac{k}{N}\right)
\tag{176}
$$

Meaning: Investment per hour is the steady-state investment-capital ratio, determined by depreciation and trend growth, times capital per hour.

<!-- kind: display; id: 176.u1; section: C.2.3; page: 107; pdf_page: 113 -->
**Display 176.u1: Domestic intermediate output plus fixed cost, from the profit share (157)**

$$
\left(h^{s} + \psi\right) = \left(1 - s_{D}\right) \frac{p_{Y} y}{mc}
$$

Meaning: Domestic intermediate supply plus the fixed cost equals nominal GDP net of the profit share, divided by marginal cost.

<!-- kind: eq; id: 177; section: C.2.3; page: 107; pdf_page: 113 -->
**(177) Output per hour worked**

$$
\left(\frac{y}{N}\right) = \left(1 - s_{D}\right)^{-1} \left(\left(g_{z}\right)^{-1} \frac{k}{N}\right)^{\alpha} \frac{mc}{p_{Y}}
\tag{177}
$$

Meaning: Output per hour is the growth-adjusted capital-hours ratio to the power $\alpha$, times marginal cost over the deflator, scaled by the profit-share term.

<!-- kind: eq; id: 178; section: C.2.3; page: 107; pdf_page: 113 -->
**(178) Government consumption per hour worked**

$$
\left(\frac{g}{N}\right) = s_{G} \frac{p_{Y}}{p_{G}} \left(\frac{y}{N}\right)
\tag{178}
$$

Meaning: Real government consumption per hour is its nominal GDP share, converted at the relative government-good price, times output per hour.

### C.2.4 Solving for hours worked ($N$)

**Summary.** The aggregate resource constraint (153) written per hour worked, together with the trade-share definitions (141)–(143), gives consumption per hour $c/N$ (179) as a residual, using the given $\Delta inv$, $s_{TB}$ from (174) and the per-hour ratios of C.2.3. Combining household wage setting (117) with the consumption FOC (110) gives a labour-supply condition in which hours enter through $N^{\zeta}$ and through $c=(c/N)N$, which is solved in closed form for $N$ (180), taking $\varphi^{W}$, $w_{\tau^{C}}$, $\tau^{C}$, $\kappa$, $g_{z}$, $\tau^{N}$, $\tau^{W_{h}}$ and $\zeta$ as given.

<!-- kind: display; id: 178.u1; section: C.2.4; page: 108; pdf_page: 114 -->
**Display 178.u1: Aggregate resource constraint (153) per hour worked**

$$
p_{Y} \frac{y}{N} = \frac{c}{N} + p_{I} \frac{i}{N} + \Delta inv \cdot p_{I} \frac{y}{N} + p_{G} \frac{g}{N} + \frac{s \cdot p_{X} p_{Y} x - p_{IM} im}{N}
$$

Meaning: Nominal output per hour equals consumption, fixed investment, inventory investment, government consumption and net exports, each per hour worked.

<!-- kind: eq; id: 179; section: C.2.4; page: 108; pdf_page: 114 -->
**(179) Consumption per hour worked**

$$
\left(\frac{c}{N}\right) = p_{Y} \left(\frac{y}{N}\right) - p_{I} \left(\frac{i}{N}\right) - \Delta inv \cdot p_{I} \left(\frac{y}{N}\right) - p_{G} \left(\frac{g}{N}\right) - s_{TB} p_{Y} \left(\frac{y}{N}\right)
\tag{179}
$$

Meaning: Consumption per hour is nominal output per hour minus investment, inventory investment, government consumption and the trade balance, all per hour.

<!-- kind: display; id: 179.u1; section: C.2.4; page: 108; pdf_page: 114 -->
**Display 179.u1: Wage setting (117) combined with the consumption FOC (110)**

$$
\left(1 - \tau^{N} - \tau^{W_{h}}\right) w = \varphi^{W} N^{\zeta} \left(\lambda\right)^{-1} = \varphi^{W} N^{\zeta} \left(\frac{\left(1 - \kappa/g_{z}\right)^{-1}}{1 + w_{\tau^{C}} \tau^{C}} \frac{1}{c}\right)^{-1}
$$

Meaning: The after-tax real wage equals the wage markup times hours to the power $\zeta$ over the marginal utility of income, which is replaced by its consumption expression.

<!-- kind: eq; id: 180; section: C.2.4; page: 108; pdf_page: 114 -->
**(180) Hours worked**

$$
N = \left[\varphi^{W} \left(1 + w_{\tau^{C}} \tau^{C}\right) \left(1 - \kappa/g_{z}\right) \left(1 - \tau^{N} - \tau^{W_{h}}\right)^{-1} \left(\frac{c}{N}\right) w^{-1}\right]^{-\left(\frac{1}{\zeta+1}\right)}
\tag{180}
$$

Meaning: Closed-form steady-state hours from the wage markup, VAT, habit, labour taxes, consumption per hour and the real wage, raised to minus one over $\zeta+1$.

### C.2.5 Returning to levels

**Summary.** With $N$ known from (180), the levels of consumption, output, government consumption, investment and capital follow by multiplying the per-hour ratios (179), (177), (178), (176) and (175) by $N$, giving (181)–(185). Capital services, domestic intermediate supply and domestic intermediate demand are then set from (145), (155) and (146): $k^{s}=k$ (186), $h^{s}=y$ (187) and $h=h^{s}$ (188).

<!-- kind: eq; id: 181; section: C.2.5; page: 108; pdf_page: 114 -->
**(181) Consumption level**

$$
c = \left(\frac{c}{N}\right) N
\tag{181}
$$

Meaning: Consumption equals consumption per hour times hours worked.

<!-- kind: eq; id: 182; section: C.2.5; page: 108; pdf_page: 114 -->
**(182) Output level**

$$
y = \left(\frac{y}{N}\right) N
\tag{182}
$$

Meaning: Real output equals output per hour times hours worked.

<!-- kind: eq; id: 183; section: C.2.5; page: 108; pdf_page: 114 -->
**(183) Government consumption level**

$$
g = \left(\frac{g}{N}\right) N
\tag{183}
$$

Meaning: Real government consumption equals its per-hour value times hours worked.

<!-- kind: eq; id: 184; section: C.2.5; page: 108; pdf_page: 114 -->
**(184) Investment level**

$$
i = \left(\frac{i}{N}\right) N
\tag{184}
$$

Meaning: Fixed investment equals investment per hour times hours worked.

<!-- kind: eq; id: 185; section: C.2.5; page: 109; pdf_page: 115 -->
**(185) Capital stock level**

$$
k = \left(\frac{k}{N}\right) N
\tag{185}
$$

Meaning: The normalized capital stock equals capital per hour times hours worked.

<!-- kind: eq; id: 186; section: C.2.5; page: 109; pdf_page: 115 -->
**(186) Capital services**

$$
k^{s} = k
\tag{186}
$$

Meaning: Capital services equal the capital stock (capital-market clearing (145)).

<!-- kind: eq; id: 187; section: C.2.5; page: 109; pdf_page: 115 -->
**(187) Supply of domestic intermediate goods**

$$
h^{s} = y
\tag{187}
$$

Meaning: Domestic intermediate-goods supply equals real output (definition of real output (155)).

<!-- kind: eq; id: 188; section: C.2.5; page: 109; pdf_page: 115 -->
**(188) Demand for domestic intermediate goods**

$$
h = h^{s}
\tag{188}
$$

Meaning: Total demand for domestic intermediate goods equals their supply (market clearing (146)).

### C.2.6 Solving for sector-specific intermediate goods, imports and exports

**Summary.** Final-goods market clearing (148)–(150) gives $q^{C}$, $q^{I}$, $q^{G}$ (189)–(191), with the given inventory share $\Delta inv$ in $q^{I}$. The steady-state demands for domestic and imported intermediate goods in the C, I and G sectors, (124)–(126) and (128)–(130), give $h^{C}$, $h^{I}$, $h^{G}$ and $im^{C}$, $im^{I}$, $im^{G}$ (192)–(197), given $\nu_{C},\nu_{I},\nu_{G}$ and $\mu_{C},\mu_{I},\mu_{G}$. The exporters' use of domestic intermediates $h^{X}$ is the residual of total $h$ (198), from an aggregation identity that holds in steady state but is not among the 48 equations; then (127) gives $q^{X}$ (199), (131) gives $im^{X}$ (200) and import-market clearing (147) gives total imports $im$ (201). The import share, export share and export volume follow from (143), (141) and (142) as (202)–(204), and inverting export demand (137) gives world trade $wt^{*}$ (205), given $\nu^{*}$, $\tilde{z}$, $\mu^{*}$ and $p_{X}^{c,*}$.

<!-- kind: eq; id: 189; section: C.2.6; page: 109; pdf_page: 115 -->
**(189) Output of the final consumption good**

$$
q^{C} = c
\tag{189}
$$

Meaning: Output of the final consumption good equals private consumption.

<!-- kind: eq; id: 190; section: C.2.6; page: 109; pdf_page: 115 -->
**(190) Output of the final investment good**

$$
q^{I} = i + \Delta inv \cdot y
\tag{190}
$$

Meaning: Output of the final investment good covers fixed investment plus inventory investment, the latter a fixed share of output.

<!-- kind: eq; id: 191; section: C.2.6; page: 109; pdf_page: 115 -->
**(191) Output of the final government-consumption good**

$$
q^{G} = g
\tag{191}
$$

Meaning: Output of the final government-consumption good equals government consumption.

<!-- kind: eq; id: 192; section: C.2.6; page: 109; pdf_page: 115 -->
**(192) Domestic intermediate goods used in the consumption sector**

$$
h^{C} = \nu_{C} \left(p_{H}\right)^{-\mu_{C}} q^{C}
\tag{192}
$$

Meaning: Consumption-sector demand for domestic intermediates: home-bias weight times the relative domestic price to the power minus the elasticity, times sector output.

<!-- kind: eq; id: 193; section: C.2.6; page: 109; pdf_page: 115 -->
**(193) Domestic intermediate goods used in the investment sector**

$$
h^{I} = \nu_{I} \left(\frac{p_{H}}{p_{I}}\right)^{-\mu_{I}} q^{I}
\tag{193}
$$

Meaning: Investment-sector demand for domestic intermediates, decreasing in their price relative to the investment-good price, proportional to investment-good output.

<!-- kind: eq; id: 194; section: C.2.6; page: 109; pdf_page: 115 -->
**(194) Domestic intermediate goods used in the government sector**

$$
h^{G} = \nu_{G} \left(\frac{p_{H}}{p_{G}}\right)^{-\mu_{G}} q^{G}
\tag{194}
$$

Meaning: Government-sector demand for domestic intermediates, decreasing in their price relative to the government-good price, proportional to that sector's output.

<!-- kind: eq; id: 195; section: C.2.6; page: 109; pdf_page: 115 -->
**(195) Imported intermediate goods used in the consumption sector**

$$
im^{C} = \left(1 - \nu_{C}\right) \left(p_{IM}\right)^{-\mu_{C}} q^{C}
\tag{195}
$$

Meaning: Consumption-sector demand for imports: one minus home bias, times the relative import price to the power minus the elasticity, times sector output.

<!-- kind: eq; id: 196; section: C.2.6; page: 109; pdf_page: 115 -->
**(196) Imported intermediate goods used in the investment sector**

$$
im^{I} = \left(1 - \nu_{I}\right) \left(\frac{p_{IM}}{p_{I}}\right)^{-\mu_{I}} q^{I}
\tag{196}
$$

Meaning: Investment-sector demand for imports, decreasing in the import price relative to the investment-good price, proportional to investment-good output.

<!-- kind: eq; id: 197; section: C.2.6; page: 109; pdf_page: 115 -->
**(197) Imported intermediate goods used in the government sector**

$$
im^{G} = \left(1 - \nu_{G}\right) \left(\frac{p_{IM}}{p_{G}}\right)^{-\mu_{G}} q^{G}
\tag{197}
$$

Meaning: Government-sector demand for imports, decreasing in the import price relative to the government-good price, proportional to that sector's output.

<!-- kind: inline; id: 197.i1; section: C.2.6; page: 110; pdf_page: 116 -->
**Inline 197.i1: Aggregation of domestic intermediate-goods demand across sectors**

$$
h = h_{C} + h_{I} + h_{G} + h_{X}
$$

Meaning: Total domestic intermediate demand is the sum of the four final-good sectors' uses; the paper says it holds in steady state but is not one of the 48 equations.

Note: the sector labels are printed as subscripts here ($h_{C}$, …), but as superscripts ($h^{C}$, …) in (192)–(199) (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: eq; id: 198; section: C.2.6; page: 110; pdf_page: 116 -->
**(198) Domestic intermediate goods used in the export sector (residual)**

$$
h^{X} = h - h^{C} - h^{I} - h^{G}
\tag{198}
$$

Meaning: Export-sector use of domestic intermediates is total domestic intermediate demand minus the consumption, investment and government sectors' uses.

<!-- kind: eq; id: 199; section: C.2.6; page: 110; pdf_page: 116 -->
**(199) Output of the final export good**

$$
q^{X} = \left(\nu_{X}\right)^{-1} \left(\frac{p_{H}}{p_{DX}}\right)^{\mu_{X}} h^{X}
\tag{199}
$$

Meaning: Final export-good output obtained by inverting the export sector's demand for domestic intermediates (127).

<!-- kind: eq; id: 200; section: C.2.6; page: 110; pdf_page: 116 -->
**(200) Imported intermediate goods used in the export sector**

$$
im^{X} = \left(1 - \nu_{X}\right) \left(\frac{p_{IM}}{p_{DX}}\right)^{-\mu_{G}} q^{X}
\tag{200}
$$

Meaning: Export-sector demand for imports: one minus export home bias, times the import price relative to the export-good price raised to the printed exponent, times export-good output.

Note: the exponent is printed $-\mu_{G}$ (as in (131)); by analogy with (195)–(197) and (199) the export elasticity $-\mu_{X}$ would be expected. Suspected typo, transcribed as printed (see [transcription notes](transcription-notes/T10.md)).

<!-- kind: eq; id: 201; section: C.2.6; page: 110; pdf_page: 116 -->
**(201) Total imports**

$$
im = im^{C} + im^{I} + im^{G} + im^{X}
\tag{201}
$$

Meaning: Total imports are the sum of imported intermediates used in the four final-good sectors (import-market clearing (147)).

<!-- kind: eq; id: 202; section: C.2.6; page: 110; pdf_page: 116 -->
**(202) Import share of GDP**

$$
s_{IM} = \frac{p_{IM} im}{p_{Y} y}
\tag{202}
$$

Meaning: The import share is the value of imports divided by nominal GDP.

<!-- kind: eq; id: 203; section: C.2.6; page: 110; pdf_page: 116 -->
**(203) Export share of GDP**

$$
s_{X} = s_{TB} + s_{IM}
\tag{203}
$$

Meaning: The export share of GDP equals the trade-balance share plus the import share.

<!-- kind: eq; id: 204; section: C.2.6; page: 110; pdf_page: 116 -->
**(204) Export volume**

$$
x = \frac{s_{X} y}{s \cdot p_{X}}
\tag{204}
$$

Meaning: Exports equal the export share times output, divided by the real exchange rate times the foreign-market export price.

<!-- kind: eq; id: 205; section: C.2.6; page: 110; pdf_page: 116 -->
**(205) World trade (scaled)**

$$
wt^{*} = \left(\nu^{*} \tilde{z}\right)^{-1} \left(p_{X}^{c,*}\right)^{-\mu^{*}} \left(p_{X}\right)^{\mu^{*}} x
\tag{205}
$$

Meaning: Scaled world trade backed out from the export-demand equation, given exports, the export price, competitors' price, the export weight and relative technology.

### C.2.7 Solving for government debt

**Summary.** Lump-sum taxes are zero in steady state by (139), which gives (206). The government budget constraint (138) is then solved for the debt-to-GDP ratio $s_{B}$ (207), taking as given the tax parameters $w_{\tau^{C}}$, $\tau^{C}$, $\tau^{N}$, $\tau^{W_{h}}$, $\tau^{W_{f}}$, $\tau^{K}$, $\tau^{D}$ and $s_{G}$, $s_{D}$, $\Pi$, $g_{z}$, and using the previously solved $c$, $w$, $N$, $r_{K}$, $p_{I}$, $k$, $p_{Y}$, $y$, $R$ and $s_{T}$.

<!-- kind: eq; id: 206; section: C.2.7; page: 110; pdf_page: 116 -->
**(206) Lump-sum taxes**

$$
s_{T} = 0
\tag{206}
$$

Meaning: The lump-sum tax share of GDP is zero in the steady state.

<!-- kind: eq; id: 207; section: C.2.7; page: 111; pdf_page: 117 -->
**(207) Government debt as a share of GDP**

$$
\begin{aligned}
s_{B} ={}& \left[w_{\tau^{C}} \tau^{C} \frac{c}{p_{Y} y} + \left(\tau^{N} + \tau^{W_{h}} + \tau^{W_{f}}\right) \frac{w N}{p_{Y} y}\right] \cdot \left[\left(\Pi g_{z}\right)^{-1} - R^{-1}\right]^{-1} \\
&+ \left[\frac{\tau^{K}}{g_{z}} \left(r_{K} - \delta p_{I}\right) \frac{k}{p_{Y} y} + \tau^{D} s_{D} + s_{T} - s_{G}\right] \cdot \left[\left(\Pi g_{z}\right)^{-1} - R^{-1}\right]^{-1}
\end{aligned}
\tag{207}
$$

Meaning: Debt-to-GDP equals tax revenues plus lump-sum taxes minus government consumption (all GDP shares), multiplied by the inverse of $(\Pi g_{z})^{-1} - R^{-1}$.

### C.2.8 Solving for fixed costs

**Summary.** The fixed costs, which were turned into unknowns, are backed out so that the profit shares equal their imposed values. Combining the total profit-share definition (157) with $y=h^{s}$ (155) gives $\psi$ (208), and the export profit-share definition (156) gives $\psi^{X}$ (209); the given inputs are $s_{D}$, $s_{DX}$ and $s$, together with the solved $p_{Y}$, $mc$, $y$, $p_{X}$, $p_{DX}$ and $x$.

<!-- kind: eq; id: 208; section: C.2.8; page: 111; pdf_page: 117 -->
**(208) Fixed cost of domestic intermediate-goods firms**

$$
\psi = \left[\left(1 - s_{D}\right) \frac{p_{Y}}{mc} - 1\right] y
\tag{208}
$$

Meaning: The domestic fixed cost is set so that the economy-wide profit share equals $s_{D}$, given output, the deflator and marginal cost.

<!-- kind: eq; id: 209; section: C.2.8; page: 111; pdf_page: 117 -->
**(209) Fixed cost of exporters**

$$
\psi^{X} = \left(\frac{s \cdot p_{X} p_{Y}}{p_{DX}} - 1\right) x - s_{DX} \frac{p_{Y} y}{p_{DX}}
\tag{209}
$$

Meaning: The exporters' fixed cost is set so that the export-sector profit share equals $s_{DX}$, given exports, export and domestic prices, and output.

### C.2.9 Solving for additional variables

**Summary.** The two remaining unknowns follow directly from earlier results. The consumption FOC (110) gives the normalized marginal utility of income $\lambda$ (210) from $c$ and the given $\kappa$, $g_{z}$, $w_{\tau^{C}}$, $\tau^{C}$, and the resource constraint at market prices (154), divided by $y$, gives the market-price output deflator $p_{Y}^{M}$ (211).

<!-- kind: eq; id: 210; section: C.2.9; page: 111; pdf_page: 117 -->
**(210) Marginal utility of income**

$$
\lambda = \frac{\left(1 - \kappa/g_{z}\right)^{-1}}{1 + w_{\tau^{C}} \tau^{C}} \frac{1}{c}
\tag{210}
$$

Meaning: The normalized marginal utility of income is inversely proportional to consumption, adjusted for habit persistence relative to trend growth and for VAT.

<!-- kind: eq; id: 211; section: C.2.9; page: 111; pdf_page: 117 -->
**(211) Output deflator at market prices**

$$
p_{Y}^{M} = \left(1 + w_{\tau^{C}} \tau^{C}\right) \frac{c}{y} + p_{I} \frac{i}{y} + \Delta inv \cdot p_{I} + p_{G} \frac{g}{y} + s_{TB} p_{Y}
\tag{211}
$$

Meaning: The market-price deflator sums VAT-inclusive consumption, investment, inventory investment and government consumption relative to output, plus the trade-balance term.
