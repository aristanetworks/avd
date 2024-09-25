#!/usr/bin/env python3
# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, str(Path(__file__).parent.parent))

from pyavd.constants import (
    EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_TEMPLATE_PATH,
)
from pyavd.templater import Templar

templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH])
templar.compile_templates_in_paths(
    precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH]
)
templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])
templar.compile_templates_in_paths(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])
