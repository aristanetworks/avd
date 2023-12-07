# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from collections.abc import Mapping
from functools import cached_property
from ipaddress import ip_interface

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item

LOGGER = logging.getLogger(__name__)
LOGGING_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class AvdTestBase:
    """
    Base class for all AVD eos_validate_state tests.
    """

    def __init__(self, device_name: str, hostvars: dict | object):
        """
        Initialize the AvdTestBase class.

        Args:
            device_name (str): The current device name for which the plugin is being run.
            hostvars (dict | object): A dictionary that contains a key for each device with a value of the structured_config.
                                      When using Ansible, this is the `task_vars['hostvars']` object.
        """
        self.hostvars = hostvars
        self.device_name = device_name
        self.structured_config = self.get_host_struct_cfg(host=device_name)

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

    def get_host_struct_cfg(self, host: str) -> dict:
        """
        Retrieves and returns the structured configuration for a specified host.

        The function fetches the structured_config from hostvars. It ensures the returned object is a non-empty
        dictionary, converting Ansible dictionary-like objects to a standard dictionary if necessary.

        Args:
            host (str): Hostname to retrieve the structured_config.

        Returns:
            dict: Structured configuration for the host.

        Raises:
            AristaAvdError: If host is not in hostvars or if its structured_config is not a dictionary or is empty.
        """
        if host not in self.hostvars:
            raise AristaAvdError(f"Host '{host}' is missing from the hostvars.")
        struct_cfg = get(self.hostvars, host, separator="..")

        # Check if struct_cfg is a dict or behaves like a dict (e.g. Ansible 'hostvars' object)
        if not isinstance(struct_cfg, (dict, Mapping)):
            raise AristaAvdError(f"Host '{host}' structured_config is not a dictionary or dictionary-like object.")

        if not isinstance(struct_cfg, dict):
            struct_cfg = dict(struct_cfg)

        return struct_cfg

    def log_skip_message(
        self, message=None, key: str | None = None, value=None, key_path: str | None = None, is_missing: bool = True, logging_level: str = "INFO"
    ) -> None:
        """
        Logging function that logs the test being skipped appended to a formatted message based on the provided parameters.

        Args:
            message (Any | None): The message to be logged. If provided, it will be logged as is, ignoring other parameters.
            key (str | None): The key to be logged.
            value (Any | None): The expected value of the key. Must be provided when logging an invalid value.
            key_path (str | None): The key path in dot notation.
            is_missing (bool): Indicates whether the key is missing.
            logging_level (str): The logging level to use for the log message.
        """
        # Validate logging level
        if logging_level.upper() not in LOGGING_LEVELS:
            raise AristaAvdError("Invalid logging level. Please choose from DEBUG, INFO, WARNING, ERROR, CRITICAL.")

        # If message is provided, it will be logged as is, ignoring other parameters
        if message:
            log_msg = str(message)
        else:
            if key is None:
                raise AristaAvdError("Error creating the log message: Key argument is missing.")
            if value is None and is_missing is False:
                raise AristaAvdError("Error creating the log message: The key's value must be provided when logging an invalid value.")
            dot_notation = f"{key_path}.{key}" if key_path else f"{key}"
            msg_type = "is missing" if is_missing else f"!= '{value}'"
            log_msg = f"Key '{dot_notation}' {msg_type}."

        # Appending the skipped test
        log_msg += f" {self.__class__.__name__} is skipped."

        # Logging the message
        log_level = logging.getLevelName(logging_level.upper())
        LOGGER.log(log_level, log_msg)

    def update_interface_shutdown(self, interface: dict, host: str | None = None) -> None:
        """
        Check if an interface is shutdown or not, considering EOS defaults.

        Args:
            interface (dict): The interface to verify.
            host (str): Host to verify. Defaults to the host running the test.

        Returns:
            bool: Returns the interface shutdown key's value, or `interface_defaults.ethernet` if not available.
                  Returns False if both are absent, which is the default EOS behavior.
        """
        host_struct_cfg = self.get_host_struct_cfg(host=host) if host else self.structured_config
        if "Ethernet" in get(interface, "name", ""):
            interface["shutdown"] = default(get(interface, "shutdown"), get(host_struct_cfg, "interface_defaults.ethernet.shutdown"), False)
        else:
            interface["shutdown"] = get(interface, "shutdown", default=False)

    def is_peer_available(self, peer: str) -> bool:
        """
        Check if a peer is deployed by looking at his `is_deployed` key.

        Args:
            peer (str): The peer to verify.

        Returns:
            bool: True if the peer is deployed, False otherwise.
        """
        if peer not in self.hostvars:
            self.log_skip_message(message=f"Peer '{peer}' is not configured by AVD.")
            return False
        if not get(self.hostvars[peer], "is_deployed", default=True):
            self.log_skip_message(message=f"Peer '{peer}' is marked as not deployed.")
            return False
        return True

    def get_interface_ip(self, interface_model: str, interface_name: str, host: str | None = None) -> str | None:
        """
        Retrieve the IP address of a specified host interface.

        Args:
            interface_model (str): Interface model in the structured config (e.g., ethernet_interfaces).
            interface_name (str): Interface name to retrive the IP.
            host (str): Host to verify. Defaults to the host running the test.

        Returns:
            str | None: IP address of the host interface or None if unavailable.
        """
        host_struct_cfg = self.get_host_struct_cfg(host=host) if host else self.structured_config
        try:
            peer_interfaces = get(host_struct_cfg, interface_model, required=True)
            peer_interface = get_item(peer_interfaces, "name", interface_name, required=True)
            return get(peer_interface, "ip_address", required=True)
        except AristaAvdMissingVariableError:
            self.log_skip_message(message=f"Host '{host or self.device_name}' interface '{interface_name}' IP address is unavailable.", logging_level="WARNING")
            return None

    def logged_get(self, key: str, host: str | None = None, logging_level: str = "WARNING"):
        """
        Attempts to retrieve a value associated with a given key from structured_config and logs if it's missing.

        Args:
            key (str): The key to retrieve.
            host (str | None): The host from which to retrieve the key. Defaults to the device running the test.
            logging_level (str): The logging level to use for the log message.
        """
        host_struct_cfg = self.get_host_struct_cfg(host=host) if host else self.structured_config
        try:
            return get(host_struct_cfg, key, required=True, separator="..")
        except AristaAvdMissingVariableError:
            self.log_skip_message(key=key, logging_level=logging_level)
            return None

    def validate_data(
        self,
        data: dict | None = None,
        data_path: str | None = None,
        host: str | None = None,
        required_keys: str | list[str] | None = None,
        logging_level: str | None = None,
        **kwargs,
    ) -> bool:
        """
        Validates data based on given requirements such as expected key-value pairs and required keys.

        Args:
            data (dict | None): A data dictionary to be validated. Defaults to the structured_config of the device running the test.
            data_path (str | None): The data path in dot notation. Used for logging purposes. Index or primary key can be used for lists.
            host (str | None): The host from which data should be retrieved. Defaults to the device running the test.
            required_keys (str | list[str] | None): The keys that are expected to be in the data.
            logging_level (str): Overwrites all default logging levels within this function.
                                If not provided, the default logging level is 'WARNING' when a key is missing and 'INFO' when his value is not matching.
            **kwargs: Expected key-value pairs in the data.

        Returns:
            bool: True if the data meets all validation requirements, otherwise False.

        Example:
            >>> validate_data(data={"a": 1, "b": 2}, data_path="some.path", required_keys=["a", "b"], c=3)

            In this case, the function will log a warning message because the key 'c' with value '3' is not found,
            and it will return False as the data doesn't meet all validation requirements.
        """
        data = data or (self.get_host_struct_cfg(host=host) if host else self.structured_config)
        valid = True

        # Check the expected key/value pairs first
        for key, value in kwargs.items():
            actual_value = get(data, key)
            if actual_value is None:
                self.log_skip_message(key=key, value=value, key_path=data_path, is_missing=True, logging_level=logging_level or "WARNING")
                valid = False
            elif actual_value != value:
                self.log_skip_message(key=key, value=value, key_path=data_path, is_missing=False, logging_level=logging_level or "INFO")
                valid = False

        # Return False if any of the expected values are missing or not matching
        if not valid:
            return False

        # Check the required keys
        if required_keys:
            required_keys = [required_keys] if isinstance(required_keys, str) else required_keys
            for key in required_keys:
                if get(data, key) is None:
                    self.log_skip_message(key=key, key_path=data_path, is_missing=True, logging_level=logging_level or "WARNING")
                    valid = False
        return valid

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

        # FIXME @cbaillar: Need to refactor this: https://github.com/aristanetworks/ansible-avd/issues/3304
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
