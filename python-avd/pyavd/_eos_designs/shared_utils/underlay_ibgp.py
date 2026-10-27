# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.undefined import Undefined
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import SharedUtilsProtocol

MSG_PREFIX = "Invalid combination of inputs."


class UnderlayIbgpMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.

    The route reflector (RR) logic relies on the facts of other devices, so the members below
    must only be used while generating structured config, never while generating facts.
    """

    @cached_property
    def underlay_ibgp(self: SharedUtilsProtocol) -> bool:
        """Is this an underlay router running 'underlay_routing_protocol: ibgp'."""
        return self.underlay_router and self.underlay_routing_protocol == "ibgp"

    @cached_property
    def underlay_ibgp_cluster_id(self: SharedUtilsProtocol) -> str | None:
        """The BGP cluster ID shared by this node and the other route reflectors of the same clients. None if this node is not a route reflector."""
        if (rr_group := self._underlay_ibgp_rr_group) is None:
            return None
        return rr_group[1]

    @cached_property
    def _underlay_ibgp_rr_group(self: SharedUtilsProtocol) -> tuple[frozenset[str], str] | None:
        """The route reflector group of this node and its cluster ID. None if this node is not a route reflector."""
        if not self.underlay_ibgp or not self.switch_facts.downlink_switches:
            return None
        return self._resolve_underlay_ibgp_rr_group(self.hostname)

    def _resolve_underlay_ibgp_rr_group(self: SharedUtilsProtocol, rr: str) -> tuple[frozenset[str], str]:
        """
        Resolve the route reflector group of the given route reflector.

        The group is the common set of uplink switches of all the clients of the route reflector.
        All route reflectors in the group must have the same clients.

        Returns:
            Tuple of the route reflectors in the group and the resolved cluster ID.

        Raises:
            AristaAvdInvalidInputsError: If the clients or the route reflectors do not form a full mesh,
                or if 'bgp_cluster_id' is not consistent within the group.
        """
        clients = natural_sort(self.get_peer_facts(rr).downlink_switches)
        client_set = frozenset(clients)

        first_client = clients[0]
        rr_set = frozenset(self.get_peer_facts(first_client).uplink_peers)
        for client in clients[1:]:
            if (client_uplinks := frozenset(self.get_peer_facts(client).uplink_peers)) != rr_set:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all clients of a route reflector to have the same uplink switches, "
                    f"but '{first_client}' has {natural_sort(rr_set)} and '{client}' has {natural_sort(client_uplinks)}."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        members = natural_sort(rr_set)
        for member in members:
            if (member_clients := frozenset(self.get_peer_facts(member).downlink_switches)) != client_set:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all route reflectors sharing clients to have the same downlink switches, "
                    f"but '{rr}' has {clients} and '{member}' has {natural_sort(member_clients)}."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        cluster_ids = {member: self.get_peer_facts(member).bgp_cluster_id for member in members}
        if len(set(cluster_ids.values())) > 1:
            msg = (
                f"{MSG_PREFIX} 'bgp_cluster_id' must be set to the same value on all the route reflectors {members} sharing the same clients, "
                f"or on none of them, but got {cluster_ids}."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if (cluster_id := cluster_ids[members[0]]) is not None:
            return rr_set, cluster_id

        router_ids = []
        for member in members:
            if (router_id := self.get_peer_facts(member).router_id) is None:
                msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires a router ID on all route reflectors, but '{member}' has none."
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            router_ids.append(ipaddress.ip_address(router_id))
        return rr_set, str(min(router_ids))

    def validate_underlay_ibgp(self: SharedUtilsProtocol) -> None:
        """
        Raise if the inputs are not supported with 'underlay_routing_protocol: ibgp'.

        Does nothing if this node is not an iBGP underlay router.
        Must only be called while generating structured config, since it relies on the facts of other devices.
        """
        if not self.underlay_ibgp:
            return

        self._validate_underlay_ibgp_node_inputs()
        self._validate_underlay_ibgp_neighbors()
        self._validate_underlay_ibgp_cluster_ids()

    def _validate_underlay_ibgp_node_inputs(self: SharedUtilsProtocol) -> None:
        """Validate the inputs of this node, without looking at other devices."""
        if self.inputs.underlay_rfc5549 is not True:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'underlay_rfc5549: true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.underlay_ipv6 or self.inputs.underlay_ipv6_numbered:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support 'underlay_ipv6' or 'underlay_ipv6_numbered'; set them to false."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.overlay_routing_protocol != "none":
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'overlay_routing_protocol: none', but got '{self.overlay_routing_protocol}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.uplink_type != "p2p":
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'uplink_type: p2p', but got '{self.uplink_type}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.mpls_lsr:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported on node types with 'mpls_lsr: true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.mlag:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported with MLAG; set 'mlag: false'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.is_wan_router:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported on WAN routers; remove 'wan_role'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.l3_bgp_neighbors:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support BGP peers on 'l3_interfaces' or 'l3_port_channels'; "
                "remove their 'bgp' settings."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        for tenant in self.filtered_tenants:
            if tenant.vrfs or tenant.l2vlans:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support network services, but tenant '{tenant.name}' has VRFs or L2 VLANs "
                    "on this node; remove them or exclude the tenant with 'filter.tenants'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if (
            self.configure_inband_mgmt
            or self.configure_inband_mgmt_ipv6
            or self.node_config.inband_ztp
            # Inband management of downlink switches.
            or self.inband_management_parent_vlans
        ):
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support inband management or 'inband_ztp'; "
                "remove the inband management settings from this node and its downlink switches."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.any_multicast_enabled:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support underlay multicast; "
                "disable 'underlay_multicast_pim_sm', 'underlay_multicast_static' and the node 'underlay_multicast' settings."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.inputs.bgp_peer_groups._get_defined_attr("ipv4_underlay_peers") is not Undefined:
            msg = (
                f"{MSG_PREFIX} 'bgp_peer_groups.ipv4_underlay_peers' is not used with 'underlay_routing_protocol: ibgp'; "
                "move its settings to 'bgp_peer_groups.rr_underlay_peers' and 'bgp_peer_groups.rr_clients_underlay_peers'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.node_config.uplink_bfd:
            msg = (
                f"{MSG_PREFIX} 'uplink_bfd: true' is not supported with 'underlay_routing_protocol: ibgp'; "
                "use 'bgp_peer_groups.rr_underlay_peers.bfd' and 'bgp_peer_groups.rr_clients_underlay_peers.bfd' instead."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.inputs.underlay_filter_peer_as:
            msg = f"{MSG_PREFIX} 'underlay_filter_peer_as: true' is not supported with 'underlay_routing_protocol: ibgp'; set it to false."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.node_config.bgp_cluster_id is not None and not self.switch_facts.downlink_switches:
            msg = (
                f"{MSG_PREFIX} 'bgp_cluster_id' is set on a node without downlink switches, "
                "which is not a route reflector with 'underlay_routing_protocol: ibgp'; remove 'bgp_cluster_id'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        rr_underlay_peers_name = self.inputs.bgp_peer_groups.rr_underlay_peers.name
        if rr_underlay_peers_name == self.inputs.bgp_peer_groups.rr_clients_underlay_peers.name:
            msg = (
                f"{MSG_PREFIX} 'bgp_peer_groups.rr_underlay_peers.name' and 'bgp_peer_groups.rr_clients_underlay_peers.name' must be different, "
                f"but both are '{rr_underlay_peers_name}'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

    def _validate_underlay_ibgp_neighbors(self: SharedUtilsProtocol) -> None:
        """Validate that all uplink and downlink switches are iBGP underlay routers with p2p links and the same BGP AS."""
        switch_facts = self.switch_facts
        neighbors = [("uplink", peer) for peer in switch_facts.uplink_peers] + [("downlink", peer) for peer in natural_sort(switch_facts.downlink_switches)]
        for direction, peer in neighbors:
            peer_facts = self.get_peer_facts(peer)
            reason = None
            if peer_facts.underlay_routing_protocol != "ibgp":
                reason = f"uses 'underlay_routing_protocol: {peer_facts.underlay_routing_protocol}'"
            elif direction == "downlink" and (
                uplink_types := {uplink.type for uplink in peer_facts.uplinks if uplink.peer == self.hostname and uplink.type != "underlay_p2p"}
            ):
                reason = f"connects with uplinks of type {natural_sort(uplink_types)}"
            elif direction == "downlink" and any(uplink.subinterfaces for uplink in peer_facts.uplinks if uplink.peer == self.hostname):
                reason = "connects with uplink subinterfaces"
            elif peer_facts.bgp_as is None:
                reason = "is not an underlay router"

            if reason is not None:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires all uplink and downlink switches to be 'ibgp' underlay routers "
                    f"with 'uplink_type: p2p', but {direction} switch '{peer}' {reason}."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

            if (peer_bgp_as := self.get_asn(peer_facts.bgp_as)) != self.formatted_bgp_as:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires the same 'bgp_as' on all fabric nodes, "
                    f"but {direction} switch '{peer}' has '{peer_bgp_as}' and this node has '{self.formatted_bgp_as}'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

    def _validate_underlay_ibgp_cluster_ids(self: SharedUtilsProtocol) -> None:
        """
        Validate the route reflector group of this node and that no other group uses the same cluster ID.

        Groups of other route reflectors that fail to resolve are skipped, since those raise on their own devices.
        """
        if (own_rr_group := self._underlay_ibgp_rr_group) is None:
            return

        own_rr_set, own_cluster_id = own_rr_group
        resolved_rrs = set(own_rr_set)
        for rr in natural_sort(self.all_fabric_devices):
            if rr in resolved_rrs:
                continue

            rr_facts = self.get_peer_facts(rr)
            if rr_facts.underlay_routing_protocol != "ibgp" or not rr_facts.downlink_switches:
                continue

            # Only route reflectors with at least one iBGP client, so we skip L2 parents.
            if not any(
                uplink.peer == rr and uplink.type == "underlay_p2p" for client in rr_facts.downlink_switches for uplink in self.get_peer_facts(client).uplinks
            ):
                continue

            try:
                rr_set, cluster_id = self._resolve_underlay_ibgp_rr_group(rr)
            except AristaAvdInvalidInputsError:
                continue

            resolved_rrs.update(rr_set)
            if cluster_id == own_cluster_id:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires a unique cluster ID per group of route reflectors, "
                    f"but {natural_sort(own_rr_set)} and {natural_sort(rr_set)} both use '{cluster_id}'; set a unique 'bgp_cluster_id' per group."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
