# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd_utils.validation import get_validated_data


@pytest.mark.usefixtures("init_store")
def test_get_validated_data() -> None:
    expected_coercions: list[tuple[list[str], str]] = [(["ethernet_interfaces", "0", "description"], 'Coerced value from 12345 to "12345".')]

    coercion_and_validation_result = get_validated_data('{"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}]}', "eos_cli_config_gen")
    validated_data = coercion_and_validation_result.validated_data
    assert validated_data == (
        '{"ethernet_interfaces":[{"name":"Ethernet1","description":"12345","ospf_authentication_key_type":"7"}],"avd_data_validation_mode":"error",'
        '"config_end":false,"generate_default_config":false,"generate_device_documentation":true,"transceiver_qsfp_default_mode_4x10":true}'
    )
    validation_result = coercion_and_validation_result.validation_result
    assert len(validation_result.violations) == 0

    assert len(validation_result.coercions) == len(expected_coercions)
    for coercion in validation_result.coercions:
        assert (coercion.path, coercion.message) in expected_coercions, f"Coercion not expected: {coercion.path}, {coercion.message}"


@pytest.mark.usefixtures("init_store")
def test_get_validated_data_not_ok() -> None:
    expected_violations: list[tuple[list[str], str]] = [
        (["ethernet_interfaces", "0", "unknown"], "Invalid key."),
    ]

    get_validated_data_result = get_validated_data('{"ethernet_interfaces": [{"name": "Ethernet1", "unknown": 12345}]}', "eos_cli_config_gen")
    validated_data = get_validated_data_result.validated_data
    assert validated_data is None

    validation_result = get_validated_data_result.validation_result
    assert len(validation_result.violations) == len(expected_violations)
    for violation in validation_result.violations:
        assert (violation.path, violation.message) in expected_violations, f"Violation not expected: {violation.path}, {violation.message}"
