# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._cv.schema import CvDeploy
from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

EOS_CLI_CONFIG_GEN_ROLE_KEYS = {
    "avd_structured_config_file_format",
    "avd_vault_id",
    "custom_templates",
    "eos_cli_config_gen_configuration",
    "eos_cli_config_gen_custom_templates",
    "eos_cli_config_gen_documentation",
    "eos_cli_config_gen_read_structured_config_from_file",
    "eos_cli_config_gen_structured_config_file_format",
    "eos_cli_config_gen_validate_inputs_batch_size",
    "eos_cli_config_gen_vault_id",
    "read_structured_config_from_file",
}
"""
Set of eos_cli_config_gen role keys.
Note that for now this is manually maintained but this shall change.
TODO: separate role inputs in their own schema.
"""
EOS_CLI_CONFIG_GEN_INPUT_KEYS = set(EosCliConfigGen._fields.keys()) - EOS_CLI_CONFIG_GEN_ROLE_KEYS
"""Set of eos_cli_config_gen schema keys which are not role keys."""

CV_DEPLOY_INPUT_KEYS = set(CvDeploy._fields.keys())
"""Set of cv_deploy schema keys."""
