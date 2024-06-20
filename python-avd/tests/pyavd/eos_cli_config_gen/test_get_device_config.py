# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_config, validate_structured_config


def test_get_device_config(hostname: str, all_inputs: dict, configs: dict):
    """
    Test get_device_config
    """

    structured_config: dict = all_inputs[hostname]
    expected_config: str = configs[hostname]

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    # assert f"hostname {hostname}\n" in eos_config

    assert device_config == expected_config
