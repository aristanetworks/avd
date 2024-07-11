# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

LOGGER = logging.getLogger(__name__)


class AvdTestAvtPath(AvdTestBase):
    """
    AvdTestAvtPath class for AVT (Adaptive Virtual Topology) tests.
    Validates the status and type of AVT paths for a specified VRF in WAN scenarios.
    It constructs a list of static peer addresses for each device by searching through
    router_path_selection.path_groups.static_peers.
    """

    anta_module = "anta.tests.avt"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the ANTA test definition for AVT path tests.

        Returns:
            dict | None: ANTA test definition or None if the configuration is incomplete.
        """
        # Retrieve path groups from the structured configuration
        path_groups = get(self.structured_config, "router_path_selection.path_groups")
        if not path_groups:
            LOGGER.info("Path groups are not configured to collect AVT peer information. %s is skipped.", self.__class__.__name__)
            return None

        # Retrieve AVT profiles from the structured configuration
        avt_profiles = get(self.structured_config, "router_adaptive_virtual_topology.vrfs")
        if not avt_profiles:
            LOGGER.info("AVT profiles are not configured for any VRF. %s is skipped.", self.__class__.__name__)
            return None

        # Build a set of static peers
        static_peers = {
            peers_data["router_ip"]
            for group_idx, path_group in enumerate(path_groups)
            if self.validate_data(data=path_group, data_path=f"router_path_selection.path_groups.[{group_idx}]", required_keys="static_peers")
            for peer_idx, peers_data in enumerate(path_group["static_peers"])
            if self.validate_data(
                data=peers_data, data_path=f"router_path_selection.path_groups.[{group_idx}].static_peers.[{peer_idx}]", required_keys="router_ip"
            )
        }
        if not static_peers:
            LOGGER.info("No static peers are configured under router path selection. %s is skipped.", self.__class__.__name__)
            return None

        # Construct the list of ANTA tests
        anta_tests = [
            {
                "VerifyAVTSpecificPath": {
                    "avt_paths": [
                        {
                            "avt_name": avt_profile["name"],
                            "vrf": vrf["name"],
                            "destination": dst_address,
                            "next_hop": dst_address,
                        }
                    ],
                    "result_overwrite": {
                        "custom_field": f"AVT profile: {avt_profile['name']}, vrf: {vrf['name']}, "
                        f"Destination IPv4 Address: {dst_address}, Nexthop VTEP: {dst_address}"
                    },
                }
            }
            for vrf in avt_profiles
            for avt_profile in vrf["profiles"]
            for dst_address in static_peers
        ]

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestAvtRole(AvdTestBase):
    """
    AvdTestAvtRole class for AVT (Adaptive Virtual Topology) role tests.
    Validates the Adaptive Virtual Topology (AVT) role of a device.
    """

    anta_module = "anta.tests.avt"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the ANTA test definition for AVT role tests.

        Returns:
            dict | None: ANTA test definition or None if the configuration is incomplete.
        """

        # Retrieve AVT role from the structured configuration
        avt_role = get(self.structured_config, "router_adaptive_virtual_topology.topology_role")
        if not avt_role:
            LOGGER.info("AVT role is not configured. %s is skipped.", self.__class__.__name__)
            return None

        # Construct the list of ANTA tests
        anta_tests = [
            {
                "VerifyAVTRole": {
                    "role": avt_role,
                }
            }
        ]

        return {self.anta_module: anta_tests} if anta_tests else None
