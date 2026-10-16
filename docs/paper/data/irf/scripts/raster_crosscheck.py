#!/usr/bin/env python3
"""Independent raster cross-check of the vector extraction (extract_irf.py).

Every panel is rendered with Poppler (pdftoppm, a different PDF engine from the
pdfminer/pdfplumber parser used for the extraction) at 1200 dpi, grey, without
anti-aliasing, so that every pixel has exactly one of the four paint values
(white 255, light grey 204, dark grey 166, black 0).  Then, using ONLY the raster
(plus the printed tick-label values):
  * the frame lines and the y tick marks are located in pixels and the y-axis is
    re-calibrated from the tick marks (value = a + b * pixel row; the y=0 tick is
    left out of the fit when it is merged with the 2x wider zero line);
  * quarters are located from the left/right frame lines (q = 0 / 20; the right
    line's centre is taken from its never-overpainted outer edge);
  * in pixel columns at q = 1.1, 1.5, 2, 2.5, ..., 19.5, 19.9 the band edges are
    measured as colour transitions (white->light = 90% upper, light->dark = 70%
    upper, dark->light = 70% lower, light->white = 90% lower), and at q = 1.5, ...,
    19.5 the centre of the thick black line (= mean; centred on the segment there)
    is measured;
  * each measured edge pixel is compared with the polyline implied by the extracted
    CSV values (mapped with the RASTER calibration): reported both as the vertical
    row difference and as the Euclidean distance to that polyline (the meaningful
    one on steep segments).  Edges covered by a black line are counted as hidden.
It also checks the top-to-bottom colour order in every column (white, light, dark,
light, white), which confirms that the dark band is the inner (70%) band.

Usage: python3 raster_crosscheck.py [--pdf PATH] [--dir docs/paper/data/irf]
Writes <dir>/raster_crosscheck.csv (one row per panel) and prints a summary.
"""
import argparse
import csv
import json
import os
import subprocess
import tempfile

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DPI = 1200
W_, L_, D_, K_ = 0, 1, 2, 3          # classes: white, light grey, dark grey, black
CLASS_NAMES = "WLDK"


def read_pgm(fn):
    data = open(fn, "rb").read()
    toks, i = [], 0
    while len(toks) < 4:
        while data[i:i + 1].isspace():
            i += 1
        if data[i:i + 1] == b"#":
            while data[i:i + 1] not in (b"\n", b""):
                i += 1
            continue
        j = i
        while not data[j:j + 1].isspace():
            j += 1
        toks.append(data[i:j])
        i = j
    i += 1
    w, h = int(toks[1]), int(toks[2])
    return np.frombuffer(data[i:i + w * h], dtype=np.uint8).reshape(h, w)


def render(pdf, page, box_pt, dpi, aa):
    x0, t0, x1, t1 = box_pt
    X, Y = int(np.floor(x0 * dpi / 72)), int(np.floor(t0 * dpi / 72))
    W, H = int(np.ceil(x1 * dpi / 72)) - X, int(np.ceil(t1 * dpi / 72)) - Y
    cmd = ["pdftoppm", "-gray", "-r", str(dpi), "-f", str(page), "-l", str(page),
           "-x", str(X), "-y", str(Y), "-W", str(W), "-H", str(H), "-singlefile"]
    if not aa:
        cmd += ["-aa", "no", "-aaVector", "no"]
    with tempfile.TemporaryDirectory() as td:
        base = os.path.join(td, "r")
        subprocess.run(cmd + [pdf, base], check=True)
        return read_pgm(base + ".pgm"), X, Y


def classify(img):
    c = np.full(img.shape, -1, dtype=np.int8)
    c[img >= 250] = W_
    c[(img >= 195) & (img <= 215)] = L_
    c[(img >= 155) & (img <= 175)] = D_
    c[img < 100] = K_
    return c


def runs(mask):
    """Start/stop (exclusive) of True runs in a 1-D boolean array."""
    m = np.concatenate([[False], mask, [False]]).astype(int)
    d = np.diff(m)
    return list(zip(np.where(d == 1)[0], np.where(d == -1)[0]))


