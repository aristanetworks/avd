# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import warnings
from typing import TYPE_CHECKING, Any

import pytest
from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_logging import (
    AVD_GLOBAL_DISPLAY_HANDLER_NAME,
    SaveToResultHandler,
    avd_logging,
    init_avd_logging,
)

if TYPE_CHECKING:
    from unittest.mock import MagicMock

# The logger we will use inside our test plugin
logger = logging.getLogger("ansible_collections.arista.avd.test_plugin")


class TestAvdLoggingDecorator:
    """A test class for the @avd_logging decorator."""

    @pytest.fixture(autouse=True)
    def setup(self, mock_display: MagicMock, mock_action_plugin: MagicMock) -> None:
        """
        Set up a consistent baseline for every test in this class.

        This runs automatically before each test method in this class.
        """
        # Establish the global logging state with verbosity 1 (INFO)
        mock_display.verbosity = 1
        init_avd_logging(display=mock_display)

        self.mock_display = mock_display
        self.plugin = mock_action_plugin

        # Get the global handler to check its existence later
        self.global_handler = logging.getLogger("ansible_collections.arista.avd").handlers[0]
        assert self.global_handler.name == AVD_GLOBAL_DISPLAY_HANDLER_NAME

    @pytest.mark.parametrize(
        ("add_hostname", "add_role", "task_vars", "expected_format"),
        [
            pytest.param(True, True, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "[my-role] - <host1> {}", id="hostname_and_role"),
            pytest.param(True, False, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "<host1> {}", id="hostname_only"),
            pytest.param(False, True, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "[my-role] - {}", id="role_only"),
            pytest.param(False, False, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "{}", id="no_context"),
        ],
    )
    def test_decorator_with_context_and_format(
        self,
        caplog: pytest.LogCaptureFixture,
        add_hostname: bool,
        add_role: bool,
        task_vars: dict[str, Any],
        expected_format: str,
    ) -> None:
        """Tests that context variables are added and the log format is changed based on decorator arguments."""

        # Dynamically create the decorated function with parametrized arguments
        @avd_logging(add_hostname_context=add_hostname, add_role_context=add_role)
        def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            _unused = task_vars
            logger.warning("A message from the plugin.")
            return self.result

        run_plugin(self.plugin, task_vars=task_vars)

        # Test the context filter injected data into the record (if applicable)
        if add_hostname:
            assert caplog.records[0].hostname == "host1"
        if add_role:
            assert caplog.records[0].role_name == "my-role"

        # Test the display handler received the correctly formatted string
        expected_message = expected_format.format("A message from the plugin.")
        self.mock_display.warning.assert_called_once_with(expected_message)

    def test_decorator_save_logs(self) -> None:
        """Tests the `save_logs: true` functionality."""

        @avd_logging()
        def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            _unused = task_vars
            logger.warning("A warning to save.")
            logger.error("An error to save.")
            logger.info("An info message not to save.")
            return self.result

        # Enable the feature via task args
        self.plugin._task.args["save_logs"] = True
        result = run_plugin(self.plugin, task_vars={})

        # Assert that the logs were saved to the result dictionary
        assert result["logs"]["warnings"] == ["A warning to save."]
        assert result["logs"]["errors"] == ["An error to save."]

        # Assert that the temporary SaveToResultHandler was removed after execution
        assert not any(isinstance(h, SaveToResultHandler) for h in logger.handlers)

    def test_decorator_live_display_false(self) -> None:
        """Tests that `live_display: false` removes the global handler during execution and restores it afterward."""
        # Define the parent logger that the decorator actually targets by default
        parent_logger = logging.getLogger("ansible_collections.arista.avd")

        @avd_logging()
        def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            _unused = task_vars
            # This logger is the one emitting the message
            child_logger = logging.getLogger("ansible_collections.arista.avd.test_plugin")

            # This log should NOT go to the display handler because the handler on the parent_logger has been removed
            child_logger.warning("This should not be displayed live.")

            # Check *during* execution that the handler is gone from the PARENT logger
            assert self.global_handler not in parent_logger.handlers
            return self.result

        self.plugin._task.args["live_display"] = False
        run_plugin(self.plugin, task_vars={})

        # Assert the display handler was NOT called
        self.mock_display.warning.assert_not_called()

        # Assert the handler was RESTORED after execution to the PARENT logger
        assert self.global_handler in parent_logger.handlers

    def test_decorator_exception_handling(self) -> None:
        """Tests that any exception is caught and re-raised as AnsibleActionFail."""

        @avd_logging()
        def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            _unused = self, task_vars
            msg = "Something went wrong inside"
            raise ValueError(msg)

        with pytest.raises(AnsibleActionFail, match="Error during plugin execution: Something went wrong inside"):
            run_plugin(self.plugin, task_vars={})

    @pytest.mark.parametrize(
        ("warning_type", "message", "expected_key"),
        [
            pytest.param(UserWarning, "This is a standard warning.", "warnings", id="user_warning"),
            pytest.param(DeprecationWarning, "This is a deprecation.", "deprecations", id="deprecation_warning"),
        ],
    )
    def test_decorator_warning_capture(self, warning_type: type[Warning], message: str, expected_key: str) -> None:
        """Tests that Python warnings are captured and added to the correct list in the result."""

        @avd_logging()
        def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            _unused = task_vars
            warnings.warn(message, warning_type, stacklevel=1)
            return self.result

        result = run_plugin(self.plugin, task_vars={})

        # Assert that the message is in the correct list (either 'warnings' or 'deprecations')
        if expected_key == "deprecations":
            assert result[expected_key] == [{"msg": message}]
        else:
            assert result[expected_key] == [message]
