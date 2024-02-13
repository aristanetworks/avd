#!/usr/bin/env python3
# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from json import dump as json_dump
from pathlib import Path
from sys import path
from textwrap import indent

from deepmerge import always_merger
from yaml import CSafeDumper, CSafeLoader
from yaml import dump as yaml_dump
from yaml import load as yaml_load

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.constants import JSONSCHEMA_PATHS, LICENSE_HEADER, REPO_ROOT, SCHEMA_FRAGMENTS_PATHS, SCHEMA_PATHS
from schema_tools.generate_docs.mdtabsgen import get_md_tabs
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema

path.insert(0, str(REPO_ROOT))

from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdtojsonschemaconverter import AvdToJsonSchemaConverter
from ansible_collections.arista.avd.plugins.plugin_utils.schema.store import create_store

FRAGMENTS_PATTERN = "*.schema.yml"


def combine_schemas():
    """
    Combine all schema fragments into a single YAML file.
    """
    for schema_name, fragments_path in SCHEMA_FRAGMENTS_PATHS.items():
        print("Combining fragments", fragments_path)
        if schema_name not in SCHEMA_PATHS:
            raise KeyError(f"Invalid schema name '{schema_name}'")

        schema = {}
        for fragment_filename in sorted(fragments_path.glob(FRAGMENTS_PATTERN)):
            # print("Combining fragment", fragment_filename)
            with fragment_filename.open(mode="r", encoding="UTF-8") as fragment_stream:
                schema = always_merger.merge(schema, yaml_load(fragment_stream, Loader=CSafeLoader))

        with SCHEMA_PATHS[schema_name].open(mode="w", encoding="UTF-8") as schema_stream:
            schema_stream.write(indent(LICENSE_HEADER, prefix="# ") + "\n")
            schema_stream.write(yaml_dump(schema, Dumper=CSafeDumper, sort_keys=False))


def convert_to_jsonschema(schema_store):
    for schema_name, jsonschema_file in JSONSCHEMA_PATHS.items():
        print("Converting JSON schema", schema_name)
        if schema_name not in schema_store:
            raise KeyError(f"Invalid schema name '{schema_name}'")

        with jsonschema_file.open(mode="w", encoding="UTF-8") as file_stream:
            json_dump(AvdToJsonSchemaConverter().convert_schema(schema_store[schema_name]), file_stream, sort_keys=False, indent=2)


def build_schema_tables(schema_store):
    for schema_name, schema_path in SCHEMA_PATHS.items():
        if schema_name not in SCHEMA_FRAGMENTS_PATHS:
            continue

        schema = AristaAvdSchema(**schema_store[schema_name])
        table_names = sorted(schema._descendant_tables)
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


def main():
    combine_schemas()
    print("Rebuilding pickled schemas")
    schema_store = create_store(force_rebuild=True)
    convert_to_jsonschema(schema_store)
    build_schema_tables(schema_store)


if __name__ == "__main__":
    main()
