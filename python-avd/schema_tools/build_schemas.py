# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import gzip
import io
import json
import logging
import subprocess
from os.path import relpath
from pathlib import Path
from textwrap import indent

from deepmerge import always_merger
from yaml import CSafeDumper, CSafeLoader
from yaml import dump as yaml_dump
from yaml import load as yaml_load

from .constants import LICENSE_HEADER, METASCHEMA_DIR, SCHEMA_STORE_ARCHIVE_FILE, SCHEMA_STORE_GZ_FILE, SCHEMAS
from .store import create_store

try:
    import jsonschema_rs

    JSON_SCHEMA_VALIDATOR = jsonschema_rs.Draft7Validator
    HAS_JSONSCHEMA_RS = True
except ImportError:
    HAS_JSONSCHEMA_RS = False

FRAGMENTS_PATTERN = "*.yml"
METASCHEMA_FILE = METASCHEMA_DIR.joinpath("avd_meta_schema.json")

LOGGER = logging.getLogger(__name__)


def _get_relative_metaschema_path(schema_file: Path) -> str:
    """Compute the relative path from a schema file directory to the metaschema JSON file."""
    schema_dir = schema_file.parent
    return relpath(METASCHEMA_FILE, schema_dir).replace("\\", "/")


def combine_schemas() -> None:
    """
    Combine all schema fragments into a single YAML file.

    Also writes the schemas.json.gz file.
    """
    store: dict[str, dict] = {}
    for schema_name, schema_paths in SCHEMAS.items():
        if not (fragments_path := schema_paths.fragments_dir):
            continue

        LOGGER.info("Combining fragments %s", fragments_path)

        schema = {}
        for fragment_filename in sorted(fragments_path.glob(FRAGMENTS_PATTERN)):
            with fragment_filename.open(mode="r", encoding="UTF-8") as fragment_stream:
                schema = always_merger.merge(schema, yaml_load(fragment_stream, Loader=CSafeLoader))

        # Compute the relative path from this schema file to the metaschema
        metaschema_rel_path = _get_relative_metaschema_path(schema_paths.yaml_file)

        with schema_paths.yaml_file.open(mode="w", encoding="UTF-8") as schema_stream:
            schema_stream.write(indent(LICENSE_HEADER, prefix="# ") + "\n")
            schema_stream.write(
                f"# yaml-language-server: $schema={metaschema_rel_path}\n"
                "# Line above is used by RedHat's YAML Schema vscode extension\n"
                "# Use Ctrl + Space to get suggestions for every field. Autocomplete will pop up after typing 2 letters.\n",
            )
            schema_stream.write(yaml_dump(schema, Dumper=CSafeDumper, sort_keys=False))

        store[schema_name] = schema

    with io.TextIOWrapper(
        # Using mtime=0 to ensure a consistent Gzip file each time for the same content.
        buffer=gzip.GzipFile(filename=SCHEMA_STORE_GZ_FILE, mode="wb", mtime=0),
        encoding="UTF-8",
    ) as gz_file:
        json.dump(store, gz_file)


def validate_schemas(schema_store: dict) -> None:
    """Validate schemas according to metaschema."""
    if not HAS_JSONSCHEMA_RS:
        LOGGER.warning(
            "'jsonschema_rs' was not found. If you are a developer using AVD make sure to install the dev requirements for the collection. "
            "The schemas could not be validated."
        )
        return
    schema_validator = JSON_SCHEMA_VALIDATOR(schema_store["avd_meta_schema"])
    for schema_name, schema in schema_store.items():
        if schema_name == "avd_meta_schema":
            continue

        LOGGER.info("Validating schema '%s'", schema_name)
        schema_validator.validate(schema)


def build_schema_tables() -> None:
    """Build schema tables."""
    from pyavd_utils_gen.schema_generation import generate_schema_documentation_from_paths  # noqa: PLC0415

    LOGGER.info("Rebuilding schema documentation tables...")
    raw_yaml_schema_paths = {schema_name: schema_paths.yaml_file for schema_name, schema_paths in SCHEMAS.items() if schema_name != "avd_meta_schema"}
    for schema_name, schema_paths in SCHEMAS.items():
        if not schema_paths.docs_path:
            continue

        LOGGER.info("Building schema documentation: %s", schema_name)
        generate_schema_documentation_from_paths(raw_yaml_schema_paths, schema_name, schema_paths.docs_path.joinpath("tables"))


def build_schema_classes() -> None:
    """Build Python Classes from schema."""
    from pyavd_utils_gen.schema_generation import generate_python_schema_models_from_paths  # noqa: PLC0415

    LOGGER.info("Rebuilding schema Python Classes...")
    # Load unresolved source schemas so generation can preserve references and reuse eligible model types.
    raw_yaml_schema_paths = {schema_name: schema_paths.yaml_file for schema_name, schema_paths in SCHEMAS.items() if schema_paths.python_class}
    for schema_name, schema_paths in SCHEMAS.items():
        if not schema_paths.python_class:
            continue

        LOGGER.info("Building Python Classes from schema: %s", schema_name)
        generate_python_schema_models_from_paths(
            raw_yaml_schema_paths,
            schema_name,
            schema_paths.python_class,
        )

        LOGGER.info("Running 'ruff' for Python class file: %s", schema_paths.python_class)
        subprocess.run(["ruff", "check", "--fix", str(schema_paths.python_class)], check=False)  # noqa: S603, S607
        subprocess.run(["ruff", "format", str(schema_paths.python_class)], check=False)  # noqa: S603, S607


def build_schemas() -> None:
    """Combines the schema fragments, and rebuild the pickled schemas."""
    combine_schemas()
    from pyavd_utils_gen.schema_store import compile_schema_archive  # noqa: PLC0415

    LOGGER.info("Compiling archived schema store")
    compile_schema_archive(SCHEMA_STORE_GZ_FILE, SCHEMA_STORE_ARCHIVE_FILE)
    LOGGER.info("Rebuilding pickled schemas")
    schema_store = create_store(force_rebuild=True)
    validate_schemas(schema_store)
    build_schema_tables()
    build_schema_classes()
