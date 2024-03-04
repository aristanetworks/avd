# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

REPO_ROOT = Path(__file__).parents[3]
EOS_DESIGNS_SCHEMA_DIR = REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_designs/schemas")
EOS_DESIGNS_SCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.yml")
EOS_DESIGNS_FRAGMENTS_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("schema_fragments")
EOS_DESIGNS_PICKLED_SCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.pickle")
EOS_DESIGNS_JSONSCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.jsonschema.json")

EOS_CLI_CONFIG_GEN_SCHEMA_DIR = REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/schemas")
EOS_CLI_CONFIG_GEN_SCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.yml")
EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("schema_fragments")
EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.pickle")
EOS_CLI_CONFIG_GEN_JSONSCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.jsonschema.json")

METASCHEMA_DIR = REPO_ROOT.joinpath("ansible_collections/arista/avd/plugins/plugin_utils/schema")
METASCHEMA_PATH = METASCHEMA_DIR.joinpath("avd_meta_schema.json")
METASCHEMA_PICKLED_SCHEMA_PATH = METASCHEMA_DIR.joinpath("avd_meta_schema.pickle")

SCHEMA_PATHS = {
    "avd_meta_schema": METASCHEMA_PATH,
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_SCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_SCHEMA_PATH,
}
SCHEMA_FRAGMENTS_PATHS = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH,
    "eos_designs": EOS_DESIGNS_FRAGMENTS_PATH,
}
PICKLED_SCHEMAS = {
    "avd_meta_schema": METASCHEMA_PICKLED_SCHEMA_PATH,
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_PICKLED_SCHEMA_PATH,
}
JSONSCHEMA_PATHS = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_JSONSCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_JSONSCHEMA_PATH,
}
LICENSE_HEADER = REPO_ROOT.joinpath("development/license-short.txt").read_text(encoding="UTF-8").strip()
