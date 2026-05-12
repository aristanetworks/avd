#!/bin/sh

# Installing git
echo "Installing dependencies"
apk add --no-cache git git-fast-import

# Making /data and /site safe for git
git config --global --add safe.directory /data
git config --global --add safe.directory /site

# install pip requirements (the doc group includes the Schema Explorer
# build-time deps: pyyaml, referencing, deepmerge, pydantic, jsonschema-rs)
echo "Installing Documentation python requirements"
pip install --group doc --upgrade

# Build the Schema Explorer (static assets + per-release SQLite) into
# tools/schema-explorer/build/. Source lives at tools/schema-explorer/.
# mkdocs_hook.py copies the built tree into site/schema-explorer/ on each
# `mkdocs build`. Skipped when the SQLite is already present and newer
# than the eos_designs YAML (rough mtime check) — keeps container restarts
# fast during iteration.
SCHEMA_OUT=/data/tools/schema-explorer/build/data/devel/schema.sqlite
SCHEMA_SRC=/data/python-avd/pyavd/_eos_designs/schema/eos_designs.schema.yml
if [ ! -f "$SCHEMA_OUT" ] || [ "$SCHEMA_SRC" -nt "$SCHEMA_OUT" ]; then
    echo "Building Schema Explorer"
    python /data/tools/schema-explorer/generate.py \
        --avd-root /data --release devel --site-dir /data/tools/schema-explorer/build
else
    echo "Schema Explorer is up to date — skipping rebuild"
fi

# Start mkdocs
echo "Starting mkdocs"
mkdocs serve --no-livereload --dev-addr=127.0.0.1:8000 -f mkdocs.yml
