# PostGIS Codespaces Template

A Codespaces-friendly PostGIS starter modeled after the LinkedIn Learning course repo structure.

## Use in GitHub Codespaces
1. Push this repository to GitHub.
2. Click **Code → Codespaces → Create codespace on main**.
3. Codespaces will start `db` and `adminer` services automatically.
4. Open **Ports** tab to access Adminer at forwarded port (default 8080).

## Local Quick Start
```bash
docker compose up -d --build
```
Connect: `postgres://postgres:postgres@localhost:5432/geo_db`  
Adminer: `http://localhost:8080` (Server: `db`, user/pass: from `.env`).

## Seeding GeoJSON
Drop `*.geojson` files into `seed/`. First start will auto-import into `training.places`.

## Reset
```bash
docker compose down -v
docker compose up -d --build
```

## License
MIT (see LICENSE)
