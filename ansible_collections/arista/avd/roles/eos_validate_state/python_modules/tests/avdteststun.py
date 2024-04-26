# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

LOGGER = logging.getLogger(__name__)


class AvdTestStun(AvdTestBase):
    """
    AvdTestStun class for STUN tests.
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
            LOGGER.info("No local interface found with STUN configuration. %s is skipped.", self.__class__.__name__)
            return None

        # Get the interfaces with STUN configuration
        stun_interfaces = [
            local_interfaces.get("name")
            for path_group in path_groups
            for local_interfaces in path_group.get("local_interfaces")
            if get(local_interfaces, "stun.server_profiles") is not None
        ]

        # Generate the ANTA tests for each interface with STUN configuration
        for source_interface in stun_interfaces:
            interfaces_data = get(self.structured_config, "ethernet_interfaces")
            interface_address = get_item(interfaces_data, "name", source_interface)
            ip_address = interface_address.get("ip_address")
            if ip_address is None:
                LOGGER.info("No IP address found for interface %s. Skipping this interface.", source_interface)
                continue
            source_address = ip_address.split("/")[0]
            source_port = 4500  # TODO: Keeping source port as default 4500. We might need to change it later.
            anta_tests.append(
                {
                    "VerifyStunClient": {
                        "stun_clients": [{"source_address": source_address, "source_port": source_port}],
                        "result_overwrite": {"custom_field": f"source address: {source_address} source port: {source_port}"},
                    }
                }
            )

        # Return the ANTA tests as a dictionary
        return {self.anta_module: anta_tests}
