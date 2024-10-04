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
#       Test Formats once that is part of the pydantic converter - replacing format.
#       Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "str",
            "convert_types": ["bool", "int", "float"],
            "default": "foo",
            "valid_values": ["a", "foo", "zoo", "baaar", "1.0", "42", "true"],
            "convert_to_lower_case": True,
            "max_length": 4,
            "min_length": 2,
            "dynamic_valid_values": ["valid_strings"],  # Part of meta schema but not implemented in converter
            "pattern": "[abf14t].*",
            "required": True,
            "description": "Some string",
            "display_name": "String",
        },
    },
}

TESTS = [
    # (id, test_value, expected_warnings: tuple, expected_warning_pattern: str)
    ("foo", None, None),  # Valid value. No errors.
    ("FoO", None, None),  # Lowered to "foo" which is valid.
    (True, None, None),  # True is converted and lowered to "true" which is valid.
    (
        False,
        (pyavd._schema.types.InvalidValue, pyavd._schema.types.InvalidLength),
        None,
    ),  # False is converted and lowered to "false" which is not valid.
    (42, None, None),  # Converted to "42". No errors.
    (1.000, None, None),  # Converted to "1.0". No errors.
    (
        None,
        (pyavd._schema.types.InvalidType,),
        r"Got invalid type for 'test_value'. Expected '<class 'str'>', got '<class 'NoneType'>'",
    ),  # Required is set, so None is not ignored.
    ([], (pyavd._schema.types.InvalidType,), r"Got invalid type for 'test_value'. Expected '<class 'str'>', got '<class 'list'>'"),  # Invalid type.
    (
        "a",
        (pyavd._schema.types.InvalidLength,),
        r"Got invalid length for 'test_value'. Expected a length of >=2, but the value had a length of '1'",
    ),  # Valid but below min length.
    (
        "baaar",
        (pyavd._schema.types.InvalidLength,),
        r"Got invalid length for 'test_value'. Expected a length of <=4, but the value had a length of '5'",
    ),  # Valid but below min length.
    (
        22,
        (pyavd._schema.types.InvalidValue, pyavd._schema.types.InvalidPattern),
        None,
    ),  # Converted to "22" which is not valid.
    (
        "zoo",
        (pyavd._schema.types.InvalidPattern,),
        r"Got invalid value for 'test_value'. Expected a value matching the pattern '\[abf14t\]\.\*', got 'zoo'",
    ),  # Valid value but does not match pattern.
]


@pytest.fixture(scope="module")
def str_schema_model() -> pyavd._schema.models.AvdBase:
    schema_name = "str_schema"
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
    test_value: Any, expected_warnings: tuple | None, expected_warning_pattern: str | None, str_schema_model: pyavd._schema.models.AvdBase
) -> None:
    test_value_id = id(test_value)
    if expected_warnings:
        with pytest.warns(expected_warnings, match=expected_warning_pattern):
            assert not str_schema_model._validate_dict({"test_value": test_value})

    else:
        # No errors expected.
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            assert str_schema_model._validate_dict({"test_value": test_value})

    # Make sure the test value was not changed
    assert id(test_value) == test_value_id
