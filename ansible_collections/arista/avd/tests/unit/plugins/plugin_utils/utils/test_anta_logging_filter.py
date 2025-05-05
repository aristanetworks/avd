# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Unit tests for the anta_logging_filter module."""
import logging

from ansible_collections.arista.avd.plugins.plugin_utils.utils import AntaLoggingFilter


class TestAntaLoggingFilter:
    """Test the AntaLoggingFilter class."""

    def test_exclude_anta_logs(self, anta_record: logging.LogRecord, non_anta_record: logging.LogRecord) -> None:
        """Test that ANTA library logs are excluded when exclude=True."""
        filter_obj = AntaLoggingFilter(exclude=True)

        # ANTA library logs should be filtered out (return False)
        assert filter_obj.filter(anta_record) is False

        # Non-ANTA library logs should be kept (return True)
        assert filter_obj.filter(non_anta_record) is True

    def test_include_anta_logs(self, anta_record: logging.LogRecord, non_anta_record: logging.LogRecord) -> None:
        """Test that ANTA library logs are included when exclude=False."""
        filter_obj = AntaLoggingFilter(exclude=False)

        # ANTA library logs should be kept (return True)
        assert filter_obj.filter(anta_record) is True

        # Non-ANTA library logs should be filtered out (return False)
        assert filter_obj.filter(non_anta_record) is False

    def test_warning_tracking(self, anta_record: logging.LogRecord, warning_record: logging.LogRecord) -> None:
        """Test that warnings from ANTA libraries are tracked."""
        has_warnings = [False]
        filter_obj = AntaLoggingFilter(has_warnings_ref=has_warnings)

        # Filter should not change the warning tracker for INFO records
        filter_obj.filter(anta_record)
        assert has_warnings[0] is False

        # Filter should update the warning tracker for WARNING records
        filter_obj.filter(warning_record)
        assert has_warnings[0] is True

    def test_other_anta_libraries(self) -> None:
        """Test that logs from other ANTA libraries are filtered correctly."""
        filter_obj = AntaLoggingFilter(exclude=True)

        # Test each ANTA library
        for library in AntaLoggingFilter._anta_libraries:
            record = logging.LogRecord(
                name=f"{library}.something",
                level=logging.INFO,
                pathname="",
                lineno=0,
                msg="Test message",
                args=(),
                exc_info=None
            )

            # Should be filtered out in exclude mode
            assert filter_obj.filter(record) is False

    def test_non_anta_libraries(self) -> None:
        """Test that non-ANTA libraries are correctly identified."""
        filter_obj = AntaLoggingFilter(exclude=True)

        # Test some non-ANTA libraries
        for library in ["pyavd", "ansible_collections.arista.avd"]:
            record = logging.LogRecord(
                name=f"{library}.something",
                level=logging.INFO,
                pathname="",
                lineno=0,
                msg="Test message",
                args=(),
                exc_info=None
            )

            # Should be kept in exclude mode
            assert filter_obj.filter(record) is True
