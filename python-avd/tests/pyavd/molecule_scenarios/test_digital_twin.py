# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
import sys
from collections import defaultdict
from copy import deepcopy
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from pyavd import get_device_config, get_device_doc, get_device_structured_config, get_fabric_documentation, validate_inputs, validate_structured_config
from pyavd._utils import get
from pyavd.api.fabric_documentation import FabricDocumentation
from tests.models import MoleculeHost, MoleculeScenario


def mocked_hostvars(self: MoleculeHost, digital_twin_environment: str = "act") -> dict:
    match digital_twin_environment:
        case "act":
            staged_hostvars = json.loads(
                json.dumps(
                    self.scenario._vars.get_vars(host=self.ansible_host)
                    | {
                        "digital_twin_mode": True,
                        "digital_twin": {
                            "environment": "act",
                            "fabric": {
                                "username": "act_user",
                                "password": "act_pass",
                                "os_version": "4.33.0F",
                            },
                        },
                    }
                )
            )
            # Drop Inline Jinja keys
            for node_type_key in get(staged_hostvars, "node_type_keys", []):
                if "ip_addressing" in node_type_key:
                    node_type_key.pop("ip_addressing", None)
            return staged_hostvars
        case _:
            return {}


@pytest.mark.molecule_scenarios(
    ("eos_designs-twodc-5stage-clos", "inventory/digital_twin/act"),
)
def test_digital_twin_act_get_device_config(molecule_host: MoleculeHost) -> None:
    """Test get_device_config for Digital Twin ACT mode."""
    structured_config = deepcopy(molecule_host.structured_config)

    expected_config = molecule_host.config

    if not get(structured_config, "eos_cli_config_gen_configuration.enable", default=True):
        return

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    assert device_config == expected_config


@pytest.mark.molecule_scenarios(
    ("eos_designs-twodc-5stage-clos", "inventory/digital_twin/act"),
)
def test_digital_twin_act_get_device_doc(molecule_host: MoleculeHost) -> None:
    """Test get_device_config for Digital Twin ACT mode."""
    structured_config = deepcopy(molecule_host.structured_config)

    if not get(structured_config, "eos_cli_config_gen_documentation.enable", default=True):
        return

    if not get(structured_config, "generate_device_documentation", default=True):
        return

    # run validation on structured_config to ensure it is covered
    validate_structured_config(structured_config)

    expected_doc = molecule_host.doc

    add_md_toc = get(structured_config, "eos_cli_config_gen_documentation.toc", default=True)
    device_doc = get_device_doc(structured_config, add_md_toc=add_md_toc)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc


@pytest.mark.molecule_scenarios(
    ("eos_designs-twodc-5stage-clos", "inventory/digital_twin/act"),
)
def test_digital_twin_act_get_device_structured_config(molecule_host: MoleculeHost, monkeypatch: Any) -> None:
    """Test get_device_structured_config for Digital Twin ACT mode."""
    for host in molecule_host.scenario.hosts:
        host.__dict__.pop("hostvars", None)
        monkeypatch.setattr(type(host), "hostvars", property(lambda host: mocked_hostvars(host, "act")))

    inputs = deepcopy(molecule_host.hostvars)

    # run validation on inputs to ensure it is converted
    validate_inputs(inputs)

    expected_structured_config = molecule_host.structured_config

    with patch("sys.path", [*sys.path, *molecule_host.scenario.extra_python_paths]):
        avd_facts = molecule_host.scenario.avd_facts
        structured_config = get_device_structured_config(molecule_host.name, inputs, avd_facts)

    # Drop calculated IPs on Spines' P2P links due to inability to support inline Jinja
    for ethernet_interface in get(expected_structured_config, "ethernet_interfaces", []):
        ethernet_interface.pop("ip_address", None)
    for bgp_peer in get(expected_structured_config, "router_bgp.neighbors", []):
        bgp_peer.pop("ip_address", None)
    for ethernet_interface in get(structured_config, "ethernet_interfaces", []):
        ethernet_interface.pop("ip_address", None)
    for bgp_peer in get(structured_config, "router_bgp.neighbors", []):
        bgp_peer.pop("ip_address", None)

    assert isinstance(structured_config, dict)
    assert molecule_host.name == structured_config["hostname"]
    assert expected_structured_config == structured_config
    # Test that we can dump the returned data as json.
    assert json.dumps(structured_config)


