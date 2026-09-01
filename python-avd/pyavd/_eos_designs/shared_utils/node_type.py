# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils import default

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import SharedUtilsProtocol


class NodeTypeMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @property
    def type(self: SharedUtilsProtocol) -> str:
        """Type fact set based on the type variable or default_node_type."""
        return self.consolidated.type

    @cached_property
    def connected_endpoints(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure connected endpoints?

        connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints.
        """
        return self.consolidated.node_type_keys_item.connected_endpoints

    @cached_property
    def underlay_router(self: SharedUtilsProtocol) -> bool:
        """
        Is this an underlay router?

        underlay_router set based on
        node_type_keys.<node_type_key>.underlay_router.
        """
        return self.consolidated.node_type_keys_item.underlay_router

    @cached_property
    def uplink_type(self: SharedUtilsProtocol) -> EosDesigns.NodeTypeKeysItem.UplinkType:
        """
        Uplink type.

        uplink_type set based on <node_type_key>.nodes.[].uplink_type and node_type_keys.<node_type_key>.uplink_type.
        """
        return default(self.node_config.uplink_type, self.consolidated.node_type_keys_item.uplink_type)

    @cached_property
    def network_services_l1(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L1 network services?

        network_services_l1 set based on node_type_keys.<node_type_key>.network_services.l1.
        """
        return self.consolidated.node_type_keys_item.network_services.l1

    @cached_property
    def network_services_l2(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L2 network services?

        network_services_l2 set based on node_type_keys.<node_type_key>.network_services.l2.
        """
        return self.consolidated.node_type_keys_item.network_services.l2

    @cached_property
    def network_services_l3(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L3 network services?

        network_services_l3 set based on node_type_keys.<node_type_key>.network_services.l3
        and <node_type_key>.<defaults | node_groups.<> | nodes.<> >.evpn_services_l2_only.
        """
        # network_services_l3 override based on evpn_services_l2_only
        if self.vtep and self.node_config.evpn_services_l2_only:
            return False
        return self.consolidated.node_type_keys_item.network_services.l3

    @cached_property
    def network_services_l2_as_subint(self: SharedUtilsProtocol) -> bool:
        """
        Should we deploy SVIs as subinterfaces?

        network_services_l2_as_subint set based on
        node_type_keys.<node_type_key>.network_services.l3 for uplink_type "lan" or "lan-port-channel".
        """
        return self.network_services_l3 and self.uplink_type in ["lan", "lan-port-channel"]

    @cached_property
    def any_network_services(self: SharedUtilsProtocol) -> bool:
        """Returns True if either L1, L2 or L3 network_services are enabled."""
        return self.network_services_l1 or self.network_services_l2 or self.network_services_l3

    @cached_property
    def mpls_lsr(self: SharedUtilsProtocol) -> bool:
        """
        Is this an MPLS LSR?

        mpls_lsr set based on
        node_type_keys.<node_type_key>.mpls_lsr.
        """
        return self.consolidated.node_type_keys_item.mpls_lsr

    @cached_property
    def vtep(self: SharedUtilsProtocol) -> bool:
        """
        Is this a VTEP?

        vtep set based on
        <node_type_key>.nodes.[].vtep and
        node_type_keys.<node_type_key>.vtep.
        """
        return default(self.node_config.vtep, self.consolidated.node_type_keys_item.vtep)

    @cached_property
    def hint_type(self: SharedUtilsProtocol) -> str | None:
        """Type hint fact set based on type variable."""
        return default(self.node_config.cv_tags_topology_type, self.inputs.cv_tags_topology_type, self.consolidated.node_type_keys_item.cv_tags_topology_type)

    @cached_property
    def campus_hint_type(self: SharedUtilsProtocol) -> str | None:
        """Type hint fact for Campus devices set based on type variable."""
        return hint_type.title() if (hint_type := self.hint_type) in ["spine", "leaf", "member-leaf"] else None
