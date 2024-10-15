#!/usr/bin/env python3
# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from sys import path, argv

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, str(Path(__file__).parent.parent))

from pyavd.constants import (
    EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_TEMPLATE_PATH,
)
from pyavd.templater import Templar


def main(log_level: int = logging.INFO) -> None:
    """
    Main entrypoint for the script.

    It combines the schema fragments, and rebuild the pickled schemas.

    """
    logging.basicConfig(level=log_level, format="[compile_templates] - %(message)s")

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(
        precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH]
    )
    templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])


if __name__ == "__main__":
    log_level_str = argv[1].upper() if len(argv) > 1 else "INFO"
    log_level = logging.getLevelName(log_level_str)
    main(log_level)
