# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Testing get_avd_facts and get_device_structured_config for the variations of supported inputs.

Only covering variants not already handled in e2e-test-avd,
and just testing that we don't raise.
"""

from copy import deepcopy

import pytest

from pyavd import get_avd_facts, get_device_config, get_device_structured_config
from pyavd._eos_designs.structured_config.network_services import AvdStructuredConfigNetworkServices
from pyavd.api.schemas import AVDDesign

INPUTS = {
    "testhost1": {"fabric_name": "FABRIC", "devices": [{"name": "testhost1", "type": "l2leaf"}]},
}

CV_PATHFINDER_ZSCALER_SHARED_NAT_HOSTNAME = "cv-pathfinder-zscaler-shared-nat-prereqs"
CV_PATHFINDER_ZSCALER_SHARED_NAT_INPUTS = {
    "fabric_name": "EOS_DESIGNS_UNIT_TESTS",
    "wan_mode": "cv-pathfinder",
    "underlay_routing_protocol": "none",
    "type": "wan_router",
    "bgp_as": 65000,
    "cv_pathfinder_regions": [
        {
            "name": "AVD_Land_Test",
            "id": 88,
            "description": "AVD Region",
            "sites": [{"name": "Site188", "id": 188, "location": "Somewhere"}],
        }
    ],
    "bgp_peer_groups": {
        "wan_overlay_peers": {
            "password": "htm4AZe9mIQOO1uiMuGgYQ==",
            "listen_range_prefixes": ["192.168.255.0/24"],
        }
    },
    "wan_route_servers": [
        {
            "hostname": "cv-pathfinder-pathfinder",
            "vtep_ip": "10.10.10.10",
            "path_groups": [{"name": "INET", "interfaces": [{"name": "Ethernet1", "public_ip": "198.51.100.10"}]}],
        }
    ],
    "wan_ipsec_profiles": {
        "control_plane": {"shared_key": "ABCDEF1234567890"},
        "data_plane": {"shared_key": "ABCDEF1234567890666"},
    },
    "wan_router": {
        "defaults": {
            "loopback_ipv4_pool": "192.168.42.0/24",
            "vtep_loopback_ipv4_pool": "192.168.255.0/24",
            "filter": {"always_include_vrfs_in_tenants": ["TenantA"]},
        },
        "nodes": [
            {
                "name": CV_PATHFINDER_ZSCALER_SHARED_NAT_HOSTNAME,
                "cv_pathfinder_region": "AVD_Land_Test",
                "cv_pathfinder_site": "Site188",
                "id": 1,
                "l3_interfaces": [
                    {
                        "name": "Ethernet1",
                        "wan_carrier": "ATT",
                        "wan_circuit_id": "188-1",
                        "ip_address": "198.51.100.11/31",
                        "peer_ip": "198.51.100.10",
                        "cv_pathfinder_internet_exit": {
                            "policies": [
                                {"name": "ZSCALER-EXIT-POLICY-1", "tunnel_interface_numbers": "100-102"},
                                {"name": "ZSCALER-EXIT-POLICY-2", "tunnel_interface_numbers": "110-112"},
                            ]
                        },
                    }
                ],
            }
        ],
    },
    "wan_path_groups": [{"name": "INET", "id": 101}],
    "wan_carriers": [{"name": "ATT", "path_group": "INET", "trusted": True}],
    "tenants": [{"name": "TenantA", "vrfs": [{"name": "default", "vrf_id": 1}, {"name": "PROD", "vrf_id": 42}]}],
    "wan_virtual_topologies": {
        "vrfs": [{"name": "PROD", "wan_vni": 42}],
        "policies": [
            {
                "name": "DEFAULT-POLICY",
                "default_virtual_topology": {"path_groups": [{"names": ["INET"]}]},
                "application_virtual_topologies": [
                    {
                        "application_profile": "APP-1",
                        "path_groups": [{"names": ["INET"]}],
                        "internet_exit": {"policy": "ZSCALER-EXIT-POLICY-1"},
                        "id": 2,
                    },
                    {
                        "application_profile": "APP-2",
                        "path_groups": [{"names": ["INET"]}],
                        "internet_exit": {"policy": "ZSCALER-EXIT-POLICY-2"},
                        "id": 4,
                    },
                ],
            }
        ],
    },
    "application_classification": {"application_profiles": [{"name": "APP-1"}, {"name": "APP-2"}]},
    "cv_pathfinder_internet_exit_policies": [
        {
            "name": "ZSCALER-EXIT-POLICY-1",
            "type": "zscaler",
            "zscaler": {"domain_name": "test.local", "ipsec_key_salt": "THIS_SHOULD_BE_VAULTED"},
        },
        {
            "name": "ZSCALER-EXIT-POLICY-2",
            "fallback_to_system_default": False,
            "type": "zscaler",
            "zscaler": {"domain_name": "test.local", "ipsec_key_salt": "THIS_SHOULD_BE_VAULTED"},
        },
    ],
    "ipv4_acls": [
        {
            "name": "ACL-NAT-IE-ZSCALER",
            "entries": [
                {"sequence": 10, "action": "permit", "protocol": "ip", "source": "any", "destination": "10.10.10.0/24"},
                {"sequence": 20, "action": "deny", "protocol": "ip", "source": "any", "destination": "any"},
            ],
        }
    ],
    "zscaler_endpoints": {
        "cloud_name": "zscalerbeta",
        "device_location": {"city": "Santa Clara, CA", "country": "United States"},
        "primary": {
            "city": "Fremont, CA",
            "datacenter": "FMT1",
            "country": "United States",
            "region": "us-west1",
            "latitude": 37,
            "longitude": -121,
            "ip_address": "203.0.113.10",
        },
    },
}


def test_get_avd_facts_get_device_structured_config_dicts() -> None:
    avd_facts = get_avd_facts(all_inputs=INPUTS, all_hostvars=None)
    assert len(avd_facts) == len(INPUTS)

    for hostname, hostvars in INPUTS.items():
        structured_config = get_device_structured_config(hostname, hostvars, avd_facts, hostvars=None)
        assert structured_config.hostname == hostname


def test_get_avd_facts_get_device_structured_config_models() -> None:
    models = {name: AVDDesign._load(hostvars) for name, hostvars in INPUTS.items()}
    avd_facts = get_avd_facts(all_inputs=models, all_hostvars=INPUTS)
    assert len(avd_facts) == len(INPUTS)

    for hostname, model in models.items():
        structured_config = get_device_structured_config(hostname, model, avd_facts, hostvars=INPUTS[hostname])
        assert structured_config.hostname == hostname


def test_get_device_structured_config_resolves_dns_profiles() -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "devices": [{"name": "testhost1", "type": "l2leaf", "dns_settings_profile": "testhost1_dns_profile"}],
        "dns_settings": {"servers": [{"ip_address": "192.0.2.53", "vrf": "default", "priority": 1}]},
        "dns_settings_profiles": [
            {
                "profile": "testhost1_dns_profile",
                "domain": "testhost1.example.com",
                "domain_list": ["testhost1.example.com"],
            },
        ],
    }
    avd_facts = get_avd_facts(all_inputs={"testhost1": inputs}, all_hostvars=None)

    structured_config = get_device_structured_config("testhost1", inputs, avd_facts)

    assert structured_config.dns_domain == "testhost1.example.com"
    assert list(structured_config.domain_list) == ["testhost1.example.com"]


def test_get_device_structured_config_zscaler_shared_nat_prereqs_are_initialized_once(monkeypatch: pytest.MonkeyPatch) -> None:
    hostvars = deepcopy(CV_PATHFINDER_ZSCALER_SHARED_NAT_INPUTS)

    zscaler_nat_acl_calls = 0
    original_set_zscaler_ie_policy_acl = AvdStructuredConfigNetworkServices._set_zscaler_ie_policy_acl

    def _count_zscaler_nat_acl_calls(self: AvdStructuredConfigNetworkServices, acl_name: str) -> None:
        nonlocal zscaler_nat_acl_calls
        zscaler_nat_acl_calls += 1
        original_set_zscaler_ie_policy_acl(self, acl_name)

    monkeypatch.setattr(AvdStructuredConfigNetworkServices, "_set_zscaler_ie_policy_acl", _count_zscaler_nat_acl_calls)

    avd_facts = get_avd_facts(
        all_inputs={CV_PATHFINDER_ZSCALER_SHARED_NAT_HOSTNAME: hostvars},
        all_hostvars={CV_PATHFINDER_ZSCALER_SHARED_NAT_HOSTNAME: hostvars},
    )

    structured_config = get_device_structured_config(
        CV_PATHFINDER_ZSCALER_SHARED_NAT_HOSTNAME,
        hostvars,
        avd_facts,
        hostvars=hostvars,
    )

    assert zscaler_nat_acl_calls == 1
    assert sum(pool.name == "PORT-ONLY-POOL" for pool in structured_config.ip_nat.pools) == 1
    assert sum(profile.name == "NAT-IE-ZSCALER" for profile in structured_config.ip_nat.profiles) == 1

    zscaler_policy_names = {policy.name for policy in structured_config.router_internet_exit.policies}
    assert {"ZSCALER-EXIT-POLICY-1", "ZSCALER-EXIT-POLICY-2"} <= zscaler_policy_names

    acl = next(acl for acl in structured_config.ip_access_lists if acl.name == "ACL-NAT-IE-ZSCALER")
    assert any(entry.destination == "10.10.10.0/24" for entry in acl.entries)

    device_config = get_device_config(structured_config)
    assert device_config.count("ip nat source dynamic access-list ACL-NAT-IE-ZSCALER pool PORT-ONLY-POOL") == 1
    assert device_config.count("ip nat pool PORT-ONLY-POOL port-only") == 1
