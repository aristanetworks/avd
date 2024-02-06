# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class StaticRoutesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def static_routes(self) -> list[dict] | None:
        """
        Returns structured config for static_routes

        Consist of
        - default route injected for l3interfaces when `set_default_route` is True
          note that only VRF default is supported today.
        """

        static_routes = []

        for l3_interface in self.shared_utils.l3_interfaces:
            interface_name = get(l3_interface, "name", required=True, org_key=f"<node_type_key>...[node={self.shared_utils.hostname}].l3_interfaces[].name]")
            ip_address = get(
                l3_interface,
                "ip_address",
                required=True,
                org_key=f"{self.shared_utils.node_type_key_data['key']}.nodes[name={self.shared_utils.hostname}].l3_interfaces[name={interface_name}.ip]",
            )

            # 'dhcp' is handled at the interface level
            if ip_address == "dhcp":
                continue

            if not l3_interface.get("set_default_route", False):
                # No route to inject
                continue

            gateway = get(
                l3_interface,
                "peer_ip",
                required=True,
                org_key=f"Cannot set a default route for interface {interface_name} because 'peer_ip' is missing",
            )

            static_route = {
                "destination_address_prefix": "0.0.0.0/0",
                "gateway": gateway,
            }

            if static_route not in static_routes:
                static_routes.append(static_route)

        if static_routes:
            return static_routes

        return None
