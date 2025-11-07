# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.logging import VerifyLoggingErrors

from ._base_classes import AntaTestInputFactory


class VerifyLoggingErrorsInputFactory(AntaTestInputFactory[VerifyLoggingErrors.Input]):
    """
    Input factory class for the `VerifyLoggingErrors` test.

    Generates inputs using `validate_no_errors_period` from metadata to check the last N minutes if configured.
    If not set, returns default input to validate the entire log buffer on EOS.
    """

    def create(self) -> list[VerifyLoggingErrors.Input] | None:
        """Create a list of inputs for the `VerifyLoggingErrors` test."""
        if (last_number_time_units := self.structured_config.metadata.validate_no_errors_period) is None:
            return [VerifyLoggingErrors.Input()]
        return [VerifyLoggingErrors.Input(last_number_time_units=last_number_time_units, time_unit="minutes")]
