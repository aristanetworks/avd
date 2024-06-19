# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import lru_cache
from pickle import load

from .constants import PICKLED_SCHEMAS


@lru_cache
def create_store(load_from_yaml=False):
    if load_from_yaml:
        raise NotImplementedError("'load_from_yaml' not supported for create_store under PyAVD")
    store = {}
    for id, schema_file in PICKLED_SCHEMAS.items():
        with open(schema_file, "rb") as file:
            store[id] = load(file)

    return store
