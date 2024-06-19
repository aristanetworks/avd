# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

RUNNING_FROM_SRC = Path(__file__).parent.joinpath("running_from_src.txt").exists()
EOS_CLI_CONFIG_GEN_SCHEMA_ID = "eos_cli_config_gen"
EOS_DESIGNS_SCHEMA_ID = "eos_designs"
JINJA2_CONFIG_TEMPLATE = "eos-intended-config.j2"
JINJA2_DOCUMENTAITON_TEMPLATE = "eos-device-documentation.j2"
JINJA2_EXTENSIONS = ["jinja2.ext.loopcontrols", "jinja2.ext.do", "jinja2.ext.i18n"]
JINJA2_PRECOMPILED_TEMPLATE_PATH = Path(__file__).parent.joinpath("_eos_cli_config_gen/j2templates", "compiled_templates")
JINJA2_TEMPLATE_PATHS = [Path(__file__).parent.joinpath("_eos_cli_config_gen/j2templates")]
