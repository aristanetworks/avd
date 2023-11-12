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
# - Test Formats once that is part of the pydantic converter - replacing format.
# - Test default value with required False.

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "valid_values": {"type": "list"},
        "test_value": {
            "type": "str",
            "convert_types": ["bool", "int", "float"],
            "default": "foo",
            "valid_values": ["a", "foo", "zoo", "baaar", "1.0", "42", "true"],
            "convert_to_lower_case": True,
            "max_length": 4,
            "min_length": 2,
            "dynamic_valid_values": "valid_strings",
            "pattern": "[abf14t].*",
            "required": True,
            "description": "Some string",
            "display_name": "String",
        },
    },
}

TESTS = [
    # (test_value: str | None, valid_values: list[str] | None, expected_errors: set, expected_value: str)
    ("foo", None, None, "foo"),  # Valid value. No errors.
    ("FoO", None, None, "foo"),  # Lowered to "foo" which is valid.
    (True, None, None, "true"),  # True is converted and lowered to "true" which is valid.
    (False, None, {"Input should be 'a', 'foo', 'zoo', 'baaar', '1.0', '42' or 'true'"}, None),  # False is converted and lowered to "false" which is not valid.
    (42, None, None, "42"),  # Converted to "42". No errors.
    (1.000, None, None, "1.0"),  # Converted to "1.0". No errors.
    (None, None, {"Input should be 'a', 'foo', 'zoo', 'baaar', '1.0', '42' or 'true'"}, None),  # Required is set, so None is not ignored.
    ([], None, {"Input should be 'a', 'foo', 'zoo', 'baaar', '1.0', '42' or 'true'"}, None),  # Invalid type.
    ("a", None, {"Value should have at least 2 items after validation, not 1"}, None),  # Valid but below min length.
    ("baaar", None, {"Value should have at most 4 items after validation, not 5"}, None),  # Valid but below min length.
    (22, None, {"Input should be 'a', 'foo', 'zoo', 'baaar', '1.0', '42' or 'true'"}, None),  # Converted to "22" which is not valid.
    ("zoo", None, {"String should match pattern '[abf14t].*'"}, None),  # Valid value but does not match pattern.
]


@pytest.fixture(scope="module")
def StrSchemaModel() -> type[BaseModel]:
    schema_name = "str_schema"
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
def test_generated_schema(test_value, valid_values: list | None, expected_errors: set, expected_value: int | None, StrSchemaModel: type[BaseModel]):
    test_value_id = id(test_value)
    if expected_errors:
        with pytest.raises(ValidationError) as exc_info:
            StrSchemaModel(test_value=test_value, valid_values=valid_values)
        errors = exc_info.value.errors()
        msgs = set(error["msg"] for error in errors)
        assert msgs == expected_errors

    else:
        # No errors expected.
        data = StrSchemaModel(test_value=test_value, valid_values=valid_values)
        assert hasattr(data, "test_value")
        assert getattr(data, "test_value") == expected_value

    # Make sure the test value was not changed
    assert id(test_value) == test_value_id
