#!/usr/bin/env python3
"""Plot the model's impulse responses against the paper's Figures 6-18.

Usage (from the repo root; needs matplotlib):
    python tools/replication/plot_irfs.py                      # posterior-mean parameters
    python tools/replication/plot_irfs.py --param-set value    # posterior mode
    python tools/replication/plot_irfs.py --decision D13=printed --out /tmp/irfs

Writes one PNG per figure (12 panels each): the paper's posterior-mean response (black), its 70% and
90% bands (gray), and this model (red). Panel units and variables come from the `reporting` section
of model/moise.yaml.
"""
import argparse
import csv
import os
import sys

import numpy as np
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "src"))
import moise  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--param-set", default="posterior_mean")
    ap.add_argument("--decision", action="append", default=[], help="ID=choice, e.g. D13=printed")
    ap.add_argument("--out", default=os.path.join(ROOT, "docs", "phase1", "figures"))
    args = ap.parse_args()

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    spec = yaml.safe_load(open(os.path.join(ROOT, "model", "moise.yaml"), encoding="utf-8"))
    irf_spec = spec["reporting"]["irf"]
    decisions = dict(d.split("=", 1) for d in args.decision)
    sol = moise.solve(moise.load(param_set=args.param_set, decisions=decisions,
                                 blocks_excluded=("measurement",)).linear_system())
    os.makedirs(args.out, exist_ok=True)
    T = irf_spec["horizon"]
    q = np.arange(1, T + 1)
    for fig in irf_spec["figures"]:
        data = {}
        with open(os.path.join(ROOT, "docs", "paper", "data", "irf", fig["file"]), encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                data.setdefault((r["panel_title"], r["series"]), {})[int(r["quarter"])] = float(r["value"])
        irf = moise.impulse_response(sol, fig["shock"], periods=T,
                                     variables=[p["variable"] for p in irf_spec["panels"]])
        f, axes = plt.subplots(3, 4, figsize=(13, 8.2))
        for ax, p in zip(axes.flat, irf_spec["panels"]):
            def s(name):
                d = data[(p["panel"], name)]
                return np.array([d[k] for k in q])
            ax.fill_between(q, s("hpd90_lower"), s("hpd90_upper"), color="0.88", lw=0)
            ax.fill_between(q, s("hpd70_lower"), s("hpd70_upper"), color="0.75", lw=0)
            ax.plot(q, s("mean"), color="black", lw=1.6, label="paper (posterior mean)")
            ax.plot(q, irf[p["variable"]] * p["scale"], color="#c0392b", lw=1.6, ls="--", label="this model")
            ax.axhline(0, color="0.5", lw=0.6)
            ax.set_title(f"{p['panel']}  ({p['variable']})", fontsize=9)
            ax.tick_params(labelsize=7)
            ax.set_xlim(1, T)
        axes.flat[0].legend(fontsize=7, loc="best", frameon=False)
        label = args.param_set + "".join(f", {k}={v}" for k, v in decisions.items())
        f.suptitle(f"Figure {fig['figure']}: {fig['title']} - one S.D.; model at {label}", fontsize=11)
        f.tight_layout(rect=(0, 0, 1, 0.96))
        path = os.path.join(args.out, f"irf_fig{fig['figure']:02d}.png")
        f.savefig(path, dpi=80)
        plt.close(f)
        print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
