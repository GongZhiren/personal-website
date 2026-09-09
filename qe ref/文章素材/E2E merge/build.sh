#!/usr/bin/env bash
set -euo pipefail

run_bibtex() {
  local stem="$1"
  if command -v bibtex >/dev/null 2>&1 && bibtex "$stem"; then
    return 0
  fi
  if command -v bibtex.original >/dev/null 2>&1; then
    bibtex.original "$stem"
    return 0
  fi
  echo "bibtex executable not found" >&2
  exit 1
}

pdflatex -interaction=nonstopmode -halt-on-error main.tex
run_bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex

# supplement.tex is self-contained (no cross-document references).
pdflatex -interaction=nonstopmode -halt-on-error supplement.tex
run_bibtex supplement
pdflatex -interaction=nonstopmode -halt-on-error supplement.tex
pdflatex -interaction=nonstopmode -halt-on-error supplement.tex

pdflatex -interaction=nonstopmode -halt-on-error full.tex
run_bibtex full
pdflatex -interaction=nonstopmode -halt-on-error full.tex
pdflatex -interaction=nonstopmode -halt-on-error full.tex

pdflatex -interaction=nonstopmode -halt-on-error reproducibility_checklist_draft.tex
