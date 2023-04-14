from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class RoutingMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    evpn_role: str
    mpls_overlay_role: str
    hostname: str
    hostvars: dict
    id: int
    mlag: bool
    mlag_switch_ids: dict
    mpls_lsr: bool
    node_type_key_data: dict
    switch_data_combined: dict
    underlay_router: bool
    underlay_ipv6: bool
    uplink_type: str

    @cached_property
    def underlay_routing_protocol(self) -> str:
        default_underlay_routing_protocol = get(self.node_type_key_data, "default_underlay_routing_protocol", default="ebgp")
        underlay_routing_protocol = str(get(self.hostvars, "underlay_routing_protocol", default=default_underlay_routing_protocol)).lower()
        return underlay_routing_protocol

    @cached_property
    def overlay_routing_protocol(self) -> str:
        default_overlay_routing_protocol = get(self.node_type_key_data, "default_overlay_routing_protocol", default="ebgp")
        overlay_routing_protocol = str(get(self.hostvars, "overlay_routing_protocol", default=default_overlay_routing_protocol)).lower()
        return overlay_routing_protocol

    @cached_property
    def overlay_address_families(self) -> list:
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            default_overlay_address_families = get(self.node_type_key_data, "default_overlay_address_families", ["evpn"])
            return get(self.switch_data_combined, "overlay_address_families", default=default_overlay_address_families)
        return []

    @cached_property
    def bgp(self) -> bool:
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
    def router_id(self) -> str | None:
        """
        Render IP address for router_id
        """
        if self.underlay_router:
            return self.ip_addressing.router_id()
        return None

    @cached_property
    def ipv6_router_id(self) -> str | None:
        """
        Render IPv6 address for router_id
        """
        if self.underlay_router and self.underlay_ipv6:
            return self.ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def isis_instance_name(self) -> str | None:
        if self.underlay_router:
            if self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
                if self.mpls_lsr:
                    default_isis_instance_name = "CORE"
                else:
                    default_isis_instance_name = "EVPN_UNDERLAY"
                return get(self.hostvars, "underlay_isis_instance_name", default=default_isis_instance_name)
        return None

    @cached_property
    def bgp_as(self) -> str | None:
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
        if self.underlay_routing_protocol == "ebgp" or self.evpn_role != "none" or self.mpls_overlay_role != "none":
            if get(self.hostvars, "bgp_as") is not None:
                return str(get(self.hostvars, "bgp_as"))
            else:
                bgp_as_range_expanded = range_expand(str(get(self.switch_data_combined, "bgp_as", required=True)))
                try:
                    if len(bgp_as_range_expanded) == 1:
                        return bgp_as_range_expanded[0]
                    elif self.mlag:
                        return bgp_as_range_expanded[self.mlag_switch_ids["primary"] - 1]
                    else:
                        if self.id is None:
                            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required when expanding 'bgp_as'")
                        return bgp_as_range_expanded[self.id - 1]
                except IndexError as exc:
                    raise AristaAvdError(
                        f"Unable to allocate BGP AS: bgp_as range is too small ({len(bgp_as_range_expanded)}) for the id of the device"
                    ) from exc

        # Hack to make mpls PR non-breaking, adds empty bgp to igp topology spines
        # TODO: Remove this as part of AVD4.0
        elif self.underlay_routing_protocol in ["isis", "ospf"] and self.evpn_role == "none" and get(self.hostvars, "bgp_as") is not None:
            return str(get(self.hostvars, "bgp_as"))
