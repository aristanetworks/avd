# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib
import json
import logging
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
import yaml
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_documentation import (
    ActionModule,
    setup_module_logging,
)
from ansible_collections.arista.avd.plugins.plugin_utils.utils import PythonToAnsibleHandler

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_documentation"
MOCK_TMP_DIR = "/avd/mocked/tmp"
FABRIC_NAME = "DC1_FABRIC"


@pytest.fixture
def action_module() -> Callable[..., ActionModule]:
    def _factory(task_args: dict | None = None) -> ActionModule:
        mock_task = MagicMock()
        mock_task.args = task_args or {}
        mock_task.async_val = False
        mock_task.check_mode = False
        return ActionModule(
            task=mock_task,
            connection=MagicMock(),
            play_context=MagicMock(),
            loader=MagicMock(),
            templar=MagicMock(),
            shared_loader_obj=MagicMock(),
        )

    return _factory


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


def _make_output(
    *,
    fabric_documentation: str = "",
    topology_csv: str = "",
    p2p_links_csv: str = "",
    digital_twin: object = None,
) -> MagicMock:
    """Build a stand-in for the FabricDocumentation dataclass that pyavd returns."""
    output = MagicMock()
    output.fabric_documentation = fabric_documentation
    output.topology_csv = topology_csv
    output.p2p_links_csv = p2p_links_csv
    output.digital_twin = digital_twin
    return output


def test_run_strips_empty_args_and_invokes_main(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """Empty values (None and "") are stripped before main() sees them, and tmp_dir is captured on the module."""
    module = action_module()
    raw_args = {**base_validated_args, "structured_config_suffix": None, "fabric_documentation_file": ""}
    expected_main_args = {k: v for k, v in raw_args.items() if k not in {"structured_config_suffix", "fabric_documentation_file"}}

    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), raw_args)),
        patch.object(module, "main", return_value={"changed": False}) as mock_main,
    ):
        result = module.run(task_vars={"fabric_name": FABRIC_NAME})

    mock_main.assert_called_once()
    assert mock_main.call_args.args[0] == expected_main_args
    assert module.tmp_dir == MOCK_TMP_DIR
    assert result == {"changed": False}


