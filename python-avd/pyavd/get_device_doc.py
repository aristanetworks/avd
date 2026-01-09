# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd.api.schemas import EOSConfig


def get_device_doc(structured_config: EOSConfig | dict, add_md_toc: bool = False) -> str:
    """
    Render and return the device documentation using AVD eos_cli_config_gen templates.

    Args:
        structured_config:
            EOSConfig instance or dictionary with the validated structured configuration.

            - Preferably use the EOSConfig instance returned from `pyavd.get_device_structured_config`.
            - Alternatively variables could be validated and loaded into EOSConfig using `pyavd.load_eos_config`.
            - Finally, for backwards compatibility, variables can be given as a dictionary,
              which should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`,
                which will return the data as a JSON string in the 'validated_data' attribute.
                The JSON string should be loaded into a dictionary before calling this function.

        add_md_toc:
            Add a table of contents for markdown headings.

    Returns:
        Device documentation in Markdown format.
    """
    from .api.schemas import EOSConfig  # noqa: PLC0415
    from .constants import EOS_CLI_CONFIG_GEN_JINJA2_DOCUMENTAITON_TEMPLATE, EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH  # noqa: PLC0415
    from .j2filters import add_md_toc as filter_add_md_toc  # noqa: PLC0415
    from .templater import Templar  # noqa: PLC0415

    if isinstance(structured_config, EOSConfig):
        structured_config = structured_config._as_dict()

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    result: str = templar.render_template_from_file(template_file=EOS_CLI_CONFIG_GEN_JINJA2_DOCUMENTAITON_TEMPLATE, template_vars=structured_config)
    if add_md_toc:
        return filter_add_md_toc(result, skip_lines=3)

    return result
