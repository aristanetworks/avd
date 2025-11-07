# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd_utils.validation import Issue, Value, Violation, get_validated_data


@pytest.mark.usefixtures("init_store")
def test_get_validated_data() -> None:
    coercion_and_validation_result = get_validated_data('{"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}]}', "eos_cli_config_gen")
    validated_data = coercion_and_validation_result.validated_data
    assert validated_data == (
        '{"ethernet_interfaces":[{"name":"Ethernet1","description":"12345","ospf_authentication_key_type":"7"}],"avd_data_validation_mode":"error",'
        '"config_end":false,"generate_default_config":false,"generate_device_documentation":true,"transceiver_qsfp_default_mode_4x10":true}'
    )
    validation_result = coercion_and_validation_result.validation_result
    assert len(validation_result.violations) == 0

    coercion_feedbacks = list(filter(lambda feedback: (isinstance(feedback.issue, Issue.Coercion)), validation_result.coercions))
    assert len(coercion_feedbacks) == 1
    feedback = coercion_feedbacks[0]
    assert feedback.path == ["ethernet_interfaces", "0", "description"]
    assert isinstance(feedback.issue, Issue.Coercion)
    assert isinstance(feedback.issue._0.found, Value.Int)
    assert feedback.issue._0.found._0 == 12345
    assert isinstance(feedback.issue._0.made, Value.Str)
    assert feedback.issue._0.made._0 == "12345"


@pytest.mark.usefixtures("init_store")
def test_get_validated_data_not_ok() -> None:
    coercion_and_validation_result = get_validated_data('{"ethernet_interfaces": [{"name": "Ethernet1", "unknown": 12345}]}', "eos_cli_config_gen")
    validated_data = coercion_and_validation_result.validated_data
    assert validated_data == (
        '{"ethernet_interfaces":[{"name":"Ethernet1","unknown":12345,"ospf_authentication_key_type":"7"}],"avd_data_validation_mode":"error",'
        '"config_end":false,"generate_default_config":false,"generate_device_documentation":true,"transceiver_qsfp_default_mode_4x10":true}'
    )
    validation_result = coercion_and_validation_result.validation_result
    assert len(validation_result.violations) == 1
    feedback = validation_result.violations[0]
    assert feedback.path == ["ethernet_interfaces", "0", "unknown"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.UnexpectedKey)
