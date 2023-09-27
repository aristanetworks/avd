# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd import get_device_config, validate_structured_config


def test_get_device_config(hostname: str, all_inputs: dict, structured_configs: dict, configs: dict):
    """
    Test get_device_config
    """

    # Loading inputs first and then updating structured config on top.
    # This is how Ansible behaves, so we need this to generate the same configs.
    # The underlying cause is eos_cli_config_gen inputs being set in eos_designs molecule vars,
    #   which are then _not_ included in the structured_config, hence lost unless we include the
    #   inputs as well.
    structured_config: dict = all_inputs[hostname]
    structured_config.update(structured_configs[hostname])
    expected_config: str = configs[hostname]

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    assert f"hostname {hostname}\n" in device_config
    assert device_config == expected_config
