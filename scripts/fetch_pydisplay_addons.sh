#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Download display_driver.py from PyDevices/lv_bindings (LVGL glue for pydisplay).
#
# Usage:
#   ./scripts/fetch_pydisplay_addons.sh DEST_DIR
#
# Environment:
#   LV_BINDINGS_GITHUB_REPO   GitHub repo (default: PyDevices/lv_bindings)
#   LV_BINDINGS_GITHUB_REF    Branch, tag, or commit (default: main)
set -euo pipefail

DEST="${1:-}"
if [[ -z "$DEST" ]]; then
  echo "Usage: $0 DEST_DIR" >&2
  exit 1
fi

REPO="${LV_BINDINGS_GITHUB_REPO:-PyDevices/lv_bindings}"
REF="${LV_BINDINGS_GITHUB_REF:-main}"
BASE="https://raw.githubusercontent.com/${REPO}/${REF}/python"

mkdir -p "$DEST"

fetch_one() {
  local name=$1
  local url="${BASE}/${name}"
  local dest="${DEST}/${name}"
  echo "==> Fetching ${name} (${REPO}@${REF})"
  curl -fSL "$url" -o "$dest"
  [[ -s "$dest" ]] || {
    echo "Download failed or empty: $url" >&2
    exit 1
  }
}

fetch_one display_driver.py
