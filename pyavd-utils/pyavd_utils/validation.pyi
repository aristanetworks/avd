# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
# Including docstrings since that is why we want this. Also allowing bad name style to match pyo3 output.
# ruff: noqa: PYI021
from pathlib import Path
from typing import Literal

class Feedback:
    """Feedback item carried in the Context under either `coercions`, `insertions` or `violations`."""

    path: list[str]
    """Path to the data which the feedback concerns."""

    message: str
    """String detailing the feedback."""

class ValidationResult:
    """Result of data validation."""

    violations: list[Feedback]
    coercions: list[Feedback]
    insertions: list[Feedback]

class GetValidatedDataResult:
    """Result of data validation including the validated data as JSON."""

    validation_result: ValidationResult
    validated_data: str | None

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

def validate_json(data_as_json: str, schema_name: Literal["eos_cli_config_gen", "eos_designs"]) -> ValidationResult:
    """
    Validate data against a schema specified by name.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_name: The name of the schema to validate against.

    Returns:
        ValidationResult holding lists of violations and coercions as Feedback objects.
    """

def get_validated_data(data_as_json: str, schema_name: Literal["eos_cli_config_gen", "eos_designs"]) -> GetValidatedDataResult:
    """
    Validate data against a schema specified by name and return the data after coercion and validation.

    This returned data is the type-coerced data encoded as JSON, which also contains default values that got inserted during validation.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_name: The name of the schema to validate against.

    Returns:
        CoercionAndValidationResult holding the validated data and the ValidationResult with lists of violations and coercions as Feedback objects.
    """

def validate_json_with_adhoc_schema(data_as_json: str, schema_as_json: str) -> ValidationResult:
    """
    Validate data against the given schema.

    Args:
        data_as_json: Structured data dumped as JSON.
        schema_as_json: A fully resolved schema dumped as JSON.

    Returns:
        ValidationResult holding lists of violations and coercions as Feedback objects.
    """
