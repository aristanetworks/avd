# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test pyAVD entrypoint input variants and focused consolidation contracts not covered by e2e-test-avd."""

import json

import pytest

from pyavd import get_avd_facts, get_device_structured_config
from pyavd._eos_designs.consolidate.consolidator import consolidate_avd_design
from pyavd.api.interface_descriptions import AvdInterfaceDescriptions, InterfaceDescriptionData
from pyavd.api.schemas import AVDDesign, ConsolidatedAVDDesign

INPUTS = {
    "testhost1": {"fabric_name": "FABRIC", "devices": [{"name": "testhost1", "type": "l2leaf"}]},
}


class RawInputsInterfaceDescriptions(AvdInterfaceDescriptions):
    """Custom interface descriptions used to verify the public input attributes."""

    def connected_endpoints_ethernet_interface(self, data: InterfaceDescriptionData) -> str:  # noqa: ARG002
        assert self.inputs.devices
        assert self.inputs.network_ports
        assert self.shared_utils.inputs is self.inputs
        return "RAW_INPUTS"


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


def test_custom_interface_descriptions_receive_raw_inputs(monkeypatch: pytest.MonkeyPatch) -> None:
    raw_inputs = {
        "fabric_name": "FABRIC",
        "devices": [{"name": "testhost1", "type": "l2leaf"}],
        "network_ports": [{"switches": ["testhost1"], "switch_ports": ["Ethernet1"], "mode": "access", "vlans": "10"}],
        "network_services": [{"name": "TEST", "l2vlans": [{"id": 10}]}],
    }
    inputs = AVDDesign._load(raw_inputs)
    node_type_key = next(node_type_key for node_type_key in inputs.node_type_keys if node_type_key.type == "l2leaf")
    node_type_key.interface_descriptions.python_module = "custom_interface_descriptions"
    consolidated_inputs = consolidate_avd_design("testhost1", inputs)
    monkeypatch.setattr(
        "pyavd._eos_designs.shared_utils.interface_descriptions.load_python_class",
        lambda *_args: RawInputsInterfaceDescriptions,
    )

    avd_facts = get_avd_facts(
        {"testhost1": inputs},
        all_consolidated_inputs={"testhost1": consolidated_inputs},
    )
    structured_config = get_device_structured_config(
        "testhost1",
        inputs,
        avd_facts,
        consolidated_inputs=consolidated_inputs,
    )

    assert structured_config.ethernet_interfaces["Ethernet1"].description == "RAW_INPUTS"


def test_get_avd_facts_does_not_mutate_input_models() -> None:
    raw_inputs = {
        "fabric_name": "FABRIC",
        "_root_custom_data": {"preserved": True},
        "type": "l2leaf",
        "l2leaf": {
            "defaults": {"platform": "7050SX3"},
            "nodes": [{"name": "testhost1", "filter": {"tags": ["accepted"]}}],
        },
        "network_services_keys": [{"name": "tenants"}],
        "tenants": [
            {
                "name": "TEST",
                "l2vlans": [
                    {"id": 10, "tags": ["accepted"]},
                    {"id": 20, "tags": ["rejected"]},
                ],
                "vrfs": [
                    {
                        "name": "BLUE",
                        "svis": [
                            {"id": 30, "tags": ["accepted"]},
                            {"id": 40, "tags": ["rejected"]},
                        ],
                    }
                ],
            }
        ],
    }
    inputs = AVDDesign._load(raw_inputs)
    source_node = inputs._dynamic_keys.node_types["l2leaf"].value.nodes["testhost1"]
    source_tenant = inputs._dynamic_keys.network_services["tenants"].value["TEST"]
    original_node = source_node._dump()
    original_tenant = source_tenant._dump()

    avd_facts = get_avd_facts(all_inputs={"testhost1": inputs})

    assert "l2leaf" in inputs._dynamic_keys.node_types
    assert source_node._dump() == original_node
    assert source_tenant._dump() == original_tenant
    assert inputs._custom_data == {"_root_custom_data": {"preserved": True}}
    assert avd_facts["testhost1"].vlans == "10,30"

    structured_config = get_device_structured_config("testhost1", inputs, avd_facts)

    assert "l2leaf" in inputs._dynamic_keys.node_types
    assert source_node._dump() == original_node
    assert source_tenant._dump() == original_tenant
    assert inputs._custom_data == {"_root_custom_data": {"preserved": True}}
    assert structured_config.hostname == "testhost1"
    assert [vlan.id for vlan in structured_config.vlans] == [30, 10]


