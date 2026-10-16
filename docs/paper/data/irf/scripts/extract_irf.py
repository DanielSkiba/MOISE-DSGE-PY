#!/usr/bin/env python3
"""Extract the impulse responses plotted in Figures 6-18 of Argov et al. (2012),
"MOISE: A DSGE Model for the Israeli Economy", Bank of Israel DP 2012.06,
directly from the vector graphics of the PDF (no pixel digitising).

Usage:
    python3 extract_irf.py [--pdf PATH] [--out DIR]
Defaults (relative to this file): PDF = ../../../moise.pdf (pass --pdf with your own copy of the paper), OUT = ../ (= this data/irf folder)

What is in the PDF (verified by the checks below)
-------------------------------------------------
Every figure is a MATLAB-exported PDF page embedded as a form XObject (scaled
0.9, or 0.6 for Figure 11).  The 12 panels (4 rows x 3 columns) each contain, in
drawing order:
  1. filled polygon, gray 1.0 (white)    baseline 0 -> B0   (invisible base of a stacked area plot)
  2. filled polygon, gray 0.80 (light)   B0 -> B1
  3. filled polygon, gray 0.65 (dark)    B1 -> B2
  4. filled polygon, gray 0.80 (light)   B2 -> B3
  5. stroked polyline, black, 3x the axes line width   = mean impulse response
  6. black horizontal line at y = 0 (2x axes line width)
Each polygon k is traversed (q1,B[k-1]) -> (q1,B[k]) -> ... B[k] ... -> (q20,B[k]) ->
(q20,B[k-1]) -> ... B[k-1] ... -> (q1,B[k-1]): the forward chain is the new boundary,
the backward chain repeats the previous one (checked: identical, and the white
polygon's backward chain is exactly the y=0 line).  Hence B0 = lower bound of the
90% interval, B1 = lower 70%, B2 = upper 70%, B3 = upper 90% (dark = inner = 70%,
light = outer = 90%; caption: "Gray area - 70 and 90 percent highest interval").

All coordinates of the MATLAB file lie on a 1/12-pt grid (in the figure's own
points), i.e. 0.075 pt on the page at scale 0.9 (0.05 pt at 0.6).  Collinear
vertices on horizontal runs were dropped by the PDF writer; every dropped vertex
is on a flat run, so re-inserting it by interpolation is exact (checked).
"""
import argparse
import csv
import json
import os
import sys
import unicodedata

import numpy as np
import pdfplumber
from pdfminer.pdftypes import resolve1

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_PDF = os.path.abspath(os.path.join(HERE, "..", "..", "..", "moise.pdf"))
DEFAULT_OUT = os.path.abspath(os.path.join(HERE, ".."))

FIGURES = [
    dict(figure=6, page=80, shock="interest_rate", title="Impulse Response to an Interest Rate Shock"),
    dict(figure=7, page=82, shock="external_risk_premium", title="Impulse Response to an External Risk Premium Shock"),
    dict(figure=8, page=84, shock="symmetric_premium", title="Impulse Response to a Symmetric Premium Shock"),
    dict(figure=9, page=86, shock="foreign_demand", title="Impulse Response to a Foreign Demand Shock"),
    dict(figure=10, page=88, shock="transitory_technology", title="Impulse Response to a Transitory Technology Shock"),
    dict(figure=11, page=133, shock="domestic_price_markup", title="Impulse Response to a Domestic Price Markup Shock"),
    dict(figure=12, page=134, shock="import_price_markup", title="Impulse Response to an Import Price Markup Shock"),
    dict(figure=13, page=135, shock="oil_price", title="Impulse Response to an Oil Price Shock"),
    dict(figure=14, page=136, shock="investment_specific_technology",
         title="Impulse Response to an Investment Specific Technology Shock"),
    dict(figure=15, page=137, shock="export_share", title="Impulse Response to an Export Share Shock"),
    dict(figure=16, page=138, shock="home_bias", title="Impulse Response to a Home Bias Shock"),
    dict(figure=17, page=139, shock="wage_markup", title="Impulse Response to a Wage Markup Shock"),
    dict(figure=18, page=140, shock="inventories_investment_demand",
         title="Impulse Response to an Inventories Investment Demand Shock"),
]
PAGE_OFFSET = 6  # printed page = PDF page - 6

