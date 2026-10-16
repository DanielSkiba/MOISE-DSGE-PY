# The model (Section 3): firms

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

3.2 Firms: the production structure (Figure 1), domestic and foreign intermediate-goods firms, domestic final-goods firms, exporters and foreign retail firms. Equations (17)–(57).

## 3.2 Firms

**Summary.** The production side has five kinds of firms: domestic and foreign producers of differentiated intermediate goods (both monopolistically competitive), perfectly competitive domestic producers of four final goods, monopolistically competitive exporters who brand the homogeneous export good, and foreign retailers who bundle the branded goods into one exported good. All firms with market power reset prices only occasionally (Calvo), and their prices are sticky in the buyer's currency. The staged export chain lets exports contain imported inputs while export prices remain sticky in the destination currency. Figure 1 shows the flows between the firm types.

<!-- kind: inline; id: 16.i1; section: 3.2; page: 12; pdf_page: 18 -->
**(16.i1) Domestic differentiated intermediate goods and their index set**

$$
H_{f,t}, \text{ where } f \in \left[0,1\right]
$$

Meaning: Each domestic firm with market power, indexed by f on the unit interval, supplies its own variety of intermediate good.

<!-- kind: inline; id: 16.i2; section: 3.2; page: 12; pdf_page: 18 -->
**(16.i2) Imported differentiated intermediate goods and their index set**

$$
IM_{f^{*},t}, \text{ where } f^{*} \in \left[0,1\right]
$$

Meaning: Foreign firms with market power, indexed by f* on the unit interval, each supply one intermediate-good variety that the domestic economy buys from abroad.

<!-- kind: inline; id: 16.i3; section: 3.2; page: 12; pdf_page: 18 -->
**(16.i3) Final goods for consumption, investment, government consumption and export**

$$
Q_{t}^{C}, Q_{t}^{I}, Q_{t}^{G}, \text{ and } Q_{t}^{X}
$$

Meaning: Competitive final-goods producers turn domestic ($H_{f,t}$) and imported ($IM_{f^{*},t}$) intermediate varieties into consumption, investment, government-consumption and export goods.

<!-- kind: inline; id: 16.i4; section: 3.2; page: 12; pdf_page: 18 -->
**(16.i4) Differentiated (branded) export goods and their index set**

$$
X_{f^{X},t} \text{ where } f^{x} \in \left[0,1\right]
$$

Meaning: Exporters with market power purchase the homogeneous export good $Q_{t}^{X}$, attach a brand to it, and supply the branded varieties to foreign retailers.
Note: the subscript is printed with upper-case $f^{X}$ but the index set with lower-case $f^{x}$; Figure 1 prints $X_{f^{x},t}$. Transcribed as printed.

<!-- kind: inline; id: 16.i5; section: 3.2; page: 12; pdf_page: 18 -->
**(16.i5) Homogeneous exported good**

$$
X_{t}
$$

Meaning: Foreign retailers bundle all branded export varieties $X_{f^{X},t}$ into this one homogeneous good.

### Figure 1: The Structure of the Production Sector (page 13; pdf_page 19)

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

### 3.2.1 Domestic intermediate goods firms

**Summary.** A unit continuum of domestic firms produces with a Cobb-Douglas technology in rented capital services and a CES bundle of household-specific labor, subject to a transitory technology shock, a unit-root labor-augmenting productivity level whose growth rate is AR(1), and a fixed cost calibrated to give zero steady-state profits. The wage markup that governs substitutability between labor types follows a log-AR(1) process, the form shared by all markups in the model (footnote 11). Cost minimization gives household-specific labor demand, the aggregate wage index, total variable cost including the employer social security tax and a working-capital channel, the optimal capital-labor condition and a nominal marginal cost common to all firms. Prices are Calvo-sticky: firms that cannot reoptimize index to lagged domestic inflation and the inflation objective, reoptimizers all pick the same reset price, and together these give the law of motion of the domestic price index. Capital services are treated as homogeneous and traded in a competitive market, and firms are assumed symmetric (printed p.14).

<!-- kind: eq; id: 17; section: 3.2.1; page: 14; pdf_page: 20 -->
**(17) Production technology of domestic intermediate goods firms**

$$
H_{f,t}^{s} = \max\left[\varepsilon_{t}\left(K_{f,t}^{s}\right)^{\alpha}\left(z_{t} N_{f,t}\right)^{1-\alpha} - \psi z_{t}, 0\right]
\tag{17}
$$

Meaning: Firm f's output is Cobb-Douglas in capital services and productivity-augmented labor, scaled by the transitory technology shock, minus a fixed cost proportional to $z_{t}$, and never negative.

<!-- kind: inline; id: 17.i1; section: 3.2.1; page: 14; pdf_page: 20 -->
**(17.i1) Gross growth rate of labor-augmenting productivity**

$$
g_{z,t} \equiv z_{t}/z_{t-1}
$$

Meaning: Gross period-on-period growth of the unit-root productivity level $z_{t}$, whose trend all real variables share along the balanced growth path.

<!-- kind: eq; id: 18; section: 3.2.1; page: 14; pdf_page: 20 -->
**(18) AR(1) process for productivity growth**

$$
g_{z,t} = \left(1-\rho_{g_{z}}\right) g_{z} + \rho_{g_{z}} \cdot g_{z,t-1} + \eta_{t}^{g_{z}}
\tag{18}
$$

Meaning: Productivity growth reverts to its steady-state value $g_{z}$ with persistence $\rho_{g_{z}}$ and is hit by the innovation $\eta_{t}^{g_{z}}$.

<!-- kind: eq; id: 19; section: 3.2.1; page: 14; pdf_page: 20 -->
**(19) CES labor composite employed by firm f**

$$
N_{f,t} = \left(\int_{0}^{1}\left(N_{f,t}^{h}\right)^{\frac{1}{\varphi_{t}^{W}}} dh\right)^{\varphi_{t}^{W}}
\tag{19}
$$

