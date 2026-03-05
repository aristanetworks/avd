# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

import pytest
from jinja2 import TemplateRuntimeError
from jinja2.runtime import Undefined

from pyavd.j2filters import mandatory

# Valid values that should pass through the filter
VALID_VALUES = [
    1,
    0,
    -1,
    "string",
    "",  # Empty string is still a valid value
    True,
    False,
    [],  # Empty list is still a valid value
    [1, 2, 3],
    {},  # Empty dict is still a valid value
    {"key": "value"},
    0.0,
    1.5,
]

# Invalid values that should raise TemplateRuntimeError
INVALID_VALUES = [
    None,
    Undefined(),
]


class TestMandatoryFilter:
    @pytest.mark.parametrize("value", VALID_VALUES)
    def test_mandatory_with_valid_values(self, value: Any) -> None:
        """Test that valid values pass through the filter unchanged."""
        result = mandatory(value)
        assert result == value

    @pytest.mark.parametrize("value", INVALID_VALUES)
    def test_mandatory_with_invalid_values_default_message(self, value: Any) -> None:
        """Test that invalid values raise TemplateRuntimeError with default message."""
        with pytest.raises(TemplateRuntimeError, match="Variable is required but not defined"):
            mandatory(value)

    @pytest.mark.parametrize("value", INVALID_VALUES)
    def test_mandatory_with_invalid_values_custom_message(self, value: Any) -> None:
        """Test that invalid values raise TemplateRuntimeError with custom message."""
        custom_msg = "Custom error: This field is mandatory!"
        with pytest.raises(TemplateRuntimeError, match=custom_msg):
            mandatory(value, msg=custom_msg)

    @pytest.mark.parametrize("value", VALID_VALUES)
    def test_mandatory_with_valid_values_and_message(self, value: Any) -> None:
        """Test that valid values pass through even when custom message is provided."""
        custom_msg = "This should not be raised"
        result = mandatory(value, msg=custom_msg)
        assert result == value
