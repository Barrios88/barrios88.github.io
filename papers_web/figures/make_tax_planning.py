#!/usr/bin/env python3
"""
Regenerate figures/tax_planning_results.svg for
"Tax Planning Knowledge Diffusion via the Labor Market"
(Barrios & Gallemore; Management Science 70(2), 2024, pp.1194-1215).

CORRECT-TO-PAPER version. Every bar is traceable to the paper:
  * Left panel  — effect of Hire from TA Firm on Cash ETR by specification (Table 3):
        (1) No controls                  -0.037 ***
        (2) Time-varying controls        -0.031 ***
        (3) Controls + Sector/Year FE    -0.028 ***
        (4) Full controls + Firm FE      -0.018 *   (p<0.10, saturated model)
  * Right panel — robustness (Table 4):
        Baseline                         -0.027 ***
        Bottom 20%                       -0.034 ***
        Bottom 30%                       -0.025 ***
        Sector-Size Adj Only             -0.022 **
        Unadjusted ETR Only              -0.021 ***
        Entropy Balancing                -0.021 ***
All coefficients are negative (hiring from a tax-aggressive firm LOWERS the
destination firm's cash ETR). Prior fabricated bars (e.g. right-panel Baseline
-0.037) have been replaced with the values above. Text is emitted as real
<text> (svg.fonttype='none') in Inter so it renders in the site typeface.

Run:  python3 make_tax_planning.py
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
VLAB_KW  = dict(fontsize=10, fontweight="bold", color=YALE)


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK_SOFT)


def draw(ax, labels, vals, stars, emph_idx, title):
    """Horizontal bars, all negative, value+stars labelled to the left of each tip."""
    y = range(len(labels))
    cols = [BLUE if i == emph_idx else YALE for i in range(len(labels))]
    ax.barh(y, vals, color=cols, edgecolor="white", linewidth=0.8, height=0.62, zorder=3)
    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.set_xlim(-0.052, 0.004)
    ax.set_xticks([-0.04, -0.03, -0.02, -0.01, 0.0])
    ax.axvline(0, color="#9aa1ab", linewidth=1.0, zorder=2)
    ax.set_xlabel("Coefficient (change in cash ETR)",
                  fontsize=10.5, color=INK_SOFT, labelpad=8)
    ax.set_title(title, **TITLE_KW)
    ax.grid(axis="x", color=RULE, linewidth=1, zorder=0)
    for yi, v, s in zip(y, vals, stars):
        ax.text(v - 0.0015, yi, f"−{abs(v):.3f}{s}", va="center", ha="right", **VLAB_KW)
    style(ax)


fig, (axL, axR) = plt.subplots(1, 2, figsize=(13.6, 5.2), layout="constrained")
fig.suptitle("Hiring from a Tax-Aggressive Firm Lowers the Destination Firm's Cash ETR",
             fontsize=15.5, fontweight="bold", color=YALE)

# ── Left panel: effect by specification (Table 3) ──────────────────
draw(
    axL,
    labels=["(1) No controls",
            "(2) Time-varying controls",
            "(3) Controls + Sector/Year FE",
            "(4) Full controls + Firm FE"],
    vals=[-0.037, -0.031, -0.028, -0.018],
    stars=["***", "***", "***", "*"],
    emph_idx=3,
    title="Effect by Specification\n(Table 3)",
)

# ── Right panel: robustness (Table 4) ──────────────────────────────
draw(
    axR,
    labels=["Baseline",
            "Bottom 20%",
            "Bottom 30%",
            "Sector-Size Adj Only",
            "Unadjusted ETR Only",
            "Entropy Balancing"],
    vals=[-0.027, -0.034, -0.025, -0.022, -0.021, -0.021],
    stars=["***", "***", "***", "**", "***", "***"],
    emph_idx=0,
    title="Robustness\n(Table 4)",
)

# significance-key footnote
fig.text(0.5, 0.012,
         "*** p<0.01,   ** p<0.05,   * p<0.10.",
         ha="center", fontsize=9.5, color=MUTED)

out = "tax_planning_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
