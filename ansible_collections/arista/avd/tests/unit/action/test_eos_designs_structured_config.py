# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import logging
import warnings
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_designs_structured_config import ActionModule

if TYPE_CHECKING:
    from collections.abc import Callable

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_designs_structured_config"
MOCK_TMP_DIR = "/avd/mocked/tmp"
MOCK_HOSTNAME = "my-spine-1"


def _structured_config_stub(data: dict | None = None) -> MagicMock:
    """Build a stub matching the structured_config return shape (has `_as_dict()`)."""
    stub = MagicMock()
    stub._as_dict.return_value = data if data is not None else {"hostname": MOCK_HOSTNAME}
    return stub


def _run_full_happy_path(module: ActionModule, task_args: dict) -> dict:
    """Drive ActionModule.run() through a fully mocked happy path."""
    module._task.args = task_args
    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}.get_templar", return_value=MagicMock()),
        patch.object(ActionModule, "load_validated_inputs", return_value=(MagicMock(), {})),
        patch.object(ActionModule, "load_facts", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.get_structured_config", create=True, return_value=_structured_config_stub()),
        patch(f"{MODULE_PATH}.write_file", return_value=True),
        patch(f"{MODULE_PATH}.AvdSchema"),
        patch(f"{MODULE_PATH}.templater", return_value="extra: value\n"),
        patch(f"{MODULE_PATH}.merge"),
    ):
        return module.run(task_vars={"inventory_hostname": MOCK_HOSTNAME})


# ---------------------------------------------------------------------------
# Logging baseline
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "task_args",
    [
        pytest.param({"tmp_dir": MOCK_TMP_DIR, "dest": "/output/structured.yml"}, id="yaml_dest"),
        pytest.param({"tmp_dir": MOCK_TMP_DIR, "dest": "/output/structured.json"}, id="json_dest"),
        pytest.param({"tmp_dir": MOCK_TMP_DIR}, id="no_dest"),
        pytest.param({"tmp_dir": MOCK_TMP_DIR, "return_structured_config": True}, id="return_facts"),
        pytest.param(
            {"tmp_dir": MOCK_TMP_DIR, "eos_designs_custom_templates": [{"template": "t.j2"}]},
            id="custom_templates",
        ),
    ],
)
def test_run_emits_no_logs_baseline(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    task_args: dict,
) -> None:
    """Baseline assertion that a successful run() emits no log records (DEBUG or higher)."""
    module = action_module(ActionModule)

    with caplog.at_level(logging.DEBUG):
        _run_full_happy_path(module, task_args)

    formatted = [f"{r.levelname} {r.name}: {r.getMessage()}" for r in caplog.records]
    assert formatted == [], f"Unexpected log records emitted by run(): {formatted}"


# ---------------------------------------------------------------------------
# Warnings baseline (including DeprecationWarning)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "task_args",
    [
        pytest.param({"tmp_dir": MOCK_TMP_DIR, "dest": "/output/structured.yml"}, id="yaml_dest"),
        pytest.param({"tmp_dir": MOCK_TMP_DIR, "dest": "/output/structured.json"}, id="json_dest"),
        pytest.param({"tmp_dir": MOCK_TMP_DIR}, id="no_dest"),
        pytest.param(
            {"tmp_dir": MOCK_TMP_DIR, "eos_designs_custom_templates": [{"template": "t.j2"}]},
            id="custom_templates",
        ),
    ],
)
def test_run_emits_no_warnings_baseline(action_module: Callable[..., ActionModule], task_args: dict) -> None:
    """Baseline assertion that a successful run() emits no Python warnings (including DeprecationWarning)."""
    module = action_module(ActionModule)

    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        _run_full_happy_path(module, task_args)

    formatted = [f"{w.category.__name__}: {w.message} ({w.filename}:{w.lineno})" for w in recorded]
    assert formatted == [], f"Unexpected warnings emitted by run(): {formatted}"


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """FileNotFoundError is raised with the documented message when pyavd is missing."""
    module = action_module(ActionModule, ansible_name="arista.avd.eos_designs_structured_config")

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(
            AnsibleActionFail,
            match=(
                r"Error during plugin 'arista.avd.eos_designs_structured_config' execution: "
                r"Requires the 'pyavd' Python library. Got import error"
            ),
        ),
    ):
        module.run(task_vars={"inventory_hostname": MOCK_HOSTNAME})


def test_run_wraps_get_structured_config_exception_with_no_logs(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
) -> None:
    """When get_structured_config raises, run() chains the original via __cause__ and emits no logs."""
    module = action_module(ActionModule, {"tmp_dir": MOCK_TMP_DIR}, ansible_name="arista.avd.eos_designs_structured_config")
    original_error = RuntimeError("pyavd exploded")

    with (
        caplog.at_level(logging.DEBUG, logger="ansible_collections.arista.avd"),
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}.get_templar", return_value=MagicMock()),
        patch.object(ActionModule, "load_validated_inputs", return_value=(MagicMock(), {})),
        patch.object(ActionModule, "load_facts", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.get_structured_config", create=True, side_effect=original_error),
        pytest.raises(AnsibleActionFail, match=r"^Error during plugin 'arista.avd.eos_designs_structured_config' execution: pyavd exploded") as exc_info,
    ):
        module.run(task_vars={"inventory_hostname": MOCK_HOSTNAME})

    assert isinstance(exc_info.value.__cause__, RuntimeError)
    assert "Error during plugin 'arista.avd.eos_designs_structured_config' execution: pyavd exploded" in str(exc_info.value)
    formatted = [f"{r.levelname} {r.name}: {r.getMessage()}" for r in caplog.records]
    assert formatted == [], f"Unexpected log records emitted on error path: {formatted}"


