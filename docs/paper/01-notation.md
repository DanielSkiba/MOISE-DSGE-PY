# Notation

> Part of the **MOISE agent edition**: an AI-readable restatement of Argov, Barnea, Binyamini, Borenstein, Elkayam & Rozenshtrom (2012), *MOISE: A DSGE Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. Not affiliated with or endorsed by the Bank of Israel. Equations, numbers and notation are transcribed from the paper; explanations are paraphrased. Conventions and verification status: [README](README.md).

Two tables. **Part A** lists every symbol that appears in the log-linearized model (Appendix D, `10-log-linear-model.md`) with the code name used in the code forms; implementers should use these names. **Part B** lists every symbol that the transcribers recorded anywhere in the paper, with its meaning as defined there. Machine-readable versions: `data/notation_codes.csv`, `data/notation_all.csv`.

Conventions in Appendix D: a hat marks a log deviation from the steady state; a symbol with the same letters but no hat and no time index is a steady-state value (code name ends in `_ss`); `*` marks foreign variables or parameters (`_star`). Where the paper writes the same object in two ways, the code forms keep two names (suffix `_nohat`) and the pair is listed under Known issues in the README. Obvious printed variants of a standard symbol (lower-case subscripts, a missing comma, a stray letter) share the standard symbol's code name; each such mapping and its reason is in `data/notation_aliases.csv`. The LaTeX always stays as printed.

## Part A: symbols of the log-linearized model and their code names

