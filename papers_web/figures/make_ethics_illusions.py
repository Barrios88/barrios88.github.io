#!/usr/bin/env python3
"""
Regenerate figures/ethics_illusions_results.svg for
"Ethics and Illusions: How Ethical Declarations Shape Market Behavior"
(Barrios, Bertomeu, Lunawat, Sall; working paper, 2024).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Panel A (dollar levels) — average seller report bias $4.11 with no ethical
      statement and $5.65 under mandatory signing (Section 3.2, Figure 3;
      difference +$1.85, Table 4 col. 3, NOT statistically significant); and
      winning-bidder overbidding of $11.87 in the baseline (Section 1 / results).
  * Panel B (dollars per round) — the round coefficient on bidders' prediction
      error: -$0.23 with no ethical statement (Table 6 col. 1, sig. at 1%) and
      statistically insignificant (~0) under mandatory ethics (Table 6 col. 2);
      the between-regime learning differential is $0.17/round (Table 6 col. 3,
      sig. at 5%).

The previous SVG's fabricated bars have been removed:
  overbidding-under-ethics $14.50, learning-under-ethics -$2.50, and the two
  zero-valued seller-misreporting bars. Text is emitted as real <text>
  (svg.fonttype='none') in Inter so it matches the site typeface.

Run:  python3 make_ethics_illusions.py
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


fig, axes = plt.subplots(1, 2, figsize=(11.6, 4.9), layout="constrained",
                         gridspec_kw={"width_ratios": [1.35, 1.0]})
fig.suptitle("Ethics and Illusions: Key Experimental Results",
             fontsize=16, fontweight="bold", color=YALE)

# ── Panel A: dollar levels (seller bias + winner overbidding) ──────
axA = axes[0]
labelsA = ["Seller bias\n(No Ethics)", "Seller bias\n(Mandatory)",
           "Winner overbidding\n(Baseline)"]
valsA   = [4.11, 5.65, 11.87]
colsA   = [BLUE_LIGHT, YALE, BLUE]
xA = range(len(labelsA))
axA.bar(xA, valsA, color=colsA, edgecolor="white", linewidth=0.8, width=0.62, zorder=3)
axA.set_xticks(list(xA), labelsA)
axA.set_ylim(0, 13.5)
axA.set_ylabel("Dollars ($)", fontsize=11, color=INK_SOFT)
axA.set_title("Dollar Magnitudes in the Auction", **TITLE_KW)
axA.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in zip(xA, valsA):
    axA.text(x, v + 0.2, f"${v:.2f}", ha="center", va="bottom", **VLAB_KW)
# annotate the (insignificant) ethics effect on seller bias
axA.annotate("", xy=(1, 6.35), xytext=(0, 6.35),
             arrowprops=dict(arrowstyle="<->", color=MUTED, lw=1.0))
axA.text(0.5, 6.65, "+$1.85 (n.s.)", ha="center", va="bottom",
         fontsize=9.5, color=MUTED, fontstyle="italic")
style(axA)

# ── Panel B: bidder learning per round ($/round) ───────────────────
axB = axes[1]
labelsB = ["No Ethics", "With Ethics"]
valsB   = [-0.23, 0.0]
colsB   = [BLUE, BLUE_LIGHT]
xB = range(len(labelsB))
axB.bar(xB, valsB, color=colsB, edgecolor="white", linewidth=0.8, width=0.55, zorder=3)
axB.set_xticks(list(xB), labelsB)
axB.set_ylim(-0.30, 0.10)
axB.axhline(0, color="#9aa1ab", linewidth=1.0, zorder=2)
axB.set_ylabel("Change in prediction error\nper round ($)", fontsize=11, color=INK_SOFT)
axB.set_title("Bidder Learning per Round", **TITLE_KW)
axB.grid(axis="y", color=RULE, linewidth=1, zorder=0)
axB.text(0, -0.23 - 0.006, "−$0.23**", ha="center", va="top", **VLAB_KW)
axB.text(1, 0.012, "≈ 0 (n.s.)", ha="center", va="bottom",
         fontsize=10.5, fontweight="bold", color=MUTED)
axB.text(0.5, -0.285, "Between-regime differential: $0.17/round (sig. 5%)",
         ha="center", va="bottom", fontsize=9, color=MUTED, fontstyle="italic")
style(axB)

out = "ethics_illusions_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
