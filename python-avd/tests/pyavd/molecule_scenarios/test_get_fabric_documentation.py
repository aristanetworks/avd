# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import pytest

from pyavd import get_fabric_documentation
from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
from pyavd.api.fabric_documentation import ACTDigitalTwin, ContainerlabDigitalTwin, FabricDocumentation


def test_get_fabric_documentation_with_no_connected_endpoints(monkeypatch: pytest.MonkeyPatch) -> None:
    """Test connected endpoints documentation empty state."""

    class FabricDocumentationFacts:
        def __init__(self, *args: object, **kwargs: object) -> None:
            pass

        def render(self) -> dict[str, object]:
            return {
                "fabric_name": "EMPTY_FABRIC",
                "toc": False,
                "fabric_switches": [],
                "topology_links": [],
                "uplink_ipv4_networks": [],
                "loopback_ipv4_networks": [],
                "vtep_loopback_ipv4_networks": [],
                "has_isis": False,
                "all_connected_endpoints": {},
                "all_connected_endpoints_keys": [],
                "all_port_profiles": [],
            }

    monkeypatch.setattr("pyavd._eos_designs.fabric_documentation_facts.FabricDocumentationFacts", FabricDocumentationFacts)

    fabric_documentation_obj = get_fabric_documentation(
        avd_facts={},
        structured_configs={},
        fabric_name="EMPTY_FABRIC",
        include_connected_endpoints=True,
        toc=False,
    )

    assert "## Connected Endpoints\n\nNo connected endpoint configured!" in fabric_documentation_obj.fabric_documentation


@pytest.mark.parametrize("digital_twin_enabled", [True, False])
def test_get_fabric_documentation_containerlab(digital_twin_enabled: bool) -> None:
    """Test Containerlab environment selection and the Digital Twin enable flag."""
    fabric_documentation_obj = get_fabric_documentation(
        avd_facts={"leaf1": EosDesignsFacts._from_dict({"mgmt_ip": "192.0.2.1/24"})},
        structured_configs={"leaf1": {"metadata": {"digital_twin": {"environment": "containerlab"}}}},
        fabric_name="CONTAINERLAB_FABRIC",
        fabric_documentation=False,
        digital_twin=digital_twin_enabled,
    )

    assert isinstance(fabric_documentation_obj, FabricDocumentation)
    if digital_twin_enabled:
        assert isinstance(fabric_documentation_obj.digital_twin, ContainerlabDigitalTwin)
        assert fabric_documentation_obj.digital_twin.name == "CONTAINERLAB_FABRIC"
        assert fabric_documentation_obj.digital_twin.prefix == ""
        assert fabric_documentation_obj.digital_twin.mgmt.ipv4_subnet == "192.0.2.0/24"
    else:
        assert fabric_documentation_obj.digital_twin is None


def test_get_digital_twin_returns_none_for_unsupported_environment() -> None:
    """Test fallback behavior through the public documentation API."""
    output = get_fabric_documentation(
        avd_facts={},
        structured_configs={"leaf1": {"metadata": {"digital_twin": {"environment": "unsupported"}}}},
        fabric_name="UNSUPPORTED_FABRIC",
        fabric_documentation=False,
        digital_twin=True,
    )

    assert output.digital_twin is None


def test_get_fabric_documentation_act_gates_optional_node_settings() -> None:
    """Test defensive ACT node-type capability gating through the public documentation API."""
    digital_twin_metadata = {
        "environment": "act",
        "ip_addr": "192.0.2.1/24",
        "version": "4.33.1.1F",
        "username": "cvpadmin",
        "password": "cvp123!",
        "ztp": True,
        "internet_access": True,
    }
    structured_configs = {
        "third-party-tests": {
            "metadata": {
                "serial_number": "THIRD-PARTY-SERIAL",
                "system_mac_address": "02:1c:73:00:00:01",
                "digital_twin": {**digital_twin_metadata, "node_type": "third-party"},
            }
        },
        "veos-tests": {
            "metadata": {
                "serial_number": "VEOS-SERIAL",
                "system_mac_address": "02:1c:73:00:00:02",
                "digital_twin": {**digital_twin_metadata, "node_type": "veos"},
            }
        },
    }
    output = get_fabric_documentation(
        avd_facts={hostname: EosDesignsFacts._from_dict({"mgmt_ip": "192.0.2.1/24"}) for hostname in structured_configs},
        structured_configs=structured_configs,
        fabric_name="ACT_FABRIC",
        fabric_documentation=False,
        digital_twin=True,
    )

    assert isinstance(output.digital_twin, ACTDigitalTwin)
    third_party_node = output.digital_twin.nodes[0]["third-party-tests"]
    assert third_party_node.serial_number is None
    assert third_party_node.system_mac_address is None
    assert third_party_node.ztp is None
    assert third_party_node.internet_access is None

    veos_node = output.digital_twin.nodes[1]["veos-tests"]
    assert veos_node.serial_number == "VEOS-SERIAL"
    assert veos_node.system_mac_address == "02:1c:73:00:00:02"
    assert veos_node.ztp is True
    assert veos_node.internet_access is True
