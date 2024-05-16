# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

LOGGER = logging.getLogger(__name__)


class AvdTestStun(AvdTestBase):
    """
    AvdTestStun class for STUN tests.
    Validates the configuration of the STUN client, focusing specifically on the IPv4 source address and port,
    exclusively for WAN scenarios by inspecting the path-groups.
    """

    anta_module = "anta.tests.stun"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all STUN tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        # Check if there are any path groups with STUN configuration
        if (path_groups := get(self.structured_config, "router_path_selection.path_groups")) is None:
            LOGGER.info("Path groups are not configured to collect STUN interfaces information. %s is skipped.", self.__class__.__name__)
            return None

        # Get the interfaces with STUN configuration
        stun_interfaces = [
            local_interfaces["name"]
            for group_idx, path_group in enumerate(path_groups)
            if self.validate_data(data=path_group, data_path=f"router_path_selection.path_groups.[{group_idx}]", required_keys="local_interfaces")
            for local_interfaces in path_group["local_interfaces"]
            if self.validate_data(data=local_interfaces, data_path=f"router_path_selection.path_groups.[{group_idx}]", required_keys="stun.server_profiles")
        ]
        if not stun_interfaces:
            LOGGER.info("No local interface found with STUN configuration. %s is skipped.", self.__class__.__name__)
            return None

        # Generate the ANTA tests for each identified local interface.
        for source_interface in stun_interfaces:
            ip_address = self.get_interface_ip("ethernet_interfaces", source_interface)
            source_address = ip_address.split("/")[0]
            source_port = 4500
            anta_tests.append(
                {
                    "VerifyStunClient": {
                        "stun_clients": [{"source_address": source_address, "source_port": source_port}],
                        "result_overwrite": {"custom_field": f"Source IPv4 Address: {source_address} Source Port: {source_port}"},
                    }
                }
            )

        # Return the ANTA tests as a dictionary
        return {self.anta_module: anta_tests} if anta_tests else None
