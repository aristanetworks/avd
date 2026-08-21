# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Testing get_avd_facts and get_device_structured_config for the variations of supported inputs.

Only covering variants not already handled in e2e-test-avd,
and just testing that we don't raise.
"""

import json

from pyavd import get_avd_facts, get_device_structured_config
from pyavd.api.schemas import AVDDesign, ConsolidatedAVDDesign

INPUTS = {
    "testhost1": {"fabric_name": "FABRIC", "devices": [{"name": "testhost1", "type": "l2leaf"}]},
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


def test_consolidated_avd_design_json_round_trip() -> None:
    consolidated_inputs = ConsolidatedAVDDesign._from_avd_design("testhost1", INPUTS["testhost1"])
    dumped_inputs = consolidated_inputs._dump()

    loaded_inputs = ConsolidatedAVDDesign._from_dict(json.loads(json.dumps(dumped_inputs)))

    assert isinstance(loaded_inputs, ConsolidatedAVDDesign)
    assert loaded_inputs._dump() == dumped_inputs


def test_connected_endpoints_are_consolidated_and_pruned() -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "devices": [{"name": "testhost1", "type": "l2leaf"}],
        "port_profiles": [{"profile": "ACCESS_10", "mode": "access", "vlans": "10"}],
        "connected_endpoints": [
            {
                "name": "server1",
                "adapters": [
                    {"switches": ["other"], "switch_ports": ["Ethernet1"]},
                    {"profile": "ACCESS_10", "switches": ["testhost1"], "switch_ports": ["Ethernet2"]},
                ],
            }
        ],
        "network_ports": [
            {"switches": ["other"], "switch_ports": ["Ethernet3"]},
            {"profile": "ACCESS_10", "switches": ["testhost1"], "switch_ports": ["Ethernet4"]},
            {"profile": "ACCESS_10", "platforms": [".*EOS.*"], "switch_ports": ["Ethernet5"]},
        ],
    }

    consolidated_inputs = ConsolidatedAVDDesign._from_avd_design("testhost1", inputs)

    assert len(consolidated_inputs._connected_endpoints) == 1
    connected_endpoint = consolidated_inputs._connected_endpoints["connected_endpoints"].value["server1"]
    assert connected_endpoint._adapter_indices == [1]
    assert connected_endpoint.adapters[0].mode == "access"
    assert connected_endpoint.adapters[0].vlans == "10"
    assert [network_port._source_index for network_port in consolidated_inputs._network_ports] == [1, 2]
    assert consolidated_inputs._network_ports[0].mode == "access"
    assert [(profile.profile, profile.parent_profile) for profile in consolidated_inputs._port_profile_names] == [("ACCESS_10", None)]

    assert "connected_endpoints" not in consolidated_inputs.__dict__
    assert "network_ports" not in consolidated_inputs.__dict__
    assert "port_profiles" not in consolidated_inputs.__dict__

    loaded_inputs = ConsolidatedAVDDesign._from_dict(json.loads(json.dumps(consolidated_inputs._dump())))
    assert loaded_inputs._dump() == consolidated_inputs._dump()


def test_network_port_platform_candidates_are_included_in_endpoint_vlan_facts() -> None:
    """
    Document the current conservative facts behavior for network-port platform selectors.

    Historically, facts included switch-matched entries without checking their platform, but omitted platform-only entries.
    Including platform-only candidates avoids underestimating endpoint VLANs before structured config applies the exact platform filter.
    However, this can expand the VLANs configured with `only_vlans_in_use`, so it is questionable whether this is the correct
    compatibility behavior. Revisit this test when that potential breaking change is decided explicitly.
    """
    inputs = {
        "leaf1": {
            "fabric_name": "FABRIC",
            "devices": [{"name": "leaf1", "type": "l2leaf", "platform": "OTHER", "filter": {"only_vlans_in_use": True}}],
            "network_ports": [
                {"platforms": ["MATCH"], "switch_ports": ["Ethernet1"], "mode": "access", "vlans": "123"},
                {"switches": ["leaf1"], "platforms": ["MATCH"], "switch_ports": ["Ethernet2"], "mode": "access", "vlans": "124"},
            ],
            "tenants": [{"name": "TEST", "l2vlans": [{"id": 123}, {"id": 124}]}],
        }
    }

    facts = get_avd_facts(inputs, None)["leaf1"]

    assert facts.endpoint_vlans == "123-124"
