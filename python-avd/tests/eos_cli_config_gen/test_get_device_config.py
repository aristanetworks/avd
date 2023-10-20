# Copyright (c) 2023 Arista Networks, Inc.
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

    # Hack to insert newline if the config is empty.
    # This is to match the jinja generated output from Ansible, where Ansible has a special output function
    # adding this extra newline if the config is empty.
    if not device_config:
        device_config = "\n"

    assert device_config == expected_config
