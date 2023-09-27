#!/usr/bin/env python3
# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pickle import HIGHEST_PROTOCOL, dump
from sys import path

from yaml import safe_load

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, ".")

from pyavd.vendor.schema.default_schemas import DEFAULT_PICKLED_SCHEMAS, DEFAULT_SCHEMAS

for schema, schema_file in DEFAULT_SCHEMAS.items():
    print(f"Pickling schema {schema}: {schema_file}")
    pickle_file = DEFAULT_PICKLED_SCHEMAS[schema]
    with open(schema_file, "r", encoding="UTF-8") as file:
        schema_file_data = safe_load(file.read())
    with open(pickle_file, "wb") as file:
        dump(schema_file_data, file, HIGHEST_PROTOCOL)