Meaning: Firm f's labor input is a Dixit-Stiglitz aggregate of the labor services of all households h, with curvature set by the wage markup $\varphi_{t}^{W}$.

<!-- kind: inline; id: 19.i1; section: 3.2.1; page: 14; pdf_page: 20 -->
**(19.i1) Elasticity of substitution between labor types; markup restriction**

$$
\varphi_{t}^{W}/\left(\varphi_{t}^{W}-1\right) > 1, \text{ where } \varphi_{t}^{W} > 1
$$

Meaning: The exogenous substitution elasticity between labor varieties is $\varphi_{t}^{W}/(\varphi_{t}^{W}-1)$, above one; $\varphi_{t}^{W}>1$ is read as an exogenous wage markup shock.

<!-- kind: eq; id: 20; section: 3.2.1; page: 14; pdf_page: 20 -->
**(20) AR(1) process for the wage markup**

$$
\log\left(\varphi_{t}^{W}\right) = \left(1-\rho_{W}\right) \log\left(\varphi^{W}\right) + \rho_{W} \cdot \log\left(\varphi_{t-1}^{W}\right) + \eta_{t}^{W}
\tag{20}
$$

Meaning: The log wage markup reverts to its steady-state log value with persistence $\rho_{W}$ and innovation $\eta_{t}^{W}$; footnote 11 says every markup in the model follows this form.

<!-- kind: inline; id: 20.i1; section: 3.2.1; page: 14; pdf_page: 20 -->
**(20.i1) Fixed cost term of the production technology (17)**

$$
\psi z_{t}
$$

Meaning: The fixed cost in (17) grows with productivity; $\psi$ is calibrated so that steady-state profits are zero, matching the assumption of no firm entry or exit.

#### Resource allocation

<!-- kind: eq; id: 21; section: 3.2.1; page: 15; pdf_page: 21 -->
**(21) Firm f's demand for the labor of household h**

$$
N_{f,t}^{h} = \left(\frac{W_{h,t}}{W_{t}}\right)^{-\frac{\varphi_{t}^{W}}{\varphi_{t}^{W}-1}} N_{f,t}
\tag{21}
$$

Meaning: From cost minimization, demand for household h's labor falls with its wage relative to the aggregate wage and is proportional to the firm's total labor input.

<!-- kind: inline; id: 21.i1; section: 3.2.1; page: 15; pdf_page: 21 -->
**(21.i1) Definition of the aggregate wage index**

$$
W_{t} \equiv \frac{1}{N_{f,t}} \int_{0}^{1} W_{h,t} \cdot N_{f,t}^{h} \cdot dh
$$

Meaning: The aggregate wage is the wage bill over all household labor types divided by the firm's total labor input, i.e. a labor-weighted average wage.

<!-- kind: eq; id: 22; section: 3.2.1; page: 15; pdf_page: 21 -->
**(22) Aggregate wage index**

$$
W_{t} = \left(\int_{0}^{1}\left(W_{h,t}\right)^{\frac{1}{1-\varphi_{t}^{W}}} dh\right)^{1-\varphi_{t}^{W}}
\tag{22}
$$

Meaning: The aggregate wage index is a power mean of household wages whose exponent depends on the wage markup.

<!-- kind: eq; id: 23; section: 3.2.1; page: 15; pdf_page: 21 -->
**(23) Total variable production cost**

$$
TVC_{t} = R_{K,t} K_{f,t}^{S} + R_{t}^{F}\left(1+\tau_{t}^{W_{f}}\right) W_{t} N_{f,t}
\tag{23}
$$

Meaning: Variable cost is the rental bill for capital services plus the wage bill, grossed up by the employer social security tax rate and the working-capital factor $R_{t}^{F}$.
Note: capital services are printed $K_{f,t}^{S}$ (upper-case S) here and in (24), but $K_{f,t}^{s}$ (lower-case s) in (17) and the text. Transcribed as printed.

<!-- kind: inline; id: 23.i1; section: 3.2.1; page: 15; pdf_page: 21 -->
**(23.i1) Working-capital channel: effective interest factor on the wage bill**

$$
R_{t}^{F} = 1 + \nu^{F}\left(R_{t}-1\right)
$$

Meaning: Working-capital channel (after Adolfson et al., 2007): firms pre-finance the fraction $\nu^{F}$ of wages at the gross rate $R_{t}$, raising the effective cost of labor.

<!-- kind: eq; id: 24; section: 3.2.1; page: 15; pdf_page: 21 -->
**(24) Cost-minimizing allocation of capital and labor**

$$
\frac{R_{K,t}}{R_{t}^{F}\left(1+\tau_{t}^{W_{f}}\right) W_{t}} = \frac{\alpha}{\left(1-\alpha\right)} \frac{N_{f,t}}{K_{f,t}^{S}}
\tag{24}
$$

Meaning: The ratio of the capital rental rate to the effective cost of labor equals $\alpha/(1-\alpha)$ times the labor-to-capital ratio.
Note: printed $K_{f,t}^{S}$ (upper-case S), as in (23); (17) prints $K_{f,t}^{s}$. Transcribed as printed.

<!-- kind: eq; id: 25; section: 3.2.1; page: 15; pdf_page: 21 -->
**(25) Nominal marginal cost of domestic intermediate goods firms**

$$
MC_{t} = \frac{1}{\alpha^{\alpha}\left(1-\alpha\right)^{1-\alpha}} \frac{1}{\varepsilon_{t} z_{t}^{1-\alpha}} \left(R_{K,t}\right)^{\alpha}\left[R_{t}^{F}\left(1+\tau_{t}^{W_{f}}\right) W_{t}\right]^{1-\alpha}
\tag{25}
$$

Meaning: Marginal cost is the same for all firms: a Cobb-Douglas index of the capital rental rate and the effective labor cost, divided by technology $\varepsilon_{t} z_{t}^{1-\alpha}$.

#### Price setting

<!-- kind: eq; id: 26; section: 3.2.1; page: 16; pdf_page: 22 -->
**(26) Price indexation of domestic firms that do not reoptimize**

