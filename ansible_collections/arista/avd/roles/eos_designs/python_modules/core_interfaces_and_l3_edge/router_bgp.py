# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict

from .utils import UtilsMixin


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Return structured config for router_bgp
        """
        router_bgp = {
            "neighbors": [],
            "neighbor_interfaces": [],
        }

        self._router_bgp_p2p_links(router_bgp)
        self._router_bgp_l3_interfaces(router_bgp)

        return strip_empties_from_dict(router_bgp) or None

    def _router_bgp_p2p_links(self, router_bgp: dict) -> None:
        """
        In place update of neighbor and / or neighbor_interfaces
        """
        if not self.shared_utils.underlay_bgp:
            return

        for p2p_link in self._filtered_p2p_links:
            if not (p2p_link.get("include_in_underlay_protocol", True) is True):
                continue

            if p2p_link["data"]["bgp_as"] is None or p2p_link["data"]["peer_bgp_as"] is None:
                raise AristaAvdMissingVariableError("l3_edge.p2p_links.[].as")

            neighbor = {
                "remote_as": p2p_link["data"]["peer_bgp_as"],
                "peer": p2p_link["data"]["peer"],
                "description": p2p_link["data"]["peer"],
                "peer_group": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
            }

            # RFC5549
            if self.shared_utils.underlay_rfc5549:
                router_bgp["neighbor_interfaces"].append({"name": p2p_link["data"]["interface"], **neighbor})
                continue

            # Regular BGP Neighbors
            if p2p_link["data"]["ip"] is None or p2p_link["data"]["peer_ip"] is None:
                raise AristaAvdMissingVariableError("l3_edge.p2p_links.[].ip, .subnet or .ip_pool")

            neighbor["bfd"] = p2p_link.get("bfd")
            if p2p_link["data"]["bgp_as"] != self.shared_utils.bgp_as:
                neighbor["local_as"] = p2p_link["data"]["bgp_as"]

            # Remove None values
            neighbor = {key: value for key, value in neighbor.items() if value is not None}

            router_bgp["neighbors"].append({"ip_address": p2p_link["data"]["peer_ip"].split("/")[0], **neighbor})
        return

    def _router_bgp_l3_interfaces(self, router_bgp: dict) -> None:
        """
        In place update of router_bgp / neighbors
        """
        # Review
        for l3_interface in self._filtered_l3_interfaces:
            local_as = l3_interface.get("bgp_as")
            remote_as = l3_interface.get("peer_bgp_as")
            if local_as is None and remote_as is None:
                # No BGP config for this interface
                continue
            # One or the other is set
            neighbor_as = local_as if remote_as is None else remote_as

            neighbor = {
                "remote_as": neighbor_as,
                "peer": l3_interface["peer"],
                "description": f"{l3_interface['peer']}",
            }

            # RFC5549
            if self.shared_utils.underlay_rfc5549:
                router_bgp["neighbor_interfaces"].append({"name": l3_interface["interface"], **neighbor})
                continue

            # Regular BGP Neighbors
            if l3_interface.get("peer_ip") is None:
                raise AristaAvdMissingVariableError("l3_edge.l3_interfaces.[].peer_ip")
            peer_ip = l3_interface["peer_ip"].split("/")[0]

            neighbor["bfd"] = l3_interface.get("bfd")

            if local_as != self.shared_utils.bgp_as:
                neighbor["local_as"] = local_as

            # Remove None values
            neighbor = {key: value for key, value in neighbor.items() if value is not None}

            router_bgp["neighbors"].append({"ip_address": peer_ip, **neighbor})

            address_family = f"address_family_ipv{ipaddress.ip_address(peer_ip).version}"
            af_neighbor = {
                "ip_address": peer_ip,
                "activate": True,
            }

            router_bgp.setdefault(address_family, {}).setdefault("neighbors", []).append(af_neighbor)

        return
