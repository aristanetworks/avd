# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property
from ipaddress import ip_interface
from typing import Mapping

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item

from .config_manager import ConfigManager
from .device_utils import DeviceUtils
from .mixins import LoggingMixin

LOGGER = logging.getLogger(__name__)



class AvdTestBase(LoggingMixin):
    """
    Base class for all AVD eos_validate_state tests.
    """

    def __init__(self, config_manager: ConfigManager):
        """
        Initialize the AvdTestBase class.

        Args:
            device_name (str): The current device name for which the plugin is being run.
            hostvars (Mapping): A mapping that contains a key for each device with a value of the structured_config.
                                      When using Ansible, this is the `task_vars['hostvars']` object.
        """
        super().__init__()
        self.config_manager = config_manager
        self.device_utils = DeviceUtils(config_manager)

    @property
    def device_name(self) -> str:
        return self.config_manager.device_name
    
    @property
    def hostvars(self) -> Mapping:
        return self.config_manager.hostvars
    
    @property
    def structured_config(self) -> Mapping:
        return self.config_manager.structured_config
    
    @property
    def loopback0_mapping(self) -> list[tuple[str, str]]:
        return self.config_manager.loopback0_mapping
    
    @property
    def vtep_mapping(self) -> list[tuple[str, str]]:
        return self.config_manager.vtep_mapping

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

    def validate_data(
        self,
        data: dict | None = None,
        data_path: str | None = None,
        host: str | None = None,
        required_keys: str | list[str] | None = None,
        logging_level: str = "INFO",
        **kwargs,
    ) -> bool:
        """
        Validates data based on given requirements such as expected key-value pairs and required keys.

        Args:
            data (dict | None): A data dictionary to be validated. Defaults to the structured_config of the device running the test.
            data_path (str | None): The data path in dot notation. Used for logging purposes. Index or primary key can be used for lists.
            host (str | None): The host from which data should be retrieved. Defaults to the device running the test.
            required_keys (str | list[str] | None): The keys that are expected to be in the data.
            logging_level (str): The logging level to use for the log message. Defaults to "INFO".
            **kwargs: Expected key-value pairs in the data.

        Returns:
            bool: True if the data meets all validation requirements, otherwise False.

        Example:
            >>> validate_data(data={"a": 1, "b": 2}, data_path="some.path", required_keys=["a", "b"], c=3)

            In this case, the function will log a warning message because the key 'c' with value '3' is not found,
            and it will return False as the data doesn't meet all validation requirements.
        """
        data = data or (self.config_manager.get_host_structured_config(host=host) if host else self.structured_config)
        valid = True

        # Check the expected key/value pairs first
        for key, value in kwargs.items():
            actual_value = get(data, key)
            if actual_value is None:
                self.log_skip_message(key=key, value=value, key_path=data_path, is_missing=True, logging_level=logging_level)
                valid = False
            elif actual_value != value:
                self.log_skip_message(key=key, value=value, key_path=data_path, is_missing=False, logging_level=logging_level)
                valid = False

        # Return False if any of the expected values are missing or not matching
        if not valid:
            return False

        # Check the required keys
        if required_keys:
            required_keys = [required_keys] if isinstance(required_keys, str) else required_keys
            for key in required_keys:
                if get(data, key) is None:
                    self.log_skip_message(key=key, key_path=data_path, is_missing=True, logging_level=logging_level)
                    valid = False
        return valid
