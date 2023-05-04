from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class PrefixListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def prefix_lists(self) -> list | None:
        """
        Return structured config for prefix_lists
        """
        if self.shared_utils.underlay_bgp is not True:
            return None

        if self.shared_utils.overlay_routing_protocol == "none":
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        # IPv4 - PL-LOOPBACKS-EVPN-OVERLAY
        sequence_numbers = [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv4_pool} eq 32"}]

        if self.shared_utils.overlay_vtep and self.shared_utils.vtep_loopback.lower() != "loopback0":
            sequence_numbers.append({"sequence": 20, "action": f"permit {self.shared_utils.vtep_loopback_ipv4_pool} eq 32"})

        if self.shared_utils.vtep_vvtep_ip is not None and self.shared_utils.network_services_l3 is True:
            sequence_numbers.append({"sequence": 30, "action": f"permit {self.shared_utils.vtep_vvtep_ip}"})

        prefix_lists = [{"name": "PL-LOOPBACKS-EVPN-OVERLAY", "sequence_numbers": sequence_numbers}]

        return prefix_lists

    @cached_property
    def ipv6_prefix_lists(self) -> dict | None:
        """
        Return structured config for IPv6 prefix_lists
        """
        if self.shared_utils.underlay_bgp is not True:
            return None

        if self.shared_utils.underlay_ipv6 is not True:
            return None

        if self.shared_utils.overlay_routing_protocol == "none":
            return None

        if not self.shared_utils.underlay_filter_redistribute_connected:
            return None

        # IPv6 - PL-LOOPBACKS-EVPN-OVERLAY-V6
        return [
            {"name": "PL-LOOPBACKS-EVPN-OVERLAY-V6", "sequence_numbers": [{"sequence": 10, "action": f"permit {self.shared_utils.loopback_ipv6_pool} eq 128"}]}
        ]
