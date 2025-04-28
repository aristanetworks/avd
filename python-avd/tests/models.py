# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from yaml import CSafeLoader, load

from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
from pyavd._eos_designs.schema import EosDesigns
from pyavd.api.pool_manager import PoolManager

if TYPE_CHECKING:
    from ansible.inventory.host import Host as AnsibleHost

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts

REPO_ROOT = Path(__file__).parents[2]
MOLECULE_PATH = REPO_ROOT / "ansible_collections/arista/avd/molecule"
EXAMPLE_PATH = REPO_ROOT / "ansible_collections/arista/avd/examples"


class MoleculeHost:
    """Class representing one host defined in a Molecule scenario."""

    name: str
    ansible_host: AnsibleHost
    scenario: MoleculeScenario

    def __init__(self, name: str, ansible_host: AnsibleHost, scenario: MoleculeScenario) -> None:
        self.name = name
        self.ansible_host = ansible_host
        self.scenario = scenario

    @cached_property
    def structured_config(self) -> dict:
        """The intended structured config for the host, as read from the YAML file in the molecule scenario."""
        structured_config_path = self.scenario.path / "intended/structured_configs" / f"{self.name}.yml"
        if not structured_config_path.exists():
            return {}

        return load(structured_config_path.read_text(), CSafeLoader)

    @cached_property
    def config(self) -> str | None:
        """The intended EOS config for the host, as read from the cfg file in the molecule scenario."""
        config_path = self.scenario.path / "intended/configs" / f"{self.name}.cfg"
        if not config_path.exists():
            return None

        return config_path.read_text()

    @cached_property
    def doc(self) -> str | None:
        """The intended MarkDown documentation for the host, as read from the md file in the molecule scenario."""
        doc_path = self.scenario.path / "documentation/devices" / f"{self.name}.md"
        if not doc_path.exists():
            return None

        return doc_path.read_text()

    @cached_property
    def hostvars(self) -> dict:
        """The input vars for the host, as read from the Ansible inventory in the molecule scenario."""
        return json.loads(json.dumps(self.scenario._vars.get_vars(host=self.ansible_host)))


class MoleculeScenario:
    """Class representing one Molecule scenario."""

    name: str
    path: Path
    hosts: list[MoleculeHost]
    pool_manager: PoolManager | None
    extra_python_paths: list[str]

    def __init__(self, name: str) -> None:
        """
        Class representing one Molecule scenario.

        Args:
            name: Molecule scenario name

        The Ansible inventory of the Molecule scenario will be parsed and MoleculeHost instances will be inserted into the `hosts` property
        for each host found in the inventory.
        """
        self.name = name
        if name.startswith("example-"):
            # Example paths
            self.path = EXAMPLE_PATH / name.removeprefix("example-")
            inventory_path = self.path / "inventory.yml"
        else:
            # Molecule paths
            self.path = MOLECULE_PATH / name
            inventory_path = self.path / "inventory/hosts.yml"

        if not inventory_path.exists():
            msg = "Molecule inventory file not found: %s"
            raise FileNotFoundError(msg, inventory_path)

        self._inventory = InventoryManager(loader=DataLoader(), sources=[inventory_path.as_posix()])
        self._vars = VariableManager(loader=DataLoader(), inventory=self._inventory)
        self.hosts = []
        for host in self._inventory.get_hosts():
            if self.name.startswith("example-") and host.name in ["cvp", "cloudvision"]:
                # Ignore CVP devices in examples without bloating the example without test groups.
                continue
            if "IGNORE_IN_PYTEST" in [group.name for group in host.groups]:
                # Ignore members of the group IGNORE_IN_PYTEST from Molecule scenarios.
                continue
            self.hosts.append(MoleculeHost(name=host.name, ansible_host=host, scenario=self))
        self.pool_manager = PoolManager(self.path / "intended")

        self.extra_python_paths = []
        if (extra_python_paths_file := self.path / "extra_python_paths").exists():
            with extra_python_paths_file.open() as f:
                self.extra_python_paths = [str(self.path / line[:-1]) for line in f.readlines()]

    @cached_property
    def avd_facts(self) -> dict[str, EosDesignsFacts]:
        """The AVD facts calculated from the full Ansible inventory in the molecule scenario."""
        all_hostvars = {host.name: deepcopy(host.hostvars) for host in self.hosts}
        all_inputs = {hostname: EosDesigns._from_dict(hostvars) for hostname, hostvars in all_hostvars.items()}
        return get_facts(all_inputs=all_inputs, pool_manager=self.pool_manager, all_hostvars=all_hostvars)

    @cached_property
    def fabric_documentation(self) -> str | None:
        """
        The generated Fabric documentation as a markdown string.

        None if no fabric documentation is found in the molecule artifacts.
        """
        fabric_doc_path = self.path / "documentation/fabric"
        files = list(fabric_doc_path.glob("*-documentation.md"))
        if not files:
            return None

        if len(files) > 1:
            msg = "Found too many fabric documentation files: %s"
            raise LookupError(msg, files)

        return files[0].read_text("UTF-8")

    @cached_property
    def topology_csv(self) -> str | None:
        """
        The generated Topology CSV as a markdown string.

        None if no Topology CSV is found in the molecule artifacts.
        """
        fabric_doc_path = self.path / "documentation/fabric"
        files = list(fabric_doc_path.glob("*-topology.csv"))
        if not files:
            return None

        if len(files) > 1:
            msg = "Found too many Topology CSV files: %s"
            raise LookupError(msg, files)

        return files[0].read_text("UTF-8")

    @cached_property
    def p2p_links_csv(self) -> str | None:
        """
        The generated P2P Links CSV as a markdown string.

        None if no P2P Links CSV is found in the molecule artifacts.
        """
        fabric_doc_path = self.path / "documentation/fabric"
        files = list(fabric_doc_path.glob("*-p2p-links.csv"))
        if not files:
            return None

        if len(files) > 1:
            msg = "Found too many P2P Links CSV files: %s"
            raise LookupError(msg, files)

        return files[0].read_text("UTF-8")
