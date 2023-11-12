# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import sys
from importlib import import_module
from pathlib import Path
from sys import path
from unittest import mock

import pytest
from pydantic import BaseModel, ValidationError

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

import pyavd.schema.models
import pyavd.schema.types
from pyavd.schema.generate_pydantic.models import PydanticFileSrc
from pyavd.schema.generate_pydantic.utils import generate_class_name
from pyavd.schema.metaschema.meta_schema_model import AristaAvdSchema

# TODO:
# - Decide to either implement valid values or remove it from meta schema for bools
# - Decide if we should keep convert_types for boolean.
# - Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "bool",
            "convert_types": ["int", "str"],
            "default": True,
            "valid_values": [True],  # Part of meta schema but not implemented in converter
            "dynamic_valid_values": "valid_booleans",  # Part of meta schema but not implemented in converter
            "required": True,
            "description": "Some boolean",
            "display_name": "Boolean",
        },
    },
}

TESTS = [
    # (test_value: int | None, expected_errors: set, expected_value: int)
    (True, None, True),  # Valid value. No errors.
    (False, None, False),  # Valid value. No errors.
    (11.0123, {"Input should be a valid boolean"}, None),  # Invalid value.
    (None, {"Input should be a valid boolean"}, None),  # Required is set, so None is not ignored.
    ("11", None, True),  # Converted to True. No errors.
    ("", None, False),  # Converted to False. No errors.
    (12, None, True),  # Converted to True. No errors.
    (0, None, False),  # Converted to False. No errors.
]


@pytest.fixture(scope="module")
def BoolSchemaModel() -> type[BaseModel]:
    schema_name = "bool_schema"
    schema_model = AristaAvdSchema(**TEST_SCHEMA)
    output_file = Path(__file__).parent.joinpath(f"artifacts/{schema_name}.py")
    schemasrc = schema_model._generate_pydantic_src(class_name=schema_name)
    src_file_contents = PydanticFileSrc(classes=[schemasrc.cls])
    with open(output_file, mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    with mock.patch.dict(sys.modules, {"artifacts.types": pyavd.schema.types, "artifacts.models": pyavd.schema.models}):
        module = import_module(f"artifacts.{schema_name}")
    class_name = generate_class_name(schema_name)
    Cls = getattr(module, class_name)
    # Yield the class
    yield Cls

    # After testing remove the file
    # output_file.unlink()


@pytest.mark.parametrize(("test_value", "expected_errors", "expected_value"), TESTS)
def test_generated_schema(test_value, expected_errors: set, expected_value: int | None, BoolSchemaModel: type[BaseModel]):
    test_value_id = id(test_value)
    if expected_errors:
        with pytest.raises(ValidationError) as exc_info:
            BoolSchemaModel(test_value=test_value)
        errors = exc_info.value.errors()
        msgs = set(error["msg"] for error in errors)
        assert msgs == expected_errors

    else:
        # No errors expected.
        data = BoolSchemaModel(test_value=test_value)
        assert hasattr(data, "test_value")
        assert getattr(data, "test_value") == expected_value

    # Make sure the test value was not changed
    assert id(test_value) == test_value_id
