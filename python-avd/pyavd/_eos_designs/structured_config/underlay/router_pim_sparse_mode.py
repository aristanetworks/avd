# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, get_item

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouterPimSparseModeMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_pim_sparse_mode(self: AvdStructuredConfigUnderlay) -> dict | None:
        """
        return structured config for router_pim_sparse_mode.

        Used for to configure multicast RPs for the underlay
        """
        if self.shared_utils.underlay_multicast_rps is None:
            return None

        rp_addresses = []
        anycast_rps = []
        for rp_entry in self.shared_utils.underlay_multicast_rps:
            rp_address = {"address": rp_entry["rp"]}
            if rp_entry.get("groups") is not None:
                if (acl := rp_entry.get("access_list_name")) is not None:
                    rp_address["access_lists"] = [acl]
                else:
                    rp_address["groups"] = rp_entry["groups"]

            rp_addresses.append(rp_address)

            if (nodes := get(rp_entry, "nodes")) is None or len(nodes) < 2:
                continue

            if get_item(nodes, "name", self.shared_utils.hostname) is None:
                continue

            if self.shared_utils.underlay_multicast_anycast_rp_mode == "pim":
                # Anycast-RP using PIM (default)
                anycast_rps.append(
                    {
                        "address": rp_entry["rp"],
                        "other_anycast_rp_addresses": [
                            {
                                "address": get(self.shared_utils.get_peer_facts(node["name"]), "router_id", required=True),
                            }
                            for node in nodes
                        ],
                    },
                )

        if rp_addresses:
            router_pim_sparse_mode = {
                "ipv4": {
                    "rp_addresses": rp_addresses,
                },
            }
            if anycast_rps:
                router_pim_sparse_mode["ipv4"]["anycast_rps"] = anycast_rps

            return router_pim_sparse_mode

        return None
