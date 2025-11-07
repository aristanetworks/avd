# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd_utils.validation import Issue, Value, Violation, validate_json


@pytest.mark.usefixtures("init_store")
def test_validate_json() -> None:
    validation_result = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")

    violations = iter(validation_result.violations)
    feedback = next(violations)
    assert feedback.path == ["ethernet_interfaces", "2"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.MissingRequiredKey)
    assert feedback.issue._0.key == "name"
    feedback = next(violations)
    assert feedback.path == ["ethernet_interfaces", "0", "name"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.ValueNotUnique)
    assert feedback.issue._0.other_path == ["ethernet_interfaces", "1", "name"]
    feedback = next(violations)
    assert feedback.path == ["ethernet_interfaces", "1", "name"]
    assert isinstance(feedback.issue, Issue.Validation)
    assert isinstance(feedback.issue._0, Violation.ValueNotUnique)
    assert feedback.issue._0.other_path == ["ethernet_interfaces", "0", "name"]

    coercions = iter(validation_result.coercions)
    feedback = next(coercions)
    assert feedback.path == ["avd_data_validation_mode"]
    assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    feedback = next(coercions)
    assert feedback.path == ["config_end"]
    assert isinstance(feedback.issue, Issue.DefaultValueInserted)
    feedback = next(coercions)
    assert feedback.path == ["ethernet_interfaces", "0", "description"]
    assert isinstance(feedback.issue, Issue.Coercion)
    assert isinstance(feedback.issue._0.found, Value.Int)
    assert feedback.issue._0.found._0 == 12345
    assert isinstance(feedback.issue._0.made, Value.Str)
    assert feedback.issue._0.made._0 == "12345"
    feedback = next(coercions)
    feedback = next(coercions)
    feedback = next(coercions)
    feedback = next(coercions)
    feedback = next(coercions)
    feedback = next(coercions)
    assert feedback.path == ["transceiver_qsfp_default_mode_4x10"]
    assert isinstance(feedback.issue, Issue.DefaultValueInserted)
