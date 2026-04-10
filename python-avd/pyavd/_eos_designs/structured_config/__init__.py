# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.shared_utils import SharedUtils

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
from .parent_interfaces import AvdStructuredConfigParentInterfaces
from .structured_config_generator import StructCfgs
from .structured_config_utils import StructuredConfigUtils
from .underlay import AvdStructuredConfigUnderlay

if TYPE_CHECKING:
    from collections.abc import Mapping, MutableMapping

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._utils import AVDTemplar

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
    # The Parent Interfaces module must be rendered after all modules that create subinterfaces,
    # but before the Flows module so that parent interfaces get flow tracking metadata.
    AvdStructuredConfigParentInterfaces,
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
    inputs: EosDesigns,
    all_facts: Mapping[str, EosDesignsFacts],
    hostvars: MutableMapping | None = None,
    templar: AVDTemplar | None = None,
    digital_twin: bool = False,
) -> EosCliConfigGen:
    """
    Generate structured_config for a device.

    Args:
        hostname:
            The hostname of the device.
        inputs:
            Validated inputs loaded into an instance of the EosDesigns class.
        all_facts:
            Map of all devices and their facts.
        hostvars:
            Raw hostvars exposed to custom jinja templates or custom python logic for each device.
            This is optional and only needed if custom templates or python modules are used for descriptions or IP addressing.
        templar:
            Templater used to render custom jinja templates.
            This is optional and only needed if custom templates are used for descriptions or IP addressing.
        digital_twin:
            Optional flag to enable avd_digital_twin_mode.

    Returns:
        The structured config as an EosCliConfigGen instance or None if validation failed.
    """
    if hostvars is None:
        hostvars = {}

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

    # Create a single shared structured config utils instance for all structured config classes.
    structured_config_utils = StructuredConfigUtils(
<<<<<<< eos_designs_run_once_method_refactoring
        structured_config=structured_config, custom_structured_configs=custom_structured_configs, inputs=inputs, shared_utils=shared_utils
=======
        structured_config=structured_config, inputs=inputs, shared_utils=shared_utils, custom_structured_configs=custom_structured_configs
>>>>>>> devel
    )

    for cls in AVD_STRUCTURED_CONFIG_CLASSES:
        eos_designs_module = cls(
            hostvars=hostvars,
            inputs=inputs,
            facts=all_facts[hostname],
            shared_utils=shared_utils,
            structured_config=structured_config,
            custom_structured_configs=custom_structured_configs,
            structured_config_utils=structured_config_utils,
        )
        eos_designs_module.render()

    return structured_config
