#!/usr/bin/env python3
"""
Regenerate figures/figure_1_key_results.svg for
"Measurement Matters: Financial Reporting and Productivity"
(Barrios, Fujiy, Lisowsky, Minnis; NBER WP 34536, 2025).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Left panel  — reporting quality explains ~10-20% of intra-industry TFP
                  dispersion (P10-P90), abstract & p.185-187. Shown as a
                  10-20% range with a 15% illustrative midpoint.
  * Right panel — Table 5 "horse race" magnitudes: audits raise productivity
                  ~2.5-3% and profitability ~0.7-0.8%; management practices
                  ~2.7-3.4% and ~0.8-0.9%. Bars are illustrative midpoints;
                  labels give the paper's ranges.

Removed from the previous version: the fabricated "IT Investments 17%" and
"Management Practices 14%" dispersion-share bars (no such shares appear in the
paper). Text is emitted as real <text> (svg.fonttype='none') in Inter so it
renders in the site typeface on the page.

Run:  python3 make_measurement_matters.py
"""

import matplotlib
matplotlib.use("svg")
import numpy as np
import matplotlib.pyplot as plt

YALE       = "#00356b"
BLUE       = "#1d63d8"
BLUE_LIGHT = "#6f9bcc"
INK_SOFT   = "#3f4650"
MUTED      = "#6b7280"
RULE       = "#e7e9ec"

plt.rcParams.update({
    "svg.fonttype": "none",
    "font.family": "Inter, Helvetica, Arial, sans-serif",
    "text.color": INK_SOFT,
    "axes.edgecolor": "#c9ced6",
    "axes.linewidth": 1.0,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
})

TITLE_KW = dict(fontsize=12.5, fontweight="bold", color=YALE, pad=12)
VLAB_KW  = dict(fontsize=10.5, fontweight="bold", color=YALE)


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK_SOFT)


fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 5.0), layout="constrained")
fig.suptitle("Measurement Matters: Key Empirical Results",
             fontsize=16, fontweight="bold", color=YALE)

# ── Left: reporting quality's share of TFP dispersion (10-20%) ─────
mid, lo, hi = 15, 10, 20
axL.bar([0], [mid], width=0.46, color=BLUE, edgecolor="white",
        linewidth=0.8, zorder=3)
axL.errorbar([0], [mid], yerr=[[mid - lo], [hi - mid]], fmt="none",
             ecolor=YALE, elinewidth=2.2, capsize=10, capthick=2.2, zorder=4)
axL.text(0, 20.6, "10–20%", ha="center", va="bottom", **VLAB_KW)
axL.text(0, 22.7, "15% midpoint (illustrative)", ha="center", va="bottom",
         fontsize=9, color=MUTED, style="italic")
axL.set_xticks([0], ["Financial\nReporting Quality"])
axL.set_xlim(-0.7, 0.7)
axL.set_ylim(0, 25)
axL.set_ylabel("% of TFP Dispersion (P10–P90)", fontsize=11, color=INK_SOFT)
axL.set_title("Share of Productivity\nDispersion Explained", **TITLE_KW)
axL.grid(axis="y", color=RULE, linewidth=1, zorder=0)
style(axL)

# ── Right: independent effects on productivity & profitability ─────
#            (Table 5 ranges; bars = illustrative midpoints)
groups = ["Productivity", "Profitability"]
audit_mid = [2.75, 0.75]   # 2.5-3% ; 0.7-0.8%
mgmt_mid  = [3.05, 0.85]   # 2.7-3.4% ; 0.8-0.9%
audit_lab = ["2.5–3%", "0.7–0.8%"]
mgmt_lab  = ["2.7–3.4%", "0.8–0.9%"]

x = np.arange(len(groups))
w = 0.36
b1 = axR.bar(x - w / 2, audit_mid, width=w, color=YALE, edgecolor="white",
             linewidth=0.8, label="Audits", zorder=3)
b2 = axR.bar(x + w / 2, mgmt_mid, width=w, color=BLUE, edgecolor="white",
             linewidth=0.8, label="Management Practices", zorder=3)
axR.set_xticks(x, groups)
axR.set_ylim(0, 4.2)
axR.set_ylabel("% Gain vs. Comparable Firms", fontsize=11, color=INK_SOFT)
axR.set_title("Independent Effects\n(Table 5 ranges)", **TITLE_KW)
axR.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for bars, labs in ((b1, audit_lab), (b2, mgmt_lab)):
    for rect, lab in zip(bars, labs):
        axR.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 0.08,
                 lab, ha="center", va="bottom", fontsize=9.5,
                 fontweight="bold", color=YALE)
axR.legend(frameon=False, fontsize=10, loc="upper right",
           labelcolor=INK_SOFT)
style(axR)

fig.text(0.5, -0.01,
         "Bars show illustrative midpoints of the ranges reported in the paper; range labels are the paper's estimates.",
         ha="center", va="top", fontsize=9, color=MUTED, style="italic")

out = "figure_1_key_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
