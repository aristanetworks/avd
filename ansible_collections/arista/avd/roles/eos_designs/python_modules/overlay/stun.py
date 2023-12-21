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
            local_interfaces = [wan_interface.get("interface") for wan_interface in self.shared_utils.wan_interfaces]
            stun["server"] = {"local_interfaces": local_interfaces}

        if self.shared_utils.wan_role == "client":
            server_profiles = []

            for wan_route_server, data in self._wan_route_servers.items():
                for path_group in data.get("wan_path_groups", []):
                    if not self._should_connect_to_wan_rr([path_group["name"]]):
                        continue

                    server_profiles.extend(
                        {
                            "name": self._stun_server_profile_name(wan_route_server, path_group["name"], index),
                            "ip_address": get(interface_dict, "ip_address", required=True),
                        }
                        for index, interface_dict in enumerate(get(path_group, "interfaces", required=True))
                    )
            if server_profiles:
                stun["client"] = {"server_profiles": server_profiles}

        return stun or None
