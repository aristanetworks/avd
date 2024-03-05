# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface
from typing import Mapping

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

LOGGER = logging.getLogger(__name__)


class ConfigManager:
    """"""
    def __init__(self, device_name: str, hostvars: Mapping):
        """"""
        self.device_name = device_name
        self.hostvars = hostvars
        self.structured_config = self.get_host_structured_config(host=device_name)
        self.loopback0_mapping = self.get_loopback0_mapping()
        self.vtep_mapping = self.get_vtep_mapping()

    def get_host_structured_config(self, host: str) -> Mapping:
        """Get a specified host's structured configuration from the hostvars.

        Args:
        ----
            host (str): Hostname to retrieve the structured_config.

        Returns:
        -------
            dict: Structured configuration for the host.

        Raises:
        ------
            AristaAvdError: If host is not in hostvars or if its structured_config is not a mapping object.
        """
        if host not in self.hostvars:
            raise AristaAvdError(f"Host '{host}' is missing from the hostvars.")
        struct_cfg = self.hostvars[host]

        # Check if struct_cfg is a mapping object (e.g. Ansible 'hostvars' object or regular dict)
        if not isinstance(struct_cfg, Mapping):
            raise AristaAvdError(f"Host '{host}' structured_config is not a dictionary or dictionary-like object.")

        return struct_cfg

    def get_loopback0_mapping(self) -> list[tuple[str, str]]:
        return self._get_loopback_mappings["loopback0_mapping"]

    def get_vtep_mapping(self) -> list[tuple[str, str]]:
        return self._get_loopback_mappings["vtep_mapping"]

    @cached_property
    def _get_loopback_mappings(self) -> dict:
        """Generate variables for the eos_validate_state tests, which are used in AvdTestBase subclasses.

        These variables include mappings for loopback and VTEP interfaces.

        Returns
        -------
            dict: A dictionary containing:
            - "loopback0_mapping": a list of tuples where each tuple contains a hostname and its Loopback0 IP address.
            - "vtep_mapping": a list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.

        """
        results = {"loopback0_mapping": [], "vtep_mapping": []}

        for host in self.hostvars:
            host_struct_cfg = self.get_host_structured_config(host)
            loopback_interfaces = host_struct_cfg.get("loopback_interfaces", [])
            for loopback_interface in loopback_interfaces:
                if loopback_interface.get("name") == "Loopback0":
                    if (loopback_ip := loopback_interface.get("ip_address")) is None:
                        LOGGER.warning("Variable 'ip_address' of interface 'Loopback0' is missing.")
                        continue
                    results["loopback0_mapping"].append((host, str(ip_interface(loopback_ip).ip)))

            # If the host is a VTEP, add the VTEP IP to the mapping
            vtep_interface = get(host_struct_cfg, "vxlan_interface.Vxlan1.vxlan.source_interface")
            if vtep_interface is not None:
                if (loopback_interface := get_item(loopback_interfaces, "name", vtep_interface)) is None:
                    LOGGER.warning("Interface %s is missing.", vtep_interface)
                    continue
                if (loopback_ip := loopback_interface.get("ip_address")) is None:
                    LOGGER.warning("Variable 'ip_address' of interface '%s' is missing.", vtep_interface)
                    continue
                results["vtep_mapping"].append((host, str(ip_interface(loopback_ip).ip)))
        return results
