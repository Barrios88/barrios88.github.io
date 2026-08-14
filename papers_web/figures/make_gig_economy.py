#!/usr/bin/env python3
"""
Regenerate figures/figure1_main_results.svg for
"Launching with a Parachute: The Gig Economy and New Business Formation"
(Barrios, Hochberg, Yi; JFE 144(1), 2022).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Panel A -- main effects of ridehailing entry:
        new business registrations ~5% (4-6% band, abstract + p.text),
        small business lending ~5% ("correspondingly-sized", abstract),
        entrepreneurship-related searches ~7% (abstract).
  * Panel B -- heterogeneity gradient: a 3 percentage-point larger effect
        in cities with a one-standard-deviation-higher wage-growth
        volatility (Section text; "3 percentage point larger effect").

The previous baked-matplotlib version showed four invented per-specification
coefficients (3.9 / 5.3 / 5.9 / 4.2%) that appear nowhere in the paper.
Those have been removed. Text is emitted as real <text> (svg.fonttype='none')
in Inter so it renders in the site typeface on the page.

Run:  python3 make_gig_economy.py
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


fig, axes = plt.subplots(
    1, 2, figsize=(12.4, 4.8), layout="constrained",
    gridspec_kw={"width_ratios": [2.15, 1]},
)
fig.suptitle("Ridehailing Entry and New Business Formation: Main Results",
             fontsize=16, fontweight="bold", color=YALE)

# -- Panel A: main effects of ridehailing entry ---------------------
axA = axes[0]
labelsA = ["New Business\nRegistrations", "Small-Business\nLending",
           "Entrepreneurship\nSearches"]
valsA   = [5, 5, 7]
colsA   = [BLUE, YALE, BLUE_LIGHT]
# 4-6% band reported for registrations only; point estimates elsewhere.
xerrA   = [[1, 0, 0], [1, 0, 0]]
yA = range(len(labelsA))
axA.barh(yA, valsA, color=colsA, edgecolor="white", linewidth=0.8, height=0.62,
         zorder=3, xerr=xerrA,
         error_kw=dict(ecolor="#9aa1ab", elinewidth=1.4, capsize=5, zorder=4))
axA.set_yticks(list(yA), labelsA)
axA.invert_yaxis()
axA.set_xlim(0, 9)
axA.set_xlabel("% increase after ridehailing entry", fontsize=11, color=INK_SOFT, labelpad=8)
axA.set_title("Effect on New Business Formation", **TITLE_KW)
axA.grid(axis="x", color=RULE, linewidth=1, zorder=0)
lblsA = ["~5% (4–6%)", "~5%", "~7%"]
for y, v, t in zip(yA, valsA, lblsA):
    pad = 1.15 if y == 0 else 0.25  # clear the error whisker on the first bar
    axA.text(v + pad, y, t, va="center", ha="left", **VLAB_KW)
style(axA)

# -- Panel B: heterogeneity by local uncertainty --------------------
axB = axes[1]
catsB = ["+1 SD Wage-Growth\nVolatility"]
valsB = [3]
axB.bar(catsB, valsB, color=YALE, edgecolor="white", linewidth=0.8, width=0.5, zorder=3)
axB.set_ylim(0, 5)
axB.set_ylabel("Extra pp on registration effect\nper SD of local uncertainty",
               fontsize=10.5, color=INK_SOFT)
axB.set_title("Larger Where Ex-Ante\nUncertainty Is Higher", **TITLE_KW)
axB.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsB):
    axB.text(x, v + 0.12, f"+{v}pp", ha="center", va="bottom", **VLAB_KW)
style(axB)

out = "figure1_main_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
