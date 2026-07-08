# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import pytest

from pyavd._utils import AvdStringFormatter


class DummyClass:
    _private = "private"
    public = "public"


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
    pytest.param("{interface.public?!u}", (), {"interface": DummyClass()}, "PUBLIC", id="optional_field_with_attribute_and_upper"),
    # positional fields with upper
    pytest.param("{!u}", ("Ethernet1",), {}, "ETHERNET1", id="positional_field_with_existing_arg_and_upper"),
    pytest.param("{?!u}", (), {}, "", id="positional_optional_field_with_missing_arg_and_upper"),
    pytest.param("{?!u}", (None,), {}, "", id="positional_optional_field_with_none_arg_and_upper"),
    pytest.param("{?!u}", ("Ethernet1",), {}, "ETHERNET1", id="positional_optional_field_with_existing_arg_and_upper"),
    pytest.param("{0?!u}{1?!u}{0?!u}", ("foo", "bar"), {}, "FOOBARFOO", id="positional_optional_repeated_fields_with_existing_args_and_upper"),
    pytest.param("{0.public?!u}", (DummyClass(),), {}, "PUBLIC", id="positional_optional_field_with_attribute_and_upper"),
    # named fields with prefix
    pytest.param("{interface<foo  }", (), {"interface": "Ethernet1"}, "foo  Ethernet1", id="field_with_prefix_existing_arg"),
    pytest.param("{interface?<foo}", (), {}, "", id="optional_field_with_prefix_missing_arg"),
    pytest.param("{interface?< f o o }", (), {"interface": None}, "", id="optional_field_with_prefix_none_arg"),
    pytest.param("{interface?< f o o }", (), {"interface": "Ethernet1"}, " f o o Ethernet1", id="optional_field_with_prefix_existing_arg"),
    pytest.param("{interface.public?<foo}", (), {"interface": DummyClass()}, "foopublic", id="optional_field_with_prefix_attribute"),
    # positional fields with prefix
    pytest.param("{<foo  }", ("Ethernet1",), {}, "foo  Ethernet1", id="positional_field_with_prefix_existing_arg"),
    pytest.param("{?<foo}", (), {}, "", id="positional_optional_field_with_prefix_missing_arg"),
    pytest.param("{?< f o o }", (None,), {}, "", id="positional_optional_field_with_prefix_none_arg"),
    pytest.param("{?< f o o }", ("Ethernet1",), {}, " f o o Ethernet1", id="positional_optional_field_with_prefix_existing_arg"),
    pytest.param("{0<one}{1<two}{0<three}", ("foo", "bar"), {}, "onefootwobarthreefoo", id="positional_repeated_fields_with_prefix_existing_args"),
    # named fields with suffix
    pytest.param("{interface>foo  }", (), {"interface": "Ethernet1"}, "Ethernet1foo  ", id="field_with_suffix_existing_arg"),
    pytest.param("{interface?>foo}", (), {}, "", id="optional_field_with_suffix_missing_arg"),
    pytest.param("{interface?> f o o }", (), {"interface": None}, "", id="optional_field_with_suffix_none_arg"),
    pytest.param("{interface?> f o o }", (), {"interface": "Ethernet1"}, "Ethernet1 f o o ", id="optional_field_with_suffix_existing_arg"),
    pytest.param("{interface.public?>foo}", (), {"interface": DummyClass()}, "publicfoo", id="optional_field_with_prefix_attribute"),
    # positional fields with suffix
    pytest.param("{>foo  }", ("Ethernet1",), {}, "Ethernet1foo  ", id="positional_field_with_suffix_existing_arg"),
    pytest.param("{?>foo}", (), {}, "", id="positional_optional_field_with_suffix_missing_arg"),
    pytest.param("{?> f o o }", (None,), {}, "", id="positional_optional_field_with_suffix_none_arg"),
    pytest.param("{?> f o o }", ("Ethernet1",), {}, "Ethernet1 f o o ", id="positional_optional_field_with_suffix_existing_arg"),
    pytest.param("{0>one}{1>two}{0>three}", ("foo", "bar"), {}, "fooonebartwofoothree", id="positional_repeated_fields_with_suffix_existing_args"),
    # named fields with prefix and suffix
    pytest.param("{interface<foo  >bar  }", (), {"interface": "Ethernet1"}, "foo  Ethernet1bar  ", id="field_with_prefix_and_suffix_existing_arg"),
    pytest.param("{interface?<foo>bar}", (), {}, "", id="optional_field_with_prefix_and_suffix_missing_arg"),
    pytest.param("{interface?< f o o > b a r }", (), {"interface": None}, "", id="optional_field_with_prefix_and_suffix_none_arg"),
    pytest.param(
        "{interface?< f o o > b a r }", (), {"interface": "Ethernet1"}, " f o o Ethernet1 b a r ", id="optional_field_with_prefix_and_suffix_existing_arg"
    ),
    pytest.param("{interface.public<foo>bar}", (), {"interface": DummyClass()}, "foopublicbar", id="field_with_prefix_attribute"),
    # positional fields with prefix and suffix
    pytest.param("{<foo  >bar  }", ("Ethernet1",), {}, "foo  Ethernet1bar  ", id="positional_field_with_prefix_and_suffix_existing_arg"),
    pytest.param("{?<foo>bar}", (), {}, "", id="positional_optional_field_with_prefix_and_suffix_missing_arg"),
    pytest.param("{?< f o o > b a r }", (None,), {}, "", id="positional_optional_field_with_prefix_and_suffix_none_arg"),
    pytest.param("{?< f o o > b a r }", ("Ethernet1",), {}, " f o o Ethernet1 b a r ", id="positional_optional_field_with_prefix_and_suffix_existing_arg"),
    pytest.param(
        "{0<aaa>one}_{1<bbb>two}_{0<ccc>three}",
        ("foo", "bar"),
        {},
        "aaafooone_bbbbartwo_cccfoothree",
        id="positional_repeated_fields_with_prefix_and_suffix_existing_args",
    ),
    # positional fields with prefix and suffix and upper
    pytest.param("{<foo  >bar  !u}", ("Ethernet1",), {}, "foo  ETHERNET1bar  ", id="positional_field_with_prefix_and_suffix_existing_arg_and_upper"),
    pytest.param("{?<foo>bar!u}", (), {}, "", id="positional_optional_field_with_prefix_and_suffix_missing_arg_and_upper"),
    pytest.param("{?< f o o > b a r !u}", (None,), {}, "", id="positional_optional_field_with_prefix_and_suffix_none_arg_and_upper"),
    pytest.param(
        "{?< f o o > b a r !u}", ("Ethernet1",), {}, " f o o ETHERNET1 b a r ", id="positional_optional_field_with_prefix_and_suffix_existing_arg_and_upper"
    ),
    # named fields with lower
    pytest.param("{interface!l}", (), {"interface": "Ethernet1"}, "ethernet1", id="field_with_existing_arg_and_lower"),
    pytest.param("{interface?!l}", (), {}, "", id="optional_field_with_missing_arg_and_lower"),
    pytest.param("{interface?!l}", (), {"interface": None}, "", id="optional_field_with_none_arg_and_lower"),
    pytest.param("{interface?!l}", (), {"interface": "Ethernet1"}, "ethernet1", id="optional_field_with_existing_arg_and_lower"),
    # positional fields with lower
    pytest.param("{!l}", ("ETHERNET1",), {}, "ethernet1", id="positional_field_with_existing_arg_and_lower"),
    pytest.param("{?!l}", (), {}, "", id="positional_optional_field_with_missing_arg_and_lower"),
    pytest.param("{?!l}", (None,), {}, "", id="positional_optional_field_with_none_arg_and_lower"),
    pytest.param("{?!l}", ("ETHERNET1",), {}, "ethernet1", id="positional_optional_field_with_existing_arg_and_lower"),
    # named fields with title
    pytest.param("{interface!t}", (), {"interface": "ETHERNET1"}, "Ethernet1", id="field_with_existing_arg_and_title"),
    pytest.param("{interface?!t}", (), {}, "", id="optional_field_with_missing_arg_and_title"),
    pytest.param("{interface?!t}", (), {"interface": None}, "", id="optional_field_with_none_arg_and_title"),
    pytest.param("{interface?!t}", (), {"interface": "ETHERNET1"}, "Ethernet1", id="optional_field_with_existing_arg_and_title"),
    # positional fields with title
    pytest.param("{!t}", ("ETHERNET1",), {}, "Ethernet1", id="positional_field_with_existing_arg_and_title"),
    pytest.param("{?!t}", (), {}, "", id="positional_optional_field_with_missing_arg_and_title"),
    pytest.param("{?!t}", (None,), {}, "", id="positional_optional_field_with_none_arg_and_title"),
    pytest.param("{?!t}", ("ETHERNET1",), {}, "Ethernet1", id="positional_optional_field_with_existing_arg_and_title"),
    # named fields with short interface name (!c conversion)
    pytest.param("{interface!c}", (), {"interface": "Ethernet2"}, "Et2", id="field_with_ethernet_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Ethernet 2"}, "Et2", id="field_with_ethernet_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Ethernet 2/2/2"}, "Et2", id="field_with_ethernet_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Port-channel20"}, "Po20", id="field_with_portchannel_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Port-channel20.200"}, "Po20.200", id="field_with_portchannel_subinterface_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Vlan100"}, "Vl100", id="field_with_vlan_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Loopback0"}, "Lo0", id="field_with_loopback_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "Tunnel1"}, "Tu1", id="field_with_tunnel_and_compact"),
    pytest.param("{interface!c}", (), {"interface": "GigabitEthernet1"}, "GigabitEthernet1", id="field_with_non_matching_interface_and_compact"),
    pytest.param("{interface?!c}", (), {}, "", id="optional_field_with_missing_arg_and_compact"),
    pytest.param("{interface?!c}", (), {"interface": None}, "", id="optional_field_with_none_arg_and_compact"),
    pytest.param("{interface?!c}", (), {"interface": "Ethernet1"}, "Et1", id="optional_field_with_existing_arg_and_compact"),
    # positional fields with short interface name (!c conversion)
    pytest.param("{!c}", ("Ethernet1",), {}, "Et1", id="positional_field_with_ethernet_and_compact"),
    pytest.param("{?!c}", (), {}, "", id="positional_optional_field_with_missing_arg_and_compact"),
    pytest.param("{?!c}", (None,), {}, "", id="positional_optional_field_with_none_arg_and_compact"),
    pytest.param("{?!c}", ("Ethernet1",), {}, "Et1", id="positional_optional_field_with_existing_arg_and_compact"),
]


