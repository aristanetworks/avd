# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from .tests import (
    AvdTestAPIHttpsSSL,
    AvdTestBGP,
    AvdTestHardware,
    AvdTestInbandReachability,
    AvdTestInterfacesState,
    AvdTestLLDPTopology,
    AvdTestLoopback0Reachability,
    AvdTestMLAG,
    AvdTestNTP,
    AvdTestP2PIPReachability,
    AvdTestReloadCause,
    AvdTestRoutingTable,
)

ACRONYM_CATEGORIES: set[str] = {"aaa", "mlag", "snmp", "bgp", "ospf", "vxlan", "stp", "igmp", "ip", "lldp", "ntp"}
"""
A set of network protocol or feature acronyms that should be represented in uppercase in the eos_validate_state report.
"""

AVD_TEST_CLASSES = {
    AvdTestHardware: {"legacy_ansible_tags": ["hardware", "platform_information"]},
    AvdTestNTP: {"legacy_ansible_tags": ["ntp"]},
    AvdTestInterfacesState: {"legacy_ansible_tags": ["interfaces_state"]},
    AvdTestLLDPTopology: {"legacy_ansible_tags": ["lldp_topology"]},
    AvdTestMLAG: {"legacy_ansible_tags": ["mlag"]},
    AvdTestP2PIPReachability: {"legacy_ansible_tags": ["ip_reachability"]},
    AvdTestBGP: {"legacy_ansible_tags": ["bgp_check"]},
    AvdTestReloadCause: {"legacy_ansible_tags": ["reload_cause", "optional", "never"]},
    AvdTestRoutingTable: {"legacy_ansible_tags": ["routing_table"]},
    AvdTestInbandReachability: {"legacy_ansible_tags": ["loopback_reachability", "loopback0_reachability", "optional"]},
    AvdTestLoopback0Reachability: {"legacy_ansible_tags": ["loopback_reachability", "loopback0_reachability"]},
    AvdTestAPIHttpsSSL: {},
}
"""
A dict of all AVD eos_validate_state test classes with their equivalent legacy Ansible tags.

These classes each contains a `test_definition` attribute generated from the AVD structured_config.
"""
