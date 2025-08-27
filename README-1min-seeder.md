# 60-second seeder loop

This compose includes a **seeder** service that runs every 60 seconds:
- waits for the DB to be ready
- runs `/usr/local/bin/setup-geojson.py`
- sleeps 60 seconds and repeats

To make it idempotent, we pass `SEED_MODE=replace`, which performs `TRUNCATE training.places` before each import.
If you prefer appending on every cycle, set `SEED_MODE=append` (beware duplicates).

Usage:
```bash
docker compose up -d --build
docker compose logs -f seeder
```

Change the cadence by editing `sleep 60` in the seeder command.
