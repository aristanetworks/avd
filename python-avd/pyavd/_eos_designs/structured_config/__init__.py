# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap

from ..._utils import get, merge
from ...avd_schema_tools import AvdSchemaTools
from ..avdfacts import AvdFacts
from ..shared_utils import SharedUtils
from .base import AvdStructuredConfigBase
from .connected_endpoints import AvdStructuredConfigConnectedEndpoints
from .core_interfaces_and_l3_edge import AvdStructuredConfigCoreInterfacesAndL3Edge
from .custom_structured_configuration import AvdStructuredConfigCustomStructuredConfiguration
from .flows import AvdStructuredConfigFlows
from .inband_management import AvdStructuredConfigInbandManagement
from .metadata import AvdStructuredConfigMetadata
from .mlag import AvdStructuredConfigMlag
from .network_services import AvdStructuredConfigNetworkServices
from .overlay import AvdStructuredConfigOverlay
from .underlay import AvdStructuredConfigUnderlay

AVD_STRUCTURED_CONFIG_CLASSES = [
    AvdStructuredConfigBase,
    AvdStructuredConfigMlag,
    AvdStructuredConfigUnderlay,
    AvdStructuredConfigOverlay,
    AvdStructuredConfigCoreInterfacesAndL3Edge,
    AvdStructuredConfigNetworkServices,
    AvdStructuredConfigConnectedEndpoints,
    AvdStructuredConfigInbandManagement,
    # The Flows module must be rendered after others contributing interfaces,
    # since it parses those interfaces for sFlow or flow tracking (ipfix) config.
    AvdStructuredConfigFlows,
    # Metadata must be after anything else that can generate structured config, since CV tags can consume from structured config.
    AvdStructuredConfigMetadata,
    # The Custom Structured Configuration module must be rendered last,
    # since it parses all supported object looking for `struct_cfg`.
    AvdStructuredConfigCustomStructuredConfiguration,
]
"""
AVD_STRUCTURED_CONFIG contains a list of AvdStructuredConfig classes which generate the complete structured config.
The order is important, since later modules can overwrite or read config created by earlier ones.
"""


def get_structured_config(
    vars: dict,
    input_schema_tools: AvdSchemaTools,
    output_schema_tools: AvdSchemaTools,
    result: dict,
    templar: object | None = None,
) -> dict:
    structured_config = {}
    module_vars = ChainMap(
        structured_config,
        vars,
    )

    # Initialize SharedUtils class to be passed to each python_module below.
    shared_utils = SharedUtils(module_vars, templar)

    # Insert dynamic keys into the input data if not set.
    # These keys are required by the schema, but the default values are set inside shared_utils.
    vars.setdefault("node_type_keys", shared_utils.node_type_keys)
    vars.setdefault("connected_endpoints_keys", shared_utils.connected_endpoints_keys)
    vars.setdefault("network_services_keys", shared_utils.network_services_keys)

    # Validate input data
    result.update(input_schema_tools.convert_and_validate_data(vars))
    if result.get("failed"):
        # Input data validation failed so return empty dict. Calling function should check result.get("failed").
        return {}

    for cls in AVD_STRUCTURED_CONFIG_CLASSES:
        eos_designs_module: AvdFacts = cls(module_vars, shared_utils)
        results = eos_designs_module.render()

        # Modules can return a dict or a list of dicts
        if not isinstance(results, list):
            results = [results]

        # All lists will be merged with "append" except for custom structured configuration where
        # the default list merge is "append_rp" and can be overridden.
        # TODO: Each dict entry can contain a list_merge key, which will be picked up by the merge function for all underlying lists.
        if issubclass(cls, AvdStructuredConfigCustomStructuredConfiguration):
            list_merge = get(module_vars, "custom_structured_configuration_list_merge", default="append_rp")

            # Only for structured config run conversion on the data in since we still have some structured config inputs without full schema validation.
            for res in results:
                output_schema_tools.convert_data(res)

        else:
            list_merge = "append"

        merge(structured_config, *results, list_merge=list_merge, schema=output_schema_tools.avdschema)

    return structured_config
