# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

from yaml import safe_load

EOS_DESIGNS_SCHEMA_PATH = Path(__file__).parents[1].joinpath("ansible_collections/arista/avd/roles/eos_designs/schemas/eos_designs.schema.yml")
EOS_CLI_CONFIG_GEN_SCHEMA_PATH = (
    Path(__file__).parents[1].joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/schemas/eos_cli_config_gen.schema.yml")
)

with open(EOS_CLI_CONFIG_GEN_SCHEMA_PATH, encoding="UTF-8") as file:
    EOS_CLI_CONFIG_GEN_SCHEMA = safe_load(file)

with open(EOS_DESIGNS_SCHEMA_PATH, encoding="UTF-8") as file:
    EOS_DESIGNS_SCHEMA = safe_load(file)

STORE = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_SCHEMA,
    "eos_designs": EOS_DESIGNS_SCHEMA,
}
