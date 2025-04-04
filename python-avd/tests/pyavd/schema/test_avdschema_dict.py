# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path
from typing import Any

import pytest

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

from pyavd._errors import AvdValidationError
from pyavd._schema.avdschema import AvdSchema

TEST_SCHEMA = {
    "type": "dict",
    "keys": {
        "test_value": {
            "type": "dict",
            "default": {"pri": 1, "foo": "foo1"},
            "required": True,
            "description": "Some string",
            "display_name": "String",
            "allow_other_keys": False,
            "keys": {
                "pri": {"type": "int", "convert_types": ["str"]},
                "foo": {"type": "str", "convert_types": ["int"]},
                "nested_dict": {  # nested_dict is not required, but the key inside is.
                    "type": "dict",
                    "keys": {"required_key": {"type": "str", "required": True}},
                },
                "dynamic": {
                    "type": "list",
                    "items": {
                        "type": "dict",
                        "keys": {"key": {"type": "str"}},
                    },
                },
            },
            "dynamic_keys": {"dynamic.key": {"type": "int"}},
        },
    },
}


@pytest.fixture(scope="module")
def avd_schema() -> AvdSchema:
    return AvdSchema(TEST_SCHEMA)


@pytest.mark.parametrize(
    ("test_value", "expected_errors", "expected_error_messages"),
    [
        pytest.param({"pri": 1, "foo": "foo1"}, None, None, id="ok"),
        pytest.param({"pri": "1", "foo": 123}, None, None, id="ok-nested-coercion"),
        pytest.param(
            {"invalid_key": True},
            (AvdValidationError,),
            ("'Validation Error: test_value': Unexpected key(s) 'invalid_key' found in dict.",),
            id="err-invalid-key",
        ),
        pytest.param({}, None, None, id="ok-empty"),
        pytest.param(None, (AvdValidationError,), ("'Validation Error: ': Required key 'test_value' is not set in dict.",), id="err-missing-required-value"),
        pytest.param(
            {"nested_dict": {}},
            (AvdValidationError,),
            ("'Validation Error: test_value.nested_dict': Required key 'required_key' is not set in dict.",),
            id="err-missing-nested-required-value",
        ),
        pytest.param("a", (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'str'. Expected a 'dict'.",), id="err-invalid-type-str"),
        pytest.param({"mykey": 123, "dynamic": [{"key": "mykey"}]}, None, None, id="ok-dynamic-key-mykey"),
        pytest.param(
            {"mykey2": 123, "dynamic": [{"key": "mykey"}]},
            (AvdValidationError,),
            ("'Validation Error: test_value': Unexpected key(s) 'mykey2' found in dict.",),
            id="err-invalid-dynamic-key-mykey2",
        ),
        pytest.param(
            {"mykey": "bar", "dynamic": [{"key": "mykey"}]},
            (AvdValidationError,),
            ("'Validation Error: test_value.mykey': Invalid type 'str'. Expected a 'int'.",),
            id="err-invalid-dynamic-key-value-bar",
        ),
    ],
)
def test_generated_schema(
    test_value: Any, expected_errors: tuple[type[AvdValidationError], ...] | None, expected_error_messages: tuple[str, ...] | None, avd_schema: AvdSchema
) -> None:
    instance = {"test_value": test_value}
    list(avd_schema.convert(instance))
    validation_errors = list(avd_schema.validate(instance))
    if expected_errors and expected_error_messages:
        for validation_error in validation_errors:
            assert isinstance(validation_error, expected_errors)
            assert str(validation_error) in expected_error_messages

        assert len(validation_errors) == len(expected_error_messages)
    else:
        # No errors expected.
        assert not validation_errors
