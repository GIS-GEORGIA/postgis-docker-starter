FROM postgis/postgis:15-3.3

# Install Python and GDAL for spatial data imports
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip gdal-bin \
    && pip3 install --no-cache-dir psycopg2-binary \
    && rm -rf /var/lib/apt/lists/*

# Copy startup helpers
COPY startup.sh /docker-entrypoint-initdb.d/010-startup.sh
COPY setup-geojson.py /usr/local/bin/setup-geojson.py
RUN chmod +x /docker-entrypoint-initdb.d/010-startup.sh \
    && chmod +x /usr/local/bin/setup-geojson.py