def test_run_wraps_get_structured_config_exception_with_no_warnings(action_module: Callable[..., ActionModule]) -> None:
    """When get_structured_config raises, run() must not emit any Python warnings."""
    module = action_module(ActionModule, {"tmp_dir": MOCK_TMP_DIR}, ansible_name="arista.avd.eos_designs_structured_config")

    with warnings.catch_warnings(record=True) as recorded:
        warnings.simplefilter("always")
        with (
            patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
            patch("ansible.plugins.action.ActionBase.run", return_value={}),
            patch(f"{MODULE_PATH}.get_templar", return_value=MagicMock()),
            patch.object(ActionModule, "load_validated_inputs", return_value=(MagicMock(), {})),
            patch.object(ActionModule, "load_facts", return_value=MagicMock()),
            patch(f"{MODULE_PATH}.get_structured_config", create=True, side_effect=RuntimeError("boom")),
            pytest.raises(AnsibleActionFail),
        ):
            module.run(task_vars={"inventory_hostname": MOCK_HOSTNAME})

    formatted = [f"{w.category.__name__}: {w.message} ({w.filename}:{w.lineno})" for w in recorded]
    assert formatted == [], f"Unexpected warnings emitted on error path: {formatted}"


def test_run_wraps_custom_template_merge_exception(action_module: Callable[..., ActionModule]) -> None:
    """A failure inside merge() during custom-template processing surfaces as AnsibleActionFail with the original chained."""
    module = action_module(
        ActionModule,
        {
            "tmp_dir": MOCK_TMP_DIR,
            "eos_designs_custom_templates": [{"template": "bad.j2"}],
        },
        ansible_name="arista.avd.eos_designs_structured_config",
    )
    original_error = RuntimeError("merge failed")

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch(f"{MODULE_PATH}.get_templar", return_value=MagicMock()),
        patch.object(ActionModule, "load_validated_inputs", return_value=(MagicMock(), {})),
        patch.object(ActionModule, "load_facts", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.get_structured_config", create=True, return_value=_structured_config_stub()),
        patch(f"{MODULE_PATH}.AvdSchema"),
        patch(f"{MODULE_PATH}.templater", return_value="key: value\n"),
        patch(f"{MODULE_PATH}.strip_null_from_data", side_effect=lambda d: d),
        patch(f"{MODULE_PATH}.merge", side_effect=original_error),
        pytest.raises(AnsibleActionFail, match=r"Error during plugin 'arista.avd.eos_designs_structured_config' execution: merge failed") as exc_info,
    ):
        module.run(task_vars={"inventory_hostname": MOCK_HOSTNAME})

    assert isinstance(exc_info.value.__cause__, RuntimeError)
    assert "Error during plugin 'arista.avd.eos_designs_structured_config' execution: merge failed" in str(exc_info.value)


def test_load_validated_inputs_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """load_validated_inputs raises FileNotFoundError with the documented message when the file is missing."""
    module = action_module(ActionModule)
    module.tmp_dir = MOCK_TMP_DIR

    mock_file_path = MagicMock()
    mock_file_path.exists.return_value = False
    mock_validated_path = MagicMock()
    mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

    with (
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
        patch(f"{MODULE_PATH}.get_consolidated_path", return_value=MagicMock()),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        pytest.raises(
            FileNotFoundError,
            match=(
                r"Missing validated inputs for host 'my-spine-1'. "
                r"Ensure the 'arista.avd.validate_inputs' task ran successfully for this host "
                r"and that no validation errors occurred."
            ),
        ),
    ):
        module.load_validated_inputs(MOCK_HOSTNAME)


def test_load_facts_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """load_facts raises FileNotFoundError naming both the host and the missing file path."""
    module = action_module(ActionModule)
    module.tmp_dir = MOCK_TMP_DIR

    facts_path_str = "/avd/mocked/tmp/eos_designs_facts.json"

    class _MissingFactsPath:
        def exists(self) -> bool:
            return False

        def __str__(self) -> str:
            return facts_path_str

    with (
        patch(f"{MODULE_PATH}.get_eos_designs_facts_path", return_value=_MissingFactsPath()),
        pytest.raises(
            FileNotFoundError,
            match=(
                r"Missing AVD eos_designs facts for host 'my-spine-1' "
                rf"\({facts_path_str}\). "
                r"Ensure the 'arista.avd.eos_designs_facts' task ran successfully."
            ),
        ),
    ):
        module.load_facts(MOCK_HOSTNAME)
