# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from copy import deepcopy
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal

from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from yaml import CSafeLoader, load

from pyavd._eos_designs.eos_designs_facts.get_facts import get_facts
from pyavd._eos_designs.schema import EosDesigns
from pyavd._utils import get
from pyavd.api.pool_manager import PoolManager

if TYPE_CHECKING:
    from ansible.inventory.host import Host as AnsibleHost

    from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts

REPO_ROOT = Path(__file__).parents[2]
MOLECULE_PATH = REPO_ROOT / "ansible_collections/arista/avd/extensions/molecule"
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
    def structured_config(self) -> dict[str, Any]:
        """The intended structured config for the host, as read from the YAML file in the molecule scenario."""
        structured_config_path = self.scenario.path.joinpath(self.scenario.artifacts_path_offset, "intended/structured_configs", f"{self.name}.yml")
        if not structured_config_path.exists():
            return {}

        return load(structured_config_path.read_text(), CSafeLoader)

    def get_test_catalog(self, run_name: Literal["default_run", "allow_bgp_vrfs_run", "filtered_run"]) -> dict[str, Any]:
        """
        Gets the expected ANTA test catalog for a specific run.

        Args:
            run_name: The subdirectory name for the test run.

        Returns:
            The test catalog as a dictionary, or an empty dict if not found.
        """
        test_catalog_path = self.scenario.path.joinpath(
            self.scenario.artifacts_path_offset,
            f"anta/avd_catalogs/{run_name}",
            f"{self.name}.json",
        )

        if not test_catalog_path.exists():
            return {}

        return load(test_catalog_path.read_text(), CSafeLoader)

    @cached_property
    def config(self) -> str | None:
        """The intended EOS config for the host, as read from the cfg file in the molecule scenario."""
        config_path = self.scenario.path.joinpath(self.scenario.artifacts_path_offset, "intended/configs", f"{self.name}.cfg")
        if not config_path.exists():
            return None

        return config_path.read_text()

    @cached_property
    def doc(self) -> str | None:
        """The intended MarkDown documentation for the host, as read from the md file in the molecule scenario."""
        doc_path = self.scenario.path.joinpath(self.scenario.artifacts_path_offset, "documentation/devices", f"{self.name}.md")
        if not doc_path.exists():
            return None

        return doc_path.read_text()

    @cached_property
    def hostvars(self) -> dict[str, Any]:
        """The input vars for the host, as read from the Ansible inventory in the molecule scenario."""
        hostvars = json.loads(json.dumps(self.scenario._vars.get_vars(host=self.ansible_host)))

        # Workaround to drop Jinja templates for tests with digital_twin.
        # TODO: Avoid relying on templates in scenarios executed in pytest.
        if self.scenario.digital_twin:
            for node_type_key in get(hostvars, "node_type_keys", []):
                if "ip_addressing" in node_type_key:
                    node_type_key.pop("ip_addressing", None)
        return hostvars


class MoleculeScenario:
    """Class representing one Molecule scenario."""

    name: str
    path: Path
    hosts: list[MoleculeHost]
    pool_manager: PoolManager | None
    extra_python_paths: list[str]
    artifacts_path_offset: Path
    digital_twin: bool

    def __init__(self, name: str, digital_twin: bool = False) -> None:
        """
        Class representing one Molecule scenario.

        Args:
            name: Molecule scenario name
            digital_twin: Run in digital twin mode. Will prepend "digital_twin" to the paths for 'intended' and 'documentation' folders.

        The Ansible inventory of the Molecule scenario will be parsed and MoleculeHost instances will be inserted into the `hosts` property
        for each host found in the inventory.
        """
        self.name = name
        self.digital_twin = digital_twin
        self.artifacts_path_offset = Path("digital_twin" if self.digital_twin else "")
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
        return get_facts(all_inputs=all_inputs, pool_manager=self.pool_manager, all_hostvars=all_hostvars, digital_twin=self.digital_twin)

    @cached_property
    def fabric_documentation(self) -> str | None:
        """
        The generated Fabric documentation as a markdown string.

        None if no fabric documentation is found in the molecule artifacts.
        """
        fabric_doc_path = self.path.joinpath(self.artifacts_path_offset, "documentation/fabric")
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
        fabric_doc_path = self.path.joinpath(self.artifacts_path_offset, "documentation/fabric")
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
        fabric_doc_path = self.path.joinpath(self.artifacts_path_offset, "documentation/fabric")
        files = list(fabric_doc_path.glob("*-p2p-links.csv"))
        if not files:
            return None

        if len(files) > 1:
            msg = "Found too many P2P Links CSV files: %s"
            raise LookupError(msg, files)

        return files[0].read_text("UTF-8")

    @property
    def structured_configs(self) -> dict[str, dict[str, Any]]:
        """
        A dictionary of intended structured configs for all hosts in the scenario, keyed by hostname.

        This property collects the `structured_config` from each host object in the inventory.
        """
        return {host.name: host.structured_config for host in self.hosts}
