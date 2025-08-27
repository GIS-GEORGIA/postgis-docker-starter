-- Enable spatial extensions
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Training schema
CREATE SCHEMA IF NOT EXISTS training;

-- Example table
CREATE TABLE IF NOT EXISTS training.places (
  id SERIAL PRIMARY KEY,
  name TEXT,
  props JSONB,
  geom GEOMETRY(Geometry, 4326)
);

-- Spatial index
CREATE INDEX IF NOT EXISTS idx_places_geom
  ON training.places USING GIST (geom);
