-- Enable core spatial extensions
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Training schema and demo table
CREATE SCHEMA IF NOT EXISTS training;
CREATE TABLE IF NOT EXISTS training.places (
  id SERIAL PRIMARY KEY,
  name TEXT,
  props JSONB,
  geom GEOMETRY(Geometry, 4326)
);
CREATE INDEX IF NOT EXISTS idx_places_geom ON training.places USING GIST (geom);
