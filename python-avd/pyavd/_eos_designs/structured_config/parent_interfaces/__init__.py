# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Centralized Parent Interfaces Module.

This module provides centralized generation of parent interfaces for subinterfaces.

## Architecture Overview

The parent interfaces functionality uses a global tracking pattern:

1. A `ParentInterfacesTracker` instance is created at the start of structured config generation
    and passed to each of the `AvdStructuredConfig` classes (in `structured_config/__init__.py`).

2. As each structured config module creates interfaces, it registers them with the tracker:
   - Subinterfaces (e.g., "Ethernet1.100") are registered as requiring a parent
   - Parent interfaces (e.g., "Ethernet1") are registered as existing
   - Registration happens in all modules that create ethernet_interfaces or port_channel_interfaces.

3. **Parent Creation Phase**: The `AvdStructuredConfigParentInterfaces` module runs near the end
   of the pipeline (before flow and custom_structured_configuration) and creates any missing parent interfaces
   with minimal configuration:
   - `shutdown: false`
   - `switchport.enabled: false` (for Ethernet interfaces)
   - `metadata.peer_type: subinterface_parent`
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import (
    StructuredConfigGenerator,
    StructuredConfigGeneratorProtocol,
    structured_config_contributor,
)
from pyavd._errors import AristaAvdError
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigParentInterfacesProtocol


class ParentInterfacesTracker:
    """
    Global tracker for parent interfaces that need to be created.

    This class maintains sets of parent interface names that are required
    and those that already exist, allowing the centralized parent_interfaces
    module to create only the missing ones at the end of the pipeline.
    """

    def __init__(self) -> None:
        self.required_ethernet_parents: set[str] = set()
        """Set of Ethernet parent interface names required by subinterfaces."""

        self.existing_ethernet_parents: set[str] = set()
        """Set of Ethernet parent interface names that already exist."""

        self.required_port_channel_parents: set[str] = set()
        """Set of Port-Channel parent interface names required by subinterfaces."""

        self.existing_port_channel_parents: set[str] = set()
        """Set of Port-Channel parent interface names that already exist."""

    def register_ethernet_subinterface(self, subinterface_name: str) -> None:
        """Register an Ethernet subinterface and track its required parent."""
        if "." in subinterface_name:
            parent_name = subinterface_name.split(".", maxsplit=1)[0]
            self.required_ethernet_parents.add(parent_name)
        else:
            msg = f"Expected subinterface name with dot, got '{subinterface_name}'"
            raise AristaAvdError(msg)

    def register_ethernet_parent(self, parent_name: str) -> None:
        """Register an existing Ethernet parent interface."""
        self.existing_ethernet_parents.add(parent_name)

    def register_port_channel_subinterface(self, subinterface_name: str) -> None:
        """Register a Port-Channel subinterface and track its required parent."""
        if "." in subinterface_name:
            parent_name = subinterface_name.split(".", maxsplit=1)[0]
            self.required_port_channel_parents.add(parent_name)
        else:
            msg = f"Expected subinterface name with dot, got '{subinterface_name}'"
            raise AristaAvdError(msg)

    def register_port_channel_parent(self, parent_name: str) -> None:
        """Register an existing Port-Channel parent interface."""
        self.existing_port_channel_parents.add(parent_name)

    def get_missing_ethernet_parents(self) -> set[str]:
        """Return the set of Ethernet parent interfaces that need to be created."""
        return self.required_ethernet_parents.difference(self.existing_ethernet_parents)

    def get_missing_port_channel_parents(self) -> set[str]:
        """Return the set of Port-Channel parent interfaces that need to be created."""
        return self.required_port_channel_parents.difference(self.existing_port_channel_parents)


class AvdStructuredConfigParentInterfacesProtocol(
    StructuredConfigGeneratorProtocol,
    Protocol,
):
    """
    Protocol for the AvdStructuredConfigParentInterfaces Class.

    This class is responsible for generating parent interfaces for all subinterfaces
    that were created by other modules but don't have their parent interfaces defined.
    """

    @structured_config_contributor
    def ethernet_interfaces(self: AvdStructuredConfigParentInterfacesProtocol) -> None:
        """
        Generate missing parent Ethernet interfaces for all subinterfaces.

        This method uses the global ParentInterfacesTracker to determine which
        parent interfaces need to be created based on tracking done throughout
        the structured config generation pipeline.
        """
        for interface_name in natural_sort(self.parent_interfaces_tracker.get_missing_ethernet_parents()):
            interface = EosCliConfigGen.EthernetInterfacesItem(
                name=interface_name,
                shutdown=False,
            )
            interface.metadata.peer_type = "subinterface_parent"
            interface.switchport.enabled = False
            self.structured_config.ethernet_interfaces.append(interface)

    @structured_config_contributor
    def port_channel_interfaces(self: AvdStructuredConfigParentInterfacesProtocol) -> None:
        """
        Generate missing parent Port-Channel interfaces for all subinterfaces.

        This method uses the global ParentInterfacesTracker to determine which
        parent interfaces need to be created based on tracking done throughout
        the structured config generation pipeline.
        """
        for interface_name in natural_sort(self.parent_interfaces_tracker.get_missing_port_channel_parents()):
            interface = EosCliConfigGen.PortChannelInterfacesItem(
                name=interface_name,
                shutdown=False,
            )
            interface.metadata.peer_type = "subinterface_parent"
            self.structured_config.port_channel_interfaces.append(interface)


class AvdStructuredConfigParentInterfaces(StructuredConfigGenerator, AvdStructuredConfigParentInterfacesProtocol):
    """
    Centralized module for generating parent interfaces for subinterfaces.

    This module must be rendered after all other modules that create subinterfaces
    (network_services, underlay, core_interfaces_and_l3_edge, connected_endpoints, etc.)
    but before custom_structured_configuration.

    It uses the global ParentInterfacesTracker (attached to shared_utils) to determine
    which parent interfaces need to be created based on tracking done throughout
    the structured config generation pipeline.
    """


__all__ = ["AvdStructuredConfigParentInterfaces", "ParentInterfacesTracker"]
