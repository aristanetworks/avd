#!/usr/bin/env python3
# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.store import create_store

"""
Script that outputs the public schema store.

Output should be compressed and published as artifact for the release on github.

`python-avd/scripts/schema_release_artifact.py | gzip > schemas.json.gz`
"""
if __name__ == "__main__":
    store = create_store(load_from_yaml=True)
    # We only include the external facing schemas in the artifact.
    store.pop("avd_meta_schema")
    store.pop("eos_designs_facts_protocol")
    print(json.dumps(store))
