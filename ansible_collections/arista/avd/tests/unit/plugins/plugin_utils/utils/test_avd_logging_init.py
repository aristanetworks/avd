# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from unittest.mock import MagicMock

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.utils.avd_logging import (
    AVD_GLOBAL_DISPLAY_HANDLER_NAME,
    EXTERNAL_LIB_LOGGERS,
    INTERNAL_LIB_LOGGERS,
    AnsibleDisplayHandler,
    init_avd_logging,
)

MANAGED_LOGGERS = INTERNAL_LIB_LOGGERS + EXTERNAL_LIB_LOGGERS
"""Combined list of all loggers managed by the `init_avd_logging` function."""


def test_init_avd_logging_handler_setup(mock_display: MagicMock) -> None:
    """Test that init_avd_logging adds the correct handler to all loggers."""
    mock_display.verbosity = 1
    init_avd_logging(display=mock_display)

    for logger_name in MANAGED_LOGGERS:
        logger = logging.getLogger(logger_name)
        assert len(logger.handlers) == 1
        handler = logger.handlers[0]
        assert isinstance(handler, AnsibleDisplayHandler)
        assert handler.name == AVD_GLOBAL_DISPLAY_HANDLER_NAME


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
def test_init_avd_logging_levels(mock_display: MagicMock, verbosity: int, expected_levels: dict[str, int]) -> None:
    """Test that log levels are set correctly based on verbosity for both internal and external libraries."""
    mock_display.verbosity = verbosity
    init_avd_logging(display=mock_display)

    for logger_name, expected_level in expected_levels.items():
        logger = logging.getLogger(logger_name)
        assert logger.level == expected_level


@pytest.mark.parametrize(
    ("verbosity", "expected_methods_called"),
    [
        pytest.param(0, ["warning", "error"], id="v0-warn_error_only"),
        pytest.param(1, ["v", "warning", "error"], id="v1-info_enabled"),
        pytest.param(3, ["vvv", "v", "warning", "error"], id="v3-debug_enabled"),
    ],
)
def test_baseline_logging_output_with_verbosity(mock_display: MagicMock, verbosity: int, expected_methods_called: list[str]) -> None:
    """Test the end-to-end default logging behavior for an undecorated plugin."""
    # Setup the logging environment with the specified verbosity
    mock_display.verbosity = verbosity
    init_avd_logging(display=mock_display)

    # Simulate a plugin emitting logs at various levels
    logger = logging.getLogger("ansible_collections.arista.avd.some_plugin")
    logger.debug("A debug message.")
    logger.info("An info message.")
    logger.warning("A warning message.")
    logger.error("An error message.")

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