PANEL_TITLES = ["Output", "Consumption", "Fixed investment",
                "Exports", "Imports", "Hours worked",
                "Interest rate", "Real wage", "Real exchange rate",
                "CPI inflation", "Domestic inflation", "Imported inflation"]
U_REAL = "percentage deviation from steady state"
U_INFL = "percentage-point deviation from steady state"
U_RATE = "annualized percentage-point deviation from steady state"
UNITS = {t: U_REAL for t in PANEL_TITLES}
UNITS.update({"Interest rate": U_RATE, "CPI inflation": U_INFL,
              "Domestic inflation": U_INFL, "Imported inflation": U_INFL})

SERIES = ["mean", "hpd70_lower", "hpd70_upper", "hpd90_lower", "hpd90_upper"]
FILL_GRAYS = [1.0, 0.800781, 0.650391, 0.800781]  # white, light, dark, light
NQ = 20  # quarters plotted: 1..20

# broken ToUnicode of the TeX "Dc" text fonts (ligatures): seen as e.g. "Speci…c", "In‡ation"
DC_LIGATURES = {"…": "fi", "‡": "fl", "¤": "ff"}


class CheckError(RuntimeError):
    pass


def check(cond, msg):
    if not cond:
        raise CheckError(msg)


def gray(c):
    if isinstance(c, (tuple, list)):
        check(len(c) == 1, f"unexpected colour {c}")
        c = c[0]
    return float(c)


def group_strings(chars):
    """Join chars that sit on one baseline and touch each other into strings."""
    chars = sorted(chars, key=lambda c: (round(c["top"], 2), c["x0"]))
    out = []
    for c in chars:
        if (out and abs(c["top"] - out[-1]["top"]) < 0.05
                and -0.5 < c["x0"] - out[-1]["x1"] < 0.3 * c["size"]):
            s = out[-1]
            s["text"] += c["text"]
            s["x1"] = c["x1"]
            s["bottom"] = max(s["bottom"], c["bottom"])
        else:
            out.append(dict(text=c["text"], x0=c["x0"], x1=c["x1"], top=c["top"],
                            bottom=c["bottom"], size=c["size"]))
    return out


def assemble(chars, ligmap=None):
    """Chars of one line -> text, with spaces inferred from horizontal gaps."""
    chars = sorted(chars, key=lambda c: c["x0"])
    s, prev = "", None
    for c in chars:
        if prev is not None and c["x0"] - prev["x1"] > 0.15 * c["size"]:
            s += " "
        t = c["text"]
        if ligmap:
            t = "".join(ligmap.get(ch, ch) for ch in t)
        s += unicodedata.normalize("NFKC", t)
        prev = c
    return s


def text_lines(chars, ligmap=None):
    rows = {}
    for c in chars:
        rows.setdefault(round(c["top"], 1), []).append(c)
    return [assemble(rows[k], ligmap) for k in sorted(rows)]


def embedded_sources(page):
    """PTEX.FileName of the embedded figure file(s) (names the MATLAB source file)."""
    out = []

    def walk(xobjs):
        for _, ref in xobjs.items():
            o = resolve1(ref)
            a = getattr(o, "attrs", {})
            fn = a.get("PTEX.FileName")
            if fn is not None:
                out.append(fn.decode("latin-1") if isinstance(fn, bytes) else str(fn))
            r = a.get("Resources")
            r = resolve1(r) if r is not None else None
            if r and "XObject" in r:
                walk(resolve1(r["XObject"]))

    res = resolve1(page.page_obj.resources)
    if res and "XObject" in res:
        walk(resolve1(res["XObject"]))
    return out


