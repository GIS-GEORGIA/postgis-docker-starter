#!/usr/bin/env python3
import json, os, glob, psycopg2

DB = os.environ.get("POSTGRES_DB", "geo_db")
USER = os.environ.get("POSTGRES_USER", "postgres")
PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
HOST = os.environ.get("POSTGRES_HOST", "localhost")
PORT = int(os.environ.get("POSTGRES_PORT", 5432))

SEED_DIR = "/seed"
TABLE = "training.places"

if not os.path.isdir(SEED_DIR):
    print("[seed] No /seed directory mounted — skipping.")
    raise SystemExit(0)
files = sorted(glob.glob(os.path.join(SEED_DIR, "*.geojson")))
if not files:
    print("[seed] No *.geojson files — skipping.")
    raise SystemExit(0)

conn = psycopg2.connect(dbname=DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
conn.autocommit = True
cur = conn.cursor()

print(f"[seed] Loading {len(files)} GeoJSON file(s) into {TABLE}...")
for path in files:
    print(f"[seed] -> {os.path.basename(path)}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for feat in data.get("features", []):
        props = feat.get("properties", {}) or {}
        geom = feat.get("geometry")
        if not geom:
            continue
        cur.execute(
            f"""
INSERT INTO {TABLE} (name, props, geom)
VALUES (
  %(name)s,
  %(props)s::jsonb,
  ST_SetSRID(ST_GeomFromGeoJSON(%(gjson)s), 4326)
)
""",
            {
                "name": props.get("name") or props.get("Name") or None,
                "props": json.dumps(props),
                "gjson": json.dumps(geom),
            },
        )
cur.close(); conn.close()
print("[seed] Done.")
