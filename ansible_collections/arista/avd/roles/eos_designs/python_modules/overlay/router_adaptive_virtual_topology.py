# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class RouterAdaptiveVirtualTopologyMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_adaptive_virtual_topology(self) -> dict | None:
        """
        Return structured config for router path-selection (DPS)
        """
        if not self.shared_utils.sdwan_role:
            return None

        router_adaptive_virtual_topology = {}

        role = self.shared_utils.sdwan_role
        # TODO add a key at node level to indicate this
        if role == "transit":
            role = "transit region"

        router_adaptive_virtual_topology["topology_role"] = role
        router_adaptive_virtual_topology["region"] = {"name": self._wan_region["name"], "id": self._wan_region["id"]}
        router_adaptive_virtual_topology["zone"] = {"name": self._wan_zone["name"], "id": self._wan_zone["id"]}
        router_adaptive_virtual_topology["site"] = {"name": self._wan_site["name"], "id": self._wan_site["id"]}

        # TODO - handle Policy/Profile/VRF here

        return router_adaptive_virtual_topology
