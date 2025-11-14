# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd_utils.validation import validate_json


@pytest.mark.usefixtures("init_store")
def test_validate_json() -> None:
    expected_errors: list[tuple[list[str], str]] = [
        (["ethernet_interfaces", "2"], "Missing the required key 'name'."),
        (["ethernet_interfaces", "0", "name"], "The value is not unique among similar items. Conflicting item: ethernet_interfaces[1].name"),
        (["ethernet_interfaces", "1", "name"], "The value is not unique among similar items. Conflicting item: ethernet_interfaces[0].name"),
    ]
    validation_result = validate_json('{"ethernet_interfaces": [{"name": "Ethernet1", "description": 12345}, {"name": "Ethernet1"}, {}]}', "eos_cli_config_gen")

    assert len(validation_result.errors) == len(expected_errors)
    for error in validation_result.errors:
        assert (error.path, error.message) in expected_errors, f"Error not expected: {error.path}, {error.message}"

    assert len(validation_result.infos) == 0
