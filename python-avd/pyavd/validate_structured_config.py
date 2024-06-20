# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .validation_result import ValidationResult

eos_cli_config_gen_schema_tools = None


def validate_structured_config(structured_config: dict) -> ValidationResult:
    """
    Validate structured config according the `eos_cli_config_gen` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        structured_config: Dictionary with structured configuration.

    Returns:
        Validation result object with any validation errors or deprecation warnings.
    """
    # pylint: disable=import-outside-toplevel
    from .avd_schema_tools import AvdSchemaTools
    from .constants import EOS_CLI_CONFIG_GEN_SCHEMA_ID

    # pylint: enable=import-outside-toplevel
    # Initialize a global instance of eos_cli_config_gen_schema_tools
    global eos_cli_config_gen_schema_tools
    if eos_cli_config_gen_schema_tools is None:
        eos_cli_config_gen_schema_tools = AvdSchemaTools(schema_id=EOS_CLI_CONFIG_GEN_SCHEMA_ID)

    # Inplace conversion of data
    deprecation_warnings = eos_cli_config_gen_schema_tools.convert_data(structured_config)

    # Validate input data
    validation_result = eos_cli_config_gen_schema_tools.validate_data(structured_config)
    validation_result.deprecation_warnings.extend(deprecation_warnings)
    return validation_result
