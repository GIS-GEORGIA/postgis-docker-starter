# postgis-dev-template

<!-- CI Badge -->
[![CI](https://github.com/<your-username>/postgis-dev-template/actions/workflows/ci.yml/badge.svg)](https://github.com/<your-username>/postgis-dev-template/actions/workflows/ci.yml)


Minimal Docker + PostGIS + init scripts + Dev Container.
Ready-to-use template for local development or GitHub Codespaces.

Includes:
- `.env` variables for easy configuration
- Docker Compose with PostGIS + Adminer (web UI)
- Optional pgAdmin4 service (commented, enable if needed)
- GDAL installed in DB container for spatial imports
- Auto-init SQL + GeoJSON seeding
- VS Code Dev Container + settings

## Quick start
1. Clone this repository
   ```bash
   git clone https://github.com/<your-username>/postgis-dev-template.git
   cd postgis-dev-template
   ```
2. Adjust `.env` if needed.
3. (Optional) Drop your `*.geojson` files into `seed/`.
4. Launch services:
   ```bash
   docker compose up -d --build
   ```
5. Connect to DB:
   ```
   postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@localhost:${PG_PORT}/$POSTGRES_DB
   ```
6. Open Adminer:
   - URL: `http://localhost:${ADMINER_PORT}`
   - Server: `db`
   - User/Password: from `.env`
   - Database: from `.env`

## Useful commands
- Logs:
  ```bash
  docker compose logs -f db
  ```
- Enter container psql:
  ```bash
  docker compose exec -it db psql -U ${POSTGRES_USER} -d ${POSTGRES_DB}
  ```
- Reset database (WARNING: removes data volume):
  ```bash
  docker compose down -v
  docker compose up -d --build
  ```

## Notes
- To enable pgAdmin4, uncomment the `pgadmin` service in `docker-compose.yml` and configure `.env`.
- GDAL (`ogr2ogr`) is available inside the db container.
- Works locally and in GitHub Codespaces (via `.devcontainer`).

## CI
This repository includes a basic GitHub Actions workflow (`.github/workflows/ci.yml`) that:
- Builds the Docker image on every push/PR to `main`
- Runs `docker compose config` to validate syntax

## Continuous Integration (GitHub Actions)
This repository ships with a minimal CI workflow (`.github/workflows/ci.yml`) that:
- Builds the Docker image
- Starts the database via `docker compose up -d db`
- Waits until PostgreSQL is ready
- Runs smoke tests to verify PostGIS is installed and the training schema/table exist
- Tears everything down

The badge above will reflect the latest build status once you push to GitHub.
