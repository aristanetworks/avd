# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import warnings
from collections.abc import Callable, Generator
from concurrent.futures import ProcessPoolExecutor
from contextlib import ExitStack
from logging.handlers import QueueHandler
from multiprocessing import get_context
from threading import Thread
from typing import Any
from unittest.mock import MagicMock, patch

import pytest
from ansible.errors import AnsibleActionFail
from ansible.utils.display import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin import AVDActionPlugin, AVDLoggingConfig
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.log_handlers import AnsibleDisplayHandler, LoggingOutcome, log_context
from pyavd._errors import AvdDeprecationWarning


def _emit_logs_from_worker(logger_name: str, worker_log_context: str | None = None) -> None:
    """Emit records from a forked worker for queue logging tests."""
    with log_context(worker_log_context):
        logger = logging.getLogger(logger_name)
        logger.warning("A warning from a worker.")
        logger.error("An error from a worker.")


def _emit_log_and_raise_from_worker(logger_name: str) -> None:
    """Emit a record and raise from a forked worker for queue cleanup tests."""
    logging.getLogger(logger_name).warning("A warning before a worker exception.")
    msg = "Worker failed"
    raise RuntimeError(msg)


def _emit_log_from_thread_in_worker(logger_name: str, worker_log_context: str) -> None:
    """Emit a record from a new thread in a forked worker."""
    with log_context(worker_log_context):
        thread = Thread(target=logging.getLogger(logger_name).warning, args=("A warning from a worker thread.",))
        thread.start()
        thread.join()


