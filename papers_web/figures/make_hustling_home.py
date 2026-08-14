#!/usr/bin/env python3
"""
Regenerate figures/hustling_home_results.svg for
"Hustling from Home? Work from Home Flexibility and Entrepreneurial Entry"
(Barrios, Hochberg, Yi; NBER WP 33237, working paper).

CORRECT-TO-PAPER version. Every value here is traceable to the paper's tables:
  * Panel A — Table 2: pre-pandemic Teleworkable Share coefficients
              (0.494, 0.146, 0.140), Log New Business Registration.
  * Panel B — Table 3: DiD Post x Teleworkable Share across specifications
              (-0.103, -0.100, -0.093, -0.072).
  * Panel C — Table 4 (OLS): main Post x Teleworkable Share coefficients in the
              telework x internet-speed model (-0.088, -0.082, -0.079).
              NOTE: relabeled from "2SLS" to OLS Table 4 per number-accuracy audit;
              these bars are OLS coefficients, not the 2SLS second-stage estimates.
  * Panel D — Table 8: gender DiD (Post x Teleworkable) on women-led formation
              (All-female share -0.892, Some-female share -1.589).
  * Panel E — Table 9 col (1): survey effects on likelihood of leaving to start a
              business (values flexibility +0.086**, current job offers flexibility
              -0.039 [insignificant, NO star], interaction -0.174*).

The prior baked-matplotlib figure mislabeled Panel C as "2SLS" and carried a
spurious significance star on the -0.039 survey coefficient; both are fixed here.
No "89-159%" gender gloss is displayed (unsupported by the paper). Text is emitted
as real <text> (svg.fonttype='none') in Inter so it renders in the site typeface.

Run:  python3 make_hustling_home.py
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

TITLE_KW = dict(fontsize=12, fontweight="bold", color=YALE, pad=10)
VLAB_KW  = dict(fontsize=9.5, fontweight="bold", color=YALE)


def style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors=MUTED, labelsize=9, length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(INK_SOFT)


def bar_panel(ax, cats, vals, colors, stars, title, ylabel, ylim):
    """Vertical bar panel with signed value+star labels placed clear of the bar."""
    x = range(len(cats))
    ax.bar(x, vals, color=colors, edgecolor="white", linewidth=0.8,
           width=0.62, zorder=3)
    ax.set_xticks(list(x))
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylim(*ylim)
    ax.axhline(0, color="#9aa1ab", linewidth=1.0, zorder=2)
    ax.set_ylabel(ylabel, fontsize=10, color=INK_SOFT)
    ax.set_title(title, **TITLE_KW)
    ax.grid(axis="y", color=RULE, linewidth=1, zorder=0)
    span = ylim[1] - ylim[0]
    off = 0.022 * span
    for xi, v, s in zip(x, vals, stars):
        sign = "+" if v >= 0 else "−"
        txt = f"{sign}{abs(v):.3f}{s}"
        if v >= 0:
            ax.text(xi, v + off, txt, ha="center", va="bottom", **VLAB_KW)
        else:
            ax.text(xi, v - off, txt, ha="center", va="top", **VLAB_KW)
    style(ax)


mosaic = """
AABBCC
DDDEEE
"""
fig, axd = plt.subplot_mosaic(mosaic, figsize=(15, 8.7), layout="constrained")
fig.suptitle("Work-from-Home Potential and Entrepreneurial Entry: Key Empirical Results",
             fontsize=16, fontweight="bold", color=YALE)

# Panel A — Table 2 (pre-pandemic baseline)
bar_panel(
    axd["A"],
    cats=["No\nControls", "+ Controls", "+ Controls &\nState×Qtr FE"],
    vals=[0.494, 0.146, 0.140],
    colors=[BLUE, BLUE, YALE],
    stars=["***", "***", "***"],
    title="A. Pre-Pandemic Baseline\nLog New Business Registration (Table 2)",
    ylabel="Coefficient on\nTeleworkable Share (std)",
    ylim=(0, 0.60),
)

# Panel B — Table 3 (difference-in-differences)
bar_panel(
    axd["B"],
    cats=["(1)\nControls", "(2)\nState &\nTime FE", "(3)\nZip &\nTime FE", "(4)\nZip &\nState×Month FE"],
    vals=[-0.103, -0.100, -0.093, -0.072],
    colors=[YALE, YALE, YALE, BLUE],
    stars=["***", "***", "***", "***"],
    title="B. Difference-in-Differences\nPost × Teleworkable Share (Table 3)",
    ylabel="Coefficient",
    ylim=(-0.135, 0.02),
)

# Panel C — Table 4 (OLS: telework x internet speed)  [relabeled from 2SLS]
bar_panel(
    axd["C"],
    cats=["(1)", "(2)", "(3)"],
    vals=[-0.088, -0.082, -0.079],
    colors=[YALE, YALE, YALE],
    stars=["***", "***", "***"],
    title="C. Telework × Internet Speed\n(OLS, Table 4)",
    ylabel="Coefficient",
    ylim=(-0.115, 0.02),
)

# Panel D — Table 8 (gender)
bar_panel(
    axd["D"],
    cats=["All-Female\nFounders", "Some-Female\nFounders"],
    vals=[-0.892, -1.589],
    colors=[YALE, BLUE],
    stars=["***", "***"],
    title="D. Gender: Women-Led Formation\nPost × Teleworkable Share (Table 8)",
    ylabel="Coefficient on share of\nwomen-founded businesses",
    ylim=(-1.85, 0.12),
)

# Panel E — Table 9 col (1) (survey)
bar_panel(
    axd["E"],
    cats=["Values Flexibility\nHighly", "Current Job\nOffers Flexibility", "Values Flex. ×\nJob Offers Flex."],
    vals=[0.086, -0.039, -0.174],
    colors=[BLUE, BLUE_LIGHT, YALE],
    stars=["**", "", "*"],
    title="E. Survey Evidence\nLikelihood of Leaving to Start a Business (Table 9)",
    ylabel="Effect on likelihood\nof leaving to start-up",
    ylim=(-0.24, 0.16),
)

out = "hustling_home_results.svg"
fig.savefig(out, format="svg", bbox_inches="tight", facecolor="white")
print("wrote", out)