$$
P_{H,f,t} = \Pi_{H,t-1}^{\chi_{H}} \bar{\Pi}_{t}^{1-\chi_{H}} P_{H,f,t-1}
\tag{26}
$$

Meaning: With probability $\xi_{H}$ a firm gets no reoptimization signal and raises its price by lagged domestic inflation (weight $\chi_{H}$) and the current inflation objective (weight $1-\chi_{H}$).
Note: the bar over $\Pi$ is printed full-width in this chunk; written $\bar{\Pi}$ (single-letter accent, CONVENTIONS 4.5).

<!-- kind: inline; id: 26.i1; section: 3.2.1; page: 16; pdf_page: 22 -->
**(26.i1) Gross inflation of domestic intermediate goods prices**

$$
\Pi_{H,t} \equiv P_{H,t}/P_{H,t-1}
$$

Meaning: Gross domestic-goods inflation is the current over the lagged domestic price index; the same sentence names $\bar{\Pi}_{t}$ the gross time-varying inflation objective.

<!-- kind: eq; id: 27; section: 3.2.1; page: 16; pdf_page: 22 -->
**(27) Objective of a reoptimizing domestic firm**

$$
\max E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t+k} \xi_{H}^{k}\left(P_{H,f,t+k} H_{f,t+k} - MC_{t+k} H_{f,t+k}\right)\right]
\tag{27}
$$

Meaning: A reoptimizing firm maximizes expected discounted gross profits, weighting period t+k by the discount factor and by the probability $\xi_{H}^{k}$ that its price is still in force.

<!-- kind: inline; id: 27.i1; section: 3.2.1; page: 16; pdf_page: 22 -->
**(27.i1) Discount factor used by firms**

$$
\Lambda_{t,t+k} \equiv \beta^{k} E_{t}\left[\frac{\Lambda_{h,t+k}}{\Lambda_{h,t}} \frac{P_{C,t}}{P_{C,t+k}}\right]
$$

Meaning: Discounts period-t+k profits by $\beta^{k}$ times the expected marginal-utility ratio adjusted for CPI growth; (27) also multiplies by $\xi_{H}^{k}$, the probability of no reoptimization for k periods.

<!-- kind: inline; id: 27.i2; section: 3.2.1; page: 16; pdf_page: 22 -->
**(27.i2) Total variable cost of firm f in period t**

$$
MC_{t} H_{f,t}
$$

Meaning: Because marginal cost is independent of how much the firm produces, its period-t variable cost equals marginal cost times output.

<!-- kind: eq; id: 28; section: 3.2.1; page: 16; pdf_page: 22 -->
**(28) Optimality condition for the reset price of domestic firms**

$$
E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t+k} \xi_{H}^{k}\left(\Pi_{H,t,t+k}^{\dagger} \tilde{P}_{H,t} - \varphi_{t+k}^{H} MC_{t+k}\right) H_{f,t+k}\right] = 0
\tag{28}
$$

Meaning: Given indexation (26) and demand (39), all reoptimizers choose the same price $\tilde{P}_{H,t}$, setting the expected discounted gap between indexed price and markup times marginal cost to zero.
Note: the tilde over $P$ is printed wide; written $\tilde{P}$ (single-letter accent).

<!-- kind: inline; id: 28.i1; section: 3.2.1; page: 16; pdf_page: 22 -->
**(28.i1) Cumulative indexation factor for domestic prices**

$$
\Pi_{H,t,t+k}^{\dagger} \equiv \prod_{s=1}^{k}\left(\Pi_{H,t+s-1}^{\chi_{H}} \bar{\Pi}_{t+s}^{1-\chi_{H}}\right) \text{ for } k \geq 1 \text{ and } \Pi_{H,t,t+k}^{\dagger} \equiv 1 \text{ for } k = 0
$$

Meaning: The total price increase from indexation over k periods without reoptimization: a product of lagged-inflation and objective terms, equal to one when k is zero.

<!-- kind: eq; id: 29; section: 3.2.1; page: 16; pdf_page: 22 -->
**(29) Law of motion of the domestic intermediate goods price index**

$$
P_{H,t} = \left[\left(1-\xi_{H}\right)\left(\tilde{P}_{H,t}\right)^{\frac{1}{1-\varphi_{t}^{H}}} + \xi_{H}\left(\Pi_{H,t-1}^{\chi_{H}} \bar{\Pi}_{H,t}^{1-\chi_{H}} P_{H,t-1}\right)^{\frac{1}{1-\varphi_{t}^{H}}}\right]^{1-\varphi_{t}^{H}}
\tag{29}
$$

Meaning: Via the price index (41) and averaging over firms, the domestic price index mixes reset prices (weight $1-\xi_{H}$) and indexed lagged prices (weight $\xi_{H}$).
Note: the objective term is printed $\bar{\Pi}_{H,t}$ (subscript H), whereas (26) and 28.i1 print $\bar{\Pi}_{t}$; suspected typo, transcribed as printed.

### 3.2.2 Foreign intermediate goods firms

**Summary.** A unit continuum of foreign firms ($f^{*} \in [0,1]$) sells differentiated intermediate goods $IM_{f^{*},t}$ to domestic final-goods producers and sets prices in the importing (consumer) currency. Their nominal marginal cost is a weighted mix, with the oil share as weight, of the lagged global oil price and the global price of foreign intermediate goods, converted at the nominal effective exchange rate. Pricing mirrors the domestic case: Calvo signals, indexation to lagged import-price inflation and the inflation objective, a common reset price chosen to maximize discounted profits measured in foreign currency, and a law of motion for the aggregate import price.

<!-- kind: eq; id: 30; section: 3.2.2; page: 17; pdf_page: 23 -->
**(30) Nominal marginal cost of foreign intermediate goods firms**

$$
MC_{t}^{*} = S_{t}\left(\bar{\Pi}_{Y}^{*} P_{OIL,t-1}^{*}\right)^{\omega^{*}}\left(P_{Y,t}^{*}\right)^{1-\omega^{*}}
\tag{30}
$$

