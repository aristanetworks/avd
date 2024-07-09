# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .validation_result import ValidationResult

eos_designs_schema_tools = None


def validate_inputs(inputs: dict) -> ValidationResult:
    """
    Validate input variables according to the `eos_designs` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        inputs: Dictionary with inputs for "eos_designs".

    Returns:
        Validation result object with any validation errors or deprecation warnings.
    """
    # pylint: disable=import-outside-toplevel
    from ._eos_designs.shared_utils import SharedUtils
    from .avd_schema_tools import AvdSchemaTools
    from .constants import EOS_DESIGNS_SCHEMA_ID

    # pylint: enable=import-outside-toplevel
    # Initialize a global instance of eos_designs_schema_tools
    global eos_designs_schema_tools
    if eos_designs_schema_tools is None:
        eos_designs_schema_tools = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)

    # Initialize SharedUtils class to fetch default variables below.
    shared_utils = SharedUtils(hostvars=inputs, templar=None)

    # Insert dynamic keys into the input data if not set.
    # These keys are required by the schema, but the default values are set inside shared_utils.
    inputs.setdefault("node_type_keys", shared_utils.node_type_keys)
    inputs.setdefault("connected_endpoints_keys", shared_utils.connected_endpoints_keys)
    inputs.setdefault("network_services_keys", shared_utils.network_services_keys)

    # Inplace conversion of data
    deprecation_warnings = eos_designs_schema_tools.convert_data(inputs)

    # Validate input data
    validation_result = eos_designs_schema_tools.validate_data(inputs)
    validation_result.deprecation_warnings.extend(deprecation_warnings)
    return validation_result
