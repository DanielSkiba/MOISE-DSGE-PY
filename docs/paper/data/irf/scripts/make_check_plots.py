#!/usr/bin/env python3
"""Re-plot the extracted impulse responses in the paper's own 4x3 panel layout
(data/irf/check_figNN.png) so they can be compared by eye with the PDF pages.

The styling deliberately copies the original (light gray = 90% HPD band, dark gray =
70% HPD band, thick black = mean, thin black zero line, y-limits and y-ticks = the
printed tick labels) because the only job of these images is a like-for-like visual
comparison with the source figure.

Usage: python3 make_check_plots.py [--dir docs/paper/data/irf]
"""
import argparse
import csv
import json
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=os.path.abspath(os.path.join(HERE, "..")))
    a = ap.parse_args()
    figs = json.load(open(os.path.join(a.dir, "figures.json")))
    calib = list(csv.DictReader(open(os.path.join(a.dir, "panel_calibration.csv"))))
    for f in figs:
        data = {}
        for r in csv.DictReader(open(os.path.join(a.dir, f["csv"]))):
            data.setdefault(r["panel_title"], {}).setdefault(r["series"], {})[int(r["quarter"])] = float(r["value"])
        panels = sorted([c for c in calib if int(c["figure"]) == f["figure"]], key=lambda c: int(c["panel"]))
        fig, axes = plt.subplots(4, 3, figsize=(9.0, 10.4))
        for c, ax in zip(panels, axes.ravel()):
            d = data[c["panel_title"]]
            q = np.arange(1, 21)
            s = {k: np.array([d[k][i] for i in q]) for k in d}
            ax.fill_between(q, s["hpd90_lower"], s["hpd90_upper"], color="0.80", lw=0)
            ax.fill_between(q, s["hpd70_lower"], s["hpd70_upper"], color="0.65", lw=0)
            ax.axhline(0, color="k", lw=0.9)
            ax.plot(q, s["mean"], color="k", lw=2.0)
            ticks = [float(t) for t in c["y_tick_labels"].split(";")]
            ax.set_ylim(min(ticks), max(ticks))
            ax.set_yticks(ticks)
            ax.set_yticklabels(c["y_tick_labels"].replace("-", "−").split(";"))
            ax.set_xlim(0, 20)
            ax.set_xticks([0, 10, 20])
            ax.tick_params(labelsize=9, direction="in", top=True, right=True, length=3)
            ax.set_title(c["panel_title"], fontsize=10, family="serif")
        fig.suptitle(f"{f['printed_title']}\nre-plot of extracted data ({f['csv']}; PDF p.{f['page_pdf']})",
                     fontsize=11, family="serif")
        fig.tight_layout(rect=(0, 0, 1, 0.95), h_pad=1.6, w_pad=2.0)
        out = os.path.join(a.dir, f"check_fig{f['figure']:02d}.png")
        fig.savefig(out, dpi=110)
        plt.close(fig)
        print(out)


if __name__ == "__main__":
    main()
