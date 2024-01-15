# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class RouterAdaptiveVirtualTopologyMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_adaptive_virtual_topology(self) -> dict | None:
        """
        Return structured config for router adaptive-virtual-topology (AVT)
        """
        if not (role := self.shared_utils.cv_pathfinder_role):
            return None

        router_adaptive_virtual_topology = {"topology_role": role}

        if role != "pathfinder":
            router_adaptive_virtual_topology.update(
                {
                    "region": {
                        "name": self.shared_utils.wan_region["name"],
                        "id": self.shared_utils.wan_region["id"],
                    },
                    "zone": self.shared_utils.wan_zone,
                    "site": {
                        "name": self.shared_utils.wan_site["name"],
                        "id": self.shared_utils.wan_site["id"],
                    },
                }
            )

        # TODO - handle Policy/Profile/VRF here or rather in network_services in future PR

        return router_adaptive_virtual_topology
