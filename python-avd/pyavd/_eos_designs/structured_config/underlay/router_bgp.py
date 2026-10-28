# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouterBgpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_bgp(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for router_bgp."""
        if self.shared_utils.underlay_ibgp:
            self.shared_utils.validate_underlay_ibgp()
            self._validate_underlay_ibgp_links()

        if self.shared_utils.underlay_bgp or self.shared_utils.is_wan_router or self.shared_utils.l3_bgp_neighbors:
            self.structured_config.router_bgp.redistribute.connected.enabled = True
            if (self.shared_utils.overlay_routing_protocol != "none" or self.shared_utils.is_wan_router) and self.inputs.underlay_filter_redistribute_connected:
                # Use route-map for redistribution
                self.structured_config.router_bgp.redistribute.connected.route_map = "RM-CONN-2-BGP"
                # Create route-map
                self.set_once_route_map_connected_to_bgp()

        if not self.shared_utils.underlay_bgp:
            return

        # Set BGP peer group only when underlay link is present.
        if not self._underlay_p2p_links:
            return

        if self.shared_utils.underlay_ibgp:
            self._set_underlay_ibgp_neighbor_interfaces()
            if self.facts.downlink_switches:
                # Set on all route reflectors and validated per route reflector group while generating facts.
                self.structured_config.router_bgp.bgp_cluster_id = self.shared_utils.node_config.bgp_cluster_id
            return

        # Adding the peer-group as we know we either have neighbors or neighbor_interfaces to configure
        self.structured_config_utils.set_once_peer_group_ipv4_underlay_peers()

        # Neighbor Interfaces and VRF Neighbor Interfaces
        if self.inputs.underlay_rfc5549 is True:
            for link in self._underlay_p2p_links:
                self.structured_config.router_bgp.neighbor_interfaces.append_new(
                    name=link.interface,
                    peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                    remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                    metadata=EosCliConfigGen.RouterBgp.NeighborInterfacesItem.Metadata(peer=link.peer),
                    description=f"{link.peer}_{link.peer_interface}",
                )

                for subinterface in link.subinterfaces:
                    # We need to add basic BGP VRF config in case the device is not covered by network_services. (Like a spine)
                    if subinterface.vrf not in self.structured_config.router_bgp.vrfs:
                        self.structured_config.router_bgp.vrfs.append_new(name=subinterface.vrf, router_id=self.shared_utils.router_id)

                    self.structured_config.router_bgp.vrfs[subinterface.vrf].neighbor_interfaces.append_new(
                        name=subinterface.interface,
                        peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                        remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                        # TODO: - implement some centralized way to generate these descriptions
                        description=f"{link.peer}_{subinterface.peer_interface}_vrf_{subinterface.vrf}",
                    )

        # Neighbors and VRF Neighbors
        else:
            for link in self._underlay_p2p_links:
                neighbor = EosCliConfigGen.RouterBgp.NeighborsItem(
                    ip_address=cast("str", link.peer_ip_address),
                    peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                    remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                    description=f"{link.peer}_{link.peer_interface}",
                    bfd=link.bfd,
                )
                neighbor.metadata.peer = link.peer

                if self.inputs.shutdown_bgp_towards_undeployed_peers and not link.peer_is_deployed:
                    neighbor.shutdown = True

                if self.inputs.underlay_filter_peer_as and link.peer_bgp_as is not None:
                    neighbor.route_map_out = f"RM-BGP-AS{link.peer_bgp_as}-OUT"
                    # Create the route-map
                    self.set_route_map_underlay_filter_peer_as(link.peer_bgp_as)

                self.structured_config.router_bgp.neighbors.append(neighbor)

                for subinterface in link.subinterfaces:
                    subinterface_vrf = subinterface.vrf
                    # We need to add basic BGP VRF config in case the device is not covered by network_services. (Like a spine)
                    if subinterface_vrf not in self.structured_config.router_bgp.vrfs:
                        self.structured_config.router_bgp.vrfs.append_new(name=subinterface_vrf, router_id=self.shared_utils.router_id)

                    if subinterface.peer_ipv6_address is not None:
                        self.structured_config.router_bgp.vrfs[subinterface_vrf].neighbors.append_new(
                            ip_address=cast("str", subinterface.peer_ipv6_address),
                            peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                            remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                            description=f"{f'{link.peer}_{subinterface.peer_interface}'}_vrf_{subinterface_vrf}",
                            bfd=link.bfd,
                        )
                    else:
                        self.structured_config.router_bgp.vrfs[subinterface_vrf].neighbors.append_new(
                            ip_address=cast("str", subinterface.peer_ip_address),
                            peer_group=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                            remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                            description=f"{f'{link.peer}_{subinterface.peer_interface}'}_vrf_{subinterface_vrf}",
                            bfd=link.bfd,
                        )

    def _validate_underlay_ibgp_links(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Validate that all uplink and downlink switches are iBGP underlay routers with p2p links and the same BGP AS.

        Uses the underlay links, which already hold the uplinks of the downlink switches towards this node.
        """
        uplink_peers = set(self.facts.uplink_peers)
        for link in self._underlay_links:
            direction = "uplink" if link.peer in uplink_peers else "downlink"
            reason = None
            if (peer_protocol := self.shared_utils.get_peer_facts(link.peer).underlay_routing_protocol) != "ibgp":
                reason = f"uses 'underlay_routing_protocol: {peer_protocol}'"
            elif link.type != "underlay_p2p":
                reason = f"connects with uplinks of type '{link.type}'"
            elif link.peer_bgp_as is None:
                reason = "is not an underlay router"

            if reason is not None:
                msg = (
                    "Invalid combination of inputs. 'underlay_routing_protocol: ibgp' requires all uplink and downlink switches to be 'ibgp' underlay "
                    f"routers with 'uplink_type: p2p', but {direction} switch '{link.peer}' {reason}."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            if (peer_bgp_as := self.shared_utils.get_asn(link.peer_bgp_as)) != self.shared_utils.formatted_bgp_as:
                msg = (
                    "Invalid combination of inputs. 'underlay_routing_protocol: ibgp' requires the same 'bgp_as' on all fabric nodes, "
                    f"but {direction} switch '{link.peer}' has '{peer_bgp_as}' and this node has '{self.shared_utils.formatted_bgp_as}'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

    def _set_underlay_ibgp_neighbor_interfaces(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set RFC5549 neighbor interfaces for 'underlay_routing_protocol: ibgp'.

        Uses one peer group towards uplink switches and one towards downlink switches.
        """
        uplink_peers = set(self.facts.uplink_peers)
        for link in self._underlay_p2p_links:
            if link.peer in uplink_peers:
                self.structured_config_utils.set_once_peer_group_rr_underlay_peers()
                peer_group = self.inputs.bgp_peer_groups.rr_underlay_peers.name
            else:
                self.structured_config_utils.set_once_peer_group_rr_clients_underlay_peers()
                peer_group = self.inputs.bgp_peer_groups.rr_clients_underlay_peers.name

            self.structured_config.router_bgp.neighbor_interfaces.append_new(
                name=link.interface,
                peer_group=peer_group,
                remote_as=self.shared_utils.get_asn(link.peer_bgp_as),
                metadata=EosCliConfigGen.RouterBgp.NeighborInterfacesItem.Metadata(peer=link.peer),
                description=f"{link.peer}_{link.peer_interface}",
            )
