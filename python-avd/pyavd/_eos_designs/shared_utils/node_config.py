# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class NodeConfigMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @property
    def node_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
        """NodesItem object containing the fully inherited node config."""
        return self.consolidated.node_config

    @property
    def node_group_is_primary_and_peer_hostname(self: SharedUtilsProtocol) -> tuple[bool, str] | None:
        """
        Node group position and peer used for MLAG and WAN HA.

        Returns None if the device is not in a node_group with exactly two devices.
        Returns True, <peer> if this device is the first one in the node_group.
        Returns False, <peer> if this device is the second one in the node_group.
        """
        node_group = self.consolidated._get("node_group")
        if node_group is None:
            return None
        return node_group.is_primary, node_group.peer
