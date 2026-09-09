"""Colored data-budget frontier using only values in the original manuscript."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
OURS = "#c0392b"
RM = "#2c3e50"
GUIDE = "#7f8c8d"
N = [64, 128, 256, 512, 1024]
e2e = [81.3, 83.5, 86.1, 87.7, 88.5]
rmpp = [83.3, 83.9, 84.4, 84.3, 84.5]
stream = 90.1
fig, ax = plt.subplots(figsize=(4.6, 3.3))
ax.axhline(stream, ls=":", color=OURS, lw=1.1)
ax.annotate(f"E2E, full split ({stream:.1f})", (64, stream + 0.25), fontsize=7.5,
            color=OURS, ha="left", va="bottom")
ax.plot(N, e2e, "o-", color=OURS, ms=6, lw=1.8, zorder=5, label="E2E, fixed set")
ax.plot(N, rmpp, "s--", color=RM, ms=5, lw=1.6, zorder=4, label="RegMean++")
ax.axvline(256, color=GUIDE, lw=0.8, ls=":")
ax.annotate("RegMean default\nunique-example budget", (256, 80.0), fontsize=7.0,
            color="#555555", ha="center", va="bottom")
ax.set_xscale("log", base=2)
ax.set_xticks(N)
ax.set_xticklabels([str(n) for n in N])
ax.set_xlabel("Distinct unlabeled examples / task")
ax.set_ylabel("Avg. accuracy (%)")
ax.set_title("Data-budget crossover", fontsize=10, weight="bold")
ax.legend(fontsize=8, loc="lower right", frameon=False)
fig.tight_layout()
fig.savefig("fig_dataeff.pdf")
