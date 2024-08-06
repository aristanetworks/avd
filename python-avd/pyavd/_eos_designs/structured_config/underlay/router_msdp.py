# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, get_item
from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouterMsdpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_msdp(self: AvdStructuredConfigUnderlay) -> dict | None:
        """
        return structured config for router_msdp.

        Used for to configure multicast anycast RPs for the underlay
        """
        if self.shared_utils.underlay_multicast_rps is None:
            return None

        if self.shared_utils.underlay_multicast_anycast_rp_mode != "msdp":
            return None

        peers = set()
        for rp_entry in self.shared_utils.underlay_multicast_rps:
            if (nodes := get(rp_entry, "nodes")) is None or len(nodes) < 2:
                continue

            if (node_entry := get_item(nodes, "name", self.shared_utils.hostname)) is None:
                continue

            # Anycast-RP using MSDP
            for node in nodes:
                if node == node_entry:
                    continue
                peers.add(node["name"])

        if not peers:
            return None

        return {
            "originator_id_local_interface": "Loopback0",
            "peers": [
                {
                    "ipv4_address": get(self.shared_utils.get_peer_facts(peer), "router_id", required=True),
                    "local_interface": "Loopback0",
                    "description": peer,
                    "mesh_groups": [{"name": "ANYCAST-RP"}],
                }
                for peer in natural_sort(peers)
            ],
        }
