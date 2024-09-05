# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import default, get

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class RouterOspfMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_ospf(self: AvdStructuredConfigUnderlay) -> dict | None:
        """Return structured config for router_ospf."""
        if self.shared_utils.underlay_ospf is not True:
            return None

        ospf_processes = []

        process_id = self.shared_utils.underlay_ospf_process_id

        no_passive_interfaces = [link["interface"] for link in self._underlay_links if link["type"] == "underlay_p2p"]

        if self.shared_utils.mlag_l3 is True:
            mlag_l3_vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.mlag_peer_vlan)
            no_passive_interfaces.append(f"Vlan{mlag_l3_vlan}")

        process = {
            "id": process_id,
            "passive_interface_default": True,
            "router_id": self.shared_utils.router_id,
            "max_lsa": get(self._hostvars, "underlay_ospf_max_lsa", default=12000),
            "no_passive_interfaces": no_passive_interfaces,
            "bfd_enable": get(self._hostvars, "underlay_ospf_bfd_enable", default=False),
        }

        if self.shared_utils.overlay_routing_protocol == "none":
            process["redistribute"] = {
                "connected": {"enabled": True},
            }

        # Strip None values from process before adding to list
        process = {key: value for key, value in process.items() if value is not None}

        ospf_processes.append(process)

        if ospf_processes:
            return {"process_ids": ospf_processes}

        return None
