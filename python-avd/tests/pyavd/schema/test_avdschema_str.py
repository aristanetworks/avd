# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from itertools import product
from pathlib import Path
from sys import path
from typing import Any

import pytest

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[3]))

from pyavd._errors import AvdValidationError
from pyavd._schema.avdschema import AvdSchema
from pyavd.validate_inputs import validate_inputs

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
            "dynamic_valid_values": ["dynamic.valid_value"],
            "pattern": "[abf14t].*",
            "required": True,
            "description": "Some string",
            "display_name": "String",
        },
        "dynamic": {"type": "list", "items": {"type": "dict", "keys": {"valid_value": {"type": "str"}}}},
    },
}

# f-string-based pattern is suggested to have a simple way of extending test coverage to new keys (like mlag_interfaces which is not patterned right now)
NODE_CONFIG_SCHEMA_SECTION = "{{'fabric_name': 'pytest_fabric', 'l3leaf': {{'defaults': {{'{schema_key_name}': ['{schema_key_value}']}}}}}}"


@pytest.fixture(scope="module")
def avd_schema() -> AvdSchema:
    return AvdSchema(TEST_SCHEMA)


@pytest.mark.parametrize(
    ("test_value", "dynamic_valid_values", "expected_errors", "expected_error_messages"),
    [
        pytest.param("foo", None, None, None, id="ok-no-coerce-foo"),
        pytest.param("FoO", None, None, None, id="ok-to-lower-foo"),
        pytest.param(True, None, None, None, id="ok-coerce-bool-to-str-to-lower-true"),
        pytest.param(
            False,
            None,
            (AvdValidationError,),
            (
                "Validation Error: [test_value] 'false' is not one of ['a', 'foo', 'zoo', 'baaar', '1.0', '42', 'true']",
                "Validation Error: [test_value] The value is longer (5) than the allowed maximum of 4.",
            ),
            id="err-coerce-bool-to-str-to-lower-invalid-value-false",
        ),
        pytest.param(42, None, None, None, id="ok-coerce-int-to-str-42"),
        pytest.param(1.000, None, None, None, id="ok-coerce-float-to-str-1.0"),
        pytest.param(
            None, None, (AvdValidationError,), ("Validation Error: [] Required key 'test_value' is not set in dict.",), id="err-missing-required-value"
        ),
        pytest.param([], None, (AvdValidationError,), ("Validation Error: [test_value] Invalid type 'list'. Expected a 'str'.",), id="err-invalid-type-list"),
        pytest.param(
            "a",
            None,
            (AvdValidationError,),
            ("Validation Error: [test_value] The value is shorter (1) than the allowed minimum of 2.",),
            id="err-below-min-length-1",
        ),
        pytest.param(
            "baaar",
            None,
            (AvdValidationError,),
            ("Validation Error: [test_value] The value is longer (5) than the allowed maximum of 4.",),
            id="err-above-max-length-5",
        ),  # Valid but below min length.
        pytest.param(
            22,
            None,
            (AvdValidationError,),
            (
                "Validation Error: [test_value] '22' is not one of ['a', 'foo', 'zoo', 'baaar', '1.0', '42', 'true']",
                "Validation Error: [test_value] The value '22' is not matching the pattern '[abf14t].*'.",
            ),
            id="err-coerce-int-to-str-invalid-value-22",
        ),
        pytest.param(
            "zoo",
            None,
            (AvdValidationError,),
            ("Validation Error: [test_value] The value 'zoo' is not matching the pattern '[abf14t].*'.",),
            id="err-not-matching-pattern-zoo",
        ),
        pytest.param(
            "aaaa",
            ["aaaa"],
            None,
            None,
            id="ok-dynamic-valid-value-aaaa",
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


@pytest.mark.parametrize(
    ("schema_format", "test_value", "expected_errors", "expected_error_messages"),
    [
        pytest.param("ipv4", "10.10.10.10", None, None, id="ok-ipv4"),  # TODO: Implement proper validation
        pytest.param("ipv4_cidr", "10.10.10.10/24", None, None, id="ok-ipv4-cidr"),  # TODO: Implement proper validation
        pytest.param("ipv6", "fe80::1", None, None, id="ok-ipv6"),  # TODO: Implement proper validation
        pytest.param("ipv6_cidr", "fe80::1/64", None, None, id="ok-ipv6-cidr"),  # TODO: Implement proper validation
        pytest.param("ip", "10.10.10.10", None, None, id="ok-ip-10-10-10-10"),  # TODO: Implement proper validation
        pytest.param("ip", "fe80::1", None, None, id="ok-ip-fe80-1"),  # TODO: Implement proper validation
        pytest.param("cidr", "10.10.10.10/24", None, None, id="ok-cidr-10-10-10-10-24"),  # TODO: Implement proper validation
        pytest.param("cidr", "fe80::1/64", None, None, id="ok-cidr-fe80-1-64"),  # TODO: Implement proper validation
        pytest.param("ip_pool", "10.10.10.0/24, 2001:db8::/64, 10.10.10.10-10.10.10.20, 2001:db8::-2001:db8::ffff", None, None, id="ok-ip-pool"),
        pytest.param(
            "ip_pool",
            "foo",
            (AvdValidationError,),
            (
                (
                    "Validation Error: [] The value 'foo' is not a valid IP pool (Expecting one or more comma separated prefixes "
                    "(like 10.10.10.0/24 or 2001:db8::/64) or ranges (like 10.10.10.10-10.10.10.20 or 2001:db8::-2001:db8::ffff)."
                ),
            ),
            id="err-invalid-ip-pool-foo",
        ),
        pytest.param("ipv4_pool", "10.10.10.0/24, 10.10.10.10-10.10.10.20", None, None, id="ok-ipv4-pool"),
        pytest.param(
            "ipv4_pool",
            "foo",
            (AvdValidationError,),
            (
                (
                    "Validation Error: [] The value 'foo' is not a valid IPv4 pool (Expecting one or more comma separated prefixes "
                    "(like 10.10.10.0/24) or ranges (like 10.10.10.10-10.10.10.20)."
                ),
            ),
            id="err-invalid-ipv4-pool-foo",
        ),
        pytest.param("ipv6_pool", "2001:db8::/64, 2001:db8::-2001:db8::ffff", None, None, id="ok-ipv6-pool"),
        pytest.param(
            "ipv6_pool",
            "foo",
            (AvdValidationError,),
            (
                (
                    "Validation Error: [] The value 'foo' is not a valid IPv6 pool (Expecting one or more comma separated prefixes "
                    "(like 2001:db8::/64) or ranges (like 2001:db8::-2001:db8::ffff)."
                ),
            ),
            id="err-invalid-ipv6-pool-foo",
        ),
        pytest.param("mac", "aaaa:bbbb:cccc", None, None, id="ok-mac-4-colon"),
        pytest.param("mac", "aaaa.bbbb.cccc", None, None, id="ok-mac-4-dot"),
        pytest.param("mac", "aa:aa:bb:bb:cc:cc", None, None, id="ok-mac-2-colon"),
        pytest.param(
            "mac",
            "foo",
            (AvdValidationError,),
            (("Validation Error: [] The value 'foo' is not a valid MAC address (Expecting bytes separated by colons like 01:23:45:67:89:AB)."),),
            id="err-invalid-mac-foo",
        ),
        pytest.param("invalid_format", "foo", None, None, id="ok-invalid-format"),  # TODO: Consider catching and raising NotImplementedErr for invalid format.
    ],
)
def test_str_format(
    schema_format: str, test_value: str, expected_errors: tuple[type[AvdValidationError], ...] | None, expected_error_messages: tuple[str, ...] | None
) -> None:
    schema = {
        "type": "str",
        "format": schema_format,
    }
    avd_schema = AvdSchema(schema)

    validation_errors = list(avd_schema.validate(test_value))
    if expected_errors and expected_error_messages:
        for validation_error in validation_errors:
            assert isinstance(validation_error, expected_errors)
            assert str(validation_error) in expected_error_messages
    else:
        # No errors expected.
        assert not validation_errors


# Helper function to generate possible valid Ethernet interface ranges
def generate_ethernet_range_patterns(max_depth: int = 5) -> list[str]:
    base_value = "Ethernet"
    seeds = ["1", "2,3", "4-5", "6,17-18"]
    pytest_params = []
    for length in range(1, max_depth + 1):
        pytest_params.extend(base_value + "/".join(combo) for combo in product(seeds, repeat=length))
    pytest_params.sort(key=lambda s: (len(s.split("/")), s))
    # Append static patterns testing sequence inside each item
    pytest_params.append("Ethernet1,2-3,4-5/6-7/8-9, Ethernet7,8-9,10/1-3")
    return pytest_params


# Allows a simple coverage adjustment for other schema paths that should use the same patterns in the future (like default_interfaces[].uplink_interfaces)
@pytest.mark.parametrize(
    ("raw_schema_section"),
    [
        pytest.param(NODE_CONFIG_SCHEMA_SECTION, id="NODE_CONFIG_INTERFACES"),
    ],
)
# Allows a simple coverage adjustment for other schema paths that should use the same patterns in the future (like l3leafs.defaults.mlag_interfaces)
@pytest.mark.parametrize(
    ("schema_key_name"),
    [
        pytest.param("uplink_interfaces", id="UPLINK_INTERFACES"),
    ],
)
@pytest.mark.parametrize(("schema_key_value"), generate_ethernet_range_patterns())
def test_node_config_valid_ethernet_ranges(raw_schema_section: str, schema_key_name: str, schema_key_value: str) -> None:
    """Test matching of the valid Ethernet interface ranges by the patterns of the target schema paths."""
    raw_inputs_under_test = raw_schema_section.format(schema_key_name=schema_key_name, schema_key_value=schema_key_value).replace("'", '"')
    inputs_under_test = json.loads(raw_inputs_under_test)

    validated_data_result = validate_inputs(inputs_under_test)

    assert not validated_data_result.validation_result.violations


@pytest.mark.parametrize(
    ("raw_schema_section"),
    [
        pytest.param(NODE_CONFIG_SCHEMA_SECTION, id="NODE_CONFIG_INTERFACES"),
    ],
)
@pytest.mark.parametrize(
    ("schema_key_name"),
    [
        pytest.param("uplink_interfaces", id="UPLINK_INTERFACES"),
    ],
)
@pytest.mark.parametrize(
    ("schema_key_value"),
    [
        pytest.param("Ethernet1/", id="TRAILING_SLASH"),
        pytest.param("Ethernet1-", id="TRAILING_DASH"),
        pytest.param("Ethernet1,", id="TRAILING_COMMA"),
    ],
)
def test_node_config_invalid_ethernet_ranges(raw_schema_section: str, schema_key_name: str, schema_key_value: str) -> None:
    """Test matching of the invalid Ethernet interface ranges by the patterns of the target schema paths."""
    raw_inputs_under_test = raw_schema_section.format(schema_key_name=schema_key_name, schema_key_value=schema_key_value).replace("'", '"')
    inputs_under_test = json.loads(raw_inputs_under_test)

    validated_data_result = validate_inputs(inputs_under_test)

    # TODO: Remove 'not' once strict pattern validation is enforced. Items being tested here should cause validation failure.
    assert not validated_data_result.validation_result.violations
