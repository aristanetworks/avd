# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class RouterServiceInsertionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_service_insertion(self) -> dict | None:
        """
        Return structured config for router_service_insertion

        Only used for CV Pathfinder routers today
        """
        if not self._filtered_internet_exit_policies:
            return None

        router_service_insertion = {}
        connections = []

        for policy in self._filtered_internet_exit_policies:
            for connection in policy.get("connections", []):
                if connection["type"] == "tunnel":
                    connections.append(
                        {
                            "name": f"IE-Tunnel{connection['tunnel_id']}",
                            "tunnel_interface": {
                                "primary": f"Tunnel{connection['tunnel_id']}",
                            },
                            # TODO this host need to match monitor connectivity, maybe centralize name generation in utils
                            "monitor_connectivity_host": f"IE-Tunnel{connection['tunnel_id']}",
                        }
                    )

        if connections:
            router_service_insertion["enabled"] = True
            router_service_insertion["connections"] = connections

        if router_service_insertion:
            return router_service_insertion

        return None
