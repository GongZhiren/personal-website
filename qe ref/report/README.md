# PhD QE Report — Final Release

## Deliverables
- `QE_Report_Zhiren_Gong.pdf` — official QE report (A4, 12pt, double-spaced, 1-inch margins), 65 pages.
- `QE_Executive_Summary.pdf` — standalone two-page executive summary.
- `QE_Report_Zhiren_Gong.tex` — full report source.
- `QE_Executive_Summary.tex` — executive-summary source.
- `references.bib` — bibliography.
- `figures/` — project-source figures/tables used in the report, plus the NTU logo and thesis-level overview graphics.
- `Source_Mapping.md` — project-to-story/figure mapping for future editing.

## Compile
```bash
pdflatex QE_Report_Zhiren_Gong.tex
bibtex8 QE_Report_Zhiren_Gong
pdflatex QE_Report_Zhiren_Gong.tex
pdflatex QE_Report_Zhiren_Gong.tex
```

Executive summary:
```bash
pdflatex QE_Executive_Summary.tex
```

## Structure
The report is organized around one deployment problem: how to make increasingly capable foundation models efficient, scalable, and reliable under heterogeneous deployment and reasoning conditions.

- Background observations: `XDomainBench` (external heterogeneous demand) and `CoAx` (conditional/coupled internal mechanisms).
- Part I — Adaptive Model Execution: `SubspacePath Pruner -> CoCurve -> AnchorPath`.
- Part II — Adaptive Reasoning: `SoT -> LoTR`.
- Synthesis: adaptive computation as a conditional and relational allocation problem.

The technical sections use project-source method figures, equations, tables, ablations, and headline results so that each core method is understandable within the QE report without reproducing an entire paper.


## Final QA
- Official format: A4, 12pt, double-spaced, 1-inch margins.
- Report: 65 pages; Executive Summary: 2 pages.
- Fresh LaTeX/BibTeX compilation completed with no undefined references/citations or overfull boxes.
- PDF preflight confirms both files are openable, A4, unencrypted, and text-based.
- Tables/figures use project-source material; thesis-level overview graphics are the only custom synthesis visuals.
