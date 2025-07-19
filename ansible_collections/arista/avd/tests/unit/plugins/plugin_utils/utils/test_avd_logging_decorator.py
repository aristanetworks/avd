# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import warnings
from typing import TYPE_CHECKING, Any

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.utils import avd_logging
from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_logging.handlers import AnsibleDisplayHandler

if TYPE_CHECKING:
    from unittest.mock import MagicMock


LOGGER = logging.getLogger("ansible_collections.arista.avd")


def test_decorator_raises_on_invalid_function_name() -> None:
    """Test that the @avd_logging decorator raises a TypeError if used on a function not named 'run_plugin'."""
    with pytest.raises(TypeError) as exc_info:

        @avd_logging()
        def some_other_function(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
            """A function with a name that is not 'run_plugin'."""
            _unused = self, task_vars
            return {}

    # Verify that the exception message is exactly as expected
    expected_msg = "The '@avd_logging' decorator can only be used on the 'run_plugin' method."
    assert str(exc_info.value) == expected_msg


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
def test_decorator_logger_levels(mocked_plugin_object: MagicMock, mock_display: MagicMock, verbosity: int, expected_levels: dict[str, int]) -> None:
    """Test that log levels are set correctly based on verbosity for both internal and external libraries."""
    mock_display.verbosity = verbosity
    target_loggers = list(expected_levels)

    @avd_logging(target_loggers=target_loggers, display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars

        # Verify that log levels are set correctly inside a plugin run
        for logger_name, expected_level in expected_levels.items():
            logger = logging.getLogger(logger_name)
            assert logger.level == expected_level

        return self.result

    run_plugin(mocked_plugin_object, task_vars={})

    # Verify that log levels are reset (NOTSET) after the run
    for logger_name in target_loggers:
        logger = logging.getLogger(logger_name)
        assert logger.level == logging.NOTSET


@pytest.mark.parametrize(
    ("verbosity", "expected_methods_called"),
    [
        pytest.param(0, ["warning", "error"], id="v0-warn_error_only"),
        pytest.param(1, ["v", "warning", "error"], id="v1-info_enabled"),
        pytest.param(3, ["vvv", "v", "warning", "error"], id="v3-debug_enabled"),
    ],
)
def test_decorator_logging(mocked_plugin_object: MagicMock, mock_display: MagicMock, verbosity: int, expected_methods_called: list[str]) -> None:
    """Test the end-to-end default logging behavior for a decorated plugin."""
    mock_display.verbosity = verbosity

    @avd_logging(display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        LOGGER.debug("A debug message.")
        LOGGER.info("An info message.")
        LOGGER.warning("A warning message.")
        LOGGER.error("An error message.")
        return self.result

    run_plugin(mocked_plugin_object, task_vars={})

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

    # Verify that the AnsibleDisplayHandler has been removed
    assert len(LOGGER.handlers) == 0


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
    mocked_plugin_object: MagicMock,
    mock_display: MagicMock,
    add_hostname: bool,
    add_role: bool,
    task_vars: dict[str, Any],
    expected_format: str,
) -> None:
    """Tests that context variables are added and the log format is changed based on decorator arguments."""

    # Dynamically create the decorated function with parametrized arguments
    @avd_logging(add_hostname_context=add_hostname, add_role_context=add_role, display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        LOGGER.warning("A message from the plugin.")
        return self.result

    run_plugin(mocked_plugin_object, task_vars=task_vars)

    # Test the display handler received the correctly formatted string
    expected_message = expected_format.format("A message from the plugin.")
    mock_display.warning.assert_called_once_with(expected_message)

    # Verify that all handlers have been removed after execution
    assert len(LOGGER.handlers) == 0


def test_decorator_save_logs(mocked_plugin_object: MagicMock, mock_display: MagicMock) -> None:
    """Tests the `save_logs: true` functionality."""

    @avd_logging(display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        LOGGER.warning("A warning to save.")
        LOGGER.error("An error to save.")
        LOGGER.info("An info message not to save.")
        return self.result

    # Enable the feature via task args
    mocked_plugin_object._task.args["save_logs"] = True
    result = run_plugin(mocked_plugin_object, task_vars={})

    # Assert that the logs were saved to the result dictionary
    assert result["logs"]["warnings"] == ["A warning to save."]
    assert result["logs"]["errors"] == ["An error to save."]

    # Verify that all handlers have been removed after execution
    assert len(LOGGER.handlers) == 0


def test_decorator_live_display_false(mocked_plugin_object: MagicMock, mock_display: MagicMock) -> None:
    """Tests the `live_display: false` functionality."""
    mock_display.verbosity = 1

    @avd_logging(display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        LOGGER.info("This should not be displayed live.")
        return self.result

    mocked_plugin_object._task.args["live_display"] = False
    run_plugin(mocked_plugin_object, task_vars={})

    # Assert the display handler was NOT called
    mock_display.warning.assert_not_called()


@pytest.mark.parametrize(
    ("warning_type", "message", "expected_key"),
    [
        pytest.param(UserWarning, "This is a standard warning.", "warnings", id="user_warning"),
        pytest.param(DeprecationWarning, "This is a deprecation.", "deprecations", id="deprecation_warning"),
    ],
)
def test_decorator_warning_capture(mocked_plugin_object: MagicMock, warning_type: type[Warning], message: str, expected_key: str) -> None:
    """Tests that Python warnings are captured and added to the correct list in the result."""

    @avd_logging()
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        warnings.warn(message, warning_type, stacklevel=1)
        return self.result

    result = run_plugin(mocked_plugin_object, task_vars={})

    # Assert that the message is in the correct list (either 'warnings' or 'deprecations')
    if expected_key == "deprecations":
        assert result[expected_key] == [{"msg": message}]
    else:
        assert result[expected_key] == [message]


def test_decorator_handles_dirty_logger_state(mocked_plugin_object: MagicMock, mock_display: MagicMock) -> None:
    """Tests that the decorator can handle a logger with pre-existing handlers and restores them correctly upon exit."""
    # Create a "sticky" handler and add it to the logger BEFORE the test
    sticky_handler = logging.StreamHandler()
    LOGGER.addHandler(sticky_handler)

    @avd_logging(display=mock_display)
    def run_plugin(self: MagicMock, task_vars: dict[str, Any]) -> dict[str, Any]:
        _unused = task_vars
        # Assert that the sticky handler is NOT present during execution
        assert sticky_handler not in LOGGER.handlers

        # Assert that the decorator's default handler is the only one present
        assert len(LOGGER.handlers) == 1
        assert isinstance(LOGGER.handlers[0], AnsibleDisplayHandler)
        return self.result

    run_plugin(mocked_plugin_object, task_vars={})

    # Assert that ONLY the sticky handler has been restored after execution
    assert len(LOGGER.handlers) == 1
    assert LOGGER.handlers[0] is sticky_handler

    # Final cleanup for other tests
    LOGGER.removeHandler(sticky_handler)