def test_consolidated_avd_design_json_round_trip() -> None:
    consolidated_inputs = consolidate_avd_design("testhost1", INPUTS["testhost1"])
    dumped_inputs = consolidated_inputs._dump()

    assert "inputs" not in dumped_inputs
    assert "consolidated" not in dumped_inputs
    assert dumped_inputs["type"] == "l2leaf"

    loaded_inputs = ConsolidatedAVDDesign._from_dict(json.loads(json.dumps(dumped_inputs)))

    assert isinstance(loaded_inputs, ConsolidatedAVDDesign)
    assert loaded_inputs._dump() == dumped_inputs


def test_connected_endpoints_are_consolidated() -> None:
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

    consolidated_inputs = consolidate_avd_design("testhost1", inputs)

    assert len(consolidated_inputs.connected_endpoints) == 1
    connected_endpoint = consolidated_inputs.connected_endpoints["connected_endpoints"].value["server1"]
    assert connected_endpoint._adapter_indices == [1]
    assert connected_endpoint.adapters[0].mode == "access"
    assert connected_endpoint.adapters[0].vlans == "10"
    assert [network_port._source_index for network_port in consolidated_inputs.network_ports] == [1, 2]
    assert consolidated_inputs.network_ports[0].mode == "access"
    assert [(profile.profile, profile.parent_profile) for profile in consolidated_inputs.port_profile_names] == [("ACCESS_10", None)]


def test_network_port_context_is_restored_after_json_round_trip() -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "devices": [{"name": "testhost1", "type": "l2leaf"}],
        "network_ports": [
            {
                "switches": ["testhost1"],
                "switch_ports": ["Ethernet1-2"],
                "mode": "trunk",
                "vlans": "10",
                "port_channel": {
                    "mode": "active",
                    "lacp_fallback": {"mode": "individual", "individual": {"mode": "access", "vlans": "20"}},
                },
            }
        ],
        "network_services": [{"name": "TEST", "l2vlans": [{"id": 10}, {"id": 20}]}],
    }
    consolidated_inputs = consolidate_avd_design("testhost1", inputs)
    loaded_inputs = ConsolidatedAVDDesign._from_dict(json.loads(json.dumps(consolidated_inputs._dump())))

    facts = get_avd_facts(
        {"testhost1": inputs},
        None,
        all_consolidated_inputs={"testhost1": loaded_inputs},
    )
    structured_config = get_device_structured_config(
        "testhost1",
        inputs,
        facts,
        consolidated_inputs=loaded_inputs,
    )

    assert facts["testhost1"].vlans == "10,20"
    assert [interface.name for interface in structured_config.ethernet_interfaces] == ["Ethernet1", "Ethernet2"]


def test_unsupported_connected_endpoints_and_network_services_are_not_consolidated() -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "custom_node_type_keys": [{"key": "custom", "type": "custom"}],
        "devices": [{"name": "testhost1", "type": "custom"}],
        "port_profiles": [{"profile": "UNUSED"}],
        "connected_endpoints": [{"name": "server1", "adapters": [{"profile": "MISSING"}]}],
        "network_ports": [{"profile": "MISSING"}],
        "network_services": [{"name": "UNUSED", "l2vlans": [{"id": 10}]}],
    }

    consolidated_inputs = consolidate_avd_design("testhost1", inputs)

    assert not consolidated_inputs.connected_endpoints
    assert not consolidated_inputs.network_ports
    assert not consolidated_inputs.port_profile_names
    assert not consolidated_inputs.network_services


