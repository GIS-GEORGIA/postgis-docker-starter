#!/usr/bin/env python3
import json, os, glob, psycopg2, sys

DB = os.environ.get("POSTGRES_DB", "geo_db")
USER = os.environ.get("POSTGRES_USER", "postgres")
PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
HOST = os.environ.get("POSTGRES_HOST", "localhost")
PORT = int(os.environ.get("POSTGRES_PORT", 5432))

SEED_DIR = "/seed"
TABLE = "training.places"
SEED_MODE = os.environ.get("SEED_MODE", "append").lower()  # 'append' (default) or 'replace'

def main():
    if not os.path.isdir(SEED_DIR):
        print("[seed] No /seed directory mounted — skipping.")
        return 0
    files = sorted(glob.glob(os.path.join(SEED_DIR, "*.geojson")))
    if not files:
        print("[seed] No *.geojson files — skipping.")
        return 0

    conn = psycopg2.connect(dbname=DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
    conn.autocommit = True
    cur = conn.cursor()

    if SEED_MODE == "replace":
        print(f"[seed] SEED_MODE=replace -> TRUNCATE {TABLE}")
        cur.execute(f"TRUNCATE {TABLE};")

    total = 0
    print(f"[seed] Loading {len(files)} GeoJSON file(s) into {TABLE}...")
    for path in files:
        print(f"[seed] -> {os.path.basename(path)}")
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"[seed] !! Failed to read {path}: {e}")
            continue

        features = data.get("features", [])
        for feat in features:
            props = (feat.get("properties") or {})
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

            total += 1

    cur.close(); conn.close()
    print(f"[seed] Done. Inserted {total} feature(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
