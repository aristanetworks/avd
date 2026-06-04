# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_documentation import ActionModule

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_documentation"
MOCK_TMP_DIR = "/avd/mocked/tmp"
FABRIC_NAME = "DC1_FABRIC"


@pytest.fixture
def base_validated_args() -> dict:
    return {
        "tmp_dir": MOCK_TMP_DIR,
        "structured_config_dir": "/output/structured_configs",
        "structured_config_suffix": "yml",
        "fabric_documentation_file": "/output/fabric.md",
        "mode": "0o664",
        "fabric_documentation": True,
        "include_connected_endpoints": False,
        "topology_csv_file": "/output/topology.csv",
        "topology_csv": False,
        "p2p_links_csv_file": "/output/p2p_links.csv",
        "p2p_links_csv": False,
        "toc": True,
        "digital_twin_file": "DIGITAL-TWIN-TOPOLOGY.yml",
        "digital_twin": False,
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


def test_run_routes_missing_device_warning_to_result_warnings(
    action_module: Callable[..., ActionModule], base_validated_args: dict, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """End-to-end: a WARNING logged in read_structured_configs ends up in result['warnings'] with the missing device name visible."""
    module = action_module(ActionModule)
    facts_path = tmp_path / "eos_designs_facts.json"
    facts_path.write_text(json.dumps({"spine1": {}, "leaf1": {}}), encoding="UTF-8")
    structured_dir = tmp_path / "structured_configs"
    structured_dir.mkdir()
    (structured_dir / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    validated_args = {**base_validated_args, "structured_config_dir": str(structured_dir), "fabric_documentation": False}

    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=facts_path),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_empty_output()),
        caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"),
    ):
        result = module.run(task_vars={"fabric_name": FABRIC_NAME})

    expected_message = "Could not find structured config files for 'leaf1'. The documentation may be incomplete."
    assert caplog.messages == [expected_message]
    assert result["warnings"] == [expected_message]
    assert result.get("failed") is not True


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
            AnsibleActionFail,
            match=r"Missing AVD eos_designs facts to generate documentation .*Ensure the 'arista.avd.eos_designs_facts' task ran successfully.",
        ),
    ):
        module.load_facts()
