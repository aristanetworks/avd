from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class BgpPeerGroupsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    hostvars: dict
    underlay_router: bool

    @cached_property
    def bgp_peer_groups(self):
        """
        Get bgp_peer_groups configurations or fallback to defaults

        Supporting legacy uppercase keys as well.
        """
        if self.underlay_router is True:
            return {
                "ipv4_underlay_peers": {
                    "name": get(self.hostvars, "bgp_peer_groups.ipv4_underlay_peers.name", default="IPv4-UNDERLAY-PEERS"),
                    "password": get(self.hostvars, "bgp_peer_groups.ipv4_underlay_peers.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.ipv4_underlay_peers.structured_config"),
                },
                "mlag_ipv4_underlay_peer": {
                    "name": get(self.hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.name", default="MLAG-IPv4-UNDERLAY-PEER"),
                    "password": get(self.hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config"),
                },
                "evpn_overlay_peers": {
                    "name": get(self.hostvars, "bgp_peer_groups.evpn_overlay_peers.name", default="EVPN-OVERLAY-PEERS"),
                    "password": get(self.hostvars, "bgp_peer_groups.evpn_overlay_peers.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.evpn_overlay_peers.structured_config"),
                },
                "evpn_overlay_core": {
                    "name": get(self.hostvars, "bgp_peer_groups.evpn_overlay_core.name", default="EVPN-OVERLAY-CORE"),
                    "password": get(self.hostvars, "bgp_peer_groups.evpn_overlay_core.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.evpn_overlay_core.structured_config"),
                },
                "mpls_overlay_peers": {
                    "name": get(self.hostvars, "bgp_peer_groups.mpls_overlay_peers.name", default="MPLS-OVERLAY-PEERS"),
                    "password": get(self.hostvars, "bgp_peer_groups.mpls_overlay_peers.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.mpls_overlay_peers.structured_config"),
                },
                "rr_overlay_peers": {
                    "name": get(self.hostvars, "bgp_peer_groups.rr_overlay_peers.name", default="RR-OVERLAY-PEERS"),
                    "password": get(self.hostvars, "bgp_peer_groups.rr_overlay_peers.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.rr_overlay_peers.structured_config"),
                },
                "ipvpn_gateway_peers": {
                    "name": get(self.hostvars, "bgp_peer_groups.ipvpn_gateway_peers.name", default="IPVPN-GATEWAY-PEERS"),
                    "password": get(self.hostvars, "bgp_peer_groups.ipvpn_gateway_peers.password"),
                    "structured_config": get(self.hostvars, "bgp_peer_groups.ipvpn_gateway_peers.structured_config"),
                },
            }
        return None
