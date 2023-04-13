from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class RoutingMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the SharedUtils class
    """

    hostname: str
    hostvars: dict
    id: int
    mpls_lsr: bool
    node_type_key_data: dict
    switch_data_combined: dict
    underlay_router: bool
    underlay_ipv6: bool
    uplink_type: str

    @cached_property
    def underlay_routing_protocol(self):
        default_underlay_routing_protocol = get(self.node_type_key_data, "default_underlay_routing_protocol", default="ebgp")
        underlay_routing_protocol = str(get(self.hostvars, "underlay_routing_protocol", default=default_underlay_routing_protocol)).lower()
        return underlay_routing_protocol

    @cached_property
    def overlay_routing_protocol(self):
        default_overlay_routing_protocol = get(self.node_type_key_data, "default_overlay_routing_protocol", default="ebgp")
        overlay_routing_protocol = str(get(self.hostvars, "overlay_routing_protocol", default=default_overlay_routing_protocol)).lower()
        return overlay_routing_protocol

    @cached_property
    def overlay_address_families(self):
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            default_overlay_address_families = get(self.node_type_key_data, "default_overlay_address_families", ["evpn"])
            return get(self.switch_data_combined, "overlay_address_families", default=default_overlay_address_families)
        return []

    @cached_property
    def bgp(self):
        """
        Boolean telling if BGP Routing should be configured.
        """
        return (
            self.underlay_router
            and self.uplink_type == "p2p"
            and (
                self.underlay_routing_protocol == "ebgp"
                or (
                    self.overlay_routing_protocol in ["ebgp", "ibgp"]
                    and (
                        get(self.hostvars, "switch.evpn_role") in ["client", "server"] or get(self.hostvars, "switch.mpls_overlay_role") in ["client", "server"]
                    )
                )
            )
        )

    @cached_property
    def router_id(self):
        """
        Render IP address for router_id
        """
        if self.underlay_router:
            return self.ip_addressing.router_id()
        return None

    @cached_property
    def ipv6_router_id(self):
        """
        Render IPv6 address for router_id
        """
        if self.underlay_ipv6:
            return self.ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def isis_instance_name(self):
        if self.underlay_router:
            if self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
                if self.mpls_lsr:
                    default_isis_instance_name = "CORE"
                else:
                    default_isis_instance_name = "EVPN_UNDERLAY"
                return get(self.hostvars, "underlay_isis_instance_name", default=default_isis_instance_name)
        return None
