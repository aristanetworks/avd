# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.action.eos_cli_config_gen import (
    ActionModule,
    setup_module_logging,
)

MODULE_PATH = "ansible_collections.arista.avd.plugins.action.eos_cli_config_gen"
MOCK_TMP_DIR = "/avd/mocked/tmp"


def get_action_module() -> ActionModule:
    """Create an ActionModule instance bypassing ActionBase.__init__."""
    module = ActionModule.__new__(ActionModule)
    module._task = MagicMock()
    module._connection = MagicMock()
    module._play_context = MagicMock()
    module._loader = MagicMock()
    module._templar = MagicMock()
    module._shared_loader_obj = MagicMock()
    return module


# ===========================
# Tests for setup_module_logging
# ===========================


class TestSetupModuleLogging:
    def test_adds_handler_to_logger(self) -> None:
        """Test that setup_module_logging adds a PythonToAnsibleHandler to the AVD logger."""
        with (
            patch(f"{MODULE_PATH}.PythonToAnsibleContextFilter") as mock_filter_cls,
            patch(f"{MODULE_PATH}.PythonToAnsibleHandler") as mock_handler_cls,
            patch(f"{MODULE_PATH}.LOGGER") as mock_logger,
        ):
            mock_filter_instance = MagicMock()
            mock_handler_instance = MagicMock()
            mock_filter_cls.return_value = mock_filter_instance
            mock_handler_cls.return_value = mock_handler_instance

            setup_module_logging("test-host", {})

            mock_filter_cls.assert_called_once_with("test-host")
            mock_handler_instance.addFilter.assert_called_once_with(mock_filter_instance)
            mock_logger.addHandler.assert_called_once_with(mock_handler_instance)
            mock_logger.setLevel.assert_called_once_with(logging.DEBUG)

    def test_uses_hostname_for_filter(self) -> None:
        """Test that the hostname is passed to PythonToAnsibleContextFilter."""
        with (
            patch(f"{MODULE_PATH}.PythonToAnsibleContextFilter") as mock_filter_cls,
            patch(f"{MODULE_PATH}.PythonToAnsibleHandler"),
            patch(f"{MODULE_PATH}.LOGGER"),
        ):
            setup_module_logging("my-spine-1", {})
            mock_filter_cls.assert_called_once_with("my-spine-1")

    def test_passes_result_and_display_to_handler(self) -> None:
        """Test that result dict and display are passed to PythonToAnsibleHandler."""
        with (
            patch(f"{MODULE_PATH}.PythonToAnsibleContextFilter"),
            patch(f"{MODULE_PATH}.PythonToAnsibleHandler") as mock_handler_cls,
            patch(f"{MODULE_PATH}.LOGGER"),
            patch(f"{MODULE_PATH}.display") as mock_display,
        ):
            result = {"some": "data"}
            setup_module_logging("host", result)
            mock_handler_cls.assert_called_once_with(result, mock_display)


# ===========================
# Tests for error handling
# ===========================


class TestLoadStructuredConfigErrors:
    def test_raises_action_fail_when_file_missing(self) -> None:
        """Test that AnsibleActionFail is raised when the validated config file is absent."""
        module = get_action_module()
        module.tmp_dir = MOCK_TMP_DIR

        mock_file_path = MagicMock()
        mock_file_path.exists.return_value = False
        mock_validated_path = MagicMock()
        mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

        with (
            patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
            patch(f"{MODULE_PATH}.AVDVaultHandler"),
            patch(f"{MODULE_PATH}.AVDFileHandler"),
            pytest.raises(AnsibleActionFail, match="Missing the validated structured config"),
        ):
            module.load_structured_config("missing-device")

    def test_error_message_contains_hostname(self) -> None:
        """Test that the AnsibleActionFail message includes the hostname."""
        module = get_action_module()
        module.tmp_dir = MOCK_TMP_DIR

        mock_file_path = MagicMock()
        mock_file_path.exists.return_value = False
        mock_validated_path = MagicMock()
        mock_validated_path.__truediv__ = MagicMock(return_value=mock_file_path)

        with (
            patch(f"{MODULE_PATH}.get_tmp_paths", return_value=(MagicMock(), mock_validated_path)),
            patch(f"{MODULE_PATH}.AVDVaultHandler"),
            patch(f"{MODULE_PATH}.AVDFileHandler"),
            pytest.raises(AnsibleActionFail, match="my-spine-device"),
        ):
            module.load_structured_config("my-spine-device")


class TestMainErrors:
    def test_exception_calls_raise_action_fail(self) -> None:
        """Test that any exception during execution is forwarded to raise_action_fail."""
        module = get_action_module()
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
            patch(f"{MODULE_PATH}.raise_action_fail") as mock_raise_fail,
        ):
            module.main("test-device", {}, {})

        mock_raise_fail.assert_called_once()
        assert "pyavd exploded" in str(mock_raise_fail.call_args)


class TestRunErrors:
    def test_raises_when_pyavd_not_installed(self) -> None:
        """Test that AnsibleActionFail is raised immediately when pyavd is missing."""
        module = get_action_module()

        with (
            patch(f"{MODULE_PATH}.HAS_PYAVD", new=False),
            patch("ansible.plugins.action.ActionBase.run", return_value={}),
            pytest.raises(AnsibleActionFail, match="pyavd"),
        ):
            module.run(task_vars={"inventory_hostname": "test-device"})
