# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

LOGGER = logging.getLogger(__name__)


class AvdTestBase:
    """
    Base class for all AVD eos_validate_state tests.
    """

    def __init__(self, device_name: str, hostvars: dict):
        """
        Initialize the AvdTestBase class.

        Args:
            device_name (str): The current device name for which the plugin is being run
            hostvars (dict): A dictionnary that contains a key for each device with a value of the structured_config
                           when using Ansible, this is the equivalent of `task_vars['hostvars']`
        """
        self.hostvars = hostvars
        self.device_name = device_name

    def render(self) -> dict:
        """
        Return the test_definition of the class.

        This method attempts to retrieve the value of the `test_definition` attribute.
        If `test_definition` is not set or returns a falsy value (e.g., None),
        an empty dictionary will be returned instead.

        Returns:
            dict: The test definition if available and valid; otherwise, an empty dictionary.
        """
        return getattr(self, "test_definition", None) or {}

    def is_peer_available(self, peer: str) -> bool:
        """
        TODO
        """
        if peer not in self.hostvars:
            LOGGER.warning("Peer %s is not configured by AVD.", peer)
            return False
        elif not get(self.hostvars[peer], "is_deployed", default=True):
            LOGGER.warning("Peer %s is marked as not deployed.", peer)
            return False
        return True

    def get_interface_ip(self, interface_model: str, interface_name: str, host: str | None = None) -> str | None:
        """
        Retrieve the IP address of a specified peer interface.

        Parameters:
            hostvars (dict): A dictionnary that contains a key for each device with a value of the structured_config.
                              When using Ansible, this is the equivalent of `task_vars['hostvars']`.
            peer (str): Peer whose interface information is retrieved.
            interface_model (str): Type of interface (e.g., ethernet_interfaces).
            peer_interface_name (str): Name of the peer interface.

        Returns:
          str | None: IP address of the peer interface or None if unavailable.
        """
        host = host if host else self.device_name

        try:
            peer_interfaces = get(self.hostvars[host], interface_model, required=True)
            peer_interface = get_item(peer_interfaces, "name", interface_name, required=True)
            return get(peer_interface, "ip_address", required=True)
        except AristaAvdMissingVariableError:
            LOGGER.warning("Host %s interface '%s' IP address is unavailable.", host, interface_name)
            return None

    def validate_vars(self, data_model: str, host: str | None = None, loop_through_items: bool = False, required_keys: str | list[str] | None = None, **kwargs):
        """
        TODO
        """

        def _log_message(entry: int, key: str, is_missing=False) -> None:
            msg_type = "missing" if is_missing else "mismatch"
            msg = f"Entry #{entry} from '{data_model}': Variable '{key}' is {msg_type}. {self.__class__.__name__} is skipped for this entry."
            LOGGER.warning(msg) if msg_type == "missing" else LOGGER.info(msg)

        host = host if host else self.device_name

        try:
            data = get(self.hostvars[host], data_model, required=True)
        except AristaAvdMissingVariableError:
            msg = f"Data model '{data_model}' is missing from the structured_config. {self.__class__.__name__} is skipped."
            LOGGER.warning(msg)
            return None

        if loop_through_items:
            if not required_keys:
                raise AristaAvdError(message="'required_keys' must be provided when 'loop_through_items' is set to True")

            required_keys = [required_keys] if isinstance(required_keys, str) else required_keys

            valid_entries = []
            for idx, entries in enumerate(data, start=1):
                valid_entry = True

                # Check the expected key/value pairs first
                for key, value in kwargs.items():
                    if (entry_value := get(entries, key)) is None:
                        _log_message(entry=idx, key=key, is_missing=True)
                        valid_entry = False
                    elif entry_value != value:
                        _log_message(entry=idx, key=key, is_missing=False)
                        valid_entry = False

                # Skip this entry if the expected values are not matching
                if not valid_entry:
                    continue

                # Check the required_keys
                for key in required_keys:
                    if get(entries, key) is None:
                        _log_message(entry=idx, key=key, is_missing=True)
                        valid_entry = False

                # Add this entry to the list
                if valid_entry:
                    valid_entries.append(entries)

            return valid_entries if valid_entries else None

        return data

    @property
    def loopback0_mapping(self) -> dict:
        return self._get_eos_validate_state_vars["loopback0_mapping"]

    @property
    def vtep_mapping(self) -> dict:
        return self._get_eos_validate_state_vars["vtep_mapping"]

    @cached_property
    def _get_eos_validate_state_vars(self) -> dict:
        """
        Generates variables for the eos_validate_state tests, which are used in AvdTestBase subclasses.
        These variables include mappings for loopback and VTEP interfaces.

        Returns:
            dict: A dictionary containing:
                - "loopback0_mapping": a list of tuples where each tuple contains a hostname and its Loopback0 IP address.
                - "vtep_mapping": a list of tuples where each tuple contains a hostname and its VTEP IP address if `Vxlan1` is the source_interface.
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
