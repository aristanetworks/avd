# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from dataclasses import dataclass, field
from typing import Any

import pytest

from pyavd._utils.normalize_yaml_data import normalize_yaml_data
from pyavd.api.fabric_documentation import ContainerlabKind, ContainerlabMgmt, ContainerlabNode


def test_normalize_yaml_data_nested_dataclasses() -> None:
    """Preserve aliases and mapping keys when serializing nested Digital Twin data."""

    @dataclass(frozen=True)
    class Topology:
        mgmt: ContainerlabMgmt
        nodes: dict[str, ContainerlabNode]
        kinds: tuple[ContainerlabKind, ...]
        interface_mapping: dict[str, dict[str, str]]
        links: list[tuple[str, str]] = field(metadata={"yaml_key": "topology-links"})

    data = Topology(
        mgmt=ContainerlabMgmt(network="custom_mgmt", ipv4_subnet="172.16.1.0/24"),
        nodes={"leaf_1": ContainerlabNode(mgmt_ipv4="172.16.1.101")},
        kinds=(ContainerlabKind(enforce_startup_config=True, image="arista/ceos:latest"),),
        interface_mapping={"EthernetIntf": {"eth1_1": "Ethernet1/1"}},
        links=[("leaf_1:eth1_1", "spine1:eth1")],
    )

    assert normalize_yaml_data(data) == {
        "mgmt": {"network": "custom_mgmt", "ipv4-subnet": "172.16.1.0/24"},
        "nodes": {"leaf_1": {"mgmt-ipv4": "172.16.1.101"}},
        "kinds": [{"enforce-startup-config": True, "image": "arista/ceos:latest", "binds": None}],
        "interface_mapping": {"EthernetIntf": {"eth1_1": "Ethernet1/1"}},
        "topology-links": [["leaf_1:eth1_1", "spine1:eth1"]],
    }


@pytest.mark.parametrize("data", [None, "", "text", 0, True])
def test_normalize_yaml_data_scalars(data: Any) -> None:
    assert normalize_yaml_data(data) == data


def test_normalize_yaml_data_mapping_keys() -> None:
    assert normalize_yaml_data({1: ("leaf1:eth1", "spine1:eth1")}) == {"1": ["leaf1:eth1", "spine1:eth1"]}
