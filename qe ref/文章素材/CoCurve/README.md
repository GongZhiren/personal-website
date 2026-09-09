# CoCurve — ICLR 2027 submission (canonical source)

**This directory is the single source of truth.** All further edits happen here.
`paper/edge_taylor/` and `paper/new/` are the frozen arXiv version (verified
byte-identical to each other on 2026-08-03) and are kept for reference only —
do not edit them.

## Build

```bash
./build.sh          # pdflatex -> bibtex -> pdflatex x2, reports pages + undefined refs
```

`TEXINPUTS=./texstub:` is required; `texstub/` holds local copies of packages
(`algorithm`, `algorithmic`, `cleveref`, `eso-pic`, …) missing from the host TeX tree.
`build.sh` sets it for you.

## What changed from the arXiv version

| | arXiv version | this version |
|---|---|---|
| style | `iclr2025_conference` + `\iclrfinalcopy` | **`iclr2027_conference`, anonymous** |
| authors | full NTU author block | `Anonymous authors / Paper under double-blind review` |
| resource links | Code / Project Page / Tutorial icon row | **removed** (de-anonymising) |
| page header | ICLR review ruler suppressed | ruler kept (required for review) |
| abstract | "the extra damage of removing two units together" | softened to "the surrogate mixed curvature governing the predicted marginal risk" (the stronger claim is not what we validate) |
| abstract | "a single calibration statistic predicts … when the edges should be trusted or damped" | "the interaction strength is set by a label-free calibration probe rather than a tuned hyper-parameter" (pending the §1.1 protocol) |

## Anonymity checklist (ICLR 2027 desk-rejects violations)

- [x] `\iclrfinalcopy` commented out
- [x] no author names / affiliations / emails in `main.tex`
- [x] no GitHub / project-page / tutorial URLs in the main text
- [ ] **grep the appendix and figures** for `GongZhiren`, `ntu.edu.sg`, `CoCurve-website`,
      and any absolute `/scratch/...` paths before submitting
- [ ] cite our own arXiv preprint in the third person if we cite it at all
- [ ] supplementary material (code zip) must also be anonymised

## Hard constraint: 9 pages of main text

ICLR 2027 allows **9 pages at submission** (10 during discussion / camera-ready).
References, appendix, and the ethics / reproducibility statements do **not** count.

**Current state (2026-08-31 build): 18 pages of main text (p1–p18;
references start p19). We must remove 9 pages — 50% of the body.**

The build now detects the bibliography page directly and reports the main-text
count; the previous check printed only the total PDF length and allowed this
status line to drift out of date.

ICLR 2027 also requires an explicit AI use statement.  The canonical draft does
not yet contain one; its wording must reflect the authors' actual use and should
be added before submission rather than inferred from repository history.

Planned reductions (see `PLAN_ICLR2027.md` §4):
1. Main results table → 6 columns (Wiki PPL / commonsense avg / MMLU / EvalPlus code
   avg / realised parameter reduction / speedup); the full 14-task tables move to the
   appendix.
2. Figure 1 → 3 panels (node ranking fails → Gram estimator → shared-budget joint
   selection); physical slicing and compensation drop out of the teaser.
3. Delete the defensive prose ("We do not read this as evidence against…", "We take
   no position on which metric is canonical", "a transparent operating-point choice").
4. §2.5 compensation → appendix (it is an orthogonal extension, not the core method).
5. Collapse the §3.3–§3.4 ratio-sweep and ablation prose; keep the figures.
6. Old Proposition 1 is being deleted anyway (its proof is wrong — `PLAN` §0.3).

A page-count check runs in `build.sh` on every build.
