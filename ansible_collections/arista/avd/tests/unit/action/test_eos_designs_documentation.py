# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
import logging
import warnings
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_documentation import ActionModule
from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

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
    """Stand-in for pyavd's FabricDocumentation with all outputs empty (no writes triggered)."""
    output = MagicMock()
    output.fabric_documentation = ""
    output.topology_csv = ""
    output.p2p_links_csv = ""
    output.digital_twin = None
    return output


def _run_full_happy_path(module: ActionModule, validated_args: dict) -> dict:
    """Drive ``run()`` end-to-end through a no-op pyavd. All devices present, no writes, no warnings."""
    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch.object(ActionModule, "load_facts", return_value={}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_empty_output()),
    ):
        return module.run(task_vars={"fabric_name": FABRIC_NAME})


# ---------------------------------------------------------------------------
# Baseline: the happy path emits no warnings and no log records.
# These pin down the "silent on success" contract so post-migration noise is visible.
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "toggles",
    [
        pytest.param({}, id="defaults"),
        pytest.param({"fabric_documentation": False, "topology_csv": True, "p2p_links_csv": True}, id="csvs_only"),
        pytest.param({"fabric_documentation": False, "digital_twin": True}, id="digital_twin_only"),
    ],
)
def test_run_emits_no_warnings_baseline(action_module: Callable[..., ActionModule], base_validated_args: dict, toggles: dict) -> None:
    module = action_module(ActionModule)
    validated_args = {**base_validated_args, **toggles}

    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        _run_full_happy_path(module, validated_args)

    formatted = [f"{w.category.__name__}: {w.message} ({w.filename}:{w.lineno})" for w in recorded]
    assert formatted == [], f"Unexpected warnings emitted by run(): {formatted}"


@pytest.mark.parametrize(
    "toggles",
    [
        pytest.param({}, id="defaults"),
        pytest.param({"fabric_documentation": False, "topology_csv": True, "p2p_links_csv": True}, id="csvs_only"),
        pytest.param({"fabric_documentation": False, "digital_twin": True}, id="digital_twin_only"),
    ],
)
def test_run_emits_no_logs_baseline(
    action_module: Callable[..., ActionModule], base_validated_args: dict, caplog: pytest.LogCaptureFixture, toggles: dict
) -> None:
    module = action_module(ActionModule)
    validated_args = {**base_validated_args, **toggles}

    with caplog.at_level(logging.DEBUG, logger="ansible_collections.arista.avd"):
        _run_full_happy_path(module, validated_args)

    formatted = [f"{r.levelname} {r.name}: {r.getMessage()}" for r in caplog.records]
    assert formatted == [], f"Unexpected log records emitted by run(): {formatted}"


def test_read_structured_configs_warns_with_each_missing_device_name(
    action_module: Callable[..., ActionModule], tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """The WARNING message names every missing device and explains the user-visible impact."""
    module = action_module(ActionModule)
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    with caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"):
        result = module.read_structured_configs(["spine1", "leaf1", "leaf2"], str(tmp_path), "yml")

    assert result == {"spine1": {"hostname": "spine1"}}
    assert [r.levelno for r in caplog.records] == [logging.WARNING]
    message = caplog.records[0].getMessage()
    assert "leaf1" in message
    assert "leaf2" in message
    assert "spine1" not in message
    assert "documentation may be incomplete" in message


def test_read_structured_configs_silent_when_all_devices_present(
    action_module: Callable[..., ActionModule], tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """No WARNING is emitted when every device has a structured config."""
    module = action_module(ActionModule)
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    with caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"):
        module.read_structured_configs(["spine1"], str(tmp_path), "yml")

    assert caplog.records == []


def test_run_routes_missing_device_warning_to_result_warnings(
    action_module: Callable[..., ActionModule], base_validated_args: dict, tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """
    End-to-end: a WARNING raised in read_structured_configs flows through the bridge handler into result['warnings'].

    This is the post-migration display anchor. The device name in the WARNING message must remain
    visible to the operator after the logging plumbing is replaced.
    """
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


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """When pyavd is missing, the imported symbols are RaiseOnUse sentinels that raise AnsibleActionFail on first call."""
    module = action_module(ActionModule)
    sentinel = RaiseOnUse(
        AnsibleActionFail(
            "The 'arista.avd.eos_designs_documentation' plugin requires the 'pyavd' Python library. Got import error",
        ),
    )

    with (
        patch(f"{MODULE_PATH}.strip_empties_from_dict", new=sentinel),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), base_validated_args)),
        pytest.raises(AnsibleActionFail, match=r"requires the 'pyavd' Python library"),
    ):
        module.run(task_vars={"fabric_name": FABRIC_NAME})


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


def test_run_raises_when_fabric_name_missing(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """fabric_name is required from task_vars; pyavd.get raises a clear error naming the missing key when it is absent."""
    module = action_module(ActionModule)

    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), base_validated_args)),
        patch.object(ActionModule, "load_facts", return_value={}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        pytest.raises(Exception, match="fabric_name"),
    ):
        module.run(task_vars={})