Meaning: Import marginal cost is the exchange rate times a geometric mix of the lagged oil price (scaled by steady-state foreign inflation) and the foreign goods price, with oil share $\omega^{*}$.
Note: all variables except $S_{t}$ are in producer (foreign) currency. Footnote 12: unlike Christoffel et al. (2008), the oil price affects import costs with a one-period delay.

<!-- kind: eq; id: 31; section: 3.2.2; page: 17; pdf_page: 23 -->
**(31) Price indexation of import firms that do not reoptimize**

$$
P_{IM,f^{*},t} = \Pi_{IM,t-1}^{\chi^{*}} \bar{\Pi}_{t}^{1-\chi^{*}} P_{IM,f^{*},t-1}
\tag{31}
$$

Meaning: With probability $\xi^{*}$ an import firm cannot reoptimize and raises its consumer-currency price by lagged import inflation (weight $\chi^{*}$) and the current inflation objective.

<!-- kind: inline; id: 31.i1; section: 3.2.2; page: 17; pdf_page: 23 -->
**(31.i1) Gross import price inflation**

$$
\Pi_{IM,t} \equiv P_{IM,t}/P_{IM,t-1}
$$

Meaning: Gross inflation of aggregate imported-goods prices, the ratio of the current to the lagged import price index.

<!-- kind: eq; id: 32; section: 3.2.2; page: 17; pdf_page: 23 -->
**(32) Objective of a reoptimizing import firm**

$$
\max E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t+k}^{*}\left(\xi^{*}\right)^{k}\left(P_{IM,f^{*},t} IM_{f^{*},t} - MC_{t}^{*} IM_{f^{*},t}\right)/S_{t}\right]
\tag{32}
$$

Meaning: A reoptimizing import firm maximizes expected discounted profits, converted to foreign currency by dividing by the exchange rate, over the periods its price stays in force.
Note: inside the sum every time subscript is printed $t$ ($P_{IM,f^{*},t}$, $IM_{f^{*},t}$, $MC_{t}^{*}$, $S_{t}$), not $t+k$ as in (27) and (33); suspected typo, transcribed as printed. (32) is printed only once.

<!-- kind: inline; id: 32.i1; section: 3.2.2; page: 17; pdf_page: 23 -->
**(32.i1) Foreign discount factor and non-reoptimization probability**

$$
\Lambda_{t,t+k}^{*} \text{ and } \left(\xi^{*}\right)^{k}
$$

Meaning: These are the foreign analogues of $\Lambda_{t,t+k}$ and $\xi_{H}^{k}$ in (27); this section gives no separate formula for $\Lambda_{t,t+k}^{*}$.

<!-- kind: eq; id: 33; section: 3.2.2; page: 18; pdf_page: 24 -->
**(33) Optimality condition for the reset price of import firms**

$$
E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t+k}^{*}\left(\xi^{*}\right)^{k}\left(\Pi_{IM,t,t+k}^{\dagger} \tilde{P}_{IM,t} - \varphi_{t+k}^{*} MC_{t+k}^{*}\right) IM_{f^{*},t+k}/S_{t+k}\right] = 0
\tag{33}
$$

Meaning: Given indexation (31) and demand (40), all reoptimizers pick the same price $\tilde{P}_{IM,t}$, zeroing the expected discounted, exchange-rate-converted gap between indexed price and markup times marginal cost.

<!-- kind: inline; id: 33.i1; section: 3.2.2; page: 18; pdf_page: 24 -->
**(33.i1) Cumulative indexation factor for import prices**

$$
\Pi_{IM,t,t+k}^{\dagger} \equiv \prod_{s=1}^{k}\left(\Pi_{IM,t+s-1}^{\chi^{*}} \bar{\Pi}_{t+s}^{1-\chi^{*}}\right) \text{ for } k \geq 1 \text{ and } \Pi_{IM,t,t+k}^{\dagger} \equiv 1 \text{ for } k = 0
$$

Meaning: Total indexation of import prices over k periods without reoptimization, equal to one for k zero; the same sentence names $\varphi_{t}^{*}$ the foreign firms' optimal markup.

<!-- kind: eq; id: 34; section: 3.2.2; page: 18; pdf_page: 24 -->
**(34) Law of motion of the aggregate import price index**

$$
P_{IM,t} = \left[\left(1-\xi^{*}\right)\left(\tilde{P}_{IM,t}\right)^{\frac{1}{1-\varphi_{t}^{*}}} + \xi^{*}\left(\Pi_{IM,t-1}^{\chi^{*}} \bar{\Pi}_{IM,t}^{1-\chi^{*}} P_{IM,t-1}\right)^{\frac{1}{1-\varphi_{t}^{*}}}\right]^{1-\varphi_{t}^{*}}
\tag{34}
$$

Meaning: The import price index combines new reset prices (share $1-\xi^{*}$) and indexed lagged prices (share $\xi^{*}$), with an exponent set by the foreign markup.
Note: the objective term is printed $\bar{\Pi}_{IM,t}$ (subscript IM), whereas (31) and 33.i1 print $\bar{\Pi}_{t}$; suspected typo, transcribed as printed.

### 3.2.3 Domestic final goods firms

**Summary.** Final goods are made by four perfectly competitive sectors: consumption ($Q_{t}^{C}$), investment ($Q_{t}^{I}$), government consumption ($Q_{t}^{G}$) and exported goods ($Q_{t}^{X}$). The text works through the consumption sector; the others reuse the same equations with the index changed. Each producer mixes a bundle of domestic intermediate goods with a bundle of imported ones in a CES technology. That technology has a time-varying home-bias weight and an adjustment cost on changes in import intensity. From it the subsection derives demand within each bundle and the bundle price indices (CES with time-varying markups), demand between the two bundles, and a final-good price equal to marginal cost.

#### Technology

**Summary.** States the CES production function of the final consumption good and the two CES bundles of intermediate goods it uses. It also introduces the quadratic cost of changing import intensity.

<!-- kind: eq; id: 35; section: 3.2.3; page: 18; pdf_page: 24 -->
**(35) Production function of the final consumption good (CES of domestic and imported bundles)**

