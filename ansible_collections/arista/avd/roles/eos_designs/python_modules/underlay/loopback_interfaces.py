from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class LoopbackInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def loopback_interfaces(self) -> dict | None:
        """
        Return structured config for loopback_interfaces
        """
        if self._underlay_router is not True:
            return None

        loopback_interfaces = {}
        # Loopback 0
        loopback0 = {
            "description": self._avd_interface_descriptions.overlay_loopback_interface(get(self._hostvars, "overlay_loopback_description")),
            "shutdown": False,
            "ip_address": f"{self._router_id}/32",
        }

        if self._ipv6_router_id is not None:
            loopback0["ipv6_address"] = f"{self._ipv6_router_id}/128"

        if self._underlay_ospf is True:
            loopback0["ospf_area"] = self._underlay_ospf_area

        if self._underlay_ldp is True:
            loopback0["mpls"] = {"ldp": {"interface": True}}

        if self._underlay_isis is True:
            isis_config = {"isis_enable": self._isis_instance_name, "isis_passive": True}
            if self._underlay_sr is True:
                isis_config["node_segment"] = {"ipv4_index": self._node_sid}
                if self._underlay_ipv6 is True:
                    isis_config["node_segment"].update({"ipv6_index": self._node_sid})

            loopback0.update(isis_config)

        loopback0 = {key: value for key, value in loopback0.items() if value is not None}

        loopback_interfaces["Loopback0"] = loopback0

        # VTEP loopback
        if self._overlay_vtep is True and self._vtep_loopback.lower() != "loopback0":
            vtep_loopback = {
                "description": self._avd_interface_descriptions.vtep_loopback_interface(),
                "shutdown": False,
                "ip_address": f"{self._vtep_ip}/32",
            }

            if self._network_services_l3 is True and self._vtep_vvtep_ip is not None:
                vtep_loopback["ip_address_secondaries"] = [self._vtep_vvtep_ip]

            if self._underlay_ospf is True:
                vtep_loopback["ospf_area"] = self._underlay_ospf_area

            if self._underlay_isis is True:
                vtep_loopback.update({"isis_enable": self._isis_instance_name, "isis_passive": True})

            vtep_loopback = {key: value for key, value in vtep_loopback.items() if value is not None}

            loopback_interfaces[self._vtep_loopback] = vtep_loopback

        return loopback_interfaces
