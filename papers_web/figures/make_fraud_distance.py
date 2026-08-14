#!/usr/bin/env python3
"""
Regenerate figures/fraud_distance_results.svg for
"Fraud at a Distance? How Remote Work Shapes Financial Misconduct"
(Barrios, Guo, Zhu; working paper, 2026).

CORRECT-TO-PAPER version. Every value here is traceable to the paper:
  * Panel A — Logit-implied predicted probability of misconduct falls from a
              sample mean of ~2% to ~0.8% for high-WFH-feasibility firms
              (Section 4, pp. 22-23; sample mean of Misconduct = 0.017).
  * Panel B — detection lag (time from fraud onset to class-action filing)
              is ~52% shorter in the post-period for higher-WFH firms
              (Table 3 Panel B, p. 22). Shown as an illustrative relative
              index (100 -> 48) that encodes the real 52% reduction.
  * Panel C — implied Q1->Q3 declines in misconduct probability across the
              cross-sectional cuts, from the interaction coefficients:
              Low Overall culture -0.071*** (~2.5pp, LARGEST), High Teamwork
              -0.058*** (~2.0pp), Effective SOX 302 -0.057*** (~2.0pp),
              Effective SOX 404 -0.055*** (~1.9pp) (Tables 6-8).
The previous version's fabricated bars (Panel A quartile bars 2.2/2.1/0.2%;
Panel C cross-section 3.8/3.2/3.5%, mis-ordered) have been removed. The
paper's LARGEST cross-sectional effect is weak culture, not teamwork.
Text is emitted as real <text> (svg.fonttype='none') in Inter so it renders
in the site typeface on the page.

Run:  python3 make_fraud_distance.py
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
fig.suptitle("Fraud at a Distance: Key Empirical Results",
             fontsize=16, fontweight="bold", color=YALE)

# ── Panel A: Logit-implied predicted probability of misconduct ─────
axA = axes[0]
catsA = ["At Sample Mean", "High WFH\nFeasibility"]
valsA = [2.0, 0.8]
axA.bar(catsA, valsA, color=[BLUE_LIGHT, YALE], edgecolor="white",
        linewidth=0.8, width=0.6, zorder=3)
axA.set_ylim(0, 2.6)
axA.set_ylabel("Predicted Misconduct\nProbability (%)", fontsize=11, color=INK_SOFT)
axA.set_title("Logit-Implied Probability\nof Misconduct", **TITLE_KW)
axA.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsA):
    axA.text(x, v + 0.06, f"{v:.1f}%", ha="center", va="bottom", **VLAB_KW)
style(axA)

# ── Panel B: detection lag, ~52% shorter (illustrative index) ──────
axB = axes[1]
catsB = ["Low WFH\n(reference)", "High WFH\nFeasibility"]
valsB = [100, 48]
axB.bar(catsB, valsB, color=[BLUE_LIGHT, YALE], edgecolor="white",
        linewidth=0.8, width=0.6, zorder=3)
axB.set_ylim(0, 122)
axB.set_ylabel("Detection Lag Index\n(illustrative)", fontsize=11, color=INK_SOFT)
axB.set_title("Time to Detection\n(~52% Shorter)", **TITLE_KW)
axB.grid(axis="y", color=RULE, linewidth=1, zorder=0)
for x, v in enumerate(valsB):
    axB.text(x, v + 2.5, f"{v}", ha="center", va="bottom", **VLAB_KW)
axB.annotate("", xy=(1, 52), xytext=(1, 98),
             arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.8))
axB.text(1.0, 74, "52%\nshorter", ha="center", va="center",
         fontsize=10, fontweight="bold", color=BLUE)
style(axB)

# ── Panel C: implied Q1->Q3 declines, weak culture is LARGEST ──────
axC = axes[2]
catsC = ["Weak Culture\n(Low Overall)", "Teamwork-\nIntensive",
         "Effective\nSOX 302", "Effective\nSOX 404"]
valsC = [2.5, 2.0, 2.0, 1.9]
colsC = [BLUE, YALE, YALE, YALE]
axC.bar(catsC, valsC, color=colsC, edgecolor="white",
        linewidth=0.8, width=0.66, zorder=3)
axC.set_ylim(0, 3.0)
axC.set_ylabel("Implied Decline in\nMisconduct (pp)", fontsize=11, color=INK_SOFT)
axC.set_title("Where the Decline\nConcentrates (Q1→Q3)", **TITLE_KW)
axC.grid(axis="y", color=RULE, linewidth=1, zorder=0)
axC.tick_params(axis="x", labelsize=8.5)
for x, v in enumerate(valsC):
    axC.text(x, v + 0.06, f"{v:.1f}", ha="center", va="bottom", **VLAB_KW)
style(axC)

out = "fraud_distance_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