$$
Q_{t}^{C} = \left(\nu_{C,t}^{\frac{1}{\mu_{C}}} \left[H_{t}^{C}\right]^{1-\frac{1}{\mu_{C}}} + \left(1-\nu_{C,t}\right)^{\frac{1}{\mu_{C}}} \left\{\left[1-\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right)\right] IM_{t}^{C}\right\}^{1-\frac{1}{\mu_{C}}}\right)^{\frac{\mu_{C}}{\mu_{C-1}}}
\tag{35}
$$

Meaning: Consumption-good output is a CES combination of the domestic bundle and the imported bundle net of adjustment costs, with home-bias weight $\nu_{C,t}$ and substitution elasticity $\mu_{C}$.

Note: In the outer exponent the denominator is printed with "C−1" entirely as the subscript of μ ($\mu_{C-1}$), not as $\mu_{C}-1$. This was confirmed from the glyph baselines and is transcribed as printed; see [transcription notes](transcription-notes/T03.md).

<!-- kind: inline; id: 35.i1; section: 3.2.3; page: 19; pdf_page: 25 -->
**(35.i1) Steady-state import intensity of the consumption sector**

$$
1-\nu_{C}
$$

Meaning: In steady state, the share of imports in $Q_{t}^{C}$ production equals one minus the home-bias weight. Footnote 15: the home-bias weights follow AR(1) processes like (20).

<!-- kind: eq; id: 36; section: 3.2.3; page: 19; pdf_page: 25 -->
**(36) Bundle of domestically produced intermediate goods**

$$
H_{t}^{C} = \left(\int_{0}^{1} \left(H_{f,t}^{C}\right)^{\frac{1}{\varphi_{t}^{H}}} df\right)^{\varphi_{t}^{H}}
\tag{36}
$$

Meaning: The domestic bundle aggregates the continuum of domestic intermediate goods $f$ with a CES aggregator governed by the time-varying markup $\varphi_{t}^{H}$.

<!-- kind: eq; id: 37; section: 3.2.3; page: 19; pdf_page: 25 -->
**(37) Bundle of imported intermediate goods**

$$
IM_{t}^{C} = \left(\int_{0}^{1} \left(IM_{f^{*},t}^{C}\right)^{\frac{1}{\varphi_{t}^{*}}} df^{*}\right)^{\varphi_{t}^{*}}
\tag{37}
$$

Meaning: The imported bundle aggregates the continuum of foreign intermediate goods $f^{*}$ with a CES aggregator governed by the time-varying markup $\varphi_{t}^{*}$.

<!-- kind: inline; id: 37.i1; section: 3.2.3; page: 19; pdf_page: 25 -->
**(37.i1) Import intensity in production**

$$
\left(IM_{t}^{C}/Q_{t}^{C}\right)
$$

Meaning: Import intensity is the imported bundle per unit of consumption-good output; changing it is costly.

<!-- kind: eq; id: 38; section: 3.2.3; page: 19; pdf_page: 25 -->
**(38) Adjustment cost of changing import intensity**

$$
\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right) = \frac{\gamma_{IM^{C}}}{2}\left[\left(\varepsilon_{t}^{IM}\right)^{-\frac{1}{\gamma_{IM^{C}}}} \frac{IM_{t}^{C}/Q_{t}^{C}}{IM_{t-1}^{C}/Q_{t-1}^{C}} - 1\right]^{2}
\tag{38}
$$

Meaning: A quadratic cost in the growth of import intensity, scaled by $\gamma_{IM^{C}}$ and shifted by the import-demand shock $\varepsilon_{t}^{IM}$, which acts on imported-input productivity.

<!-- kind: inline; id: 38.i1; section: 3.2.3; page: 19; pdf_page: 25 -->
**(38.i1) Footnote 16: lagged import intensity is the aggregate one**

$$
IM_{t-1}^{C}/Q_{t-1}^{C}
$$

Meaning: In (38) the previous-period import intensity is the economy-wide aggregate, which the individual firm takes as given.

<!-- kind: inline; id: 38.i2; section: 3.2.3; page: 19; pdf_page: 25 -->
**(38.i2) Footnote 16: current import intensity is the firm's choice**

$$
IM_{t}^{C}/Q_{t}^{C}
$$

Meaning: The current-period import intensity in (38) is chosen by the individual firm. The firm therefore ignores how today's intensity affects future import productivity.

#### Resource allocation and price setting

**Summary.** Derives the cost-minimizing demands within each bundle and the matching price indices, then the demands for the two bundles. Marginal-cost pricing then gives the final-good price.

<!-- kind: eq; id: 39; section: 3.2.3; page: 19; pdf_page: 25 -->
**(39) Demand for domestic intermediate good f**

$$
H_{f,t}^{C} = \left(\frac{P_{H,f,t}}{P_{H,t}}\right)^{-\frac{\varphi_{t}^{H}}{\varphi_{t}^{H}-1}} H_{t}^{C}
\tag{39}
$$

Meaning: Demand for variety $f$ is proportional to the domestic bundle. It falls with the variety's price relative to the domestic price index, with exponent $-\varphi_{t}^{H}/(\varphi_{t}^{H}-1)$.

<!-- kind: eq; id: 40; section: 3.2.3; page: 20; pdf_page: 26 -->
**(40) Demand for an imported intermediate variety**

$$
IM_{f^{*},t}^{C} = \left(\frac{P_{IM,f^{*},t}}{P_{IM,t}}\right)^{-\frac{\varphi_{t}^{*}}{\varphi_{t}^{*}-1}} IM_{t}^{C}
\tag{40}
$$

Meaning: Demand for imported variety $f^{*}$ is proportional to the imported bundle. It falls with the variety's price relative to the import price index, with exponent $-\varphi_{t}^{*}/(\varphi_{t}^{*}-1)$.

<!-- kind: inline; id: 40.i1; section: 3.2.3; page: 20; pdf_page: 26 -->
**(40.i1) Definition of the domestic intermediate-goods price index**

