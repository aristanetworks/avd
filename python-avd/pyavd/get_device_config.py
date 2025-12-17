# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd.api.schemas import EOSConfig


def get_device_config(structured_config: EOSConfig | dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        structured_config: EOSConfig instance or dictionary with the validated structured configuration.

    Returns:
        Device configuration in EOS CLI format.
    """
    from pyavd.api.schemas import EOSConfig  # noqa: PLC0415

    from .constants import EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH  # noqa: PLC0415
    from .templater import Templar  # noqa: PLC0415

    if isinstance(structured_config, EOSConfig):
        structured_config = structured_config._as_dict()

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    return templar.render_template_from_file(template_file=EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, template_vars=structured_config)
