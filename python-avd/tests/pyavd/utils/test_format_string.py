# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import pytest

from pyavd._utils import AvdStringFormatter

FORMAT_STRING_TESTS = [
    # (<format_string>, <args ()>, <kwargs {}>, <expected_output>)
    # no fields
    pytest.param("Ethernet1", (), {}, "Ethernet1", id="no_fields"),
    pytest.param("Ethernet1", (), {"foo": "bar"}, "Ethernet1", id="no_fields_with_args"),
    pytest.param("{{Ethernet1}}", (), {}, "{Ethernet1}", id="escaped_curly_brace"),
    # named fields with upper
    pytest.param("{interface!u}", (), {"interface": "Ethernet1"}, "ETHERNET1", id="field_with_existing_arg_and_upper"),
    pytest.param("{interface?!u}", (), {}, "", id="optional_field_with_missing_arg_and_upper"),
    pytest.param("{interface?!u}", (), {"interface": None}, "", id="optional_field_with_none_arg_and_upper"),
    pytest.param("{interface?!u}", (), {"interface": "Ethernet1"}, "ETHERNET1", id="optional_field_with_existing_arg_and_upper"),
    # positional fields with upper
    pytest.param("{!u}", ("Ethernet1",), {}, "ETHERNET1", id="positional_field_with_existing_arg_and_upper"),
    pytest.param("{?!u}", (), {}, "", id="positional_optional_field_with_missing_arg_and_upper"),
    pytest.param("{?!u}", (None,), {}, "", id="positional_optional_field_with_none_arg_and_upper"),
    pytest.param("{?!u}", ("Ethernet1",), {}, "ETHERNET1", id="positional_optional_field_with_existing_arg_and_upper"),
    # named fields with prefix
    pytest.param("{interface<foo  }", (), {"interface": "Ethernet1"}, "foo  Ethernet1", id="field_with_prefix_existing_arg"),
    pytest.param("{interface?<foo}", (), {}, "", id="optional_field_with_prefix_missing_arg"),
    pytest.param("{interface?< f o o }", (), {"interface": None}, "", id="optional_field_with_prefix_none_arg"),
    pytest.param("{interface?< f o o }", (), {"interface": "Ethernet1"}, " f o o Ethernet1", id="optional_field_with_prefix_existing_arg"),
    # positional fields with prefix
    pytest.param("{<foo  }", ("Ethernet1",), {}, "foo  Ethernet1", id="positional_field_with_prefix_existing_arg"),
    pytest.param("{?<foo}", (), {}, "", id="positional_optional_field_with_prefix_missing_arg"),
    pytest.param("{?< f o o }", (None,), {}, "", id="positional_optional_field_with_prefix_none_arg"),
    pytest.param("{?< f o o }", ("Ethernet1",), {}, " f o o Ethernet1", id="positional_optional_field_with_prefix_existing_arg"),
    # named fields with suffix
    pytest.param("{interface>foo  }", (), {"interface": "Ethernet1"}, "Ethernet1foo  ", id="field_with_suffix_existing_arg"),
    pytest.param("{interface?>foo}", (), {}, "", id="optional_field_with_suffix_missing_arg"),
    pytest.param("{interface?> f o o }", (), {"interface": None}, "", id="optional_field_with_suffix_none_arg"),
    pytest.param("{interface?> f o o }", (), {"interface": "Ethernet1"}, "Ethernet1 f o o ", id="optional_field_with_suffix_existing_arg"),
    # positional fields with suffix
    pytest.param("{>foo  }", ("Ethernet1",), {}, "Ethernet1foo  ", id="positional_field_with_suffix_existing_arg"),
    pytest.param("{?>foo}", (), {}, "", id="positional_optional_field_with_suffix_missing_arg"),
    pytest.param("{?> f o o }", (None,), {}, "", id="positional_optional_field_with_suffix_none_arg"),
    pytest.param("{?> f o o }", ("Ethernet1",), {}, "Ethernet1 f o o ", id="positional_optional_field_with_suffix_existing_arg"),
    # named fields with prefix and suffix
    pytest.param("{interface<foo  >bar  }", (), {"interface": "Ethernet1"}, "foo  Ethernet1bar  ", id="field_with_prefix_and_suffix_existing_arg"),
    pytest.param("{interface?<foo>bar}", (), {}, "", id="optional_field_with_prefix_and_suffix_missing_arg"),
    pytest.param("{interface?< f o o > b a r }", (), {"interface": None}, "", id="optional_field_with_prefix_and_suffix_none_arg"),
    pytest.param(
        "{interface?< f o o > b a r }", (), {"interface": "Ethernet1"}, " f o o Ethernet1 b a r ", id="optional_field_with_prefix_and_suffix_existing_arg"
    ),
    # positional fields with prefix and suffix
    pytest.param("{<foo  >bar  }", ("Ethernet1",), {}, "foo  Ethernet1bar  ", id="positional_field_with_prefix_and_suffix_existing_arg"),
    pytest.param("{?<foo>bar}", (), {}, "", id="positional_optional_field_with_prefix_and_suffix_missing_arg"),
    pytest.param("{?< f o o > b a r }", (None,), {}, "", id="positional_optional_field_with_prefix_and_suffix_none_arg"),
    pytest.param("{?< f o o > b a r }", ("Ethernet1",), {}, " f o o Ethernet1 b a r ", id="positional_optional_field_with_prefix_and_suffix_existing_arg"),
    # positional fields with prefix and suffix and upper
    pytest.param("{<foo  >bar  !u}", ("Ethernet1",), {}, "foo  ETHERNET1bar  ", id="positional_field_with_prefix_and_suffix_existing_arg_and_upper"),
    pytest.param("{?<foo>bar!u}", (), {}, "", id="positional_optional_field_with_prefix_and_suffix_missing_arg_and_upper"),
    pytest.param("{?< f o o > b a r !u}", (None,), {}, "", id="positional_optional_field_with_prefix_and_suffix_none_arg_and_upper"),
    pytest.param(
        "{?< f o o > b a r !u}", ("Ethernet1",), {}, " f o o ETHERNET1 b a r ", id="positional_optional_field_with_prefix_and_suffix_existing_arg_and_upper"
    ),
]


class TestAvdStringFormatter:
    @pytest.mark.parametrize(("format_string", "args", "kwargs", "expected_output"), FORMAT_STRING_TESTS)
    def test_avd_formatter(self, format_string: str, args: tuple, kwargs: dict, expected_output: list) -> None:
        resp = AvdStringFormatter().format(format_string, *args, **kwargs)
        assert resp == expected_output
