# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for the anta_workflow_logging module."""

import logging
from unittest.mock import MagicMock

import pytest
from ansible.cli import Display

from ansible_collections.arista.avd.plugins.plugin_utils.utils import AntaWorkflowFilter, AntaWorkflowHandler


def create_log_record(name: str, level: int, msg: str, unique_id: str | None = None, args: tuple = ()) -> logging.LogRecord:
    """Helper function to create a LogRecord, optionally adding unique_id."""
    record = logging.LogRecord(
        name=name,
        level=level,
        pathname="dummy_path",
        lineno=123,
        msg=msg,
        args=args,
        exc_info=None,
        func="dummy_func",
    )
    # Simulate the filter adding the unique_id *before* it reaches the handler
    if unique_id:
        record.unique_id = unique_id
    return record


class TestAntaWorkflowFilter:
    """Test suite for the AntaWorkflowFilter class."""

    def test_anta_workflow_filter_init(self) -> None:
        """Test AntaWorkflowFilter initialization."""
        test_id = "test-filter-id-123"
        custom_filter = AntaWorkflowFilter(unique_id=test_id)
        assert custom_filter.unique_id == test_id

    def test_anta_workflow_filter_adds_unique_id(self) -> None:
        """Test AntaWorkflowFilter adds unique_id to the record."""
        test_id = "filter-id-for-record"
        custom_filter = AntaWorkflowFilter(unique_id=test_id)
        record = create_log_record("test.logger", logging.INFO, "A test message")

        # Ensure unique_id is not present before filtering
        assert not hasattr(record, "unique_id")

        result = custom_filter.filter(record)

        assert result is True
        assert hasattr(record, "unique_id")
        assert record.unique_id == test_id


class TestAntaWorkflowHandler:
    """Test suite for the AntaWorkflowHandler class."""

    def test_anta_workflow_handler_init(self) -> None:
        """Test AntaWorkflowHandler initialization."""
        errors_list = [False]
        handler = AntaWorkflowHandler(has_errors_ref=errors_list)
        assert handler.display is not None
        assert isinstance(handler.display, Display)
        assert handler.has_errors_ref == errors_list

    @pytest.mark.parametrize(
        ("level", "msg", "expected_display_method_name", "set_error_true"),
        [
            pytest.param(logging.DEBUG, "Debug message", "vvv", False, id="debug_level"),
            pytest.param(logging.INFO, "Info message", "v", False, id="info_level"),
            pytest.param(logging.WARNING, "Warning message", "warning", False, id="warning_level"),
            pytest.param(logging.ERROR, "Error message", "error", True, id="error_level"),
            pytest.param(logging.CRITICAL, "Critical message", "error", True, id="critical_level"),
        ],
    )
    def test_anta_workflow_handler_emit_levels(
        self, mock_display: MagicMock, level: int, msg: str, expected_display_method_name: str, set_error_true: bool
    ) -> None:
        """Test AntaWorkflowHandler emit calls the correct display method and updates errors."""
        unique_context_id = "ctx-123"
        errors_list = [False]
        handler = AntaWorkflowHandler(has_errors_ref=errors_list)
        handler.display = mock_display
        # Set a basic formatter to ensure record.getMessage() works as expected
        handler.setFormatter(logging.Formatter("%(message)s"))

        record = create_log_record("test.emit", level, msg, unique_id=unique_context_id)
        handler.emit(record)

        expected_message = f"[{unique_context_id}] {msg}"

        # Get the mock method from the display mock
        display_method_mock = getattr(mock_display, expected_display_method_name)

        if expected_display_method_name == "error":
            display_method_mock.assert_called_once_with(expected_message, wrap_text=False)
        else:
            display_method_mock.assert_called_once_with(expected_message)

        # Verify other display methods were NOT called
        all_display_methods = {"v", "vvv", "warning", "error"}
        for method_name in all_display_methods:
            if method_name != expected_display_method_name:
                method_to_check = getattr(mock_display, method_name)
                method_to_check.assert_not_called()

        assert errors_list[0] is set_error_true

    def test_anta_workflow_handler_emit_unknown_unique_id(self, mock_display: MagicMock) -> None:
        """Test AntaWorkflowHandler emit with a record that has no unique_id attribute."""
        errors_list = [False]
        handler = AntaWorkflowHandler(has_errors_ref=errors_list)
        handler.display = mock_display
        handler.setFormatter(logging.Formatter("%(message)s"))

        log_message = "Info message without explicit unique_id"
        # Create a record without unique_id (it won't be added by the helper in this case)
        record = logging.LogRecord(
            name="test.unknown_id",
            level=logging.INFO,
            pathname="dummy_path",
            lineno=123,
            msg=log_message,
            args=(),
            exc_info=None,
            func="dummy_func",
        )
        # Sanity check: ensure unique_id is not on the record
        assert not hasattr(record, "unique_id")

        handler.emit(record)

        expected_message = f"[unknown] {log_message}"
        mock_display.v.assert_called_once_with(expected_message)
        assert errors_list[0] is False

    def test_anta_workflow_handler_emit_message_formatting_with_args(self, mock_display: MagicMock) -> None:
        """Test that emit correctly formats messages with arguments."""
        unique_context_id = "ctx-format"
        errors_list = [False]
        handler = AntaWorkflowHandler(has_errors_ref=errors_list)
        handler.display = mock_display
        # Using a formatter that includes the message part
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)

        msg_template = "User %s logged in from %s"
        msg_args = ("testuser", "192.168.1.100")
        # The LogRecord will store the template and args separately
        # record.getMessage() or handler.format(record) will combine them
        record = create_log_record("test.format", logging.INFO, msg_template, unique_id=unique_context_id, args=msg_args)

        handler.emit(record)

        # The formatter will produce "User testuser logged in from 192.168.1.100"
        formatted_base_message = msg_template % msg_args
        expected_final_message = f"[{unique_context_id}] {formatted_base_message}"

        mock_display.v.assert_called_once_with(expected_final_message)
        assert not errors_list[0]
