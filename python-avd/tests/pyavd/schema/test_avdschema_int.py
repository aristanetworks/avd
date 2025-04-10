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
            "type": "int",
            "convert_types": ["bool", "str", "float"],
            "default": 11,
            "min": 2,
            "max": 20,
            "valid_values": [0, 11, 22],
            "dynamic_valid_values": ["dynamic.valid_value"],  # Part of meta schema but not implemented in converter
            "required": True,
            "description": "Some integer",
            "display_name": "Integer",
        },
        "dynamic": {"type": "list", "items": {"type": "dict", "keys": {"valid_value": {"type": "int"}}}},
    },
}


@pytest.fixture(scope="module")
def avd_schema() -> AvdSchema:
    return AvdSchema(TEST_SCHEMA)


@pytest.mark.parametrize(
    ("test_value", "dynamic_valid_values", "expected_errors", "expected_error_messages"),
    [
        pytest.param(11, None, None, None, id="ok-no-coerce-11"),  # Valid value. No errors.
        pytest.param(
            False,
            None,
            (AvdValidationError,),
            ("'Validation Error: test_value': '0' is lower than the allowed minimum of 2.",),
            id="err-coerce-bool-to-int-below-min-0",
        ),  # False is converted to 0 which is valid but below min.
        pytest.param(
            True,
            None,
            (AvdValidationError,),
            ("'Validation Error: test_value': '1' is lower than the allowed minimum of 2.", "'Validation Error: test_value': '1' is not one of [0, 11, 22]"),
            id="err-coerce-bool-to-int-invalid-value-1",
        ),
        pytest.param("11", None, None, None, id="ok-coerce-str-to-int"),
        pytest.param(11.0123, None, None, None, id="ok-coerce-float-to-int"),
        pytest.param(
            None, None, (AvdValidationError,), ("'Validation Error: ': Required key 'test_value' is not set in dict.",), id="err-missing-required-value"
        ),
        pytest.param(12, None, (AvdValidationError,), ("'Validation Error: test_value': '12' is not one of [0, 11, 22]",), id="err-invalid-value-12"),
        pytest.param(12, [12], None, None, id="ok-dynamic-valid-value-12"),
        pytest.param([], None, (AvdValidationError,), ("'Validation Error: test_value': Invalid type 'list'. Expected a 'int'.",), id="err-invalid-type-list"),
        pytest.param(0, None, (AvdValidationError,), ("'Validation Error: test_value': '0' is lower than the allowed minimum of 2.",), id="err-below-min-0"),
        pytest.param(
            22, None, (AvdValidationError,), ("'Validation Error: test_value': '22' is higher than the allowed maximum of 20.",), id="err-above-max-22"
        ),
    ],
)
def test_generated_schema(
    test_value: Any,
    dynamic_valid_values: list[int] | None,
    expected_errors: tuple[type[AvdValidationError], ...] | None,
    expected_error_messages: tuple[str, ...] | None,
    avd_schema: AvdSchema,
) -> None:
    instance = {"test_value": test_value, "dynamic": [{"valid_value": valid_value} for valid_value in dynamic_valid_values or []]}
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