$$
P_{H,t} H_{t}^{C} = \int_{0}^{1} P_{H,f,t} \cdot H_{f,t}^{C} \cdot df
$$

Meaning: $P_{H,t}$ is the unit cost of the domestic bundle, so spending on the bundle equals total spending on its varieties.

<!-- kind: inline; id: 40.i2; section: 3.2.3; page: 20; pdf_page: 26 -->
**(40.i2) Definition of the import price index**

$$
P_{IM,t} IM_{t}^{C} = \int_{0}^{1} P_{IM,f^{*},t} \cdot IM_{f^{*},t}^{C} \cdot df^{*}
$$

Meaning: $P_{IM,t}$ is the unit cost of the imported bundle, so spending on the bundle equals total spending on imported varieties.

<!-- kind: eq; id: 41; section: 3.2.3; page: 20; pdf_page: 26 -->
**(41) Price index of domestic intermediate goods**

$$
P_{H,t} = \left(\int_{0}^{1} \left(P_{H,f,t}\right)^{\frac{1}{1-\varphi_{t}^{H}}} df\right)^{1-\varphi_{t}^{H}}
\tag{41}
$$

Meaning: Substituting (39) into the spending identity gives the domestic price index as a CES aggregate of variety prices, with exponents set by $\varphi_{t}^{H}$.

<!-- kind: eq; id: 42; section: 3.2.3; page: 20; pdf_page: 26 -->
**(42) Import price index**

$$
P_{IM,t} = \left(\int_{0}^{1} \left(P_{IM,f^{*},t}\right)^{\frac{1}{1-\varphi_{t}^{*}}} df^{*}\right)^{1-\varphi_{t}^{*}}
\tag{42}
$$

Meaning: Substituting (40) into the spending identity gives the import price index as a CES aggregate of imported variety prices, with exponents set by $\varphi_{t}^{*}$.

<!-- kind: eq; id: 43; section: 3.2.3; page: 20; pdf_page: 26 -->
**(43) Demand for the domestic bundle**

$$
H_{t}^{C} = \nu_{C,t}\left(\frac{P_{H,t}}{P_{C,t}}\right)^{-\mu_{C}} Q_{t}^{C}
\tag{43}
$$

Meaning: Demand for the domestic bundle is output times the home-bias weight $\nu_{C,t}$ times $(P_{H,t}/P_{C,t})^{-\mu_{C}}$. It falls with the domestic price relative to the consumption-good price, with elasticity $\mu_{C}$.

<!-- kind: eq; id: 44; section: 3.2.3; page: 20; pdf_page: 26 -->
**(44) Demand for the imported bundle**

$$
IM_{t}^{C} = \left(1-\nu_{C,t}\right)\left(\frac{P_{IM,t}}{P_{C,t} \Gamma_{IM^{C}}^{\dagger}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right)}\right)^{-\mu_{C}} \frac{Q_{t}^{C}}{1-\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right)}
\tag{44}
$$

Meaning: Import demand rises with output, grossed up for adjustment costs. It falls with the import price relative to $P_{C,t}$ times $\Gamma^{\dagger}$, with elasticity $\mu_{C}$.

<!-- kind: inline; id: 44.i1; section: 3.2.3; page: 20; pdf_page: 26 -->
**(44.i1) Definition of the auxiliary function Γ† for imports**

$$
\Gamma_{IM^{C}}^{\dagger}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right) = 1-\Gamma_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right)-\Gamma'_{IM^{C}}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right) IM_{t}^{C}
$$

Meaning: $\Gamma^{\dagger}$ is one minus the adjustment cost, minus the cost function's derivative multiplied by $IM_{t}^{C}$.

Note: The derivative term is multiplied by the level $IM_{t}^{C}$, not by the ratio $IM_{t}^{C}/Q_{t}^{C}$, as printed. The paper does not say what $\Gamma'$ is the derivative with respect to; see [transcription notes](transcription-notes/T03.md).

<!-- kind: eq; id: 45; section: 3.2.3; page: 21; pdf_page: 27 -->
**(45) Price of the final consumption good (equal to marginal cost)**

$$
P_{C,t} = \left\{\nu_{C,t}\left[P_{H,t}\right]^{1-\mu_{C}} + \left(1-\nu_{C,t}\right)\left(\frac{P_{IM,t}}{\Gamma_{IM^{C}}^{\dagger}\left(IM_{t}^{C}/Q_{t}^{C};\varepsilon_{t}^{IM}\right)}\right)^{1-\mu_{C}}\right\}^{\frac{1}{1-\mu_{C}}}
\tag{45}
$$

Meaning: With perfect competition the consumption-good price equals marginal cost: a CES index of $P_{H,t}$ and the import price over $\Gamma^{\dagger}$, weighted by $\nu_{C,t}$ and $1-\nu_{C,t}$.

#### Generalization to other production categories

**Summary.** Equations (35)–(45) hold for the investment, government-consumption and export sectors with the index C replaced by I, G or X. The one exception is notation: the price of exported final goods is written $P_{DX,t}$.

<!-- kind: inline; id: 45.i1; section: 3.2.3; page: 21; pdf_page: 27 -->
**(45.i1) Notation for the price of exported final goods**

$$
P_{DX,t}
$$

Meaning: $P_{DX,t}$ is the price of exported final goods $Q_{t}^{X}$, playing the role of $P_{C,t}$ for sector X; $P_{X,t}$ is reserved for exporters' foreign-currency price.

### 3.2.4 Exporters

**Summary.** Final-good firms are competitive and intermediate firms make domestic prices sticky. To make export prices sticky in foreign currency as well, the paper adds a monopolistically competitive layer of exporters. Each exporter buys the homogeneous export good, brand-names it one-for-one less a fixed cost, and sets a foreign-currency price under Calvo rigidity. Prices that are not reoptimized are indexed to past export inflation and to the foreign inflation objective. The subsection gives the indexation rule, the exporter's problem, its marginal cost (the price of the exported final good), the optimal-price condition, and the law of motion of the aggregate export price.

