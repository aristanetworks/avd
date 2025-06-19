# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy
from typing import Any

import pytest
from yaml import CSafeLoader, load

from pyavd import get_device_config, get_device_doc, validate_structured_config
from pyavd._utils import get
from tests.models import MoleculeHost


def mocked_structured_config(self: MoleculeHost, digital_twin_environment: str = "act") -> dict:
    structured_config_path = self.scenario.path / f"inventory/digital_twin/{digital_twin_environment}/intended/structured_configs" / f"{self.name}.yml"
    if not structured_config_path.exists():
        return {}
    return load(structured_config_path.read_text(), CSafeLoader)


def mocked_config(self: MoleculeHost, digital_twin_environment: str = "act") -> str | None:
    config_path = self.scenario.path / f"inventory/digital_twin/{digital_twin_environment}/intended/configs" / f"{self.name}.cfg"
    if not config_path.exists():
        return None
    return config_path.read_text()


def mocked_doc(self: MoleculeHost, digital_twin_environment: str = "act") -> str | None:
    doc_path = self.scenario.path / f"inventory/digital_twin/{digital_twin_environment}/documentation/devices" / f"{self.name}.md"
    if not doc_path.exists():
        return None

    return doc_path.read_text()


@pytest.mark.molecule_scenarios(
    "eos_designs-twodc-5stage-clos",
)
def test_digital_twin_act_get_device_config(molecule_host: MoleculeHost, monkeypatch: Any) -> None:
    """Test get_device_config for Digital Twin ACT mode."""
    molecule_host.__dict__.pop("structured_config", None)
    monkeypatch.setattr(type(molecule_host), "structured_config", property(lambda molecule_host: mocked_structured_config(molecule_host, "act")))
    structured_config = deepcopy(molecule_host.structured_config)

    molecule_host.__dict__.pop("config", None)
    monkeypatch.setattr(type(molecule_host), "config", property(lambda molecule_host: mocked_config(molecule_host, "act")))
    expected_config = molecule_host.config

    if not get(structured_config, "eos_cli_config_gen_configuration.enable", default=True):
        return

    # run validation on structured_config to ensure it is converted
    validate_structured_config(structured_config)

    device_config = get_device_config(structured_config)

    assert isinstance(device_config, str)
    assert device_config == expected_config


@pytest.mark.molecule_scenarios(
    "eos_designs-twodc-5stage-clos",
)
def test_digital_twin_act_get_device_doc(molecule_host: MoleculeHost, monkeypatch: Any) -> None:
    """Test get_device_config for Digital Twin ACT mode."""
    molecule_host.__dict__.pop("structured_config", None)
    monkeypatch.setattr(type(molecule_host), "structured_config", property(lambda molecule_host: mocked_structured_config(molecule_host, "act")))
    structured_config = deepcopy(molecule_host.structured_config)

    if not get(structured_config, "eos_cli_config_gen_documentation.enable", default=True):
        return

    # TODO: Deprecated, remove in 6.0.0
    if not get(structured_config, "generate_device_documentation", default=True):
        return

    # run validation on structured_config to ensure it is covered
    validate_structured_config(structured_config)

    molecule_host.__dict__.pop("doc", None)
    monkeypatch.setattr(type(molecule_host), "doc", property(lambda molecule_host: mocked_doc(molecule_host, "act")))
    expected_doc = molecule_host.doc

    add_md_toc = get(structured_config, "eos_cli_config_gen_documentation.toc", default=True)
    device_doc = get_device_doc(structured_config, add_md_toc=add_md_toc)

    assert isinstance(device_doc, str)
    assert device_doc == expected_doc
