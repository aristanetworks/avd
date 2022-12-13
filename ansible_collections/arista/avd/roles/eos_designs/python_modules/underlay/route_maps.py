from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class RouteMapsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def route_maps(self) -> dict | None:
        """
        Return structured config for route_maps

        Contains two parts.
        - Route map for connected routes redistribution in BGP
        - Route map to filter peer AS in uderlay
        """
        if self._underlay_bgp is not True:
            return None

        route_maps = {}

        if self._overlay_routing_protocol != "none":
            # RM-CONN-2-BGP
            sequence_numbers = {}
            sequence_numbers[10] = {
                "type": "permit",
                "match": ["ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"],
            }

            # SEQ 20 is set by inband management if applicable, so avoid setting that here

            if self._underlay_ipv6 is True:
                sequence_numbers[30] = {
                    "type": "permit",
                    "match": ["ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6"],
                }

            route_maps["RM-CONN-2-BGP"] = {"sequence_numbers": sequence_numbers}

        # RM-BGP-AS{{ asn }}-OUT
        for asn in self._underlay_filter_peer_as_route_maps_asns:
            route_map_name = f"RM-BGP-AS{ asn }-OUT"
            route_maps[route_map_name] = {
                "sequence_numbers": {
                    10: {
                        "type": "deny",
                        "match": [f"as { asn }"],
                    },
                    20: {
                        "type": "permit",
                    },
                },
            }

        if route_maps:
            return route_maps

        return None
