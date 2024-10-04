# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
import warnings
from importlib import import_module
from pathlib import Path
from sys import path
from typing import Any
from unittest import mock

import pytest

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

import pyavd._schema.models
import pyavd._schema.types
from schema_tools.generate_classes.src_generators import FileSrc
from schema_tools.generate_classes.utils import generate_class_name
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema

# TODO: Decide to either implement valid values or remove it from meta schema for bools
#       Decide if we should keep convert_types for boolean.
#       Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "bool",
            "convert_types": ["int", "str"],  # Part of meta schema but not implemented in converter
            "default": True,
            "valid_values": [True],
            "dynamic_valid_values": ["valid_booleans"],  # Part of meta schema but not implemented in converter
            "required": True,
            "description": "Some boolean",
            "display_name": "Boolean",
        },
    },
}

TESTS = [
    # (test_value, expected_warnings: tuple, expected_warning_pattern: str)
    (True, None, None),  # Valid value. No errors.
    (False, (pyavd._schema.types.InvalidValue,), "Got invalid value for 'test_value'. Expected 'True', got 'False'"),  # Valid value. Not a valid value.
    (
        11.0123,
        (pyavd._schema.types.InvalidType,),
        "Got invalid type for 'test_value'. Expected '<class 'bool'>', got '<class 'float'>'",
    ),  # Invalid value.
    (
        None,
        (pyavd._schema.types.InvalidType,),
        "Got invalid type for 'test_value'. Expected '<class 'bool'>', got '<class 'NoneType'>'",
    ),  # Required is set, so None is not ignored.
    ("11", None, None),  # Converted to True. No errors.
    ("", (pyavd._schema.types.InvalidValue,), "Got invalid value for 'test_value'. Expected 'True', got 'False'"),  # Converted to False. Not a valid value.
    (12, None, None),  # Converted to True. No errors.
    (0, (pyavd._schema.types.InvalidValue,), "Got invalid value for 'test_value'. Expected 'True', got 'False'"),  # Converted to False. Not a valid value.
]


@pytest.fixture(scope="module")
def bool_schema_model() -> pyavd._schema.models.AvdBase:
    schema_name = "bool_schema"
    schema_model = AristaAvdSchema(**TEST_SCHEMA)
    output_file = Path(__file__).parent.joinpath(f"artifacts/{schema_name}.py")
    schemasrc = schema_model._generate_class_src(class_name=schema_name)
    src_file_contents = FileSrc(classes=[schemasrc.cls])
    with output_file.open(mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd._schema.types, "artifacts.models": pyavd._schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    return getattr(module, class_name)


@pytest.mark.parametrize(("test_value", "expected_warnings", "expected_warning_pattern"), TESTS)
def test_generated_schema(
    test_value: Any, expected_warnings: tuple | None, expected_warning_pattern: str | None, bool_schema_model: pyavd._schema.models.AvdBase
) -> None:
    if expected_warnings:
        with pytest.warns(expected_warnings, match=expected_warning_pattern):
            assert not bool_schema_model._validate_dict({"test_value": test_value})

    else:
        # No errors expected.
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            assert bool_schema_model._validate_dict({"test_value": test_value})
