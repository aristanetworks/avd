# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from .avd_schema_tools import AvdSchemaTools
from .constants import EOS_CLI_CONFIG_GEN_SCHEMA_ID
from .validation_result import ValidationResult

eos_cli_config_gen_schema_tools = None


def validate_structured_config(structured_config: dict) -> ValidationResult:
    """
    Validate structured config according the `eos_cli_config_gen` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        structured_config: Dictionary with structured configuration.

    Returns:
        Instance of ValidationResult, where "failed" is True if data is not valid according to the schema
            and "errors" is a list of AvdValidationErrors containing schema violations.
    """

    # Initialize a global instance of eos_cli_config_gen_schema_tools
    global eos_cli_config_gen_schema_tools
    if eos_cli_config_gen_schema_tools is None:
        eos_cli_config_gen_schema_tools = AvdSchemaTools(schema_id=EOS_CLI_CONFIG_GEN_SCHEMA_ID)

    # Inplace conversion of data
    eos_cli_config_gen_schema_tools.convert_data(structured_config)

    # Validate input data
    return eos_cli_config_gen_schema_tools.validate_data(structured_config)
