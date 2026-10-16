# Impulse-response data extracted from MOISE (Argov et al. 2012), Figures 6–18

Source: Argov, Barnea, Binyamini, Borenstein, Elkayam and Rozenshtrom (2012), *MOISE: A DSGE
Model for the Israeli Economy*, Bank of Israel Discussion Paper 2012.06. PDF page = printed
page + 6.

These CSVs are **replication-test targets**. They are the values the paper *plots*, read out of
the PDF's vector graphics. They are not numbers printed by the authors.

## Files

| file | content |
|---|---|
| `figNN_<shock>.csv` | one file per figure, long format: `figure, page_pdf, shock, panel_title, series, quarter, value` (12 panels × 5 series × 20 quarters = 1,200 rows) |
| `panel_calibration.csv` | one row per panel (156): tick labels and tick positions, fitted PDF→value and PDF→quarter maps, fit residuals, plot limits, resolution, and all per-panel check results |
| `figures.json` | per figure: printed title, units (paraphrased from the caption), name of the MATLAB file embedded in the PDF, scale, etc. |
| `raster_crosscheck.csv` | independent raster cross-check, one row per panel (see Validation) |
| `spotcheck_points.csv` | the 39 points spot-checked by eye (3 per figure) |
| `check_figNN.png` | re-plot of the extracted data in the paper's 4×3 panel layout |
| `scripts/extract_irf.py` | the extraction (vector graphics → CSV). Rerun it with your own copy of the paper (the PDF is not in this repo): `python3 scripts/extract_irf.py --pdf path/to/dp12065e.pdf --out .` |
| `scripts/make_check_plots.py` | writes `check_figNN.png` |
| `scripts/raster_crosscheck.py` | writes `raster_crosscheck.csv` |

Values have 6 decimals. Rerunning `extract_irf.py` reproduces the CSVs byte for byte. This was checked.

## Figures and panels

| Fig | PDF p. (printed) | shock (`shock` column) | caption title | MATLAB file embedded in the PDF |
|---|---|---|---|---|
| 6 | 80 (74) | `interest_rate` | Impulse Response to an Interest Rate Shock | `BaysianIRF_ETA_R.pdf` |
| 7 | 82 (76) | `external_risk_premium` | … to an External Risk Premium Shock | `BaysianIRF_ETA_RP_FX.pdf` |
| 8 | 84 (78) | `symmetric_premium` | … to a Symmetric Premium Shock | `BaysianIRF_ETA_RP.pdf` |
| 9 | 86 (80) | `foreign_demand` | … to a Foreign Demand Shock | `BaysianIRF_ETA_Y_ROW.pdf` |
| 10 | 88 (82) | `transitory_technology` | … to a Transitory Technology Shock | `BaysianIRF_ETA.pdf` |
| 11 | 133 (127) | `domestic_price_markup` | … to a Domestic Price Markup Shock | `BaysianIRF_ETA_H.pdf` |
| 12 | 134 (128) | `import_price_markup` | … to an Import Price Markup Shock | `BaysianIRF_ETA_PIM.pdf` |
| 13 | 135 (129) | `oil_price` | … to an Oil Price Shock | `BaysianIRF_ETA_P_OIL.pdf` |
| 14 | 136 (130) | `investment_specific_technology` | … to an Investment Specific Technology Shock | `BaysianIRF_ETA_I.pdf` |
| 15 | 137 (131) | `export_share` | … to an Export Share Shock | `BaysianIRF_ETA_NU_ROW.pdf` |
| 16 | 138 (132) | `home_bias` | … to a Home Bias Shock | `BaysianIRF_ETA_NU.pdf` |
| 17 | 139 (133) | `wage_markup` | … to a Wage Markup Shock | `BaysianIRF_ETA_W.pdf` |
| 18 | 140 (134) | `inventories_investment_demand` | … to an Inventories Investment Demand Shock | `BaysianIRF_ETA_DINV.pdf` |

Each figure sits on a single page; there are no continuation pages. The script matches the figure
title on every page exactly. Section 6.2 (PDF p. 79) names the shocks of Figs 6–10 as
η^R, η^{RP*}, η^{RP}, η^{Y*} and η. The embedded file names match these, plus the Appendix E shocks.

All 13 figures share the same 12 panels in the same order (row by row): Output, Consumption,
Fixed investment / Exports, Imports, Hours worked / Interest rate, Real wage, Real exchange rate /
CPI inflation, Domestic inflation, Imported inflation. That makes 156 panels, all extracted.

## Units (as stated on the figures)

The note under every figure states (paraphrased): the shock is one standard deviation; the solid line is the mean impulse response and the gray areas are the 70% and 90% highest-probability intervals; real variables are in percent deviation from steady state, inflation in percentage-point deviation, and the interest rate in annualized percentage-point deviation.

So:

* **Output, Consumption, Fixed investment, Exports, Imports, Hours worked, Real wage, Real exchange
  rate**: percentage deviation from steady state. A clipped note inside the MATLAB file says
  "non-stochastic steady state".