def fill_gaps(d, what):
    """d: {quarter: top}.  Re-insert vertices dropped by the PDF writer.
    Returns array of NQ tops, number filled, number of filled gaps that were NOT flat."""
    check(1 in d and NQ in d, f"{what}: chain does not span q1..q{NQ}: {sorted(d)}")
    qs = sorted(d)
    out = np.empty(NQ)
    filled = sloped = 0
    for a, b in zip(qs[:-1], qs[1:]):
        out[a - 1] = d[a]
        if b - a > 1:
            if abs(d[b] - d[a]) > 1e-6:
                sloped += 1
            for q in range(a + 1, b):
                out[q - 1] = d[a] + (d[b] - d[a]) * (q - a) / (b - a)
                filled += 1
    out[qs[-1] - 1] = d[qs[-1]]
    return out, filled, sloped


def quarters_of(pts, qmap, what):
    q = np.array([qmap(x) for x, _ in pts])
    qi = np.rint(q).astype(int)
    dev = float(np.max(np.abs(q - qi)))
    check(dev < 0.05, f"{what}: vertex x not on integer quarters (max dev {dev:.3f})")
    check(qi.min() >= 1 and qi.max() <= NQ, f"{what}: quarters outside 1..{NQ}: {qi.min()}..{qi.max()}")
    verts = []
    for k, (_, t) in zip(qi, pts):
        if verts and verts[-1][0] == k and abs(verts[-1][1] - t) < 1e-6:
            continue  # exact duplicate vertex
        verts.append((int(k), float(t)))
    return verts, dev


def decode_polygon(pts, qmap, what):
    """Closed stacked-area polygon -> (forward chain tops, backward chain tops, stats)."""
    V, dev = quarters_of(pts, qmap, what)
    if V[0] != V[-1]:
        V.append(V[0])  # implicit close
    idx = [i for i, (k, _) in enumerate(V) if k == NQ]
    check(idx and idx == list(range(idx[0], idx[-1] + 1)), f"{what}: q{NQ} vertices not contiguous")
    fwd, bwd = V[:idx[0] + 1], V[idx[-1]:]
    fq, bq = [k for k, _ in fwd], [k for k, _ in bwd]
    # forward: q1 may appear twice (vertical move from previous boundary), then strictly increasing
    f_inc = fq[1:] if (len(fq) > 1 and fq[0] == fq[1] == 1) else fq
    check(fq[0] == 1 and all(b > a for a, b in zip(f_inc[:-1], f_inc[1:])), f"{what}: bad forward chain {fq}")
    check(bq[-1] == 1 and all(b < a for a, b in zip(bq[:-1], bq[1:])), f"{what}: bad backward chain {bq}")
    fd, bd = {}, {}
    for k, t in fwd:
        fd[k] = t  # last occurrence at q1 = the new boundary
    for k, t in bwd:
        bd.setdefault(k, t)
    f, nf1, s1 = fill_gaps(fd, what + " fwd")
    b, nf2, s2 = fill_gaps(bd, what + " bwd")
    return f, b, dict(nvert=len(pts), filled=nf1 + nf2, sloped=s1 + s2, qdev=dev)


def decode_polyline(pts, qmap, what):
    V, dev = quarters_of(pts, qmap, what)
    q = [k for k, _ in V]
    check(q[0] == 1 and q[-1] == NQ and all(b > a for a, b in zip(q[:-1], q[1:])), f"{what}: bad polyline {q}")
    arr, nf, s = fill_gaps(dict(V), what)
    return arr, dict(nvert=len(pts), filled=nf, sloped=s, qdev=dev)


