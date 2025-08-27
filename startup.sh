#!/usr/bin/env bash
set -euo pipefail
echo "[startup] Optional GeoJSON seeding..."
if [ -x /usr/local/bin/setup-geojson.py ]; then
  if ! /usr/local/bin/setup-geojson.py; then
    echo "[startup] GeoJSON seed skipped or failed (non-fatal)."
  fi
fi
echo "[startup] Done."
