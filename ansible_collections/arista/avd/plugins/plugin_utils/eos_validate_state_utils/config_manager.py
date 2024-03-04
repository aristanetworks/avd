# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Mapping

import logging

from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

from .mixins import LoggingMixin

LOGGER = logging.getLogger(__name__)


class ConfigManager(LoggingMixin):
    """"""
    def __init__(self, device_name: str, hostvars: Mapping):
        """"""
        self.device_name = device_name
        self.hostvars = hostvars
        self.structured_config = self.get_host_structured_config(host=device_name)
        self.loopback0_mapping = self.get_loopback0_mapping()
        self.vtep_mapping = self.get_vtep_mapping()

    def logged_get(self, key: str, host: str | None = None, logging_level: str = "INFO"):
        """
        Attempts to retrieve a value associated with a given key from structured_config and logs if it's missing.

        Args:
            key (str): The key to retrieve.
            host (str | None): The host from which to retrieve the key. Defaults to the device running the test.
            logging_level (str): The logging level to use for the log message. Defaults to "INFO".
        """
        host_struct_cfg = self.get_host_structured_config(host=host) if host else self.structured_config
        try:
            return get(host_struct_cfg, key, required=True, separator="..")
        except AristaAvdMissingVariableError:
            self.log_skip_message(key=key, logging_level=logging_level)
            return None

    def get_host_structured_config(self, host: str) -> Mapping:
        """
        Get a specified host's structured configuration from the hostvars.

        Args:
            host (str): Hostname to retrieve the structured_config.

        Returns:
            dict: Structured configuration for the host.

        Raises:
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
        return self._get_mappings["loopback0_mapping"]

    def get_vtep_mapping(self) -> list[tuple[str, str]]:
        return self._get_mappings["vtep_mapping"]

    @cached_property
    def _get_mappings(self) -> dict:
        """
        Generates variables for the eos_validate_state tests, which are used in AvdTestBase subclasses.
        These variables include mappings for loopback and VTEP interfaces.

        Returns:
            dict: A dictionary containing:
                - "loopback0_mapping": a list of tuples where each tuple contains a hostname and its Loopback0 IP address.
                - "vtep_mapping": a list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.

        # FIXME @cbaillar: Need to refactor this: https://github.com/aristanetworks/avd/issues/3304
        """
        results = {"loopback0_mapping": [], "vtep_mapping": []}

        for host in self.hostvars:
            loopback_interfaces = get(self.hostvars, f"{host}..loopback_interfaces", [], separator="..")
            for loopback_interface in loopback_interfaces:
                # TODO Add more conditions here to avoid using type `l3leaf` in connectivity tests; router_id or update_source maybe?
                if loopback_interface["name"] == "Loopback0":
                    try:
                        loopback_ip = get(loopback_interface, "ip_address", required=True)
                        results["loopback0_mapping"].append((host, str(ip_interface(loopback_ip).ip)))
                    except AristaAvdMissingVariableError as e:
                        LOGGER.warning("Variable '%s' is missing. Please validate the Loopback interfaces data model of this host.", str(e))
                        continue

            vtep_interface = get(self.hostvars, f"{host}..vxlan_interface..Vxlan1..vxlan..source_interface", separator="..")
            if vtep_interface is not None:
                try:
                    loopback_interface = get_item(loopback_interfaces, "name", vtep_interface, required=True, var_name=f"name: {vtep_interface}")
                    loopback_ip = get(loopback_interface, "ip_address", required=True)
                    results["vtep_mapping"].append((host, str(ip_interface(loopback_ip).ip)))
                except AristaAvdMissingVariableError as e:
                    LOGGER.warning("Variable '%s' is missing. Please validate the Loopback interfaces data model of this host.", str(e))
                    continue

        return results
