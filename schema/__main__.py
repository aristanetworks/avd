# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from .constants import SCHEMA_PATHS, STORE
from .generate_docs.mdtabsgen import get_md_tabs
from .generate_docs.utils import list_tables
from .metaschema.meta_schema_model import AristaAvdSchema
from .metaschema.resolvemodel import merge_schema_from_ref

# output_dir = SCHEMA_PATHS["eos_designs"].parents[1].joinpath("docs/tables")
# schema = AristaAvdSchema(**STORE["eos_designs"])
# table_names = list_tables(schema)
# # print(table_names)
# files = list(output_dir.glob("*.md"))
# print([file.name.removesuffix(".md") for file in files if file.name.removesuffix(".md") not in table_names])
# print(len(files), len(table_names))

for schema_name, schema_path in SCHEMA_PATHS.items():
    if schema_name not in STORE:
        raise KeyError(f"Invalid schema name '{schema_name}'")

    resolved_schema = merge_schema_from_ref(STORE[schema_name])
    schema = AristaAvdSchema(**resolved_schema)
    table_names = sorted(list_tables(schema))
    output_dir = schema_path.parents[1].joinpath("docs/tables")
    for table_name in table_names:
        print(f"Building table: {table_name} from schema {schema_name}")
        table_file = output_dir.joinpath(f"{table_name}.md")
        with open(table_file, mode="w", encoding="UTF-8") as file:
            file.write(get_md_tabs(schema, table_name))

    # Clean up other markdown files not covered by the tables.
    [file.unlink() for file in output_dir.glob("*.md") if file.is_file() and file.name.removesuffix(".md") not in table_names]
