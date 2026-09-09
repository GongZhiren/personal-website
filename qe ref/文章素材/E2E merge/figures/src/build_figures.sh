#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python src/make_figures.py
python src/make_dataeff_fig.py
python src/make_figures_rebuttal.py
python src/make_budget_frontiers.py
src/outline_pdfs.sh fig_main.pdf fig_pertask.pdf fig_lr.pdf fig_scaling.pdf \
  fig_compound.pdf fig_dataeff.pdf fig_blockwise.pdf fig_budget_frontiers.pdf
