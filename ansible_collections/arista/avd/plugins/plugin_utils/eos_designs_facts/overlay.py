from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

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
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.evpn_role

    @cached_property
    def mpls_overlay_role(self):
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.mpls_overlay_role

    @cached_property
    def evpn_route_servers(self):
        """
        Exposed in avd_switch_facts

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
        """
        Exposed in avd_switch_facts
        """
        if self.shared_utils.underlay_router is True:
            if self.mpls_overlay_role in ["client", "server"] or (self.evpn_role in ["client", "server"] and self.overlay["evpn_mpls"]):
                return get(self.shared_utils.switch_data_combined, "mpls_route_reflectors")
        return None

    @cached_property
    def overlay(self) -> dict:
        """
        Exposed in avd_switch_facts
        """
        return {
            "peering_address": self.shared_utils.overlay_peering_address,
            "evpn_mpls": self.shared_utils.overlay_evpn_mpls,
        }