<!-- kind: inline; id: 45.i2; section: 3.2.4; page: 21; pdf_page: 27 -->
**(45.i2) Index set of exporters**

$$
f^{x} \in \left[0,1\right]
$$

Meaning: Exporters form a unit continuum, indexed by $f^{x}$.

Note: Printed with a lowercase superscript x here and in some text mentions; elsewhere the paper writes the same index as $f^{X}$.

<!-- kind: eq; id: 46; section: 3.2.4; page: 21; pdf_page: 27 -->
**(46) Exporter's brand-naming production function**

$$
X_{f^{X},t} = Q_{f^{X},t}^{X} - \psi^{X} z_{t}
\tag{46}
$$

Meaning: Exporter $f^{X}$ turns purchased homogeneous export goods one-for-one into its differentiated good, net of a fixed cost proportional to productivity $z_{t}$.

<!-- kind: inline; id: 46.i1; section: 3.2.4; page: 22; pdf_page: 28 -->
**(46.i1) Fixed cost of brand naming**

$$
\psi^{X} z_{t}
$$

Meaning: Brand naming has a fixed cost: the parameter $\psi^{X}$ times labor-augmenting productivity $z_{t}$, as for domestic intermediate producers.

<!-- kind: eq; id: 47; section: 3.2.4; page: 22; pdf_page: 28 -->
**(47) Indexation of the export price when not reoptimized**

$$
P_{X,f^{X},t} = \left(\Pi_{X,t-1}\right)^{\chi_{X}} \left(\bar{\Pi}_{t}^{*}\right)^{\left(1-\chi_{X}\right)} P_{X,f^{X},t-1}
\tag{47}
$$

Meaning: With probability $\xi_{X}$ an exporter keeps its price, updated by past export inflation (weight $\chi_{X}$) and the foreign inflation objective (weight $1-\chi_{X}$).

Note: The paper typesets the bar as a full-width overline over Π; it is transcribed as `\bar{\Pi}` per the conventions.

<!-- kind: inline; id: 47.i1; section: 3.2.4; page: 22; pdf_page: 28 -->
**(47.i1) Export-price inflation in foreign currency**

$$
\Pi_{X,t} \equiv P_{X,t}/P_{X,t-1}
$$

Meaning: Gross inflation of the aggregate foreign-currency export price. The same sentence says $\bar{\Pi}_{t}^{*}$ is the foreign inflation target in gross terms, which may vary over time.

<!-- kind: eq; id: 48; section: 3.2.4; page: 22; pdf_page: 28 -->
**(48) Exporter's price-setting problem**

$$
\max E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t-1} \xi_{X}^{k} \left(S_{t} P_{X,f^{X},t} X_{f^{X},t} - MC_{t}^{X} X_{f^{X},t}\right)\right]
\tag{48}
$$

Meaning: A reoptimizing exporter maximizes expected discounted dividends. Each period's dividend is the export price converted to domestic currency at $S_{t}$, minus marginal cost, times the quantity $X_{f^{X},t}$. Discounting uses $\Lambda$ and the Calvo non-reset probability $\xi_{X}^{k}$.

Note: As printed, the discount factor is $\Lambda_{t,t-1}$ and every term inside the sum is dated t, although the sum runs over k. The domestic analogue (27) uses $\Lambda_{t,t+k}$ and t+k dating; see [transcription notes](transcription-notes/T03.md).

<!-- kind: eq; id: 49; section: 3.2.4; page: 22; pdf_page: 28 -->
**(49) Exporters' nominal marginal cost**

$$
MC_{t}^{X} = P_{DX,t}
\tag{49}
$$

Meaning: Exporters' marginal cost, measured nominally and in domestic currency, is simply the price they pay for the homogeneous exported final good.

<!-- kind: eq; id: 50; section: 3.2.4; page: 22; pdf_page: 28 -->
**(50) Optimality condition for the reoptimized export price**

$$
E_{t}\left[\sum_{k=0}^{\infty} \Lambda_{t,t+1} \xi_{X}^{k} \left(\Pi_{X,t,t+k}^{\dagger} \tilde{P}_{X,t} - \varphi_{t+k}^{X} S_{t}^{-1} MC_{t+k}^{X}\right) X_{f^{X},t+k}\right] = 0
\tag{50}
$$

Meaning: The common optimal foreign-currency price $\tilde{P}_{X,t}$ sets to zero the expected discounted, demand-weighted gap between the indexed new price and marked-up marginal cost in foreign currency.

Note: As printed, the discount factor is $\Lambda_{t,t+1}$ and the exchange-rate term is $S_{t}^{-1}$, dated t. The domestic analogue (28) has $\Lambda_{t,t+k}$, and the import analogue (33) divides by $S_{t+k}$. The paper typesets $\tilde{P}$; it is transcribed as `\tilde{P}`.

<!-- kind: inline; id: 50.i1; section: 3.2.4; page: 22; pdf_page: 28 -->
**(50.i1) Cumulative indexation factor of export prices, k ≥ 1**

$$
\Pi_{X,t,t+k}^{\dagger} \equiv \prod_{s=1}^{k}\left[\left(\Pi_{X,t+s-1}^{\chi_{X}}\right)^{\chi_{X}}\left(\bar{\Pi}_{X,t+s}^{*}\right)^{1-\chi_{X}}\right] \text{ for } k \ge 1
$$

Meaning: The factor by which a non-reoptimized export price grows from t to t+k under scheme (47). It is a product of past export-inflation and foreign-objective terms.

Note: As printed, $\chi_{X}$ appears twice, as the superscript of Π inside the parentheses and again as the outer exponent; the analogues (28) and (33) have a single exponent. The objective is printed with subscript X here ($\bar{\Pi}_{X,t+s}^{*}$) but without it in (47); see [transcription notes](transcription-notes/T03.md).

<!-- kind: inline; id: 50.i2; section: 3.2.4; page: 22; pdf_page: 28 -->
**(50.i2) Cumulative indexation factor, boundary case (as printed)**

