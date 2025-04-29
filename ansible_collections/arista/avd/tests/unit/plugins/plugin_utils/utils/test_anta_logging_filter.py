# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for the anta_logging_filter module."""

import logging
from collections import defaultdict
from unittest.mock import Mock

import pytest

from ansible_collections.arista.avd.plugins.plugin_utils.utils import AntaWorkflowFilter, AntaWorkflowHandler
from ansible_collections.arista.avd.plugins.plugin_utils.utils.anta_workflow_logging import ANTA_LIBRARIES

from .conftest import create_log_record


class TestAntaWorkflowFilter:
    """Tests for the AntaWorkflowFilter class."""

    def test_injects_unique_id(
        self,
        anta_workflow_filter: AntaWorkflowFilter,
        unique_id: str,
    ) -> None:
        """Test that unique_id is injected into both ANTA and non-ANTA records."""
        record_anta = create_log_record(name="anta.runner", level=logging.INFO, msg="ANTA message")
        record_non_anta = create_log_record(name="pyavd", level=logging.INFO, msg="Non-ANTA message")

        anta_workflow_filter.filter(record_anta)
        anta_workflow_filter.filter(record_non_anta)

        assert getattr(record_anta, "unique_id", None) == unique_id
        assert getattr(record_non_anta, "unique_id", None) == unique_id

    def test_filters_anta_below_warning(
        self,
        anta_workflow_filter: AntaWorkflowFilter,
    ) -> None:
        """Test ANTA records below WARNING are filtered out (return False)."""
        info_anta_record = create_log_record(name="anta.runner", level=logging.INFO, msg="anta info")
        debug_anta_record = create_log_record(name="anta.models", level=logging.DEBUG, msg="anta debug")

        assert anta_workflow_filter.filter(info_anta_record) is False
        assert anta_workflow_filter.filter(debug_anta_record) is False

    def test_allows_non_anta(
        self,
        anta_workflow_filter: AntaWorkflowFilter,
    ) -> None:
        """Test non-ANTA records are allowed regardless of level (return True)."""
        info_non_anta_record = create_log_record(name="pyavd", level=logging.INFO, msg="non-anta info")
        debug_non_anta = create_log_record(name="otherlib", level=logging.DEBUG, msg="other debug")
        warn_non_anta = create_log_record(name="another.lib", level=logging.WARNING, msg="other warn")

        assert anta_workflow_filter.filter(info_non_anta_record) is True
        assert anta_workflow_filter.filter(debug_non_anta) is True
        assert anta_workflow_filter.filter(warn_non_anta) is True

    def test_allows_anta_warning_or_higher(
        self,
        anta_workflow_filter: AntaWorkflowFilter,
    ) -> None:
        """Test ANTA records at WARNING or higher levels are allowed (return True)."""
        warn_anta_record = create_log_record(name="anta.runner", level=logging.WARNING, msg="anta warning")
        error_anta_record = create_log_record(name="anta.inventory", level=logging.ERROR, msg="anta error")
        critical_anta_record = create_log_record(name="anta.reporter", level=logging.CRITICAL, msg="anta critical")

        assert anta_workflow_filter.filter(warn_anta_record) is True
        assert anta_workflow_filter.filter(error_anta_record) is True
        assert anta_workflow_filter.filter(critical_anta_record) is True

    @pytest.mark.parametrize("anta_lib_name", [pytest.param(lib_name, id=lib_name) for lib_name in ANTA_LIBRARIES])
    def test_filter_various_anta_libs(self, anta_workflow_filter: AntaWorkflowFilter, anta_lib_name: str) -> None:
        """Test filtering logic against various ANTA library names."""
        info_record = create_log_record(name=f"{anta_lib_name}.sub", level=logging.INFO, msg="Info")
        warn_record = create_log_record(name=anta_lib_name, level=logging.WARNING, msg="Warn")

        assert anta_workflow_filter.filter(info_record) is False
        assert anta_workflow_filter.filter(warn_record) is True


class TestAntaWorkflowHandler:
    """Tests for the AntaWorkflowHandler class."""

    @pytest.mark.parametrize(
        ("level", "expected_display_method", "expected_error_count", "expected_warning_count"),
        [
            pytest.param(logging.DEBUG, "vvv", 0, 0, id="DEBUG"),
            pytest.param(logging.INFO, "v", 0, 0, id="INFO"),
            pytest.param(logging.WARNING, "warning", 0, 1, id="WARNING"),
            pytest.param(logging.ERROR, "error", 1, 0, id="ERROR"),
            pytest.param(logging.CRITICAL, "error", 1, 0, id="CRITICAL"),
        ],
    )
    def test_emit_routing_and_stats(
        self,
        anta_workflow_handler: AntaWorkflowHandler,
        mock_display: Mock,
        log_stats: defaultdict[str, dict[str, int]],
        unique_id: str,
        level: int,
        expected_display_method: str,
        expected_error_count: int,
        expected_warning_count: int,
    ) -> None:
        """Test log routing to correct Display method and stats tracking."""
        message = f"Message level {level}"
        # Use helper to create record *with* unique_id already set
        record = create_log_record(name="test.logger", level=level, msg=message, unique_id=unique_id)
        expected_formatted_message = f"[{unique_id}] {message}"

        anta_workflow_handler.emit(record)

        display_method = getattr(mock_display, expected_display_method)

        if level >= logging.ERROR:
            display_method.assert_called_once_with(expected_formatted_message, wrap_text=False)
        else:
            display_method.assert_called_once_with(expected_formatted_message)

        # Assert other display methods were not called
        all_methods = {"error", "warning", "v", "vvv"}
        called_method_set = {expected_display_method}
        for method_name in all_methods - called_method_set:
            getattr(mock_display, method_name).assert_not_called()

        assert log_stats[unique_id]["error_count"] == expected_error_count
        assert log_stats[unique_id]["warning_count"] == expected_warning_count

    def test_emit_with_unknown_unique_id(
        self,
        anta_workflow_handler: AntaWorkflowHandler,
        mock_display: Mock,
        log_stats: defaultdict[str, dict[str, int]],
    ) -> None:
        """Test handling when unique_id is missing from the record (uses 'unknown')."""
        message = "Error without ID"
        # Create record *without* unique_id (level ERROR)
        record = create_log_record(name="test.logger", level=logging.ERROR, msg=message)
        # The handler should format using 'unknown' when unique_id is missing
        expected_formatted_message = f"[unknown] {message}"

        anta_workflow_handler.emit(record)

        mock_display.error.assert_called_once_with(expected_formatted_message, wrap_text=False)
        assert log_stats["unknown"]["error_count"] == 1
        assert log_stats["unknown"]["warning_count"] == 0  # Ensure warning count is not affected
