from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

import pytest
import yaml

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AvdValidationError
from ansible_collections.arista.avd.plugins.plugin_utils.schema.avdschema import AvdSchema

script_dir = os.path.dirname(__file__)
with open(f"{script_dir}/formats.schema.yml", "r", encoding="utf-8") as schema_file:
    formats_schema = yaml.load(schema_file, Loader=yaml.SafeLoader)

avdschema = AvdSchema(formats_schema)

VALID_VALUES = [
    ("string_format_ipv4", "10.10.10.10"),
    ("string_format_ipv4_cidr", "10.10.10.10/24"),
    ("string_format_ipv6", "fe80::1"),
    ("string_format_ipv6_cidr", "cafe::666/64"),
    ("string_format_ip", "10.10.10.10"),
    ("string_format_ip", "fe80::1"),
    ("string_format_cidr", "10.10.10.10/24"),
    ("string_format_cidr", "cafe::666/64"),
    ("string_format_mac", "00:00:00:00:00:00"),
    ("string_format_regex_interface", "Ethernet1/12/4.123"),
]

INVALID_VALUES = [
    ("string_format_ipv4", "10.10.10."),
    ("string_format_ipv4", "10.10.10.10/24"),
    ("string_format_ipv4_cidr", "10.10.10.10"),
    ("string_format_ipv4_cidr", "10.10.10.10/"),
    ("string_format_ipv4_cidr", "fe80::1/128"),
    ("string_format_ipv6", "fe80::1/64"),
    ("string_format_ipv6", "fe80:1"),
    ("string_format_ipv6_cidr", "cafe::666"),
    ("string_format_ipv6_cidr", "cafe::666/1000"),
    ("string_format_ip", "www.arista.com"),
    ("string_format_ip", "10.10.10.10/32"),
    ("string_format_cidr", "10.10.10.10/255.255.255.0"),
    ("string_format_cidr", "10.10.10.10 255.255.255.0"),
    ("string_format_mac", "0000.0000.0000"),
    ("string_format_regex_interface", "Port-Channel1.123"),
    ("string_format_regex_interface", "eth1"),
    ("string_format_regex_interface", "eth1"),
    ("string_format_regex_interface", "ethernet1"),
]


class TestAvdSchemaFormats:
    @pytest.mark.parametrize("KEY, VALUE", VALID_VALUES)
    def test_avd_schema_format_with_valid_value(self, KEY, VALUE):
        VALID_DATA = {KEY: VALUE}
        try:
            for validation_error in avdschema.validate(VALID_DATA):
                assert False, f"Validation Error '{validation_error.message}' returned"
        except Exception as e:
            assert False, f"avdschema.validate({VALID_DATA}) {e}"

        assert avdschema.is_valid(VALID_DATA)

    @pytest.mark.parametrize("KEY, VALUE", INVALID_VALUES)
    def test_avd_schema_format_with_invalid_value(self, KEY, VALUE):
        INVALID_DATA = {KEY: VALUE}
        try:
            for validation_error in avdschema.validate(INVALID_DATA):
                try:
                    assert isinstance(validation_error, AvdValidationError)
                except AssertionError:
                    assert False, f"avdschema.validate({INVALID_DATA}) raised an unexpected exception: {validation_error}"
        except Exception as e:
            assert False, f"avdschema.validate({INVALID_DATA}) raised an exception: {e}"
