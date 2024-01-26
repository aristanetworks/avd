# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import lru_cache
from pickle import load

from yaml import safe_load

from .constants import PICKLED_SCHEMAS, SCHEMA_PATHS


@lru_cache
def create_store(load_from_yaml=False) -> dict[str, dict]:
    store = {}

    # Load from YAML if set. This is used by the tool that creates the pickle.
    if load_from_yaml:
        for id, schema_file in SCHEMA_PATHS.items():
            with open(schema_file, "r", encoding="UTF-8") as file:
                schema_file_data = safe_load(file.read())
                store[id] = schema_file_data

    # Load from Pickle
    else:
        for id, schema_file in PICKLED_SCHEMAS.items():
            with open(schema_file, "rb") as file:
                store[id] = load(file)

    return store
