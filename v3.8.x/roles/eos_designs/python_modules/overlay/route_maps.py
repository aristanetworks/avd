from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort

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

        TODO
        """
        if self._overlay_mpls is True:
            # some logic
            pass
        if self._overlay_evpn is True:
            # some logic
            pass

        route_maps = {}

        if self._overlay_routing_protocol == "ebgp":
            if self._evpn_prevent_readvertise_to_server is True:
                remote_asns = natural_sort(set(rs_dict.get("bgp_as") for route_server, rs_dict in self._evpn_route_servers.items()))
                for remote_asn in remote_asns:
                    route_map_name = f"RM-EVPN-FILTER-AS{ remote_asn }"
                    route_maps[route_map_name] = {
                        "sequence_numbers": {
                            10: {
                                "type": "deny",
                                "match": [f"as {remote_asn}"],
                            },
                            20: {
                                "type": "permit",
                            },
                        }
                    }

        elif self._overlay_routing_protocol == "ibgp":
            if self._vtep_ip is not None:
                # Route-map IN and OUT for SOO
                route_maps["RM-EVPN-SOO-IN"] = {
                    "sequence_numbers": {
                        10: {
                            "type": "deny",
                            "match": ["extcommunity ECL-EVPN-SOO"],
                        },
                        20: {
                            "type": "permit",
                        },
                    }
                }
                route_maps["RM-EVPN-SOO-OUT"] = {
                    "sequence_numbers": {
                        10: {
                            "type": "permit",
                            "set": [f"extcommunity soo {self._vtep_ip}:1 additive"],
                        },
                    }
                }

        # TODO - maybe need to clean None
        if route_maps:
            return route_maps

        return None
