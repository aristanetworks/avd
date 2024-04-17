# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate

from .utils import UtilsMixin


class MonitorConnectivityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def monitor_connectivity(self) -> dict | None:
        """
        Return structured config for monitor_connectivity

        Only used for CV Pathfinder routers today
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        monitor_connectivity = {}
        interface_sets = []
        hosts = []

        # TODO mayb append if no duplicate
        for policy in self._filtered_internet_exit_policies:
            for connection in policy["connections"]:
                if connection["type"] == "tunnel":
                    interface_sets.append(
                        {
                            "name": f"SET-Tunnel{connection['tunnel_id']}",
                            "interfaces": f"Tunnel{connection['tunnel_id']}",
                        }
                    )

                    host = {
                        "name": f"IE-Tunnel{connection['tunnel_id']}",
                        "description": connection["description"],
                        "ip": connection["tunnel_destination_ip"],
                        "local_interfaces": f"SET-Tunnel{connection['tunnel_id']}",
                        "address_only": False,
                        "url": connection["monitor_url"],
                    }
                    append_if_not_duplicate(
                        list_of_dicts=hosts,
                        primary_key="name",
                        new_dict=host,
                        context="Monitor connectivity host for Internet Exit policy",
                        context_keys=["name"],
                    )

        monitor_connectivity["interface_sets"] = interface_sets
        monitor_connectivity["hosts"] = hosts

        monitor_connectivity = strip_empties_from_dict(monitor_connectivity)

        if monitor_connectivity:
            return monitor_connectivity

        return None