@pytest.mark.parametrize(
    ("output_kwargs", "expected_files", "write_results", "expected_changed"),
    [
        pytest.param(
            {"fabric_documentation": "# Fabric\n"},
            {"/output/fabric.md": "# Fabric\n"},
            [True],
            True,
            id="fabric_documentation_only",
        ),
        pytest.param(
            {"topology_csv": "a,b\n1,2\n"},
            {"/output/topology.csv": "a,b\n1,2\n"},
            [True],
            True,
            id="topology_csv_only",
        ),
        pytest.param(
            {"p2p_links_csv": "x,y\n3,4\n"},
            {"/output/p2p_links.csv": "x,y\n3,4\n"},
            [True],
            True,
            id="p2p_links_csv_only",
        ),
        pytest.param(
            {
                "fabric_documentation": "# Fabric\n",
                "topology_csv": "a,b\n1,2\n",
                "p2p_links_csv": "x,y\n3,4\n",
            },
            {
                "/output/fabric.md": "# Fabric\n",
                "/output/topology.csv": "a,b\n1,2\n",
                "/output/p2p_links.csv": "x,y\n3,4\n",
            },
            # First write changed, the other two were no-ops — `changed` must stay True.
            [True, False, False],
            True,
            id="all_text_outputs_changed_accumulates",
        ),
        pytest.param(
            {"fabric_documentation": "# Fabric\n"},
            {"/output/fabric.md": "# Fabric\n"},
            [False],
            False,
            id="output_returned_but_file_unchanged",
        ),
    ],
)
def test_main_writes_only_outputs_returned_by_pyavd(
    action_module: Callable[..., ActionModule],
    base_validated_args: dict,
    output_kwargs: dict[str, str],
    expected_files: dict[str, str],
    write_results: list[bool],
    expected_changed: bool,
) -> None:
    """
    Validate the conditional write logic in ``main()`` for the three text outputs (markdown, topology CSV, p2p-links CSV).

    Asserts four contracts:

    1. A file is written **iff** pyavd's ``FabricDocumentation`` returned non-empty content for that output —
       no extra files, no missing files.
    2. Each output is written to the filename configured in ``validated_args`` (``fabric_documentation_file``,
       ``topology_csv_file``, ``p2p_links_csv_file``).
    3. The per-output toggles from ``validated_args`` are forwarded to ``get_fabric_documentation`` unchanged,
       along with ``fabric_name`` from ``task_vars``.
    4. ``result["changed"]`` OR-accumulates across writes: once any ``write_file`` returns ``True``, the flag
       stays ``True`` even if later writes return ``False`` (file already up-to-date). When the only write
       returns ``False`` the flag stays ``False``.
    """
    module = action_module()
    # Toggle on every requested output so the pyavd call kwargs reflect the test scenario.
    validated_args = {
        **base_validated_args,
        "fabric_documentation": "fabric_documentation" in output_kwargs,
        "topology_csv": "topology_csv" in output_kwargs,
        "p2p_links_csv": "p2p_links_csv" in output_kwargs,
    }

    with (
        patch.object(module, "load_facts", return_value={"spine1": {"hostname": "spine1"}}),
        patch.object(module, "read_structured_configs", return_value={"spine1": {"hostname": "spine1"}}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_make_output(**output_kwargs)) as mock_get_doc,
        patch(f"{MODULE_PATH}.write_file", side_effect=write_results) as mock_write,
    ):
        result = module.main(validated_args, {"fabric_name": FABRIC_NAME}, {})

    written = {call.kwargs["filename"]: call.kwargs["content"] for call in mock_write.call_args_list}
    assert written == expected_files
    assert result.get("changed", False) is expected_changed
    # pyavd is told exactly which outputs were requested.
    assert mock_get_doc.call_args.kwargs["fabric_name"] == FABRIC_NAME
    assert mock_get_doc.call_args.kwargs["fabric_documentation"] is ("fabric_documentation" in output_kwargs)
    assert mock_get_doc.call_args.kwargs["topology_csv"] is ("topology_csv" in output_kwargs)
    assert mock_get_doc.call_args.kwargs["p2p_links_csv"] is ("p2p_links_csv" in output_kwargs)


