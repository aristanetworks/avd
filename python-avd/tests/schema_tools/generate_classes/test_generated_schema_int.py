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

# TODO: Test Dynamic valid values once that is part of the pydantic converter.
#       Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "int",
            "convert_types": ["bool", "str", "float"],
            "default": 11,
            "min": 2,
            "max": 20,
            "valid_values": [0, 11, 22],
            "dynamic_valid_values": ["valid_values"],  # Part of meta schema but not implemented in converter
            "required": True,
            "description": "Some integer",
            "display_name": "Integer",
        },
    },
}

TESTS = [
    # (test_value, expected_warnings: tuple, expected_warning_pattern: str)
    (11, None, None),  # Valid value. No errors.
    (
        False,
        (pyavd._schema.types.InvalidValue,),
        r"Got invalid value for 'test_value'. Expected '>=2', got 'False'",
    ),  # False is converted to 0 which is valid but below min.
    (
        True,
        (pyavd._schema.types.InvalidValue,),
        r"Got invalid value for 'test_value'. Expected '0 or 11 or 22', got 'True'",
    ),  # True is converted to 1 which is not valid.
    ("11", None, None),  # Converted to 11. No errors.
    (
        11.0123,
        (pyavd._schema.types.InvalidType,),
        r"Got invalid type for 'test_value'. Expected '<class 'int'>', got '<class 'float'>'",
    ),  # Converted to 11. No errors.
    (
        None,
        (pyavd._schema.types.InvalidType,),
        r"Got invalid type for 'test_value'. Expected '<class 'int'>', got '<class 'NoneType'>'",
    ),  # Required is set, so None is not ignored.
    (12, (pyavd._schema.types.InvalidValue,), r"Got invalid value for 'test_value'. Expected '0 or 11 or 22', got '12'"),  # Invalid value.
    ([], (pyavd._schema.types.InvalidType,), r"Got invalid type for 'test_value'. Expected '<class 'int'>', got '<class 'list'>'"),  # Invalid type.
    (0, (pyavd._schema.types.InvalidValue,), r"Got invalid value for 'test_value'. Expected '>=2', got '0'"),  # Valid but below min.
    (22, (pyavd._schema.types.InvalidValue,), r"Got invalid value for 'test_value'. Expected '<=20', got '22'"),  # Valid but above max.
]


@pytest.fixture(scope="module")
def int_schema_model() -> pyavd._schema.models.AvdBase:
    schema_name = "int_schema"
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
    test_value: Any, expected_warnings: tuple | None, expected_warning_pattern: str | None, int_schema_model: pyavd._schema.models.AvdBase
) -> None:
    test_value_id = id(test_value)
    if expected_warnings:
        with pytest.warns(expected_warnings, match=expected_warning_pattern):
            assert not int_schema_model._validate_dict({"test_value": test_value})

    else:
        # No errors expected.
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            assert int_schema_model._validate_dict({"test_value": test_value})

    # Make sure the test value was not changed
    assert id(test_value) == test_value_id
