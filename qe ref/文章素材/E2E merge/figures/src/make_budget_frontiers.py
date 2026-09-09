"""Colored three-panel budget frontier, using only original reported data."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Nimbus Roman", "Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})
OURS = "#c0392b"
RM = "#2c3e50"
ORANGE = "#e67e22"
TEAL = "#16a085"
GREY = "#7f8c8d"

fig, axes = plt.subplots(1, 3, figsize=(10.2, 2.65))

# Data budget.
N = [64, 128, 256, 512, 1024]
e2e_n = [81.3, 83.5, 86.1, 87.7, 88.5]
rm_n = [83.3, 83.9, 84.4, 84.3, 84.5]
axes[0].plot(N, e2e_n, "o-", color=OURS, lw=1.8, ms=5, label="E2E, fixed set")
axes[0].plot(N, rm_n, "s--", color=RM, lw=1.6, ms=4.5, label="RegMean++")
axes[0].axhline(90.1, color=ORANGE, linestyle=":", lw=1.2, label="E2E, full split")
axes[0].axvline(256, color=GREY, linestyle=":", lw=0.8)
axes[0].set_xscale("log", base=2)
axes[0].set_xticks(N)
axes[0].set_xticklabels([str(x) for x in N])
axes[0].set_xlabel("Distinct examples / task")
axes[0].set_ylabel("Average accuracy (%)")
axes[0].set_title("Data budget", weight="bold")
axes[0].legend(fontsize=7, frameon=False, loc="lower right")

# Iteration budget.
steps = [4000, 8000, 12000]
e2e_steps = [89.2, 90.1, 90.2]
axes[1].plot(steps, e2e_steps, "o-", color=OURS, lw=1.8, ms=5,
             label=r"E2E, $5\times10^{-6}$")
axes[1].axhline(84.2, color=RM, linestyle="--", lw=1.2, label="RegMean++")
for x, y in zip(steps, e2e_steps):
    axes[1].annotate(f"{y:.1f}", (x, y), xytext=(0, 5), textcoords="offset points",
                     ha="center", fontsize=7, color=OURS)
axes[1].set_xticks(steps)
axes[1].set_xlabel("Student update steps")
axes[1].set_title("Iteration budget", weight="bold")
axes[1].legend(fontsize=7, frameon=False, loc="lower right")

# Memory budget.
mem = [3.7, 3.9, 4.0, 4.2, 4.5, 5.4, 8.0]
acc = [85.3, 87.4, 88.4, 88.9, 89.2, 89.8, 90.2]
labels = ["1", "2", "3", "4", "6", "12", "full"]
axes[2].plot(mem, acc, "o-", color=TEAL, lw=1.8, ms=5)
for x, y, lab in zip(mem, acc, labels):
    axes[2].annotate(lab, (x, y), xytext=(2, 4), textcoords="offset points",
                     fontsize=7, color=TEAL)
axes[2].axhline(84.2, color=RM, linestyle="--", lw=1.2, label="RegMean++ acc.")
axes[2].set_xlabel("Peak memory (GB)")
axes[2].set_title("Memory budget (B/32)", weight="bold")
axes[2].legend(fontsize=7, frameon=False, loc="lower right")

for ax in axes:
    ax.grid(True, linewidth=0.35, alpha=0.25, color=GREY)
    ax.tick_params(axis="both", labelsize=8)
fig.tight_layout(pad=0.7, w_pad=1.2)
fig.savefig("fig_budget_frontiers.pdf", bbox_inches="tight")
