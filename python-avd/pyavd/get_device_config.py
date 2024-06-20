# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


def get_device_config(structured_config: dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        structured_config: Dictionary with structured configuration.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

    Returns:
        Device configuration in EOS CLI format.
    """
    # pylint: disable=import-outside-toplevel
    from .constants import JINJA2_CONFIG_TEMPLATE
    from .templater import Templar

    # pylint: enable=import-outside-toplevel

    templar = Templar()
    return templar.render_template_from_file(JINJA2_CONFIG_TEMPLATE, structured_config)
