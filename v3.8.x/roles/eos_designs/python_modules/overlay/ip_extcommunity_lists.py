from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class IpExtCommunityListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_extcommunity_lists(self) -> dict | None:
        """
        Return structured config for ip_extcommunity_lists
        """
        if self._overlay_routing_protocol != "ibgp":
            return None

        if self._vtep_ip is not None:
            return {
                "ECL-EVPN-SOO": [
                    {
                        "type": "permit",
                        "extcommunities": f"soo {self._vtep_ip}:1",
                    },
                ],
            }

        return None
