# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class IpNameServersMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_name_servers(self) -> dict | None:
        """
        ip_name_servers set based on "dns_settings" data-model or the deprecated "name_servers" input data-model.

        Servers in the new data model may have management VRFs dynamically set.
        """
        dns_settings_servers = get(self._hostvars, "dns_settings.servers", default=[])
        ip_name_servers = self._name_servers

        if not dns_settings_servers:
            return ip_name_servers or None

        has_mgmt_ip = (self.shared_utils.mgmt_ip is not None) or (self.shared_utils.ipv6_mgmt_ip is not None)
        for server in dns_settings_servers:
            server = server.copy()  # Shallow copy to avoid popping in the original.

            # Initialize a set with vrf defined under the server
            vrfs = set()
            if (vrf := server.pop("vrf", None)) is not None:
                vrfs.add(vrf)
            if (use_mgmt_interface_vrf := server.pop("use_mgmt_interface_vrf", False)) is True and has_mgmt_ip:
                vrfs.add(self.shared_utils.mgmt_interface_vrf)

            if (use_inband_mgmt_vrf := server.pop("use_inband_mgmt_vrf", False)) is True and self.shared_utils.inband_mgmt_interface is not None:
                # self.shared_utils.inband_mgmt_vrf returns None for the default VRF, but here we need "default" to avoid duplicates.
                vrfs.add(self.shared_utils.inband_mgmt_vrf or "default")

            if not any([vrfs, use_mgmt_interface_vrf, use_inband_mgmt_vrf]):
                # If no VRFs are defined (and we are not just ignoring missing mgmt config)
                vrfs.add("default")

            # Ensure default VRF is added first
            if "default" in vrfs:
                vrfs.remove("default")
                # Add server without VRF field
                ip_name_servers.append(server)

            for vrf in natural_sort(vrfs):
                # Add server with VRF field.
                ip_name_servers.append({**server, "vrf": vrf})

        return ip_name_servers or None

    @cached_property
    def _name_servers(self) -> list:
        """
        ip_name_servers set based on the deprecated name_servers data-model and mgmt_interface_vrf

        TODO: Remove support in AVD 5.0.0
        """
        return [
            {
                "ip_address": name_server,
                "vrf": self.shared_utils.mgmt_interface_vrf,
            }
            for name_server in get(self._hostvars, "name_servers", default=[])
        ]
