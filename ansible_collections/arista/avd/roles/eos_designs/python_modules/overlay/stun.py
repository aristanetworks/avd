# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class StunMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def stun(self) -> dict | None:
        """
        Return structured config for stun
        """

        if not self.shared_utils.wan_role:
            return None

        stun = {}
        if self.shared_utils.wan_role == "server":
            local_interfaces = []
            for wan_interface in self.shared_utils.wan_interfaces:
                local_interfaces.append(wan_interface.get("interface"))

            stun["server"] = {"local_interfaces": local_interfaces}

        if self.shared_utils.wan_role == "client":
            server_profiles = []

            local_path_group_names = [path_group["name"] for path_group in self.shared_utils.wan_local_path_groups]

            for wan_route_server, data in self._wan_route_servers.items():
                for path_group in data.get("wan_path_groups", []):
                    if path_group["name"] not in local_path_group_names:
                        continue

                    for index, interface_dict in enumerate(get(path_group, "interfaces", required=True)):
                        # Today one wan_path_group can only have one IP. May need to relax this in the futur
                        server_profiles.append(
                            {
                                "name": self._stun_server_profile_name(wan_route_server, path_group["name"], index),
                                "ip_address": get(interface_dict, "ip_address", required=True),
                            }
                        )

            if server_profiles:
                stun["client"] = {"server_profiles": server_profiles}

        return stun or None