def test_main_skips_writes_when_pyavd_returns_no_content(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """No write calls are made when pyavd returns an output object with empty fields."""
    module = action_module()

    with (
        patch.object(module, "load_facts", return_value={"spine1": {}}),
        patch.object(module, "read_structured_configs", return_value={"spine1": {}}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_make_output()),
        patch(f"{MODULE_PATH}.write_file") as mock_write,
    ):
        result = module.main(base_validated_args, {"fabric_name": FABRIC_NAME}, {})

    mock_write.assert_not_called()
    assert "changed" not in result


def test_main_writes_digital_twin_with_dashed_keys_and_listified_tuples(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """Digital-twin output is dumped as YAML after key dashing, tuple-to-list coercion, and empty stripping."""
    module = action_module()
    validated_args = {**base_validated_args, "fabric_documentation": False, "digital_twin": True}
    asdict_payload = {"nodes": ({"spine1": "settings"},), "links": (("a", "b"),), "extra_field": None}

    with (
        patch.object(module, "load_facts", return_value={"spine1": {}}),
        patch.object(module, "read_structured_configs", return_value={"spine1": {}}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_make_output(digital_twin=MagicMock())),
        patch(f"{MODULE_PATH}.asdict", return_value=asdict_payload),
        patch(f"{MODULE_PATH}.write_file", return_value=True) as mock_write,
    ):
        module.main(validated_args, {"fabric_name": FABRIC_NAME}, {})

    mock_write.assert_called_once()
    call = mock_write.call_args
    assert call.kwargs["filename"] == "DIGITAL-TWIN-TOPOLOGY.yml"
    dumped = yaml.safe_load(call.kwargs["content"])
    assert dumped == {"nodes": [{"spine1": "settings"}], "links": [["a", "b"]]}
    assert "extra-field" not in dumped  # stripped because the value was None
    assert "extra_field" not in dumped  # underscore form must not survive either


def test_main_raises_when_fabric_name_missing(action_module: Callable[..., ActionModule], base_validated_args: dict) -> None:
    """fabric_name is required from task_vars; pyavd.get raises when it is missing."""
    module = action_module()

    with (
        patch.object(module, "load_facts", return_value={}),
        patch.object(module, "read_structured_configs", return_value={}),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        pytest.raises(Exception, match="fabric_name"),
    ):
        module.main(base_validated_args, {}, {})


def test_load_facts_returns_parsed_json(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """load_facts reads the JSON facts file written by eos_designs_facts."""
    module = action_module()
    module.tmp_dir = str(tmp_path)
    facts = {"spine1": {"hostname": "spine1"}}
    facts_path = tmp_path / "eos_designs_facts.json"
    facts_path.write_text(json.dumps(facts), encoding="UTF-8")

    with patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=facts_path):
        assert module.load_facts() == facts


def test_load_facts_raises_when_file_missing(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """A clear AnsibleActionFail is raised pointing the user at the upstream task."""
    module = action_module()
    module.tmp_dir = str(tmp_path)
    missing_path = tmp_path / "eos_designs_facts.json"

    with (
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=missing_path),
        pytest.raises(
            AnsibleActionFail,
            match=r"Missing AVD eos_designs facts to generate documentation .*Ensure the 'arista\.avd\.eos_designs_facts' task ran successfully\.",
        ),
    ):
        module.load_facts()


def test_read_structured_configs_collects_all_devices(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """All present device files are loaded into a single dict keyed by hostname."""
    module = action_module()
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")
    (tmp_path / "leaf1.yml").write_text("hostname: leaf1\n", encoding="UTF-8")

    result = module.read_structured_configs(["spine1", "leaf1"], str(tmp_path), "yml")

    assert result == {"spine1": {"hostname": "spine1"}, "leaf1": {"hostname": "leaf1"}}


def test_read_structured_configs_warns_when_devices_missing(
    action_module: Callable[..., ActionModule], tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    """A WARNING log lists every device whose structured config file is missing."""
    module = action_module()
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    with caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"):
        result = module.read_structured_configs(["spine1", "leaf1", "leaf2"], str(tmp_path), "yml")

    assert result == {"spine1": {"hostname": "spine1"}}
    assert len(caplog.records) == 1
    assert caplog.records[0].levelno == logging.WARNING
    assert "leaf1" in caplog.text
    assert "leaf2" in caplog.text
    assert "spine1" not in caplog.text
    assert "documentation may be incomplete" in caplog.text


def test_read_structured_configs_silent_when_all_present(action_module: Callable[..., ActionModule], tmp_path: Path, caplog: pytest.LogCaptureFixture) -> None:
    """No warning is emitted when every device has a structured config."""
    module = action_module()
    (tmp_path / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    with caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"):
        module.read_structured_configs(["spine1"], str(tmp_path), "yml")

    assert caplog.records == []


@pytest.mark.parametrize("suffix", ["yml", "yaml"])
def test_read_one_structured_config_loads_yaml(action_module: Callable[..., ActionModule], tmp_path: Path, suffix: str) -> None:
    """YAML files are parsed for both .yml and .yaml suffixes."""
    module = action_module()
    (tmp_path / f"spine1.{suffix}").write_text("hostname: spine1\nrole: spine\n", encoding="UTF-8")

    assert module.read_one_structured_config("spine1", str(tmp_path), suffix) == {"hostname": "spine1", "role": "spine"}


def test_read_one_structured_config_loads_json(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """A non-yaml suffix falls through to JSON parsing."""
    module = action_module()
    (tmp_path / "spine1.json").write_text('{"hostname": "spine1"}', encoding="UTF-8")

    assert module.read_one_structured_config("spine1", str(tmp_path), "json") == {"hostname": "spine1"}


def test_read_one_structured_config_returns_empty_dict_when_missing(action_module: Callable[..., ActionModule], tmp_path: Path) -> None:
    """A missing file produces an empty dict (falsy) — used by the caller to detect missing devices."""
    module = action_module()
    assert module.read_one_structured_config("nope", str(tmp_path), "yml") == {}


def test_setup_module_logging_attaches_handler_and_sets_debug_level() -> None:
    """The bridge handler is attached and the logger level is dropped to DEBUG."""
    result: dict = {}
    setup_module_logging(result)

    logger = logging.getLogger("ansible_collections.arista.avd")
    assert logger.level == logging.DEBUG
    assert any(isinstance(handler, PythonToAnsibleHandler) for handler in logger.handlers)


def test_setup_module_logging_routes_levels_to_result_and_display() -> None:
    """ERROR routes to result['stderr']/failed, WARNING to result['warnings'], INFO/DEBUG to display.v/vvv."""
    result: dict = {}
    setup_module_logging(result)
    logger = logging.getLogger("ansible_collections.arista.avd")
    handler = next(h for h in logger.handlers if isinstance(h, PythonToAnsibleHandler))
    mock_display = MagicMock()
    handler.display = mock_display

    logger.error("boom")
    logger.warning("careful")
    logger.info("fyi")
    logger.debug("trace")

    assert result["failed"] is True
    assert "boom" in result["stderr"]
    assert result["warnings"] == ["careful"]
    mock_display.v.assert_called_once_with("fyi")
    mock_display.vvv.assert_called_once_with("trace")


def test_run_routes_missing_device_warning_through_handler_to_result_warnings(
    action_module: Callable[..., ActionModule],
    base_validated_args: dict,
    tmp_path: Path,
    caplog: pytest.LogCaptureFixture,
) -> None:
    """
    End-to-end: a WARNING raised in read_structured_configs flows through the bridge handler into result['warnings'].

    Runs ``module.run()`` with the real logger/handler chain attached and asserts on both the logger side
    (caplog) and the handler-bridge side (the Ansible result dict).
    """
    module = action_module()
    facts_path = tmp_path / "eos_designs_facts.json"
    facts_path.write_text(json.dumps({"spine1": {}, "leaf1": {}}), encoding="UTF-8")
    structured_dir = tmp_path / "structured_configs"
    structured_dir.mkdir()
    # Only spine1 has a structured config; leaf1 will trigger the WARNING.
    (structured_dir / "spine1.yml").write_text("hostname: spine1\n", encoding="UTF-8")

    validated_args = {**base_validated_args, "structured_config_dir": str(structured_dir), "fabric_documentation": False}

    with (
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_argument_spec", return_value=(MagicMock(), validated_args)),
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=facts_path),
        patch(f"{MODULE_PATH}.EosDesignsFacts"),
        patch(f"{MODULE_PATH}.get_fabric_documentation", return_value=_make_output()),
        caplog.at_level(logging.WARNING, logger="ansible_collections.arista.avd"),
    ):
        result = module.run(task_vars={"fabric_name": FABRIC_NAME})

    expected_message = "Could not find structured config files for 'leaf1'. The documentation may be incomplete."
    # Logger side — the WARNING was emitted exactly once at the right level.
    assert [r.levelno for r in caplog.records] == [logging.WARNING]
    assert caplog.messages == [expected_message]
    # Handler-bridge side — the same message landed in result['warnings'] for Ansible to surface.
    assert result["warnings"] == [expected_message]
    assert result.get("failed") is not True


def test_module_falls_back_to_raise_on_use_when_pyavd_missing() -> None:
    """When pyavd cannot be imported, the symbols become RaiseOnUse sentinels that raise AnsibleActionFail on first call."""
    real_import = importlib.__import__

    def fake_import(name: str, *args: object, **kwargs: object) -> object:
        if name.startswith("pyavd"):
            msg = "pyavd not installed"
            raise ImportError(msg)
        return real_import(name, *args, **kwargs)  # type: ignore[arg-type]

    with patch("builtins.__import__", side_effect=fake_import):
        reloaded = importlib.reload(importlib.import_module(MODULE_PATH))

    try:
        with pytest.raises(AnsibleActionFail, match=r"requires the 'pyavd' Python library"):
            reloaded.get_fabric_documentation()
        with pytest.raises(AnsibleActionFail, match=r"requires the 'pyavd' Python library"):
            reloaded.strip_empties_from_dict({})
    finally:
        # Restore the real module so subsequent tests in this session see pyavd again.
        importlib.reload(importlib.import_module(MODULE_PATH))