def locate(img, approx_px, scale, dark=100):
    """Frame lines, y-tick rows and the zero-line rows of one panel, from the raster only."""
    K = img < dark
    fx0, ft0, fx1, ft1 = approx_px
    h = ft1 - ft0
    rows = slice(int(ft0 + 0.1 * h), int(ft1 - 0.1 * h))
    # left frame line: the leftmost column that is black over the inner 80% of the frame height
    frac = K[rows, :].mean(axis=0)
    cand = [r for r in runs(frac > 0.97) if abs((r[0] + r[1]) / 2 - fx0) < 20]
    assert len(cand) == 1, f"left frame line not found {cand}"
    L = (cand[0][0] + cand[0][1]) / 2.0
    lw_px = cand[0][1] - cand[0][0]
    # right frame line: the band polygons end exactly on its centre line and are painted
    # after it, so its inner half is over-painted wherever a band (or the invisible white
    # base polygon) reaches q20.  Its outer edge is never over-painted: centre = modal
    # outer edge - half the line width measured on the (clean) left frame line.
    ends = []
    for r in range(rows.start, rows.stop):
        for a_, b_ in runs(K[r, :]):
            if a_ - 3 <= fx1 <= b_ + 3:
                ends.append(b_)
    assert ends, "right frame line not found"
    vals, cnts = np.unique(ends, return_counts=True)
    R = float(vals[np.argmax(cnts)]) - lw_px / 2.0
    # y ticks: black runs in a column just inside the left frame line (between the line and q1)
    strip = int(round(L + 0.6 * scale / 0.9 * DPI / 72))
    tr = [r for r in runs(K[:, strip]) if ft0 - 20 < (r[0] + r[1]) / 2 < ft1 + 20]
    centres = [(a + b) / 2.0 for a, b in tr]
    widths = [b - a for a, b in tr]
    return L, R, strip, centres, widths, tr


def measure_column(cls, col, top_run, bot_run):
    """Class sequence of one column strictly inside the frame (between the edge black runs)."""
    seq = cls[:, col].copy()
    lo, hi = top_run[1], bot_run[0]            # first row below the top edge run, row of bottom edge run
    # extend past black pixels glued to the edge runs (e.g. x-ticks, zero line on the frame edge)
    while lo < hi and seq[lo] == K_:
        lo += 1
    while hi > lo and seq[hi - 1] == K_:
        hi -= 1
    return seq, lo, hi


def find_transition(seq, lo, hi, pred, above, below, win):
    """Row j (edge between j-1 and j) with seq[j-1] in above and seq[j] in below, nearest to pred."""
    best = None
    a = max(lo + 1, int(np.floor(pred - win)))
    b = min(hi - 1, int(np.ceil(pred + win)))
    for j in range(a, b + 1):
        if seq[j - 1] in above and seq[j] in below:
            if best is None or abs(j - pred) < abs(best - pred):
                best = j
    return best


