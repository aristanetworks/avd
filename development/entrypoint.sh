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

# Build the Schema Explorer (static assets + SQLite) into
# tools/schema-explorer/build/. Source lives at tools/schema-explorer/.
# mkdocs_hook.py copies the built tree into site/_assets/schema-explorer/ on each
# `mkdocs build`. Skipped when the SQLite is already present and newer than the
# generator, classifier, static assets, and source schema YAMLs. Keeps container
# restarts fast during iteration without serving stale generated data.
SCHEMA_OUT=/data/tools/schema-explorer/build/data/schema.sqlite
SCHEMA_INPUTS="
/data/python-avd/pyavd/_eos_designs/schema/eos_designs.schema.yml
/data/python-avd/pyavd/_eos_cli_config_gen/schema/eos_cli_config_gen.schema.yml
/data/tools/schema-explorer/generate.py
/data/tools/schema-explorer/static/index.html
/data/tools/schema-explorer/static/css/style.css
/data/tools/schema-explorer/static/js/app.js
"
SCHEMA_REBUILD=false
if [ ! -f "$SCHEMA_OUT" ]; then
    SCHEMA_REBUILD=true
else
    for SCHEMA_SRC in $SCHEMA_INPUTS; do
        if [ ! -f "$SCHEMA_SRC" ] || [ "$SCHEMA_SRC" -nt "$SCHEMA_OUT" ]; then
            SCHEMA_REBUILD=true
            break
        fi
    done
fi
if [ "$SCHEMA_REBUILD" = true ]; then
    echo "Building Schema Explorer"
    python /data/tools/schema-explorer/generate.py \
        --avd-root /data --site-dir /data/tools/schema-explorer/build
else
    echo "Schema Explorer is up to date — skipping rebuild"
fi

# Start mkdocs
echo "Starting mkdocs"
mkdocs serve --no-livereload --dev-addr=127.0.0.1:8000 -f mkdocs.yml
