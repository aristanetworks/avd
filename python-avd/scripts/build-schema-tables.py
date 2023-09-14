#!/usr/bin/env python3
# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[1].joinpath("pyavd")))

from schema.constants import SCHEMA_PATHS, STORE
from schema.generate_docs.mdtabsgen import get_md_tabs
from schema.generate_docs.utils import list_tables
from schema.metaschema.meta_schema_model import AristaAvdSchema

for schema_name, schema_path in SCHEMA_PATHS.items():
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    schema = AristaAvdSchema(**STORE[schema_name])
    table_names = sorted(list_tables(schema))
    output_dir = schema_path.parents[1].joinpath("docs/tables")
    for table_name in table_names:
        print(f"Building table: {table_name} from schema {schema_name}")
        table_file = output_dir.joinpath(f"{table_name}.md")
        with open(table_file, mode="w", encoding="UTF-8") as file:
            file.write(get_md_tabs(schema, table_name))

    # Clean up other markdown files not covered by the tables.
    remove_files = [file for file in output_dir.glob("*.md") if file.is_file() and file.name.removesuffix(".md") not in table_names]
    for file in remove_files:
        print(f"Deleting file {file.absolute()}")
        file.unlink()
