# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_documentation import ActionModule, _normalize_yaml_data
from pyavd.api.fabric_documentation import (
    ContainerlabDefaults,
    ContainerlabDigitalTwin,
    ContainerlabKind,
    ContainerlabMgmt,
    ContainerlabNode,
    ContainerlabTopology,
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_documentation"
LOG_HANDLERS_PATH = "ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_handlers"
LOG_CONFIG_PATH = "ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_config"
MOCK_TMP_DIR = "/avd/mocked/tmp"
FABRIC_NAME = "DC1_FABRIC"


"""Default validated_args returned by the action module's argument-spec validation.

Tests spread this and override only the keys relevant to the scenario under test.
"""
BASE_VALIDATED_ARGS = {
    "tmp_dir": MOCK_TMP_DIR,
    "structured_config_dir": "/output/structured_configs",
    "structured_config_suffix": "yml",
    "fabric_documentation": True,
    "include_connected_endpoints": False,
    "topology_csv": False,
    "p2p_links_csv": False,
    "toc": True,
    "digital_twin": False,
}


def test_normalize_yaml_data_recursively_honors_dataclass_yaml_keys() -> None:
    """Normalize nested cLab-shaped dataclasses into YAML-ready data while preserving explicit YAML key aliases."""

    @dataclass(frozen=True)
    class ContainerlabNode:
        mgmt_ipv4: str = field(metadata={"yaml_key": "mgmt-ipv4"})

    @dataclass(frozen=True)
    class ContainerlabKind:
        enforce_startup_config: bool = field(metadata={"yaml_key": "enforce-startup-config"})
        image: str

    @dataclass(frozen=True)
    class ContainerlabMgmt:
        network: str
        ipv4_subnet: str = field(metadata={"yaml_key": "ipv4-subnet"})

    @dataclass(frozen=True)
    class ContainerlabTopology:
        nodes: dict[object, ContainerlabNode]
        kinds: tuple[ContainerlabKind, ...]
        endpoint_lists: list[tuple[str, str]]

    @dataclass(frozen=True)
    class ContainerlabDigitalTwin:
        mgmt: ContainerlabMgmt
        topology: ContainerlabTopology

    data = ContainerlabDigitalTwin(
        mgmt=ContainerlabMgmt(network="clab-mgmt", ipv4_subnet="172.16.1.0/24"),
        topology=ContainerlabTopology(
            nodes={1: ContainerlabNode(mgmt_ipv4="172.16.1.101")},
            kinds=(ContainerlabKind(enforce_startup_config=True, image="ceos:latest"),),
            endpoint_lists=[("leaf1:eth1", "spine1:eth1")],
        ),
    )

    assert _normalize_yaml_data(data) == {
        "mgmt": {"network": "clab-mgmt", "ipv4-subnet": "172.16.1.0/24"},
        "topology": {
            "nodes": {"1": {"mgmt-ipv4": "172.16.1.101"}},
            "kinds": [{"enforce-startup-config": True, "image": "ceos:latest"}],
            "endpoint_lists": [["leaf1:eth1", "spine1:eth1"]],
        },
    }


def _empty_output() -> MagicMock:
    """Return a mock FabricDocumentation with all outputs empty so no files are written."""
    output = MagicMock()
    output.fabric_documentation = ""
    output.topology_csv = ""
    output.p2p_links_csv = ""
    output.digital_twin = None
    return output


def test_read_structured_configs_warns_with_each_missing_device_name(
    action_module: Callable[..., ActionModule], tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    module = action_module(ActionModule)
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    with caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"):
        result = module.read_structured_configs(["spine1", "leaf1", "leaf2"], str(tmp_path), "yml")

    assert result == {"spine1": {"hostname": "spine1"}}
    assert len(caplog.records) == 1
    record = caplog.records[0]
    assert record.levelno == logging.WARNING
    assert record.getMessage() == "Could not find structured config files for 'leaf1,leaf2'. The documentation may be incomplete."


def test_run_routes_missing_device_warning_to_display(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """End-to-end: a WARNING logged in read_structured_configs is routed to display.warning with the missing device name visible."""
    module = action_module(ActionModule)
    facts_path = tmp_path / "eos_designs_facts.json"
    facts_path.write_text(json.dumps({"spine1": {}, "leaf1": {}}), encoding="UTF-8")
    structured_dir = tmp_path / "structured_configs"
    structured_dir.mkdir()
    (structured_dir / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    validated_args = {**BASE_VALIDATED_ARGS, "structured_config_dir": str(structured_dir), "fabric_documentation": False}

    # verbosity=3 makes the base class configure the AVD logger at DEBUG, routing WARNING to display.warning
    shared_display = MagicMock(verbosity=3)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=facts_path),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_empty_output()),
        patch(f"{LOG_HANDLERS_PATH}.Display", return_value=shared_display),
        patch(f"{LOG_CONFIG_PATH}.Display", return_value=shared_display),
    ):
        result = module.run(task_vars={"fabric_name": FABRIC_NAME, "inventory_hostname": "spine1"})

    expected_message = "Could not find structured config files for 'leaf1'. The documentation may be incomplete."
    warning_messages = [call.args[0] for call in shared_display.warning.call_args_list]
    assert warning_messages == [expected_message]
    assert result.get("failed") is not True


def test_main_writes_containerlab_topology_with_ordered_name_and_prefix(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """Cover the cLab-only topology key ordering: name and prefix must be emitted first."""
    module = action_module(ActionModule)
    module.result["changed"] = False
    topology_file = tmp_path / "fabric.clab.yml"
    output = _empty_output()
    output.digital_twin = ContainerlabDigitalTwin(
        name="DC1",
        prefix="",
        mgmt=ContainerlabMgmt(network="clab-mgmt", ipv4_subnet="172.16.1.0/24"),
        topology=ContainerlabTopology(
            defaults=ContainerlabDefaults(kind="arista_ceos"),
            kinds={"arista_ceos": ContainerlabKind(enforce_startup_config=True, image="ceos:latest")},
            nodes={"leaf1": ContainerlabNode(mgmt_ipv4="172.16.1.101")},
            links=(),
        ),
    )
    written_files: dict[str, str] = {}

    def mock_write_file(content: str, filename: str, file_mode: str) -> bool:
        assert file_mode == "0o664"
        written_files[filename] = content
        return True

    with (
        patch.object(
            module,
            "_validate_args",
            return_value={
                **BASE_VALIDATED_ARGS,
                "digital_twin": True,
                "digital_twin_file": str(topology_file),
                "mode": "0o664",
            },
        ),
        patch.object(module, "load_facts", return_value={}),
        patch.object(module, "read_structured_configs", return_value={}),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=output),
        patch(f"{MODULE_PATH}.write_file", side_effect=mock_write_file),
    ):
        module.main(task_vars={"fabric_name": FABRIC_NAME, "digital_twin": {"environment": "containerlab"}})

    assert written_files[str(topology_file)].splitlines()[:3] == ["---", "name: DC1", "prefix: ''"]


# ---------------------------------------------------------------------------
# Exceptions: user-visible failure messages.
# ---------------------------------------------------------------------------


def test_load_facts_raises_with_path_and_upstream_task_when_file_missing(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """The error message names the missing path and points the user at the upstream eos_designs_facts task."""
    module = action_module(ActionModule)
    module.tmp_dir = str(tmp_path)
    missing_path = tmp_path / "eos_designs_facts.json"

    with (
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=missing_path),
        pytest.raises(
            FileNotFoundError,
            match=r"Missing AVD eos_designs facts to generate documentation .*Ensure the 'arista.avd.eos_designs_facts' task ran successfully.",
        ),
    ):
        module.load_facts()


def test_run_wraps_exceptions_as_action_fail(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """Test that any exception during execution is wrapped with the 'Error during plugin ... execution:' prefix and chained."""
    module = action_module(ActionModule, ansible_name="arista.avd.eos_designs_documentation")
    facts_path = tmp_path / "eos_designs_facts.json"
    facts_path.write_text(json.dumps({"spine1": {}}), encoding="UTF-8")
    validated_args = {**BASE_VALIDATED_ARGS, "structured_config_dir": str(tmp_path)}
    original_error = RuntimeError("pyavd exploded")
    shared_display = MagicMock(verbosity=0)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=facts_path),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", side_effect=original_error),
        patch(f"{LOG_HANDLERS_PATH}.Display", return_value=shared_display),
        patch(f"{LOG_CONFIG_PATH}.Display", return_value=shared_display),
        pytest.raises(AnsibleActionFail, match=r"Error during plugin 'arista.avd.eos_designs_documentation' execution: pyavd exploded") as exc_info,
    ):
        module.run(task_vars={"fabric_name": FABRIC_NAME, "inventory_hostname": "spine1"})

    assert exc_info.value.__cause__ is original_error


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised immediately when pyavd is missing."""
    module = action_module(ActionModule, ansible_name="arista.avd.eos_designs_documentation")
    shared_display = MagicMock(verbosity=0)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{LOG_HANDLERS_PATH}.Display", return_value=shared_display),
        patch(f"{LOG_CONFIG_PATH}.Display", return_value=shared_display),
        pytest.raises(AnsibleActionFail, match=r"The 'arista.avd.eos_designs_documentation' plugin requires the 'pyavd' Python library. Got import error."),
    ):
        module.run(task_vars={"fabric_name": FABRIC_NAME, "inventory_hostname": "spine1"})
