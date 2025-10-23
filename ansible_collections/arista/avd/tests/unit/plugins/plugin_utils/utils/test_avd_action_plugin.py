# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import warnings
from collections.abc import Generator
from contextlib import ExitStack
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AvdActionPlugin, AvdLoggingConfig
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_handlers import AnsibleDisplayHandler


class TestAvdActionPlugin:
    """Test suite for the AvdActionPlugin base class."""

    @pytest.fixture
    def mock_display(self) -> Generator[MagicMock, Any, None]:
        """
        A fixture that patches the Display singleton in all necessary locations for these unit tests.

        Yields a single shared MagicMock instance that represents the Display() singleton
        to make sure all parts of the code interact with the same mock.
        """
        # This will be the one true mock instance for the singleton
        shared_mock_instance = MagicMock(spec=Display, verbosity=0)

        with ExitStack() as stack:
            # Patch the first location
            log_handlers_patch = stack.enter_context(patch("ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_handlers.Display"))
            # Patch the second location
            log_config_patch = stack.enter_context(patch("ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_config.Display"))

            # Ensure both patched classes return our shared mock instance
            log_handlers_patch.return_value = shared_mock_instance
            log_config_patch.return_value = shared_mock_instance

            yield shared_mock_instance

    def _plugin_factory(self, cls: type[AvdActionPlugin], task_args: dict[str, Any] | None = None) -> AvdActionPlugin:
        """Factory method to instantiate the provided AvdActionPlugin class with mocks for testing."""
        # Create mock objects for the Ansible ActionBase constructor arguments
        mock_task = MagicMock()
        mock_task.args = task_args or {}
        mock_task.async_val = False
        mock_task.check_mode = False

        # Return the instantiated plugin class with a full set of mocks
        instance = cls(task=mock_task, connection=MagicMock(), play_context=MagicMock(), loader=MagicMock(), templar=MagicMock(), shared_loader_obj=MagicMock())

        # Ignoring Pyright since 'ansible_name' is not typed in Ansible world
        instance.ansible_name = "pytest_action_plugin"  # pyright: ignore[reportAttributeAccessIssue]
        return instance

    def test_wrong_logging_config(self) -> None:
        """Test that an exception is raised when _primary_logger_name is not part of the targeted loggers."""

        class ActionModule(AvdActionPlugin):
            _logging_config = AvdLoggingConfig(target_loggers=("pyavd", "anta"))

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars

        match = (
            "The _primary_logger_name 'ansible_collections.arista.avd' must be included in "
            "the _logging_config.target_loggers tuple for the plugin to work correctly."
        )
        with pytest.raises(ValueError, match=match):
            self._plugin_factory(ActionModule)

    def test_run_success(self) -> None:
        """Test a successful run of the plugin."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.result["status"] = "success"

        plugin = self._plugin_factory(cls=ActionModule)

        result = plugin.run()

        assert result["status"] == "success"
        assert "failed" not in result

    def test_run_failure_recast_as_ansible_exception(self) -> None:
        """Test that a generic exception in main() is recast as AnsibleActionFail."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                msg = "Something went wrong"
                raise ValueError(msg)

        plugin = self._plugin_factory(ActionModule)

        with pytest.raises(AnsibleActionFail, match="Error during plugin 'pytest_action_plugin' execution: 'Something went wrong'"):
            plugin.run()

    @pytest.mark.parametrize(
        ("verbosity", "expected_levels"),
        [
            pytest.param(
                0,
                {
                    "ansible_collections.arista.avd": logging.WARNING,
                    "pyavd": logging.WARNING,
                    "anta": logging.WARNING,
                    "httpx": logging.WARNING,
                },
                id="v0-default_warning",
            ),
            pytest.param(
                1,
                {
                    "ansible_collections.arista.avd": logging.INFO,
                    "pyavd": logging.INFO,
                    "anta": logging.WARNING,
                    "httpx": logging.WARNING,
                },
                id="v1-avd_info",
            ),
            pytest.param(
                3,
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.INFO,
                    "httpx": logging.WARNING,
                },
                id="v3-avd_debug_anta_info",
            ),
            pytest.param(
                5,
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.DEBUG,
                    "httpx": logging.INFO,
                },
                id="v5-external_libs_info",
            ),
            pytest.param(
                6,
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.DEBUG,
                    "httpx": logging.DEBUG,
                },
                id="v6-all_debug",
            ),
            pytest.param(
                99,  # Testing fallback for out-of-bounds verbosity
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.DEBUG,
                    "httpx": logging.DEBUG,
                },
                id="v99-fallback_to_max_debug",
            ),
        ],
    )
    def test_log_levels_set_by_verbosity(self, mock_display: MagicMock, verbosity: int, expected_levels: dict[str, int]) -> None:
        """Test that log levels are set correctly based on verbosity for both internal and external libraries."""

        class ActionModule(AvdActionPlugin):
            _logging_config = AvdLoggingConfig(target_loggers=tuple(expected_levels.keys()))

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars

                # Verify that log levels are set correctly inside a plugin run
                for logger_name, expected_level in expected_levels.items():
                    logger = logging.getLogger(logger_name)
                    assert logger.level == expected_level

        plugin = self._plugin_factory(ActionModule)

        # Set the desired verbosity and run the plugin
        mock_display.verbosity = verbosity
        plugin.run()

    @pytest.mark.parametrize(
        ("verbosity", "expected_methods_called"),
        [
            pytest.param(0, ["warning", "error"], id="v0-warn_error_only"),
            pytest.param(1, ["v", "warning", "error"], id="v1-info_enabled"),
            pytest.param(3, ["vvv", "v", "warning", "error"], id="v3-debug_enabled"),
        ],
    )
    def test_default_logging_behavior(self, mock_display: MagicMock, verbosity: int, expected_methods_called: list[str]) -> None:
        """Test the end-to-end default logging behavior (live display on, save logs off)."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.debug("A debug message.")
                self.logger.info("An info message.")
                self.logger.warning("A warning message.")
                self.logger.error("An error message.")

        plugin = self._plugin_factory(ActionModule)

        # Set the desired verbosity and run the plugin
        mock_display.verbosity = verbosity
        result = plugin.run()

        # Verify that the correct display methods were called
        all_display_methods = {
            "vvv": mock_display.vvv,
            "v": mock_display.v,
            "warning": mock_display.warning,
            "error": mock_display.error,
        }

        for method_name, method_mock in all_display_methods.items():
            if method_name in expected_methods_called:
                method_mock.assert_called_once()
            else:
                method_mock.assert_not_called()

        # Verify that logs were not saved
        assert "logs" not in result

    @pytest.mark.parametrize(
        ("add_hostname", "add_role", "task_vars", "expected_format"),
        [
            pytest.param(True, True, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "[my-role] - <host1> {}", id="hostname_and_role"),
            pytest.param(True, False, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "<host1> {}", id="hostname_only"),
            pytest.param(False, True, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "[my-role] - {}", id="role_only"),
            pytest.param(False, False, {"inventory_hostname": "host1", "ansible_role_name": "my-role"}, "{}", id="no_context"),
        ],
    )
    def test_logging_with_context_and_format(
        self,
        mock_display: MagicMock,
        add_hostname: bool,
        add_role: bool,
        task_vars: dict[str, Any],
        expected_format: str,
    ) -> None:
        """Test that context variables are added and the log format is changed based on the logging config."""

        class ActionModule(AvdActionPlugin):
            _logging_config = AvdLoggingConfig(add_hostname_context=add_hostname, add_role_context=add_role)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.warning("A message from the plugin.")

        plugin = self._plugin_factory(ActionModule)

        plugin.run(task_vars=task_vars)

        # Test the display handler received the correctly formatted string
        expected_message = expected_format.format("A message from the plugin.")
        mock_display.warning.assert_called_once_with(expected_message)

    @pytest.mark.usefixtures("mock_display")
    def test_logging_with_save_logs(self) -> None:
        """Test that logs are saved to the result."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.warning("A warning to save.")
                self.logger.error("An error to save.")
                self.logger.info("An info message not to save.")

        # Enable the feature via task args
        plugin = self._plugin_factory(ActionModule, task_args={"save_logs": True})
        result = plugin.run()

        # Assert that the logs were saved to the result dictionary
        assert result["logs"]["warnings"] == ["A warning to save."]
        assert result["logs"]["errors"] == ["An error to save."]

    def test_logging_with_live_display_false(self, mock_display: MagicMock) -> None:
        """Test that logs are never displayed in Ansible."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.info("This should not be displayed live.")

        # Enable the feature via task args
        plugin = self._plugin_factory(ActionModule, task_args={"live_display": False})

        # Set the desired verbosity and run the plugin
        mock_display.verbosity = 1
        plugin.run()

        # Assert the display handler was NOT called
        mock_display.warning.assert_not_called()

    @pytest.mark.parametrize(
        ("warning_type", "message", "expected_key"),
        [
            pytest.param(UserWarning, "This is a standard warning.", "warnings", id="user_warning"),
            pytest.param(DeprecationWarning, "This is a deprecation.", "deprecations", id="deprecation_warning"),
        ],
    )
    def test_warning_capture(self, warning_type: type[Warning], message: str, expected_key: str) -> None:
        """Test that Python warnings are captured and added to the correct list in the result."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                warnings.warn(message, warning_type, stacklevel=1)

        plugin = self._plugin_factory(ActionModule)

        result = plugin.run()

        # Assert that the message is in the correct list (either 'warnings' or 'deprecations')
        if expected_key == "deprecations":
            assert result[expected_key] == [{"msg": message}]
        else:
            assert result[expected_key] == [message]

    def test_handles_dirty_logger_state(self) -> None:
        """Test that the plugin can handle a logger with pre-existing handlers and restore them correctly upon exit."""

        class ActionModule(AvdActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars

                # Assert that the sticky handler is NOT present during execution
                assert sticky_handler not in self.logger.handlers

                # Assert that the plugin default handler is the only one present
                assert len(self.logger.handlers) == 1
                assert isinstance(self.logger.handlers[0], AnsibleDisplayHandler)

        # Create a "sticky" handler and add it to the AVD logger BEFORE the test
        logger = logging.getLogger("ansible_collections.arista.avd")
        sticky_handler = logging.StreamHandler()
        logger.addHandler(sticky_handler)

        plugin = self._plugin_factory(ActionModule)
        plugin.run()

        # Assert that ONLY the sticky handler has been restored after execution
        assert len(logger.handlers) == 1
        assert logger.handlers[0] is sticky_handler

        # Final cleanup for other tests
        logger.removeHandler(sticky_handler)
