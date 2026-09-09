#!/usr/bin/env bash
# Build all three AAAI-2027 submission documents (each is independent and self-contained).
#   main.tex                      -> the 7-page main paper (references on pp. 8-9)
#   supplement.tex               -> the Technical Supplement (self-contained appendix)
#   ReproducibilityChecklist.tex -> the answered AAAI reproducibility checklist
#
# Figures are regenerated from data/ by make_figs.py (matplotlib only).
set -euo pipefail
cd "$(dirname "$0")"

if command -v python3 >/dev/null 2>&1; then
  python3 make_figs.py || echo "make_figs.py skipped (matplotlib not installed); using existing figs/"
fi

build () {
  local doc="$1"
  pdflatex -interaction=nonstopmode "$doc.tex" >/dev/null
  bibtex "$doc" >/dev/null 2>&1 || true
  pdflatex -interaction=nonstopmode "$doc.tex" >/dev/null
  pdflatex -interaction=nonstopmode "$doc.tex" >/dev/null
  echo "  built $doc.pdf ($(pdfinfo "$doc.pdf" | awk '/Pages/{print $2}') pages)"
}

echo "Building submission documents:"
build main
build supplement
pdflatex -interaction=nonstopmode ReproducibilityChecklist.tex >/dev/null
echo "  built ReproducibilityChecklist.pdf"
echo "Done."
