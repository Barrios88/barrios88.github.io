#!/usr/bin/env python3
"""
Regenerate figures/civic_capital_results.svg for
"Civic Capital and Social Distancing during the COVID-19 Pandemic"
(Barrios, Benmelech, Hochberg, Sapienza, Zingales; JPubE 193, 2021).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Panel A — Exhibit 2 Panel B (col 1) regression coefficients.
  * Panel B — incremental mobility reduction under stay-home mandates
              (bottom-3-quartiles 2% vs top-quartile 7%), paper text pp.6-7.
  * Panel C — Exhibit 3 coefficients of civic capital on mask usage.
The previous version's fabricated bars (mask shares 25/45/30/12%, a
low/medium/high "trust" panel, and coefficients -0.040/-0.015) have been
removed. Text is emitted as real <text> (svg.fonttype='none') in Inter so
it renders in the site typeface on the page.

Run:  python3 make_civic_capital_results.py
"""

import matplotlib
matplotlib.use("svg")
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


fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.9), layout="constrained")
fig.suptitle("Civic Capital and Social Distancing: Key Empirical Results",
             fontsize=16, fontweight="bold", color=YALE)

# ── Panel A: regression coefficients (Exhibit 2 Panel B, col 1) ────
axA = axes[0]
labelsA = ["National Guidelines\n+ High CC Effect",
           "High Civic Capital\nAdditional Effect",
           "State Mandate\nEffect"]
valsA   = [-0.039, -0.014, -0.018]
colsA   = [BLUE, YALE, YALE]
yA = range(len(labelsA))
axA.barh(yA, valsA, color=colsA, edgecolor="white", linewidth=0.8, height=0.6, zorder=3)
axA.set_yticks(list(yA), labelsA)
axA.invert_yaxis()
axA.set_xlim(-0.05, 0.006)
axA.axvline(0, color="#9aa1ab", linewidth=1.0, zorder=2)
axA.set_xlabel("Regression Coefficient", fontsize=11, color=INK_SOFT, labelpad=8)
axA.set_title("Change in Distance Traveled\n(Exhibit 2)", **TITLE_KW)
axA.grid(axis="x", color=RULE, linewidth=1, zorder=0)
for y, v in zip(yA, valsA):
    axA.text(v - 0.0015, y, f"−{abs(v):.3f}", va="center", ha="right", **VLAB_KW)
style(axA)

# ── Panel B: stay-at-home effect by civic capital (text pp.6-7) ────
axB = axes[1]
catsB = ["Bottom 3 Quartiles\nCivic Capital", "Top Quartile\nCivic Capital"]
valsB = [2, 7]
axB.bar(catsB, valsB, color=[BLUE_LIGHT, YALE], edgecolor="white", linewidth=0.8, width=0.6, zorder=3)
axB.set_ylim(0, 10)
axB.set_ylabel("Incremental % Reduction\nin Distance Traveled", fontsize=11, color=INK_SOFT)
axB.set_title("Effect of Stay-at-Home Mandates\nby Civic Capital Level", **TITLE_KW)
axB.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsB):
    axB.text(x, v + 0.25, f"{v}%", ha="center", va="bottom", **VLAB_KW)
style(axB)

# ── Panel C: civic capital and mask usage (Exhibit 3 coefficients) ─
axC = axes[2]
catsC = ["Frequently /\nAlways", "Always", "Never"]
valsC = [0.145, 0.114, -0.058]
colsC = [YALE, YALE, BLUE_LIGHT]
axC.bar(catsC, valsC, color=colsC, edgecolor="white", linewidth=0.8, width=0.6, zorder=3)
axC.set_ylim(-0.1, 0.2)
axC.axhline(0, color="#9aa1ab", linewidth=1.0, zorder=2)
axC.set_ylabel("Coefficient on Civic Capital", fontsize=11, color=INK_SOFT)
axC.set_title("Civic Capital and Mask Usage\n(Exhibit 3)", **TITLE_KW)
axC.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsC):
    off = 0.006 if v >= 0 else -0.006
    va = "bottom" if v >= 0 else "top"
    axC.text(x, v + off, f"{'+' if v >= 0 else '−'}{abs(v):.3f}", ha="center", va=va, **VLAB_KW)
style(axC)

out = "civic_capital_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
