#!/usr/bin/env python3
"""Publication-quality figure suite for the AnchorPath paper.

One cohesive house style: Times-matching serif body + STIX math so every figure reads as a
seamless extension of the (Times-set) paper. Every number is real (from outputs/experiments).
Run: python paper/curvflow/make_figs.py
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import numpy as np
import os

OUT = os.path.join(os.path.dirname(__file__), "figs")
os.makedirs(OUT, exist_ok=True)

# ---------------- house style : Times-matching serif + STIX math ----------------
# Nimbus Roman is a metric clone of Times; STIX gives Times-like math glyphs. Together the
# figures share the body font, which is the single biggest step away from a "default matplotlib" look.
PAL = dict(
    one="#B42318",      # one-shot  (deep warm red)
    flow="#1D4ED8",     # AnchorPath  (deep blue)  -- ours, everywhere
    flow_soft="#93B4F5",# light blue fill / K=4
    k4="#7FA8D9",       # K=4 (mid blue)
    fl="#0E7C66",       # front-loaded schedule (teal-green, a third hue)
    true="#334155",     # "true risk" reference curve (slate ink)
    grey="#94A3B8",
    ink="#1E293B",
    band="#DBE4F3",     # soft blue band fill
)
BASE_COLORS = {"Wanda-sp":"#7E3FB0","FLAP":"#C77C0E","LLM-Pruner (no FT)":"#1C8A54",
               "Magnitude":"#9AA4AF","Random":"#6B7A8D"}
plt.rcParams.update({
    "figure.dpi": 150, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
    "font.family": "serif",
    "font.serif": ["Nimbus Roman", "Times New Roman", "STIXGeneral", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 12.0, "axes.titlesize": 12.5, "axes.labelsize": 12.0,
    "axes.edgecolor": "#5A5A5A", "axes.linewidth": 0.8,
    "axes.grid": True, "grid.color": "#D2D7DE", "grid.linewidth": 0.55, "grid.alpha": 0.55,
    "axes.axisbelow": True, "legend.frameon": False, "legend.fontsize": 10.0,
    "legend.handlelength": 1.7, "legend.handletextpad": 0.5, "legend.labelspacing": 0.32,
    "xtick.color": "#3A3A3A", "ytick.color": "#3A3A3A",
    "xtick.labelsize": 10.5, "ytick.labelsize": 10.5,
    "axes.labelcolor": "#1E293B", "text.color": "#1E293B",
    "lines.solid_capstyle": "round", "lines.dash_capstyle": "round",
})

def despine(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

def title(ax, txt, **kw):
    ax.set_title(txt, fontweight="bold", pad=7, **kw)

def gainbox(ax, x, y, txt, color):
    ax.annotate(txt, xy=(x, y), ha="center", va="center", fontsize=11.0, fontweight="bold",
                color=color, zorder=8,
                bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=color, lw=1.1, alpha=0.97))

R = [0.10, 0.20, 0.30, 0.40, 0.50]
# ---- real data (WikiText-2 ppl) ----
# fl = front-loaded schedule at K=8 (default for rho>=0.3); coincides with equal at trivial sparsity.
L2  = dict(one=[6.38, 9.27, 19.86, 92.64, 1496.89], k4=[6.09, 9.01, 16.50, 56.38, 822.59],
           k8=[5.92, 8.63, 15.65, 33.59, 388.69], fl=[5.92, 9.08, 14.08, 32.30, 125.61])
L31 = dict(r=[0.20, 0.30, 0.40, 0.50], one=[14.0, 33.0, 245.9, 4106.4], k8=[12.1, 23.2, 47.2, 244.9])
QW  = dict(r=[0.20, 0.30, 0.40, 0.50], one=[14.3, 26.7, 63.7, 270.1],  k8=[11.1, 17.6, 41.5, 141.0])
YI  = dict(r=[0.20, 0.30, 0.40, 0.50], one=[423.6, 2479.6, 5194.4, 16509.6], k8=[7.8, 13.6, 31.9, 61.7])

ONE_LBL  = "One-shot ($K{=}1$)"
OURS_LBL = "\\textsc{AnchorPath}" if False else "AnchorPath"

# ============================================================ FIG 1: headline radar (single-column)
# Seven models on the spokes, WikiText-2 perplexity at rho=0.5 on a log radius. One-shot forms a large
# outer polygon; AnchorPath is contained deep inside it. Models ordered by descending one-shot ppl.
from matplotlib.lines import Line2D
_mods = ["Yi-1.5\n9B", "LLaMA-3.1\n8B", "LLaMA-3.2\n3B", "LLaMA-2\n7B", "Qwen2.5\n14B", "Qwen2.5\n7B", "Falcon3\n7B"]
_one05 = [16510.0, 4106.0, 3027.0, 1497.0, 300.8, 270.1, 62.5]
_ap05  = [61.7,    245.0,  325.0,  389.0,  156.0, 141.0, 27.8]
_N = len(_mods)
_ang = np.linspace(0, 2 * np.pi, _N, endpoint=False)
_ac = np.concatenate([_ang, _ang[:1]])
_or = np.log10(np.array(_one05 + _one05[:1]))
_ar = np.log10(np.array(_ap05 + _ap05[:1]))
fig = plt.figure(figsize=(3.5, 3.15))
ax = fig.add_subplot(111, polar=True)
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)
ax.fill(_ac, _or, color=PAL["one"], alpha=0.12, zorder=1)
ax.plot(_ac, _or, "-", color=PAL["one"], lw=1.9, zorder=3)
ax.fill(_ac, _ar, color=PAL["flow"], alpha=0.24, zorder=2)
ax.plot(_ac, _ar, "-", color=PAL["flow"], lw=2.1, zorder=4)
ax.plot(_ang, _or[:-1], "o", color=PAL["one"], ms=4.2, mec="white", mew=0.6, zorder=5)
ax.plot(_ang, _ar[:-1], "D", color=PAL["flow"], ms=4.2, mec="white", mew=0.6, zorder=6)
ax.set_xticks(_ang)
ax.set_xticklabels(_mods, fontsize=7.6)
ax.tick_params(axis="x", pad=1.0)
ax.set_ylim(1.0, 4.45)
ax.set_yticks([1, 2, 3, 4])
ax.set_yticklabels(["$10$", "$10^2$", "$10^3$", "$10^4$"], fontsize=7.0, color="#777")
ax.set_rlabel_position(0)
ax.grid(color="#CBD2DA", lw=0.5, alpha=0.8)
ax.spines["polar"].set_color("#B8C0C8")
_leg = [Line2D([0], [0], color=PAL["one"], lw=2, marker="o", ms=4, label="One-shot"),
        Line2D([0], [0], color=PAL["flow"], lw=2, marker="D", ms=4, label="AnchorPath")]
ax.legend(handles=_leg, loc="center", bbox_to_anchor=(0.5, -0.13), ncol=2,
          fontsize=8.4, frameon=False, columnspacing=1.3, handletextpad=0.4)
ax.set_title("WikiText-2 ppl at $\\rho{=}0.5$", fontsize=9.5, fontweight="bold", pad=9)
fig.savefig(f"{OUT}/fig_headline.pdf", bbox_inches="tight")
plt.close(fig)

# ============================================================ FIG 2 (fig_method): conceptual overview
# Schematic. (a) one-shot: a single quadratic built at the dense point, extrapolated -> gap = collapse.
# (b) AnchorPath: K re-linearizations track the true risk; errors add (1/K^2) not multiply.
fig, ax = plt.subplots(1, 2, figsize=(9.4, 3.55))
b = np.linspace(0, 1, 200)
true = 4.3 * b**2 * (0.45 + 0.55*b)          # cubic-ish true risk -> curves up, "collapse"
quad = 4.3 * 0.45 * b**2                      # the dense-point quadratic: right slope at 0, under-reads far out
for a in ax:
    despine(a); a.grid(False)
    a.set_xlim(-0.03, 1.06); a.set_ylim(-0.25, 5.0)
    a.set_xlabel(r"compression budget $b/C$")
    a.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    a.set_yticks([])
ax[0].set_ylabel("pruning risk  (KL to dense)")

# --- panel (a): one-shot ---
ax[0].plot(b, true, "-", color=PAL["true"], lw=2.4, zorder=3)
ax[0].plot(b, quad, "--", color=PAL["one"], lw=2.4, zorder=3)
ax[0].fill_between(b, quad, true, color=PAL["one"], alpha=0.12, zorder=1)
ax[0].scatter([0], [0], s=120, color=PAL["ink"], zorder=6, ec="white", lw=1.2)
ax[0].annotate("anchor $=$ expansion\npoint (dense)", xy=(0.0, 0.0), xytext=(0.10, 1.30),
               fontsize=10.0, color=PAL["ink"], ha="left", va="center",
               arrowprops=dict(arrowstyle="-|>", color=PAL["ink"], lw=1.1,
                               connectionstyle="arc3,rad=-0.25"))
ax[0].text(0.99, true[-1]+0.12, "true risk", color=PAL["true"], fontsize=10.5,
           ha="right", va="bottom", style="italic")
ax[0].text(0.99, quad[-1]-0.28, "one-shot\nquadratic", color=PAL["one"], fontsize=10.5,
           ha="right", va="top")
ax[0].annotate("extrapolation error\n$\\Rightarrow$ collapse", xy=(0.72, (true[144]+quad[144])/2),
               xytext=(0.30, 3.55), fontsize=10.5, color=PAL["one"], ha="center", va="center",
               arrowprops=dict(arrowstyle="-|>", color=PAL["one"], lw=1.2,
                               connectionstyle="arc3,rad=0.20"))
title(ax[0], "(a) One-shot: one quadratic, extrapolated", fontsize=12.0)

# --- panel (b): AnchorPath ---
ax[1].plot(b, true, "-", color=PAL["true"], lw=2.4, zorder=2, alpha=0.55)
ax[1].plot(b, true, "-", color=PAL["flow"], lw=2.8, zorder=3)   # continuation rides the true risk
anchors = [0.0, 0.25, 0.5, 0.75, 1.0]
ay = [4.3 * x**2 * (0.45 + 0.55*x) for x in anchors]
ax[1].scatter(anchors[1:], ay[1:], s=52, facecolor="white", edgecolor=PAL["flow"],
              lw=1.8, zorder=6)
ax[1].scatter([0], [0], s=120, color=PAL["ink"], zorder=7, ec="white", lw=1.2)
ax[1].annotate("fixed anchor $p_0$", xy=(0.0, 0.0), xytext=(0.09, 1.15),
               fontsize=10.0, color=PAL["ink"], ha="left", va="center",
               arrowprops=dict(arrowstyle="-|>", color=PAL["ink"], lw=1.1,
                               connectionstyle="arc3,rad=-0.25"))
ax[1].annotate("expansion point moves\n$s_1, s_2, \\ldots$ along the path", xy=(0.5, ay[2]),
               xytext=(0.06, 3.55), fontsize=10.0, color=PAL["flow"], ha="left", va="center",
               arrowprops=dict(arrowstyle="-|>", color=PAL["flow"], lw=1.1,
                               connectionstyle="arc3,rad=0.22"))
ax[1].text(0.99, true[-1]+0.12, "true risk", color=PAL["true"], fontsize=10.5,
           ha="right", va="bottom", style="italic", alpha=0.8)
ax[1].text(0.60, 0.32, r"errors add, not multiply  $(1/K^2)$", color=PAL["flow"],
           fontsize=10.0, ha="left", va="center", style="italic")
title(ax[1], "(b) AnchorPath: $K$ re-anchored steps", fontsize=12.0)
fig.tight_layout(); fig.savefig(f"{OUT}/fig_method.pdf"); plt.close(fig)

# ============================================================ FIG (mechanism): collapse + first-order drift
fig, ax = plt.subplots(1, 2, figsize=(9.4, 3.7))
seg = ["0.1$\\to$0.2", "0.2$\\to$0.3", "0.3$\\to$0.4", "0.4$\\to$0.5"]
inf_one = [L2["one"][i+1]/L2["one"][i] for i in range(4)]
inf_fl  = [L2["fl"][i+1]/L2["fl"][i] for i in range(4)]
x = np.arange(4); w = 0.38
ax[0].bar(x-w/2, inf_one, w, color=PAL["one"], label=ONE_LBL, zorder=2)
ax[0].bar(x+w/2, inf_fl, w, color=PAL["flow"], label="AnchorPath ($K{=}8$)", zorder=2)
for i, v in enumerate(inf_one):
    ax[0].text(i-w/2, v+0.35, f"{v:.1f}"+r"$\times$", ha="center", fontsize=9.0, color=PAL["one"])
for i, v in enumerate(inf_fl):
    ax[0].text(i+w/2, v+0.35, f"{v:.1f}"+r"$\times$", ha="center", fontsize=9.0, color=PAL["flow"])
ax[0].set_xticks(x); ax[0].set_xticklabels(seg, fontsize=10)
ax[0].set_ylabel(r"ppl inflation per $+0.1$ sparsity"); despine(ax[0])
ax[0].set_ylim(0, max(inf_one)*1.16)
title(ax[0], "(a) Collapse is super-exponential", fontsize=12)
ax[0].legend(loc="upper left")
steps = [1, 2, 3]
fo = {0.30:[0.044,0.069,0.105], 0.40:[0.082,0.125,0.240], 0.50:[0.136,0.187,0.419]}
shades = {0.30:PAL["flow_soft"], 0.40:PAL["k4"], 0.50:PAL["flow"]}
for r in [0.30, 0.40, 0.50]:
    ax[1].plot(steps, fo[r], "o-", color=shades[r], lw=2.2, ms=7, label=fr"$\rho={r}$",
               mec="white", mew=0.8)
ax[1].set_xticks(steps); ax[1].set_xlabel(r"Continuation step $k$")
ax[1].set_ylabel(r"first-order drift mass $\|g^{(k)}\|$"); despine(ax[1])
title(ax[1], "(b) The discarded term grows along the path", fontsize=12)
ax[1].legend(title="target sparsity", loc="upper left")
fig.tight_layout(); fig.savefig(f"{OUT}/fig_mechanism.pdf"); plt.close(fig)

# ============================================================ FIG (kstep): K-step + schedule
fig, ax = plt.subplots(1, 2, figsize=(9.6, 3.7))
ax[0].plot(R, L2["one"], "o-", color=PAL["one"], lw=2.1, ms=6.0, label="$K{=}1$ (one-shot)", mec="white", mew=0.7)
ax[0].plot(R, L2["k4"], "s-", color=PAL["k4"], lw=2.1, ms=6.0, label="$K{=}4$", mec="white", mew=0.7)
ax[0].plot(R, L2["k8"], "D-", color=PAL["flow"], lw=2.5, ms=7, label="$K{=}8$", mec="white", mew=0.8)
ax[0].set_yscale("log"); despine(ax[0]); ax[0].set_xticks(R)
ax[0].set_xlabel(r"Prune ratio $\rho$"); ax[0].set_ylabel("WikiText-2 ppl (log)")
title(ax[0], r"(a) Monotone in $K$ (the $1/K^2$ bound)", fontsize=12); ax[0].legend(loc="upper left")
ax[1].plot(R, L2["k8"], "D--", color=PAL["flow"], lw=2.0, ms=6, label="$K{=}8$, equal bands", mec="white", mew=0.8)
ax[1].plot(R, L2["fl"], "^-", color=PAL["fl"], lw=2.5, ms=7.6, label="$K{=}8$, front-loaded", mec="white", mew=0.8)
ax[1].set_yscale("log"); despine(ax[1]); ax[1].set_xticks(R)
ax[1].set_xlabel(r"Prune ratio $\rho$"); ax[1].set_ylabel("WikiText-2 ppl (log)")
title(ax[1], "(b) Front-loading helps most where the path is steep", fontsize=11.5)
ax[1].legend(loc="upper left")
gainbox(ax[1], 0.5, (L2["k8"][-1]*L2["fl"][-1])**0.5, r"$3.1\times$", PAL["fl"])
fig.tight_layout(); fig.savefig(f"{OUT}/fig_kstep.pdf"); plt.close(fig)

# ============================================================ FIG 3 (whitebox): single-column, stacked
fig, ax = plt.subplots(2, 1, figsize=(3.42, 3.55))
rr = [0.20, 0.30, 0.50]
one_attn = [1, 1, 1]; cf_attn = [47, 71, 156]
x = np.arange(3); w = 0.36
ax[0].bar(x-w/2, one_attn, w, color=PAL["one"], label="One-shot", zorder=2)
ax[0].bar(x+w/2, cf_attn, w, color=PAL["flow"], label="AnchorPath", zorder=2)
for i, v in enumerate(cf_attn):
    ax[0].text(i+w/2, v+4, str(v), ha="center", fontsize=8, color=PAL["flow"])
ax[0].set_xticks(x); ax[0].set_xticklabels([fr"$\rho={r}$" for r in rr], fontsize=8.5)
ax[0].set_ylabel("heads pruned", fontsize=9); despine(ax[0])
ax[0].set_ylim(0, max(cf_attn)*1.20); ax[0].tick_params(labelsize=8)
title(ax[0], "(a) Attention heads pruned", fontsize=9.0)
ax[0].legend(loc="upper left", fontsize=8, borderpad=0.2)
pts = {"One-shot": (19.86, 0.629, PAL["one"], "o"),
       "AnchorPath, equal": (15.65, 0.381, PAL["flow"], "D"),
       "AnchorPath, front-loaded": (14.08, 0.676, PAL["fl"], "*")}
for name, (p, bq, c, mk) in pts.items():
    ax[1].scatter(p, bq, s=180 if mk == "*" else 75, c=c, marker=mk, zorder=4,
                  edgecolor="white", linewidth=1.0, label=name)
ax[1].set_xlabel(r"WikiText-2 ppl ($\leftarrow$better)", fontsize=9)
ax[1].set_ylabel(r"BoolQ ($\uparrow$)", fontsize=9)
despine(ax[1]); ax[1].set_xlim(13.0, 21.2); ax[1].set_ylim(0.34, 0.73); ax[1].tick_params(labelsize=8)
title(ax[1], r"(b) ppl$\leftrightarrow$BoolQ front ($\rho{=}0.3$)", fontsize=9.0)
ax[1].legend(loc="lower right", fontsize=7.2, borderpad=0.2)
fig.tight_layout(h_pad=1.4); fig.savefig(f"{OUT}/fig_whitebox.pdf"); plt.close(fig)

# ============================================================ FIG (baselines): lower-envelope, LLaMA-3.1-8B
fig, ax = plt.subplots(figsize=(4.2, 3.05))
R31b = [0.20, 0.30, 0.40, 0.50]
base = {"Wanda-sp":[29.35,101.4,1015.15,17610.82], "FLAP":[37.62,1030.43,49940.23,376016.93],
        "LLM-Pruner (no FT)":[14.51,30.0,103.35,718.16], "Magnitude":[36.69,2184.33,27101.43,76312.56],
        "Random":[22.67,56.62,4168.39,60359.60]}
for n, ys in base.items():
    ax.plot(R31b, ys, "^--", color=BASE_COLORS[n], lw=1.3, ms=5.0, alpha=0.85, label=n,
            mec="white", mew=0.5)
ax.plot(R31b, L31["one"], "o-", color=PAL["one"], lw=2.0, ms=6.5, label=ONE_LBL, mec="white", mew=0.8)
ax.plot(R31b, L31["k8"], "D-", color=PAL["flow"], lw=2.8, ms=7.6, label="AnchorPath ($K{=}8$)",
        zorder=5, mec="white", mew=0.9)
ax.set_yscale("log"); despine(ax); ax.set_xticks(R31b)
ax.set_xlabel(r"Prune ratio $\rho$"); ax.set_ylabel("WikiText-2 perplexity (log)")
title(ax, "AnchorPath is the lower envelope at every sparsity", fontsize=11.5)
ax.legend(loc="upper left", fontsize=8.6, ncol=1)
fig.savefig(f"{OUT}/fig_baselines.pdf"); plt.close(fig)

# ============================================================ FIG (geometry): budget homotopy, LLaMA-2-7B
fig, ax = plt.subplots(figsize=(4.35, 3.15))
rho = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
g_one = [4.9, 6.38, 9.27, 19.86, 92.64, 1496.89]
g_k8  = [4.9, 5.92, 8.63, 15.65, 33.59, 388.69]
ax.fill_between(rho, g_k8, g_one, color=PAL["flow"], alpha=0.10, zorder=1)
ax.plot(rho, g_one, "o-", color=PAL["one"], lw=2.3, ms=6.5, label="One-shot (single quadratic)",
        zorder=3, mec="white", mew=0.8)
ax.plot(rho, g_k8, "D-", color=PAL["flow"], lw=2.6, ms=7.0, label=r"AnchorPath ($K{=}8$ anchors)",
        zorder=4, mec="white", mew=0.8)
ax.set_yscale("log")
ax.scatter([0], [4.9], s=150, c=PAL["ink"], marker="*", edgecolor="white", lw=1.2, zorder=6)
for r, y in zip(rho[1:], g_k8[1:]):
    ax.scatter([r], [y], s=48, facecolor="white", edgecolor=PAL["flow"], lw=1.6, zorder=7)
ax.annotate("dense anchor", xy=(0, 4.9), xytext=(0.045, 4.0), fontsize=9.5, color=PAL["ink"],
            va="center", arrowprops=dict(arrowstyle="-|>", color=PAL["ink"], lw=1.0,
                                         connectionstyle="arc3,rad=-0.2"))
ax.annotate("re-linearize at\nthe current budget", xy=(0.3, 15.65), xytext=(0.055, 150),
            fontsize=9.2, color=PAL["flow"], ha="left", va="center",
            arrowprops=dict(arrowstyle="-|>", color=PAL["flow"], lw=1.1,
                            connectionstyle="arc3,rad=0.2"))
ax.annotate("extrapolated far past\nits trust region", xy=(0.4, 92.64), xytext=(0.20, 470),
            fontsize=9.2, color=PAL["one"], ha="center", va="center",
            arrowprops=dict(arrowstyle="-|>", color=PAL["one"], lw=1.1,
                            connectionstyle="arc3,rad=-0.2"))
gainbox(ax, 0.5, (388.69*1496.89)**0.5, r"$3.9\times$", PAL["flow"])
despine(ax); ax.set_xticks(rho)
ax.set_xlabel(r"Prune ratio $\rho$"); ax.set_ylabel("WikiText-2 perplexity (log)")
ax.set_ylim(3.4, 4200)
title(ax, "The budget path stays inside the trust region", fontsize=11.0)
ax.legend(loc="lower right", fontsize=9.0)
fig.savefig(f"{OUT}/fig_geometry.pdf"); plt.close(fig)

# ============================================================ FIG (curvature): node -> edge structure
_Hpath = os.path.join(os.path.dirname(__file__), "..", "..",
                      "outputs/experiments/llama-2-7b/flow_prepare/matrices/H.npy")
if os.path.isfile(_Hpath):
    H = np.load(_Hpath).astype(np.float64)
    dd = np.sqrt(np.clip(np.diag(H), 1e-12, None))
    C = np.abs(H / np.outer(dd, dd))
    offE = (np.abs(H - np.diag(np.diag(H)))**2).sum(); totE = (H**2).sum()
    frac = float(offE / totE)
    fig, ax = plt.subplots(1, 2, figsize=(9.4, 3.75), gridspec_kw={"width_ratios":[1.12, 1]})
    sub = C[:80, :80]
    im = ax[0].imshow(sub, cmap="magma", vmin=0, vmax=float(np.percentile(sub, 99)))
    title(ax[0], "(a) Fisher curvature couples units", fontsize=11.5)
    ax[0].set_xlabel("unit index"); ax[0].set_ylabel("unit index")
    ax[0].grid(False)
    cb = fig.colorbar(im, ax=ax[0], fraction=0.046, pad=0.03)
    cb.set_label("normalized coupling", fontsize=9.5)
    cb.ax.tick_params(labelsize=9)
    ax[1].barh([1], [1-frac], color=PAL["grey"], zorder=2)
    ax[1].barh([1], [frac], left=[1-frac], color=PAL["flow"], zorder=2)
    ax[1].text((1-frac)/2, 1, f"{100*(1-frac):.0f}%\ndiagonal", ha="center", va="center",
               color="white", fontweight="bold", fontsize=11)
    ax[1].text(1-frac/2, 1, f"{100*frac:.0f}%\noff-diag.", ha="center", va="center",
               color="white", fontweight="bold", fontsize=11)
    ax[1].set_xlim(0, 1); ax[1].set_ylim(0.35, 1.75); ax[1].set_yticks([])
    ax[1].set_xlabel(r"share of curvature energy $\|H\|_F^2$"); despine(ax[1]); ax[1].grid(False)
    ax[1].annotate("off-diagonal couplings\ntracked by the refresh", xy=(1-frac/2, 0.62),
                   xytext=(0.46, 0.46), fontsize=9.0, color=PAL["flow"], ha="center", va="center",
                   arrowprops=dict(arrowstyle="-|>", color=PAL["flow"], lw=1.05,
                                   connectionstyle="arc3,rad=0.15"))
    title(ax[1], "(b) A quarter of the curvature is off-diagonal", fontsize=11.5)
    fig.tight_layout(); fig.savefig(f"{OUT}/fig_curvature.pdf"); plt.close(fig)

print("wrote:", sorted(os.listdir(OUT)))
