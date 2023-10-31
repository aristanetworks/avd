# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from tests.unit.roles.eos_validate_state.avdtests import test_avd_tests  # noqa: F401; pylint: disable=unused-import

DATA: list[dict] = [
    {
        "test_name": "all-good",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "DC1-LEAF1A", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            },
            "DC1-LEAF1A": {},
        },
        "expected_result": {
            "anta.tests.connectivity": [
                {
                    "VerifyLLDPNeighbors": {
                        "neighbors": [{"neighbor_device": "DC1-LEAF1A", "neighbor_port": "Ethernet1", "port": "Ethernet1"}],
                        "result_overwrite": {
                            "categories": ["LLDP Topology"],
                            "description": "LLDP topology - validate peer and interface",
                            "custom_field": "local: Ethernet1 - remote: DC1-LEAF1A_Ethernet1",
                        },
                    }
                }
            ]
        },
        "expected_log": None,
        "expected_log_level": None,
    },
    {
        "test_name": "missing-ethernet-interfaces",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {},
        },
        "expected_result": {},
        "expected_log": "Key 'ethernet_interfaces' is missing. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-peer",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            }
        },
        "expected_result": {},
        "expected_log": "Key 'ethernet_interfaces.[0].peer' is missing. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-name",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"peer": "DC1-LEAF1A", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            }
        },
        "expected_result": {},
        "expected_log": "Key 'ethernet_interfaces.[0].name' is missing. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-shutdown",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {
                        "name": "Ethernet1",
                        "peer": "DC1-LEAF1A",
                        "peer_interface": "Ethernet1",
                    },
                ]
            }
        },
        "expected_result": {},
        "expected_log": "Key 'ethernet_interfaces.[0].shutdown' is missing. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-peer-interface",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "DC1-LEAF1A", "shutdown": False},
                ]
            }
        },
        "expected_result": {},
        "expected_log": "Key 'ethernet_interfaces.[0].peer_interface' is missing. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "peer-not-deployed",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "DC1-LEAF1A", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            },
            "DC1-LEAF1A": {"is_deployed": False},
        },
        "expected_result": {},
        "expected_log": "Peer 'DC1-LEAF1A' is marked as not deployed. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "INFO",
    },
    {
        "test_name": "peer-not-configured",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "HOST-1", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            }
        },
        "expected_result": {},
        "expected_log": "Peer 'HOST-1' is not configured by AVD. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "INFO",
    },
    {
        "test_name": "two-interfaces-one-shutdown",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "DC1-LEAF1A", "peer_interface": "Ethernet1", "shutdown": False},
                    {"name": "Ethernet2", "peer": "DC1-LEAF1B", "peer_interface": "Ethernet1", "shutdown": True},
                ]
            },
            "DC1-LEAF1A": {},
        },
        "expected_result": {
            "anta.tests.connectivity": [
                {
                    "VerifyLLDPNeighbors": {
                        "neighbors": [{"neighbor_device": "DC1-LEAF1A", "neighbor_port": "Ethernet1", "port": "Ethernet1"}],
                        "result_overwrite": {
                            "categories": ["LLDP Topology"],
                            "description": "LLDP topology - validate peer and interface",
                            "custom_field": "local: Ethernet1 - remote: DC1-LEAF1A_Ethernet1",
                        },
                    }
                }
            ]
        },
        "expected_log": "Key 'ethernet_interfaces.[1].shutdown' != 'False'. AvdTestLLDPTopology is skipped.",
        "expected_log_level": "INFO",
    },
    {
        "test_name": "all-good-with-dns-domain",
        "test_module": "AvdTestLLDPTopology",
        "hostvars": {
            "DC1-SPINE1": {
                "ethernet_interfaces": [
                    {"name": "Ethernet1", "peer": "DC1-LEAF1A", "peer_interface": "Ethernet1", "shutdown": False},
                ]
            },
            "DC1-LEAF1A": {"dns_domain": "test.lab"},
        },
        "expected_result": {
            "anta.tests.connectivity": [
                {
                    "VerifyLLDPNeighbors": {
                        "neighbors": [{"neighbor_device": "DC1-LEAF1A.test.lab", "neighbor_port": "Ethernet1", "port": "Ethernet1"}],
                        "result_overwrite": {
                            "categories": ["LLDP Topology"],
                            "description": "LLDP topology - validate peer and interface",
                            "custom_field": "local: Ethernet1 - remote: DC1-LEAF1A_Ethernet1",
                        },
                    }
                }
            ]
        },
        "expected_log": None,
        "expected_log_level": None,
    },
]
"""Data for `ansible_collections.arista.avd.roles.eos_validate_state.python_modules.tests.avdtestconnectivity.py` unit tests"""
