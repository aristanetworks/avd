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


@pytest.mark.parametrize(
    ("generate_device_config", "generate_device_doc", "with_custom_templates", "expected_messages"),
    [
        pytest.param(
            True,
            True,
            False,
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
            False,
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
        pytest.param(
            True,
            True,
            True,
            [
                "Validating task arguments...",
                "Validating task arguments [done].",
                "Loading structured config...",
                "Loading structured config [done].",
                "Rendering configuration...",
                "Rendering config custom templates...",
                "Rendering config custom templates [done].",
                "Rendering configuration [done].",
                "Rendering documentation...",
                "Rendering documentation custom templates...",
                "Rendering documentation custom templates [done].",
                "Rendering documentation [done].",
            ],
            id="config_and_doc_with_custom_templates",
        ),
    ],
)
def test_run_emits_expected_debug_logs_and_routes_to_display(
    action_module: Callable[..., ActionModule],
    caplog: pytest.LogCaptureFixture,
    generate_device_config: bool,
    generate_device_doc: bool,
    with_custom_templates: bool,
    expected_messages: list[str],
) -> None:
    """Verify run emits the expected DEBUG logs and routes them to display.vvv prefixed with the hostname."""
    hostname = "my-spine-1"
    module = action_module(ActionModule)
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": generate_device_config,
        "generate_device_doc": generate_device_doc,
        "config_filename": "/output/config.cfg",
        "documentation_filename": "/output/doc.md",
        "device_doc_toc": False,
    }
    task_vars: dict = {"inventory_hostname": hostname}
    if with_custom_templates:
        task_vars["custom_templates"] = ["some/template.j2"]

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=True),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value={}),
        patch.object(module, "write_file", return_value=False),
        patch.object(module, "render_template_with_ansible_templar", return_value="! custom\n"),
        patch(f"{MODULE_PATH}.get_device_config", return_value="! config\n", create=True),
        patch(f"{MODULE_PATH}.get_device_doc", return_value="# doc\n", create=True),
        patch(f"{MODULE_PATH}.display") as mock_display,
        caplog.at_level(logging.DEBUG, logger="ansible_collections.arista.avd"),
    ):
        module.run(task_vars=task_vars)

    assert caplog.messages == expected_messages
    assert all(r.levelno == logging.DEBUG for r in caplog.records)
    display_messages = [call.args[0] for call in mock_display.vvv.call_args_list]
    assert display_messages == [f"<{hostname}> {msg}" for msg in expected_messages]


def test_load_structured_config_raises_when_file_missing(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised with a message identifying the missing host."""
    module = action_module(ActionModule)
    module.tmp_dir = MOCK_TMP_DIR

    mock_file_path = MagicMock()
    mock_file_path.exists.return_value = False
    mock_validated_path = MagicMock()
    mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

    with (
        patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
        patch(f"{MODULE_PATH}.AVDVaultHandler"),
        patch(f"{MODULE_PATH}.AVDFileHandler"),
        pytest.raises(
            AnsibleActionFail,
            match=(
                r"Missing the validated structured config for host 'my-spine-device'. "
                r"Ensure the 'arista.avd.validate_inputs' task ran successfully for this host "
                r"and that no validation errors occurred."
            ),
        ),
    ):
        module.load_structured_config("my-spine-device")


def test_main_wraps_exceptions_as_action_fail(action_module: Callable[..., ActionModule]) -> None:
    """Test that any exception during execution is wrapped with the 'Error during plugin execution:' prefix and chained."""
    module = action_module(ActionModule)
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": True,
        "generate_device_doc": False,
        "config_filename": "/output/config.cfg",
    }
    original_error = RuntimeError("pyavd exploded")

    with (
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value={}),
        patch(f"{MODULE_PATH}.get_device_config", side_effect=original_error, create=True),
        pytest.raises(AnsibleActionFail, match=r"Error during plugin execution: pyavd exploded") as exc_info,
    ):
        module.main("test-device", {}, {})

    assert exc_info.value.__cause__ is original_error


def test_main_passes_hide_passwords_options_to_pyavd(action_module: Callable[..., ActionModule]) -> None:
    """Verify role render settings are passed explicitly to PyAVD."""
    module = action_module(ActionModule)
    structured_config = {"hostname": "test-device"}
    validated_args = {
        "tmp_dir": MOCK_TMP_DIR,
        "generate_device_config": True,
        "generate_device_doc": True,
        "config_filename": "/output/config.cfg",
        "documentation_filename": "/output/doc.md",
        "device_doc_toc": False,
        "configuration_hide_passwords": True,
        "documentation_hide_passwords": False,
    }

    with (
        patch.object(module, "validate_args", return_value=validated_args),
        patch.object(module, "load_structured_config", return_value=structured_config),
        patch.object(module, "write_file", return_value=False),
        patch(f"{MODULE_PATH}.get_device_config", return_value="! config\n", create=True) as mock_get_device_config,
        patch(f"{MODULE_PATH}.get_device_doc", return_value="# doc\n", create=True) as mock_get_device_doc,
    ):
        module.main("test-device", {}, {})

    assert mock_get_device_config.call_args.args == (structured_config,)
    assert mock_get_device_config.call_args.kwargs["configuration"].hide_passwords is True
    assert mock_get_device_doc.call_args.args == (structured_config,)
    assert mock_get_device_doc.call_args.kwargs["add_md_toc"] is False
    assert mock_get_device_doc.call_args.kwargs["configuration"].hide_passwords is False


def test_run_raises_when_pyavd_not_installed(action_module: Callable[..., ActionModule]) -> None:
    """Test that AnsibleActionFail is raised immediately when pyavd is missing."""
    module = action_module(ActionModule)

    with (
        patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
        patch("ansible.plugins.action.ActionBase.run", return_value={}),
        pytest.raises(AnsibleActionFail, match=r"The arista.avd.eos_cli_config_gen' plugin requires the 'pyavd' Python library. Got import error"),
    ):
        module.run(task_vars={"inventory_hostname": "test-device"})
