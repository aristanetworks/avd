# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils.password_utils.password import bgp_encrypt
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import SharedUtilsProtocol

    BgpPeerGroupOrNeighbor = (
        EosDesigns.BgpPeerGroups.Ipv4UnderlayPeers
        | EosDesigns.BgpPeerGroups.MlagIpv4UnderlayPeer
        | EosDesigns.BgpPeerGroups.WanOverlayPeers
        | EosDesigns.BgpPeerGroups.WanRrOverlayPeers
        | EosDesigns.BgpPeerGroups.MplsOverlayPeers
        | EosDesigns.BgpPeerGroups.EvpnOverlayCore
        | EosDesigns.BgpPeerGroups.EvpnOverlayPeers
        | EosDesigns.BgpPeerGroups.RrOverlayPeers
        | EosDesigns.BgpPeerGroups.MlagIpv4VrfsPeer
        | EosDesigns.BgpPeerGroups.IpvpnGatewayPeers
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.BgpPeerGroupsItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.BgpPeerGroupsItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.BgpPeersItem
    )


class RoutingMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_routing_protocol(self: SharedUtilsProtocol) -> str:
        default_underlay_routing_protocol = self.node_type_key_data.default_underlay_routing_protocol
        return (self.inputs.underlay_routing_protocol or default_underlay_routing_protocol).lower()

    @cached_property
    def overlay_routing_protocol(self: SharedUtilsProtocol) -> str:
        default_overlay_routing_protocol = self.node_type_key_data.default_overlay_routing_protocol
        if self.is_wan_router and not self.inputs.wan_use_evpn_node_settings_for_lan:
            # For WAN routers without the knob, overlay_routing_protocol should be ignored.
            return "none"
        return (self.inputs.overlay_routing_protocol or default_overlay_routing_protocol).lower()

    @cached_property
    def overlay_address_families(self: SharedUtilsProtocol) -> list[str]:
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            default_overlay_address_families = self.node_type_key_data.default_overlay_address_families
            return self.node_config.overlay_address_families._as_list() or default_overlay_address_families._as_list()
        return []

    @cached_property
    def bgp(self: SharedUtilsProtocol) -> bool:
        """Boolean telling if BGP Routing should be configured."""
        if not self.underlay_router:
            return False

        return (
            self.uplink_type in ["p2p", "p2p-vrfs", "lan"]
            and (
                self.underlay_routing_protocol == "ebgp"
                or (
                    self.overlay_routing_protocol in ["ebgp", "ibgp"]
                    and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
                )
                or self.bgp_in_network_services
            )
        ) or bool(self.l3_bgp_neighbors)

    @cached_property
    def router_id(self: SharedUtilsProtocol) -> str | None:
        """Render IP address for router_id."""
        if self.underlay_router:
            return self.ip_addressing.router_id()
        return None

    @cached_property
    def ipv6_router_id(self: SharedUtilsProtocol) -> str | None:
        """Render IPv6 address for router_id."""
        if self.underlay_router and self.underlay_ipv6:
            return self.ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def isis_instance_name(self: SharedUtilsProtocol) -> str | None:
        if self.underlay_router and self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
            default_isis_instance_name = "CORE" if self.mpls_lsr else "EVPN_UNDERLAY"
            return self.inputs.underlay_isis_instance_name or default_isis_instance_name
        # This point cannot be reached because the function won't be called if either of the conditions in the if-block is not satisfied.
        return None

    @cached_property
    def bgp_as(self: SharedUtilsProtocol) -> str | None:
        """
        Get global bgp_as or fabric_topology bgp_as.

        At least one of global bgp_as or fabric_topology bgp_as must be defined.

        AS ranges in fabric_topology bgp_as will be expanded to a list and:
         - For standalone or A/A MH devices, the node id will be used to index into the list to find the ASN.
         - For MLAG devices, the node id of the first node in the node group will be used to index into the ASN list.
         - If a bare ASN is used, that ASN will be used for all relevant devices (depending on whether defined
           at the defaults, node_group or node level).
         - Lower level definitions override higher level definitions as is standard with AVD.
        """
        if not self.bgp:
            return None

        if self.inputs.bgp_as:
            return self.inputs.bgp_as

        if self.node_config.bgp_as is None:
            msg = "bgp_as"
            raise AristaAvdMissingVariableError(msg, host=self.hostname)

        bgp_as_range_expanded = range_expand(self.node_config.bgp_as)
        try:
            if len(bgp_as_range_expanded) == 1:
                return bgp_as_range_expanded[0]
            if self.mlag_switch_ids:
                return bgp_as_range_expanded[self.mlag_switch_ids["primary"] - 1]

            if self.id is None:
                msg = f"'id' is not set on '{self.hostname}' and is required when expanding 'bgp_as'"
                raise AristaAvdInvalidInputsError(msg)
            return bgp_as_range_expanded[self.id - 1]
        except IndexError as exc:
            msg = f"Unable to allocate BGP AS: bgp_as range '{self.node_config.bgp_as}' is too small ({len(bgp_as_range_expanded)}) for the id '{self.id}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname) from exc

    def get_bgp_password(
        self: SharedUtilsProtocol,
        peer_group_or_neighbor: BgpPeerGroupOrNeighbor,
    ) -> str | None:
        """
        Take a peer group name or a neighbor return a type 7 password, potentially encrypting a cleartext_password.

        This function assumes that the `.password` attributes is always a type 7 as per the schema.

        Args:
            peer_group_or_neighbor: The Peer Group or Neighbor object to get the password for.

        Returns:
            str: The type 7 encrypted password
            None: if the password is None
        """
        if peer_group_or_neighbor.password is not None:
            return peer_group_or_neighbor.password
        if peer_group_or_neighbor.cleartext_password is not None:
            if isinstance(peer_group_or_neighbor, EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.BgpPeersItem):
                key = peer_group_or_neighbor.ip_address
            else:
                key = peer_group_or_neighbor.name

            return bgp_encrypt(peer_group_or_neighbor.cleartext_password, key)
        return None
