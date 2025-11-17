# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd_utils.validation import validate_json


@pytest.mark.usefixtures("init_store")
def test_validate_json() -> None:
    expected_violations: list[tuple[list[str], str]] = [
        (["ethernet_interfaces", "2"], "Missing the required key 'name'."),
        (["ethernet_interfaces", "0", "name"], "The value is not unique among similar items. Conflicting item: ethernet_interfaces[1].name"),
        (["ethernet_interfaces", "1", "name"], "The value is not unique among similar items. Conflicting item: ethernet_interfaces[0].name"),
    ]
    validation_result = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")

    assert len(validation_result.violations) == len(expected_violations)
    for violation in validation_result.violations:
        assert (violation.path, violation.message) in expected_violations, f"Error not expected: {violation.path}, {violation.message}"

    assert len(validation_result.deprecations) == 0
