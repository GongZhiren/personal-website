# AAAI-26 submission package

This package uses the unmodified `aaai2026.sty` and `aaai2026.bst` files from the supplied official AAAI-26 Author Kit.

## Files to compile

- `main.tex` — anonymous submission paper. It contains seven pages of technical content; references begin on page 8. This is the PDF intended for the main-paper upload.
- `supplement.tex` — standalone technical supplement. It is self-contained and compiles standalone with its own bibliography.
- `full.tex` — combined internal/full version containing the main paper, references, and appendices. Do not upload this file as the limited-page main paper.
- `reproducibility_checklist_draft.tex` — a draft of the official AAAI-26 checklist. Authors must verify every response before submission.

## Build

Run:

```bash
./build.sh
```

The script creates `main.pdf`, `supplement.pdf`, `full.pdf`, and `reproducibility_checklist_draft.pdf`.

## Empirical-data policy

No new training or evaluation result was introduced in this revision. `DATA_PROVENANCE.md` records the source of every numerical value used in the paper and identifies arithmetic summaries derived from existing measurements.

## Submission checks

Before upload, verify the anonymous code/data supplement separately for author names, repository usernames, machine paths, and institution identifiers. The current paper PDFs use only anonymous metadata. Color appears only inside figures, and the included figure PDFs contain no Type 3 fonts.
