# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_cli_config_gen import ActionModule

if TYPE_CHECKING:
    from collections.abc import Callable

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_cli_config_gen"
MOCK_TMP_DIR = "/avd/mocked/tmp"


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


@pytest.mark.parametrize(
    ("generate_device_config", "generate_device_doc", "expected_messages"),
    [
        pytest.param(
            True,
            True,
            [
                "Validating task arguments...",
                "Validating task arguments [done].",
                "Loading structured config...",
                "Loading structured config [done].",
                "Rendering configuration...",
                "Rendering configuration [done].",
                "Rendering documentation...",
                "Rendering documentation [done].",
            ],
            id="config_and_doc",
        ),
        pytest.param(
            True,
            False,
            [
                "Validating task arguments...",
                "Validating task arguments [done].",
                "Loading structured config...",
                "Loading structured config [done].",
                "Rendering configuration...",
                "Rendering configuration [done].",
            ],
            id="config_only",
        ),
        pytest.param(
            False,
            True,
            [
                "Validating task arguments...",
                "Validating task arguments [done].",
                "Loading structured config...",
                "Loading structured config [done].",
                "Rendering documentation...",
                "Rendering documentation [done].",
            ],
            id="doc_only",
        ),
    ],
)
def test_main_emits_expected_debug_logs(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    generate_device_config: bool,
    generate_device_doc: bool,
    expected_messages: list[str],
) -> None:
    """Verify that main emits the expected sequence of DEBUG log messages."""
    module = action_module()
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": generate_device_config,
        "generate_device_doc": generate_device_doc,
        "config_filename": "/output/config.cfg",
        "documentation_filename": "/output/doc.md",
        "device_doc_toc": False,
    }

    with (
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value={}),
        patch.object(module, "write_file", return_value=False),
        patch(f"{MODULE_PATH}.get_device_config", return_value="! config\n", create=True),
        patch(f"{MODULE_PATH}.get_device_doc", return_value="# doc\n", create=True),
        caplog.at_level(logging.DEBUG, logger="ansible_collections.arista.avd"),
    ):
        module.main("test-device", {}, {})

    assert caplog.messages == expected_messages
    assert all(r.levelno == logging.DEBUG for r in caplog.records)


@pytest.mark.parametrize(
    ("generate_device_config", "generate_device_doc", "expected_display_messages"),
    [
        pytest.param(
            True,
            True,
            [
                "<my-spine-1> Validating task arguments...",
                "<my-spine-1> Validating task arguments [done].",
                "<my-spine-1> Loading structured config...",
                "<my-spine-1> Loading structured config [done].",
                "<my-spine-1> Rendering configuration...",
                "<my-spine-1> Rendering configuration [done].",
                "<my-spine-1> Rendering documentation...",
                "<my-spine-1> Rendering documentation [done].",
            ],
            id="config_and_doc",
        ),
        pytest.param(
            True,
            False,
            [
                "<my-spine-1> Validating task arguments...",
                "<my-spine-1> Validating task arguments [done].",
                "<my-spine-1> Loading structured config...",
                "<my-spine-1> Loading structured config [done].",
                "<my-spine-1> Rendering configuration...",
                "<my-spine-1> Rendering configuration [done].",
            ],
            id="config_only",
        ),
        pytest.param(
            False,
            True,
            [
                "<my-spine-1> Validating task arguments...",
                "<my-spine-1> Validating task arguments [done].",
                "<my-spine-1> Loading structured config...",
                "<my-spine-1> Loading structured config [done].",
                "<my-spine-1> Rendering documentation...",
                "<my-spine-1> Rendering documentation [done].",
            ],
            id="doc_only",
        ),
    ],
)
def test_run_routes_debug_logs_to_display_with_hostname(
    action_module: Callable[..., ActionModule],
    generate_device_config: bool,
    generate_device_doc: bool,
    expected_display_messages: list[str],
) -> None:
    """Verify that debug log messages reach display.vvv prefixed with the device hostname."""
    module = action_module()
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": generate_device_config,
        "generate_device_doc": generate_device_doc,
        "config_filename": "/output/config.cfg",
        "documentation_filename": "/output/doc.md",
        "device_doc_toc": False,
    }

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value={}),
        patch.object(module, "write_file", return_value=False),
        patch(f"{MODULE_PATH}.get_device_config", return_value="! config\n", create=True),
        patch(f"{MODULE_PATH}.get_device_doc", return_value="# doc\n", create=True),
        patch(f"{MODULE_PATH}.display") as mock_display,
    ):
        module.run(task_vars={"inventory_hostname": "my-spine-1"})

    actual = [call.args[0] for call in mock_display.vvv.call_args_list]
    assert actual == expected_display_messages


def test_load_structured_config_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised with a message identifying the missing host."""
    module = action_module()
    module.tmp_dir = MOCK_TMP_DIR

    mock_file_path = MagicMock()
    mock_file_path.exists.return_value = False
    mock_validated_path = MagicMock()
    mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

    with (
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        pytest.raises(AnsibleActionFail, match="Missing the validated structured config for host 'my-spine-device'"),
    ):
        module.load_structured_config("my-spine-device")


def test_main_wraps_exceptions_as_action_fail(action_module: Callable[..., ActionModule]) -> None:
    """Test that any exception during execution is forwarded to raise_action_fail."""
    module = action_module()
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": True,
        "generate_device_doc": False,
        "config_filename": "/output/config.cfg",
    }

    with (
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value={}),
        patch(f"{MODULE_PATH}.get_device_config", side_effect=RuntimeError("pyavd exploded"), create=True),
        pytest.raises(AnsibleActionFail, match="pyavd exploded"),
    ):
        module.main("test-device", {}, {})


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised immediately when pyavd is missing."""
    module = action_module()

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(AnsibleActionFail, match="pyavd"),
    ):
        module.run(task_vars={"inventory_hostname": "test-device"})
