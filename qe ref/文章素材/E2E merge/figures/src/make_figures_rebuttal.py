"""Colored memory--accuracy frontiers from the original block-wise results."""
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
MEM = "#e67e22"
b32 = [(1, 85.31, 3.71), (2, 87.36, 3.85), (3, 88.40, 4.01),
       (4, 88.94, 4.16), (6, 89.17, 4.47), (12, 89.84, 5.40)]
l14 = [(1, 92.05, 13.26), (4, 93.05, 15.42), (24, 94.22, 30.87)]
panels = [
    ("ViT-B/32 (12 blocks)", b32, 84.2, (83.5, 90.6)),
    ("ViT-L/14 (24 blocks)", l14, 90.9, (89.5, 95.2)),
]
fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.1))
for ax, (title, data, baseline, ylim) in zip(axes, panels):
    groups = [r[0] for r in data]
    accs = [r[1] for r in data]
    ax.axhline(baseline, ls="--", color=RM, lw=1.2)
    ax.text(groups[-1], baseline + (ylim[1] - ylim[0]) * 0.012,
            f"RegMean++: {baseline}", fontsize=7.5, color=RM, ha="right")
    ax.plot(groups, accs, "o-", color=OURS, ms=6, lw=1.8, zorder=5)
    for g, acc, mem in data:
        ax.annotate(f"{mem:.0f} GB", (g, acc), fontsize=7, color=MEM,
                    xytext=(0, -13), textcoords="offset points", ha="center")
    ax.annotate("full", (groups[-1], accs[-1]), fontsize=8, color=OURS,
                xytext=(-4, 7), textcoords="offset points", ha="right")
    ax.annotate("1 block", (groups[0], accs[0]), fontsize=8, color=OURS,
                xytext=(8, -1), textcoords="offset points")
    ax.set_xlabel("Blocks optimized jointly", fontsize=9)
    ax.set_ylabel("Avg. accuracy (%)", fontsize=9)
    ax.set_title(title, fontsize=10, weight="bold")
    ax.set_xticks(groups)
    ax.set_ylim(*ylim)
fig.tight_layout()
fig.savefig("fig_blockwise.pdf")