* **CPI, Domestic, Imported inflation**: percentage-point deviation from steady state. The figures
  do not say whether this is quarterly or annualized.
* **Interest rate**: annualized percentage-point deviation from steady state.
* **x axis**: quarters after the shock. Points are plotted at q = 1…20 (the axis runs 0–20, and
  nothing is plotted at q = 0), so `quarter` 1 is the impact period.
* The shock is one standard deviation, and the IRFs are posterior means over parameter **and**
  shock-size draws (§6.2). This matters when comparing with a single posterior-mode IRF.

`panel_calibration.csv` has a `units` column. The CSVs keep the figure's numbers unchanged: no
rescaling, no sign changes.

## Method

1. **What the PDF contains.** Every figure is a MATLAB-exported PDF embedded as a form XObject.
   It is scaled 0.9 on the page, or 0.6 for Fig 11 (Appendix E's first page). pdfplumber
   flattens it to page coordinates. Each panel is drawn as: a frame (rect plus lines), tick marks
   (short lines on all four edges) and Helvetica tick labels (y labels left, x labels 0/10/20
   below). Then, in this order:
   * four filled polygons with grays 1.0 (white), 0.80, 0.65 and 0.80;
   * one stroked black polyline, three times the axes line width;
   * a black horizontal line, twice the axes line width.

   That makes 60 curves per page, and the script checks this: every curve on the page lies
   inside exactly one panel, five per panel.
2. **Calibration (per panel).** The y tick marks are found on the left and right frame edges; the
   two sets must match. Each Helvetica label (the U+2212 minus is handled) is matched to the
   nearest tick. The script checks that the labels are evenly spaced and that every label sits at
   the same offset from its tick. A straight line is then fitted through all (label value, tick
   position) pairs, giving page y as a linear function of value. The same is done for x with
   0/10/20. All coordinates lie on the MATLAB file's 1/12-pt grid: 0.075 pt on the page, or
   0.05 pt for Fig 11. The tick fits are linear to within that grid rounding: worst residual
   0.40 grid units (y) and 0.34 (x) over all 156 panels.
   *Resolution*: one grid unit is 1/1200 of the axis range, about 0.08 % of the axis span.
   It ranges from 5e-5 to 0.0067 value units depending on the panel; see the
   `value_per_grid_unit` column.
3. **Decoding the lines.** Every vertex x maps to an integer quarter to within 0.011 quarter. The
   black polyline gives the mean directly. The four filled polygons form a MATLAB stacked area
   plot. Each polygon runs forward along its new upper boundary from q1 to q20, then back along
   the previous boundary. Polygon k's backward chain is identical to polygon k−1's forward chain
   (checked: 0.0 difference). The white base polygon's backward chain is the y = 0 line (checked).
   So the boundaries, bottom to top, are: 90 % lower, 70 % lower, 70 % upper, 90 % upper.
   The PDF paths hold 25,242 vertices. The PDF writer had dropped another 3,453 where consecutive
   points were collinear, which shows up as gaps of more than one quarter. **All 3,453 gaps lie on
   exactly flat runs**, so re-inserting the missing points is exact; the script verifies flatness
   and stops if a run is not flat.
4. **Series names.** `mean`, `hpd70_lower`, `hpd70_upper`, `hpd90_lower`, `hpd90_upper`.

## How the lines were identified

* **Mean**: the caption says "Solid line – mean". The only solid, thick black line in each panel
  is the 3×-width polyline. The thin black horizontal line maps to the value 0 in every panel
  (|value| ≤ 0.001, i.e. under one grid unit), so it is the zero reference and is not exported.
* **Bands**: the caption gives two gray intervals, 70 % and 90 % HPD. The dark gray area (0.65)
  lies inside the light gray (0.80). A narrower interval must lie inside a wider one, so dark is
  70 % and light is 90 %. This is confirmed three ways: (i) the polygon stacking order; (ii) a
  check that 90lo ≤ 70lo ≤ 70hi ≤ 90hi at every point (0 violations across 3,120 quarter
  points); and (iii) the raster check (below): in none of the 6,084 sampled pixel columns does the
  top-to-bottom colour order depart from white–light–dark–light–white.
* The mean lies inside the 90 % band at every point, and inside the 70 % band at all but one point.
  The exception is Fig 18, Hours worked, q12: the mean is 0.0012 above `hpd70_upper`, i.e. one grid
  unit. That is how the PDF draws it, not an extraction error. An HPD interval need not contain
  the mean.
* No other line types or styles exist in these figures: no dashes, no legend, no second variant.

## Validation

* **Built-in checks** (the script stops on failure): page title; panel titles and order; 4×3 grid;
  left/right and top/bottom ticks agree; labels evenly spaced; linear tick fit within grid rounding;
  frame edges at the extreme ticks; fill grays and stroke widths; zero line at value 0; all vertices
  on the 1/12-pt grid; integer quarters 1…20; shared polygon boundaries identical; dropped vertices
  flat; every curve assigned to a panel. No data value lies on a frame edge, so nothing was
  clipped.
* **Re-plots**: `check_figNN.png` was viewed next to the page crops for all 13 figures. They were
  also composited side by side with a pdftoppm render of the original. Shapes, signs, peaks and
  troughs, crossing points, y tick ranges and panel order match in all 156 panels.
* **Spot checks by zooming the original**: 3 points per figure, 39 in total, listed in
  `spotcheck_points.csv`. They include q1 means, peaks/troughs, and 90 % band corners. For each
  point, a 24 pt window around the extracted point was rendered at 1200 dpi with a cross-hair
  centred on it. In all 39 cases the line end, vertex or band corner sits at the cross-hair
  centre. Examples: Fig 6 interest rate q1 = 0.781 (§6.2: "immediate rise … of 0.75 percentage
  points"); Fig 10 real exchange rate q3 = 1.392 (§6.2: "peaks at 1.4 percent"); Fig 8 exports
  q5 = 0.699 (§6.2: "up to 0.7 percent").
* **Independent raster cross-check** (`raster_crosscheck.csv`). Every panel is rendered with
  Poppler, a different PDF engine, at 1200 dpi without anti-aliasing. The axis is re-calibrated
  from the tick marks *in the raster*. Band edges (20,033 measured) and mean-line centres (2,480)
  are then measured in 39 columns per panel and compared with the CSV polylines:
  * band-edge distance: median 0.6 px, max 2.1 px;
  * mean-line distance: median 0.3 px, max 1.4 px;
  * the largest difference is 0.2 % of the panel's axis range.

  1 px = 0.06 pt, so the agreement is within about 1–2 grid units, which is renderer pixel
  snapping. There were 0 colour-order violations, and 0 edges were missing except where a black
  line covers them.
* **Text consistency** (§6.2 compared with the extracted means).
  These agree:
  * Fig 6: output trough −0.233 at q2 (text: "approximately 0.2 percent … lowest level only after
    two quarters"); CPI inflation summed over q1–4 = −0.41 (text: "accumulated effect after one
    year is about 0.4 percentage points").
  * Fig 7: interest rate 0.51 on impact (text: 0.5); output peak 0.32 (text: "approximately 0.3").
  * Fig 8: consumption −1.08 and investment −1.88 on impact (text: "about one and two percent");
    exports peak 0.70 (text: "up to 0.7").
  * Fig 9: output peak 0.398 (text: "approximately 0.4").
  * Fig 10: real exchange rate peak 1.392 (text: "peaks at 1.4 percent"); CPI inflation summed
    over q1–4 = −0.27 (text: "reduced by 0.3 percentage points").

  These are looser in the text than in the plot:
  * Fig 7 interest-rate peak 0.85 at q3 vs "up to 1.0 … within three quarters";
  * Fig 7 exports peak 0.79 vs "approximately 0.5 percent";
  * Fig 9 exports peak 2.84 vs "approximately two percent".

  The original figure shows the same values (Fig 7 exports peak just below the "1" tick; Fig 9
  exports peak confirmed by zoom), so the difference comes from the text, not the extraction.
  Treat the figures as the target.

## Precision to assume in tests

* Accuracy of the reading itself: within about ±1 grid unit, i.e. ±1/1200 of the panel's axis
  range (`value_per_grid_unit`, per panel). This combines two roundings in the MATLAB→PDF export:
  ±0.5 grid unit for the data point itself, and up to 0.4 grid units of tick-position rounding
  in the calibration. Use that as the tolerance floor.
* The plotted numbers are means of a posterior simulation. A re-implementation will reproduce them
  only up to Monte-Carlo noise and the posterior draws used, so realistic test tolerances are much
  wider than the reading precision. The 70/90 % HPD bands are particularly noisy.

## Not extracted / caveats

* Nothing in Figures 6–18 was left out. All 156 panels × 5 series × 20 quarters are in the CSVs.
* The zero reference line is not exported. The axis frames, ticks and labels are kept only as
  calibration (`panel_calibration.csv`).
* The figures do not say whether inflation is quarterly or annualized; only the interest rate is
  stated as annualized. *Inference, not stated*: summing Fig 6's CPI inflation over q1–4 gives
  −0.41, which matches the text's "accumulated effect after one year … about 0.4 percentage points".
  That fits non-annualized quarterly rates.
* `quarter` 1 is the first plotted point (the impact period); there is no q0 point in the PDF.
* The visible LaTeX caption is the same on all 13 pages; Fig 11's differs only in line breaks and
  spacing. Each embedded MATLAB file also carries its own note, clipped out of view, with the same
  content in different words. Both texts are stored in `figures.json`.
* Other figures of the paper (e.g. Figs 1–5: model structure, estimation and evaluation charts)
  were out of scope.
