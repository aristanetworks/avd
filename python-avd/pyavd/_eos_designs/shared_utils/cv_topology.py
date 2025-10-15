# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class CvTopology(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def cv_topology(self: SharedUtilsProtocol) -> EosDesigns.CvTopologyItem | None:
        """Returns the cv_topology for this device after checking other dependencies."""
        if not self.inputs.use_cv_topology:
            return None

        if not self.inputs.cv_topology:
            msg = "'cv_topology' is required when 'use_cv_topology' is set to 'true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if not self.inputs.cv_topology_levels:
            msg = "'cv_topology_levels' is required when 'use_cv_topology' is set to 'true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if (
            self.node_config.uplink_switches
            or self.node_config.uplink_interfaces
            or self.node_config.uplink_switch_interfaces
            or self.node_config.mlag_interfaces
        ):
            msg = (
                "'uplink_switches', 'uplink_interfaces', 'uplink_switch_interfaces' and 'mlag_interfaces' "
                "should not be set when 'use_cv_topology' is set to 'true'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.hostname not in self.inputs.cv_topology:
            # Ignoring missing data for this device in cv_topology. Historic behavior and needed for hybrid scenarios.
            return None

        return self.inputs.cv_topology[self.hostname]

    @cached_property
    def cv_topology_platform(self: SharedUtilsProtocol) -> str | None:
        if self.cv_topology is not None:
            return self.cv_topology.platform
        return None

    def get_cv_topology_level(self: SharedUtilsProtocol, node_type: str) -> int:
        if not (cv_topology_level := self.inputs.cv_topology_levels.get(node_type)):
            msg = f"'cv_topology_levels' must include all node types when 'use_cv_topology' is set to 'true'. Missing type '{node_type}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)
        return cv_topology_level.level

    @cached_property
    def cv_topology_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
        """Returns node config derived from cv_topology to make it easy to merge on top of other node config."""
        node_config = EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem()
        if self.cv_topology is None:
            return node_config

        level = self.get_cv_topology_level(self.type)
        for interface in self.cv_topology.interfaces._natural_sorted():
            if interface.name.startswith("Management"):
                # Only set the first management interface we find.
                # For modulars that would be the alias interface.
                if not node_config.mgmt_interface:
                    node_config.mgmt_interface = interface.name
                continue

            if not interface.neighbor or not interface.neighbor_interface:
                # Silently ignore missing/incomplete peering information.
                continue

            if self.mlag and interface.neighbor == self.mlag_peer:
                node_config.mlag_interfaces.append(interface.name)
                continue

            if not (neighbor_facts := self.get_peer_facts(interface.neighbor, required=False)):
                # Ignoring neighbors that are not part of the inventory.
                continue

            neighbor_level = self.get_cv_topology_level(neighbor_facts.type)

            if neighbor_level < level:
                # This device is the child.
                node_config.uplink_switches.append(interface.neighbor)
                node_config.uplink_interfaces.append(interface.name)
                node_config.uplink_switch_interfaces.append(interface.neighbor_interface)

            # Same levels or this device is the parent. We expect the child to set up the uplink information, so ignoring here.

        return node_config
