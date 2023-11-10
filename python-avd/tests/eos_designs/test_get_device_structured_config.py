# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_structured_config, validate_inputs


def test_get_device_structured_config(hostname: str, all_inputs: dict, avd_facts: dict, structured_configs: dict):
    """
    Test get_device_structured_config
    """
    inputs = all_inputs[hostname]

    # run validation on inputs to ensure it is converted
    validate_inputs(inputs)

    expected_structured_config = structured_configs[hostname]
    structured_config = get_device_structured_config(hostname, inputs, avd_facts)

    assert isinstance(structured_config, dict)
    assert hostname == structured_config["hostname"]
    assert expected_structured_config == structured_config
