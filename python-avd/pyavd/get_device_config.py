# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api.schemas import EOSConfig


def get_device_config(structured_config: EOSConfig | dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        structured_config:
            EOSConfig instance or dictionary with the validated structured configuration.

            - Preferably, use the EOSConfig instance returned from `pyavd.get_device_structured_config`.
            - Alternatively, for backwards compatibility, variables can be given as a dictionary,
              which should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`,
              and take the data from the 'validated_data' attribute.

    Returns:
        Device configuration in EOS CLI format.

    Notes:
        Currently the `get_device_config` and `get_device_doc` functions need the validated data as a dict,
        so they will dump the loaded class if given.
        For now it is more efficient to use the `validate_structured_config` function and give the returned dict
        to those functions instead of using the EOSConfig class.
        If you already have the EOSConfig instance loaded as returned from `get_device_structured_config`,
        you can just use that instance directly without further validation.
    """
    from .api.schemas import EOSConfig  # noqa: PLC0415
    from .constants import EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH  # noqa: PLC0415
    from .templater import Templar  # noqa: PLC0415

    if isinstance(structured_config, EOSConfig):
        structured_config = structured_config._as_dict()

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    return templar.render_template_from_file(template_file=EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, template_vars=structured_config)