def grid_dev(objs, X0, T0, g):
    """Max distance (in grid units) of all vertices from the 1/12-pt grid anchored at the frame corner."""
    m = 0.0
    for o in objs:
        for x, t in o["pts"]:
            for v in ((x - X0) / g, (t - T0) / g):
                m = max(m, abs(v - round(v)))
    return m


def fmt(v):
    s = f"{v:.6f}"
    return "0.000000" if s == "-0.000000" else s


def process_figure(pdf, spec):
    pn = spec["page"]
    p = pdf.pages[pn - 1]
    log = dict(figure=spec["figure"], page_pdf=pn, page_printed=pn - PAGE_OFFSET, shock=spec["shock"])

    # ---- figure title, caption, embedded file -------------------------------------------
    frames = [r for r in p.rects if r["stroke"]]
    check(len(frames) == 12, f"p{pn}: expected 12 panel frames, found {len(frames)}")
    first_top = min(r["top"] for r in frames)
    last_bottom = max(r["bottom"] for r in frames)
    title_chars = [c for c in p.chars if "Dcr10" in c["fontname"] and c["size"] > 11 and c["top"] < first_top]
    lines = [l for l in text_lines(title_chars, DC_LIGATURES) if l.startswith("Figure")]
    want = f"Figure {spec['figure']}: {spec['title']}"
    check(lines and lines[0] == want, f"p{pn}: title {lines!r} != {want!r}")
    log["printed_title"] = lines[0]
    cap_chars = [c for c in p.chars if "Dcr10" in c["fontname"] and abs(c["size"] - 9.9626) < 0.05
                 and c["top"] > last_bottom]
    log["caption"] = " ".join(text_lines(cap_chars, DC_LIGATURES))
    lw = frames[0]["linewidth"]
    scale = lw / 0.5          # MATLAB axes lines are 0.5 pt wide in the figure file
    g = scale / 12.0          # 1/12 pt grid of the MATLAB file, in page points
    log["scale"] = round(scale, 4)
    log["grid_pt"] = g
    log["embedded_files"] = embedded_sources(p)
    hidden = [c for c in p.chars if "CMR10" in c["fontname"] and abs(c["size"] - 9.0 * scale) < 0.05]
    log["clipped_matlab_note"] = " ".join(text_lines(hidden))

    tops = sorted({round(r["top"], 1) for r in frames})
    lefts = sorted({round(r["x0"], 1) for r in frames})
    check(len(tops) == 4 and len(lefts) == 3, f"p{pn}: panels are not a 4x3 grid")
    frames.sort(key=lambda r: (tops.index(round(r["top"], 1)), lefts.index(round(r["x0"], 1))))

    helv = group_strings([c for c in p.chars if c["fontname"] == "Helvetica"])
    cmr_title = [c for c in p.chars if "CMR10" in c["fontname"] and abs(c["size"] - 10.0 * scale) < 0.05]

    rows, calib = [], []
    assigned_curves = 0
    for k, r in enumerate(frames):
        X0, T0, X1, T1 = r["x0"], r["top"], r["x1"], r["bottom"]
        where = f"fig{spec['figure']} p{pn} panel{k + 1}"

        def inside(o, tol):
            return (o["x0"] >= X0 - tol and o["x1"] <= X1 + tol and
                    o["top"] >= T0 - tol and o["bottom"] <= T1 + tol)

        # ---- panel title ----
        tch = [c for c in cmr_title if T0 - 16 * scale < c["top"] < T0 and X0 - 10 < c["x0"] < X1 + 10]
        title = assemble(tch)
        check(title == PANEL_TITLES[k], f"{where}: title {title!r} != {PANEL_TITLES[k]!r}")

        # ---- tick marks (short lines on the frame edges) ----
        plines = [l for l in p.lines if inside(l, 0.05)]
        short = [l for l in plines if max(l["x1"] - l["x0"], l["bottom"] - l["top"]) < 3 * scale]
        eps = 0.02
        uniq = lambda v: sorted({round(t, 4) for t in v})
        yt_l = uniq(l["top"] for l in short if abs(l["top"] - l["bottom"]) < 1e-6 and abs(l["x0"] - X0) < eps)
        yt_r = uniq(l["top"] for l in short if abs(l["top"] - l["bottom"]) < 1e-6 and abs(l["x1"] - X1) < eps)
        xt_b = uniq(l["x0"] for l in short if abs(l["x0"] - l["x1"]) < 1e-6 and abs(l["bottom"] - T1) < eps)
        xt_t = uniq(l["x0"] for l in short if abs(l["x0"] - l["x1"]) < 1e-6 and abs(l["top"] - T0) < eps)
        check(yt_l == yt_r and len(yt_l) >= 3, f"{where}: left/right y ticks differ {yt_l} {yt_r}")
        check(xt_b == xt_t and len(xt_b) == 3, f"{where}: bottom/top x ticks differ {xt_b} {xt_t}")

        # ---- tick labels ----
        ylab = [s for s in helv if X0 - 8 * scale < s["x1"] < X0 and T0 - 6 < (s["top"] + s["bottom"]) / 2 < T1 + 6]
        xlab = [s for s in helv if T1 < s["top"] < T1 + 8 * scale and X0 - 8 < (s["x0"] + s["x1"]) / 2 < X1 + 8]
        check(len(ylab) == len(yt_l), f"{where}: {len(ylab)} y labels vs {len(yt_l)} y ticks")
        check(len(xlab) == 3, f"{where}: {len(xlab)} x labels")

        def match(labels, ticks, centre):
            pairs, used = [], set()
            for s in labels:
                c = centre(s)
                j = int(np.argmin([abs(c - t) for t in ticks]))
                check(j not in used, f"{where}: two labels on one tick")
                used.add(j)
                pairs.append((float(s["text"].replace("−", "-")), ticks[j], c - ticks[j], s["text"]))
            return sorted(pairs)

        yp = match(ylab, yt_l, lambda s: (s["top"] + s["bottom"]) / 2)
        xp = match(xlab, xt_b, lambda s: (s["x0"] + s["x1"]) / 2)
        offs = [o for _, _, o, _ in yp]
        check(max(offs) - min(offs) < 0.05, f"{where}: inconsistent label/tick offsets {offs}")
        yv = np.array([v for v, _, _, _ in yp])
        ytop = np.array([t for _, t, _, _ in yp])
        steps = np.diff(yv)
        check(np.allclose(steps, steps[0], rtol=1e-9, atol=1e-12), f"{where}: y labels not evenly spaced {yv}")
        check(np.all(np.diff(ytop) < 0), f"{where}: y ticks not monotone")
        beta, alpha = np.polyfit(yv, ytop, 1)          # top = alpha + beta * value
        yres = (ytop - (alpha + beta * yv)) / g
        xv = np.array([v for v, _, _, _ in xp])
        check(list(xv) == [0.0, 10.0, 20.0], f"{where}: x labels {xv}")
        xpos = np.array([t for _, t, _, _ in xp])
        bx, ax = np.polyfit(xv, xpos, 1)               # x = ax + bx * quarter
        xres = (xpos - (ax + bx * xv)) / g
        check(np.max(np.abs(yres)) <= 0.75 and np.max(np.abs(xres)) <= 0.75,
              f"{where}: tick fit not linear within grid rounding (y {yres}, x {xres})")
        vmap = lambda t: (t - alpha) / beta
        qmap = lambda x: (x - ax) / bx

        # ---- graphics in the panel ----
        cv = [c for c in p.curves if inside(c, 0.05)]
        assigned_curves += len(cv)
        check(len(cv) == 5, f"{where}: {len(cv)} curves (expected 5)")
        fills, stroke = cv[:4], cv[4]
        check(all(c["fill"] and not c["stroke"] for c in fills), f"{where}: first four paths are not fills")
        greys = [gray(c["non_stroking_color"]) for c in fills]
        check(np.allclose(greys, FILL_GRAYS, atol=1e-4), f"{where}: fill greys {greys}")
        check(stroke["stroke"] and not stroke["fill"] and gray(stroke["stroking_color"]) == 0.0
              and abs(stroke["linewidth"] - 3 * lw) < 1e-6, f"{where}: last path is not the thick black line")
        zl = [l for l in plines if abs(l["top"] - l["bottom"]) < 1e-6 and abs(l["x0"] - X0) < eps
              and abs(l["x1"] - X1) < eps and l["linewidth"] > 1.5 * lw]
        check(len(zl) == 1 and gray(zl[0]["stroking_color"]) == 0.0, f"{where}: zero line not found")
        gdev = grid_dev(cv + zl, X0, T0, g)
        check(gdev < 0.02, f"{where}: vertices off the 1/12-pt grid ({gdev:.3f} grid units)")

        bounds, st = [], dict(nvert=0, filled=0, sloped=0, qdev=0.0)
        prev_upper = None
        shared = 0.0
        for j, poly in enumerate(fills):
            f, b, s = decode_polygon(poly["pts"], qmap, f"{where} fill{j}")
            if j == 0:
                base_dev = float(np.max(np.abs(vmap(b)))) / abs(1 / beta * g)  # baseline vs value 0, grid units
                baseline_value = float(np.max(np.abs(vmap(b))))
            else:
                shared = max(shared, float(np.max(np.abs(b - prev_upper))) / g)
            prev_upper = f
            bounds.append(f)
            for kk in ("nvert", "filled", "sloped"):
                st[kk] += s[kk]
            st["qdev"] = max(st["qdev"], s["qdev"])
        check(shared < 1e-3, f"{where}: polygon chains disagree on shared boundaries ({shared} grid units)")
        check(base_dev <= 0.75, f"{where}: white polygon baseline is not y=0 ({baseline_value})")
        mean_top, sm = decode_polyline(stroke["pts"], qmap, f"{where} mean")
        for kk in ("nvert", "filled", "sloped"):
            st[kk] += sm[kk]
        st["qdev"] = max(st["qdev"], sm["qdev"])
        check(st["sloped"] == 0, f"{where}: a dropped vertex was not on a flat run")

        B = [vmap(t) for t in bounds]
        mean = vmap(mean_top)
        data = dict(mean=mean, hpd90_lower=B[0], hpd70_lower=B[1], hpd70_upper=B[2], hpd90_upper=B[3])
        tol = 1e-9
        order_viol = int(np.sum(B[0] > B[1] + tol) + np.sum(B[1] > B[2] + tol) + np.sum(B[2] > B[3] + tol))
        out90 = int(np.sum((mean < B[0] - tol) | (mean > B[3] + tol)))
        out70 = int(np.sum((mean < B[1] - tol) | (mean > B[2] + tol)))
        for sname in SERIES:
            for q in range(1, NQ + 1):
                rows.append([spec["figure"], pn, spec["shock"], title, sname, q, fmt(data[sname][q - 1])])

        vpg = abs(g / beta)  # value units per grid unit (= max rounding error x 2)
        # data drawn exactly on the frame edge could have been clipped by the plotting program
        # (out-of-range data would otherwise lie outside the frame, which the 5-curves-inside
        # check above already excludes)
        lim_lo, lim_hi = vmap(T1), vmap(T0)
        on_edge = int(sum(np.sum((np.abs(arr - lim_lo) < 0.5 * vpg) | (np.abs(arr - lim_hi) < 0.5 * vpg))
                          for arr in data.values()))
        if on_edge:
            print(f"WARNING {where}: {on_edge} data values lie on the frame edge (possible clipping)")
        calib.append(dict(
            figure=spec["figure"], page_pdf=pn, panel=k + 1, row=k // 3 + 1, col=k % 3 + 1,
            panel_title=title, units=UNITS[title],
            y_tick_labels=";".join(t for _, _, _, t in yp).replace("−", "-"),
            y_tick_top_pt=";".join(f"{t:.4f}" for t in ytop),
            pt_per_unit=f"{-beta:.6f}", top_of_zero_pt=f"{alpha:.4f}",
            y_fit_max_resid_grid=f"{np.max(np.abs(yres)):.3f}",
            ylim_low=f"{vmap(T1):.6g}", ylim_high=f"{vmap(T0):.6g}",
            x_tick_x_pt=";".join(f"{t:.4f}" for t in xpos), pt_per_quarter=f"{bx:.6f}",
            x_fit_max_resid_grid=f"{np.max(np.abs(xres)):.3f}", quarter_max_dev=f"{st['qdev']:.4f}",
            grid_pt=f"{g:.4f}", value_per_grid_unit=f"{vpg:.3g}",
            zero_line_value=f"{vmap(zl[0]['top']):.2e}", white_baseline_max_abs=f"{baseline_value:.2e}",
            shared_edge_max_diff_grid=f"{shared:.1e}", vertices=st["nvert"], vertices_reinserted=st["filled"],
            band_order_violations=order_viol, mean_outside_hpd90=out90, mean_outside_hpd70=out70,
            data_values_on_frame_edge=on_edge,
        ))
        check(abs(vmap(zl[0]["top"])) <= 0.75 * vpg, f"{where}: zero line maps to {vmap(zl[0]['top'])}")
        check(abs(vmap(T1) - yv[0]) <= 0.75 * vpg and abs(vmap(T0) - yv[-1]) <= 0.75 * vpg,
              f"{where}: frame edges are not the extreme ticks")
    check(assigned_curves == len(p.curves), f"p{pn}: {len(p.curves) - assigned_curves} curves outside panels")
    return rows, calib, log


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pdf", default=DEFAULT_PDF)
    ap.add_argument("--out", default=DEFAULT_OUT)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    pdf = pdfplumber.open(a.pdf)
    all_calib, logs = [], []
    for spec in FIGURES:
        rows, calib, log = process_figure(pdf, spec)
        fn = os.path.join(a.out, f"fig{spec['figure']:02d}_{spec['shock']}.csv")
        with open(fn, "w", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["figure", "page_pdf", "shock", "panel_title", "series", "quarter", "value"])
            w.writerows(rows)
        all_calib += calib
        log["csv"] = os.path.basename(fn)
        log["rows"] = len(rows)
        logs.append(log)
        yr = max(float(c["y_fit_max_resid_grid"]) for c in calib)
        xr = max(float(c["x_fit_max_resid_grid"]) for c in calib)
        print(f"Figure {spec['figure']:2d} p{spec['page']}: {len(calib)} panels, {len(rows)} rows, "
              f"max tick residual y {yr:.2f} / x {xr:.2f} grid units, "
              f"re-inserted vertices {sum(c['vertices_reinserted'] for c in calib)}, "
              f"band-order violations {sum(c['band_order_violations'] for c in calib)}, "
              f"mean outside 90%/70% {sum(c['mean_outside_hpd90'] for c in calib)}/"
              f"{sum(c['mean_outside_hpd70'] for c in calib)}  -> {log['csv']}")
    with open(os.path.join(a.out, "panel_calibration.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_calib[0]))
        w.writeheader()
        w.writerows(all_calib)
    with open(os.path.join(a.out, "figures.json"), "w") as fh:
        json.dump(logs, fh, indent=1, ensure_ascii=False)
    caps = {l["caption"] for l in logs}
    print(f"{len(caps)} distinct caption text(s); all checks passed.")


if __name__ == "__main__":
    try:
        main()
    except CheckError as e:
        sys.exit(f"CHECK FAILED: {e}")
