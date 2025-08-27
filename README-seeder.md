# Seeder service (always-on import)

This compose file adds a **seeder** service that:
- waits for the `db` to accept connections
- runs `/usr/local/bin/setup-geojson.py` on every `docker compose up`
- imports any `seed/*.geojson` into `training.places`

Usage:
```bash
docker compose down -v   # optional reset
docker compose up -d --build
docker compose logs -f seeder
```

If you don't want it to run each time, remove the `seeder` service block or set `restart: "no"` (default).
