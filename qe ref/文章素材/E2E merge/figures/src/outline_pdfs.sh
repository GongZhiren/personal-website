#!/usr/bin/env bash
set -euo pipefail
for pdf in "$@"; do
  tmp="${pdf%.pdf}.outlined.pdf"
  gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite \
     -dCompatibilityLevel=1.7 -dNoOutputFonts \
     -sOutputFile="$tmp" "$pdf"
  mv "$tmp" "$pdf"
done
