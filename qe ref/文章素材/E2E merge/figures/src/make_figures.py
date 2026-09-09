"""Colored paper figures regenerated from the original manuscript data."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Nimbus Roman", "Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 200,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

COL = {
    "TA": "#95a5a6",
    "Fisher": "#b8aa9a",
    "Iso-C": "#e67e22",
    "TSV-M": "#16a085",
    "RegMean++": "#2c3e50",
    "E2E (ours)": "#c0392b",
}
OURS = COL["E2E (ours)"]

# Endpoint summary retained from the original source.
METHODS = ["TA", "Iso-C", "TSV-M", "RegMean++", "E2E (ours)"]
panels = [
    ("ViT-B/32 (8 tasks)",  [67.6, 80.4, 83.1, 84.2, 90.2], (60, 96)),
    ("ViT-B/16 (8 tasks)",  [77.1, 85.1, 87.1, 87.3, 92.0], (60, 96)),
    ("ViT-L/14 (8 tasks)",  [80.5, 90.7, 90.6, 90.9, 94.3], (60, 96)),
    ("ViT-L/14 (20 tasks)", [36.0, 83.4, 83.2, 82.2, 92.9], (30, 98)),
]
fig, axes = plt.subplots(2, 2, figsize=(7.2, 4.6))
for ax, (title, vals, xlim) in zip(axes.ravel(), panels):
    y = np.arange(len(METHODS))
    ax.barh(y, vals, color=[COL[m] for m in METHODS], height=0.66)
    ax.set_yticks(y)
    ax.set_yticklabels(METHODS, fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlim(*xlim)
    ax.set_xlabel("Avg. accuracy (%)", fontsize=9)
    ax.set_title(title, fontsize=10, weight="bold")
    for yi, v in zip(y, vals):
        ax.text(v - (xlim[1] - xlim[0]) * 0.012, yi, f"{v:.1f}",
                va="center", ha="right", fontsize=8, color="white", weight="bold")
fig.tight_layout()
fig.savefig("fig_main.pdf")
plt.close(fig)

# Per-task ViT-L/14 comparison.
tasks = ["SUN397", "Cars", "RESISC45", "EuroSAT", "SVHN", "GTSRB", "MNIST", "DTD"]
e2e = [82.6, 92.7, 97.1, 99.1, 97.9, 99.3, 99.7, 85.6]
rmpp = [77.0, 89.4, 92.6, 97.6, 96.9, 96.6, 99.1, 78.0]
x = np.arange(len(tasks))
w = 0.38
fig, ax = plt.subplots(figsize=(7.0, 2.6))
ax.bar(x - w / 2, rmpp, w, label="RegMean++", color=COL["RegMean++"])
ax.bar(x + w / 2, e2e, w, label="E2E (ours)", color=OURS)
ax.set_xticks(x)
ax.set_xticklabels(tasks, fontsize=8.5, rotation=18)
ax.set_ylabel("Accuracy (%)", fontsize=9)
ax.set_ylim(70, 103)
ax.set_title("Per-task accuracy, CLIP ViT-L/14 (8-task merge)", fontsize=10, weight="bold")
ax.legend(fontsize=9, frameon=False, ncol=2, loc="lower center", bbox_to_anchor=(0.5, 1.06))
for xi, (a, b) in enumerate(zip(rmpp, e2e)):
    ax.text(xi + w / 2, b + 0.5, f"+{b-a:.1f}", ha="center", fontsize=7, color=OURS)
fig.tight_layout()
fig.savefig("fig_pertask.pdf")
plt.close(fig)

# Update/learning-rate frontier.
curves = {
    r"$5\times10^{-6}$": ([4000, 8000, 12000], [89.24, 90.08, 90.24], OURS, "o"),
    r"$1\times10^{-5}$": ([2000, 4000, 6000], [86.94, 88.42, 88.80], COL["RegMean++"], "s"),
}
extra = [
    (12000, 89.95, r"$2\times10^{-6}$"),
    (8000, 89.88, r"$3\times10^{-6}$"),
    (2000, 85.85, r"$2\times10^{-5}$"),
]
fig, ax = plt.subplots(figsize=(4.4, 2.9))
for lab, (xs, ys, c, m) in curves.items():
    ax.plot(xs, ys, m + "-", color=c, ms=5, lw=1.7, label=lab)
for xx, yy, ll in extra:
    ax.plot(xx, yy, "D", color="white", mec="#555555", mew=1.1, ms=6)
    ax.annotate(ll, (xx, yy), fontsize=7.5, color="#333333", xytext=(4, -11), textcoords="offset points")
ax.axhline(84.2, ls="--", color="#7f8c8d", lw=1)
ax.text(2200, 84.55, "RegMean++ (84.2)", fontsize=8, color="#7f8c8d")
ax.set_xlabel("Student update steps", fontsize=9)
ax.set_ylabel("Avg. accuracy (%)", fontsize=9)
ax.set_title("Accuracy versus update budget (ViT-B/32)", fontsize=10, weight="bold")
ax.legend(fontsize=8, frameon=False, loc="lower right", title="learning rate", title_fontsize=8)
ax.set_ylim(83.5, 91)
fig.tight_layout()
fig.savefig("fig_lr.pdf")
plt.close(fig)

# Expert-count scaling.
ks = [2, 4, 6, 8]
e2e_s = [77.5, 86.7, 90.4, 90.2]
rm_s = [74.9, 83.4, 86.0, 84.2]
fig, ax = plt.subplots(figsize=(4.4, 2.9))
ax.fill_between(ks, rm_s, e2e_s, color=OURS, alpha=0.14)
ax.plot(ks, e2e_s, "o-", color=OURS, ms=6, lw=1.8, label="E2E (ours)")
ax.plot(ks, rm_s, "s-", color=COL["RegMean++"], ms=6, lw=1.8, label="RegMean++")
for k, a, b in zip(ks, e2e_s, rm_s):
    ax.annotate(f"+{a-b:.1f}", (k, (a+b)/2), fontsize=8, color=OURS,
                ha="center", xytext=(10, -2), textcoords="offset points")
ax.set_xticks(ks)
ax.set_xlabel("Number of merged experts", fontsize=9)
ax.set_ylabel("Avg. accuracy (%)", fontsize=9)
ax.set_title("Distillation gain grows with expert count", fontsize=10, weight="bold")
ax.legend(fontsize=8.5, frameon=False, loc="upper right")
fig.tight_layout()
fig.savefig("fig_scaling.pdf")
plt.close(fig)

# Layer-wise/final residual comparison.
perlayer = {
    "Task Arith.": [0.006, 0.147, 0.157, 0.172, 0.191, 0.241, 0.285, 0.271, 0.261, 0.239, 0.279, 0.385, 0.744],
    "RegMean++": [0.004, 0.110, 0.110, 0.119, 0.146, 0.191, 0.234, 0.213, 0.195, 0.163, 0.181, 0.262, 0.502],
    "E2E (ours)": [0.006, 0.162, 0.152, 0.157, 0.171, 0.207, 0.229, 0.202, 0.181, 0.148, 0.151, 0.185, 0.233],
}
endres = {"Task Arith.": 0.83, "RegMean++": 0.55, "E2E (ours)": 0.23}
cmap = {"Task Arith.": COL["TA"], "RegMean++": COL["RegMean++"], "E2E (ours)": OURS}
mkr = {"Task Arith.": "o", "RegMean++": "s", "E2E (ours)": "^"}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.4, 2.9), gridspec_kw={"width_ratios": [2, 1]})
for m, v in perlayer.items():
    ax1.plot(range(len(v)), v, mkr[m] + "-", color=cmap[m], ms=3.5,
             lw=2.2 if "ours" in m else 1.4, label=m, zorder=5 if "ours" in m else 2)
ax1.set_xlabel(r"Layer depth $\ell$", fontsize=9)
ax1.set_ylabel("Relative residual vs. expert", fontsize=9)
ax1.set_title("Layer-wise residuals do not determine final error", fontsize=10, weight="bold")
ax1.legend(fontsize=8.5, frameon=False, loc="upper left")
names = list(endres)
vals = [endres[m] for m in names]
ax2.bar(range(len(names)), vals, color=[cmap[m] for m in names], width=0.62)
ax2.set_xticks(range(len(names)))
ax2.set_xticklabels(names, rotation=18, fontsize=8)
ax2.set_ylabel("End-to-end residual", fontsize=9)
ax2.set_title("Final representation error", fontsize=10, weight="bold")
for i, v in enumerate(vals):
    ax2.text(i, v + 0.01, f"{v:.2f}", ha="center", va="bottom", fontsize=8.5)
ax2.set_ylim(0, 0.95)
fig.tight_layout()
fig.savefig("fig_compound.pdf")
plt.close(fig)
