#!/usr/bin/env bash
# Canonical build for the ICLR 2027 submission.
# texstub/ carries local copies of packages missing from the host TeX tree.
set -euo pipefail
cd "$(dirname "$0")"
export TEXINPUTS=./texstub:
pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null || {
  grep -E "^!|l\.[0-9]+" main.log | head -20; exit 1; }
bibtex main >/dev/null 2>&1 || true
pdflatex -interaction=nonstopmode main.tex >/dev/null
pdflatex -interaction=nonstopmode main.tex >/dev/null

pages=$(pdfinfo main.pdf | awk '/^Pages/{print $2}')
undef=$(grep -c "undefined" main.log || true)
# Locate the first page containing the bibliography heading.  Counting text
# lines cannot recover a PDF page number, which made this check silently report
# only the total page count while README drifted from 12 to 18 body pages.
refs_page=""
for ((page=1; page<=pages; page++)); do
  # Do not use grep -q here: with pipefail it exits before pdftotext finishes,
  # making a successful match look like a SIGPIPE failure from pdftotext.
  if pdftotext -f "$page" -l "$page" -layout main.pdf - 2>/dev/null \
      | grep -Ei '^[[:space:]]*R[[:space:]]*E[[:space:]]*F[[:space:]]*E[[:space:]]*R[[:space:]]*E[[:space:]]*N[[:space:]]*C[[:space:]]*E[[:space:]]*S[[:space:]]*$' >/dev/null; then
    refs_page=$page
    break
  fi
done
if [[ -n "$refs_page" ]]; then
  main_pages=$((refs_page - 1))
else
  main_pages="unknown"
fi

ai_statement=missing
if grep -Eiq '\\(subsection|section)\*?\{AI use statement\}' main.tex chapters/*.tex; then
  ai_statement=present
fi

echo "pages=$pages  main-pages=$main_pages  references-start=$refs_page  undefined-refs=$undef  ai-use-statement=$ai_statement"
echo "ICLR 2027 limit: 9 pages of MAIN TEXT at submission (references, appendix,"
echo "ethics and reproducibility statements do not count)."
if [[ "$main_pages" != "unknown" && "$main_pages" -gt 9 ]]; then
  echo "WARNING: main text exceeds the submission limit by $((main_pages - 9)) page(s)."
fi
if [[ "$ai_statement" == "missing" ]]; then
  echo "WARNING: ICLR 2027 requires an AI use statement in the paper."
fi
