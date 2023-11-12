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
# - Test Dynamic valid values once that is part of the pydantic converter.
# - Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "valid_values": {"type": "list"},
        "test_value": {
            "type": "int",
            "convert_types": ["bool", "str", "float"],
            "default": 11,
            "min": 2,
            "max": 20,
            "valid_values": [0, 11, 22],
            "dynamic_valid_values": "valid_values",
            "required": True,
            "description": "Some integer",
            "display_name": "Integer",
        },
    },
}

TESTS = [
    # (test_value: int | None, valid_values: list[int] | None, expected_errors: set, expected_value: int)
    (11, None, None, 11),  # Valid value. No errors.
    (False, None, {"Input should be greater than or equal to 2"}, None),  # False is converted to 0 which is valid but below min.
    (True, None, {"Input should be 0, 11 or 22"}, None),  # True is converted to 1 which is not valid.
    ("11", None, None, 11),  # Converted to 11. No errors.
    (11.0123, None, None, 11),  # Converted to 11. No errors.
    (None, None, {"Input should be 0, 11 or 22"}, None),  # Required is set, so None is not ignored.
    (12, None, {"Input should be 0, 11 or 22"}, None),  # Invalid value.
    ([], None, {"Input should be 0, 11 or 22"}, None),  # Invalid type.
    (0, None, {"Input should be greater than or equal to 2"}, None),  # Valid but below min.
    (22, None, {"Input should be less than or equal to 20"}, None),  # Valid but above max.
]


@pytest.fixture(scope="module")
def IntSchemaModel() -> type[BaseModel]:
    schema_name = "int_schema"
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


@pytest.mark.parametrize(("test_value", "valid_values", "expected_errors", "expected_value"), TESTS)
def test_generated_schema(test_value, valid_values: list | None, expected_errors: set, expected_value: int | None, IntSchemaModel: type[BaseModel]):
    test_value_id = id(test_value)
    if expected_errors:
        with pytest.raises(ValidationError) as exc_info:
            IntSchemaModel(test_value=test_value, valid_values=valid_values)
        errors = exc_info.value.errors()
        msgs = set(error["msg"] for error in errors)
        assert msgs == expected_errors

    else:
        # No errors expected.
        data = IntSchemaModel(test_value=test_value, valid_values=valid_values)
        assert hasattr(data, "test_value")
        assert getattr(data, "test_value") == expected_value

    # Make sure the test value was not changed
    assert id(test_value) == test_value_id
