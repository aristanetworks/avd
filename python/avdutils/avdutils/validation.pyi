# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Including docstrings since that is why we want this
# ruff: noqa: PYI021
from pathlib import Path
from typing import Literal

def init_store_from_fragments(eos_cli_config_gen: Path, eos_designs: Path) -> None:
    """
    Re-initialize the Schema store from Schema YAML fragments.

    This will overwrite the builtin-schema that was included in the Rust code during compilation.
    This must be called before running any validations, since the store is a write-once static.

    Args:
        eos_cli_config_gen: Path to the directory holding the schema fragments for `eos_cli_config_gen`.
        eos_designs: Path to the directory holding the schema fragments for `eos_designs`.

    Raises:
        RuntimeError: For any issue hit during loading, deserializing, combining and resolving schemas.
    """

def validate_json(data_as_json: str, schema_name: Literal["eos_cli_config_gen", "eos_designs"]) -> str:
    """
    Validate data against a schema specified by name.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_name: The name of the schema to validate against.

    Returns:
        A JSON string containing the validation results.
    """

def validate_json_with_adhoc_schema(data_as_json: str, schema_as_json: str) -> str:
    """
    Validate data against the given schema.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_as_json: A fully resolved schema dumped as JSON.

    Returns:
        A JSON string containing the validation results.
    """