@pytest.mark.molecule_scenarios(
    ("eos_designs-twodc-5stage-clos", "inventory/digital_twin/act"),
)
def test_digital_twin_act_get_fabric_documentation(molecule_scenario: MoleculeScenario, monkeypatch: Any) -> None:
    """Test get_fabric_documentation for Digital Twin ACT mode."""
    for host in molecule_scenario.hosts:
        host.__dict__.pop("hostvars", None)
        monkeypatch.setattr(type(host), "hostvars", property(lambda host: mocked_hostvars(host, "act")))

    with patch("sys.path", [*sys.path, *molecule_scenario.extra_python_paths]):
        device_digital_twin_metadata = defaultdict(dict)
        for host in molecule_scenario.hosts:
            device_digital_twin_metadata[host.name] = get(host.structured_config, "metadata")
            host.__dict__.pop("structured_config", None)

        # Temporarily adjust scenario's path to get original structured config for the devices.
        # This is required for generating documentation based on the same ip addressing scheme that was used by Molecule.
        original_artifacts_path_offset = molecule_scenario.artifacts_path_offset
        molecule_scenario.artifacts_path_offset = Path()

        molecule_structured_configs = {
            host.name: deepcopy(host.structured_config | {"metadata": device_digital_twin_metadata[host.name]}) for host in molecule_scenario.hosts
        }

        # Rollback scenario's path
        molecule_scenario.artifacts_path_offset = original_artifacts_path_offset
        del original_artifacts_path_offset

        molecule_avd_facts = molecule_scenario.avd_facts

        # Get variables from the first molecule host.
        first_hostvars = next(iter(molecule_scenario.hosts)).hostvars
        molecule_fabric_name: str = first_hostvars["fabric_name"]
        enable = get(first_hostvars, "eos_designs_documentation.enable", default=True)
        connected_endpoints = get(first_hostvars, "eos_designs_documentation.connected_endpoints", default=False)
        topology_csv = get(first_hostvars, "eos_designs_documentation.topology_csv", default=False)
        p2p_links_csv = get(first_hostvars, "eos_designs_documentation.p2p_links_csv", default=False)
        toc = get(first_hostvars, "eos_designs_documentation.toc", default=True)
        digital_twin = get(first_hostvars, "digital_twin_mode", default=True)

        fabric_documentation_obj = get_fabric_documentation(
            avd_facts=molecule_avd_facts,
            structured_configs=molecule_structured_configs,
            fabric_name=molecule_fabric_name,
            fabric_documentation=enable,
            include_connected_endpoints=connected_endpoints,
            topology_csv=topology_csv,
            p2p_links_csv=p2p_links_csv,
            toc=toc,
            digital_twin=digital_twin,
        )

    assert isinstance(fabric_documentation_obj, FabricDocumentation)

    if enable:
        # We expect fabric docs
        assert isinstance(molecule_scenario.fabric_documentation, str)
        assert fabric_documentation_obj.fabric_documentation == molecule_scenario.fabric_documentation
    else:
        # No fabric docs
        assert molecule_scenario.fabric_documentation is None
        assert fabric_documentation_obj.fabric_documentation == ""

    if topology_csv:
        # We expect topology csv
        assert isinstance(molecule_scenario.topology_csv, str)
        assert fabric_documentation_obj.topology_csv == molecule_scenario.topology_csv
    else:
        # No topology csv
        assert molecule_scenario.topology_csv is None
        assert fabric_documentation_obj.topology_csv == ""

    if p2p_links_csv:
        # We expect p2p links csv
        assert isinstance(molecule_scenario.p2p_links_csv, str)
        assert fabric_documentation_obj.p2p_links_csv == molecule_scenario.p2p_links_csv
    else:
        # No p2p links csv
        assert molecule_scenario.p2p_links_csv is None
        assert fabric_documentation_obj.p2p_links_csv == ""
