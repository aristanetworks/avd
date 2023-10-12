# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from tests.unit.roles.eos_validate_state.avdtests import test_avd_tests  # noqa: F401; pylint: disable=unused-import

DATA: list[dict] = [
    {
        "test_name": "all-good",
        "test_module": "AvdTestBGP",
        "hostvars": {
            "DC1-SPINE1": {
                "service_routing_protocols_model": "multi-agent",
                "router_bgp": {
                    "as": "65100",
                    "router_id": "10.1.0.1",
                    "peer_groups": [{"name": "IPv4-UNDERLAY-PEERS", "type": "ipv4"}, {"name": "EVPN-OVERLAY-PEERS", "type": "evpn"}],
                    "neighbors": [
                        {"ip_address": "10.1.255.1", "peer_group": "IPv4-UNDERLAY-PEERS"},
                        {"ip_address": "10.1.0.6", "peer_group": "EVPN-OVERLAY-PEERS"},
                    ],
                },
            }
        },
        "expected_result": {
            "anta.tests.routing": {
                "generic": [
                    {
                        "VerifyRoutingProtocolModel": {
                            "model": "multi-agent",
                            "result_overwrite": {"categories": ["BGP"], "description": "ArBGP is configured and operating", "custom_field": "ArBGP"},
                        }
                    }
                ],
                "bgp": [
                    {
                        "VerifyBGPSpecificPeers": {
                            "address_families": [{"afi": "ipv4", "safi": "unicast", "peers": ["10.1.255.1"]}],
                            "result_overwrite": {
                                "categories": ["BGP"],
                                "description": "ip bgp peer state established (ipv4)",
                                "custom_field": "bgp_neighbor: 10.1.255.1",
                            },
                        }
                    },
                    {
                        "VerifyBGPSpecificPeers": {
                            "address_families": [{"afi": "evpn", "peers": ["10.1.0.6"]}],
                            "result_overwrite": {
                                "categories": ["BGP"],
                                "description": "bgp evpn peer state established (evpn)",
                                "custom_field": "bgp_neighbor: 10.1.0.6",
                            },
                        }
                    },
                ],
            },
        },
        "expected_log": None,
        "expected_log_level": None,
    },
    {
        "test_name": "missing-router-bgp",
        "test_module": "AvdTestBGP",
        "hostvars": {"DC1-SPINE1": {}},
        "expected_result": {},
        "expected_log": "Variable 'router_bgp' is missing from the structured_config. AvdTestBGP is skipped.",
        "expected_log_level": "INFO",
    },
    {
        "test_name": "missing-service-routing-protocols-model",
        "test_module": "AvdTestBGP",
        "hostvars": {"DC1-SPINE1": {"router_bgp": {}}},
        "expected_result": {},
        "expected_log": "Variable 'service_routing_protocols_model' is missing from the structured_config. AvdTestBGP is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "wrong-service-routing-protocols-model",
        "test_module": "AvdTestBGP",
        "hostvars": {"DC1-SPINE1": {"service_routing_protocols_model": "ribd", "router_bgp": {}}},
        "expected_result": {},
        "expected_log": "Variable 'service_routing_protocols_model' is NOT set to 'multi-agent'. AvdTestBGP is skipped.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-peer-group",
        "test_module": "AvdTestBGP",
        "hostvars": {
            "DC1-SPINE1": {
                "service_routing_protocols_model": "multi-agent",
                "router_bgp": {
                    "as": "65100",
                    "router_id": "10.1.0.1",
                    "peer_groups": [{"name": "EVPN-OVERLAY-PEERS", "type": "evpn"}],
                    "neighbors": [
                        {"ip_address": "10.1.255.1", "peer_group": "IPv4-UNDERLAY-PEERS"},
                        {"ip_address": "10.1.0.6", "peer_group": "EVPN-OVERLAY-PEERS"},
                    ],
                },
            }
        },
        "expected_result": {
            "anta.tests.routing": {
                "generic": [
                    {
                        "VerifyRoutingProtocolModel": {
                            "model": "multi-agent",
                            "result_overwrite": {"categories": ["BGP"], "description": "ArBGP is configured and operating", "custom_field": "ArBGP"},
                        }
                    }
                ],
                "bgp": [
                    {
                        "VerifyBGPSpecificPeers": {
                            "address_families": [{"afi": "evpn", "peers": ["10.1.0.6"]}],
                            "result_overwrite": {
                                "categories": ["BGP"],
                                "description": "bgp evpn peer state established (evpn)",
                                "custom_field": "bgp_neighbor: 10.1.0.6",
                            },
                        }
                    },
                ],
            },
        },
        "expected_log": "Peer group 'IPv4-UNDERLAY-PEERS' dictionary is missing from the 'peer_groups' list of the 'router_bgp' data model.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-neighbor-ip-address",
        "test_module": "AvdTestBGP",
        "hostvars": {
            "DC1-SPINE1": {
                "service_routing_protocols_model": "multi-agent",
                "router_bgp": {
                    "as": "65100",
                    "router_id": "10.1.0.1",
                    "peer_groups": [{"name": "IPv4-UNDERLAY-PEERS", "type": "ipv4"}, {"name": "EVPN-OVERLAY-PEERS", "type": "evpn"}],
                    "neighbors": [
                        {"peer_group": "IPv4-UNDERLAY-PEERS"},
                        {"ip_address": "10.1.0.6", "peer_group": "EVPN-OVERLAY-PEERS"},
                    ],
                },
            }
        },
        "expected_result": {
            "anta.tests.routing": {
                "generic": [
                    {
                        "VerifyRoutingProtocolModel": {
                            "model": "multi-agent",
                            "result_overwrite": {"categories": ["BGP"], "description": "ArBGP is configured and operating", "custom_field": "ArBGP"},
                        }
                    }
                ],
                "bgp": [
                    {
                        "VerifyBGPSpecificPeers": {
                            "address_families": [{"afi": "evpn", "peers": ["10.1.0.6"]}],
                            "result_overwrite": {
                                "categories": ["BGP"],
                                "description": "bgp evpn peer state established (evpn)",
                                "custom_field": "bgp_neighbor: 10.1.0.6",
                            },
                        }
                    },
                ],
            },
        },
        "expected_log": "Neighbor entry #1 from the 'neighbors' list of the 'router_bgp' data model is missing the variable 'ip_address'.",
        "expected_log_level": "WARNING",
    },
    {
        "test_name": "missing-peer-group-type",
        "test_module": "AvdTestBGP",
        "hostvars": {
            "DC1-SPINE1": {
                "service_routing_protocols_model": "multi-agent",
                "router_bgp": {
                    "as": "65100",
                    "router_id": "10.1.0.1",
                    "peer_groups": [
                        {
                            "name": "IPv4-UNDERLAY-PEERS",
                        },
                        {"name": "EVPN-OVERLAY-PEERS", "type": "evpn"},
                    ],
                    "neighbors": [
                        {"ip_address": "10.1.255.1", "peer_group": "IPv4-UNDERLAY-PEERS"},
                        {"ip_address": "10.1.0.6", "peer_group": "EVPN-OVERLAY-PEERS"},
                    ],
                },
            }
        },
        "expected_result": {
            "anta.tests.routing": {
                "generic": [
                    {
                        "VerifyRoutingProtocolModel": {
                            "model": "multi-agent",
                            "result_overwrite": {"categories": ["BGP"], "description": "ArBGP is configured and operating", "custom_field": "ArBGP"},
                        }
                    }
                ],
                "bgp": [
                    {
                        "VerifyBGPSpecificPeers": {
                            "address_families": [{"afi": "evpn", "peers": ["10.1.0.6"]}],
                            "result_overwrite": {
                                "categories": ["BGP"],
                                "description": "bgp evpn peer state established (evpn)",
                                "custom_field": "bgp_neighbor: 10.1.0.6",
                            },
                        }
                    },
                ],
            },
        },
        "expected_log": "Peer group 'IPv4-UNDERLAY-PEERS' from the 'peer_groups' list of the 'router_bgp' data model is missing the variable 'type'.",
        "expected_log_level": "WARNING",
    },
]
"""Data for `ansible_collections.arista.avd.roles.eos_validate_state.python_modules.tests.avdtestrouting.py` unit tests"""
