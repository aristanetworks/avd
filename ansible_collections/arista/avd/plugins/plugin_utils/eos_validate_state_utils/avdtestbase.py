# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations


class AvdTestBase:
    """
    Base class for all AVD eos_validate_state tests.
    """

    def __init__(self, device_name: str, hostvars: dict, custom_data: dict = None):
        """
        Initialize the AvdTestBase class.

        Args:
            device_name (str): The current device name for which the plugin is being run
            hostvars (dict): A dictionnary that contains a key for each device with a value of the structured_config
                           when using Ansible, this is the equivalent of `task_vars['hostvars']`
            custom_data (dict, optional): Dictionary containing custom data to create required attributes for subclasses.
        """
        self.hostvars = hostvars
        self.device_name = device_name
        self.custom_data = custom_data or {}

        # TODO - can we do better here than having to use custom_data
        self.loopback0_mapping = self.custom_data.get("loopback0_mapping")
        self.vtep_mapping = self.custom_data.get("vtep_mapping")

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
