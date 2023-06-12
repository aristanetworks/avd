from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class UnderlayMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_bgp(self: SharedUtils) -> bool:
        return self.bgp and self.underlay_routing_protocol == "ebgp" and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_mpls(self: SharedUtils) -> bool:
        return (
            self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.mpls_lsr
            and self.underlay_router
            and self.uplink_type == "p2p"
        )

    @cached_property
    def underlay_ldp(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["ospf", "ospf-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_isis(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_ipv6(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_ipv6", default=False) and self.underlay_router

    @cached_property
    def underlay_multicast(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_multicast") and self.underlay_router

    @cached_property
    def underlay_filter_redistribute_connected(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_filter_redistribute_connected", default=True) is True

    @cached_property
    def underlay_rfc5549(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_rfc5549") is True

    @cached_property
    def underlay_ospf_process_id(self: SharedUtils) -> int:
        return get(self.hostvars, "underlay_ospf_process_id", default=100)

    @cached_property
    def underlay_ospf_area(self: SharedUtils) -> str:
        return get(self.hostvars, "underlay_ospf_area", default="0.0.0.0")

    @cached_property
    def underlay_filter_peer_as(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_filter_peer_as") is True and self.evpn_role not in ["client", "server"]
