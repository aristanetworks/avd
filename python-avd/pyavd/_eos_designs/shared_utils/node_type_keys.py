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


class NodeTypeKeysMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def type_or_role(self: SharedUtilsProtocol) -> str:
        """Return the name of this device's 'type' or 'role'. Used as peer_type on peers and for default_interfaces."""
        match (self.type, self.role):
            case (None, None):
                msg = "Either 'type' or 'devices[].role' must be set."
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            case (str(), str()):
                msg = "Both 'type' and 'devices[].role' is set. Only on of them should be used."
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            case (str(), None):
                return self.type
            case (None, str()):
                return self.role
            case _:
                # Should never happen.
                msg = "Not able to determine role or type"
                raise NotImplementedError(msg)

    @cached_property
    def node_type_key_data(self: SharedUtilsProtocol) -> EosDesigns.NodeTypeKeysItem:
        """node_type_key_data containing settings for this node_type or device_role."""
        if self.role:
            if not (device_role := self.inputs.device_roles.get(self.role)):
                # This never happens since we perform the same check in device_config where self.role is taken from.
                msg = f"Device Role '{self.role}' applied under 'devices' does not exist in `device_roles`."
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

            return EosDesigns.NodeTypeKeysItem(
                type=device_role.name,
                connected_endpoints=device_role.connected_endpoints,
                cv_tags_topology_type=device_role.cv_tags_topology_type,
                default_evpn_role=device_role.evpn_role,
                default_evpn_encapsulation=device_role.evpn_encapsulation,
                default_flow_tracker_type=device_role.flow_tracker_type,
                default_mpls_overlay_role=device_role.mpls_overlay_role,
                default_overlay_address_families=device_role.overlay_address_families._cast_as(EosDesigns.NodeTypeKeysItem.DefaultOverlayAddressFamilies),
                default_overlay_routing_protocol=device_role.overlay_routing_protocol,
                default_ptp_priority1=device_role.ptp.priority1,
                default_underlay_routing_protocol=device_role.underlay_routing_protocol,
                underlay_router=device_role.underlay_router,
                default_wan_role=device_role.wan_role,
                interface_descriptions=device_role.custom_interface_descriptions._cast_as(EosDesigns.NodeTypeKeysItem.InterfaceDescriptions),
                ip_addressing=device_role.custom_ip_addressing._cast_as(EosDesigns.NodeTypeKeysItem.IpAddressing),
                mlag_support=device_role.mlag_support,
                mpls_lsr=device_role.mpls_lsr,
                network_services=device_role.network_services._cast_as(EosDesigns.NodeTypeKeysItem.NetworkServices),
                uplink_type=device_role.uplink_type,
                vtep=device_role.vtep,
            )

        # We know role is not set. Calling type_or_role to trigger an error if neither is set.
        node_type = self.type_or_role

        for node_type_key in self.inputs.custom_node_type_keys:
            if node_type_key.type == node_type:
                return node_type_key._cast_as(EosDesigns.NodeTypeKeysItem)

        node_type_keys = self.inputs.node_type_keys
        for node_type_key in node_type_keys:
            if node_type_key.type == node_type:
                return node_type_key

        # This should never happen, as it should be caught during validation
        msg = f"Could not find the given type '{node_type}' in node_type_keys or custom_node_type_keys."
        raise AristaAvdInvalidInputsError(msg, host=self.hostname)
