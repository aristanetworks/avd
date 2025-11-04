# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.shared_utils import SharedUtils
from pyavd._errors import AristaAvdModelDeprecationWarning
from pyavd._schema.models.constants import EOS_CLI_CONFIG_GEN_INPUT_KEYS

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
from .structured_config_generator import StructCfgs
from .underlay import AvdStructuredConfigUnderlay

if TYPE_CHECKING:
    from collections.abc import Mapping

    from ansible.template import Templar

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd.avd_schema_tools import AvdSchemaTools

    from .structured_config_generator import StructuredConfigGenerator

AVD_STRUCTURED_CONFIG_CLASSES: list[type[StructuredConfigGenerator]] = [
    # TODO: Rewrite the world to not rely on the order of classes
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
    # since it strips empties from all previously generated structured config and then
    # applies the custom structured config snips gathered by the other generators.
    AvdStructuredConfigCustomStructuredConfiguration,
]
"""
AVD_STRUCTURED_CONFIG contains a list of AvdStructuredConfig classes which generate the complete structured config.
The order is important, since later modules can overwrite or read config created by earlier ones.
"""


def get_structured_config(
    *,
    hostname: str,
    hostvars: Mapping,
    input_schema_tools: AvdSchemaTools,
    all_facts: Mapping[str, EosDesignsFacts],
    result: dict,
    templar: Templar | None = None,
    validate: bool = True,
    digital_twin: bool = False,
) -> EosCliConfigGen | None:
    """
    Generate structured_config for a device.

    Args:
        hostname:
            The hostname of the device
        hostvars:
            The variables for the device
        input_schema_tools:
            An AvdSchemaTools object used to validate the input variables if enabled.
        all_facts:
            Map of all devices and their facts.
        result:
            Dictionary to store results.
        templar:
            The templar to use for rendering templates.
        validate:
            Optional flag to disable validation for the input schema.
        digital_twin:
            Optional flag to enable avd_digital_twin_mode.

    Returns:
        The structured config as an EosCliConfigGen instance or None if validation failed.
    """
    # Validate input data
    if validate:
        result.update(input_schema_tools.convert_and_validate_data(hostvars))
        if result.get("failed"):
            # Input data validation failed so return empty dict. Calling function should check result.get("failed").
            return None

    # Load input vars into the EosDesigns data class.
    inputs = EosDesigns._from_dict(hostvars)

    # Initialize SharedUtils class to be passed to each python_module below.
    shared_utils = SharedUtils(hostname=hostname, hostvars=hostvars, inputs=inputs, peer_facts=all_facts, templar=templar, digital_twin=digital_twin)

    # Single structured config instance which will be in-place updated by each structured config generator.
    structured_config = EosCliConfigGen()

    # Placeholder for custom structured configs added by the structured config generators.
    # Will be applied last by AvdStructuredConfigCustomStructuredConfiguration.
    # "root" holds full device structured configs given under node-config or under VRFs. They will be applied at the root level of the final structured config.
    # "nested" is one instance of structured config merged onto during parsing of various models supporting a "structured_config" option.
    # We need these variants because the order of application is important (root first, then nested).
    #
    custom_structured_configs = StructCfgs.new_from_ansible_list_merge_strategy(inputs.custom_structured_configuration_list_merge)

    for cls in AVD_STRUCTURED_CONFIG_CLASSES:
        eos_designs_module = cls(
            hostvars=hostvars,
            inputs=inputs,
            facts=all_facts[hostname],
            shared_utils=shared_utils,
            structured_config=structured_config,
            custom_structured_configs=custom_structured_configs,
        )
        eos_designs_module.render()

    # Handle detected `eos_cli_config_gen` keys when loading inputs
    _nullify_skipped_keys(inputs, structured_config)

    return structured_config


def _nullify_skipped_keys(inputs: EosDesigns, structured_config: EosCliConfigGen) -> None:
    """
    Nullify in structured_configuration the eos_cli_config_gen keys detected when loading the input if they have not been set in structured.

    For every skipped key emit a warning stating the key has been ignored.

    Args:
        inputs: Loaded inputs in EosDesigns
        structured_config: Rendered structured config as EosCliConfigGen object

    Warnings:
        TODO
    """
    eos_cli_config_gen_keys = inputs._skipped_keys.intersection(EOS_CLI_CONFIG_GEN_INPUT_KEYS)
    for skipped_key in eos_cli_config_gen_keys:
        if not structured_config._get_defined_attr(skipped_key):
            # If the skipped key has not been set by eos_designs, nullify it so it is ignored when eos_cli_config_gen runs.
            setattr(structured_config, skipped_key, None)
        # always emit a warning
    # TODO: revisit once logging is present.
    if len(eos_cli_config_gen_keys) > 0:
        quoted_keys = ", ".join([f"'{key}'" for key in eos_cli_config_gen_keys])
        warnings.warn(
            (
                "The direct usage of `eos_cli_config_gen` keys when running `eos_designs` has been removed in AVD 6.0.0. "
                f"The following keys have been detected in your inputs: {quoted_keys} and have been ignored. "
                "Prioritize using the `eos_designs` models if they address your use case, as new models are frequently added. "
                "Alternatively, use the custom structured configuration feature of `eos_designs`."
                "TODO: refer to porting guide."
            ),
            AristaAvdModelDeprecationWarning,
            stacklevel=2,
        )