class TestAVDActionPlugin:
    """Test suite for the AVDActionPlugin base class."""

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

    def test_wrong_logging_config(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Test that an exception is raised when _primary_logger_name is not part of the targeted loggers."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(target_loggers=("pyavd", "anta"))

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars

        match = (
            "The _primary_logger_name 'ansible_collections.arista.avd' must be included in "
            "the _logging_config.target_loggers tuple for the plugin to work correctly."
        )
        with pytest.raises(ValueError, match=match):
            action_module(ActionModule)

    def test_run_success(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Test a successful run of the plugin."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.result["status"] = "success"

        plugin = action_module(ActionModule)

        result = plugin.run()

        assert result["status"] == "success"
        assert "failed" not in result

    def test_run_failure_recast_as_ansible_exception(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Test that a generic exception in main() is recast as AnsibleActionFail."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                msg = "Something went wrong"
                raise ValueError(msg)

        plugin = action_module(ActionModule, ansible_name="pytest_action_plugin")

        with pytest.raises(AnsibleActionFail, match="Error during plugin 'pytest_action_plugin' execution: Something went wrong"):
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
                    "asynceapi": logging.WARNING,
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
                    "asynceapi": logging.WARNING,
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
                    "asynceapi": logging.INFO,
                    "httpx": logging.WARNING,
                },
                id="v3-avd_debug_anta_info",
            ),
            pytest.param(
                4,
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.DEBUG,
                    "asynceapi": logging.DEBUG,
                    "httpx": logging.WARNING,
                },
                id="v4-asynceapi_debug",
            ),
            pytest.param(
                5,
                {
                    "ansible_collections.arista.avd": logging.DEBUG,
                    "pyavd": logging.DEBUG,
                    "anta": logging.DEBUG,
                    "asynceapi": logging.DEBUG,
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
                    "asynceapi": logging.DEBUG,
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
                    "asynceapi": logging.DEBUG,
                    "httpx": logging.DEBUG,
                },
                id="v99-fallback_to_max_debug",
            ),
        ],
    )
    def test_log_levels_set_by_verbosity(
        self, action_module: Callable[..., AVDActionPlugin], mock_display: MagicMock, verbosity: int, expected_levels: dict[str, int]
    ) -> None:
        """Test that log levels are set correctly based on verbosity for both internal and external libraries."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(target_loggers=tuple(expected_levels.keys()))

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars

                # Verify that log levels are set correctly inside a plugin run
                for logger_name, expected_level in expected_levels.items():
                    logger = logging.getLogger(logger_name)
                    assert logger.level == expected_level

        plugin = action_module(ActionModule)

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
    def test_default_logging_behavior(
        self, action_module: Callable[..., AVDActionPlugin], mock_display: MagicMock, verbosity: int, expected_methods_called: list[str]
    ) -> None:
        """Test the end-to-end default logging behavior (live display on, save logs off)."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.debug("A debug message.")
                self.logger.info("An info message.")
                self.logger.warning("A warning message.")
                self.logger.error("An error message.")

        plugin = action_module(ActionModule)

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
        action_module: Callable[..., AVDActionPlugin],
        mock_display: MagicMock,
        add_hostname: bool,
        add_role: bool,
        task_vars: dict[str, Any],
        expected_format: str,
    ) -> None:
        """Test that context variables are added and the log format is changed based on the logging config."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(add_hostname_context=add_hostname, add_role_context=add_role)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.warning("A message from the plugin.")

        plugin = action_module(ActionModule)

        plugin.run(task_vars=task_vars)

        # Test the display handler received the correctly formatted string
        expected_message = expected_format.format("A message from the plugin.")
        mock_display.warning.assert_called_once_with(expected_message)

    @pytest.mark.usefixtures("mock_display")
    def test_logging_with_save_logs(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Test that logs are saved to the result."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.warning("A warning to save.")
                self.logger.error("An error to save.")
                self.logger.info("An info message not to save.")

        # Enable the feature via task args
        plugin = action_module(ActionModule, task_args={"save_logs": True})
        result = plugin.run()

        # Assert that the logs were saved to the result dictionary
        assert result["logs"]["warnings"] == ["A warning to save."]
        assert result["logs"]["errors"] == ["An error to save."]

    def test_logging_with_live_display_false(self, action_module: Callable[..., AVDActionPlugin], mock_display: MagicMock) -> None:
        """Test that logs are never displayed in Ansible."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.info("This should not be displayed live.")

        # Enable the feature via task args
        plugin = action_module(ActionModule, task_args={"live_display": False})

        # Set the desired verbosity and run the plugin
        mock_display.verbosity = 1
        plugin.run()

        # Assert the display handler was NOT called
        mock_display.warning.assert_not_called()

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_logs_are_saved_without_failing_action(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Unlisted records caught by a root fallback are drained without directly controlling task failure."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(
                target_loggers=("", "ansible_collections.arista.avd"),
                track_log_errors=True,
                use_multiprocessing_queue=True,
            )

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_logs_from_worker, "custom_anta_test.ExampleTest").result()

            def _handle_logging_outcome(self, logging_outcome: LoggingOutcome) -> None:
                self.result["has_log_errors"] = logging_outcome.has_errors

        plugin = action_module(ActionModule, task_args={"save_logs": True, "live_display": False})
        result = plugin.run()

        assert result["logs"] == {
            "warnings": ["A warning from a worker."],
            "errors": ["An error from a worker."],
        }
        assert result["has_log_errors"] is True
        assert "failed" not in result

    def test_multiprocessing_logs_are_displayed_once(self, action_module: Callable[..., AVDActionPlugin], mock_display: MagicMock) -> None:
        """A forked worker record is displayed exactly once by the parent listener."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_logs_from_worker, self._primary_logger_name).result()

        plugin = action_module(ActionModule)
        plugin.run()

        mock_display.warning.assert_called_once_with("A warning from a worker.")
        mock_display.error.assert_called_once_with("An error from a worker.", wrap_text=False)

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_logs_are_drained_when_worker_raises(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Queued records are drained before a worker exception is recast as AnsibleActionFail."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_log_and_raise_from_worker, self._primary_logger_name).result()

        plugin = action_module(ActionModule, task_args={"save_logs": True, "live_display": False}, ansible_name="pytest_action_plugin")

        with pytest.raises(AnsibleActionFail, match="Error during plugin 'pytest_action_plugin' execution: Worker failed"):
            plugin.run()

        assert plugin.result["logs"]["warnings"] == ["A warning before a worker exception."]

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_context_is_applied_in_parent_listener(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Role and hostname context is formatted by the parent-side sink handler."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(
                add_hostname_context=True,
                add_role_context=True,
                log_context="anta-workflow",
                use_multiprocessing_queue=True,
            )

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_logs_from_worker, self._primary_logger_name, "anta-run-12345678").result()

        plugin = action_module(ActionModule, task_args={"save_logs": True, "live_display": False})
        result = plugin.run(task_vars={"inventory_hostname": "leaf1", "ansible_role_name": "anta_runner"})

        assert result["logs"]["warnings"] == ["[anta_runner] - <leaf1> [anta-run-12345678] A warning from a worker."]
        assert result["logs"]["errors"] == ["[anta_runner] - <leaf1> [anta-run-12345678] An error from a worker."]

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_context_is_available_to_worker_threads(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """A raw worker thread uses the process context when no task-local context is available."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(log_context="anta-workflow", use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_log_from_thread_in_worker, self._primary_logger_name, "anta-run-12345678").result()

        plugin = action_module(ActionModule, task_args={"save_logs": True, "live_display": False})
        result = plugin.run()

        assert result["logs"]["warnings"] == ["[anta-run-12345678] A warning from a worker thread."]

    def test_multiprocessing_queue_tracks_errors_without_output_sinks(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Queue mode is only activated without output sinks when error tracking is requested."""

        class UntrackedActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.error("Dropped because no sinks are enabled.")

        untracked_plugin = action_module(UntrackedActionModule, task_args={"save_logs": False, "live_display": False})
        with patch("ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_action_plugin.avd_action_plugin.get_context") as mock_get_context:
            untracked_result = untracked_plugin.run()

        mock_get_context.assert_not_called()
        assert "failed" not in untracked_result
        assert "logs" not in untracked_result

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(track_log_errors=True, use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                self.logger.error("Dropped because no sinks are enabled.")

            def _handle_logging_outcome(self, logging_outcome: LoggingOutcome) -> None:
                self.result["has_log_errors"] = logging_outcome.has_errors

        plugin = action_module(ActionModule, task_args={"save_logs": False, "live_display": False})
        result = plugin.run()

        assert result["has_log_errors"] is True
        assert "failed" not in result
        assert "logs" not in result

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_descendant_records_are_not_duplicated(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Overlapping configured logger roots still handle descendant records once."""
        child_logger_name = "ansible_collections.arista.avd.worker"

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(
                target_loggers=("ansible_collections.arista.avd", child_logger_name),
                use_multiprocessing_queue=True,
            )

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                with ProcessPoolExecutor(max_workers=1, mp_context=get_context("fork")) as executor:
                    executor.submit(_emit_logs_from_worker, f"{child_logger_name}.descendant").result()

        plugin = action_module(ActionModule, task_args={"save_logs": True, "live_display": False})
        result = plugin.run()

        assert result["logs"]["warnings"] == ["A warning from a worker."]
        assert result["logs"]["errors"] == ["An error from a worker."]

    @pytest.mark.usefixtures("mock_display")
    def test_multiprocessing_context_restores_dirty_logger_state(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Queue mode restores handlers, level, and propagation after execution."""

        class ActionModule(AVDActionPlugin):
            _logging_config = AVDLoggingConfig(use_multiprocessing_queue=True)

            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                assert len(self.logger.handlers) == 1
                assert isinstance(self.logger.handlers[0], QueueHandler)

        logger = logging.getLogger("ansible_collections.arista.avd")
        sticky_handler = logging.StreamHandler()
        original_handlers = logger.handlers[:]
        original_level = logger.level
        original_propagate = logger.propagate

        try:
            logger.addHandler(sticky_handler)
            expected_handlers = [*original_handlers, sticky_handler]
            plugin = action_module(ActionModule)
            plugin.run()

            assert logger.handlers == expected_handlers
            assert logger.level == original_level
            assert logger.propagate == original_propagate
        finally:
            logger.removeHandler(sticky_handler)
            sticky_handler.close()

    @pytest.mark.parametrize(
        ("warning", "expected_result"),
        [
            pytest.param(
                UserWarning("This is a standard warning."),
                {"warnings": ["This is a standard warning."], "deprecations": []},
                id="user_warning",
            ),
            pytest.param(
                DeprecationWarning("This is a deprecation."),
                {"warnings": [], "deprecations": [{"msg": "This is a deprecation."}]},
                id="deprecation_warning",
            ),
            pytest.param(
                AvdDeprecationWarning(["old_key"], remove_in_version="7.0.0"),
                {
                    "warnings": [],
                    "deprecations": [
                        {
                            "msg": "The input data model 'old_key' is deprecated.",
                            "version": "7.0.0",
                            "collection_name": "arista.avd",
                        }
                    ],
                },
                id="deprecation_warning_with_version",
            ),
            pytest.param(
                AvdDeprecationWarning(["old_key"], remove_after_date="2027-01-01"),
                {
                    "warnings": [],
                    "deprecations": [
                        {
                            "msg": "The input data model 'old_key' is deprecated.",
                            "date": "2027-01-01",
                            "collection_name": "arista.avd",
                        }
                    ],
                },
                id="deprecation_warning_with_date",
            ),
        ],
    )
    def test_warning_capture(
        self, action_module: Callable[..., AVDActionPlugin], warning: Warning, expected_result: dict[str, list[str | dict[str, str]]]
    ) -> None:
        """Test that Python warnings are captured and added to the correct list in the result."""

        class ActionModule(AVDActionPlugin):
            def main(self, task_vars: dict[str, Any]) -> None:
                _task_vars = task_vars
                warnings.warn(warning, stacklevel=1)

        plugin = action_module(ActionModule)

        result = plugin.run()

        assert result["warnings"] == expected_result["warnings"]
        assert result["deprecations"] == expected_result["deprecations"]

    def test_handles_dirty_logger_state(self, action_module: Callable[..., AVDActionPlugin]) -> None:
        """Test that the plugin can handle a logger with pre-existing handlers and restore them correctly upon exit."""

        class ActionModule(AVDActionPlugin):
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
        original_handlers = logger.handlers[:]
        original_level = logger.level
        original_propagate = logger.propagate

        try:
            logger.addHandler(sticky_handler)
            # pytest 9.1.0 can attach multiple capture/live-log handlers to non-propagating loggers.
            # The plugin should restore all existing handlers, including pytest-owned handlers.
            expected_handlers = [*original_handlers, sticky_handler]

            plugin = action_module(ActionModule)
            plugin.run()

            assert logger.handlers == expected_handlers
            assert logger.level == original_level
            assert logger.propagate == original_propagate
        finally:
            logger.removeHandler(sticky_handler)
            sticky_handler.close()
