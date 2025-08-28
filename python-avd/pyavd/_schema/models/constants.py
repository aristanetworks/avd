# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

EOS_CLI_CONFIG_GEN_ROLE_KEYS = {
    "eos_cli_config_gen_documentation",
    "avd_data_validation_mode",
    "custom_templates",
    "eos_cli_config_gen_configuration",
    "generate_device_documentation",
    "generate_default_config",
}
"""
Set of eos_cli_config_gen role keys.
Note that for now this is manually maintained but this shall change.
TODO: separate role inputs in their own schema.
TODO: some keys above (generate_device_documentation, generate_default_config) are deprecated in 6.0.0
      so should be removed from this sadly manually maintained set.
"""
EOS_CLI_CONFIG_GEN_INPUT_KEYS = set(EosCliConfigGen._fields.keys()) - EOS_CLI_CONFIG_GEN_ROLE_KEYS
"""Set of eos_cli_config_gen which are not role keys."""
