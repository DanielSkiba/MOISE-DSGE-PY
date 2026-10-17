# The log-linearized model (Appendix D)

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

The complete log-linearized system: households, wages, intermediate- and final-good firms, fiscal and monetary authorities, net foreign assets, market clearing, foreign economy, observation equations and trend-shock processes. Equations (212)–(331). Under each equation is a plain code form generated from the LaTeX (see README).

## Appendix D The log-linearized model

**Summary.** Appendix D lists the full system of log-linearized equilibrium conditions of MOISE, grouped by agent and sector (households, labor market, intermediate-good and final-good firms here; fiscal/monetary, external, market-clearing and foreign blocks follow in later chunks). The short opening paragraph only introduces two abbreviations used in the equation labels: FOC ("First Order Condition") and WRT ("With Respect To"). It does not restate what a hat means or how variables are detrended; the normalization (real variables divided by productivity $z_{t}$, nominal ones by the CPI $P_{C,t}$, lower-case letters for stationarized variables) is described at the start of Appendix C. In the equations below, unhatted symbols such as $p_{H}$, $R$ or $h$ enter only as constant coefficients (steady-state values in the Appendix C notation).

### D.1 Households' Choice of Allocations

**Summary.** Log-linearized optimality conditions of households: the marginal utility of consumption (external habits, consumption tax), the FOCs for next-period capital (Tobin's Q), investment (two-lag adjustment cost) and capital utilization, the Euler equation for domestic bonds, a risk-adjusted uncovered interest parity condition, and the law of motion of the capital stock.

<!-- kind: eq; id: 212; section: D.1; page: 111; pdf_page: 117 -->
**(212) Marginal utility from consumption**

$$
\hat{\lambda}_{t} = \frac{\kappa g_{z}^{(-1)}}{1-\kappa g_{z}^{(-1)}} \hat{c}_{t-1} - \frac{1}{1-\kappa g_{z}^{(-1)}} \hat{c}_{t} - \frac{\kappa g_{z}^{(-1)}}{1-\kappa g_{z}^{(-1)}} \hat{g}_{z,t} - \frac{1}{1+0.78 \tau^{c}} \hat{\tau}_{t}^{C} + \hat{\epsilon}_{t}^{C}
\tag{212}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
lambda = (kappa*g_z_ss^(-1))/(1 - kappa*g_z_ss^(-1))*c(-1) - (1)/(1 - kappa*g_z_ss^(-1))*c - (kappa*g_z_ss^(-1))/(1 - kappa*g_z_ss^(-1))*g_z - (1)/(1 + 0.78*tau_C_ss)*tau_C + epsilon_C
```

Meaning: Marginal utility of consumption rises with lagged consumption (habits) and falls with current consumption, productivity growth and the consumption tax; a consumption-demand shock shifts it.

Note: The coefficient on $\hat{\tau}_{t}^{C}$ is printed with a lower-case $\tau^{c}$; 0.78 is the numerical value of the share of taxed goods $w_{\tau^{C}}$ (Table 1). Shocks in Appendix D are printed with the lunate $\epsilon$ (main text uses $\varepsilon$).

Note: Possible typo (transcribed as printed): log-linearizing (5) with $\hat{\tau}_{t}^{C}$ as an absolute deviation gives the numerator 0.78 rather than 1 in the tax coefficient (see [transcription notes](transcription-notes/T11.md)).

<!-- kind: eq; id: 213; section: D.1; page: 112; pdf_page: 118 -->
**(213) FOC WRT $K_{t+1}$ (Tobin's Q)**

$$
\begin{aligned}
\hat{Q}_{t} ={}& \frac{\beta \left(1-\delta\right)}{g_{z}} E_{t}\left(\hat{Q}_{t+1}\right) + E_{t}\left(\hat{\lambda}_{t+1}\right) - \hat{\lambda}_{t} - E_{t}\left(\hat{g}_{z,t+1}\right) \\
&- \frac{\beta \left(1-\tau^{K}\right) \gamma_{u,1}}{g_{z}} E_{t}\left(\frac{1}{1-\tau^{K}} \hat{\tau}_{t+1}^{K} - \hat{r}_{k,t+1}\right) + \frac{\beta \delta}{g_{z}} E_{t}\left(\hat{\tau}_{t+1}^{K} + \tau^{K} \hat{p}_{I,t+1}\right)
\end{aligned}
\tag{213}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Q = (beta*(1 - delta))/(g_z_ss)*(Q(+1)) + (lambda(+1)) - lambda - (g_z(+1)) - (beta*(1 - tau_K_ss)*gamma_u_1)/(g_z_ss)*((1)/(1 - tau_K_ss)*tau_K(+1) - r_k(+1)) + (beta*delta)/(g_z_ss)*(tau_K(+1) + tau_K_ss*p_I(+1))
```

Meaning: Tobin's Q equals discounted expected future Q plus expected marginal-utility growth net of productivity growth, plus terms in the expected after-tax rental return and the tax depreciation allowance.

<!-- kind: eq; id: 214; section: D.1; page: 112; pdf_page: 118 -->
**(214) FOC WRT Investment**

$$
\begin{aligned}
\hat{\imath}_{t} ={}& \frac{1}{1+\left(1-\omega_{\Gamma_{I}}\right)^{2} \beta+\omega_{\Gamma_{I}}^{2} \beta^{2}} \left(\begin{array}{c}
\omega_{\Gamma_{I}} \beta^{2} E_{t}\left(\hat{\imath}_{t+2}\right)+\left(1-\omega_{\Gamma_{I}}\right) \beta \left(1-\omega_{\Gamma_{I}} \beta\right) E_{t}\left(\hat{\imath}_{t+1}\right) \\
+\left(1-\omega_{\Gamma_{I}}\right) \left(1-\omega_{\Gamma_{I}} \beta\right) \hat{\imath}_{t-1}+\omega_{\Gamma_{I}} \hat{\imath}_{t-2}
\end{array}\right) \\
&+ \frac{1}{1+\left(1-\omega_{\Gamma_{I}}\right)^{2} \beta+\omega_{\Gamma_{I}}^{2} \beta^{2}} \left(\begin{array}{c}
\omega_{\Gamma_{I}} \beta^{2} E_{t}\left(\hat{g}_{z,t+2}\right)+\left(\omega_{\Gamma_{I}}^{2} \beta^{2}+\left(1-\omega_{\Gamma_{I}}\right) \beta\right) E_{t}\left(\hat{g}_{z,t+1}\right) \\
+\left(\beta \omega_{\Gamma_{I}} \left(1-\omega_{\Gamma_{I}}\right) \hat{g}_{z,t}-1\right)+\omega_{\Gamma_{I}} \hat{g}_{z,t-1}
\end{array}\right) \\
&+ \frac{1}{\left(1+\left(1-\omega_{\Gamma_{I}}\right)^{2} \beta+\omega_{\Gamma_{I}}^{2} \beta^{2}\right) \gamma_{I} g_{z}^{2\left(1-\omega_{\Gamma_{I}}\right)}} \left(\hat{Q}_{t}-\hat{p}_{I,t}+\hat{\epsilon}_{t}^{I}\right)
\end{aligned}
\tag{214}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
i = (1)/(1 + ((1 - omega_Gamma_I))^(2)*beta + omega_Gamma_I^(2)*beta^(2))*(omega_Gamma_I*beta^(2)*(i(+2)) + (1 - omega_Gamma_I)*beta*(1 - omega_Gamma_I*beta)*(i(+1)) + (1 - omega_Gamma_I)*(1 - omega_Gamma_I*beta)*i(-1) + omega_Gamma_I*i(-2)) + (1)/(1 + ((1 - omega_Gamma_I))^(2)*beta + omega_Gamma_I^(2)*beta^(2))*(omega_Gamma_I*beta^(2)*(g_z(+2)) + (omega_Gamma_I^(2)*beta^(2) + (1 - omega_Gamma_I)*beta)*(g_z(+1)) + (beta*omega_Gamma_I*(1 - omega_Gamma_I)*g_z - 1) + omega_Gamma_I*g_z(-1)) + (1)/((1 + ((1 - omega_Gamma_I))^(2)*beta + omega_Gamma_I^(2)*beta^(2))*gamma_I*g_z_ss^(2*(1 - omega_Gamma_I)))*(Q - p_I + epsilon_I)
```

Meaning: Investment depends on its own expected leads and lags (two each), on productivity growth at several dates, and on Tobin's Q net of the investment price, plus the investment shock.

Note: Typesetting: $\hat{\imath}$ is printed as a dotless i with a hat (investment $i$); the two-line contents of the large parentheses are kept as printed with `array`; the hat on $\hat{p}_{I,t}$ is printed displaced over the subscript and is transcribed as $\hat{p}_{I,t}$ (as in (215)).

Note: Suspected typos (transcribed as printed; see [transcription notes](transcription-notes/T11.md)): (a) $\hat{g}_{z,t}$ appears inside the parentheses $\left(\beta \omega_{\Gamma_{I}} \left(1-\omega_{\Gamma_{I}}\right) \hat{g}_{z,t}-1\right)$, whereas a derivation from (9)–(11) gives $\left(\beta \omega_{\Gamma_{I}} \left(1-\omega_{\Gamma_{I}}\right)-1\right) \hat{g}_{z,t}$; (b) the same derivation gives $-\omega_{\Gamma_{I}} \hat{g}_{z,t-1}$ instead of $+\omega_{\Gamma_{I}} \hat{g}_{z,t-1}$; (c) with $\Gamma_{I}$ as in (10) the steady-state curvature term would be $\gamma_{I} g_{z}^{2\left(1+\omega_{\Gamma_{I}}\right)}$, not $g_{z}^{2\left(1-\omega_{\Gamma_{I}}\right)}$.

<!-- kind: eq; id: 215; section: D.1; page: 112; pdf_page: 118 -->
**(215) FOC WRT Capital Utilization**

$$
\hat{r}_{k,t} = \hat{p}_{I,t} + \frac{\gamma_{u,2}}{\gamma_{u,1}} \hat{u}_{t}
\tag{215}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r_k = p_I + (gamma_u_2)/(gamma_u_1)*u
```

Meaning: The real rental rate of capital equals the relative investment price plus capital utilization scaled by the ratio of the two utilization-cost parameters.

<!-- kind: eq; id: 216; section: D.1; page: 112; pdf_page: 118 -->
**(216) FOC WRT Domestic Bonds**

$$
E_{t}\left(\hat{\lambda}_{t+1}\right) - \hat{\lambda}_{t} - E_{t}\left(\hat{g}_{z,t+1}\right) + \hat{r}_{t} - E_{t}\left(\hat{\pi}_{C,t+1}\right) + \hat{\epsilon}_{t}^{RP} + \hat{\epsilon}_{t}^{DRP} = 0
\tag{216}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
(lambda(+1)) - lambda - (g_z(+1)) + r - (pi_C(+1)) + epsilon_RP + epsilon_DRP = 0
```

Meaning: Bond Euler equation: expected marginal-utility growth (net of productivity growth) plus the ex-ante real interest rate and the symmetric and domestic premium shocks sum to zero.

<!-- kind: eq; id: 217; section: D.1; page: 112; pdf_page: 118 -->
**(217) Modified (Risk-adjusted) UIP Condition**

$$
\begin{aligned}
\hat{r}_{t} - \hat{r}_{t}^{*} ={}& \left(1-\gamma_{S}\right) \left(E_{t}\left(\hat{s}_{t+1}\right) - \hat{s}_{t}\right) + E_{t}\left(\hat{\pi}_{Y,t+1} - \hat{\pi}_{Y,t+1}^{*}\right) - \gamma_{S} \left(\hat{s}_{t} - \hat{s}_{t-1} + \hat{\pi}_{Y,t} - \hat{\pi}_{y,t}^{*}\right) \\
&+ \gamma_{S} \left(E_{t}\left(\hat{\bar{\pi}}_{t+1} - \hat{\bar{\pi}}_{t+1}^{*}\right) + \left(\hat{\bar{\pi}}_{t} - \hat{\bar{\pi}}_{t}^{*}\right)\right) - \gamma_{B} E_{t}\left(\hat{s}_{B^{*},t+1}\right) + \hat{\epsilon}_{t}^{RP^{*}} - \hat{\epsilon}_{t}^{DRP}
\end{aligned}
\tag{217}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r - r_star = (1 - gamma_S)*((s(+1)) - s) + (pi_Y(+1) - pi_Y_star(+1)) - gamma_S*(s - s(-1) + pi_Y - pi_Y_star) + gamma_S*((pibar(+1) - pibar_star(+1)) + (pibar - pibar_star)) - gamma_B*(s_Bstar(+1)) + epsilon_RPstar - epsilon_DRP
```

Meaning: The domestic-foreign interest differential depends on expected real depreciation, the expected output-inflation differential, current nominal depreciation and inflation-target differentials, expected net foreign assets, and premium shocks.

Note: The last term of the first line is printed with a lower-case $y$ ($\hat{\pi}_{y,t}^{*}$) while the other foreign-inflation terms use $Y$; $\hat{\bar{\pi}}$ is a hat printed over a bar (zoomed). The premium coefficient is printed $\gamma_{B}$ (main text eq. (4): $\gamma_{B^{*}}$).

Note: Possible inconsistency (derivation check, transcribed as printed): log-linearizing (4), (6) and (7) puts the factor $\left(1-\gamma_{S}\right)$ on the whole expected nominal depreciation, i.e. also on $E_{t}\left(\hat{\pi}_{Y,t+1} - \hat{\pi}_{Y,t+1}^{*}\right)$, which is printed here with coefficient 1.

<!-- kind: eq; id: 218; section: D.1; page: 112; pdf_page: 118 -->
**(218) Capital Accumulation**

$$
\hat{k}_{t+1} = \frac{\left(1-\delta\right)}{g_{z}} \left(\hat{k}_{t} - \hat{g}_{z,t}\right) + \left(1 - \frac{\left(1-\delta\right)}{g_{z}}\right) \left(\hat{\imath}_{t} + \hat{\epsilon}_{t}^{I}\right)
\tag{218}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
k(+1) = ((1 - delta))/(g_z_ss)*(k - g_z) + (1 - ((1 - delta))/(g_z_ss))*(i + epsilon_I)
```

Meaning: Next period's capital is undepreciated current capital (adjusted for productivity growth) plus investment augmented by the investment-specific technology shock.

### D.2 Labor Supply and Wage Setting

**Summary.** Labor-market block: the after-tax real wage, the households' marginal rate of substitution between consumption and leisure, and the Calvo wage-setting equation for nominal wage inflation, which includes indexation to lagged CPI inflation, to the inflation target and to lagged productivity growth.

<!-- kind: eq; id: 219; section: D.2; page: 112; pdf_page: 118 -->
**(219) After-tax real wage**

$$
\hat{w}_{\tau,t} = \hat{w}_{t} - \frac{1}{1-\tau^{N}-\tau^{W_{h}}} \left(\hat{\tau}_{t}^{N} + \hat{\tau}_{t}^{W_{h}}\right)
\tag{219}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
w_tau = w - (1)/(1 - tau_N_ss - tau_W_h_ss)*(tau_N + tau_W_h)
```

Meaning: The after-tax real wage equals the real wage minus the sum of the labor-income and household payroll tax-rate deviations, divided by the steady-state net-of-tax share.

<!-- kind: eq; id: 220; section: D.2; page: 113; pdf_page: 119 -->
**(220) MRS between consumption and leisure**

$$
\widehat{mrs}_{t} = \hat{\epsilon}_{N,t} + \zeta \hat{n}_{t} - \hat{\lambda}_{t}
\tag{220}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
mrs = epsilon_N + zeta*n - lambda
```

Meaning: The marginal rate of substitution rises with the labor-supply shock and with hours (scaled by the inverse Frisch elasticity) and falls with the marginal utility of consumption.

Note: The labor-supply shock is printed with $N$ as a subscript ($\hat{\epsilon}_{N,t}$); the main text writes $\varepsilon_{t}^{N}$.

<!-- kind: eq; id: 221; section: D.2; page: 113; pdf_page: 119 -->
**(221) Nominal-wage Inflation**

$$
\begin{aligned}
& \hat{g}_{z,t} + \hat{w}_{t} - \hat{w}_{t-1} + \hat{\pi}_{C,t} - \chi_{W} \hat{\pi}_{C,t-1} - \left(1-\chi_{W}\right) \hat{\bar{\pi}}_{t} - \chi_{W,g_{z}} \hat{g}_{z,t-1} \\
={}& \beta \left[E_{t}\left(\hat{g}_{z,t+1}\right) + E_{t}\left(\hat{\pi}_{C,t+1}\right) + E_{t}\left(\hat{w}_{t+1}\right) - \hat{w}_{t} - \left(\hat{\pi}_{C,t} \chi_{W} + \left(1-\chi_{W}\right) E_{t}\left(\hat{\bar{\pi}}_{t+1}\right) + \chi_{W,g_{z}} \hat{g}_{z,t}\right)\right] \\
&- \frac{\left(1-\beta \xi_{W}\right) \left(1-\xi_{W}\right)}{\xi_{W} \left(1+\zeta \frac{\phi_{w}}{\phi_{w}-1}\right)} \left[\hat{w}_{t} - \frac{1}{1-\tau^{N}-\tau^{W_{h}}} \left(\hat{\tau}_{t}^{N} + \hat{\tau}_{t}^{W_{h}}\right) - \left(\hat{\epsilon}_{N,t} + \zeta \hat{n}_{t} - \hat{\lambda}_{t}\right) - \hat{\phi}_{w,t}\right]
\end{aligned}
\tag{221}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
g_z + w - w(-1) + pi_C - chi_W*pi_C(-1) - (1 - chi_W)*pibar - chi_W_g_z*g_z(-1) = beta*((g_z(+1)) + (pi_C(+1)) + (w(+1)) - w - (pi_C*chi_W + (1 - chi_W)*(pibar(+1)) + chi_W_g_z*g_z)) - ((1 - beta*xi_W)*(1 - xi_W))/(xi_W*(1 + zeta*(phi_w_ss)/(phi_w_ss - 1)))*(w - (1)/(1 - tau_N_ss - tau_W_h_ss)*(tau_N + tau_W_h) - (epsilon_N + zeta*n - lambda) - phi_w)
```

Meaning: Nominal wage inflation net of indexation depends on its expected future value and on the gap between the after-tax real wage and the MRS, plus a wage markup shock.

Note: On the first line the hat of $\hat{\pi}_{C,t}$ is printed displaced over the subscript $C$; transcribed as $\hat{\pi}_{C,t}$. The wage markup is printed with $\phi$ (closed loop, straight stroke) and lower-case $w$ ($\phi_{w}$, $\hat{\phi}_{w,t}$), whereas Table 1 and the main text use $\varphi^{W}$.

### D.3 Intermediate-good Firms Resource Allocation

**Summary.** Cost side of domestic intermediate-good producers: the production function with a fixed cost, the cost-minimizing condition linking the rental rate of capital to labor costs, real marginal cost in CPI terms (including the firms' payroll tax and the working-capital channel), and the interest rate on working capital.

<!-- kind: eq; id: 222; section: D.3; page: 113; pdf_page: 119 -->
**(222) Production technology**

$$
\hat{h}_{s,t} = \left(1+\psi h^{(-1)}\right) \left[\hat{\epsilon}_{t} + \alpha \left(\hat{k}_{t}^{s} - \hat{g}_{z,t}\right) + \left(1-\alpha\right) \hat{n}_{t}\right]
\tag{222}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_s = (1 + psi*h_ss^(-1))*(epsilon + alpha*(k_s - g_z) + (1 - alpha)*n)
```

Meaning: Domestic intermediate output moves with transitory technology, capital services net of productivity growth, and hours, amplified by one plus the fixed-cost-to-output ratio.

Note: $\hat{k}_{t}^{s}$ is printed with the hat spanning $k^{s}$ and the time subscript placed after the superscript; transcribed in the same form as in (223).

<!-- kind: eq; id: 223; section: D.3; page: 113; pdf_page: 119 -->
**(223) Resource allocation**

$$
\hat{r}_{k,t} = \hat{w}_{t} + \hat{n}_{t} + \left(1+\tau^{W_{f}}\right)^{(-1)} \hat{\tau}_{t}^{W_{f}} + \hat{R}_{f,t} - \hat{k}_{t}^{s} + \hat{g}_{z,t}
\tag{223}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r_k = w + n + ((1 + tau_W_f_ss))^(-1)*tau_W_f + R_f - k_s + g_z
```

Meaning: Cost minimization ties the rental rate of capital to the real wage, hours, the firms' payroll tax, the working-capital rate, capital services and productivity growth.

Note: The hat of $\hat{R}_{f,t}$ is printed displaced to the right; transcribed as $\hat{R}_{f,t}$ (as in (224) and (225)).

<!-- kind: eq; id: 224; section: D.3; page: 113; pdf_page: 119 -->
**(224) Real marginal cost (in terms of CPI)**

$$
\widehat{mc}_{t} = \alpha \hat{r}_{k,t} + \left(1-\alpha\right) \left[\hat{R}_{f,t} + \hat{w}_{t} + \left(1+\tau^{W_{f}}\right)^{(-1)} \hat{\tau}_{t}^{W_{f}}\right] - \hat{\epsilon}_{t}
\tag{224}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
mc = alpha*r_k + (1 - alpha)*(R_f + w + ((1 + tau_W_f_ss))^(-1)*tau_W_f) - epsilon
```

Meaning: Real marginal cost is a capital-share-weighted sum of the rental rate and the effective labor cost (working-capital rate, wage, payroll tax), minus transitory technology.

<!-- kind: eq; id: 225; section: D.3; page: 113; pdf_page: 119 -->
**(225) Interest rate on working capital**

$$
\hat{R}_{f,t} = \frac{\nu^{f} R}{1-\nu^{f} \left(R-1\right)} \left(\hat{r}_{t} + \hat{\epsilon}_{t}^{RP} + \hat{\epsilon}_{t}^{F}\right) + \frac{\nu^{f} \left(R-1\right)}{1-\nu^{f} \left(R-1\right)} \hat{\nu}_{f,t}
\tag{225}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
R_f = (nu_f_ss*R_ss)/(1 - nu_f_ss*(R_ss - 1))*(r + epsilon_RP + epsilon_F) + (nu_f_ss*(R_ss - 1))/(1 - nu_f_ss*(R_ss - 1))*nu_f
```

Meaning: The working-capital interest rate moves with the policy rate, the symmetric premium shock and a shock $\hat{\epsilon}_{t}^{F}$, and with $\hat{\nu}_{f,t}$, using steady-state weights.

Note: Both denominators are printed $1-\nu^{f}\left(R-1\right)$; the main text defines $R_{t}^{F} = 1 + \nu^{F}\left(R_{t}-1\right)$ (PDF p.21), which would give $1+\nu^{f}\left(R-1\right)$ (suspected sign typo). $\nu^{f}$ is printed with a lower-case $f$ (Table 1: $\nu^{F}$). $\hat{\epsilon}_{t}^{F}$ and $\hat{\nu}_{f,t}$ are not defined in the text.

### D.4 Intermediate-good Firms Price Setting (Phillips Curves)

**Summary.** Calvo price setting by intermediate-good firms: the hybrid Phillips curve of domestic producers (inflation measured relative to the inflation target), the conversion of marginal cost into domestic-price terms, the law of motion of the relative domestic price, and the analogous Phillips curve, marginal cost and relative import price for foreign intermediate-good firms, which price in local currency.

<!-- kind: eq; id: 226; section: D.4; page: 113; pdf_page: 119 -->
**(226) Phillips Curve of the domestic intermediate goods firm**

$$
\begin{aligned}
\hat{\pi}_{H,t} - \hat{\bar{\pi}}_{t} ={}& \frac{\beta}{1+\beta \chi_{H}} E_{t}\left(\hat{\pi}_{H,t+1} - \hat{\bar{\pi}}_{t+1}\right) + \frac{\chi_{H}}{1+\beta \chi_{H}} \left(\hat{\pi}_{H,t-1} - \hat{\bar{\pi}}_{t}\right) \\
&+ \frac{\beta \chi_{H}}{1+\beta \chi_{H}} \left[E_{t}\left(\hat{\bar{\pi}}_{t+1}\right) - \hat{\bar{\pi}}_{t}\right] + \frac{\left(1-\beta \xi_{H}\right) \left(1-\xi_{H}\right)}{\left(1+\beta \chi_{H}\right) \xi_{H}} \left(\widehat{mc}_{t}^{H} + \hat{\varphi}_{t}^{H}\right)
\end{aligned}
\tag{226}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pi_H - pibar = (beta)/(1 + beta*chi_H)*(pi_H(+1) - pibar(+1)) + (chi_H)/(1 + beta*chi_H)*(pi_H(-1) - pibar) + (beta*chi_H)/(1 + beta*chi_H)*((pibar(+1)) - pibar) + ((1 - beta*xi_H)*(1 - xi_H))/((1 + beta*chi_H)*xi_H)*(mc_H + varphi_H)
```

Meaning: Domestic inflation relative to the target depends on expected and lagged inflation gaps, the expected change in the target, and real marginal cost plus a markup shock.

<!-- kind: eq; id: 227; section: D.4; page: 114; pdf_page: 120 -->
**(227) Real marginal cost in terms of the domestic price index**

$$
\widehat{mc}_{t}^{H} = \widehat{mc}_{t} - \hat{p}_{H,t}
\tag{227}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
mc_H = mc - p_H
```

Meaning: Domestic firms' real marginal cost re-expressed relative to the domestic price index instead of the CPI.

<!-- kind: eq; id: 228; section: D.4; page: 114; pdf_page: 120 -->
**(228) Real domestic price index (relative to CPI)**

$$
\hat{p}_{H,t} = \hat{\pi}_{H,t} + \hat{p}_{H,t-1} - \hat{\pi}_{C,t}
\tag{228}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_H = pi_H + p_H(-1) - pi_C
```

Meaning: The relative price of domestic goods rises with domestic inflation and falls with CPI inflation.

<!-- kind: eq; id: 229; section: D.4; page: 114; pdf_page: 120 -->
**(229) Phillips curve of foreign intermediate-goods firms (in local currency)**

$$
\begin{aligned}
\hat{\pi}_{IM,t} - \hat{\bar{\pi}}_{t} ={}& \frac{\beta^{*}}{1+\beta^{*} \chi^{*}} E_{t}\left(\hat{\pi}_{IM,t+1} - \hat{\bar{\pi}}_{t+1}\right) + \frac{\chi^{*}}{1+\beta^{*} \chi^{*}}\left(\hat{\pi}_{IM,t-1} - \hat{\bar{\pi}}_{t}\right) \\
&+ \frac{\beta^{*} \chi^{*}}{1+\beta^{*} \chi^{*}}\left[E_{t}\left(\hat{\bar{\pi}}_{t+1}\right) - \hat{\bar{\pi}}_{t}\right] + \frac{\left(1-\beta^{*} \xi^{*}\right)\left(1-\xi^{*}\right)}{\left(1+\beta^{*} \chi^{*}\right) \xi^{*}}\left(\widehat{mc}_{IM,t} + \hat{\varphi}_{t}^{*}\right)
\end{aligned}
\tag{229}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pi_IM - pibar = (beta_star)/(1 + beta_star*chi_star)*(pi_IM(+1) - pibar(+1)) + (chi_star)/(1 + beta_star*chi_star)*(pi_IM(-1) - pibar) + (beta_star*chi_star)/(1 + beta_star*chi_star)*((pibar(+1)) - pibar) + ((1 - beta_star*xi_star)*(1 - xi_star))/((1 + beta_star*chi_star)*xi_star)*(mc_IM + varphi_star)
```

Meaning: Import-price inflation (relative to the inflation target) depends on its expected and lagged values, the expected change in the target, and importers' real marginal cost plus a markup shock.

<!-- kind: eq; id: 230; section: D.4; page: 114; pdf_page: 120 -->
**(230) Real marginal cost of foreign intermediate-goods firms, in terms of the import price**

$$
\widehat{mc}_{IM,t} = \hat{s}_{t} + \hat{p}_{Y,t} + \omega^{*}\left[\hat{p}_{OIL,t} - \left(\hat{\pi}_{y,t}^{*} + \hat{p}_{OIL,t} - \hat{p}_{OIL,t-1}\right)\right] - \hat{p}_{IM,t}
\tag{230}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
mc_IM = s + p_Y + omega_star*(p_OIL - (pi_Y_star + p_OIL - p_OIL(-1))) - p_IM
```

Meaning: Importers' marginal cost moves with the real exchange rate, the domestic output price, and an oil-price term weighted by the oil share, relative to the import price.

<!-- kind: eq; id: 231; section: D.4; page: 114; pdf_page: 120 -->
**(231) Real price of imported goods (local currency, relative to CPI)**

$$
\hat{p}_{IM,t} = \hat{\pi}_{IM,t} + \hat{p}_{IM,t-1} - \hat{\pi}_{C,t}
\tag{231}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_IM = pi_IM + p_IM(-1) - pi_C
```

Meaning: The relative import price rises with import-price inflation and falls with CPI inflation.

### D.5 Final-Good Firms: Technology, Inputs and Prices

**Summary.** Final-good producers in four sectors (private consumption, investment, public consumption, exports) combine domestic and imported intermediate goods with sector-specific elasticities of substitution, time-varying home bias and import-share adjustment costs. For each sector the block gives the two input demands, the adjustment-cost term and a price equation. From here on prices are real, i.e. measured relative to the CPI (except the export price $\hat{p}_{X,t}$ in D.5.5, which is relative to the foreign output deflator).

<!-- kind: inline; id: 231.i1; section: D.5; page: 114; pdf_page: 120 -->
**(231.i1) Real-price notation (example for domestic intermediate goods)**

$$
\hat{p}_{H,t} \equiv \ln\left(P_{H,t}/P_{C,t}\right)
$$

Meaning: Hatted price variables denote the log of a nominal price index divided by the CPI; the example given is the domestic intermediate-goods price.

#### D.5.1 Final private consumption good

**Summary.** Private consumption good: demands for domestic and imported intermediate inputs, the import-share adjustment-cost term, and the price condition; because the consumption-good price is the CPI used as denominator, its relative price is constant, so the price condition is set equal to zero.

<!-- kind: eq; id: 232; section: D.5.1; page: 114; pdf_page: 120 -->
**(232) Demand for domestic intermediate goods (consumption good)**

$$
\hat{h}_{C,t} = \hat{q}_{C,t} - \hat{p}_{H,t} \mu_{C} + \hat{\nu}_{C,t}
\tag{232}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_C = q_C - p_H*mu_C + nu_C
```

Meaning: Domestic intermediate input demand of consumption-good producers rises with their output and with home bias and falls with the relative domestic price times the substitution elasticity.

<!-- kind: eq; id: 233; section: D.5.1; page: 115; pdf_page: 121 -->
**(233) Demand for imported intermediate goods (consumption good)**

$$
\widehat{im}_{C,t} = \hat{q}_{C,t} - \mu_{c} \left(\hat{p}_{IM,t} - \hat{\Gamma}_{IM^{C},t}^{+}\right) - \frac{\nu_{E}}{1-\nu_{E}} \hat{\nu}_{C,t}
\tag{233}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im_C = q_C - mu_C*(p_IM - Gamma_IMC_p) - (nu_E)/(1 - nu_E)*nu_C
```

Meaning: Imported input demand of consumption-good producers rises with output and falls with the import price net of the adjustment-cost term and with home bias.

Note: Printed with lower-case $\mu_{c}$ (elsewhere $\mu_{C}$, e.g. (232), (235)) and with $\nu_{E}$ in the home-bias coefficient; the analogous (237), (241), (245) use the sector's own weight ($\nu_{I}$, $\nu_{G}$, $\nu_{X}$), so $\nu_{E}$ is presumably $\nu_{C}$ (suspected typo).

<!-- kind: eq; id: 234; section: D.5.1; page: 115; pdf_page: 121 -->
**(234) Import share adjustment costs (consumption good)**

$$
\hat{\Gamma}_{IM^{C},t}^{+} = -\gamma_{IM}^{C} \left[\left(\widehat{im}_{C,t} - \hat{q}_{C,t}\right) - \left(\widehat{im}_{C,t-1} - \hat{q}_{C,t-1}\right)\right] + \hat{\epsilon}_{t}^{IM}
\tag{234}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Gamma_IMC_p = -gamma_IM_C*((im_C - q_C) - (im_C(-1) - q_C(-1))) + epsilon_IM
```

Meaning: The adjustment-cost term falls with the change in import intensity of consumption-good production and is shifted by the import demand shock.

<!-- kind: eq; id: 235; section: D.5.1; page: 115; pdf_page: 121 -->
**(235) Price of the private consumption good**

$$
0 = \nu_{C} p_{H}^{1-\mu_{C}} \hat{p}_{H,t} + \left(1-\nu_{C}\right) p_{IM}^{1-\mu_{C}} \left(\hat{p}_{IM,t} - \hat{\Gamma}_{IM^{C},t}^{+}\right) + \frac{\nu_{C}}{1-\mu_{C}} \left(p_{H}^{1-\mu_{C}} - p_{IM}^{1-\mu_{C}}\right) \hat{\nu}_{ct}
\tag{235}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
0 = nu_C_ss*p_H_ss^(1 - mu_C)*p_H + (1 - nu_C_ss)*p_IM_ss^(1 - mu_C)*(p_IM - Gamma_IMC_p) + (nu_C_ss)/(1 - mu_C)*(p_H_ss^(1 - mu_C) - p_IM_ss^(1 - mu_C))*nu_C
```

Meaning: With the consumption-good price as numeraire, the share-weighted domestic price, effective import price and home-bias term must sum to zero.

Note: The home-bias variable is printed $\hat{\nu}_{ct}$ (lower-case $c$, no comma); presumably $\hat{\nu}_{C,t}$ as in (232)–(233).

#### D.5.2 Final investment good

**Summary.** Investment good: the same structure as for consumption — domestic and imported input demands, the import-share adjustment-cost term, and the relative price of the investment good as a weighted average of input prices plus a home-bias term.

<!-- kind: eq; id: 236; section: D.5.2; page: 115; pdf_page: 121 -->
**(236) Demand for domestic intermediate goods (investment good)**

$$
\hat{h}_{I,t} = \hat{q}_{I,t} - \mu_{I} \left(\hat{p}_{H,t} - \hat{p}_{I,t}\right) + \hat{\nu}_{I,t}
\tag{236}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_I = q_I - mu_I*(p_H - p_I) + nu_I
```

Meaning: Domestic input demand of investment-good producers rises with their output and home bias and falls with the domestic price relative to the investment-good price.

<!-- kind: eq; id: 237; section: D.5.2; page: 115; pdf_page: 121 -->
**(237) Demand for imported intermediate goods (investment good)**

$$
\widehat{im}_{I,t} = \hat{q}_{I,t} - \mu_{I} \left(\hat{p}_{IM,t} - \hat{p}_{I,t} - \hat{\Gamma}_{IM^{I}t}^{+}\right) - \frac{\nu_{I}}{1-\nu_{I}} \hat{\nu}_{I,t}
\tag{237}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im_I = q_I - mu_I*(p_IM - p_I - Gamma_IMI_p) - (nu_I_ss)/(1 - nu_I_ss)*nu_I
```

Meaning: Imported input demand of investment-good producers rises with output and falls with the effective import price relative to the investment-good price and with home bias.

Note: The subscript of $\hat{\Gamma}^{+}$ is printed $IM^{I}t$ without a comma (cf. $IM^{I},t$ in (238) and (239)).

<!-- kind: eq; id: 238; section: D.5.2; page: 115; pdf_page: 121 -->
**(238) Import share adjustment costs (investment good)**

$$
\hat{\Gamma}_{IM^{I},t}^{+} = -\gamma_{IM}^{I} \left[\left(\widehat{im}_{I,t} - \hat{q}_{I,t}\right) - \left(\widehat{im}_{I,t-1} - \hat{q}_{I,t-1}\right)\right] + \hat{\epsilon}_{t}^{IM}
\tag{238}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Gamma_IMI_p = -gamma_IM_I*((im_I - q_I) - (im_I(-1) - q_I(-1))) + epsilon_IM
```

Meaning: The investment-sector adjustment-cost term falls with the change in import intensity and is shifted by the import demand shock.

<!-- kind: eq; id: 239; section: D.5.2; page: 115; pdf_page: 121 -->
**(239) Price of the investment good**

$$
\begin{aligned}
\hat{p}_{I,t} ={}& \hat{p}_{H,t} \nu_{I} \left(\frac{p_{H}}{p_{I}}\right)^{1-\mu_{I}} + \left(1-\nu_{I}\right) \left(\frac{p_{IM}}{p_{I}}\right)^{1-\mu_{I}} \left(\hat{p}_{IM,t} - \hat{\Gamma}_{IM^{I},t}^{+}\right) \\
&+ \frac{\nu_{I}}{1-\mu_{I}} \left[\left(\frac{p_{H}}{p_{I}}\right)^{1-\mu_{I}} - \left(\frac{p_{IM}}{p_{I}}\right)^{1-\mu_{I}}\right] \hat{\nu}_{I,t}
\end{aligned}
\tag{239}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_I = p_H*nu_I_ss*(((p_H_ss)/(p_I_ss)))^(1 - mu_I) + (1 - nu_I_ss)*(((p_IM_ss)/(p_I_ss)))^(1 - mu_I)*(p_IM - Gamma_IMI_p) + (nu_I_ss)/(1 - mu_I)*((((p_H_ss)/(p_I_ss)))^(1 - mu_I) - (((p_IM_ss)/(p_I_ss)))^(1 - mu_I))*nu_I
```

Meaning: The relative investment price is a steady-state-share-weighted average of the domestic price and the effective import price, plus a home-bias term.

#### D.5.3 Final public consumption good

**Summary.** Public consumption good: input demands, import-share adjustment-cost term and relative price, with the same structure as the investment-good block.

<!-- kind: eq; id: 240; section: D.5.3; page: 116; pdf_page: 122 -->
**(240) Demand for domestic intermediate goods (public consumption good)**

$$
\hat{h}_{G,t} = \hat{q}_{G,t} - \mu_{G} \left(\hat{p}_{H,t} - \hat{p}_{G,t}\right) + \hat{\nu}_{G,t}
\tag{240}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_G = q_G - mu_G*(p_H - p_G) + nu_G
```

Meaning: Domestic input demand of public-consumption-good producers rises with their output and home bias and falls with the domestic price relative to the public-good price.

<!-- kind: eq; id: 241; section: D.5.3; page: 116; pdf_page: 122 -->
**(241) Demand for imported intermediate goods (public consumption good)**

$$
\widehat{im}_{G,t} = \hat{q}_{G,t} - \mu_{G} \left(\hat{p}_{IM,t} - \hat{p}_{G,t} - \hat{\Gamma}_{IM^{G},t}^{+}\right) - \frac{\nu_{G}}{1-\nu_{G}} \hat{\nu}_{G,t}
\tag{241}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im_G = q_G - mu_G*(p_IM - p_G - Gamma_IMG_p) - (nu_G_ss)/(1 - nu_G_ss)*nu_G
```

Meaning: Imported input demand of public-good producers rises with output and falls with the effective import price relative to the public-good price and with home bias.

<!-- kind: eq; id: 242; section: D.5.3; page: 116; pdf_page: 122 -->
**(242) Import share adjustment costs (public consumption good)**

$$
\hat{\Gamma}_{IM^{G},t}^{+} = -\gamma_{IM}^{G} \left[\left(\widehat{im}_{G,t} - \hat{q}_{G,t}\right) - \left(\widehat{im}_{G,t-1} - \hat{q}_{G,t-1}\right)\right] + \hat{\epsilon}_{t}^{IM}
\tag{242}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Gamma_IMG_p = -gamma_IM_G*((im_G - q_G) - (im_G(-1) - q_G(-1))) + epsilon_IM
```

Meaning: The public-good adjustment-cost term falls with the change in import intensity and is shifted by the import demand shock.

<!-- kind: eq; id: 243; section: D.5.3; page: 116; pdf_page: 122 -->
**(243) Price of the public consumption goods**

$$
\begin{aligned}
\hat{p}_{G,t} ={}& \hat{p}_{H,t} \nu_{G} \left(\frac{p_{H}}{p_{G}}\right)^{1-\mu_{G}} + \left(1-\nu_{G}\right) \left(\frac{p_{IM}}{p_{G}}\right)^{1-\mu_{G}} \left(\hat{p}_{IM,t} - \hat{\Gamma}_{IM^{G},t}^{+}\right) \\
&+ \frac{\nu_{G}}{1-\mu_{G}} \left[\left(\frac{p_{H}}{p_{G}}\right)^{1-\mu_{G}} - \left(\frac{p_{IM}}{p_{G}}\right)^{1-\mu_{G}}\right] \hat{\nu}_{G,t}
\end{aligned}
\tag{243}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_G = p_H*nu_G_ss*(((p_H_ss)/(p_G_ss)))^(1 - mu_G) + (1 - nu_G_ss)*(((p_IM_ss)/(p_G_ss)))^(1 - mu_G)*(p_IM - Gamma_IMG_p) + (nu_G_ss)/(1 - mu_G)*((((p_H_ss)/(p_G_ss)))^(1 - mu_G) - (((p_IM_ss)/(p_G_ss)))^(1 - mu_G))*nu_G
```

Meaning: The relative public-good price is a share-weighted average of the domestic price and the effective import price, plus a home-bias term.

Note: The paper prints a stray period at the end of the first line (before the "+" continuation line); omitted here.

#### D.5.4 Final exports good

**Summary.** Exported good (the homogeneous good that exporters buy and brand): domestic and imported input demands, the import-share adjustment-cost term, and the domestic-currency price of the exported good relative to the CPI.

<!-- kind: eq; id: 244; section: D.5.4; page: 116; pdf_page: 122 -->
**(244) Demand for domestic intermediate goods (exports good)**

$$
\hat{h}_{X,t} = \hat{q}_{X,t} - \mu_{X} \left(\hat{p}_{H,t} - \hat{p}_{DX,t}\right) + \hat{\nu}_{X,t}
\tag{244}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_X = q_X - mu_X*(p_H - p_DX) + nu_X
```

Meaning: Domestic input demand of export-good producers rises with their output and home bias and falls with the domestic price relative to the exported good's price.

<!-- kind: eq; id: 245; section: D.5.4; page: 116; pdf_page: 122 -->
**(245) Demand for imported intermediate goods (exports good)**

$$
\widehat{im}_{X,t} = \hat{q}_{X,t} - \mu_{X} \left(\hat{p}_{IM,t} - \hat{p}_{DX,t} - \hat{\Gamma}_{IM^{X},t}^{+}\right) - \frac{\nu_{X}}{1-\nu_{X}} \hat{\nu}_{X,t}
\tag{245}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im_X = q_X - mu_X*(p_IM - p_DX - Gamma_IMX_p) - (nu_X_ss)/(1 - nu_X_ss)*nu_X
```

Meaning: Imported input demand of export-good producers rises with output and falls with the effective import price relative to the exported good's price and with home bias.

<!-- kind: eq; id: 246; section: D.5.4; page: 116; pdf_page: 122 -->
**(246) Import share adjustment costs (exports good)**

$$
\hat{\Gamma}_{IM^{X},t}^{+} = -\gamma_{IM}^{X} \left[\left(\widehat{im}_{X,t} - \hat{q}_{X,t}\right) - \left(\widehat{im}_{X,t-1} - \hat{q}_{X,t-1}\right)\right] + \hat{\epsilon}_{t}^{X}
\tag{246}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Gamma_IMX_p = -gamma_IM_X*((im_X - q_X) - (im_X(-1) - q_X(-1))) + epsilon_X
```

Meaning: The export-sector adjustment-cost term falls with the change in import intensity and is shifted by the shock $\hat{\epsilon}_{t}^{X}$.

Note: The shock is printed $\hat{\epsilon}_{t}^{X}$, whereas the analogous (234), (238), (242) use $\hat{\epsilon}_{t}^{IM}$; in the main text $\varepsilon_{t}^{X}$ belongs to the exporters' world-trade-share cost (eq. (56)), so this is a suspected typo.

<!-- kind: eq; id: 247; section: D.5.4; page: 117; pdf_page: 123 -->
**(247) (Domestic) Price of the exported good**

$$
\begin{aligned}
\hat{p}_{DX,t} ={}& \nu_{x} \left(\frac{p_{H}}{p_{DX}}\right)^{1-\mu_{x}} \hat{p}_{H,t} + \left(1-\nu_{X}\right) \left(\frac{p_{IM}}{p_{DX}}\right)^{1-\mu_{X}} \left(\hat{p}_{IM,t} - \hat{\Gamma}_{IM^{X},t}^{+}\right) \\
&+ \frac{\nu_{X}}{1-\mu_{X}} \left[\left(\frac{p_{H}}{p_{DX}}\right)^{1-\mu_{X}} - \left(\frac{p_{IM}}{p_{DX}}\right)^{1-\mu_{X}}\right] \hat{\nu}_{X,t}
\end{aligned}
\tag{247}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_DX = nu_X_ss*(((p_H_ss)/(p_DX_ss)))^(1 - mu_X)*p_H + (1 - nu_X_ss)*(((p_IM_ss)/(p_DX_ss)))^(1 - mu_X)*(p_IM - Gamma_IMX_p) + (nu_X_ss)/(1 - mu_X)*((((p_H_ss)/(p_DX_ss)))^(1 - mu_X) - (((p_IM_ss)/(p_DX_ss)))^(1 - mu_X))*nu_X
```

Meaning: The domestic price of the exported good is a share-weighted average of the domestic price and the effective import price, plus a home-bias term.

Note: The first term is printed with lower-case $\nu_{x}$ and $\mu_{x}$; all other terms use $\nu_{X}$, $\mu_{X}$.

#### D.5.5 Exports to foreign markets (monopolistic firms)

**Summary.** Monopolistic exporters set prices in foreign currency under Calvo pricing. The block gives the Phillips curve for export-price inflation relative to the foreign inflation objective, exporters' real marginal cost, and the law of motion of the real export price relative to the foreign output deflator.

<!-- kind: eq; id: 248; section: D.5.5; page: 117; pdf_page: 123 -->
**(248) Phillips Curve for the price of the exported good (in foreign currency)**

$$
\begin{aligned}
\hat{\pi}_{X,t} - \hat{\bar{\pi}}_{t}^{*} ={}& \frac{\beta}{1+\beta \chi_{X}} E_{t}\left(\hat{\pi}_{X,t+1} - \hat{\bar{\pi}}_{t+1}^{*}\right) + \frac{\chi_{X}}{1+\beta \chi_{X}} \left[E_{t}\left(\hat{\bar{\pi}}_{t+1}^{*}\right) - \hat{\bar{\pi}}_{t}^{*}\right] \\
&+ \frac{\beta \chi_{X}}{1+\beta \chi_{X}} \left[E_{t}\left(\hat{\bar{\pi}}_{t+1}^{*}\right) - \hat{\bar{\pi}}_{t}^{*}\right] + \frac{\left(1-\beta \xi_{X}\right) \left(1-\xi_{X}\right)}{\left(1+\beta \chi_{X}\right) \xi_{X}} \left(\widehat{mc}_{t}^{X} + \hat{\varphi}_{t}^{X}\right)
\end{aligned}
\tag{248}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pi_X - pibar_star = (beta)/(1 + beta*chi_X)*(pi_X(+1) - pibar_star(+1)) + (chi_X)/(1 + beta*chi_X)*((pibar_star(+1)) - pibar_star) + (beta*chi_X)/(1 + beta*chi_X)*((pibar_star(+1)) - pibar_star) + ((1 - beta*xi_X)*(1 - xi_X))/((1 + beta*chi_X)*xi_X)*(mc_X + varphi_X)
```

Meaning: Export-price inflation relative to the foreign inflation objective depends on its expected value, two terms in the expected change of the objective, and exporters' marginal cost plus a markup shock.

Note: As printed, the second term of the first line repeats the bracket $\left[E_{t}\left(\hat{\bar{\pi}}_{t+1}^{*}\right) - \hat{\bar{\pi}}_{t}^{*}\right]$; in the analogous (226) and (229) this position holds a lagged-inflation term, and the indexation scheme (47) would suggest $\frac{\chi_{X}}{1+\beta \chi_{X}}\left(\hat{\pi}_{X,t-1} - \hat{\bar{\pi}}_{t}^{*}\right)$ (suspected typo).

<!-- kind: eq; id: 249; section: D.5.5; page: 117; pdf_page: 123 -->
**(249) Exporters' real marginal cost (WRT the price of the exported good)**

$$
\widehat{mc}_{t}^{X} = \hat{p}_{DX,t} - \hat{s}_{t} - \hat{p}_{X,t} - \hat{p}_{Y,t}
\tag{249}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
mc_X = p_DX - s - p_X - p_Y
```

Meaning: Exporters' real marginal cost equals the domestic price of the exported good minus the real exchange rate, the real export price and the output deflator term.

<!-- kind: eq; id: 250; section: D.5.5; page: 117; pdf_page: 123 -->
**(250) Real Price of the exported good (foreign currency, WRT foreign output deflator)**

$$
\hat{p}_{X,t} = \hat{\pi}_{X,t} + \hat{p}_{X,t-1} - \hat{\pi}_{Y,t}^{*}
\tag{250}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_X = pi_X + p_X(-1) - pi_Y_star
```

Meaning: The real export price rises with export-price inflation and falls with foreign output-deflator inflation.

### D.6 The Fiscal and Monetary Authorities

**Summary.** This subsection gives the log-linear laws of motion of the exogenous fiscal variables: government consumption and six tax rates, each an AR(1) process. It then gives the output-growth identity and the monetary block. That block is a smoothed Taylor-type rule, an AR(1) inflation target, the real rate and the 5-10-year forward real rate, nominal depreciation, the output-gap measure, and the four-quarter inflation measure the central bank responds to.

<!-- kind: eq; id: 251; section: D.6; page: 117; pdf_page: 123 -->
**(251) Government consumption**

$$
\hat{g}_{t} = \rho_{G} \hat{g}_{t-1} + \eta_{t}^{G}
\tag{251}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
g = rho_G*g(-1) + eta_G
```

Meaning: Government consumption (log deviation) follows a first-order autoregressive process driven by its own innovation.

<!-- kind: eq; id: 252; section: D.6; page: 117; pdf_page: 123 -->
**(252) Direct consumption tax-rate**

$$
\hat{\tau}_{t}^{C} = \rho_{\tau^{C}} \hat{\tau}_{t-1}^{C} + \eta_{t}^{\tau^{C}}
\tag{252}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_C = rho_tauC*tau_C(-1) + eta_tauC
```

Meaning: The consumption tax rate deviation is an AR(1) process with its own persistence parameter and innovation.

<!-- kind: eq; id: 253; section: D.6; page: 117; pdf_page: 123 -->
**(253) Dividend tax**

$$
\hat{\tau}_{t}^{D} = \rho_{\tau^{D}} \hat{\tau}_{t-1}^{D} + \eta_{t}^{\tau^{D}}
\tag{253}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_D = rho_tauD*tau_D(-1) + eta_tauD
```

Meaning: The dividend tax rate deviation follows an AR(1) process with its own persistence parameter and innovation.

<!-- kind: eq; id: 254; section: D.6; page: 118; pdf_page: 124 -->
**(254) Capital rental tax**

$$
\hat{\tau}_{t}^{k} = \rho_{\tau^{K}} \hat{\tau}_{t-1}^{K} + \eta_{t}^{\tau^{K}}
\tag{254}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_K = rho_tauK*tau_K(-1) + eta_tauK
```

Meaning: The capital rental tax rate deviation follows an AR(1) process with its own persistence parameter and innovation.

Note: The left-hand side is printed with a lowercase superscript $k$, while the lag, persistence parameter and innovation use uppercase $K$. This is probably the same variable. It is transcribed as printed.

<!-- kind: eq; id: 255; section: D.6; page: 118; pdf_page: 124 -->
**(255) Income tax on households**

$$
\hat{\tau}_{t}^{N} = \rho_{\tau^{N}} \hat{\tau}_{t-1}^{N} + \eta_{t}^{\tau^{N}}
\tag{255}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_N = rho_tauN*tau_N(-1) + eta_tauN
```

Meaning: The household income-tax rate deviation follows an AR(1) process with its own persistence parameter and innovation.

<!-- kind: eq; id: 256; section: D.6; page: 118; pdf_page: 124 -->
**(256) Additional pay-roll tax on households**

$$
\hat{\tau}_{t}^{W_{h}} = \rho_{\tau^{W_{h}}} \hat{\tau}_{t-1}^{W_{h}} + \eta_{t}^{\tau^{W_{h}}}
\tag{256}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_W_h = rho_tauW_h*tau_W_h(-1) + eta_tauW_h
```

Meaning: The extra payroll tax paid by households follows an AR(1) process with its own persistence parameter and innovation.

<!-- kind: eq; id: 257; section: D.6; page: 118; pdf_page: 124 -->
**(257) Additional pay-roll tax on firms**

$$
\hat{\tau}_{t}^{W_{f}} = \rho_{\tau^{W_{f}}} \hat{\tau}_{t-1}^{W_{f}} + \eta_{t}^{\tau^{W_{f}}}
\tag{257}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_W_f = rho_tauW_f*tau_W_f(-1) + eta_tauW_f
```

Meaning: The extra payroll tax paid by firms follows an AR(1) process with its own persistence parameter and innovation.

<!-- kind: eq; id: 258; section: D.6; page: 118; pdf_page: 124 -->
**(258) Output growth**

$$
\hat{g}_{Y,t} = \hat{g}_{z,t} + \hat{y}_{t} - \hat{y}_{t-1}
\tag{258}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
g_Y = g_z + y - y(-1)
```

Meaning: Output growth (deviation) equals the permanent-technology growth term plus the change in detrended output.

<!-- kind: eq; id: 259; section: D.6; page: 118; pdf_page: 124 -->
**(259) Taylor Rule**

$$
\hat{r}_{t} = \phi_{R} \hat{r}_{t-1} + \left(1-\phi_{R}\right) \left[\hat{\bar{\pi}}_{t} + \hat{rr}_{t}^{fw} + \phi_{\Pi} \left(\hat{\pi}_{t}^{CB} - \bar{\pi}_{t}\right) + \phi_{y} y_{t}^{GAP} + \phi_{\Delta S} \Delta\hat{S}_{t}\right] + \eta_{t}^{R}
\tag{259}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r = phi_R*r(-1) + (1 - phi_R)*(pibar + rr_fw + phi_Pi*(pi_CB - pibar_nohat) + phi_y*y_GAP + phi_DeltaS*dS) + eta_R
```

Meaning: Smoothed Taylor rule: the policy rate responds to the inflation target, the forward real rate, the CB inflation gap, the output gap and nominal depreciation, plus a policy shock.

Note: These details are as printed. The first term in the bracket carries a hat over a bar, $\hat{\bar{\pi}}_{t}$, but the target inside the parentheses is $\bar{\pi}_{t}$ with a bar only. $y_{t}^{GAP}$ has no hat. The narrow hat over "rr" is centred over both letters. The superscript reads $fw$. Main-text (62) prints $\widehat{rr}_{t}^{fwd}$, hat-bar on both target terms, and $\hat{y}_{t}^{GAP}$.

<!-- kind: eq; id: 260; section: D.6; page: 118; pdf_page: 124 -->
**(260) Time-varying inflation objective**

$$
\hat{\bar{\pi}}_{t} = \rho_{\bar{\pi}} \hat{\bar{\pi}}_{t-1} + \eta_{t}^{\bar{\Pi}}
\tag{260}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pibar = rho_barpi*pibar(-1) + eta_Pibar
```

Meaning: The time-varying inflation target is an AR(1) process with persistence parameter indexed by the target and its own innovation.

<!-- kind: eq; id: 261; section: D.6; page: 118; pdf_page: 124 -->
**(261) Real interest rate**

$$
\widehat{ri}_{t} = \hat{r}_{t} - \hat{\pi}_{C,t+1}
\tag{261}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
ri = r - pi_C(+1)
```

Meaning: The real interest rate equals the nominal interest rate minus next-period CPI inflation.

Note: No expectation operator is printed on $\hat{\pi}_{C,t+1}$. The main text (p.26) defines the real rate as $\hat{r}_{t} - E_{t}\hat{\pi}_{C,t+1}$.

<!-- kind: eq; id: 262; section: D.6; page: 118; pdf_page: 124 -->
**(262) Forward 5-10 years expected real interest rate**

$$
\widehat{rr}_{t}^{fw} = \frac{1}{20} E_{t}\left(\hat{ri}_{t+20} + \ldots + \hat{ri}_{t+39}\right)
\tag{262}
$$

Meaning: The forward real rate is the average of the expected one-period real rates from 20 to 39 quarters ahead.

Note: The left-hand side has a wide hat over "rr". The terms inside the parentheses have a narrow hat centred over "ri". The sum runs from $t+20$ to $t+39$, whereas main-text (63) runs from $t+21$ to $t+40$.

<!-- kind: eq; id: 263; section: D.6; page: 118; pdf_page: 124 -->
**(263) Nominal Depreciation**

$$
\Delta\hat{S}_{t} = \hat{s}_{t} - \hat{s}_{t-1} + \hat{\pi}_{Y,t} - \hat{\pi}_{Y,t}^{*}
\tag{263}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
dS = s - s(-1) + pi_Y - pi_Y_star
```

Meaning: Nominal depreciation equals the change in the real exchange rate plus domestic minus foreign output-deflator inflation.

<!-- kind: eq; id: 264; section: D.6; page: 119; pdf_page: 125 -->
**(264) Deviation of production inputs from trend**

$$
y_{t}^{GAP} = \hat{y}_{t} - \hat{\epsilon}_{t}
\tag{264}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
y_GAP = y - epsilon
```

Meaning: The output gap is detrended output minus the transitory technology term.

Note: The symbol is printed as a lunate epsilon $\epsilon$ (with a middle bar), not $\varepsilon$.

<!-- kind: eq; id: 265; section: D.6; page: 119; pdf_page: 125 -->
**(265) The inflation that the CB reacts to**

$$
\hat{\pi}_{t}^{CB} = 0.25 \left[E_{t}\left(\hat{\pi}_{C,t+1}\right) + \hat{\pi}_{C,t} + \hat{\pi}_{C,t-1} + \hat{\pi}_{C,t-2}\right]
\tag{265}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pi_CB = 0.25*((pi_C(+1)) + pi_C + pi_C(-1) + pi_C(-2))
```

Meaning: The central bank's inflation measure averages expected next-quarter CPI inflation with current and two lagged quarterly CPI inflation rates.

Note: The factor 0.25 is printed here. Main-text (65) has the plain sum, without 0.25, inside $E_{t}[\cdot]$.

### D.7 Net Foreign Assets and the Current Account

**Summary.** This subsection log-linearizes the external accounts. It covers the trade balance, the export and import shares of output, the current-account ratio and an AR(1) process for foreign transfers. It then gives the export demand curve, the evolution of the net-foreign-asset ratio, and a relation for the real exchange rate in CPI terms.

<!-- kind: eq; id: 266; section: D.7; page: 119; pdf_page: 125 -->
**(266) Ratio of trade balance to domestic output**

$$
\hat{s}_{TB,t} = \hat{s}_{X,t} - \hat{s}_{IM,t}
\tag{266}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s_TB = s_X - s_IM
```

Meaning: The trade-balance-to-output ratio equals the export ratio minus the import ratio.

<!-- kind: eq; id: 267; section: D.7; page: 119; pdf_page: 125 -->
**(267) Ratio of exports to domestic output**

$$
\hat{s}_{X,t} = \frac{s p_{X} x}{y} \left(\hat{s}_{t} + \hat{p}_{X,t} + \hat{x}_{t} - \hat{y}_{t}\right)
\tag{267}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s_X = (s_ss*p_X_ss*x_ss)/(y_ss)*(s + p_X + x - y)
```

Meaning: The export ratio moves with the real exchange rate, export price and export volume relative to output, scaled by the steady-state export share.

<!-- kind: eq; id: 268; section: D.7; page: 119; pdf_page: 125 -->
**(268) Ratio of imports to domestic output**

$$
\hat{s}_{IM,t} = s_{IM} \left(\hat{p}_{IM,t} + \widehat{im}_{t} - \hat{p}_{Y,t} - \hat{y}_{t}\right)
\tag{268}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s_IM = s_IM_ss*(p_IM + im - p_Y - y)
```

Meaning: The import ratio moves with the import price and import volume relative to the output price and output, scaled by the steady-state import share.

<!-- kind: eq; id: 269; section: D.7; page: 119; pdf_page: 125 -->
**(269) Ratio of current account to domestic output**

$$
\left(CA/Y\right)_{t} = \hat{s}_{TB,t} + \hat{s}_{FTR,t}
\tag{269}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
CA_over_Y = s_TB + s_FTR
```

Meaning: The current-account-to-output ratio equals the trade-balance ratio plus the foreign-transfers ratio.

<!-- kind: eq; id: 270; section: D.7; page: 119; pdf_page: 125 -->
**(270) Ratio of "foreign transfers" to domestic output**

$$
\hat{s}_{FTR,t} = \rho_{FTR} \hat{s}_{FTR,t-1} + \eta_{t}^{FTR}
\tag{270}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s_FTR = rho_FTR*s_FTR(-1) + eta_FTR
```

Meaning: The ratio of foreign transfers to output follows an AR(1) process with its own innovation.

<!-- kind: eq; id: 271; section: D.7; page: 119; pdf_page: 125 -->
**(271) Export demand**

$$
\hat{x}_{t} = \hat{\tilde{z}}_{t} + \widehat{im}_{t}^{*} + \hat{\nu}_{t}^{*} - \mu^{*} \left\{\hat{p}_{x,t} - \hat{p}_{x,t}^{*} + \gamma^{*} \left[\left(\hat{x}_{t} - \widehat{im}_{t}^{*} - \hat{\tilde{z}}_{t}\right) - \left(\hat{x}_{t-1} - \widehat{im}_{t-1}^{*} - \hat{\tilde{z}}_{t-1}\right)\right]\right\}
\tag{271}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
x = ztilde + im_star + nu_star - mu_star*(p_X - p_x_star + gamma_star*((x - im_star - ztilde) - (x(-1) - im_star(-1) - ztilde(-1))))
```

Meaning: Exports rise with relative technology, world imports and a demand shock, and fall with the relative export price and with changes in the scaled export share.

Note: $\hat{\tilde{z}}$ is a hat printed over a tilde. The price subscripts are printed as lowercase $x$.

<!-- kind: eq; id: 272; section: D.7; page: 120; pdf_page: 126 -->
**(272) Ratio of net foreign assets to domestic output**

$$
s_{B_{t+1}^{*}} = r^{*} \left[\left(CA/Y\right)_{t} + \frac{1}{g_{z} \pi^{*}} s_{B_{t}^{*}}\right]
\tag{272}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s_Bstar_nohat(+1) = r_star_ss*(CA_over_Y + (1)/(g_z_ss*pi_star_ss)*s_Bstar_nohat)
```

Meaning: Next period's net-foreign-asset ratio equals the foreign gross rate times the current-account ratio plus the current ratio deflated by technology growth and foreign inflation.

Note: No hats are printed in this equation. The time index sits inside the subscript, as $B_{t+1}^{*}$ and $B_{t}^{*}$.

<!-- kind: eq; id: 273; section: D.7; page: 120; pdf_page: 126 -->
**(273) Real exchange rate in CPI terms**

$$
\hat{s}_{t} = \hat{c}_{t} + \hat{p}_{Y,t}
\tag{273}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
s = c + p_Y
```

Meaning: As printed, the real exchange rate equals the hatted variable $\hat{c}_{t}$ plus the relative output price.

Note: The right-hand side prints $\hat{c}_{t}$, which elsewhere in this chunk (275) is consumption. The same $\hat{c}_{t}$ appears in (282) and (284) where (280) has $\hat{s}_{t}$. The paper's notation here is ambiguous. Transcribed as printed.

### D.8 Market Clearing Conditions

**Summary.** These equations equate supply and demand in the domestic intermediate-goods market, in the final consumption, investment, government and export goods markets, and in the capital market. They also state the aggregate resource constraint at factor cost and at market prices. The remaining equations are the GDP-deflator inflation identity, the output-deflator relation, the composition of total imports, and the definition of real GDP.

<!-- kind: eq; id: 274; section: D.8; page: 120; pdf_page: 126 -->
**(274) Market clearing in the domestic intermediate good markets**

$$
\hat{h}_{t}^{s} = \hat{h}_{t}
\tag{274}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
h_s = h
```

Meaning: The supply of domestic intermediate goods equals their production-relevant aggregate demand.

<!-- kind: eq; id: 275; section: D.8; page: 120; pdf_page: 126 -->
**(275) Market clearing in the final consumption good market**

$$
\hat{q}_{C,t} = \hat{c}_{t}
\tag{275}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
q_C = c
```

Meaning: Output of the final consumption good equals household consumption.

<!-- kind: eq; id: 276; section: D.8; page: 120; pdf_page: 126 -->
**(276) Market clearing in the final investment good market**

$$
\hat{q}_{I,t} = \frac{i}{q^{I}} \hat{\imath}_{t} + \frac{\gamma_{u,1}}{g_{z}} \frac{k}{q^{I}} \hat{u}_{t} + \frac{y}{q^{I}} \left(\hat{\Delta inv}_{t} + \hat{y}_{t} \Delta inv\right)
\tag{276}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
q_I = (i_ss)/(q_I_ss)*i + (gamma_u_1)/(g_z_ss)*(k_ss)/(q_I_ss)*u + (y_ss)/(q_I_ss)*(dinv + y*dinv_ss)
```

Meaning: Output of the final investment good is a share-weighted sum of investment, capital-utilization costs and inventory changes.

Note: Investment $\hat{\imath}_{t}$ is printed as a dotless i with a hat. In $\hat{\Delta inv}_{t}$ a narrow hat is centred over the whole group "$\Delta inv$", whereas (284) prints $\Delta\widehat{inv}_{t}$.

<!-- kind: eq; id: 277; section: D.8; page: 120; pdf_page: 126 -->
**(277) Market clearing in the final government good market**

$$
\hat{q}_{G,t} = \hat{g}_{t}
\tag{277}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
q_G = g
```

Meaning: Output of the final government good equals government consumption.

<!-- kind: eq; id: 278; section: D.8; page: 120; pdf_page: 126 -->
**(278) Market clearing in the final export good market**

$$
\hat{q}_{X,t} = \frac{x}{q^{X}} \hat{x}_{t}
\tag{278}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
q_X = (x_ss)/(q_X_ss)*x
```

Meaning: Production of the final export good moves with exports, scaled by the steady-state ratio of exports to export-good output.

<!-- kind: eq; id: 279; section: D.8; page: 120; pdf_page: 126 -->
**(279) Market clearing in the capital market**

$$
\hat{u}_{t} + \hat{k}_{t} = \hat{k}_{s,t}
\tag{279}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
u + k = k_s
```

Meaning: Capital services used by firms equal the utilization rate times the capital stock (in log deviations).

<!-- kind: eq; id: 280; section: D.8; page: 121; pdf_page: 127 -->
**(280) Aggregate resource constraint**

$$
\begin{aligned}
\hat{p}_{Y,t} + \hat{y}_{t} ={}& \frac{p_{C} c}{p_{y} y} \hat{c}_{t} + \frac{p_{I} i}{P_{y} y} \left(\hat{\imath}_{t} + \hat{p}_{I,t}\right) + \frac{p_{I} k}{p_{y} y} \gamma_{u,1} \hat{u}_{t} + \frac{p_{I}}{P_{Y}} \left(\Delta inv \cdot \hat{y}_{t} + \hat{\Delta inv}_{t} + \Delta inv \cdot \hat{p}_{I,t}\right) \\
&+ \frac{p_{G} g}{p_{Y} g} \left(\hat{p}_{g,t} + \hat{g}_{t}\right) + \frac{s p_{X} x}{y} \left(\hat{x}_{t} + \hat{s}_{t} + \hat{p}_{Y,t} + \hat{p}_{X,t}\right) \\
&- \frac{p_{IM} im_{C}}{p_{Y} y} \left(\hat{p}_{IM,t} + \widehat{im}_{C,t} - \hat{\Gamma}_{IM^{C},t}^{+}\right) - \frac{p_{IM} im_{I}}{p_{Y} y} \left(\hat{p}_{IM,t} + \widehat{im}_{I,t} - \hat{\Gamma}_{IM^{I},t}^{+}\right) \\
&- \frac{p_{IM} im_{G}}{p_{Y} y} \left(\hat{p}_{IM,t} + \widehat{im}_{G,t} - \hat{\Gamma}_{IM^{G},t}^{+}\right) - \frac{p_{IM} im_{X}}{p_{Y} y} \left(\hat{p}_{IM,t} + \widehat{im}_{X,t} - \hat{\Gamma}_{IM^{X},t}^{+}\right)
\end{aligned}
\tag{280}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_Y + y = (p_C_ss*c_ss)/(p_Y_ss*y_ss)*c + (p_I_ss*i_ss)/(p_Y_ss*y_ss)*(i + p_I) + (p_I_ss*k_ss)/(p_Y_ss*y_ss)*gamma_u_1*u + (p_I_ss)/(p_Y_ss)*(dinv_ss*y + dinv + dinv_ss*p_I) + (p_G_ss*g_ss)/(p_Y_ss*g_ss)*(p_G + g) + (s_ss*p_X_ss*x_ss)/(y_ss)*(x + s + p_Y + p_X) - (p_IM_ss*im_C_ss)/(p_Y_ss*y_ss)*(p_IM + im_C - Gamma_IMC_p) - (p_IM_ss*im_I_ss)/(p_Y_ss*y_ss)*(p_IM + im_I - Gamma_IMI_p) - (p_IM_ss*im_G_ss)/(p_Y_ss*y_ss)*(p_IM + im_G - Gamma_IMG_p) - (p_IM_ss*im_X_ss)/(p_Y_ss*y_ss)*(p_IM + im_X - Gamma_IMX_p)
```

Meaning: Nominal output (deflator plus real output) equals share-weighted consumption, investment, utilization and inventory spending, government spending and exports, minus imports adjusted for import-share costs.

Note: Several items are printed exactly so. In line 1 the investment-price term is typeset as a full-size hat over the whole group $p_{I,t}$ (as `\hat{p_{I,t}}` would set it), so the hat sits above the $I$; it is the variable $\hat{p}_{I,t}$ and is transcribed that way (confirmed by glyph metrics in the independent check). In the $\hat{\Gamma}^{+}$ terms the comma before $t$ is raised into the superscript of $IM$ (for the $X$ term the whole ",t" is raised: $IM^{X,t}$); this is layout only, read as $IM^{C},t$, …, $IM^{X},t$. The line-2 denominator is $p_{Y} g$, possibly a typo for $p_{Y} y$. The line-1 denominators use a lowercase subscript $y$ ($p_{y}$, $P_{y}$), and the fourth fraction has $P_{Y}$. The government price term is $\hat{p}_{g,t}$ with a lowercase $g$, where (284) has $\hat{p}_{G,t}$.

<!-- kind: eq; id: 281; section: D.8; page: 121; pdf_page: 127 -->
**(281) Inflation of GDP deflator**

$$
\hat{\pi}_{Y,t} = \hat{\pi}_{C,t} + \hat{p}_{y,t} - \hat{p}_{y,t-1}
\tag{281}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
pi_Y = pi_C + p_Y - p_Y(-1)
```

Meaning: GDP-deflator inflation equals CPI inflation plus the change in the relative output price.

Note: The price subscripts are printed as lowercase $y$ ($\hat{p}_{y,t}$). Elsewhere the relative output price is written $\hat{p}_{Y,t}$.

<!-- kind: eq; id: 282; section: D.8; page: 121; pdf_page: 127 -->
**(282) Output deflator**

$$
\hat{p}_{Y,t} + \hat{y}_{t} = \frac{h p_{H}}{y p_{Y}} \left(\hat{p}_{H,t} + \hat{h}_{t}\right) + \frac{x s p_{X} p_{Y}}{P_{Y} Y} \left(\hat{c}_{t} + \hat{p}_{X,t} + \hat{p}_{Y,t} + \hat{x}_{t}\right) - \frac{p_{DX} q^{X}}{P_{Y} Y} \left(\hat{q}_{X,t} + \hat{p}_{DX,t}\right)
\tag{282}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_Y + y = (h_ss*p_H_ss)/(y_ss*p_Y_ss)*(p_H + h) + (x_ss*s_ss*p_X_ss*p_Y_ss)/(p_Y_ss*y_ss)*(c + p_X + p_Y + x) - (p_DX_ss*q_X_ss)/(p_Y_ss*y_ss)*(q_X + p_DX)
```

Meaning: Nominal output equals the value of domestic intermediate goods plus export revenue minus the domestic cost of the exported good, each share-weighted.

Note: The second term prints $\hat{c}_{t}$ where the analogous term in (280) has $\hat{s}_{t}$; see the note on (273).

<!-- kind: eq; id: 283; section: D.8; page: 121; pdf_page: 127 -->
**(283) Total imported intermediate goods**

$$
\hat{im}_{t} = \frac{im_{C}}{im} \widehat{im}_{C,t} + \frac{im_{I}}{im} \widehat{im}_{I,t} + \frac{im_{G}}{im} \widehat{im}_{G,t} + \frac{im_{X}}{im} \widehat{im}_{X,t}
\tag{283}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im = (im_C_ss)/(im_ss)*im_C + (im_I_ss)/(im_ss)*im_I + (im_G_ss)/(im_ss)*im_G + (im_X_ss)/(im_ss)*im_X
```

Meaning: Total imports are a share-weighted sum of the imports used in the consumption, investment, government and export goods.

Note: The left-hand side has a narrow hat centred over "im". The terms on the right have wide hats.

<!-- kind: eq; id: 284; section: D.8; page: 121; pdf_page: 127 -->
**(284) Aggregate resource constraint in market prices**

$$
\begin{aligned}
\hat{y}_{t} + \hat{p}_{Y,t}^{M} ={}& \frac{\left(1+0.78 \tau_{c}\right) c}{p_{Y}^{M} y} \left(\hat{c}_{t} + \frac{1}{1+0.78 \tau_{c}} \hat{\tau}_{t}^{c}\right) + \frac{p_{I} i}{p_{Y}^{M} y} \left(\hat{\imath}_{t} + \hat{p}_{I,t}\right) + \frac{p_{I} k}{p_{Y}^{M} y} \gamma_{u,1} \hat{u}_{t} \\
&+ \frac{p_{I}}{p_{Y}^{M}} \left(\hat{y}_{t} \Delta inv + \Delta\widehat{inv}_{t} + \hat{p}_{I,t} \Delta inv\right) + \frac{p_{G} g}{p_{Y}^{M} y} \left(\hat{p}_{G,t} + \hat{g}_{t}\right) \\
&+ \frac{x s p_{x} p_{y}}{p_{Y}^{M} y} \left(\hat{x}_{t} + \hat{c}_{t} + \hat{p}_{Y,t} + \hat{p}_{X,t}\right) \\
&- \frac{p_{IM} im_{C}}{p_{Y}^{M} y} \left(\hat{p}_{IM,t} + \widehat{im}_{C,t} - \hat{\Gamma}_{IM^{C},t}^{+}\right) - \frac{P_{IM} im_{I}}{p_{Y}^{M} y} \left(\hat{p}_{IM,t} + \widehat{im}_{I,t} - \hat{\Gamma}_{IM^{I},t}^{+}\right) \\
&- \frac{p_{IM} im_{G}}{y p_{Y}^{M}} \left(\hat{p}_{IM,t} + \widehat{im}_{G,t} - \hat{\Gamma}_{IM^{G},t}^{+}\right) - \frac{P_{IM} im_{X}}{p_{Y}^{M} y} \left(\hat{p}_{IM,t} + \widehat{im}_{X,t} - \hat{\Gamma}_{IM^{X},t}^{+}\right)
\end{aligned}
\tag{284}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
y + p_Y_M = ((1 + 0.78*tau_C_ss)*c_ss)/(p_Y_M_ss*y_ss)*(c + (1)/(1 + 0.78*tau_C_ss)*tau_C) + (p_I_ss*i_ss)/(p_Y_M_ss*y_ss)*(i + p_I) + (p_I_ss*k_ss)/(p_Y_M_ss*y_ss)*gamma_u_1*u + (p_I_ss)/(p_Y_M_ss)*(y*dinv_ss + dinv + p_I*dinv_ss) + (p_G_ss*g_ss)/(p_Y_M_ss*y_ss)*(p_G + g) + (x_ss*s_ss*p_X_ss*p_Y_ss)/(p_Y_M_ss*y_ss)*(x + c + p_Y + p_X) - (p_IM_ss*im_C_ss)/(p_Y_M_ss*y_ss)*(p_IM + im_C - Gamma_IMC_p) - (p_IM_ss*im_I_ss)/(p_Y_M_ss*y_ss)*(p_IM + im_I - Gamma_IMI_p) - (p_IM_ss*im_G_ss)/(y_ss*p_Y_M_ss)*(p_IM + im_G - Gamma_IMG_p) - (p_IM_ss*im_X_ss)/(p_Y_M_ss*y_ss)*(p_IM + im_X - Gamma_IMX_p)
```

Meaning: The resource constraint in market prices: consumption is valued including consumption tax, and nominal output uses the market-price output deflator. The other components are as in (280).

Note: These items are printed exactly so. The consumption tax appears as $\tau_{c}$ and $\hat{\tau}_{t}^{c}$ with a lowercase c, where (252) uses $\hat{\tau}_{t}^{C}$. Two numerators have a capital $P_{IM}$. The line-5 first denominator is ordered $y p_{Y}^{M}$. Line 3 has lowercase subscripts $p_{x} p_{y}$ and $\hat{c}_{t}$ where (280) has $\hat{s}_{t}$. In line 1 the hat on $\hat{p}_{I,t}$ sits slightly to the right, as if over the group $p_{I}$. It is read as $\hat{p}_{I,t}$, the same variable as in line 2.

<!-- kind: eq; id: 285; section: D.8; page: 121; pdf_page: 127 -->
**(285) Real GDP**

$$
\hat{y}_{t} = \hat{h}_{s,t}
\tag{285}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
y = h_s
```

Meaning: Real GDP equals the supply of domestic intermediate goods.

Note: The $s$ is printed as a subscript here, but as a superscript in (274).

### D.9 The Foreign Economy:

**Summary.** The foreign economy is a small closed New-Keynesian block. It has a hybrid IS curve for foreign output, a Taylor-type rule for the annualized foreign nominal rate, and a hybrid Phillips curve for foreign inflation with oil-price terms. A process links world imports to foreign output, and an AR(2)-type law of motion governs the relative foreign price of oil.

<!-- kind: eq; id: 286; section: D.9; page: 122; pdf_page: 128 -->
**(286) Foreign Output**

$$
\hat{y}_{t}^{*} = c_{y^{*},+} E_{t}\left(\hat{y}_{t+1}^{*}\right) + \left(1 - c_{y^{*},+}\right) \hat{y}_{t-1}^{*} - 4c_{y^{*},r} \left(\widehat{ri}_{t}^{*} - \widehat{fw}_{ri^{*},t}\right) + \hat{\epsilon}_{Y^{*},t}
\tag{286}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
y_star = c_ystar_p*(y_star(+1)) + (1 - c_ystar_p)*y_star(-1) - 4*c_ystar_r*(ri_star - fw_ristar) + epsilon_Ystar
```

Meaning: Foreign output depends on its expected and lagged values and falls when the foreign real rate exceeds its forward (natural) level, plus a shock.

Note: The shock is printed with a lunate epsilon. Main-text (89) writes the rate term as $\hat{r}_{t}^{*} - E_{t}\left[\hat{\pi}_{Y,t+1}^{*}\right] - \widehat{rr}_{t}^{*,fwd}$ and the shock as $\varepsilon_{t}^{Y^{*}}$.

<!-- kind: eq; id: 287; section: D.9; page: 122; pdf_page: 128 -->
**(287) Foreign nominal interest rate**

$$
\begin{aligned}
4\hat{r}_{t}^{*} ={}& \\
&\left(1 - c_{r^{*},-}\right) \left(\begin{array}{c} 4 \left(\bar{\pi}_{t}^{*} + \widehat{fw}_{ri^{*},t}\right) \\ +4 c_{r^{*},\pi} \left[0.2 E_{t}\left(\hat{\pi}_{y,t+1}^{*} + \hat{\pi}_{y,t}^{*} + \hat{\pi}_{y,t-1}^{*} + \hat{\pi}_{y,t+2}^{*} + \hat{\pi}_{y,t+3}^{*}\right) - \bar{\pi}_{t}^{*}\right] + c_{r^{*},y} \hat{y}_{t}^{*} \end{array}\right) \\
&+4c_{r^{*},-} \hat{r}_{t-1}^{*} + \hat{\epsilon}_{R^{*},t}
\end{aligned}
\tag{287}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
4*r_star = (1 - c_rstar_m)*(4*(pibar_star_nohat + fw_ristar) + 4*c_rstar_pi*(0.2*(pi_Y_star(+1) + pi_Y_star + pi_Y_star(-1) + pi_Y_star(+2) + pi_Y_star(+3)) - pibar_star_nohat) + c_rstar_y*y_star) + 4*c_rstar_m*r_star(-1) + epsilon_Rstar
```

Meaning: The annualized foreign policy rate smooths toward a level set by the forward natural rate, the inflation target, the five-quarter-average inflation gap and output, plus a shock.

Note: The large parentheses hold two stacked lines that are added together; the second line begins with "+". The foreign target $\bar{\pi}_{t}^{*}$ is printed with a bar only and no hat (main-text (94) has a hat over the bar). The inflation subscripts are printed as lowercase $y$.

<!-- kind: eq; id: 288; section: D.9; page: 122; pdf_page: 128 -->
**(288) Foreign CPI inflation**

$$
\begin{aligned}
4\hat{\pi}_{y,t}^{*} ={}& 4c_{\pi^{*},+} E_{t}\left(\hat{\pi}_{Y,t+1}^{*}\right) + 4\left(1 - c_{\pi^{*},+}\right) \hat{\pi}_{Y,t-1}^{*} + 0.5c_{\pi^{*},y} \left(\hat{y}_{t}^{*} + \hat{y}_{t-1}^{*}\right) \\
&+c_{\pi^{*},OIL} \hat{p}_{OIL,t} + c_{\pi^{*},\Delta OIL} \left(\hat{p}_{OIL,t} - \hat{p}_{OIL,t-2}\right) + \hat{\pi}_{Y,t}^{*}
\end{aligned}
\tag{288}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
4*pi_Y_star = 4*c_pistar_p*(pi_Y_star(+1)) + 4*(1 - c_pistar_p)*pi_Y_star(-1) + 0.5*c_pistar_y*(y_star + y_star(-1)) + c_pistar_OIL*p_OIL + c_pistar_DeltaOIL*(p_OIL - p_OIL(-2)) + pi_Y_star
```

Meaning: Annualized foreign inflation depends on expected and lagged inflation, average current and lagged foreign output, and the oil-price level and two-quarter oil-price change.

Note: The left-hand side has a lowercase $y$ subscript and the right-hand side uses uppercase $Y$. The last term is printed as $+\hat{\pi}_{Y,t}^{*}$, where main-text (92) has the shock $\varepsilon_{t}^{\Pi^{*}}$; this is probably a typo. The oil price has no star here, whereas main-text (92) has $\hat{p}_{OIL,t}^{*}$.

<!-- kind: eq; id: 289; section: D.9; page: 122; pdf_page: 128 -->
**(289) World import gap**

$$
\widehat{im}_{t}^{*} = c_{wt,y} \hat{y}_{t}^{*} + c_{wt,y-} \hat{y}_{t-1}^{*} + c_{wt,-}^{*} \widehat{im}_{t-1}^{*} + \hat{\epsilon}_{IM_{t}^{*}}
\tag{289}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
im_star = c_wt_y*y_star + c_wt_ym*y_star(-1) + c_wt_m_star*im_star(-1) + epsilon_IMstar
```

Meaning: World imports depend on current and lagged foreign output and on their own lag, plus a shock.

Note: The persistence coefficient is printed with a star, $c_{wt,-}^{*}$. The shock subscript carries the time index inside it, as $IM_{t}^{*}$.

<!-- kind: eq; id: 290; section: D.9; page: 122; pdf_page: 128 -->
**(290) Relative foreign price of oil**

$$
\hat{p}_{OILl,t} = c_{OIL,-} \hat{p}_{OIL,t-1} - c_{OIL,\Delta} \left(\hat{p}_{OIL,t-1} - \hat{p}_{OIL,t-2}\right) + \eta_{t}^{OIL}
\tag{290}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
p_OIL = c_OIL_m*p_OIL(-1) - c_OIL_Delta*(p_OIL(-1) - p_OIL(-2)) + eta_OIL
```

Meaning: The relative foreign oil price depends on its own lag and on its lagged change, plus an innovation.

Note: The left-hand-side subscript is printed "OILl" with an extra lowercase l, probably a typo for $OIL$. The change term has a minus sign, $-c_{OIL,\Delta}$, whereas main-text (93) has $+c_{oil,\Delta}$.

### D.10 Observation Equations

**Summary.** This subsection lists the measurement equations that connect each observed data series to the variables of the log-linearized model. Real per-capita quantities enter as quarterly growth rates assembled from the change in the model's detrended log-deviation, the stochastic and steady-state technology growth terms ($\hat{g}_{z,t}$ and $g_{z}-1$), the common hours trend $EX_{\Delta N,t}$ and a series-specific excess trend $EX$. Nominal series add net steady-state inflation ($\pi-1$) and subtract the inflation-target term, matching data that were detrended by the target. Interest rates are annualized (multiplied by 4), and several equations add observation errors, measurement errors or constant term premia.

<!-- kind: eq; id: 291; section: D.10; page: 122; pdf_page: 128 -->
**(291) Real per-capita GDP growth rate**

$$
\Delta Y_{t} = \hat{g}_{z,t} + \hat{y}_{t} - \hat{y}_{t-1} + g_{z} - 1 + EX_{\Delta N,t}
\tag{291}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_Y = g_z + y - y(-1) + g_z_ss - 1 + EX_DeltaN
```

Meaning: Observed per-capita GDP growth: change in the detrended output deviation, plus technology growth (stochastic deviation and steady-state net rate), plus the common hours excess trend $EX_{\Delta N,t}$.

<!-- kind: eq; id: 292; section: D.10; page: 122; pdf_page: 128 -->
**(292) Real per-capita consumption growth rate**

$$
\Delta C_{t} = EX_{\Delta N,t} + g_{z} - 1 + \hat{g}_{z,t} + \hat{c}_{t} - \hat{c}_{t-1} + EX_{\Delta C,t}
\tag{292}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_C = EX_DeltaN + g_z_ss - 1 + g_z + c - c(-1) + EX_DeltaC
```

Meaning: Observed per-capita private consumption growth: hours excess trend, steady-state and stochastic technology growth, change in the detrended consumption deviation, plus a consumption-specific excess trend.

<!-- kind: eq; id: 293; section: D.10; page: 123; pdf_page: 129 -->
**(293) Real per-capita investment growth rate (excluding inventories)**

$$
\Delta I_{NI,t} = EX_{\Delta N,t} + g_{z} - 1 + \hat{g}_{z,t} + \hat{\imath}_{t} - \hat{\imath}_{t-1} + EX_{\Delta INI,t}
\tag{293}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_I_NI = EX_DeltaN + g_z_ss - 1 + g_z + i - i(-1) + EX_DeltaINI
```

Meaning: Observed per-capita fixed-investment growth (inventories excluded): same structure as consumption, using the change in the detrended investment deviation and the investment-specific excess trend $EX_{\Delta INI,t}$.

<!-- kind: eq; id: 294; section: D.10; page: 123; pdf_page: 129 -->
**(294) Real per-capita government consumption growth rate**

$$
\Delta G_{t} = EX_{\Delta N,t} + g_{z} - 1 + \hat{g}_{z,t} + \hat{g}_{t} - \hat{g}_{t-1} + EX_{\Delta G,t}
\tag{294}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_G = EX_DeltaN + g_z_ss - 1 + g_z + g - g(-1) + EX_DeltaG
```

Meaning: Observed per-capita government consumption growth: hours excess trend, technology growth terms, change in the detrended government-consumption deviation, plus the government-specific excess trend.

<!-- kind: eq; id: 295; section: D.10; page: 123; pdf_page: 129 -->
**(295) Real per-capita export growth**

$$
\Delta X_{t} = EX_{\Delta N,t} + g_{z} - 1 + \hat{g}_{z,t} + \hat{x}_{t} - \hat{x}_{t-1} + EX_{\Delta X,t}
\tag{295}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_X = EX_DeltaN + g_z_ss - 1 + g_z + x - x(-1) + EX_DeltaX
```

Meaning: Observed per-capita export growth: hours excess trend, technology growth terms, change in the detrended export deviation, plus an export-specific excess trend.

<!-- kind: eq; id: 296; section: D.10; page: 123; pdf_page: 129 -->
**(296) Real per-capita import growth rate**

$$
\Delta IM_{t} = EX_{\Delta N,t} + g_{z} - 1 + \hat{g}_{z,t} + \widehat{im}_{t} - \widehat{im}_{t-1} + EX_{\Delta IM,t}
\tag{296}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_IM = EX_DeltaN + g_z_ss - 1 + g_z + im - im(-1) + EX_DeltaIM
```

Meaning: Observed per-capita import growth: hours excess trend, technology growth terms, change in the detrended import deviation, plus an import-specific excess trend.

<!-- kind: eq; id: 297; section: D.10; page: 123; pdf_page: 129 -->
**(297) Inflation in market price GDP deflator**

$$
\Delta P_{Y,t}^{M} = \hat{\epsilon}_{OB\_DPY,t} + \hat{\pi}_{C,t} + \hat{p}_{Y,t}^{M} - \hat{p}_{Y,t-1}^{M} + \pi - 1 - \hat{\bar{\pi}}_{t}
\tag{297}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_Y_M = epsilon_OB_DPY + pi_C + p_Y_M - p_Y_M(-1) + pi_ss - 1 - pibar
```

Meaning: Observed inflation of the market-price GDP deflator: an observation error, CPI inflation deviation, change in the relative market-price deflator, net steady-state inflation, minus the inflation-target term.

Note: the target term is printed with a hat over the bar ($\hat{\bar{\pi}}_{t}$), whereas (298), (299), (300) RHS, (304), (305) and (306) print a plain bar ($\bar{\pi}_{t}$). The $t$ in the subscript of $\Delta P$ is set slightly apart and lowered ("Y, t"); this is layout only.

<!-- kind: eq; id: 298; section: D.10; page: 123; pdf_page: 129 -->
**(298) Inflation in factor price CPI (Excluding VAT, fruits and vegetables)**

$$
\Delta P_{C,t} = \hat{\pi}_{C,t} + \pi - 1 - \bar{\pi}_{t}
\tag{298}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_C = pi_C + pi_ss - 1 - pibar_nohat
```

Meaning: Observed CPI inflation (factor prices, excluding VAT, fruit and vegetables): the CPI inflation deviation plus net steady-state inflation, minus the inflation-target term.

<!-- kind: eq; id: 299; section: D.10; page: 123; pdf_page: 129 -->
**(299) Inflation in investment deflator (including a measurement error)**

$$
\Delta P_{I,t} = \pi - 1 + \hat{\pi}_{C,t} + \hat{p}_{I,t} - \hat{p}_{I,t-1} - \bar{\pi}_{t} + \eta_{t}^{\Delta P_{I}}
\tag{299}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_I = pi_ss - 1 + pi_C + p_I - p_I(-1) - pibar_nohat + eta_DeltaP_I
```

Meaning: Observed investment-deflator inflation: net steady-state inflation, CPI inflation deviation, change in the relative investment-goods price, minus the target term, plus a measurement error.

<!-- kind: eq; id: 300; section: D.10; page: 123; pdf_page: 129 -->
**(300) Annualized inflation target**

$$
4\bar{\pi}_{t}^{*} = 4\left(\bar{\pi}_{t} + \pi - 1\right)
\tag{300}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
4*pibar_star_nohat = 4*(pibar_nohat + pi_ss - 1)
```

Meaning: The observed annualized inflation target equals four times the sum of the model's inflation-target term and net steady-state quarterly inflation.

Note: the left-hand side has a full-width overline and a star ($\bar{\pi}_{t}^{*}$, PDF draws a rule), while the right-hand side uses the short bar accent. The right-hand side contains only domestic terms; compare the foreign target $\bar{\pi}_{t}^{*}$ in (318).

<!-- kind: eq; id: 301; section: D.10; page: 123; pdf_page: 129 -->
**(301) Per capita employment (deviation from HP trend)**

$$
\hat{e}_{t} = \frac{\beta}{1+\beta \chi_{E}} E_{t}\left(\hat{e}_{t+1}\right) + \frac{\chi_{E}}{1+\beta \chi_{E}} \hat{e}_{t-1} + \frac{\left(1-\beta \xi_{E}\right)\left(1-\xi_{E}\right)}{\left(1+\beta \chi_{E}\right) \xi_{E}}\left(\hat{n}_{t} - \hat{e}_{t}\right) + \hat{\epsilon}_{OB\_E,t}
\tag{301}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
e = (beta)/(1 + beta*chi_E)*(e(+1)) + (chi_E)/(1 + beta*chi_E)*e(-1) + ((1 - beta*xi_E)*(1 - xi_E))/((1 + beta*chi_E)*xi_E)*(n - e) + epsilon_OB_E
```

Meaning: Employment (deviation from HP trend) adjusts gradually: weighted expected and lagged employment, plus a partial-adjustment term ($\xi_{E}$ plays a Calvo-like role) pulling it toward hours worked, plus an observation shock.

<!-- kind: eq; id: 302; section: D.10; page: 124; pdf_page: 130 -->
**(302) Per capita employment**

$$
\Delta EM_{t} = EX_{\Delta N,t} + \hat{e}_{t} - \hat{e}_{t-1}
\tag{302}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_EM = EX_DeltaN + e - e(-1)
```

Meaning: Observed per-capita employment growth equals the common hours excess trend plus the change in the employment deviation.

<!-- kind: eq; id: 303; section: D.10; page: 124; pdf_page: 130 -->
**(303) Per capita labor input**

$$
\Delta N_{t} = EX_{\Delta N,t} + \hat{n}_{t} - \hat{n}_{t-1}
\tag{303}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_N = EX_DeltaN + n - n(-1)
```

Meaning: Observed growth of per-capita hours worked (labor input) equals the common hours excess trend plus the change in the hours deviation.

<!-- kind: eq; id: 304; section: D.10; page: 124; pdf_page: 130 -->
**(304) Nominal wage growth rate**

$$
\Delta W_{t} = \pi - 1 + g_{z} - 1 + \hat{\pi}_{C,t} + \hat{g}_{z,t} + \hat{w}_{t} - \hat{w}_{t-1} - \bar{\pi}_{t} + EX_{\Delta W,t}
\tag{304}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_W = pi_ss - 1 + g_z_ss - 1 + pi_C + g_z + w - w(-1) - pibar_nohat + EX_DeltaW
```

Meaning: Observed nominal hourly wage growth: net steady-state inflation and technology growth, CPI-inflation and technology-growth deviations, change in the real-wage deviation, minus the target term, plus a wage excess trend.

<!-- kind: eq; id: 305; section: D.10; page: 124; pdf_page: 130 -->
**(305) Annualized nominal interest rate**

$$
r_{t}^{OB} = 4\left(\hat{r}_{t} + r - 1\right) - 4\bar{\pi}_{t}
\tag{305}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r_OB = 4*(r + R_ss - 1) - 4*pibar_nohat
```

Meaning: The observed annualized Bank of Israel rate equals four times the model's net quarterly nominal rate (deviation plus steady state) minus four times the inflation-target term.

<!-- kind: eq; id: 306; section: D.10; page: 124; pdf_page: 130 -->
**(306) Nominal depreciation rate**

$$
\Delta S_{t} = \hat{c}_{t} - \hat{c}_{t-1} + \hat{\pi}_{Y,t} - \hat{\pi}_{Y,t}^{*} + \pi - 1 - \left(\pi^{*} - 1\right) - \bar{\pi}_{t} + EX_{\Delta S,t}
\tag{306}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_S = c - c(-1) + pi_Y - pi_Y_star + pi_ss - 1 - (pi_star_ss - 1) - pibar_nohat + EX_DeltaS
```

Meaning: Observed nominal depreciation: change in $\hat{c}$ (as printed), domestic minus foreign inflation deviations, domestic minus foreign net steady-state inflation, minus the target term, plus an excess trend.

Note: suspected typo. The paper prints $\hat{c}_{t}-\hat{c}_{t-1}$ (zoomed and checked against the PDF glyphs: it is $c$), but the nominal-depreciation identity (263) and Appendix B eq. (105) use the real exchange rate change $\hat{s}_{t}-\hat{s}_{t-1}$. Transcribed as printed.

<!-- kind: eq; id: 307; section: D.10; page: 124; pdf_page: 130 -->
**(307) Foreign output growth rate**

$$
\Delta {Y^{*}}_{t} = g_{z} - 1 + \hat{g}_{z,t} + \hat{\tilde{z}}_{t} + \hat{y}_{t}^{*} - \hat{y}_{t-1}^{*} - \hat{\tilde{z}}_{t-1} + EX_{\Delta Y*,t}
\tag{307}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_Y_star = g_z_ss - 1 + g_z + ztilde + y_star - y_star(-1) - ztilde(-1) + EX_DeltaYstar
```

Meaning: Observed foreign (G4) GDP growth: technology growth terms, change in the relative technology level, change in the foreign output deviation, plus a foreign-output excess trend.

Note: the left-hand subscript $t$ is printed after the star (same series as $\Delta Y_{t}^{*}$ in the data list). In $EX_{\Delta Y*,t}$ the asterisk is printed inline at subscript size, not raised. $\hat{\tilde{z}}$ is a hat over a tilde.

<!-- kind: eq; id: 308; section: D.10; page: 124; pdf_page: 130 -->
**(308) Inflation in foreign price deflator**

$$
\Delta P_{Y^{*},t} = \hat{\pi}_{Y,t}^{*} + \pi^{*} - 1
\tag{308}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_Ystar = pi_Y_star + pi_star_ss - 1
```

Meaning: Observed foreign price inflation (G4 CPI) equals the foreign inflation deviation plus net foreign steady-state inflation.

<!-- kind: eq; id: 309; section: D.10; page: 124; pdf_page: 130 -->
**(309) Annualized foreign nominal interest rate**

$$
R_{t}^{*OB} = 4\left(\hat{r}_{t}^{*} + r^{*} - 1\right)
\tag{309}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
R_starOB = 4*(r_star + r_star_ss - 1)
```

Meaning: The observed annualized foreign (G4) nominal interest rate equals four times the model's net quarterly foreign rate (deviation plus steady state).

<!-- kind: eq; id: 310; section: D.10; page: 124; pdf_page: 130 -->
**(310) Inflation in foreign competitors price**

$$
\Delta P_{X^{*},t} = \Delta P_{Y^{*},t} + \hat{p}_{x,t}^{*} - \hat{p}_{x,t-1}^{*}
\tag{310}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_Xstar = Delta_P_Ystar + p_x_star - p_x_star(-1)
```

Meaning: Inflation of foreign competitors' prices equals observed foreign price inflation plus the change in the competitors' relative price.

<!-- kind: eq; id: 311; section: D.10; page: 124; pdf_page: 130 -->
**(311) Inflation in export deflator (NIS terms)**

$$
\Delta P_{X,t}^{NIS} = \Delta S_{t} + \Delta P_{Y^{*},t} + \hat{p}_{x,t} - \hat{p}_{x,t-1}
\tag{311}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_X_NIS = Delta_S + Delta_P_Ystar + p_X - p_X(-1)
```

Meaning: Export-deflator inflation in shekel (NIS) terms equals nominal depreciation plus foreign price inflation plus the change in the relative export price.

<!-- kind: eq; id: 312; section: D.10; page: 125; pdf_page: 131 -->
**(312) Forward long run expected real rate (5-10 years)**

$$
rr_{t}^{fwd\_ob} = \hat{\epsilon}_{fwd\_ob,t} + 4\left(\hat{fw}_{ri^{*},t} + \frac{g_{z}}{\beta} - 1\right) + tp
\tag{312}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
rr_fwd_ob = epsilon_fwd_ob + 4*(fw_ristar + (g_z_ss)/(beta) - 1) + tp
```

Meaning: Observed domestic 5-10 year forward real rate: observation error plus four times (forward real-rate term plus net steady-state real rate $g_{z}/\beta-1$) plus a constant term premium.

Note: a narrow hat is printed centred over the pair "fw" (PDF glyph positions put the hat at the centre of the two-letter group), i.e. $\hat{fw}$; (286) and (318) print the same symbol with a wide hat, $\widehat{fw}_{ri^{*},t}$.

<!-- kind: inline; id: 312.i1; section: D.10; page: 125; pdf_page: 131 -->
**(312.i1) Domestic average term premium (text after (312))**

$$
tp
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tp
```

Meaning: $tp$ is a constant average term premium in the domestic forward-rate observation equation.

<!-- kind: eq; id: 313; section: D.10; page: 125; pdf_page: 131 -->
**(313) Observable ratio of Current Account to GDP**

$$
S_{CA,t} = \left(CA/Y\right)_{t}
\tag{313}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
S_CA = CA_over_Y
```

Meaning: The observed current-account-to-GDP ratio equals the model's current-account-to-GDP ratio.

<!-- kind: eq; id: 314; section: D.10; page: 125; pdf_page: 131 -->
**(314) Observable consumption tax rate**

$$
\tau_{t}^{C\_OB} = \tau_{c} + \hat{\tau}_{t}^{c}
\tag{314}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_C_OB = tau_C_ss + tau_C
```

Meaning: The observed consumption (VAT) tax rate equals its steady-state level plus the model's tax-rate deviation.

<!-- kind: eq; id: 315; section: D.10; page: 125; pdf_page: 131 -->
**(315) Observable income tax rate**

$$
\tau_{t}^{N\_OB} = \tau_{n} + \hat{\tau}_{t}^{n}
\tag{315}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tau_N_OB = tau_N_ss + tau_N
```

Meaning: The observed income tax rate equals its steady-state level plus the model's tax-rate deviation.

<!-- kind: eq; id: 316; section: D.10; page: 125; pdf_page: 131 -->
**(316) Observable change in oil prices**

$$
\Delta P_{OIL,t} = \hat{p}_{OIL,t} - \hat{p}_{OIL,t-1} + \Delta P_{Y^{*},t} + EX_{\Delta POIL,t}
\tag{316}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_P_OIL = p_OIL - p_OIL(-1) + Delta_P_Ystar + EX_DeltaPOIL
```

Meaning: Observed oil-price change equals the change in the relative oil price plus observed foreign price inflation plus an oil-specific excess trend.

<!-- kind: eq; id: 317; section: D.10; page: 125; pdf_page: 131 -->
**(317) The change in inventories, as a share of GDP**

$$
\Delta inv_{t} = \Delta \widehat{inv}_{t} + \Delta inv + EX_{\Delta INV,t}
\tag{317}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_inv = dinv + dinv_ss + EX_DeltaINV
```

Meaning: The observed change in inventories as a share of GDP equals the model deviation plus its steady-state share plus an excess term.

Note: the wide hat covers "inv" only, not the $\Delta$. $\Delta inv$ without a time index is the steady-state share.

<!-- kind: eq; id: 318; section: D.10; page: 125; pdf_page: 131 -->
**(318) Forward long run expected nominal rate abroad (5-10 years)**

$$
r_{t}^{*fwd\_ob} = \hat{\epsilon}_{fwd\_ob^{*},t} + 4\left(\bar{\pi}_{t}^{*} + \widehat{fw}_{ri^{*},t} + r^{*} - 1\right) + tp^{*}
\tag{318}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
r_starfwd_ob = epsilon_fwd_obstar + 4*(pibar_star_nohat + fw_ristar + r_star_ss - 1) + tp_star
```

Meaning: Observed foreign 5-10 year forward nominal rate: observation error plus four times (foreign target, forward real-rate term, net steady-state foreign nominal rate) plus a foreign term premium.

<!-- kind: inline; id: 318.i1; section: D.10; page: 125; pdf_page: 131 -->
**(318.i1) Foreign average term premium (text after (318))**

$$
tp*
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
tp_star
```

Meaning: $tp*$ (written $tp^{*}$ in (318)) is the constant average term premium in the foreign forward-rate observation equation.

Note: in the sentence the asterisk is printed inline at full size, not as a superscript.

<!-- kind: eq; id: 319; section: D.10; page: 125; pdf_page: 131 -->
**(319) Observable world import growth rate**

$$
\Delta WT_{t}^{*} = \hat{g}_{z,t} + \hat{\tilde{z}}_{t} + \widehat{im}_{t}^{*} - \widehat{im}_{t-1}^{*} - \hat{\tilde{z}}_{t-1} + g_{z} - 1 + EX_{\Delta WT*,t}
\tag{319}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
Delta_WT_star = g_z + ztilde + im_star - im_star(-1) - ztilde(-1) + g_z_ss - 1 + EX_DeltaWTstar
```

Meaning: Observed world (OECD) import growth: technology growth terms, change in the relative technology level, change in the world import gap, plus a world-trade excess trend.

Note: in $EX_{\Delta WT*,t}$ the asterisk is printed inline at subscript size; on the left-hand side the star is a raised superscript.

### D.11 AR(1) processes of the idiosyncratic trend shocks

**Summary.** This subsection gives the laws of motion of the excess-trend terms $EX$ that appear in the observation equations of D.10. Most are AR(1) processes whose unconditional mean equals the component's long-run excess growth: its assumed growth rate net of technology growth and, for the domestic real components, net of hours growth. The depreciation and oil terms have zero mean and the inventory term is white noise. Equation (328) is an adding-up restriction on the share-weighted excess trends; it leaves the government-consumption term $EX_{\Delta G,t}$ (which has no process of its own) determined residually.

<!-- kind: eq; id: 320; section: D.11; page: 126; pdf_page: 132 -->
**(320) Excess trend in nominal depreciation**

$$
EX_{\Delta S,t} = \rho_{EX}^{\Delta S} EX_{\Delta S,t-1} + \eta_{EX,t}^{S}
\tag{320}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaS = rho_EX_DeltaS*EX_DeltaS(-1) + eta_EX_S
```

Meaning: AR(1) process for the excess trend in nominal depreciation, with zero mean, coefficient $\rho_{EX}^{\Delta S}$ and innovation $\eta_{EX,t}^{S}$.

Note: the coefficient superscript is $\Delta S$ but the innovation superscript is $S$ (as printed). Appendix B (text after eq. 105) calls $EX^{S}$ an i.i.d. innovation, and Table 3 lists no AR coefficient for it (only the S.D. of $\eta_{EX}^{S}$); $\rho_{EX}^{\Delta S}$ may therefore be fixed at 0 in estimation.

<!-- kind: eq; id: 321; section: D.11; page: 126; pdf_page: 132 -->
**(321) Excess trend in nominal wage growth**

$$
EX_{\Delta W,t} = \left(1 - \rho_{EX}^{\Delta W}\right)\left(g_{\Delta W} - g_{z} + 1 - \pi\right) + \rho_{EX}^{\Delta W} EX_{\Delta W,t-1} + \eta_{EX,t}^{W}
\tag{321}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaW = (1 - rho_EX_DeltaW)*(g_DeltaW - g_z_ss + 1 - pi_ss) + rho_EX_DeltaW*EX_DeltaW(-1) + eta_EX_W
```

Meaning: AR(1) process for the wage excess trend, whose mean is long-run nominal wage growth in excess of technology growth and steady-state inflation.

Note: Appendix B (text after eq. 106) calls $EX^{W}$ an i.i.d. innovation, and Table 3 lists no AR coefficient for it (only the S.D. of $\eta_{EX}^{W}$); $\rho_{EX}^{\Delta W}$ may therefore be fixed at 0 in estimation. The innovation superscript is $W$, not $\Delta W$ (as printed).

<!-- kind: eq; id: 322; section: D.11; page: 126; pdf_page: 132 -->
**(322) Common excess trend in hours (labor input) growth**

$$
EX_{\Delta N,t} = \left(1 - \rho_{EX}^{N}\right) g_{\Delta N} + \rho_{EX}^{N} EX_{\Delta N,t-1} + \eta_{EX,t}^{N}
\tag{322}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaN = (1 - rho_EX_N)*g_DeltaN + rho_EX_N*EX_DeltaN(-1) + eta_EX_N
```

Meaning: AR(1) process for the common hours trend, with mean $g_{\Delta N}$, the long-run growth of per-capita hours.

<!-- kind: eq; id: 323; section: D.11; page: 126; pdf_page: 132 -->
**(323) Excess trend in consumption growth**

$$
EX_{\Delta C,t} = \left(1 - \rho_{EX}^{C}\right)\left(g_{\Delta C} - g_{z} - g_{\Delta N}\right) + \rho_{EX}^{C} EX_{\Delta C,t-1} + \eta_{EX,t}^{C}
\tag{323}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaC = (1 - rho_EX_C)*(g_DeltaC - g_z_ss - g_DeltaN) + rho_EX_C*EX_DeltaC(-1) + eta_EX_C
```

Meaning: AR(1) process for the consumption excess trend, whose mean is long-run consumption growth in excess of technology and hours growth.

<!-- kind: eq; id: 324; section: D.11; page: 126; pdf_page: 132 -->
**(324) Excess trend in fixed-investment growth**

$$
EX_{\Delta INI,t} = \left(1 - \rho_{EX}^{I}\right)\left(g_{\Delta I} - g_{z} - g_{\Delta N}\right) + \rho_{EX}^{I} EX_{\Delta INI,t-1} + \eta_{EX,t}^{I}
\tag{324}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaINI = (1 - rho_EX_I)*(g_DeltaI - g_z_ss - g_DeltaN) + rho_EX_I*EX_DeltaINI(-1) + eta_EX_I
```

Meaning: AR(1) process for the fixed-investment excess trend, whose mean is long-run investment growth in excess of technology and hours growth.

<!-- kind: eq; id: 325; section: D.11; page: 126; pdf_page: 132 -->
**(325) Excess trend in import growth**

$$
EX_{\Delta IM,t} = \left(1 - \rho_{EX}^{IM}\right)\left(g_{\Delta IM} - g_{z} - g_{\Delta N}\right) + \rho_{EX}^{IM} EX_{\Delta IM,t-1} + \eta_{EX,t}^{IM}
\tag{325}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaIM = (1 - rho_EX_IM)*(g_DeltaIM - g_z_ss - g_DeltaN) + rho_EX_IM*EX_DeltaIM(-1) + eta_EX_IM
```

Meaning: AR(1) process for the import excess trend, whose mean is long-run import growth in excess of technology and hours growth.

<!-- kind: eq; id: 326; section: D.11; page: 126; pdf_page: 132 -->
**(326) Excess trend in export growth**

$$
EX_{\Delta X,t} = \left(1 - \rho_{EX}^{X}\right)\left(g_{\Delta X} - g_{z} - g_{\Delta N}\right) + \rho_{EX}^{X} EX_{\Delta X,t-1} + \eta_{EX,t}^{X}
\tag{326}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaX = (1 - rho_EX_X)*(g_DeltaX - g_z_ss - g_DeltaN) + rho_EX_X*EX_DeltaX(-1) + eta_EX_X
```

Meaning: AR(1) process for the export excess trend, whose mean is long-run export growth in excess of technology and hours growth.

<!-- kind: eq; id: 327; section: D.11; page: 126; pdf_page: 132 -->
**(327) Excess term in the inventory share**

$$
EX_{\Delta INV,t} = \eta_{EX,t}^{\Delta INV}
\tag{327}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaINV = eta_EX_DeltaINV
```

Meaning: The excess term in the inventory-change share is white noise (an i.i.d. innovation).

<!-- kind: eq; id: 328; section: D.11; page: 126; pdf_page: 132 -->
**(328) Adding-up restriction on the excess trends (determines the government term)**

$$
0 = \frac{c}{y} EX_{\Delta C,t} + \frac{i}{y} EX_{\Delta INI,t} + \Delta inv EX_{\Delta INV,t} + s_{G} EX_{\Delta G,t} + s_{X} EX_{\Delta X,t} - \frac{im}{y} EX_{\Delta IM,t}
\tag{328}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
0 = (c_ss)/(y_ss)*EX_DeltaC + (i_ss)/(y_ss)*EX_DeltaINI + dinv_ss*EX_DeltaINV + s_G*EX_DeltaG + s_X_ss*EX_DeltaX - (im_ss)/(y_ss)*EX_DeltaIM
```

Meaning: The GDP-share-weighted excess trends of consumption, investment, inventories, government consumption and exports, less imports, sum to zero; this pins down $EX_{\Delta G,t}$.

Note: $\Delta inv$ (the steady-state inventory share) multiplies $EX_{\Delta INV,t}$.

<!-- kind: eq; id: 329; section: D.11; page: 126; pdf_page: 132 -->
**(329) Excess trend in foreign output growth**

$$
EX_{\Delta Y*,t} = \left(1 - \rho_{EX}^{Y^{*}}\right)\left(g_{\Delta Y^{*}} - g_{z}\right) + \rho_{EX}^{Y^{*}} EX_{\Delta Y*,t-1} + \eta_{EX,t}^{Y^{*}}
\tag{329}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaYstar = (1 - rho_EX_Ystar)*(g_DeltaYstar - g_z_ss) + rho_EX_Ystar*EX_DeltaYstar(-1) + eta_EX_Ystar
```

Meaning: AR(1) process for the foreign-output excess trend, whose mean is long-run foreign output growth in excess of technology growth.

Note: in both $EX$ subscripts the asterisk is printed inline at subscript size; in $\rho$, $g$ and $\eta$ it is a raised superscript on $Y$.

<!-- kind: eq; id: 330; section: D.11; page: 126; pdf_page: 132 -->
**(330) Excess trend in world import growth**

$$
EX_{\Delta WT*,t} = \left(1 - \rho_{EX}^{WT^{*}}\right)\left(g_{\Delta WT*} - g_{z}\right) + \rho_{EX}^{WT^{*}} EX_{\Delta WT*,t-1} + \eta_{EX,t}^{WT^{*}}
\tag{330}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaWTstar = (1 - rho_EX_WTstar)*(g_DeltaWTstar - g_z_ss) + rho_EX_WTstar*EX_DeltaWTstar(-1) + eta_EX_WTstar
```

Meaning: AR(1) process for the world-import excess trend, whose mean is long-run world import growth in excess of technology growth.

Note: the asterisk is printed inline at subscript size in the $EX$ subscripts and in $g_{\Delta WT*}$; it is a raised superscript in $\rho$ and $\eta$.

<!-- kind: eq; id: 331; section: D.11; page: 126; pdf_page: 132 -->
**(331) Excess trend in oil-price change**

$$
EX_{\Delta POil,t} = \rho_{EX}^{P_{OIL}^{*}} EX_{\Delta POil,t-1} + \eta_{EX,t}^{P_{OIL}^{*}}
\tag{331}
$$

Code form (derived from the LaTeX above; LaTeX is authoritative):
```text
EX_DeltaPOIL = rho_EX_P_OILstar*EX_DeltaPOIL(-1) + eta_EX_P_OILstar
```

Meaning: AR(1) process with zero mean for the excess trend in oil-price changes.

Note: the subscript is printed "$\Delta POil$" (lowercase i, l), whereas (316) prints $EX_{\Delta POIL,t}$; presumably the same term.
