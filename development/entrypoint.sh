#!/bin/sh

# Installing git
echo "Installing dependencies"
apk add --no-cache git git-fast-import

# Making /data and /site safe for git
git config --global --add safe.directory /data
git config --global --add safe.directory /site

echo "Upgrading pip"
python -m pip install --upgrade pip

# install pip requirements (the doc group includes the Schema Explorer
# build-time dependency: pyavd-utils-gen)
echo "Installing Documentation python requirements"
python -m pip install --group doc --upgrade

# mkdocs_hook.py rebuilds the Schema Explorer directly into MkDocs' site_dir.

# Start mkdocs
echo "Starting mkdocs"
mkdocs serve --no-livereload --dev-addr=127.0.0.1:8000 -f mkdocs.yml
