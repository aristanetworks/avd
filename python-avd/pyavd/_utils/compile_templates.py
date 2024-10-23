# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging

from pyavd.constants import (
    EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_TEMPLATE_PATH,
    RUNNING_FROM_SRC,
)
from pyavd.templater import Templar

from .hash_dir import check_hash

LOGGER = logging.getLogger(__name__)


def compile_eos_cli_config_gen_templates() -> None:
    """TODO."""
    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(
        precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH]
    )


def compile_eos_designs_templates() -> None:
    """TODO."""
    templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])


def _check_eos_designs_templates() -> None:
    """TODO.

    Templates
    """
    if not RUNNING_FROM_SRC:
        return

    LOGGER.info("pyavd running from source detected, checking eos_designs templates for any changes...")
    dir_path = EOS_DESIGNS_JINJA2_TEMPLATE_PATH

    changed, new_hash = check_hash(dir_path)
    if changed:
        LOGGER.info("Recompiling eos_designs templates...")
        compile_eos_designs_templates()
        with (dir_path / ".hash").open("w") as fd:
            fd.write(new_hash)


def _check_eos_cli_config_gen_templates() -> None:
    """TODO.

    Templates
    """
    if not RUNNING_FROM_SRC:
        return

    LOGGER.info("pyavd running from source detected, checking eos_cli_config_gen templates for any changes...")
    dir_path = EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH

    changed, new_hash = check_hash(dir_path)
    if changed:
        LOGGER.info("Recompiling eos_cli_config_gen templates...")
        compile_eos_cli_config_gen_templates()
        with (dir_path / ".hash").open("w") as fd:
            fd.write(new_hash)


def check_templates() -> None:
    """TODO."""
    _check_eos_designs_templates()
    _check_eos_cli_config_gen_templates()
