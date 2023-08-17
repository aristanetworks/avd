# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

collection_dir = Path(__file__).parents[3]
DEFAULT_SCHEMAS = {
    "avd_meta_schema": collection_dir.joinpath("plugins", "plugin_utils", "schema", "avd_meta_schema.json"),
    "eos_cli_config_gen": collection_dir.joinpath("roles", "eos_cli_config_gen", "schemas", "eos_cli_config_gen.schema.yml"),
    "eos_designs": collection_dir.joinpath("roles", "eos_designs", "schemas", "eos_designs.schema.yml"),
}
