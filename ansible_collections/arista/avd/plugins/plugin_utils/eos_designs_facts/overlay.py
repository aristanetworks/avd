from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class OverlayMixin:
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to the EosDesignsFacts class
    """

    _hostvars: dict
    _vlans: list
    inband_management_vlan: int
    shared_utils: SharedUtils

    @cached_property
    def evpn_role(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.underlay_router is True:
            default_evpn_role = get(self.shared_utils.node_type_key_data, "default_evpn_role", default="none")
            return get(self.shared_utils.switch_data_combined, "evpn_role", default=default_evpn_role)
        return None

    @cached_property
    def mpls_overlay_role(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.underlay_router is True:
            default_mpls_overlay_role = get(self.shared_utils.node_type_key_data, "default_mpls_overlay_role", default="none")
            return get(self.shared_utils.switch_data_combined, "mpls_overlay_role", default=default_mpls_overlay_role)
        return None

    @cached_property
    def evpn_route_servers(self):
        """
        REQUIRED in avd_switch_facts

        For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
        For all other evpn roles there is no default.
        """
        if self.shared_utils.underlay_router is True:
            if self.evpn_role == "client":
                return get(self.shared_utils.switch_data_combined, "evpn_route_servers", default=self.shared_utils.uplink_switches)
            else:
                return get(self.shared_utils.switch_data_combined, "evpn_route_servers")
        return []

    @cached_property
    def mpls_route_reflectors(self):
        """REQUIRED in avd_switch_facts"""
        if self.shared_utils.underlay_router is True:
            if self.mpls_overlay_role in ["client", "server"] or (self.evpn_role in ["client", "server"] and self.overlay["evpn_mpls"]):
                return get(self.shared_utils.switch_data_combined, "mpls_route_reflectors")
        return None

    @cached_property
    def overlay(self) -> dict:
        """
        REQUIRED in avd_switch_facts

        Returns a dictionary of overlay parameters to configure on the node.
        """
        # Set overlay.peering_address to use
        if self._overlay_routing_protocol_address_family == "ipv6":
            peering_address = self.shared_utils.ipv6_router_id
        else:
            peering_address = self.shared_utils.router_id

        cvx = self.shared_utils.overlay_routing_protocol == "cvx"
        her = self.shared_utils.overlay_routing_protocol == "her"
        # Set overlay.evpn_vxlan and overlay.evpn_mpls to differentiate between VXLAN and MPLS use cases.
        evpn_vxlan = self._overlay_evpn and self._evpn_encapsulation == "vxlan"
        evpn_mpls = self._overlay_evpn and self._evpn_encapsulation == "mpls"
        # Set dpath based on ipvpn_gateway parameters
        dpath = self._overlay_ipvpn_gateway and get(self.shared_utils.switch_data_combined, "ipvpn_gateway.enable_d_path", default=True)

        return {
            "peering_address": peering_address,
            "ler": self._overlay_ler,
            "vtep": self._overlay_vtep,
            "cvx": cvx,
            "her": her,
            "evpn": self._overlay_evpn,
            "evpn_vxlan": evpn_vxlan,
            "evpn_mpls": evpn_mpls,
            "vpn_ipv4": self._overlay_vpn_ipv4,
            "vpn_ipv6": self._overlay_vpn_ipv6,
            "ipvpn_gateway": self._overlay_ipvpn_gateway,
            "dpath": dpath,
        }

    @cached_property
    def _overlay_routing_protocol_address_family(self):
        overlay_routing_protocol_address_family = get(self._hostvars, "overlay_routing_protocol_address_family", default="ipv4")
        if overlay_routing_protocol_address_family == "ipv6":
            if not (get(self._hostvars, "underlay_ipv6") is True and get(self._hostvars, "underlay_rfc5549") is True):
                raise AristaAvdError(
                    "'overlay_routing_protocol_address_family: ipv6' is only supported in combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
                )
        return overlay_routing_protocol_address_family

    @cached_property
    def _evpn_encapsulation(self):
        """
        EVPN encapsulation based on fabric_evpn_encapsulation and node default_evpn_encapsulation.
        """
        return get(
            self._hostvars, "fabric_evpn_encapsulation", default=get(self.shared_utils.node_type_key_data, "default_evpn_encapsulation", default="vxlan")
        )

    @cached_property
    def _overlay_evpn(self) -> bool:
        # Set overlay.evpn to enable EVPN on the node
        return (
            self.shared_utils.bgp
            and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
            and self.shared_utils.overlay_routing_protocol in ["ebgp", "ibgp"]
            and "evpn" in self.shared_utils.overlay_address_families
        )

    @cached_property
    def _overlay_ipvpn_gateway(self) -> bool:
        # Set ipvpn_gateway to trigger ipvpn interworking configuration.
        return self._overlay_evpn and get(self.shared_utils.switch_data_combined, "ipvpn_gateway.enabled", default=False)

    @cached_property
    def _overlay_ler(self) -> bool:
        return (
            self.shared_utils.underlay_mpls
            and (self.mpls_overlay_role in ["client", "server"] or self.evpn_role in ["client", "server"])
            and (self.shared_utils.any_network_services)
        )

    @cached_property
    def _overlay_vtep(self) -> bool:
        # Set overlay.vtep to enable VXLAN edge PE features
        return (
            self.shared_utils.overlay_routing_protocol in ["ebgp", "ibgp", "her", "cvx"]
            and (self.shared_utils.network_services_l2 or self.shared_utils.network_services_l3)
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type == "p2p"
            and self.shared_utils.vtep
        )

    @cached_property
    def _overlay_vpn_ipv4(self) -> bool:
        # Set overlay.vpn_ipv4 and vpn_ipv6 to enable IP-VPN configuration on the node.
        if self.shared_utils.bgp is not True:
            return False

        return (self.shared_utils.overlay_routing_protocol == "ibgp" and "vpn-ipv4" in self.shared_utils.overlay_address_families) or (
            "vpn-ipv4" in get(self.shared_utils.switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self._overlay_ipvpn_gateway
        )

    @cached_property
    def _overlay_vpn_ipv6(self) -> bool:
        # Set overlay.vpn_ipv4 and vpn_ipv6 to enable IP-VPN configuration on the node.
        if self.shared_utils.bgp is not True:
            return False

        return (self.shared_utils.overlay_routing_protocol == "ibgp" and "vpn-ipv6" in self.shared_utils.overlay_address_families) or (
            "vpn-ipv6" in get(self.shared_utils.switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self._overlay_ipvpn_gateway
        )