def order_ok(seq, lo, hi):
    """Top-to-bottom colour order (ignoring black and runs <= 2 px) must be a subsequence of W L D L W."""
    s = seq[lo:hi]
    rr = []
    for c in (W_, L_, D_):
        for a, b in runs(s == c):
            if b - a > 2:
                rr.append((a, c))
    order = [c for _, c in sorted(rr)]
    comp = [order[0]] if order else []
    for c in order[1:]:
        if c != comp[-1]:
            comp.append(c)
    target = [W_, L_, D_, L_, W_]
    i = 0
    for c in comp:
        while i < len(target) and target[i] != c:
            i += 1
        if i == len(target):
            return False, "".join(CLASS_NAMES[c] for c in comp)
        i += 1
    return True, "".join(CLASS_NAMES[c] for c in comp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.abspath(os.path.join(HERE, "..")))
    ap.add_argument("--pdf", default=os.path.abspath(os.path.join(HERE, "..", "..", "..", "moise.pdf")))
    a = ap.parse_args()
    figs = json.load(open(os.path.join(a.dir, "figures.json")))
    calib = list(csv.DictReader(open(os.path.join(a.dir, "panel_calibration.csv"))))
    import pdfplumber  # only to get approximate panel boxes for cropping
    pdf = pdfplumber.open(a.pdf)
    out_rows = []
    tot = dict(edge_meas=0, edge_occl=0, edge_degen=0, edge_missing=0, mean_meas=0, mean_occl=0, order_bad=0, cols=0)
    all_edge_d, all_mean_d, all_edge_p, all_mean_p = [], [], [], []
    worst, missing = [], []
    for f in figs:
        data = {}
        for r in csv.DictReader(open(os.path.join(a.dir, f["csv"]))):
            data.setdefault(r["panel_title"], {}).setdefault(r["series"], np.zeros(20))[int(r["quarter"]) - 1] = float(r["value"])
        p = pdf.pages[f["page_pdf"] - 1]
        frames = sorted([r for r in p.rects if r["stroke"]], key=lambda r: (round(r["top"]), r["x0"]))
        scale = f["scale"]
        for c in sorted([c for c in calib if int(c["figure"]) == f["figure"]], key=lambda c: int(c["panel"])):
            fr = frames[int(c["panel"]) - 1]
            m = 4.0 * scale
            box = (fr["x0"] - m, fr["top"] - m, fr["x1"] + m, fr["bottom"] + m)
            img, X, Y = render(a.pdf, f["page_pdf"], box, DPI, aa=False)
            approx = (fr["x0"] * DPI / 72 - X, fr["top"] * DPI / 72 - Y, fr["x1"] * DPI / 72 - X, fr["bottom"] * DPI / 72 - Y)
            L, R, strip, centres, widths, truns = locate(img, approx, scale)
            labels = sorted([float(t) for t in c["y_tick_labels"].split(";")], reverse=True)
            assert len(centres) == len(labels), f"fig{f['figure']} {c['panel_title']}: {len(centres)} tick runs vs {len(labels)} labels"
            # the y=0 tick is overdrawn by the (2x wider) zero line; when 0 is on the top/bottom
            # frame edge the zero line is clipped to the axes, so that merged run is off-centre.
            # Fit only runs with the plain tick/frame-line width.
            w0 = min(widths)
            keep = [i for i, wd in enumerate(widths) if wd <= w0 + 2]
            assert len(keep) >= 2
            cfit, lfit = np.array(centres)[keep], np.array(labels)[keep]
            b, a0 = np.polyfit(cfit, lfit, 1)                 # value = a0 + b * row
            tick_res_px = np.max(np.abs(lfit - (a0 + b * cfit))) / abs(b)
            row_of = lambda v: (v - a0) / b
            # vector calibration expressed in the same pixel frame, for comparison
            vec_zero_row = float(c["top_of_zero_pt"]) * DPI / 72 - Y
            vec_px_per_unit = float(c["pt_per_unit"]) * DPI / 72
            cal_zero_diff_px = row_of(0.0) - vec_zero_row
            cal_scale_rel = (1 / abs(b)) / vec_px_per_unit - 1
            vec_L = fr["x0"] * DPI / 72 - X
            vec_R = fr["x1"] * DPI / 72 - X
            cls = classify(img)
            top_run, bot_run = truns[0], truns[-1]
            d = data[c["panel_title"]]
            qgrid = np.arange(1, 21)
            interp = lambda s, q: float(np.interp(q, qgrid, d[s]))
            px_per_q = (R - L) / 20.0
            xs_poly = L + qgrid * px_per_q

            def slope_px(s, q):
                """Steepest local slope of series s around quarter q, in rows per pixel column."""
                k = int(min(max(np.floor(q), 1), 19))
                sl = [(row_of(d[s][k]) - row_of(d[s][k - 1])) / px_per_q]
                if abs(q - round(q)) < 0.25 and 1 < round(q) < 20:
                    k2 = int(round(q))
                    sl += [(row_of(d[s][k2 - 1]) - row_of(d[s][k2 - 2])) / px_per_q,
                           (row_of(d[s][k2]) - row_of(d[s][k2 - 1])) / px_per_q]
                return max(sl, key=abs)

            def poly_dist(s, x, y):
                """Signed (by vertical side) Euclidean distance from pixel (x, y) to the predicted
                polyline of series s (vertices at the integer quarters)."""
                ys = row_of(d[s])
                best = np.inf
                for i in range(19):
                    x0_, y0_, x1_, y1_ = xs_poly[i], ys[i], xs_poly[i + 1], ys[i + 1]
                    vx, vy = x1_ - x0_, y1_ - y0_
                    t = min(max(((x - x0_) * vx + (y - y0_) * vy) / (vx * vx + vy * vy), 0.0), 1.0)
                    best = min(best, np.hypot(x - (x0_ + t * vx), y - (y0_ + t * vy)))
                return best * np.sign(y - row_of(interp(s, (x - L) / px_per_q)))

            # differences are measured vertically (rows) and as the true Euclidean distance to the
            # predicted polyline: on steep segments a sub-pixel horizontal offset of the rasteriser
            # shows up as a large vertical difference.
            edge_d, mean_d, edge_p, mean_p = [], [], [], []
            n_occl = n_degen = n_missing = n_mean_occl = n_bad = 0
            bad_orders = []
            win = 30
            qs = [1.1] + [x / 2 for x in range(3, 40)] + [19.9]
            # zero line rows (the thick run in the strip column nearest value 0)
            zr = min(truns, key=lambda r: abs((r[0] + r[1]) / 2 - row_of(0.0)))
            for q in qs:
                col = int(np.floor(L + q * (R - L) / 20))
                qc = ((col + 0.5) - L) / (R - L) * 20
                seq, lo, hi = measure_column(cls, col, top_run, bot_run)
                ok, comp = order_ok(seq, lo, hi)
                tot["cols"] += 1
                if not ok:
                    n_bad += 1
                    bad_orders.append(f"q{q}:{comp}")
                vals = {s: interp(s, qc) for s in ("hpd90_upper", "hpd70_upper", "hpd70_lower", "hpd90_lower", "mean")}
                specs = [("hpd90_upper", {W_}, {L_, D_}), ("hpd70_upper", {L_, W_}, {D_}),
                         ("hpd70_lower", {D_}, {L_, W_}), ("hpd90_lower", {L_, D_}, {W_})]
                for s, above, below in specs:
                    pred = row_of(vals[s])
                    sl = slope_px(s, qc)
                    j = find_transition(seq, lo, hi, pred, above, below, win * np.sqrt(1 + sl * sl))
                    if j is not None:
                        edge_d.append(j - pred)
                        edge_p.append(poly_dist(s, col + 0.5, j))
                        worst.append((abs(edge_p[-1]), f["figure"], c["panel_title"], s, round(qc, 3),
                                      round(j - pred, 2), round(edge_p[-1], 2), round(sl, 2)))
                        continue
                    jj = int(round(pred))
                    # an edge is hidden when a black line (mean, zero line, frame) covers it; on a
                    # steep segment the thick mean line covers many more rows vertically
                    reach = int(np.ceil(4 * np.sqrt(1 + sl * sl)))
                    near = seq[max(lo, jj - reach):min(hi, jj + reach + 1)]
                    if pred <= lo + 2 or pred >= hi - 2 or np.any(near == K_):
                        n_occl += 1
                    else:
                        # zero-width band here? (neighbouring edge within 2 px)
                        nb = {"hpd90_upper": "hpd70_upper", "hpd70_upper": "hpd70_lower",
                              "hpd70_lower": "hpd70_upper", "hpd90_lower": "hpd70_lower"}[s]
                        if abs(row_of(vals[nb]) - pred) < 3:
                            n_degen += 1
                        else:
                            n_missing += 1
                            jj0, jj1 = max(lo, jj - 12), min(hi, jj + 13)
                            missing.append((f["figure"], c["panel_title"], s, round(qc, 3), round(pred, 1),
                                            "".join("WLDK"[v] if v >= 0 else "?" for v in seq[jj0:jj1])))
                if abs(q - round(q)) > 0.25:              # half-quarter columns: mean line is a straight segment there
                    pred = row_of(vals["mean"])
                    sl = slope_px("mean", qc)
                    Kc = seq == K_
                    cand = [(r0 + lo, r1 + lo) for r0, r1 in runs(Kc[lo:hi])]
                    # drop black runs that touch the zero line rows
                    cand = [r for r in cand if r[1] <= zr[0] - 1 or r[0] >= zr[1] + 1]
                    cand = [r for r in cand if abs((r[0] + r[1]) / 2 - pred) < win * np.sqrt(1 + sl * sl)]
                    if len(cand) == 1 and cand[0][0] > lo and cand[0][1] < hi:
                        dv = (cand[0][0] + cand[0][1]) / 2 - pred
                        mean_d.append(dv)
                        mean_p.append(poly_dist("mean", col + 0.5, (cand[0][0] + cand[0][1]) / 2))
                    else:
                        n_mean_occl += 1
            edge_d, mean_d = np.array(edge_d), np.array(mean_d)
            edge_p, mean_p = np.array(edge_p), np.array(mean_p)
            all_edge_d += list(edge_d)
            all_mean_d += list(mean_d)
            all_edge_p += list(edge_p)
            all_mean_p += list(mean_p)
            tot["edge_meas"] += len(edge_d)
            tot["edge_occl"] += n_occl
            tot["edge_degen"] += n_degen
            tot["edge_missing"] += n_missing
            tot["mean_meas"] += len(mean_d)
            tot["mean_occl"] += n_mean_occl
            tot["order_bad"] += n_bad
            px_val = abs(b)
            out_rows.append(dict(
                figure=f["figure"], panel=c["panel"], panel_title=c["panel_title"],
                raster_tick_fit_max_resid_px=f"{tick_res_px:.2f}",
                raster_vs_vector_zero_row_px=f"{cal_zero_diff_px:+.2f}",
                raster_vs_vector_scale_rel=f"{cal_scale_rel:+.2e}",
                raster_vs_vector_left_px=f"{L - vec_L:+.2f}", raster_vs_vector_right_px=f"{R - vec_R:+.2f}",
                columns=len(qs), colour_order_violations=n_bad,
                edges_measured=len(edge_d), edges_hidden_by_black=n_occl, edges_zero_width=n_degen,
                edges_not_found=n_missing,
                edge_vert_maxabs_px=f"{np.max(np.abs(edge_d)):.2f}" if len(edge_d) else "",
                edge_perp_maxabs_px=f"{np.max(np.abs(edge_p)):.2f}" if len(edge_p) else "",
                edge_perp_p95abs_px=f"{np.percentile(np.abs(edge_p), 95):.2f}" if len(edge_p) else "",
                edge_perp_mean_signed_px=f"{np.mean(edge_p):+.2f}" if len(edge_p) else "",
                edge_perp_maxabs_value=f"{np.max(np.abs(edge_p)) * abs(b):.2e}" if len(edge_p) else "",
                mean_measured=len(mean_d), mean_hidden=n_mean_occl,
                mean_vert_maxabs_px=f"{np.max(np.abs(mean_d)):.2f}" if len(mean_d) else "",
                mean_perp_maxabs_px=f"{np.max(np.abs(mean_p)):.2f}" if len(mean_p) else "",
                mean_perp_mean_signed_px=f"{np.mean(mean_p):+.2f}" if len(mean_p) else "",
                mean_perp_maxabs_value=f"{np.max(np.abs(mean_p)) * abs(b):.2e}" if len(mean_p) else "",
                value_per_px=f"{px_val:.3e}",
                bad_orders=" ".join(bad_orders[:5]),
            ))
        print(f"Figure {f['figure']:2d}: done")
    fn = os.path.join(a.dir, "raster_crosscheck.csv")
    with open(fn, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out_rows[0]))
        w.writeheader()
        w.writerows(out_rows)
    print(json.dumps(tot))
    print("largest perpendicular band-edge differences (|perp| px, figure, panel, series, quarter, vert px, perp px, slope):")
    for w_ in sorted(worst, reverse=True)[:8]:
        print("   ", w_)
    print("edges not found (figure, panel, series, quarter, predicted row, classes in +-12 rows):")
    for m_ in missing:
        print("   ", m_)
    for name, arr in (("band edges, vertical", all_edge_d), ("band edges, perpendicular", all_edge_p),
                      ("mean line, vertical", all_mean_d), ("mean line, perpendicular", all_mean_p)):
        e = np.abs(np.array(arr))
        print(f"{name:27s}: n={len(e)}  |diff| px: median {np.median(e):.2f}  p95 {np.percentile(e, 95):.2f}  "
              f"p99 {np.percentile(e, 99):.2f}  max {e.max():.2f}   signed mean {np.mean(arr):+.2f}")
    ranges = {}
    for c in calib:
        t = [float(v) for v in c["y_tick_labels"].split(";")]
        ranges[(int(c["figure"]), int(c["panel"]))] = max(t) - min(t)
    worst_rel = max(max(float(r["edge_perp_maxabs_value"] or 0), float(r["mean_perp_maxabs_value"] or 0))
                    / ranges[(int(r["figure"]), int(r["panel"]))] for r in out_rows)
    print(f"largest raster-vs-CSV difference relative to the panel's axis range: {worst_rel:.2e}")
    tf = max(float(r["raster_tick_fit_max_resid_px"]) for r in out_rows)
    zd = max(abs(float(r["raster_vs_vector_zero_row_px"])) for r in out_rows)
    sc = max(abs(float(r["raster_vs_vector_scale_rel"])) for r in out_rows)
    lr = max(max(abs(float(r["raster_vs_vector_left_px"])), abs(float(r["raster_vs_vector_right_px"]))) for r in out_rows)
    print(f"raster tick fit max resid {tf:.2f} px; raster-vs-vector calibration: zero row {zd:.2f} px, scale {sc:.1e}, frame x {lr:.2f} px")
    print("(1 px at 1200 dpi = 0.06 pt; the MATLAB coordinate grid is 0.075 pt = 1.25 px at scale 0.9, 0.83 px at 0.6)")
    print("wrote", fn)


if __name__ == "__main__":
    main()