SAFETY_TESTS = [
    # (<format_string>, <args ()>, <kwargs {}>)
    pytest.param("{foo.__class__.__name__}", (), {"foo": "bar"}, id="kwarg_dunder"),
    pytest.param("{_foo}", (), {"_foo": "bar"}, id="kwarg_private"),
    pytest.param("{foo._private}", (), {"foo": DummyClass()}, id="kwarg_private_attribute"),
    pytest.param("{0.__class__.__name__}", ("foo",), {}, id="arg_dunder"),
    pytest.param("{0._private}", (DummyClass(),), {}, id="arg_private_attribute"),
]


class TestAvdStringFormatter:
    @pytest.mark.parametrize(("format_string", "args", "kwargs", "expected_output"), FORMAT_STRING_TESTS)
    def test_avd_formatter(self, format_string: str, args: tuple, kwargs: dict, expected_output: list) -> None:
        resp = AvdStringFormatter().format(format_string, *args, **kwargs)
        assert resp == expected_output

    @pytest.mark.parametrize(("format_string", "args", "kwargs"), SAFETY_TESTS)
    def test_avd_formatter_safety(self, format_string: str, args: tuple, kwargs: dict) -> None:
        with pytest.raises(ValueError, match=r"Unsupported field name '.+'. Avoid (attributes|keys) starting with underscore."):
            AvdStringFormatter().format(format_string, *args, **kwargs)