$$
\Pi_{X,t,t+k}^{\dagger} \equiv 1 \text{ for } k = 1
$$

Meaning: Boundary case of the cumulative indexation factor, which the paper prints as holding for k = 1. In the same passage $\varphi_{t}^{X}$ is named an optimal price-markup shock.

Note: Printed "k = 1", which contradicts the k ≥ 1 case in 50.i1; the analogous definitions after (28) and (33) use k = 0.

<!-- kind: eq; id: 51; section: 3.2.4; page: 23; pdf_page: 29 -->
**(51) Law of motion of the aggregate export price**

$$
P_{X,t} = \left[\left(1-\xi_{X}\right)\left(\tilde{P}_{X,t}\right)^{\frac{1}{1-\varphi_{t}^{X}}} + \xi_{X}\left(\left(\Pi_{X,t-1}\right)^{\chi_{X}}\left(\bar{\Pi}_{X,t}^{*}\right)^{1-\chi_{X}} P_{X,t-1}\right)^{\frac{1}{1-\varphi_{t}^{X}}}\right]^{1-\varphi_{t}^{X}}
\tag{51}
$$

Meaning: The aggregate export price is a Calvo-weighted CES combination of the new optimal price and last period's aggregate price after indexation.

Note: The foreign inflation objective is printed with subscript X here ($\bar{\Pi}_{X,t}^{*}$) but as $\bar{\Pi}_{t}^{*}$ in (47).

### 3.2.5 Foreign retail firms

**Summary.** Competitive foreign retailers buy the differentiated export goods and combine them, CES fashion, into one homogeneous export good. That yields standard Dixit–Stiglitz demands and an export price index, and retailers sell at marginal cost $P_{X,t}$. The homogeneous export good is then one input into a CES index of total world trade. Demand for Israeli exports therefore depends on their price relative to world-trade prices, on world trade, on a country-specific demand shock, and on an adjustment cost of changing exports' share of world trade.

<!-- kind: inline; id: 51.i1; section: 3.2.5; page: 23; pdf_page: 29 -->
**(51.i1) Index set of differentiated export goods**

$$
f^{X} \in \left[0,1\right]
$$

Meaning: Retailers buy the differentiated export goods $X_{f^{X},t}$ of a unit continuum of exporters indexed by $f^{X}$.

<!-- kind: eq; id: 52; section: 3.2.5; page: 23; pdf_page: 29 -->
**(52) Homogeneous export good as a CES aggregate of differentiated export goods**

$$
X_{t} = \left(\int_{0}^{1} \left(X_{f^{X},t}\right)^{\frac{1}{\varphi_{t}^{X}}} df^{X}\right)^{\varphi_{t}^{X}}
\tag{52}
$$

Meaning: Foreign retailers aggregate the differentiated export goods into the homogeneous export good with a CES aggregator governed by $\varphi_{t}^{X}$.

<!-- kind: eq; id: 53; section: 3.2.5; page: 23; pdf_page: 29 -->
**(53) Demand for differentiated export good f^X**

$$
X_{f^{X},t} = \left(\frac{P_{X,f^{X},t}}{P_{X,t}}\right)^{-\frac{\varphi_{t}^{X}}{\varphi_{t}^{X}-1}} X_{t}
\tag{53}
$$

Meaning: Dixit–Stiglitz demand. The demand for exporter $f^{X}$'s good is proportional to total exports and falls with its price relative to the export price index.

<!-- kind: eq; id: 54; section: 3.2.5; page: 23; pdf_page: 29 -->
**(54) Aggregate export price index**

$$
P_{X,t} = \left(\int_{0}^{1} \left(P_{X,f^{X},t}\right)^{\frac{1}{1-\varphi_{t}^{X}}} df^{X}\right)^{1-\varphi_{t}^{X}}
\tag{54}
$$

Meaning: The foreign-currency export price index is a CES aggregate of individual exporters' prices; competitive retailers also sell at this price, since it is their marginal cost.

<!-- kind: eq; id: 55; section: 3.2.5; page: 23; pdf_page: 29 -->
**(55) Demand for Israeli exports**

$$
X_{t} = \nu_{t}^{*}\left(\frac{P_{X,t}}{P_{X,t}^{c,*} \Gamma_{X}^{\dagger}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right)}\right)^{-\mu^{*}} \frac{WT_{t}^{*}}{1-\Gamma_{X}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right)}
\tag{55}
$$

Meaning: Exports scale with world trade grossed up for adjustment costs, fall with their price relative to world-trade prices times $\Gamma_{X}^{\dagger}$ (elasticity $\mu^{*}$), and shift with $\nu_{t}^{*}$.

<!-- kind: eq; id: 56; section: 3.2.5; page: 24; pdf_page: 30 -->
**(56) Adjustment cost of changing the share in world trade**

$$
\Gamma_{X}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right) \equiv \frac{\gamma^{*}}{2}\left[\left(\varepsilon_{t}^{X}\right)^{-\frac{1}{\gamma^{*}}} \frac{X_{t}/WT_{t}^{*}}{X_{t-1}/WT_{t-1}^{*}} - 1\right]^{2}
\tag{56}
$$

Meaning: A quadratic cost in the growth of exports' world-trade share, scaled by $\gamma^{*}$ and shifted by $\varepsilon_{t}^{X}$. Footnote 17: the notational shortcut of (38) applies.

<!-- kind: eq; id: 57; section: 3.2.5; page: 24; pdf_page: 30 -->
**(57) Definition of the auxiliary function Γ† for exports**

$$
\Gamma_{X}^{\dagger}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right) \equiv 1 - \Gamma_{X}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right) - \Gamma'_{X}\left(X_{t}/WT_{t}^{*};\varepsilon_{t}^{X}\right) X_{t}
\tag{57}
$$

Meaning: $\Gamma_{X}^{\dagger}$ is one minus the export adjustment cost, minus the cost function's derivative multiplied by $X_{t}$.

Note: As in 44.i1, the derivative term is multiplied by the level $X_{t}$, not by the ratio $X_{t}/WT_{t}^{*}$, as printed.
