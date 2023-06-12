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

        Only used for EVPN services in VRF "default"
        """
        if not self._vrf_default_evpn:
            return None

        subnets = self._vrf_default_ipv4_subnets
        static_routes = self._vrf_default_ipv4_static_routes["static_routes"]
        if not subnets and not static_routes:
            return None

        prefix_lists = []
        if subnets:
            prefix_list = {"name": "PL-SVI-VRF-DEFAULT", "sequence_numbers": []}
            for index, subnet in enumerate(subnets):
                sequence = 10 * (index + 1)
                prefix_list["sequence_numbers"].append({"sequence": sequence, "action": f"permit {subnet}"})
            prefix_lists.append(prefix_list)

        if static_routes:
            prefix_list = {"name": "PL-STATIC-VRF-DEFAULT", "sequence_numbers": []}
            for index, static_route in enumerate(static_routes):
                sequence = 10 * (index + 1)
                prefix_list["sequence_numbers"].append({"sequence": sequence, "action": f"permit {static_route}"})
            prefix_lists.append(prefix_list)
        return prefix_lists
