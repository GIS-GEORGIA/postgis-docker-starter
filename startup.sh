#!/usr/bin/env bash
set -euo pipefail

echo "[startup] Running optional GeoJSON seeding (if any)..."
if [ -x /usr/local/bin/setup-geojson.py ]; then
  if ! /usr/local/bin/setup-geojson.py; then
    echo "[startup] GeoJSON load failed or skipped (non-fatal)."
  fi
fi
echo "[startup] Done."
