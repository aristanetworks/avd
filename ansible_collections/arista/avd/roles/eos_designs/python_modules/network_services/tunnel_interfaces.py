# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class TunnelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def tunnel_interfaces(self) -> list | None:
        """
        Return structured config for tunnel_interfaces

        Only used for CV Pathfinder routers today
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        tunnel_interfaces = []

        for internet_exit_policy in self._filtered_internet_exit_policies:
            for connection in internet_exit_policy.get("connections", []):
                if connection["type"] == "tunnel":
                    tunnel_interface = {
                        "name": f"Tunnel{connection['tunnel_id']}",
                        "description": connection["description"],
                        "mtu": 1394,  # TODO: do not hardcode
                        "ip_address": connection["tunnel_ip_address"],
                        "tunnel_mode": "ipsec",  # TODO: do not hardcode
                        "source_interface": connection["source_interface"],
                        "destination": connection["tunnel_destination_ip"],
                        "ipsec_profile": connection["ipsec_profile"],
                    }

                    if internet_exit_policy["type"] == "zscaler":
                        tunnel_interface["nat_profile"] = "VRF-AWARE-NAT"

                    tunnel_interfaces.append(tunnel_interface)

        if tunnel_interfaces:
            return tunnel_interfaces

        return None