| Code name | LaTeX | Kind | Meaning | Has time index | First used in |
|---|---|---|---|---|---|
| `alpha` | $\alpha$ | parameter | capital share in production | no | (222) |
| `beta` | $\beta$ | parameter | household discount factor | no | (213) |
| `beta_star` | $\beta^{*}$ | parameter | foreign discount factor | no | (229) |
| `c` | $\hat{c}$ | endogenous | private consumption (detrended), log deviation | yes | (212) |
| `c_OIL_Delta` | $c_{OIL,\Delta}$ | parameter | oil price lagged-change coefficient | no | (290) |
| `c_OIL_m` | $c_{OIL,-}$ | parameter | oil price persistence coefficient | no | (290) |
| `c_pistar_DeltaOIL` | $c_{\pi^{*},\Delta OIL}$ | parameter | foreign Phillips curve oil-price change coefficient | no | (288) |
| `c_pistar_OIL` | $c_{\pi^{*},OIL}$ | parameter | foreign Phillips curve oil-price level coefficient | no | (288) |
| `c_pistar_p` | $c_{\pi^{*},+}$ | parameter | forward-looking weight in foreign Phillips curve | no | (288) |
| `c_pistar_y` | $c_{\pi^{*},y}$ | parameter | foreign Phillips curve output coefficient | no | (288) |
| `c_rstar_m` | $c_{r^{*},-}$ | parameter | foreign interest-rate smoothing coefficient | no | (287) |
| `c_rstar_pi` | $c_{r^{*},\pi}$ | parameter | foreign policy response to inflation gap | no | (287) |
| `c_rstar_y` | $c_{r^{*},y}$ | parameter | foreign policy response to output | no | (287) |
| `c_ss` | $c$ | steady_state | steady-state consumption | no | (280) |
| `c_wt_m_star` | $c_{wt,-}^{*}$ | parameter | world imports persistence | no | (289) |
| `c_wt_y` | $c_{wt,y}$ | parameter | world imports response to current foreign output | no | (289) |
| `c_wt_ym` | $c_{wt,y-}$ | parameter | world imports response to lagged foreign output | no | (289) |
| `c_ystar_p` | $c_{y^{*},+}$ | parameter | forward-looking weight in foreign IS curve | no | (286) |
| `c_ystar_r` | $c_{y^{*},r}$ | parameter | foreign IS curve real-rate sensitivity | no | (286) |
| `CA` | $CA$ | other | current account surplus (nominal) | no | (269) |
| `CA_over_Y` | $(CA/Y)$ | endogenous | model current-account-to-GDP ratio | yes | (269) |
| `chi_E` | $\chi_{E}$ | parameter | persistence parameter of employment dynamics | no | (301) |
| `chi_H` | $\chi_{H}$ | parameter | price indexation of domestic intermediate goods firms | no | (226) |
| `chi_star` | $\chi^{*}$ | parameter | price indexation of foreign intermediate-goods firms | no | (229) |
| `chi_W` | $\chi_{W}$ | parameter | wage indexation to past CPI inflation | no | (221) |
| `chi_W_g_z` | $\chi_{W,g_{z}}$ | parameter | wage indexation to past productivity growth | no | (221) |
| `chi_X` | $\chi_{X}$ | parameter | price indexation of exporters | no | (248) |
| `delta` | $\delta$ | parameter | capital depreciation rate | no | (213) |
| `Delta_C` | $\Delta{C}$ | observable | per capita real private consumption growth | yes | (292) |
| `Delta_EM` | $\Delta{EM}$ | observable | growth of employees per working-age person | yes | (302) |
| `Delta_G` | $\Delta{G}$ | observable | per capita government consumption growth (excl. defence imports) | yes | (294) |
| `Delta_I_NI` | $\Delta{I_{NI}}$ | observable | observed real per-capita fixed investment growth (excluding inventories) | yes | (293) |
| `Delta_IM` | $\Delta{IM}$ | observable | per capita imports growth (excl. defence, ships, aircraft, diamonds) | yes | (296) |
| `Delta_inv` | $\Delta inv_{t}$ | observable | observed change in inventories as a share of GDP (the symbol with a time index) | yes | (317) |
| `Delta_N` | $\Delta{N}$ | observable | growth of hours worked per working-age person | yes | (303) |
| `Delta_P_C` | $\Delta{P_{C}}$ | observable | CPI inflation (excl. fruit/vegetables; housing excl. 1992-2006), VAT changes deducted | yes | (298) |
| `Delta_P_I` | $\Delta{P_{I}}$ | observable | observed investment-deflator inflation | yes | (299) |
| `Delta_P_OIL` | $\Delta{P_{OIL}}$ | observable | observed change in oil prices | yes | (316) |
| `Delta_P_X_NIS` | $\Delta{P_{X}^{NIS}}$ | observable | export deflator inflation in domestic currency (NIS) | yes | (311) |
| `Delta_P_Xstar` | $\Delta{P_{X^{*}}}$ | observable | inflation in foreign competitors' price | yes | (310) |
| `Delta_P_Y_M` | $\Delta{P_{Y}^{M}}$ | observable | GDP deflator inflation, market prices | yes | (297) |
| `Delta_P_Ystar` | $\Delta{P_{Y^{*}}}$ | observable | observed foreign price inflation (G4 CPI) | yes | (308) |
| `Delta_S` | $\Delta{S}$ | endogenous | nominal depreciation | yes | (306) |
| `Delta_W` | $\Delta{W}$ | observable | nominal hourly wage growth | yes | (304) |
| `Delta_WT_star` | $\Delta{WT^{*}}$ | observable | OECD import volume growth (world trade) | yes | (319) |
| `Delta_X` | $\Delta{X}$ | observable | per capita exports growth (excl. diamonds, start-ups) | yes | (295) |
| `Delta_Y` | $\Delta{Y}$ | observable | per capita real GDP growth (observed) | yes | (291) |
| `Delta_Y_star` | $\Delta{Y^{*}}$ | observable | G4 real GDP growth (weighted) | yes | (307) |
| `dinv` | $\Delta{\widehat{inv}}$ | endogenous | change in inventories (share of GDP), model deviation | yes | (284) |
| `dinv` | $\hat{\Delta inv}$ | shock_process | inventory investment (share of GDP), deviation | yes | (276) |
| `dinv_ss` | $\Delta{inv}$ | steady_state | steady-state inventory-change share of GDP | yes | (276) |
| `dS` | $\Delta{\hat{S}}$ | endogenous | nominal depreciation of the shekel, deviation (policy rule (259)) | yes | (259) |
| `e` | $\hat{e}$ | endogenous | per-capita employment, deviation from HP trend | yes | (301) |
| `epsilon` | $\hat{\epsilon}$ | shock_process | transitory technology shock | yes | (222) |
| `epsilon_C` | $\hat{\epsilon}^{C}$ | shock_process | consumption-demand (preference) shock | yes | (212) |
| `epsilon_DRP` | $\hat{\epsilon}^{DRP}$ | shock_process | domestic, highly inertial risk-premium shock | yes | (216) |
| `epsilon_F` | $\hat{\epsilon}^{F}$ | shock_process | shock in working-capital interest rate | yes | (225) |
| `epsilon_fwd_ob` | $\hat{\epsilon}_{fwd\_ob}$ | shock_process | observation error in the domestic forward real rate | yes | (312) |
| `epsilon_fwd_obstar` | $\hat{\epsilon}_{fwd\_ob^{*}}$ | shock_process | observation error in the foreign forward nominal rate | yes | (318) |
| `epsilon_I` | $\hat{\epsilon}^{I}$ | shock_process | investment-specific technology shock | yes | (214) |
| `epsilon_IM` | $\hat{\epsilon}^{IM}$ | shock_process | import demand shock (productivity of imported inputs) | yes | (234) |
| `epsilon_IMstar` | $\hat{\epsilon}_{IM^{*}}$ | innovation | world import (trade) shock | yes | (289) |
| `epsilon_N` | $\hat{\epsilon}_{N}$ | shock_process | labor-supply shock | yes | (220) |
| `epsilon_OB_DPY` | $\hat{\epsilon}_{OB\_DPY}$ | shock_process | observation error in GDP-deflator inflation | yes | (297) |
| `epsilon_OB_E` | $\hat{\epsilon}_{OB\_E}$ | shock_process | observation shock in the employment equation | yes | (301) |
| `epsilon_RP` | $\hat{\epsilon}^{RP}$ | shock_process | symmetric (common) risk-premium shock | yes | (216) |
| `epsilon_RPstar` | $\hat{\epsilon}^{RP^{*}}$ | shock_process | external risk-premium shock | yes | (217) |
| `epsilon_Rstar` | $\hat{\epsilon}_{R^{*}}$ | innovation | foreign monetary policy shock | yes | (287) |
| `epsilon_X` | $\hat{\epsilon}^{X}$ | shock_process | shock in exports import-share cost (printed epsilon^X) | yes | (246) |
| `epsilon_Ystar` | $\hat{\epsilon}_{Y^{*}}$ | innovation | foreign demand (output) shock | yes | (286) |
| `eta` | $\eta$ | innovation | innovation of transitory technology shock | yes | (260) |
| `eta_DeltaP_I` | $\eta^{\Delta P_{I}}$ | innovation | measurement error in investment-deflator inflation | yes | (299) |
| `eta_EX_C` | $\eta_{EX}^{C}$ | innovation | innovation to the consumption excess trend | yes | (323) |
| `eta_EX_DeltaINV` | $\eta_{EX}^{\Delta INV}$ | innovation | innovation (white noise) to the inventory-share excess term | yes | (327) |
| `eta_EX_I` | $\eta_{EX}^{I}$ | innovation | innovation to the investment excess trend | yes | (324) |
| `eta_EX_IM` | $\eta_{EX}^{IM}$ | innovation | innovation to the import excess trend | yes | (325) |
| `eta_EX_N` | $\eta_{EX}^{N}$ | innovation | innovation to the hours excess trend | yes | (322) |
| `eta_EX_P_OILstar` | $\eta_{EX}^{P_{OIL}^{*}}$ | innovation | innovation to the oil-price excess trend | yes | (331) |
| `eta_EX_S` | $\eta_{EX}^{S}$ | innovation | innovation to the depreciation excess trend | yes | (320) |
| `eta_EX_W` | $\eta_{EX}^{W}$ | innovation | innovation to the wage excess trend | yes | (321) |
| `eta_EX_WTstar` | $\eta_{EX}^{WT^{*}}$ | innovation | innovation to the world-import excess trend | yes | (330) |
| `eta_EX_X` | $\eta_{EX}^{X}$ | innovation | innovation to the export excess trend | yes | (326) |
| `eta_EX_Ystar` | $\eta_{EX}^{Y^{*}}$ | innovation | innovation to the foreign-output excess trend | yes | (329) |
| `eta_FTR` | $\eta^{FTR}$ | innovation | foreign transfers innovation | yes | (270) |
| `eta_G` | $\eta^{G}$ | innovation | government consumption innovation | yes | (251) |
| `eta_OIL` | $\eta^{OIL}$ | innovation | oil price innovation | yes | (290) |
| `eta_Pibar` | $\eta^{\bar{\Pi}}$ | innovation | inflation-target innovation | no | (260) |
| `eta_R` | $\eta^{R}$ | innovation | monetary policy shock (white noise) | yes | (259) |
| `eta_tauC` | $\eta^{\tau^{C}}$ | innovation | consumption tax rate innovation | yes | (252) |
| `eta_tauD` | $\eta^{\tau^{D}}$ | innovation | dividend tax rate innovation | yes | (253) |
| `eta_tauK` | $\eta^{\tau^{K}}$ | innovation | capital rental tax rate innovation | yes | (254) |
| `eta_tauN` | $\eta^{\tau^{N}}$ | innovation | household income tax rate innovation | yes | (255) |
| `eta_tauW_f` | $\eta^{\tau^{W_{f}}}$ | innovation | firm payroll tax innovation | yes | (257) |
| `eta_tauW_h` | $\eta^{\tau^{W_{h}}}$ | innovation | household payroll tax innovation | yes | (256) |
| `EX_DeltaC` | $EX_{\Delta C}$ | shock_process | excess trend in consumption growth | yes | (292) |
| `EX_DeltaG` | $EX_{\Delta G}$ | shock_process | excess trend in government consumption growth | yes | (294) |
| `EX_DeltaIM` | $EX_{\Delta IM}$ | shock_process | excess trend in import growth | yes | (296) |
| `EX_DeltaINI` | $EX_{\Delta INI}$ | shock_process | excess trend in fixed-investment growth | yes | (293) |
| `EX_DeltaINV` | $EX_{\Delta INV}$ | shock_process | excess term in the inventory share | yes | (317) |
| `EX_DeltaN` | $EX_{\Delta N}$ | shock_process | common excess trend in per-capita hours growth | yes | (291) |
| `EX_DeltaPOIL` | $EX_{\Delta POIL}$ | shock_process | excess trend in oil-price changes | yes | (316) |
| `EX_DeltaPOIL` | $EX_{\Delta POil}$ | shock_process | excess trend in oil-price changes (as printed in 331) | yes | (331) |
| `EX_DeltaS` | $EX_{\Delta S}$ | shock_process | excess trend in nominal depreciation | yes | (306) |
| `EX_DeltaW` | $EX_{\Delta W}$ | shock_process | excess trend in nominal wage growth | yes | (304) |
| `EX_DeltaWTstar` | $EX_{\Delta WT*}$ | shock_process | excess trend in world import growth | yes | (319) |
| `EX_DeltaX` | $EX_{\Delta X}$ | shock_process | excess trend in export growth | yes | (295) |
| `EX_DeltaYstar` | $EX_{\Delta Y*}$ | shock_process | excess trend in foreign output growth | yes | (307) |
| `fw_ristar` | $\hat{fw}_{ri^{*}}$ | endogenous | forward real-rate term as printed in (312) | yes | (312) |
| `fw_ristar` | $\widehat{fw}_{ri^{*}}$ | shock_process | foreign forward (natural) real rate | yes | (286) |
| `g` | $\hat{g}$ | endogenous | government consumption, log deviation | yes | (251) |
| `g_DeltaC` | $g_{\Delta C}$ | parameter | assumed long-run gross growth rate of consumption | no | (323) |
| `g_DeltaI` | $g_{\Delta I}$ | parameter | assumed long-run gross growth rate of fixed investment | no | (324) |
| `g_DeltaIM` | $g_{\Delta IM}$ | parameter | assumed long-run gross growth rate of imports | no | (325) |
| `g_DeltaN` | $g_{\Delta N}$ | parameter | assumed long-run growth of per-capita hours | no | (322) |
| `g_DeltaW` | $g_{\Delta W}$ | parameter | assumed long-run gross growth rate of nominal wages | no | (321) |
| `g_DeltaWTstar` | $g_{\Delta WT*}$ | parameter | assumed long-run gross growth rate of world imports | no | (330) |
| `g_DeltaX` | $g_{\Delta X}$ | parameter | assumed long-run gross growth rate of exports | no | (326) |
| `g_DeltaYstar` | $g_{\Delta Y^{*}}$ | parameter | assumed long-run gross growth rate of foreign output | no | (329) |
| `g_ss` | $g$ | steady_state | steady-state government consumption | no | (280) |
| `g_Y` | $\hat{g}_{Y}$ | endogenous | output growth, deviation | yes | (258) |
| `g_z` | $\hat{g}_{z}$ | shock_process | growth rate of labor-augmenting productivity, deviation | yes | (212) |
| `g_z_ss` | $g_{z}$ | parameter | steady-state gross productivity growth rate | no | (212) |
| `gamma_B` | $\gamma_{B}$ | parameter | premium sensitivity to net foreign assets | no | (217) |
| `gamma_I` | $\gamma_{I}$ | parameter | investment adjustment cost scale | no | (214) |
| `gamma_IM_C` | $\gamma_{IM}^{C}$ | parameter | import-share adjustment cost parameter, consumption sector | no | (234) |
| `gamma_IM_G` | $\gamma_{IM}^{G}$ | parameter | import-share adjustment cost parameter, public consumption sector | no | (242) |
| `gamma_IM_I` | $\gamma_{IM}^{I}$ | parameter | import-share adjustment cost parameter, investment sector | no | (238) |
| `gamma_IM_X` | $\gamma_{IM}^{X}$ | parameter | import-share adjustment cost parameter, exports sector | no | (246) |
| `Gamma_IMC_p` | $\hat{\Gamma}_{IM^{C}}^{+}$ | endogenous | import-share adjustment-cost term, consumption sector | yes | (233) |
| `Gamma_IMG_p` | $\hat{\Gamma}_{IM^{G}}^{+}$ | endogenous | import-share adjustment-cost term, public consumption sector | yes | (241) |
| `Gamma_IMI_p` | $\hat{\Gamma}_{IM^{I}t}^{+}$ | endogenous | import-share adjustment-cost term, investment sector (printed variant) | no | (237) |
| `Gamma_IMI_p` | $\hat{\Gamma}_{IM^{I}}^{+}$ | endogenous | import-share adjustment-cost term, investment sector | yes | (238) |
| `Gamma_IMX_p` | $\hat{\Gamma}_{IM^{X}}^{+}$ | endogenous | import-share adjustment-cost term, exports sector | yes | (245) |
| `gamma_S` | $\gamma_{S}$ | parameter | premium sensitivity to expected depreciation | no | (217) |
| `gamma_star` | $\gamma^{*}$ | parameter | export-share adjustment cost parameter | no | (271) |
| `gamma_u_1` | $\gamma_{u,1}$ | parameter | linear coefficient of capital-utilization cost | no | (213) |
| `gamma_u_2` | $\gamma_{u,2}$ | parameter | quadratic coefficient of capital-utilization cost | no | (215) |
| `h` | $\hat{h}$ | endogenous | production-relevant aggregate of domestic intermediate goods | yes | (274) |
| `h_C` | $\hat{h}_{C}$ | endogenous | domestic intermediate input into consumption good, log deviation | yes | (232) |
| `h_G` | $\hat{h}_{G}$ | endogenous | domestic intermediate input into public consumption good | yes | (240) |
| `h_I` | $\hat{h}_{I}$ | endogenous | domestic intermediate input into investment good, log deviation | yes | (236) |
| `h_s` | $\hat{h}^{s}$ | endogenous | supply of domestic intermediate goods, deviation | yes | (274) |
| `h_s` | $\hat{h}_{s}$ | endogenous | domestic intermediate goods supply (output), log deviation | yes | (222) |
| `h_ss` | $h$ | steady_state | steady-state domestic intermediate output | no | (222) |
| `h_X` | $\hat{h}_{X}$ | endogenous | domestic intermediate input into exported good, log deviation | yes | (244) |
| `i` | $\hat{\imath}$ | endogenous | investment (detrended), log deviation | yes | (214) |
| `i_ss` | $i$ | steady_state | steady-state investment | no | (276) |
| `im` | $\hat{im}$ | endogenous | imports (log deviation); Table 7 column header, same as \widehat{im} | yes | (283) |
| `im` | $\widehat{im}$ | endogenous | total imported intermediate goods, log deviation | yes | (268) |
| `im_C` | $\widehat{im}_{C}$ | endogenous | imported intermediate input into consumption good, log deviation | yes | (233) |
| `im_C_ss` | $im_{C}$ | steady_state | steady-state imports used in the consumption good | no | (280) |
| `im_G` | $\widehat{im}_{G}$ | endogenous | imported intermediate input into public consumption good | yes | (241) |
| `im_G_ss` | $im_{G}$ | steady_state | steady-state imports used in the public consumption good | no | (280) |
| `im_I` | $\widehat{im}_{I}$ | endogenous | imported intermediate input into investment good, log deviation | yes | (237) |
| `im_I_ss` | $im_{I}$ | steady_state | steady-state imports used in the investment good | no | (280) |
| `im_ss` | $im$ | steady_state | steady-state total imports | no | (283) |
| `im_star` | $\widehat{im}^{*}$ | endogenous | world imports (world trade), log deviation | yes | (271) |
| `im_X` | $\widehat{im}_{X}$ | endogenous | imported intermediate input into exported good, log deviation | yes | (245) |
| `im_X_ss` | $im_{X}$ | steady_state | steady-state imports used in the export good | no | (280) |
| `k` | $\hat{k}$ | endogenous | capital stock (detrended), log deviation | yes | (218) |
| `k_s` | $\hat{k}^{s}$ | endogenous | capital services, log deviation | yes | (222) |
| `k_s` | $\hat{k}_{s}$ | endogenous | capital services demanded by firms, deviation | yes | (279) |
| `k_ss` | $k$ | steady_state | steady-state capital stock | no | (276) |
| `kappa` | $\kappa$ | parameter | degree of external habit formation | no | (212) |
| `lambda` | $\hat{\lambda}$ | endogenous | marginal utility of consumption (Lagrange multiplier), log deviation | yes | (212) |
| `mc` | $\widehat{mc}$ | endogenous | real marginal cost of domestic firms (vs CPI), log deviation | yes | (224) |
| `mc_H` | $\widehat{mc}^{H}$ | endogenous | real marginal cost of domestic firms relative to domestic price index | yes | (226) |
| `mc_IM` | $\widehat{mc}_{IM}$ | endogenous | real marginal cost of foreign intermediate goods firms | yes | (229) |
| `mc_X` | $\widehat{mc}^{X}$ | endogenous | exporters' real marginal cost, log deviation | yes | (248) |
| `mrs` | $\widehat{mrs}$ | endogenous | marginal rate of substitution consumption-leisure, log deviation | yes | (220) |
| `mu_C` | $\mu_{C}$ | parameter | elasticity of substitution domestic vs imported, consumption | no | (232) |
| `mu_C` | $\mu_{c}$ | parameter | elasticity of substitution, consumption (printed lower-case) | no | (233) |
| `mu_G` | $\mu_{G}$ | parameter | elasticity of substitution, public consumption sector | no | (240) |
| `mu_I` | $\mu_{I}$ | parameter | elasticity of substitution, investment sector | no | (236) |
| `mu_star` | $\mu^{*}$ | parameter | price elasticity of export demand | no | (271) |
| `mu_X` | $\mu_{X}$ | parameter | elasticity of substitution, exports sector | no | (244) |
| `mu_X` | $\mu_{x}$ | parameter | elasticity of substitution in exports (printed lower-case) | no | (247) |
| `n` | $\hat{n}$ | endogenous | hours worked (employment), log deviation | yes | (220) |
| `nu_C` | $\hat{\nu}_{C}$ | shock_process | time-varying home bias, consumption sector | yes | (232) |
| `nu_C` | $\hat{\nu}_{ct}$ | shock_process | time-varying home bias, consumption sector (printed variant) | no | (235) |
| `nu_C_ss` | $\nu_{C}$ | parameter | steady-state home bias, consumption | no | (235) |
| `nu_E` | $\nu_{E}$ | parameter | home-bias weight in (233) as printed | no | (233) |
| `nu_f` | $\hat{\nu}_{f}$ | other | time-varying working-capital share, deviation | yes | (225) |
| `nu_f_ss` | $\nu^{f}$ | parameter | share of wage bill financed by working capital | no | (225) |
| `nu_G` | $\hat{\nu}_{G}$ | shock_process | time-varying home bias, public consumption sector | yes | (240) |
| `nu_G_ss` | $\nu_{G}$ | parameter | steady-state home bias, public consumption | no | (241) |
| `nu_I` | $\hat{\nu}_{I}$ | shock_process | time-varying home bias, investment sector | yes | (236) |
| `nu_I_ss` | $\nu_{I}$ | parameter | steady-state home bias, investment | no | (237) |
| `nu_star` | $\hat{\nu}^{*}$ | shock_process | country-specific export-demand shock | yes | (271) |
| `nu_X` | $\hat{\nu}_{X}$ | shock_process | time-varying home bias, exports sector | yes | (244) |
| `nu_X_ss` | $\nu_{X}$ | parameter | steady-state home bias, exports | no | (245) |
| `nu_X_ss` | $\nu_{x}$ | parameter | home bias in exports (printed lower-case) | no | (247) |
| `omega_Gamma_I` | $\omega_{\Gamma_{I}}$ | parameter | weight of second investment lag in adjustment cost | no | (214) |
| `omega_star` | $\omega^{*}$ | parameter | share of oil in imports | no | (230) |
| `p_C_ss` | $p_{C}$ | steady_state | steady-state relative consumption price | no | (280) |
| `p_DX` | $\hat{p}_{DX}$ | endogenous | domestic-currency relative price of exported good, log deviation | yes | (244) |
| `p_DX_ss` | $p_{DX}$ | steady_state | steady-state relative price of exported good | no | (247) |
| `p_G` | $\hat{p}_{G}$ | endogenous | relative price of public consumption good, log deviation | yes | (240) |
| `p_G` | $\hat{p}_{g}$ | endogenous | relative price of public consumption good, log deviation (printed variant) | yes | (280) |
| `p_G_ss` | $p_{G}$ | steady_state | steady-state relative price of public consumption good | no | (243) |
| `p_H` | $\hat{p}_{H}$ | endogenous | relative price of domestic intermediate goods (vs CPI), log deviation | yes | (227) |
| `p_H_ss` | $p_{H}$ | steady_state | steady-state relative price of domestic goods | no | (235) |
| `p_I` | $\hat{p}_{I}$ | endogenous | relative price of investment good (vs CPI), log deviation | yes | (213) |
| `p_I_ss` | $p_{I}$ | steady_state | steady-state relative price of investment | no | (239) |
| `p_IM` | $\hat{p}_{IM}$ | endogenous | relative price of imported goods (vs CPI), log deviation | yes | (230) |
| `p_IM_ss` | $P_{IM}$ | endogenous | price index of imported intermediate goods | no | (284) |
| `p_IM_ss` | $p_{IM}$ | steady_state | steady-state relative price of imports | no | (235) |
| `p_OIL` | $\hat{p}_{OILl}$ | shock_process | relative price of oil, log deviation (printed variant) | yes | (290) |
| `p_OIL` | $\hat{p}_{OIL}$ | shock_process | relative price of oil, log deviation | yes | (230) |
| `p_X` | $\hat{p}_{X}$ | endogenous | real export price (foreign currency, vs foreign output deflator) | yes | (249) |
| `p_X` | $\hat{p}_{x}$ | endogenous | real export price (foreign currency), deviation | yes | (271) |
| `p_X_ss` | $p_{X}$ | steady_state | steady-state relative export price (foreign currency) | no | (267) |
| `p_X_ss` | $p_{x}$ | steady_state | export price in foreign markets (lowercase variant) | no | (284) |
| `p_x_star` | $\hat{p}_{x}^{*}$ | endogenous | price of competing exporters (world-trade price aggregate), deviation | yes | (271) |
| `p_Y` | $\hat{p}_{Y}$ | endogenous | GDP (output) deflator relative to CPI, log deviation | yes | (230) |
| `p_Y` | $\hat{p}_{y}$ | steady_state | steady-state relative output price | yes | (281) |
| `p_Y_M` | $\hat{p}_{Y}^{M}$ | endogenous | output deflator in market prices, deviation | yes | (284) |
| `p_Y_M_ss` | $p_{Y}^{M}$ | steady_state | steady-state output deflator in market prices | no | (284) |
| `p_Y_ss` | $P_{Y}$ | endogenous | domestic GDP deflator | no | (280) |
| `p_Y_ss` | $P_{y}$ | steady_state | steady-state relative output price (printed variant) | no | (280) |
| `p_Y_ss` | $p_{Y}$ | steady_state | output (GDP) deflator relative to CPI | no | (280) |
| `p_Y_ss` | $p_{y}$ | steady_state | steady-state relative output price | no | (280) |
| `phi_DeltaS` | $\phi_{\Delta S}$ | parameter | policy response to nominal depreciation | no | (259) |
| `phi_Pi` | $\phi_{\Pi}$ | parameter | policy response to CB inflation gap | no | (259) |
| `phi_R` | $\phi_{R}$ | parameter | interest-rate smoothing coefficient | no | (259) |
| `phi_w` | $\hat{\phi}_{w}$ | shock_process | wage markup shock | yes | (221) |
| `phi_w_ss` | $\phi_{w}$ | parameter | steady-state wage markup | no | (221) |
| `phi_y` | $\phi_{y}$ | parameter | policy response to output gap | no | (259) |
| `pi_C` | $\hat{\pi}_{C}$ | endogenous | CPI inflation, deviation | yes | (216) |
| `pi_CB` | $\hat{\pi}^{CB}$ | endogenous | four-quarter inflation measure the central bank reacts to | yes | (259) |
| `pi_H` | $\hat{\pi}_{H}$ | endogenous | domestic intermediate goods inflation, deviation | yes | (226) |
| `pi_IM` | $\hat{\pi}_{IM}$ | endogenous | import price inflation (local currency), deviation | yes | (229) |
| `pi_ss` | $\pi$ | steady_state | gross steady-state (target) inflation rate | no | (297) |
| `pi_star_ss` | $\pi^{*}$ | steady_state | steady-state foreign gross inflation | no | (272) |
| `pi_X` | $\hat{\pi}_{X}$ | endogenous | export price inflation in foreign currency, deviation | yes | (248) |
| `pi_Y` | $\hat{\pi}_{Y}$ | endogenous | inflation of output deflator, deviation | yes | (217) |
| `pi_Y_star` | $\hat{\pi}_{Y}^{*}$ | endogenous | foreign output-price inflation, deviation | yes | (217) |
| `pi_Y_star` | $\hat{\pi}_{y}^{*}$ | endogenous | foreign output-price inflation (printed lower-case y) | yes | (217) |
| `Pibar` | $\bar{\Pi}$ | steady_state | steady-state (gross) inflation target | no | (260) |
| `pibar` | $\hat{\bar{\pi}}$ | endogenous | domestic inflation target, deviation | yes | (217) |
| `pibar_nohat` | $\bar{\pi}$ | endogenous | inflation-target term as printed (bar, no hat) | yes | (259) |
| `pibar_star` | $\hat{\bar{\pi}}^{*}$ | endogenous | foreign inflation objective, deviation | yes | (217) |
| `pibar_star_nohat` | $\bar{\pi}^{*}$ | shock_process | foreign inflation target | yes | (287) |
| `psi` | $\psi$ | parameter | fixed cost parameter in production | no | (222) |
| `Q` | $\hat{Q}$ | endogenous | Tobin's Q (real price of installed capital), log deviation | yes | (213) |
| `q_C` | $\hat{q}_{C}$ | endogenous | output of final private consumption good, log deviation | yes | (232) |
| `q_G` | $\hat{q}_{G}$ | endogenous | output of final public consumption good, log deviation | yes | (240) |
| `q_I` | $\hat{q}_{I}$ | endogenous | output of final investment good, log deviation | yes | (236) |
| `q_I_ss` | $q^{I}$ | steady_state | steady-state final investment good output | no | (276) |
| `q_X` | $\hat{q}_{X}$ | endogenous | output of final exports good, log deviation | yes | (244) |
| `q_X_ss` | $q^{X}$ | steady_state | steady-state final export good output | no | (278) |
| `r` | $\hat{r}$ | endogenous | domestic nominal policy interest rate, deviation | yes | (216) |
| `R_f` | $\hat{R}_{f}$ | endogenous | gross interest rate on working capital, log deviation | yes | (223) |
| `r_k` | $\hat{r}_{k}$ | endogenous | real rental rate of capital, log deviation | yes | (213) |
| `r_OB` | $r^{OB}$ | observable | observed annualized Bank of Israel nominal interest rate | yes | (305) |
| `R_ss` | $R$ | steady_state | steady-state gross nominal interest rate | no | (225) |
| `R_ss` | $r$ | steady_state | gross steady-state domestic nominal interest rate | no | (305) |
| `r_star` | $\hat{r}^{*}$ | endogenous | foreign nominal interest rate, deviation | yes | (217) |
| `r_star_ss` | $r^{*}$ | steady_state | steady-state foreign gross interest rate | no | (272) |
| `r_starfwd_ob` | $r^{*fwd\_ob}$ | observable | observed foreign 5-10 year forward nominal interest rate | yes | (318) |
| `R_starOB` | $R^{*OB}$ | observable | observed annualized foreign (G4) nominal interest rate | yes | (309) |
| `rho_barpi` | $\rho_{\bar{\pi}}$ | parameter | persistence of inflation target | no | (260) |
| `rho_EX_C` | $\rho_{EX}^{C}$ | parameter | AR(1) coefficient of the consumption excess trend | no | (323) |
| `rho_EX_DeltaS` | $\rho_{EX}^{\Delta S}$ | parameter | AR(1) coefficient of the depreciation excess trend | no | (320) |
| `rho_EX_DeltaW` | $\rho_{EX}^{\Delta W}$ | parameter | AR(1) coefficient of the wage excess trend | no | (321) |
| `rho_EX_I` | $\rho_{EX}^{I}$ | parameter | AR(1) coefficient of the investment excess trend | no | (324) |
| `rho_EX_IM` | $\rho_{EX}^{IM}$ | parameter | AR(1) coefficient of the import excess trend | no | (325) |
| `rho_EX_N` | $\rho_{EX}^{N}$ | parameter | AR(1) coefficient of the hours excess trend | no | (322) |
| `rho_EX_P_OILstar` | $\rho_{EX}^{P_{OIL}^{*}}$ | parameter | AR(1) coefficient of the oil-price excess trend | no | (331) |
| `rho_EX_WTstar` | $\rho_{EX}^{WT^{*}}$ | parameter | AR(1) coefficient of the world-import excess trend | no | (330) |
| `rho_EX_X` | $\rho_{EX}^{X}$ | parameter | AR(1) coefficient of the export excess trend | no | (326) |
| `rho_EX_Ystar` | $\rho_{EX}^{Y^{*}}$ | parameter | AR(1) coefficient of the foreign-output excess trend | no | (329) |
| `rho_FTR` | $\rho_{FTR}$ | parameter | persistence of foreign transfers ratio | no | (270) |
| `rho_G` | $\rho_{G}$ | parameter | persistence of government consumption process | no | (251) |
| `rho_tauC` | $\rho_{\tau^{C}}$ | parameter | persistence of consumption tax rate | no | (252) |
| `rho_tauD` | $\rho_{\tau^{D}}$ | parameter | persistence of dividend tax rate | no | (253) |
| `rho_tauK` | $\rho_{\tau^{K}}$ | parameter | persistence of capital rental tax rate | no | (254) |
| `rho_tauN` | $\rho_{\tau^{N}}$ | parameter | persistence of household income tax rate | no | (255) |
| `rho_tauW_f` | $\rho_{\tau^{W_{f}}}$ | parameter | persistence of firm payroll tax | no | (257) |
| `rho_tauW_h` | $\rho_{\tau^{W_{h}}}$ | parameter | persistence of household payroll tax | no | (256) |
| `ri` | $\widehat{ri}$ | endogenous | real interest rate (nominal rate minus next-period CPI inflation) | yes | (261) |
| `ri_star` | $\widehat{ri}^{*}$ | endogenous | foreign real interest rate | yes | (286) |
| `rr_fw` | $\hat{rr}^{fw}$ | endogenous | 5-10 year forward expected real interest rate | yes | (259) |
| `rr_fwd_ob` | $rr^{fwd\_ob}$ | observable | observed domestic 5-10 year forward real interest rate | yes | (312) |
| `s` | $\hat{s}$ | endogenous | real exchange rate, log deviation | yes | (217) |
| `s_Bstar` | $\hat{s}_{B^{*}}$ | endogenous | net foreign assets to nominal GDP ratio, deviation | yes | (217) |
| `s_Bstar_nohat` | $s_{B^{*}}$ | endogenous | net foreign assets to output ratio | yes | (272) |
| `S_CA` | $S_{CA}$ | observable | observed current-account-to-GDP ratio | yes | (313) |
| `s_FTR` | $\hat{s}_{FTR}$ | shock_process | foreign transfers to output ratio, deviation | yes | (269) |
| `s_G` | $s_{G}$ | parameter | government consumption share of GDP | no | (328) |
| `s_IM` | $\hat{s}_{IM}$ | endogenous | imports to output ratio, deviation | yes | (266) |
| `s_IM_ss` | $s_{IM}$ | steady_state | steady-state imports to output ratio | no | (268) |
| `s_ss` | $s$ | steady_state | steady-state real exchange rate | no | (267) |
| `s_TB` | $\hat{s}_{TB}$ | endogenous | trade balance to output ratio, deviation | yes | (266) |
| `s_X` | $\hat{s}_{X}$ | endogenous | exports to output ratio, deviation | yes | (266) |
| `s_X_ss` | $s_{X}$ | steady_state | export share of GDP | no | (328) |
| `tau_C` | $\hat{\tau}^{C}$ | shock_process | consumption tax (VAT) rate, deviation | yes | (212) |
| `tau_C` | $\hat{\tau}^{c}$ | shock_process | consumption tax-rate deviation | yes | (284) |
| `tau_C_OB` | $\tau^{C\_OB}$ | observable | observed consumption (VAT) tax rate | yes | (314) |
| `tau_C_ss` | $\tau^{c}$ | parameter | steady-state consumption tax rate | no | (212) |
| `tau_C_ss` | $\tau_{c}$ | steady_state | steady-state consumption tax rate | no | (284) |
| `tau_D` | $\hat{\tau}^{D}$ | endogenous | dividend tax rate, deviation | yes | (253) |
| `tau_K` | $\hat{\tau}^{K}$ | shock_process | capital income tax rate, deviation | yes | (213) |
| `tau_K` | $\hat{\tau}^{k}$ | shock_process | capital income tax rate, deviation (printed variant) | yes | (254) |
| `tau_K_ss` | $\tau^{K}$ | parameter | steady-state capital income tax rate | no | (213) |
| `tau_N` | $\hat{\tau}^{N}$ | shock_process | labor income tax rate on households, deviation | yes | (219) |
| `tau_N` | $\hat{\tau}^{n}$ | shock_process | income tax-rate deviation | yes | (315) |
| `tau_N_OB` | $\tau^{N\_OB}$ | observable | observed income tax rate | yes | (315) |
| `tau_N_ss` | $\tau^{N}$ | parameter | steady-state labor income tax rate | no | (219) |
| `tau_N_ss` | $\tau_{n}$ | steady_state | steady-state income tax rate | no | (315) |
| `tau_W_f` | $\hat{\tau}^{W_{f}}$ | shock_process | payroll (social security) tax rate on firms, deviation | yes | (223) |
| `tau_W_f_ss` | $\tau^{W_{f}}$ | parameter | steady-state firm payroll tax rate | no | (223) |
| `tau_W_h` | $\hat{\tau}^{W_{h}}$ | shock_process | payroll (social security) tax rate on households, deviation | yes | (219) |
| `tau_W_h_ss` | $\tau^{W_{h}}$ | parameter | steady-state household payroll tax rate | no | (219) |
| `tp` | $tp$ | parameter | constant average domestic term premium | no | (312) |
| `tp_star` | $tp^{*}$ | parameter | constant average foreign term premium | no | (318) |
| `u` | $\hat{u}$ | endogenous | capital utilization intensity, deviation | yes | (215) |
| `varphi_H` | $\hat{\varphi}^{H}$ | shock_process | domestic price markup shock | yes | (226) |
| `varphi_star` | $\hat{\varphi}^{*}$ | shock_process | import price markup shock | yes | (229) |
| `varphi_X` | $\hat{\varphi}^{X}$ | shock_process | export price markup shock | yes | (248) |
| `w` | $\hat{w}$ | endogenous | real wage (detrended), log deviation | yes | (219) |
| `w_tau` | $\hat{w}_{\tau}$ | endogenous | after-tax real wage, log deviation | yes | (219) |
| `x` | $\hat{x}$ | endogenous | exports, log deviation | yes | (267) |
| `x_ss` | $x$ | steady_state | steady-state exports | no | (267) |
| `xi_E` | $\xi_{E}$ | parameter | Calvo-like employment adjustment parameter | no | (301) |
| `xi_H` | $\xi_{H}$ | parameter | Calvo parameter of domestic intermediate goods firms | no | (226) |
| `xi_star` | $\xi^{*}$ | parameter | Calvo parameter of foreign intermediate-goods firms | no | (229) |
| `xi_W` | $\xi_{W}$ | parameter | Calvo parameter (probability of no wage reoptimization) | no | (221) |
| `xi_X` | $\xi_{X}$ | parameter | Calvo parameter of exporters | no | (248) |
| `y` | $\hat{y}$ | endogenous | real output (GDP), log deviation | yes | (258) |
| `y_GAP` | $y^{GAP}$ | endogenous | output gap: output relative to technology-driven trend | yes | (259) |
| `y_ss` | $Y$ | other | appears in denominator P_{Y} Y of (282) | no | (269) |
| `y_ss` | $y$ | steady_state | steady-state real output | no | (267) |
| `y_star` | $\hat{y}^{*}$ | endogenous | foreign output, log deviation | yes | (286) |
| `zeta` | $\zeta$ | parameter | inverse Frisch elasticity of labor supply | no | (220) |
| `ztilde` | $\hat{\tilde{z}}$ | endogenous | relative level of foreign to domestic technology, deviation | yes | (271) |

