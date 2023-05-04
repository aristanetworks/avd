from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class PrefixListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def prefix_lists(self) -> dict | None:
        """
        Return structured config for prefix_lists
        """
        if self._underlay_bgp is not True:
            return None

        if self._overlay_routing_protocol == "none":
            return None

        prefix_lists = {}

        # IPv4 - PL-LOOPBACKS-EVPN-OVERLAY
        sequence_numbers = {}
        sequence_numbers[10] = {
            "action": f"permit {self._loopback_ipv4_pool} eq 32",
        }

        if self._vtep_ip is not None and self._vtep_loopback.lower() != "loopback0":
            sequence_numbers[20] = {"action": f"permit {self._vtep_loopback_ipv4_pool} eq 32"}

        if self._vtep_vvtep_ip is not None and self._network_services_l3 is True:
            sequence_numbers[30] = {"action": f"permit {self._vtep_vvtep_ip}"}

        prefix_lists["PL-LOOPBACKS-EVPN-OVERLAY"] = {"sequence_numbers": sequence_numbers}

        return prefix_lists

    @cached_property
    def ipv6_prefix_lists(self) -> dict | None:
        """
        Return structured config for IPv6 prefix_lists
        """
        if self._underlay_bgp is not True:
            return None

        if self._underlay_ipv6 is not True:
            return None

        if self._overlay_routing_protocol == "none":
            return None

        # IPv6 - PL-LOOPBACKS-EVPN-OVERLAY-V6
        return {
            "PL-LOOPBACKS-EVPN-OVERLAY-V6": {
                "sequence_numbers": {
                    10: {
                        "action": f"permit {self._loopback_ipv6_pool} eq 128",
                    }
                }
            }
        }
