from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class UnderlayMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    bgp: bool
    hostvars: dict
    node_type_key_data: dict
    underlay_router: bool
    underlay_routing_protocol: str
    uplink_type: str
    mpls_lsr: bool

    @cached_property
    def underlay_bgp(self) -> bool:
        return self.bgp and self.underlay_routing_protocol == "ebgp" and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_mpls(self) -> bool:
        return (
            self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.mpls_lsr
            and self.underlay_router
            and self.uplink_type == "p2p"
        )

    @cached_property
    def underlay_ldp(self) -> bool:
        return self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self) -> bool:
        return self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self) -> bool:
        return self.underlay_routing_protocol in ["ospf", "ospf-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_isis(self) -> bool:
        return self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_ipv6(self) -> bool:
        return get(self.hostvars, "underlay_ipv6") and self.underlay_router

    @cached_property
    def underlay_multicast(self) -> bool:
        return get(self.hostvars, "underlay_multicast") and self.underlay_router