## Part B: all symbols recorded in the paper

| LaTeX | Kind | Meaning | First seen | Notes |
|---|---|---|---|---|
| $h$ | index | household index on the unit interval | 0.i1 |  |
| $k$ | index | periods-ahead index in discounted sums | 1 |  |
| $s$ | index | product index in accumulated growth and inflation terms | 15.i1 |  |
| $E$ | operator | mathematical expectations operator, conditional on period-t information | 1 | printed E_{t} |
| $\beta$ | parameter | household discount factor | 1 |  |
| $\varepsilon^{C}$ | shock_process | consumption-demand (preference) shock | 1 | log-AR(1) per footnote 4 |
| $\varepsilon^{N}$ | shock_process | labor supply shock | 1 |  |
| $\kappa$ | parameter | degree of external habit persistence | 1 |  |
| $\zeta$ | parameter | inverse of the Frisch elasticity of labor supply | 1 |  |
| $C_{h}$ | endogenous | consumption composite of household h | 1 |  |
| $C$ | endogenous | composite of aggregate consumption | 1 | enters habit term as C_{t-1} |
| $N_{h}$ | endogenous | working hours (labor services) of household h | 1 |  |
| $\rho^{C}$ | parameter | AR(1) coefficient of log consumption-demand shock | 1.i1 | footnote 4 example |
| $\eta^{C}$ | innovation | white-noise innovation to consumption-demand shock | 1.i1 | footnote 4 |
| $\tau^{C}$ | shock_process | value added tax (VAT) rate | 2 | time-varying; its process is outside this chunk |
| $w_{\tau^{C}}$ | parameter | share of goods subject to VAT | 2 |  |
| $P_{C}$ | endogenous | pre-tax price of the consumption good | 2 |  |
| $P_{I}$ | endogenous | price of investment goods | 2 | not defined in this chunk beyond use in (2) |
| $I_{h}$ | endogenous | fixed capital investment of household h | 2 |  |
| $\Delta INV$ | other | change in inventories (level), common to all households | 2 | described as exogenous (p.7); its GDP share \Delta inv_{t} (2.i2) follows (3) |
| $\varepsilon^{RP}$ | shock_process | symmetric risk-premium shock on domestic and foreign bond prices | 2 |  |
| $\varepsilon^{DRP}$ | shock_process | domestic-currency bond risk-premium shock, near unit root | 2 | process 3.u1 |
| $R$ | endogenous | short-term gross nominal interest rate set by central bank | 2 |  |
| $B_{h}$ | endogenous | domestic-currency bond holdings of household h (beginning of period) | 2 |  |
| $\Gamma_{B^{*}}$ | endogenous | external financial intermediation premium on foreign-currency bonds | 2 | printed with time subscript in (2),(7) but not on LHS of (4) |
| $R^{*}$ | endogenous | foreign risk-free nominal interest rate | 2 | foreign variable from foreign-economy block (Sec. 3.6); exogenous to domestic economy |
| $S$ | endogenous | nominal exchange rate | 2 |  |
| $B_{h}^{*}$ | endogenous | foreign-currency bond holdings of household h (beginning of period) | 2 |  |
| $\Xi$ | other | lump-sum transfers | 2 | p.8; role not detailed in this chunk |
| $\Upsilon_{h}$ | endogenous | household h's state-contingent securities insuring labor-income risk | 2 |  |
| $\tau^{N}$ | parameter | direct income tax rate on labor income | 2 | printed with t subscript; constant per p.25 |
| $\tau^{W_{h}}$ | parameter | social security tax rate on household labor income | 2 | printed with t subscript; constant per p.25 |
| $W_{h}$ | endogenous | hourly nominal wage rate of household h | 2 |  |
| $\tau^{K}$ | parameter | tax rate on net capital income | 2 | printed with t subscript; constant per p.25 |
| $R_{K}$ | endogenous | nominal price (rental rate) of capital services | 2 |  |
| $u_{h}$ | endogenous | intensity of capital utilization of household h | 2 |  |
| $\Gamma_{u}$ | function | cost function of capital utilization intensity | 2 | functional form (8) |
| $K_{h}$ | endogenous | capital stock owned by household h | 2 |  |
| $\delta$ | parameter | depreciation rate of capital | 2 |  |
| $\tau^{D}$ | parameter | tax rate on dividend income | 2 | printed with t subscript; constant per p.25 |
| $D_{h}$ | endogenous | dividends to household h from monopolistic firms | 2 |  |
| $T$ | endogenous | lump-sum tax | 2 | set by fiscal rule outside this chunk |
| $\Delta inv_{t}$ | shock_process | change in inventories as a share of GDP | 2.i2 | AR(1) in (3); time index kept to distinguish from steady state \Delta inv |
| $Y$ | endogenous | GDP (real output) | 2.i2 | used in ratios; defined outside this chunk |
| $\rho_{\Delta INV}$ | parameter | AR(1) coefficient of inventory-change share | 3 |  |
| $\Delta inv$ | steady_state | steady-state inventory-change share of GDP | 3 | printed without time subscript in (3) |
| $\eta^{\Delta INV}$ | innovation | innovation to inventory-change share process | 3 |  |
| $\eta^{DRP}$ | innovation | innovation to domestic risk-premium shock | 3.u1 |  |
| $\varepsilon^{RP^{*}}$ | shock_process | exogenous shock to the external premium | 4 |  |
| $\gamma_{B^{*}}$ | parameter | sensitivity of external premium to net foreign assets ratio | 4 |  |
| $s_{B^{*}}$ | endogenous | ratio of total net foreign assets to nominal GDP | 4 | defined 4.i1, dated t+1 |
| $\gamma_{S}$ | parameter | sensitivity of external premium to target-adjusted expected depreciation | 4 |  |
| $\bar{\Pi}^{*}$ | other | foreign (gross) inflation target | 4 | foreign counterpart of \bar{\Pi}; its process is not given in this chunk |
| $\bar{\Pi}$ | shock_process | domestic (gross) inflation target | 4 | time-varying target; its process (64) is outside this chunk |
| $B^{*}$ | endogenous | aggregate net foreign-currency bond holdings | 4.i1 | appears in 4.i1 without h |
| $P_{Y}$ | endogenous | price level of GDP (P_{Y,t}Y_{t} is nominal GDP) | 4.i1 | further defined outside this chunk |
| $\Lambda_{h}$ | endogenous | marginal utility of consumption; scaled budget-constraint multiplier | 4.i3 | written without h in (15) |
| $\Lambda$ | endogenous | marginal utility of consumption, as printed in (15) without household index | 15 | same object as \Lambda_{h}; h omitted in print |
| $\gamma_{u,1}$ | parameter | linear coefficient of utilization cost | 8 | positive |
| $\gamma_{u,2}$ | parameter | quadratic coefficient of utilization cost | 8 | positive |
| $\varepsilon^{I}$ | shock_process | investment-specific technology shock | 9 |  |
| $\Gamma_{I}$ | function | investment adjustment cost function | 9 | functional form (10) |
| $\tilde{I}_{h}$ | endogenous | investment-growth index with two lags | 9 | defined in 10.u1; printed with a wide tilde |
| $\gamma_{I}$ | parameter | scale of investment adjustment costs | 10 |  |
| $g_{z}$ | parameter | long-run (gross) labor-productivity growth rate | 10 |  |
| $\omega_{\Gamma_{I}}$ | parameter | weight on lagged investment growth in adjustment cost | 10 | zero gives standard specification |
| $Q_{h}$ | endogenous | Tobin's Q: price of installed capital in consumption-good units | 10.i2 |  |
| $\Gamma'_{I}$ | function | first derivative of investment adjustment cost function | 11 |  |
| $\Gamma'_{u}$ | function | first derivative of utilization cost function | 13 |  |
| $\xi_{W}$ | parameter | Calvo probability of not reoptimizing the wage | 13.i1 |  |
| $g_{z,t}$ | shock_process | (gross) growth rate of labor productivity | 14 | time index kept to distinguish from parameter g_{z}; listed as permanent labor-productivity shock (printed p.45) |
| $\chi_{W,g_{z}}$ | parameter | degree of wage indexation to productivity growth | 14 |  |
| $\chi_{W}$ | parameter | degree of wage indexation to inflation | 14.i1 |  |
| $\Pi_{C}^{\dagger}$ | endogenous | wage-indexation inflation factor (lagged CPI inflation and target) | 14 | defined 14.i1 |
| $\Pi_{C}$ | endogenous | gross CPI inflation | 14.i1 | defined 14.i2 |
| $\tilde{W}$ | endogenous | new optimal wage common to reoptimizing households | p.11 | printed with a narrow tilde; introduced in text just before (15) |
| $g_{z;t,t+k}$ | endogenous | accumulated productivity growth from t to t+k | 15 | defined 15.i1; in (15) as g_{z;t-1,t+k-1}; time-window indices kept to distinguish from per-period symbol |
| $\Pi_{C;t,t+k}^{\dagger}$ | endogenous | accumulated wage-indexation inflation from t to t+k | 15 | defined 15.i2; time-window indices kept to distinguish from per-period symbol |
| $\Pi_{C;t,t+k}$ | endogenous | accumulated CPI inflation from t to t+k | 15 | defined 15.i3; time-window indices kept to distinguish from per-period symbol |
| $\varphi^{W}$ | shock_process | wage markup shock | 15 | defined p.14 (pdf 20) as markup > 1; not defined in this chunk |
| $W$ | endogenous | aggregate wage composite | 16 |  |
| $H_{f}$ | endogenous | differentiated intermediate good produced by domestic firm f | 16.i1 | f in [0,1]; also used in (27), (28), 27.i2 |
| $f$ | index | index of domestic intermediate goods firms, on [0,1] | 16.i1 |  |
| $IM_{f^{*}}$ | endogenous | differentiated imported intermediate good of foreign firm f* | 16.i2 | f* in [0,1] |
| $f^{*}$ | index | index of foreign intermediate goods firms, on [0,1] | 16.i2 |  |
| $Q^{C}$ | endogenous | final consumption good, perfectly competitive producers | 16.i3 |  |
| $Q^{I}$ | endogenous | final investment good | 16.i3 |  |
| $Q^{G}$ | endogenous | final government-consumption good | 16.i3 |  |
| $Q^{X}$ | endogenous | final homogeneous export good, bought by exporters | 16.i3 |  |
| $X_{f^{X}}$ | endogenous | differentiated (branded) export good of exporter f^X | 16.i4 | text prints f^{X} in subscript, f^{x} in index set; Figure 1 prints X_{f^{x},t} |
| $f^{x}$ | index | index of exporters, on [0,1] | 16.i4 | printed lower-case in the index set (and in Figure 1) |
| $X$ | endogenous | homogeneous exported good assembled by foreign retail firms | 16.i5 |  |
| $I$ | endogenous | investment (final use, Figure 1) | p.13 | Figure 1 label only; defined in 3.1 |
| $G$ | endogenous | government consumption (final use, Figure 1) | p.13 | Figure 1 label only; process given in 3.3 |
| $WT^{*}$ | other | foreign demand / world trade (Figure 1) | p.13 | figure prints WT_t*; foreign variable defined in 3.2.5/3.6, not this chunk |
| $X^{*}$ | other | foreign competitors' exports (Figure 1) | p.13 | figure prints X_t*; not defined in this chunk |
| $H_{f}^{s}$ | endogenous | output (supply) of domestic intermediate goods firm f | 17 | superscript s |
| $\varepsilon$ | shock_process | transitory technology shock, symmetric across firms | 17 | its process is not given in this chunk |
| $K_{f}^{s}$ | endogenous | homogeneous capital services rented by firm f | 17 | printed K^{S} (upper-case S) in (23), (24) |
| $K_{f}^{S}$ | endogenous | capital services of firm f (as printed in (23), (24)) | 23 | same variable as K_{f}^{s}; capitalization differs as printed |
| $\alpha$ | parameter | capital elasticity in production (Cobb-Douglas exponent) | 17 | Table 1 (p.44) calls it capital share in production |
| $z$ | shock_process | difference-stationary labor-augmenting productivity level | 17 | unit-root level, growth g_{z,t}; sets balanced growth path; symmetric across firms |
| $N_{f}$ | endogenous | CES labor composite employed by firm f | 17 | defined in (19) |
| $\psi$ | parameter | fixed-cost coefficient, calibrated for zero steady-state profits | 17 | fixed cost is \psi z_{t} |
| $\max$ | operator | maximum (of two arguments; or maximization in (27), (32)) | 17 |  |
| $\rho_{g_{z}}$ | parameter | persistence of productivity growth AR(1) | 18 |  |
| $\eta^{g_{z}}$ | innovation | innovation to productivity growth | 18 |  |
| $N_{f}^{h}$ | endogenous | labor of household h employed by firm f | 19 |  |
| $\int$ | operator | integral over households | 19 |  |
| $\rho_{W}$ | parameter | persistence of wage markup AR(1) | 20 |  |
| $\eta^{W}$ | innovation | innovation to the wage markup | 20 |  |
| $\log$ | operator | logarithm | 20 |  |
| $TVC$ | endogenous | total variable production cost | 23 |  |
| $R^{F}$ | endogenous | effective gross interest factor on wage bill (working capital) | 23 | R^{F}_{t}=1+\nu^{F}(R_{t}-1) |
| $\tau^{W_{f}}$ | parameter | social security tax rate levied on firms | 23 | carries time index t; assumed constant (pp.25, 46) |
| $\nu^{F}$ | parameter | fraction of wage bill borrowed before production | 23.i1 | Greek nu (zoom-checked) |
| $MC$ | endogenous | nominal marginal cost of domestic intermediate goods firms | 25 | identical across firms |
| $P_{H,f}$ | endogenous | price of domestic intermediate good f | 26 |  |
| $\Pi_{H}$ | endogenous | gross domestic intermediate goods inflation | 26 | \Pi_{H,t}=P_{H,t}/P_{H,t-1} |
| $\chi_{H}$ | parameter | indexation of domestic prices to past domestic inflation | 26 |  |
| $\xi_{H}$ | parameter | probability a domestic firm does not reoptimize (Calvo) | p.15 | defined in text before (26) |
| $P_{H}$ | endogenous | aggregate price index of domestic intermediate goods | 26.i1 |  |
| $\Lambda_{t,t+k}$ | other | firms' stochastic discount factor between t and t+k | 27 | defined in 27.i1 |
| $\sum$ | operator | summation over k | 27 |  |
| $\tilde{P}_{H}$ | endogenous | reset price chosen by reoptimizing domestic firms | 28 | tilde printed wide |
| $\Pi_{H,t,t+k}^{\dagger}$ | other | cumulative domestic indexation factor from t to t+k | 28 | defined in 28.i1; =1 for k=0 |
| $\varphi^{H}$ | shock_process | optimal markup of domestic intermediate goods firms | 28 | time-varying (p.19); Table 1: 1.3 |
| $\prod$ | operator | product over s | 28.i1 |  |
| $\bar{\Pi}_{H}$ | other | barred Pi with subscript H, as printed in (29) | 29 | likely typo for \bar{\Pi}_{t} as in (26) |
| $MC^{*}$ | endogenous | nominal marginal cost of foreign intermediate goods firms | 30 | in domestic currency via S_{t} |
| $\bar{\Pi}_{Y}^{*}$ | steady_state | gross steady-state inflation rate in the foreign economy | 30 | producer currency |
| $P_{OIL}^{*}$ | other | global price of oil | 30 | producer currency; enters (30) lagged t-1; exogenous foreign variable (relative oil price AR(2), Section 3.6) |
| $P_{Y}^{*}$ | endogenous | global price of foreign intermediate goods | 30 | producer currency |
| $\omega^{*}$ | parameter | oil share in the import basket | 30 |  |
| $P_{IM,f^{*}}$ | endogenous | consumer-currency price of imported good f* | 31 |  |
| $\Pi_{IM}$ | endogenous | gross import price inflation | 31 | \Pi_{IM,t}=P_{IM,t}/P_{IM,t-1} |
| $\chi^{*}$ | parameter | indexation of import prices to past import inflation | 31 |  |
| $\xi^{*}$ | parameter | probability a foreign firm does not reoptimize (Calvo) | p.17 | defined in text before (31) |
| $P_{IM}$ | endogenous | aggregate import price index (consumer currency) | 31.i1 |  |
| $\Lambda_{t,t+k}^{*}$ | other | foreign counterpart of the discount factor \Lambda_{t,t+k} | 32 | no explicit formula in this chunk |
| $\tilde{P}_{IM}$ | endogenous | reset price chosen by reoptimizing import firms | 33 | tilde printed wide |
| $\Pi_{IM,t,t+k}^{\dagger}$ | other | cumulative import-price indexation factor from t to t+k | 33 | defined in 33.i1; =1 for k=0 |
| $\varphi^{*}$ | shock_process | optimal markup of foreign intermediate goods firms | 33 | time-varying (p.19); Table 1: 1.3 |
| $\bar{\Pi}_{IM}$ | other | barred Pi with subscript IM, as printed in (34) | 34 | likely typo for \bar{\Pi}_{t} as in (31) |
| $Q_{f^{X}}^{X}$ | endogenous | homogeneous export good bought by exporter f^X | p.21 |  |
| $H^{C}$ | endogenous | bundle of domestic intermediate goods used in sector C | p.18 |  |
| $H_{f}^{C}$ | endogenous | domestic intermediate variety f used in sector C | 36 |  |
| $IM^{C}$ | endogenous | bundle of imported intermediate goods used in sector C | p.18 | IM^C/Q^C is import intensity (37.i1); lagged ratio is aggregate (38.i1) |
| $IM_{f^{*}}^{C}$ | endogenous | imported intermediate variety f* used in sector C | 37 |  |
| $\nu_{C}$ | shock_process | time-varying home-bias weight in sector C | 35 | AR(1) like (20) per footnote 15; 1-nu_C is steady-state import intensity |
| $\mu_{C}$ | parameter | elasticity of substitution between domestic and imported bundles | 35 | printed as CES between domestic and imported goods |
| $\Gamma_{IM^{C}}$ | function | adjustment cost of changing import intensity in sector C | 35 | defined in (38) |
| $\Gamma_{IM^{C}}^{\dagger}$ | function | auxiliary function: 1 - Gamma - Gamma' times IM^C | 44 | defined in 44.i1 |
| $\Gamma'_{IM^{C}}$ | function | derivative of the import-intensity adjustment cost | 44.i1 | argument of differentiation not stated in chunk |
| $\varepsilon^{IM}$ | shock_process | import-demand shock acting via imported-input productivity | 35 |  |
| $\gamma_{IM^{C}}$ | parameter | scale of import-intensity adjustment cost in sector C | 38 |  |
| $\varphi^{X}$ | shock_process | optimal price-markup shock of exporters | 50 | also governs CES aggregator in (51)-(54) |
| $P_{DX}$ | endogenous | price of homogeneous exported final good, domestic currency | 45.i1 | exception to the C-to-X renaming |
| $f^{X}$ | index | index of exporters / differentiated export goods | p.21 | same index as f^x |
| $\psi^{X}$ | parameter | fixed-cost parameter of brand naming | 46 |  |
| $\xi_{X}$ | parameter | Calvo probability that an exporter does not reoptimize | p.22 | named in text before (47) |
| $\chi_{X}$ | parameter | weight on past export inflation in export price indexation | 47 |  |
| $P_{X,f^{X}}$ | endogenous | foreign-currency price of exporter f^X | 47 |  |
| $P_{X}$ | endogenous | aggregate foreign-currency export price | p.21 | equal to retailers' marginal cost; index (54) |
| $\Pi_{X}$ | endogenous | gross foreign-currency inflation of export prices | 47 | defined in 47.i1 |
| $\bar{\Pi}_{X}^{*}$ | shock_process | foreign inflation objective, as printed with subscript X | 50.i1 | appears in 50.i1 and (51); cf. bar Pi^* in (47) |
| $\Pi_{X}^{\dagger}$ | endogenous | cumulative indexation factor of export prices from t to t+k | 50 | written with time subscripts t,t+k; defined in 50.i1 and 50.i2 |
| $\tilde{P}_{X}$ | endogenous | optimal foreign-currency price of reoptimizing exporters | p.22 | printed with wide tilde; used in (50), (51) |
| $MC^{X}$ | endogenous | exporters' nominal marginal cost in domestic currency | 48 | equals P_DX by (49) |
| $P_{X}^{c,*}$ | endogenous | price aggregate of world trade | 55 |  |
| $\mu^{*}$ | parameter | price elasticity of exports | 55 |  |
| $\nu^{*}$ | shock_process | country-specific export-demand shock | 55 |  |
| $\Gamma_{X}$ | function | adjustment cost of changing exports' share of world trade | 55 | defined in (56) |
| $\Gamma_{X}^{\dagger}$ | function | auxiliary function: 1 - Gamma_X - Gamma'_X times X | 55 | defined in (57) |
| $\Gamma'_{X}$ | function | derivative of the world-trade-share adjustment cost | 57 | argument of differentiation not stated in chunk |
| $\varepsilon^{X}$ | shock_process | shock in the export adjustment cost function | 55 | not separately defined in chunk; enters like eps^IM in (38) |
| $\gamma^{*}$ | parameter | scale of export adjustment cost | 56 |  |
| $P_{G}$ | endogenous | price of government-consumption final good | 58 |  |
| $B$ | endogenous | government bonds (domestic-currency debt) | 58 | B_{t+1} issued at t |
| $N$ | endogenous | production-relevant aggregate of labor services | 58 | defined 71.i2 |
| $u$ | endogenous | aggregate capital utilization rate | 58 | u_{t}K_{t} defined 72.i2 |
| $K$ | endogenous | capital stock | 58 |  |
| $D$ | endogenous | aggregate profits (dividends) of intermediate firms and exporters | 58 | defined (88) |
| $g$ | endogenous | government spending stationarized by productivity | 59 | g_{t} = G_{t}/z_{t} (59.i1); g without t is steady state |
| $\rho_{G}$ | parameter | persistence of government spending | 59 |  |
| $\eta^{G}$ | innovation | government spending innovation | 59 |  |
| $\eta^{\tau^{C}}$ | innovation | VAT rate innovation | 60 |  |
| $s_{T}$ | endogenous | lump-sum taxes as share of GDP | 61 | defined 61.i1 |
| $\phi_{B}$ | parameter | response of lump-sum taxes to debt-to-GDP gap | 61 |  |
| $s_{B}$ | endogenous | government debt as share of GDP | 61 | s_{B,t+1} defined 61.i2; s_{B} without t is steady state |
| $\hat{r}$ | endogenous | nominal policy interest rate (log deviation) | 62 |  |
| $\phi_{R}$ | parameter | interest-rate smoothing coefficient | 62 |  |
| $\widehat{rr}^{fwd}$ | endogenous | forward real rate: average expected real rate 5-10 years ahead | 62 | defined (63) |
| $\hat{\bar{\pi}}$ | shock_process | time-varying inflation target (deviation) | 62 | hat over bar; printed wide hat over full-width bar; process (64) |
| $\phi_{\Pi}$ | parameter | response to deviation of CB inflation measure from target | 62 |  |
| $\hat{\pi}^{CB}$ | endogenous | inflation measure the central bank reacts to | 62 | defined (65) |
| $\phi_{y}$ | parameter | response to the output gap | 62 |  |
| $\hat{y}^{GAP}$ | endogenous | output deviation from technology-driven trend | 62 | defined 62.i1 |
| $\phi_{\Delta S}$ | parameter | response to nominal depreciation | 62 |  |
| $\Delta S$ | endogenous | nominal depreciation | 62 | defined 62.i2 |
| $\eta^{R}$ | innovation | monetary policy shock (white noise) | 62 |  |
| $Z$ | other | productivity trend in output-gap definition | 62.i1 | printed upper case Z_{t} here; elsewhere productivity is z_{t} |
| $y$ | steady_state | steady-state (detrended) output | 62.i1 | log y in 62.i1 |
| $\hat{s}$ | endogenous | real exchange rate (log deviation) | 62.i2 | not defined in this chunk |
| $\hat{\pi}_{Y}$ | endogenous | inflation of P_{Y} (GDP-deflator) prices | 62.i2 | not defined in this chunk |
| $\hat{\pi}_{Y}^{*}$ | endogenous | foreign intermediate-goods (world) inflation | 62.i2 | Phillips curve (92) |
| $\widehat{ri}$ | endogenous | log-linearized one-quarter real interest rate | 63 | defined 63.i1 |
| $\hat{\pi}_{C}$ | endogenous | CPI inflation (log deviation) | 63.i1 |  |
| $\eta^{\bar{\Pi}}$ | innovation | inflation target innovation | 64 | bar printed full width over Pi |
| $TB$ | endogenous | trade balance | 66 |  |
| $IM$ | endogenous | aggregate imports (sum of sectoral import aggregates) | 66 | defined 79.i1 |
| $CA$ | endogenous | current account | 67 |  |
| $FTR$ | shock_process | exogenous foreign transfers | 67 | share s_{FTR} follows (69) |
| $s_{FTR}$ | shock_process | foreign transfers as share of nominal GDP | 68.i1 | s_{FTR} without t is steady state |
| $\rho_{FTR}$ | parameter | persistence of foreign-transfers share | 69 |  |
| $\eta^{FTR}$ | innovation | foreign-transfers innovation | 69 |  |
| $\check{s}_{W}$ | endogenous | wage dispersion measure | 71 | defined 71.i1 |
| $K^{s}$ | endogenous | aggregate capital services demanded by firms | 72.i1 |  |
| $H$ | endogenous | sum of sectoral domestic intermediate aggregates | 74.u1 | defined 74.i1 |
| $H^{s}$ | endogenous | simple sum of domestic intermediate supply | 74.i2 |  |
| $\check{s}_{H}$ | endogenous | price dispersion of domestic intermediate goods | 74.i3 |  |
| $\check{s}_{IM}$ | endogenous | price dispersion of imported intermediate goods | 76.i1 |  |
| $IM^{s}$ | endogenous | simple sum of imported intermediate goods | 76.i2 |  |
| $Q_{f^{X}}$ | endogenous | homogeneous export good bought by exporter f^{X} | 82.u1 |  |
| $\check{s}_{X}$ | endogenous | price dispersion in the export sector | 82.i1 |  |
| $Q$ | endogenous | output of final-goods sectors (Q^{C},Q^{I},Q^{G},Q^{X}) | 85 |  |
| $\epsilon^{IM}$ | shock_process | import-productivity shock | 85 | printed lunate epsilon in (85)-(86); varepsilon in (38) |
| $P_{Y}^{M}$ | endogenous | GDP deflator at market prices (incl. VAT) | 86 |  |
| $D_{H,f}$ | endogenous | profits of domestic intermediate-goods firm f | 88 |  |
| $D_{X,f^{X}}$ | endogenous | profits of exporter f^{X} | 88 |  |
| $s_{D}$ | endogenous | profits as share of nominal GDP | 88.u1 |  |
| $\hat{y}^{*}$ | endogenous | foreign output (log deviation) | 89 |  |
| $c_{y^{*},+}$ | parameter | forward-looking weight in foreign IS curve | 89 |  |
| $c_{y^{*},r}$ | parameter | real-rate sensitivity in foreign IS curve | 89 |  |
| $\hat{r}^{*}$ | endogenous | foreign nominal interest rate (log deviation) | 89 |  |
| $\widehat{rr}^{*,fwd}$ | shock_process | foreign forward rate; proxy for foreign natural rate | 89 | near random walk (90) |
| $\varepsilon^{Y^{*}}$ | innovation | foreign output (demand) shock | 89 |  |
| $\varepsilon^{*,fwd}$ | innovation | foreign forward-rate shock | 90 |  |
| $\widehat{wt}^{*}$ | endogenous | world trade (log deviation) | 91 |  |
| $c_{wt,y}$ | parameter | response of world trade to foreign output | 91 |  |
| $c_{wt,y\_lag}$ | parameter | response of world trade to lagged foreign output | 91 | underscore printed literally |
| $c_{wt,-}$ | parameter | persistence of world trade | 91 |  |
| $\varepsilon^{WT^{*}}$ | innovation | world trade shock | 91 |  |
| $c_{\pi^{*},+}$ | parameter | forward-looking weight in foreign Phillips curve | 92 |  |
| $c_{\pi^{*},y}$ | parameter | response of foreign inflation to average foreign output | 92 |  |
| $c_{\pi^{*},OIL}$ | parameter | response of foreign inflation to relative oil price | 92 |  |
| $c_{\pi^{*},\Delta OIL}$ | parameter | response of foreign inflation to two-quarter oil-price change | 92 |  |
| $\hat{p}_{OIL}^{*}$ | endogenous | relative price of oil (log deviation) | 92 | AR(2) process (93) |
| $\varepsilon^{\Pi^{*}}$ | innovation | foreign inflation (cost-push) shock | 92 |  |
| $p_{OIL}^{*}$ | endogenous | relative price of oil, P_{OIL}^{*}/P_{Y}^{*} | 92.i1 |  |
| $c_{oil,-}$ | parameter | persistence of relative oil price | 93 |  |
| $c_{oil,\Delta}$ | parameter | coefficient on lagged change in relative oil price | 93 |  |
| $\varepsilon^{OIL}$ | innovation | oil price shock | 93 |  |
| $c_{r^{*},-}$ | parameter | interest-rate smoothing in foreign Taylor rule | 94 |  |
| $\hat{\bar{\pi}}^{*}$ | shock_process | foreign inflation target (deviation) | 94 | hat over bar; process not given in this chunk |
| $c_{r^{*},\pi}$ | parameter | response to foreign inflation gap (5-quarter average) | 94 |  |
| $c_{r^{*},y}$ | parameter | response to foreign output | 94 |  |
| $\varepsilon^{R^{*}}$ | innovation | foreign monetary policy shock | 94 |  |
| $p_{X}^{c,*}$ | other | competitors' export price relative to P_{Y}^{*}; fixed at 1 | 94.i1 |  |
| $\Delta$ | operator | log-difference operator (quarterly log change) | 94.i2 | defined p.34 as log(X_t/X_{t-1}); p.87 prints lower-case x inside the log |
| $\Delta Y$ | observable | per capita real GDP growth (observed) | p.35 | CBS; written \Delta Y_{t}^{OB} in (101) |
| $\Delta C$ | observable | per capita real private consumption growth | p.35 | CBS; covered by (104) with J=C |
| $\Delta I$ | observable | per capita fixed capital investment growth (excl. ships, aircraft) | p.35 | CBS; covered by (104) with J=I |
| $\Delta G$ | observable | per capita government consumption growth (excl. defence imports) | p.35 | CBS; covered by (104) with J=G |
| $\Delta X$ | observable | per capita exports growth (excl. diamonds, start-ups) | p.35 | CBS; covered by (104) with J=X; 94.i2, 95.u1 and 97.i101 also use X_t for a generic series |
| $\Delta IM$ | observable | per capita imports growth (excl. defence, ships, aircraft, diamonds) | p.35 | CBS; covered by (104) with J=IM |
| $\Delta P_{Y}^{M}$ | observable | GDP deflator inflation, market prices | p.35 | CBS; its observation equation has measurement error (fn 52); detrended by inflation target |
| $\Delta P_{X}^{NIS}$ | observable | export deflator inflation in domestic currency (NIS) | 94.i3 | defined as \Delta(S_t P_{X,t}) |
| $s_{CA}$ | observable | current account surplus as share of nominal GDP | 94.i4 | printed '=' on p.35 and '\equiv' on p.90 |
| $\Delta P_{C}$ | observable | CPI inflation (excl. fruit/vegetables; housing excl. 1992-2006), VAT changes deducted | p.35 | CBS; detrended by inflation target |
| $\bar{\pi}$ | observable | inflation target (quarterly); observed annualized as 4 times it | 94.i5 | Bank of Israel; bar over pi |
| $\Delta W$ | observable | nominal hourly wage growth | p.35 | total wages / total hours; detrended by inflation target; written \Delta W_{t}^{OB} in (106) |
| $\Delta N$ | observable | growth of hours worked per working-age person | p.35 | written \Delta N_{t}^{OB} in (99) |
| $\Delta EM$ | observable | growth of employees per working-age person | p.35 | written \Delta EM_{t}^{OB} in (100) |
| $r^{OB}$ | observable | Bank of Israel key nominal interest rate (annualized) | p.35 | level; detrended by inflation target |
| $rr^{fwd,OB}$ | observable | observed 5-10 year forward real interest rate (annualized) | p.35 | from indexed government bond yields; LHS of (108) |
| $r^{*,OB}$ | observable | G4 nominal central bank key interest rate (weighted) | p.35 | Bloomberg; level |
| $\Delta P_{Y}^{*}$ | observable | G4 CPI inflation (weighted) | p.35 | OECD; also appears on RHS of (107) |
| $\Delta Y^{*}$ | observable | G4 real GDP growth (weighted) | p.35 | OECD; covered by (104) with J=Y^{*} |
| $\Delta WT^{*}$ | observable | OECD import volume growth (world trade) | p.35 | OECD; covered by (104) with J=WT^{*} |
| $r^{*,fwd,OB}$ | observable | observed 5-10 year forward G4 nominal interest rate (annualized) | p.35 | Bloomberg; LHS of (109) |
| $\Delta P_{OIL}^{*}$ | observable | Brent crude oil price change (effective exchange rate terms) | p.35 | Bloomberg; written \Delta P_{OIL,t}^{*,OB} in (107) |
| $\widehat{EM}$ | endogenous | employment, log deviation from steady state | 95 | wide hat over EM |
| $\hat{N}$ | endogenous | per capita hours worked, log deviation from steady state | 95 | printed with wide hat in (95), narrow hat in (99) |
| $\chi_{EM}$ | parameter | persistence parameter of employment dynamics | 95 | added by the authors (footnote 20) |
| $\xi_{EM}$ | parameter | Calvo-like employment adjustment parameter | 95 | higher value means employment less sensitive to hours |
| $\varepsilon^{EM}$ | shock_process | employment equation shock (non-structural, no feedback) | 95 | non-structural; process type (AR or i.i.d.) not stated in this chunk |
| $\hat{x}$ | endogenous | generic model counterpart of an observable, log deviation | 95.u1 | generic notation p.39 |
| $J^{g}$ | index | 0/1 selection indicator for technology growth in observation equation | 95.u1 | upper-case J; not the component index J of B.2 |
| $J^{N}$ | index | 0/1 selection indicator for hours-trend growth in observation equation | 95.u1 |  |
| $\hat{g}_{z}$ | shock_process | growth rate of labor-augmenting productivity shock, deviation | 95.u1 | process is eq. (18); printed with wide hat on p.39 |
| $GR^{N}$ | shock_process | secular (trend) growth component of per capita hours worked | 95.u1 | unobserved AR(1) trend component, eq. (98) |
| $EX$ | shock_process | generic idiosyncratic trend shock (AR(1)) in observation equation | 95.u1 | generic form, p.39 |
| $\theta_{i}$ | parameter | parameter vector of model i | 96 | theta_j for comparison model j (97.u1) |
| $M_{i}$ | index | model i (j for comparison model) | 96 |  |
| $p$ | function | probability density (likelihood, prior, posterior, marginal) | 96 |  |
| $BF_{ij}$ | other | Bayes factor of model i versus model j | 97.u1 |  |
| $x$ | other | generic series level in log-difference definition | 97.i101 | lower-case x printed inside the log on p.87 |
| $\rho_{GR}^{N}$ | parameter | AR(1) persistence of secular hours growth | 98 | estimated |
| $g_{\Delta N}$ | steady_state | (gross) long-run growth rate of per capita hours (and employment rate) | 98 | constant of AR process within sample (fn 53) |
| $\eta_{GR}^{N}$ | innovation | i.i.d. innovation to secular hours growth | 98 |  |
| $\hat{y}$ | endogenous | stationarized per capita output, log deviation from steady state | 98.i1 | \hat{y}_t = y_t - y, y_t = log(Y_t/z_t), y its steady state (fn 54) |
| $\Delta N^{OB}$ | observable | observed per capita hours growth (incl. excess trend) | 99 |  |
| $\Delta EM^{OB}$ | observable | observed employment-rate growth (incl. excess trend) | 100 |  |
| $\Delta Y^{OB}$ | observable | observed per capita GDP growth (incl. excess trend) | 101 |  |
| $J$ | index | real component index: C, I, G, X, IM, Y*, WT* | 101.i1 | AR process for C, I, X, IM, Y*, WT*; G via (103) |
| $EX^{J}$ | shock_process | excess trend of component J (AR(1)) | 102 | EX^{G} instead determined by (103) |
| $\rho_{EX}^{J}$ | parameter | AR(1) persistence of excess trend of component J | 102 | estimated |
| $g_{\Delta J}$ | steady_state | assumed long-run growth rate of component J | 102 |  |
| $j^{H}$ | function | domestic-component indicator (1 for C, I, X, IM; 0 for Y*, WT*) | 102 | printed without argument in (104) |
| $\eta_{EX}^{J}$ | innovation | i.i.d. innovation to excess growth of component J | 102 |  |
| $s_{J}$ | parameter | share of component J in GDP | 103 | s_C, s_I, s_G, s_X, s_IM in (103); calibrated in 4.4 (outside chunk) |
| $EX^{G}$ | shock_process | excess trend of government consumption, set by (103) | 103 | no own AR process |
| $\Delta J^{OB}$ | observable | observed growth of real component J | 104 |  |
| $\hat{\jmath}$ | endogenous | log deviation of J_t/z_t from steady state | 104 | printed as hatted dotless j |
| $\Delta S^{OB}$ | observable | observed nominal depreciation rate | 105 |  |
| $EX^{S}$ | innovation | i.i.d. exchange-rate observation term | 105 | specified as i.i.d., not AR |
| $\Delta W^{OB}$ | observable | observed nominal hourly wage growth | 106 |  |
| $\hat{w}$ | endogenous | scaled real wage, log deviation from steady state | 106 | w_t = W_t/(P_{C,t} z_t) |
| $EX^{W}$ | innovation | i.i.d. wage observation term | 106 | specified as i.i.d., not AR |
| $\Delta P_{OIL}^{*,OB}$ | observable | observed quarterly change in Brent oil price | 107 |  |
| $EX^{P_{OIL}^{*}}$ | shock_process | excess trend of the oil price (AR(1), zero in steady state) | 107 | persistence \rho_{EX}^{P_{OIL}^{*}} |
| $\rho_{EX}^{P_{OIL}^{*}}$ | parameter | AR(1) persistence of oil-price excess trend | p.94 | pattern of (102) |
| $w$ | endogenous | scaled real wage level | 107.i2 |  |
| $tp$ | parameter | constant domestic term premium | 108 | estimated |
| $\varepsilon^{fwd,OB}$ | shock_process | serially correlated observation error, domestic forward rate | 108 |  |
| $tp^{*}$ | parameter | constant foreign term premium | 109 | estimated |
| $\varepsilon^{*,fwd,OB}$ | shock_process | serially correlated observation error, foreign forward rate | 109 |  |
| $\mu^{C}$ | parameter | elasticity of substitution, domestic vs imported inputs, consumption | p.42 | Table 1: 1.1 |
| $\mu^{I}$ | parameter | elasticity of substitution, domestic vs imported inputs, investment | p.42 | Table 1: 1.1 |
| $\mu^{G}$ | parameter | elasticity of substitution, domestic vs imported inputs, government | p.42 | Table 1: 0.2 |
| $\mu^{X}$ | parameter | elasticity of substitution, domestic vs imported inputs, exports | p.42 | Table 1: 1.1 |
| $p_{X}^{C}$ | parameter | export competitors' relative price (steady state) | p.43 | Table 1: 1.0 (normalized); capital C in Table 1 |
| $\tilde{z}$ | steady_state | steady-state relative level of foreign technology | p.43 | Table 1: 1.0 (normalized); wide tilde |
| $IM^{*}$ | endogenous | world imports (as in Table 1 label X's weight in IM*) | p.44 |  |
| $\nu^{C}$ | parameter | home bias, consumption (time-varying nu_t^C shares the common process) | p.42 | Table 1: 0.65 |
| $\nu^{I}$ | parameter | home bias, investment | p.42 | Table 1: 0.60 |
| $\nu^{G}$ | parameter | home bias, government consumption | p.42 | Table 1: 0.95 |
| $\nu^{X}$ | parameter | home bias, exports | p.42 | Table 1: 0.68 |
| $s_{G}$ | steady_state | government consumption to GDP ratio | p.41 | Table 1: 0.26 |
| $s_{TR}$ | steady_state | government transfers to GDP ratio | p.43 | Table 1: 0.15; set to balance budget |
| $P^{DX}$ | endogenous | price of exporters' inputs | p.42 | printed P_t^{DX} |
| $\gamma_{IM^{I}}$ | parameter | import-intensity adjustment cost, investment final goods | 97.i3 | set to 0 |
| $\gamma_{IM^{G}}$ | parameter | import-intensity adjustment cost, government final goods | 97.i3 | set to 0 |
| $\gamma_{IM^{X}}$ | parameter | import-intensity adjustment cost, export final goods | 97.i3 | set to 0 |
| $g_{\Delta Y^{*}}$ | steady_state | long-run growth rate of foreign GDP (annual) | p.43 | 2.2% |
| $g_{\Delta WT^{*}}$ | steady_state | long-run growth rate of world trade (annual) | p.43 | 5.3% |
| $g_{\Delta C}$ | steady_state | long-run growth of per capita private consumption (annual) | p.43 | 1.7% |
| $g_{\Delta I}$ | steady_state | long-run growth of per capita fixed capital investment (annual) | p.43 | 1.7% |
| $g_{\Delta X}$ | steady_state | long-run growth of per capita exports (annual) | p.43 | 4.9% |
| $g_{\Delta IM}$ | steady_state | long-run growth of per capita imports (annual) | p.45 | 2.9% |
| $g_{\Delta G}$ | steady_state | implied long-run growth of per capita government consumption (annual) | p.45 | (-1%) |
| $\varepsilon^{G}$ | shock_process | government consumption shock | p.45 |  |
| $\nu$ | shock_process | common time-varying home bias process of all final-good sectors | p.45 | printed nu_t; shared by nu^C, nu^G, nu^I, nu^X; AR rho_nu, innovation eta^nu |
| $P^{*}$ | endogenous | foreign price level | 97.i5 | printed P_t^*; Section 3.6 uses P_{Y,t}^* |
| $\eta$ | innovation | innovation of transitory technology shock | p.45 | Table 3 S.D.(eta) |
| $\eta^{RP}$ | innovation | innovation of symmetric premium shock | p.45 |  |
| $\eta^{RP^{*}}$ | innovation | innovation of external premium shock | p.45 |  |
| $\eta^{I}$ | innovation | innovation of investment technology shock | p.45 |  |
| $\eta^{\Delta inv}$ | innovation | innovation of inventory investment shock | p.45 | Table 3 prints eta^{Delta INV} |
| $\eta^{\nu^{*}}$ | innovation | innovation of time-varying export share | p.45 |  |
| $\eta^{\nu}$ | innovation | common innovation of home bias (general negative import demand shock) | p.45 |  |
| $\eta^{H}$ | innovation | innovation of domestic price markup (4.4.2 label) | p.45 | Table 3: eta^{varphi^H} |
| $\eta^{*}$ | innovation | innovation of import price markup (4.4.2 label) | p.45 | Table 3: eta^{varphi^*} |
| $\eta^{X}$ | innovation | innovation of export price markup (4.4.2 label) | p.45 | Table 3: eta^{varphi^X} |
| $\eta^{\varphi^{H}}$ | innovation | domestic markup innovation (Table 3 label) | p.51 |  |
| $\eta^{\varphi^{*}}$ | innovation | import markup innovation (Table 3 label) | p.51 |  |
| $\eta^{\varphi^{W}}$ | innovation | wage markup innovation (Table 3 label) | p.51 |  |
| $\eta^{\varphi^{X}}$ | innovation | export markup innovation (Table 3 label) | p.51 |  |
| $\eta^{Y^{*}}$ | innovation | world demand innovation | p.45 | Table 4: Demand |
| $\eta^{\Pi^{*}}$ | innovation | world cost push innovation | p.45 | Table 4: Supply |
| $\eta^{R^{*}}$ | innovation | world interest rate innovation | p.45 | Table 4: Interest rate |
| $\eta^{WT^{*}}$ | innovation | world trade innovation | p.45 | Table 4: World trade |
| $\eta^{OIL}$ | innovation | oil price innovation | p.45 | Table 4: Oil price |
| $\eta^{*,fwd}$ | innovation | world long-run (forward) rate innovation | p.45 | Table 4: LR rate; eq (90) prints epsilon^{*,fwd} |
| $\chi_{E}$ | parameter | indexation, employment (equation) | p.50 | eq (95) writes chi_{EM} |
| $\chi_{IM}$ | parameter | indexation, import prices | p.50 |  |
| $\xi_{E}$ | parameter | Calvo parameter, employment (equation) | p.50 | eq (95) writes xi_{EM} |
| $\xi_{IM}$ | parameter | Calvo parameter, import prices | p.50 |  |
| $\gamma_{B}$ | parameter | FX (external) premium coefficient on net foreign assets | p.48 | Table 2: FX premium - B* |
| $\rho$ | parameter | AR coefficient, transitory technology | p.45 |  |
| $\rho_{RP}$ | parameter | AR coefficient, symmetric premium | p.45 |  |
| $\rho_{RP^{*}}$ | parameter | AR coefficient, external premium | p.45 |  |
| $\rho_{DRP}$ | parameter | AR coefficient, domestic premium (listed, not estimated) | p.45 | no estimate in Tables 2-4 |
| $\rho_{C}$ | parameter | AR coefficient, consumption demand | p.45 |  |
| $\rho_{I}$ | parameter | AR coefficient, investment technology | p.45 |  |
| $\rho_{\Delta inv}$ | parameter | AR coefficient, inventory investment (4.4.2 label) | p.45 | tables: rho_{Delta INV} |
| $\rho_{\nu^{*}}$ | parameter | AR coefficient, export share | p.45 |  |
| $\rho_{\nu}$ | parameter | AR coefficient, common home bias | p.45 |  |
| $\rho_{H}$ | parameter | AR coefficient, domestic price markup (4.4.2/Table 5 label) | p.45 | Table 2: rho_{varphi^H} |
| $\rho^{*}$ | parameter | AR coefficient, import price markup (4.4.2/Table 5 label) | p.45 | Table 2: rho_{varphi^*} |
| $\rho_{X}$ | parameter | AR coefficient, export price markup (4.4.2/Table 5 label) | p.45 | Table 2: rho_{varphi^X} |
| $\rho_{\varphi^{H}}$ | parameter | AR coefficient, domestic markup (Table 2 label) | p.50 |  |
| $\rho_{\varphi^{*}}$ | parameter | AR coefficient, import markup (Table 2 label) | p.50 |  |
| $\rho_{\varphi^{W}}$ | parameter | AR coefficient, wage markup (Table 2 label) | p.50 |  |
| $\rho_{\varphi^{X}}$ | parameter | AR coefficient, export markup (Table 2 label) | p.50 |  |
| $\rho_{Y^{*}}$ | parameter | AR coefficient, world demand shock (Table 4: AR in shock, output eq.) | p.45 |  |
| $\rho_{\Pi^{*}}$ | parameter | AR coefficient, world cost push shock (Table 4: inflation eq.) | p.45 |  |
| $\rho_{R^{*}}$ | parameter | AR coefficient, world interest rate shock (Table 4: policy eq.) | p.45 |  |
| $\rho_{WT^{*}}$ | parameter | AR coefficient, world trade shock (listed, not reported) | p.45 |  |
| $\rho_{OIL}$ | parameter | AR coefficient, oil price shock (listed, not reported) | p.45 |  |
| $\rho_{OB,\Delta Y}$ | parameter | AR coeff of observation error, output deflator | p.51 | Table 3; normal prior |
| $\rho_{OB,E}$ | parameter | AR coeff of observation error, employment | p.51 | Table 3 |
| $\rho_{OB,fwd}$ | parameter | AR coeff of domestic forward-rate observation error | p.51 | Table 3: Obs. error |
| $\rho_{OB,fwd^{*}}$ | parameter | AR coeff of foreign forward-rate observation error | p.51 | Table 3: Obs. error |
| $\rho_{EX}^{N}$ | parameter | AR coeff of excess trend, hours | p.51 | Table 3 |
| $\rho_{EX}^{C}$ | parameter | AR coeff of excess trend, consumption | p.51 |  |
| $\rho_{EX}^{I}$ | parameter | AR coeff of excess trend, investment | p.51 |  |
| $\rho_{EX}^{X}$ | parameter | AR coeff of excess trend, exports | p.51 |  |
| $\rho_{EX}^{IM}$ | parameter | AR coeff of excess trend, imports | p.51 |  |
| $\rho_{EX}^{Y^{*}}$ | parameter | AR coeff of excess trend, foreign GDP | p.51 |  |
| $\rho_{EX}^{WT^{*}}$ | parameter | AR coeff of excess trend, world trade | p.51 |  |
| $\eta^{\Delta P_{Y}^{M}}$ | innovation | observation error, output deflator | p.51 | Table 3 S.D. |
| $\eta^{OB,E}$ | innovation | observation error, employment | p.51 |  |
| $\eta^{fwd,OB}$ | innovation | domestic term premium observation error | p.51 |  |
| $\eta^{*,fwd,OB}$ | innovation | foreign term premium observation error | p.51 |  |
| $\eta_{EX}^{N}$ | innovation | excess-trend innovation, hours worked | p.51 |  |
| $\eta_{EX}^{C}$ | innovation | excess-trend innovation, consumption | p.51 |  |
| $\eta_{EX}^{I}$ | innovation | excess-trend innovation, investment | p.51 |  |
| $\eta_{EX}^{X}$ | innovation | excess-trend innovation, exports | p.51 |  |
| $\eta_{EX}^{IM}$ | innovation | excess-trend innovation, imports | p.51 |  |
| $\eta_{EX}^{W}$ | innovation | excess-trend innovation, wages | p.51 |  |
| $\eta_{EX}^{Y^{*}}$ | innovation | excess-trend innovation, foreign GDP | p.51 |  |
| $\eta_{EX}^{WT^{*}}$ | innovation | excess-trend innovation, world trade | p.51 |  |
| $\eta_{EX}^{P_{OIL}^{*}}$ | innovation | excess-trend innovation, oil price | p.51 |  |
| $\eta_{EX}^{S}$ | innovation | excess-trend innovation, exchange rate | p.51 |  |
| $\mathrm{S.D.}$ | operator | standard deviation of the shock in parentheses | p.51 | printed S.D.(...) |
| $c_{wt,y-}$ | parameter | world trade equation: lagged output | p.52 | eq (91) prints c_{wt,y_lag} |
| $\Delta R$ | endogenous | change in the policy interest rate (enters lagged) | 97.i6 | printed Delta R_{t-1} |
| $\phi_{\Delta R}$ | parameter | policy response to lagged interest rate change | p.58 | Table 5 |
| $\phi_{\Delta Y}$ | parameter | policy response to lagged output growth | p.59 | Table 5 |
| $E_{t}$ | operator | expectation conditional on time-t information | 97.u2 |  |
| $\Delta P_{c}$ | observable | CPI inflation (log change of observed CPI) | 97.i11 | lower-case c in Sec. 5.1 text and Table 6; upper-case \Delta P_{C} in Sec. 5.2 and Figs 4-5 |
| $\hat{c}$ | endogenous | consumption (stationarized), deviation from steady state | p.70 |  |
| $\hat{i}$ | endogenous | investment (stationarized), deviation from steady state | p.70 | hat over dotted italic i in Table 7 header |
| $\widehat{im}$ | endogenous | imports (stationarized), deviation from steady state | p.70 | Table 7 header (p.70) prints a narrow hat over im; text p.71 prints a wide hat |
| $p_{H}$ | endogenous | price of domestic goods relative to the CPI, stationarized | p.72 | printed p_{H,t} without hat (p.72); defined p_{H,t} = P_{H,t}/P_{C,t} in App. C (p.95) |
| $\hat{im}$ | endogenous | imports (log deviation); Table 7 column header, same as \widehat{im} | Table 7 (p.70) | narrow hat as printed in Table 7 |
| $t$ | index | time (quarter) subscript, dropped in the steady state | 109.i2 |  |
| $c$ | steady_state | consumption divided by productivity | 109.i4 | c_t = C_t/z_t |
| $\xi$ | parameter | Calvo parameters (probability of not reoptimizing), generic | 109.i10 | printed as \xi's; all set to zero for the steady-state solution |
| $\lambda$ | steady_state | normalized marginal utility of the consumer's income | 110 | \lambda_t = \Lambda_t z_t (110.i1) |
| $\Pi$ | parameter | steady-state gross domestic inflation rate | 111 | not defined in this chunk; consistent with the target \bar{\pi} |
| $\Pi^{*}$ | parameter | steady-state gross foreign inflation rate | 112 | assumed equal to \Pi (112.i1) |
| $i$ | steady_state | investment divided by productivity | 113 |  |
| $p_{I}$ | steady_state | price of investment goods relative to the CPI | 114 | not defined in this chunk; lower-case convention gives P_I/P_C |
| $r_{K}$ | steady_state | real rental rate of capital services | 114.u1 | not defined in this chunk; nominal R_{K,t} defined p.9 |
| $h^{s}$ | steady_state | supply of domestic intermediate goods (normalized) | 118 |  |
| $k^{s}$ | steady_state | capital services used in production (normalized) | 118 | equals k by (145) |
| $mc$ | steady_state | real marginal cost of domestic intermediate firms, in consumer prices | 121 |  |
| $p_{Y}$ | steady_state | domestic GDP deflator relative to the CPI | 123 | not defined in this chunk; lower-case convention gives P_Y/P_C |
| $p_{IM}$ | steady_state | price of imported intermediate goods relative to the CPI | 123 |  |
| $h^{C}$ | steady_state | domestic intermediate goods used by consumption-goods producers | 124 |  |
| $q^{C}$ | steady_state | output of final consumption goods | 124 |  |
| $h^{I}$ | steady_state | domestic intermediate goods used by investment-goods producers | 125 |  |
| $\nu_{I}$ | parameter | home-bias weight on domestic inputs, investment goods | 125 |  |
| $\mu_{I}$ | parameter | elasticity of substitution between domestic and imported inputs, investment goods | 125 |  |
| $q^{I}$ | steady_state | output of final investment goods | 125 |  |
| $h^{G}$ | steady_state | domestic intermediate goods used by government-goods producers | 126 |  |
| $\nu_{G}$ | parameter | home-bias weight on domestic inputs, government-consumption goods | 126 |  |
| $\mu_{G}$ | parameter | elasticity of substitution between domestic and imported inputs, government goods | 126 | also printed in the exponent of the export-sector equation (131) |
| $q^{G}$ | steady_state | output of final government-consumption goods | 126 |  |
| $p_{G}$ | steady_state | price of government-consumption goods relative to the CPI | 126 |  |
| $h^{X}$ | steady_state | domestic intermediate goods used by export-goods producers | 127 |  |
| $\nu_{X}$ | parameter | home-bias weight on domestic inputs, export goods | 127 |  |
| $\mu_{X}$ | parameter | elasticity of substitution between domestic and imported inputs, export goods | 127 |  |
| $q^{X}$ | steady_state | output of the homogeneous final export good | 127 |  |
| $p_{DX}$ | steady_state | price of the homogeneous domestic export good relative to the CPI | 127 |  |
| $im^{C}$ | steady_state | imported intermediate goods used by consumption-goods producers | 128 |  |
| $im^{I}$ | steady_state | imported intermediate goods used by investment-goods producers | 129 |  |
| $im^{G}$ | steady_state | imported intermediate goods used by government-goods producers | 130 |  |
| $im^{X}$ | steady_state | imported intermediate goods used by export-goods producers | 131 | exponent printed as -\mu_{G} in (131); suspected typo |
| $p_{x}$ | steady_state | export price in foreign markets (lower-case subscript variant) | 136 | as printed in (136); same variable as p_{X}; suspected typo |
| $p_{X}$ | steady_state | exporters' foreign-currency export price, relative | 137 | P_{X,t} defined p.21; normalization not stated in this chunk |
| $wt^{*}$ | steady_state | world trade scaled by foreign productivity | 137 | wt^{*}_t = WT^{*}_t/z^{*}_t (137.i1) |
| $z^{*}$ | shock_process | foreign technology (productivity) level | 137.i2 | not defined further in this chunk |
| $s_{TB}$ | steady_state | trade balance as a share of GDP | 141 |  |
| $s_{X}$ | steady_state | exports as a share of GDP | 141 | defined by (142) |
| $s_{IM}$ | steady_state | imports as a share of GDP | 141 | defined by (143) |
| $im$ | steady_state | total imports of intermediate goods (normalized) | 143 | sum of sector imports in (147) |
| $p_{Y}^{M}$ | steady_state | GDP deflator at market prices (including VAT), relative to the CPI | 154 | not defined in this chunk; market-price GDP as in (86) |
| $s_{DX}$ | steady_state | export-sector profit share of nominal GDP | 156 |  |
| $p_{IM\_H}$ | steady_state | ratio of import price to domestic intermediate price | 159 | defined in (159) as p_{IM}/p_{H} |
| $A_{C}$ | steady_state | CES price composite of the consumption sector | 160 | defined in (160); p_{H}=(A_{C})^{-1} |
| $A_{I}$ | steady_state | CES price composite of the investment sector | 164 | defined in (164) |
| $A_{G}$ | steady_state | CES price composite of the government sector | 165 | defined in (165) |
| $A_{X}$ | steady_state | CES price composite of the export sector | 166 | defined in (166) |
| $h_{C}$ | steady_state | domestic intermediates used in consumption sector (subscript variant) | 197.i1 | same as h^{C} |
| $h_{I}$ | steady_state | domestic intermediates used in investment sector (subscript variant) | 197.i1 | same as h^{I} |
| $h_{G}$ | steady_state | domestic intermediates used in government sector (subscript variant) | 197.i1 | same as h^{G} |
| $h_{X}$ | steady_state | domestic intermediates used in export sector (subscript variant) | 197.i1 | same as h^{X} |
| $\hat{\lambda}$ | endogenous | marginal utility of consumption (Lagrange multiplier), log deviation | 212 |  |
| $\hat{\tau}^{C}$ | shock_process | consumption tax (VAT) rate, deviation | 212 | exogenous AR(1) (252, next chunk); absolute deviation |
| $\hat{\epsilon}^{C}$ | shock_process | consumption-demand (preference) shock | 212 | lunate epsilon in App. D; main text uses varepsilon |
| $\tau^{c}$ | parameter | steady-state consumption tax rate | 212 | printed lower-case c in (212); Table 1 writes tau^C |
| $\hat{Q}$ | endogenous | Tobin's Q (real price of installed capital), log deviation | 213 |  |
| $\hat{\tau}^{K}$ | shock_process | capital income tax rate, deviation | 213 | exogenous AR(1) (254); held constant in estimation |
| $\hat{r}_{k}$ | endogenous | real rental rate of capital, log deviation | 213 |  |
| $\hat{p}_{I}$ | endogenous | relative price of investment good (vs CPI), log deviation | 213 |  |
| $\hat{\imath}$ | endogenous | investment (detrended), log deviation | 214 | printed as dotless i with hat |
| $\hat{\epsilon}^{I}$ | shock_process | investment-specific technology shock | 214 |  |
| $\hat{u}$ | endogenous | capital utilization intensity, deviation | 215 |  |
| $\hat{\epsilon}^{RP}$ | shock_process | symmetric (common) risk-premium shock | 216 |  |
| $\hat{\epsilon}^{DRP}$ | shock_process | domestic, highly inertial risk-premium shock | 216 |  |
| $\hat{\pi}_{y}^{*}$ | endogenous | foreign output-price inflation (printed lower-case y) | 217 | in (217), (230); appears to be the same variable as \hat{\pi}_{Y}^{*} (depreciation definition p.25, eq. 30) |
| $\hat{s}_{B^{*}}$ | endogenous | net foreign assets to nominal GDP ratio, deviation | 217 | defined main text p.8 |
| $\hat{\epsilon}^{RP^{*}}$ | shock_process | external risk-premium shock | 217 |  |
| $\hat{k}$ | endogenous | capital stock (detrended), log deviation | 218 |  |
| $\hat{w}_{\tau}$ | endogenous | after-tax real wage, log deviation | 219 |  |
| $\hat{\tau}^{N}$ | shock_process | labor income tax rate on households, deviation | 219 | exogenous AR(1) (255) |
| $\hat{\tau}^{W_{h}}$ | shock_process | payroll (social security) tax rate on households, deviation | 219 | exogenous AR(1) (256) |
| $\widehat{mrs}$ | endogenous | marginal rate of substitution consumption-leisure, log deviation | 220 |  |
| $\hat{\epsilon}_{N}$ | shock_process | labor-supply shock | 220 | printed with subscript N; main text varepsilon_t^N; not used in estimation |
| $\hat{n}$ | endogenous | hours worked (employment), log deviation | 220 |  |
| $\phi_{w}$ | parameter | steady-state wage markup | 221 | printed phi lower-case w; Table 1 writes varphi^W |
| $\hat{\phi}_{w}$ | shock_process | wage markup shock | 221 | printed phi; main text varphi_t^W |
| $\hat{h}_{s}$ | endogenous | domestic intermediate goods supply (output), log deviation | 222 |  |
| $\hat{\epsilon}$ | shock_process | transitory technology shock | 222 | no superscript |
| $\hat{k}^{s}$ | endogenous | capital services, log deviation | 222 | hat spans k^s in print |
| $\hat{\tau}^{W_{f}}$ | shock_process | payroll (social security) tax rate on firms, deviation | 223 | exogenous AR(1) (257) |
| $\hat{R}_{f}$ | endogenous | gross interest rate on working capital, log deviation | 223 |  |
| $\widehat{mc}$ | endogenous | real marginal cost of domestic firms (vs CPI), log deviation | 224 |  |
| $\nu^{f}$ | parameter | share of wage bill financed by working capital | 225 | Table 1 nu^F = 0.2 |
| $\hat{\epsilon}^{F}$ | shock_process | shock in working-capital interest rate | 225 | not defined in chunk |
| $\hat{\nu}_{f}$ | other | time-varying working-capital share, deviation | 225 | not defined in chunk |
| $\hat{\pi}_{H}$ | endogenous | domestic intermediate goods inflation, deviation | 226 |  |
| $\widehat{mc}^{H}$ | endogenous | real marginal cost of domestic firms relative to domestic price index | 226 |  |
| $\hat{\varphi}^{H}$ | shock_process | domestic price markup shock | 226 | curly phi |
| $\hat{p}_{H}$ | endogenous | relative price of domestic intermediate goods (vs CPI), log deviation | 227 | defined p.114 as ln(P_H/P_C) |
| $\hat{\pi}_{IM}$ | endogenous | import price inflation (local currency), deviation | 229 |  |
| $\widehat{mc}_{IM}$ | endogenous | real marginal cost of foreign intermediate goods firms | 229 |  |
| $\hat{\varphi}^{*}$ | shock_process | import price markup shock | 229 | curly phi |
| $\beta^{*}$ | parameter | foreign discount factor | 229 |  |
| $\hat{p}_{Y}$ | endogenous | GDP (output) deflator relative to CPI, log deviation | 230 | cf. (281)-(282) in D.8; s p_Y = S P*_Y / P_C |
| $\hat{p}_{OIL}$ | shock_process | relative price of oil, log deviation | 230 | exogenous AR(2), eq. (290) in D.9 |
| $\hat{p}_{IM}$ | endogenous | relative price of imported goods (vs CPI), log deviation | 230 |  |
| $\ln$ | operator | natural logarithm | 231.i1 |  |
| $\hat{h}_{C}$ | endogenous | domestic intermediate input into consumption good, log deviation | 232 |  |
| $\hat{q}_{C}$ | endogenous | output of final private consumption good, log deviation | 232 |  |
| $\mu_{c}$ | parameter | elasticity of substitution, consumption (printed lower-case) | 233 | printed in (233); presumably mu_C |
| $\hat{\nu}_{C}$ | shock_process | time-varying home bias, consumption sector | 232 | printed \hat{\nu}_{ct} in (235) |
| $\widehat{im}_{C}$ | endogenous | imported intermediate input into consumption good, log deviation | 233 |  |
| $\hat{\Gamma}_{IM^{C}}^{+}$ | endogenous | import-share adjustment-cost term, consumption sector | 233 |  |
| $\nu_{E}$ | parameter | home-bias weight in (233) as printed | 233 | suspected typo for nu_C |
| $\gamma_{IM}^{C}$ | parameter | import-share adjustment cost parameter, consumption sector | 234 | main text gamma_{IM^C} |
| $\hat{\epsilon}^{IM}$ | shock_process | import demand shock (productivity of imported inputs) | 234 | not used in estimation |
| $\hat{\nu}_{c}$ | shock_process | home bias, consumption (printed \hat{\nu}_{ct}, no comma) | 235 | presumably \hat{\nu}_{C} |
| $\hat{h}_{I}$ | endogenous | domestic intermediate input into investment good, log deviation | 236 |  |
| $\hat{q}_{I}$ | endogenous | output of final investment good, log deviation | 236 |  |
| $\hat{\nu}_{I}$ | shock_process | time-varying home bias, investment sector | 236 |  |
| $\widehat{im}_{I}$ | endogenous | imported intermediate input into investment good, log deviation | 237 |  |
| $\hat{\Gamma}_{IM^{I}}^{+}$ | endogenous | import-share adjustment-cost term, investment sector | 237 | subscript printed IM^I t (no comma) in (237) |
| $\gamma_{IM}^{I}$ | parameter | import-share adjustment cost parameter, investment sector | 238 |  |
| $\hat{h}_{G}$ | endogenous | domestic intermediate input into public consumption good | 240 |  |
| $\hat{q}_{G}$ | endogenous | output of final public consumption good, log deviation | 240 |  |
| $\hat{p}_{G}$ | endogenous | relative price of public consumption good, log deviation | 240 |  |
| $\hat{\nu}_{G}$ | shock_process | time-varying home bias, public consumption sector | 240 |  |
| $\widehat{im}_{G}$ | endogenous | imported intermediate input into public consumption good | 241 |  |
| $\hat{\Gamma}_{IM^{G}}^{+}$ | endogenous | import-share adjustment-cost term, public consumption sector | 241 |  |
| $\gamma_{IM}^{G}$ | parameter | import-share adjustment cost parameter, public consumption sector | 242 |  |
| $\hat{h}_{X}$ | endogenous | domestic intermediate input into exported good, log deviation | 244 |  |
| $\hat{q}_{X}$ | endogenous | output of final exports good, log deviation | 244 |  |
| $\hat{p}_{DX}$ | endogenous | domestic-currency relative price of exported good, log deviation | 244 |  |
| $\hat{\nu}_{X}$ | shock_process | time-varying home bias, exports sector | 244 |  |
| $\widehat{im}_{X}$ | endogenous | imported intermediate input into exported good, log deviation | 245 |  |
| $\hat{\Gamma}_{IM^{X}}^{+}$ | endogenous | import-share adjustment-cost term, exports sector | 245 |  |
| $\gamma_{IM}^{X}$ | parameter | import-share adjustment cost parameter, exports sector | 246 |  |
| $\hat{\epsilon}^{X}$ | shock_process | shock in exports import-share cost (printed epsilon^X) | 246 | analogous eqs use epsilon^IM; possible typo |
| $\nu_{x}$ | parameter | home bias in exports (printed lower-case) | 247 | presumably nu_X |
| $\mu_{x}$ | parameter | elasticity of substitution in exports (printed lower-case) | 247 | presumably mu_X |
| $\hat{\pi}_{X}$ | endogenous | export price inflation in foreign currency, deviation | 248 |  |
| $\widehat{mc}^{X}$ | endogenous | exporters' real marginal cost, log deviation | 248 |  |
| $\hat{\varphi}^{X}$ | shock_process | export price markup shock | 248 | curly phi |
| $\hat{p}_{X}$ | endogenous | real export price (foreign currency, vs foreign output deflator) | 249 |  |
| $\hat{g}$ | endogenous | government consumption, log deviation | 251 | (277) equates final government good output to it |
| $\rho_{\tau^{C}}$ | parameter | persistence of consumption tax rate | 252 |  |
| $\hat{\tau}^{D}$ | endogenous | dividend tax rate, deviation | 253 |  |
| $\rho_{\tau^{D}}$ | parameter | persistence of dividend tax rate | 253 |  |
| $\eta^{\tau^{D}}$ | innovation | dividend tax rate innovation | 253 |  |
| $\rho_{\tau^{K}}$ | parameter | persistence of capital rental tax rate | 254 |  |
| $\eta^{\tau^{K}}$ | innovation | capital rental tax rate innovation | 254 |  |
| $\rho_{\tau^{N}}$ | parameter | persistence of household income tax rate | 255 |  |
| $\eta^{\tau^{N}}$ | innovation | household income tax rate innovation | 255 |  |
| $\rho_{\tau^{W_{h}}}$ | parameter | persistence of household payroll tax | 256 |  |
| $\eta^{\tau^{W_{h}}}$ | innovation | household payroll tax innovation | 256 |  |
| $\rho_{\tau^{W_{f}}}$ | parameter | persistence of firm payroll tax | 257 |  |
| $\eta^{\tau^{W_{f}}}$ | innovation | firm payroll tax innovation | 257 |  |
| $\hat{g}_{Y}$ | endogenous | output growth, deviation | 258 |  |
| $\hat{rr}^{fw}$ | endogenous | 5-10 year forward expected real interest rate | 259 | narrow hat over rr in (259); wide hat \widehat{rr}^{fw} in (262); main text writes fwd |
| $y^{GAP}$ | endogenous | output gap: output relative to technology-driven trend | 259 | printed without hat in (259) and (264); main text uses \hat{y}^{GAP} |
| $\Delta\hat{S}$ | endogenous | nominal exchange-rate depreciation | 259 | defined in (263) |
| $\rho_{\bar{\pi}}$ | parameter | persistence of inflation target | 260 | main text (64) sets it to 0.99 |
| $\hat{s}_{TB}$ | endogenous | trade balance to output ratio, deviation | 266 |  |
| $\hat{s}_{X}$ | endogenous | exports to output ratio, deviation | 266 |  |
| $\hat{s}_{IM}$ | endogenous | imports to output ratio, deviation | 266 |  |
| $\left(CA/Y\right)$ | endogenous | current account to output ratio | 269 | no hat printed |
| $\hat{s}_{FTR}$ | shock_process | foreign transfers to output ratio, deviation | 269 | AR(1) in (270) |
| $\hat{\tilde{z}}$ | endogenous | relative level of foreign to domestic technology, deviation | 271 | hat over tilde; \tilde{z}_{t}=z^{*}_{t}/z_{t} (p.100) |
| $\widehat{im}^{*}$ | endogenous | world imports (world trade), log deviation | 271 | main text calls it world trade \widehat{wt}^{*} |
| $\hat{\nu}^{*}$ | shock_process | country-specific export-demand shock | 271 | Greek nu |
| $\hat{p}_{x}$ | endogenous | real export price (foreign currency), deviation | 271 | printed lowercase x in (271) |
| $\hat{p}_{x}^{*}$ | endogenous | price of competing exporters (world-trade price aggregate), deviation | 271 | main text P^{c,*}_{X,t} |
| $r^{*}$ | steady_state | steady-state foreign gross interest rate | 272 |  |
| $\pi^{*}$ | steady_state | steady-state foreign gross inflation | 272 |  |
| $\hat{h}^{s}$ | endogenous | supply of domestic intermediate goods, deviation | 274 | printed \hat{h}_{s,t} (subscript) in (285) |
| $\hat{h}$ | endogenous | production-relevant aggregate of domestic intermediate goods | 274 |  |
| $\hat{\Delta inv}$ | shock_process | inventory investment (share of GDP), deviation | 276 | narrow hat over \Delta inv in (276),(280); \Delta\widehat{inv} in (284) |
| $\hat{k}_{s}$ | endogenous | capital services demanded by firms, deviation | 279 |  |
| $p_{C}$ | steady_state | steady-state relative consumption price | 280 |  |
| $p_{y}$ | steady_state | steady-state relative output price | 280 | printed variously p_{y}, P_{y}, p_{Y}, P_{Y} |
| $im_{C}$ | steady_state | steady-state imports used in consumption good | 280 | also im_{I}, im_{G}, im_{X} for other uses |
| $\hat{p}_{Y}^{M}$ | endogenous | output deflator in market prices, deviation | 284 |  |
| $\tau_{c}$ | steady_state | steady-state consumption tax rate | 284 | printed lowercase c; 0.78 is a fixed weight |
| $\widehat{ri}^{*}$ | endogenous | foreign real interest rate | 286 |  |
| $\widehat{fw}_{ri^{*}}$ | shock_process | foreign forward (natural) real rate | 286 | main text \widehat{rr}^{*,fwd}, near random walk (90) |
| $\hat{\epsilon}_{Y^{*}}$ | innovation | foreign demand (output) shock | 286 | lunate epsilon; main text \varepsilon_{t}^{Y^{*}} |
| $\bar{\pi}^{*}$ | shock_process | foreign inflation target | 287 | bar only, no hat as printed |
| $\hat{\epsilon}_{R^{*}}$ | innovation | foreign monetary policy shock | 287 | lunate epsilon |
| $c_{wt,-}^{*}$ | parameter | world imports persistence | 289 | star printed here only |
| $\hat{\epsilon}_{IM^{*}}$ | innovation | world import (trade) shock | 289 | printed \hat{\epsilon}_{IM_{t}^{*}} |
| $c_{OIL,-}$ | parameter | oil price persistence coefficient | 290 |  |
| $c_{OIL,\Delta}$ | parameter | oil price lagged-change coefficient | 290 | enters with minus sign here |
| $EX_{\Delta N}$ | shock_process | common excess trend in per-capita hours growth | 291 | AR(1) in (322); enters all domestic real growth rates |
| $EX_{\Delta C}$ | shock_process | excess trend in consumption growth | 292 | AR(1) in (323) |
| $\Delta I_{NI}$ | observable | observed real per-capita fixed investment growth (excluding inventories) | 293 |  |
| $EX_{\Delta INI}$ | shock_process | excess trend in fixed-investment growth | 293 | AR(1) in (324) |
| $EX_{\Delta G}$ | shock_process | excess trend in government consumption growth | 294 | no own process; pinned down by (328) |
| $EX_{\Delta X}$ | shock_process | excess trend in export growth | 295 | AR(1) in (326) |
| $EX_{\Delta IM}$ | shock_process | excess trend in import growth | 296 | AR(1) in (325) |
| $\hat{\epsilon}_{OB\_DPY}$ | shock_process | observation error in GDP-deflator inflation | 297 | lunate epsilon with hat; Table 3: obs. error output def. |
| $\pi$ | steady_state | gross steady-state (target) inflation rate | 297 | enters as \pi-1 |
| $\Delta P_{I}$ | observable | observed investment-deflator inflation | 299 |  |
| $\eta^{\Delta P_{I}}$ | innovation | measurement error in investment-deflator inflation | 299 |  |
| $\hat{e}$ | endogenous | per-capita employment, deviation from HP trend | 301 | written \widehat{EM} in eq. (95) |
| $\hat{\epsilon}_{OB\_E}$ | shock_process | observation shock in the employment equation | 301 | lunate epsilon with hat; Table 3 gives its AR coefficient |
| $EX_{\Delta W}$ | shock_process | excess trend in nominal wage growth | 304 | AR(1) in (321) |
| $r$ | steady_state | gross steady-state domestic nominal interest rate | 305 | enters as r-1 |
| $EX_{\Delta S}$ | shock_process | excess trend in nominal depreciation | 306 | AR(1) in (320) |
| $EX_{\Delta Y*}$ | shock_process | excess trend in foreign output growth | 307 | asterisk inline in subscript; AR(1) in (329) |
| $\Delta P_{Y^{*}}$ | observable | observed foreign price inflation (G4 CPI) | 308 |  |
| $R^{*OB}$ | observable | observed annualized foreign (G4) nominal interest rate | 309 | data list writes r_{t}^{*,OB} |
| $\Delta P_{X^{*}}$ | observable | inflation in foreign competitors' price | 310 | not in the data list of section 4.1 |
| $rr^{fwd\_ob}$ | observable | observed domestic 5-10 year forward real interest rate | 312 |  |
| $\hat{\epsilon}_{fwd\_ob}$ | shock_process | observation error in the domestic forward real rate | 312 | lunate epsilon with hat; serially correlated (Appendix B) |
| $\hat{fw}_{ri^{*}}$ | endogenous | forward real-rate term as printed in (312) | 312 | narrow hat over fw; same letters as \widehat{fw}_{ri^{*}}; see notes |
| $S_{CA}$ | observable | observed current-account-to-GDP ratio | 313 | capital S as printed; data list writes s_{CA,t} |
| $(CA/Y)$ | endogenous | model current-account-to-GDP ratio | 313 |  |
| $\tau^{C\_OB}$ | observable | observed consumption (VAT) tax rate | 314 |  |
| $\hat{\tau}^{c}$ | shock_process | consumption tax-rate deviation | 314 | lowercase c as printed; (252) writes \hat{\tau}^{C} |
| $\tau^{N\_OB}$ | observable | observed income tax rate | 315 |  |
| $\tau_{n}$ | steady_state | steady-state income tax rate | 315 | lowercase n as printed |
| $\hat{\tau}^{n}$ | shock_process | income tax-rate deviation | 315 | lowercase n as printed; (255) writes \hat{\tau}^{N} |
| $\Delta P_{OIL}$ | observable | observed change in oil prices | 316 | data list writes \Delta P_{OIL,t}^{*} |
| $EX_{\Delta POIL}$ | shock_process | excess trend in oil-price changes | 316 | AR(1) in (331), printed there as EX_{\Delta POil} |
| $\Delta \widehat{inv}$ | endogenous | change in inventories (share of GDP), model deviation | 317 | wide hat over inv only |
| $EX_{\Delta INV}$ | shock_process | excess term in the inventory share | 317 | white noise in (327) |
| $r^{*fwd\_ob}$ | observable | observed foreign 5-10 year forward nominal interest rate | 318 |  |
| $\hat{\epsilon}_{fwd\_ob^{*}}$ | shock_process | observation error in the foreign forward nominal rate | 318 | lunate epsilon with hat |
| $EX_{\Delta WT*}$ | shock_process | excess trend in world import growth | 319 | asterisk inline in subscript; AR(1) in (330) |
| $\rho_{EX}^{\Delta S}$ | parameter | AR(1) coefficient of the depreciation excess trend | 320 |  |
| $\rho_{EX}^{\Delta W}$ | parameter | AR(1) coefficient of the wage excess trend | 321 |  |
| $g_{\Delta W}$ | parameter | assumed long-run gross growth rate of nominal wages | 321 |  |
| $\eta_{EX}^{\Delta INV}$ | innovation | innovation (white noise) to the inventory-share excess term | 327 |  |
| $c/y$ | steady_state | steady-state consumption-to-output ratio | 328 | weight in (328) |
| $i/y$ | steady_state | steady-state investment-to-output ratio | 328 | weight in (328) |
| $im/y$ | steady_state | steady-state import-to-output ratio | 328 | weight in (328) |
| $g_{\Delta WT*}$ | parameter | assumed long-run gross growth rate of world imports | 330 | asterisk inline in subscript |
| $EX_{\Delta POil}$ | shock_process | excess trend in oil-price changes (as printed in 331) | 331 | presumably the same as EX_{\Delta POIL} in (316) |
