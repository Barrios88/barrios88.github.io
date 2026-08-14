#!/usr/bin/env python3
"""
Regenerate figures/figure1_behavioral_divergence.svg for
"Risk Perceptions and Politics: Evidence from the COVID-19 Pandemic"
(Barrios & Hochberg; JFE 142(2), 2021).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Panel A — partisan muting of the distancing response. A one-standard-
              deviation increase in Trump vote share (0.12) mutes the
              response by 7.8% (p.863 text); the top quartile of Trump
              counties shows ~40% muting (p.863 / Table 2 col 6).
  * Panel B — response to state stay-at-home closures (Fig. 6, p.873):
              low-Trump counties cut average daily distance traveled 9.3%
              vs. 6.7% in high-Trump counties.
The previous version's fabricated bars (-6.5% low-Trump / -3.5% high-Trump
"per log case" effects, in two identical panels) have been removed. Text is
emitted as real <text> (svg.fonttype='none') in Inter so it renders in the
site typeface on the page.

Run:  python3 make_risk_politics.py
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
VLAB_KW  = dict(fontsize=11, fontweight="bold", color=YALE)


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK_SOFT)


fig, axes = plt.subplots(1, 2, figsize=(11.4, 5.0), layout="constrained")
fig.suptitle("Partisan Differences in the COVID-19 Distancing Response",
             fontsize=16, fontweight="bold", color=YALE)

# ── Panel A: how much the distancing response is muted ─────────────
axA = axes[0]
catsA = ["+1 SD in Trump\nVote Share", "Top Quartile\nTrump Counties"]
valsA = [7.8, 40]
colsA = [BLUE_LIGHT, YALE]
axA.bar(catsA, valsA, color=colsA, edgecolor="white", linewidth=0.8, width=0.6, zorder=3)
axA.set_ylim(0, 46)
axA.set_ylabel("Muting of the Distancing Response (%)", fontsize=11, color=INK_SOFT)
axA.set_title("How Much the Response Is Muted\nin Higher Trump-Share Counties", **TITLE_KW)
axA.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsA):
    axA.text(x, v + 0.8, f"{v:g}%", ha="center", va="bottom", **VLAB_KW)
style(axA)

# ── Panel B: reduction in daily distance under state closures ──────
axB = axes[1]
catsB = ["Low Trump\nCounties", "High Trump\nCounties"]
valsB = [9.3, 6.7]
colsB = [YALE, BLUE_LIGHT]
axB.bar(catsB, valsB, color=colsB, edgecolor="white", linewidth=0.8, width=0.6, zorder=3)
axB.set_ylim(0, 11)
axB.set_ylabel("Reduction in Daily Distance Traveled (%)", fontsize=11, color=INK_SOFT)
axB.set_title("Response to State Stay-at-Home Closures\n(Figure 6)", **TITLE_KW)
axB.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsB):
    axB.text(x, v + 0.2, f"{v:g}%", ha="center", va="bottom", **VLAB_KW)
style(axB)

out = "figure1_behavioral_divergence.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
