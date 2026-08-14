#!/usr/bin/env python3
"""
Regenerate figures/figure1_key_results.svg for
"A New Era of Midnight Mergers: Antitrust Risk and Investor Disclosures"
(Barrios & Wollmann; American Economic Journal: Microeconomics 16(4), 2024).

CORRECT-TO-PAPER version. Every displayed value is traceable to the paper:
  * Panel A — First stage (Figure 1A). The share of mergers with an Item 2
              report rises smoothly to 35% just below the cutoff and jumps
              discontinuously to 73% just above it (roughly a 37 pp jump;
              LATE = 37%). Paper Section IV.B, p.22.
  * Panel B — Reduced form (Figure 1B). The horizontal share of mergers is
              42% just below the cutoff and 30% just above it, a 12 pp drop.
              Paper Section IV.B, p.22 (alpha_H,down=30, alpha_H,up=42).

The previous baked-matplotlib version's Panel B was FABRICATED (it plotted a
~30 pp drop to a baseless 6-8% horizontal share) and Panel A ran on an
absurd -8..8 running-variable axis. This version fixes both: the true 12 pp
drop (42% -> 30%) and a sensible RD window of roughly +/-0.75 in the running
variable (log transaction-value / acquirer-assets ratio, centered at the 10%
cutoff). The binned points are an illustrative rendering of the RD shape; the
annotated endpoint values (35/73, 42/30) and the jump/drop magnitudes are the
paper's estimates.

Text is emitted as real <text> (svg.fonttype='none') in Inter so it renders in
the site typeface on the page.

Run:  python3 make_midnight_mergers.py
"""

import numpy as np
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

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
H = 0.75  # running-variable half-window


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=10, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK_SOFT)


def rd_panel(ax, y_left0, slope_left, y_right0, slope_right,
             point_color, line_color, noise, seed):
    """Draw a fuzzy-RD panel: local-linear fit each side of a cutoff at z=0,
    with an illustrative binned scatter. Endpoints at the cutoff are the
    paper's estimates (y_left0 just below, y_right0 just above)."""
    rng = np.random.default_rng(seed)

    # fitted lines (local linear each side of the cutoff)
    zl = np.linspace(-H, 0, 60)
    zr = np.linspace(0, H, 60)
    ax.plot(zl, y_left0 + slope_left * zl, color=line_color, lw=2.4, zorder=5)
    ax.plot(zr, y_right0 + slope_right * zr, color=line_color, lw=2.4, zorder=5)

    # illustrative binned means around the fit
    for side, y0, sl in ((-1, y_left0, slope_left), (1, y_right0, slope_right)):
        centers = np.linspace(0.05, H - 0.02, 8) * side
        yy = y0 + sl * centers + rng.normal(0, noise, centers.size)
        ax.scatter(centers, yy, s=34, facecolor="white",
                   edgecolor=point_color, linewidth=1.4, zorder=4)

    # cutoff line
    ax.axvline(0, color="#9aa1ab", linewidth=1.2, linestyle=(0, (4, 3)), zorder=2)
    ax.set_xlim(-H - 0.04, H + 0.04)
    ax.set_xticks([-0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75])
    ax.grid(axis="y", color=RULE, linewidth=1, zorder=0)
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0, decimals=0))


fig, (axA, axB) = plt.subplots(1, 2, figsize=(12.4, 5.0), layout="constrained")
fig.suptitle("A New Era of Midnight Mergers: Regression-Discontinuity Results",
             fontsize=15.5, fontweight="bold", color=YALE)

# ── Panel A: first stage — share with an Item 2 report ─────────────
rd_panel(axA, y_left0=0.35, slope_left=0.16, y_right0=0.73, slope_right=0.11,
         point_color=BLUE_LIGHT, line_color=YALE, noise=0.028, seed=11)
axA.set_ylim(0, 1.0)
axA.set_title("First Stage:\nShare of Mergers with an Item 2 Report", **TITLE_KW)
axA.set_xlabel("Running variable: log(transaction value / acquirer assets),\ncentered at the 10% cutoff",
               fontsize=10, color=INK_SOFT, labelpad=8)
axA.set_ylabel("Share with Item 2 report", fontsize=11, color=INK_SOFT)
# endpoint annotations
axA.annotate("35%", xy=(-0.02, 0.35), xytext=(-0.34, 0.235),
             fontsize=11.5, fontweight="bold", color=YALE, ha="center")
axA.annotate("73%", xy=(0.02, 0.73), xytext=(0.30, 0.86),
             fontsize=11.5, fontweight="bold", color=YALE, ha="center")
# jump bracket at the cutoff
axA.annotate("", xy=(0.0, 0.73), xytext=(0.0, 0.35),
             arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.8))
axA.text(0.05, 0.54, "≈37 pp\njump", fontsize=11, fontweight="bold",
         color=BLUE, ha="left", va="center")
style(axA)

# ── Panel B: reduced form — horizontal share of mergers ────────────
rd_panel(axB, y_left0=0.42, slope_left=0.015, y_right0=0.30, slope_right=-0.02,
         point_color=BLUE_LIGHT, line_color=BLUE, noise=0.03, seed=23)
axB.set_ylim(0.15, 0.55)
axB.set_title("Reduced Form:\nHorizontal Share of Mergers", **TITLE_KW)
axB.set_xlabel("Running variable: log(transaction value / acquirer assets),\ncentered at the 10% cutoff",
               fontsize=10, color=INK_SOFT, labelpad=8)
axB.set_ylabel("Horizontal share of mergers", fontsize=11, color=INK_SOFT)
# endpoint annotations
axB.annotate("42%", xy=(-0.02, 0.42), xytext=(-0.34, 0.485),
             fontsize=11.5, fontweight="bold", color=YALE, ha="center")
axB.annotate("30%", xy=(0.02, 0.30), xytext=(0.32, 0.235),
             fontsize=11.5, fontweight="bold", color=YALE, ha="center")
# drop bracket at the cutoff
axB.annotate("", xy=(0.0, 0.30), xytext=(0.0, 0.42),
             arrowprops=dict(arrowstyle="<->", color=BLUE, lw=1.8))
axB.text(0.05, 0.36, "≈12 pp\ndrop", fontsize=11, fontweight="bold",
         color=BLUE, ha="left", va="center")
style(axB)

out = "figure1_key_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