def test_network_services_are_consolidated_and_filtered() -> None:
    inputs = {
        "fabric_name": "FABRIC",
        "devices": [
            {
                "name": "testhost1",
                "type": "l2leaf",
                "filter": {"tenants": ["ACCEPTED"], "tags": ["accepted_tag"]},
            }
        ],
        "network_services": [
            {
                "name": "ACCEPTED",
                "_tenant_custom_data": {"future": "retained"},
                "l2vlans": [
                    {"id": 11, "tags": ["accepted_tag"]},
                    {"id": 12, "tags": ["rejected_tag"]},
                ],
            }
        ],
        "network_services_keys": [{"name": "services_a"}, {"name": "services_b"}],
        "services_a": [
            {
                "name": "ACCEPTED",
                "vrfs": [
                    {
                        "name": "BLUE",
                        "svis": [
                            {"id": 21, "name": "accepted_svi", "tags": ["accepted_tag"]},
                            {"id": 22, "name": "rejected_svi", "tags": ["rejected_tag"]},
                        ],
                    }
                ],
            }
        ],
        "services_b": [{"name": "REJECTED", "l2vlans": [{"id": 31}]}],
    }

    consolidated_inputs = consolidate_avd_design("testhost1", inputs)

    assert list(consolidated_inputs.network_services.keys()) == ["network_services", "services_a"]
    assert [vlan.id for vlan in consolidated_inputs.network_services["network_services"].tenants["ACCEPTED"].l2vlans] == [11]
    assert [svi.id for svi in consolidated_inputs.network_services["services_a"].tenants["ACCEPTED"].vrfs["BLUE"].svis] == [21]
    assert consolidated_inputs.network_services["network_services"].tenants["ACCEPTED"]._custom_data == {"_tenant_custom_data": {"future": "retained"}}

    loaded_inputs = ConsolidatedAVDDesign._from_dict(json.loads(json.dumps(consolidated_inputs._dump())))
    assert loaded_inputs.network_services["network_services"].tenants["ACCEPTED"]._custom_data == {"_tenant_custom_data": {"future": "retained"}}


def test_consolidated_network_services_are_used_by_facts() -> None:
    inputs = {
        "leaf1": {
            "fabric_name": "FABRIC",
            "devices": [{"name": "leaf1", "type": "l2leaf", "filter": {"tags": ["accepted_tag"]}}],
            "network_services_keys": [{"name": "services"}],
            "services": [
                {
                    "name": "TEST",
                    "l2vlans": [
                        {"id": 11, "tags": ["accepted_tag"]},
                        {"id": 12, "tags": ["rejected_tag"]},
                    ],
                    "vrfs": [
                        {
                            "name": "BLUE",
                            "svis": [
                                {"id": 21, "name": "accepted_svi", "tags": ["accepted_tag"]},
                                {"id": 22, "name": "rejected_svi", "tags": ["rejected_tag"]},
                            ],
                        }
                    ],
                }
            ],
        }
    }

    facts = get_avd_facts(inputs, None)["leaf1"]

    assert facts.vlans == "11,21"


def test_network_port_platform_candidates_are_included_in_endpoint_vlan_facts() -> None:
    """Document the legacy structured-config behavior for network-port platform selectors with only_vlans_in_use."""
    inputs = {
        "leaf1": {
            "fabric_name": "FABRIC",
            "devices": [{"name": "leaf1", "type": "l2leaf", "platform": "MATCH", "filter": {"only_vlans_in_use": True}}],
            "network_ports": [
                {"platforms": ["MATCH"], "switch_ports": ["Ethernet1"], "mode": "access", "vlans": "123"},
                {"switches": ["leaf1"], "platforms": ["OTHER"], "switch_ports": ["Ethernet2"], "mode": "access", "vlans": "124"},
            ],
            "tenants": [{"name": "TEST", "l2vlans": [{"id": 123}, {"id": 124}]}],
        }
    }

    facts = get_avd_facts(inputs, None)["leaf1"]
    structured_config = get_device_structured_config("leaf1", inputs["leaf1"], {"leaf1": facts})

    assert facts.endpoint_vlans == "124"
    # BUG: The matching platform-only network port incorrectly configures Ethernet1 without configuring its VLAN 123.
    assert [ethernet_interface.name for ethernet_interface in structured_config.ethernet_interfaces] == ["Ethernet1"]
    # BUG: The platform-mismatched switch-selected network port incorrectly configures VLAN 124 without configuring Ethernet2.
    assert [vlan.id for vlan in structured_config.vlans] == [124]
