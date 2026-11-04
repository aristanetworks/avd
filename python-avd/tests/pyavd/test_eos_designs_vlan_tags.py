# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Testing "vlan_tags" on connected endpoints for cases not covered by the molecule scenarios."""

from __future__ import annotations

from typing import Any

import pytest

from pyavd import get_avd_facts, get_device_structured_config
from pyavd._errors import AristaAvdInvalidInputsError


def _inputs(adapter: dict[str, Any], node: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "fabric_name": "FABRIC",
        "type": "l3leaf",
        "l3leaf": {
            "defaults": {"bgp_as": "65001", "loopback_ipv4_pool": "192.168.0.0/24", "vtep_loopback_ipv4_pool": "192.168.1.0/24"},
            "nodes": [{"name": "testhost1", "id": 1, **(node or {})}],
        },
        "tenants": [
            {
                "name": "TENANT_A",
                "mac_vrf_vni_base": 10000,
                "vrfs": [
                    {"name": "VRF_A", "vrf_vni": 1, "svis": [{"id": 610, "name": "SVI_A", "tags": ["ESX"]}]},
                    {"name": "VRF_B", "vrf_vni": 2, "svis": [{"id": 620, "name": "SVI_B", "tags": ["ESX"]}]},
                ],
                "l2vlans": [{"id": 600, "name": "L2VLAN_ESX", "tags": ["ESX"]}],
            },
        ],
        "servers": [{"name": "server_1", "adapters": [{"switches": ["testhost1"], "switch_ports": ["Ethernet1"], **adapter}]}],
    }


def _structured_config(inputs: dict[str, Any]) -> Any:
    avd_facts = get_avd_facts(all_inputs={"testhost1": inputs}, all_hostvars=None)
    return get_device_structured_config("testhost1", inputs, avd_facts)


def _allowed_vlans(structured_config: Any) -> str:
    return structured_config.ethernet_interfaces["Ethernet1"].switchport.trunk.allowed_vlan


def test_vlan_tags_all_vrfs_accepted() -> None:
    assert _allowed_vlans(_structured_config(_inputs({"mode": "trunk", "vlan_tags": ["ESX"]}))) == "600,610,620"


def test_vlan_tags_skip_svis_in_denied_vrfs() -> None:
    inputs = _inputs({"mode": "trunk", "vlan_tags": ["ESX"]}, {"filter": {"deny_vrfs": ["VRF_B"]}})
    assert _allowed_vlans(_structured_config(inputs)) == "600,610"


def test_vlan_tags_skip_svis_in_vrfs_not_allowed() -> None:
    inputs = _inputs({"mode": "trunk", "vlan_tags": ["ESX"]}, {"filter": {"allow_vrfs": ["VRF_B"]}})
    assert _allowed_vlans(_structured_config(inputs)) == "600,620"


def test_vlan_tags_rejected_on_subinterfaces() -> None:
    inputs = _inputs({"vlan_tags": ["ESX"], "subinterfaces": [{"number": 100, "vlan_id": 100}]})
    with pytest.raises(AristaAvdInvalidInputsError, match="'vlan_tags' requires 'mode: trunk'"):
        _structured_config(inputs)


def test_vlan_tags_rejected_on_port_channel_subinterfaces() -> None:
    inputs = _inputs({"vlan_tags": ["ESX"], "port_channel": {"mode": "active", "subinterfaces": [{"number": 100, "vlan_id": 100}]}})
    with pytest.raises(AristaAvdInvalidInputsError, match="'vlan_tags' requires 'mode: trunk'"):
        _structured_config(inputs)
