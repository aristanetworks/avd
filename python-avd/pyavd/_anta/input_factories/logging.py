# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.logging import VerifyLoggingErrors

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyLoggingErrorsInputFactory(AntaTestInputFactory[VerifyLoggingErrors.Input]):
    """
    Input factory class for the `VerifyLoggingErrors` test.

    Generates inputs using `validate_no_errors_period` from metadata to check the last N minutes if configured.
    If not set, returns default input to validate the entire log buffer on EOS.
    """

    def create(self) -> Iterator[VerifyLoggingErrors.Input]:
        """Generate the inputs for the `VerifyLoggingErrors` test."""
        if (last_number_time_units := self.structured_config.metadata.validate_no_errors_period) is None:
            yield VerifyLoggingErrors.Input()
        else:
            yield VerifyLoggingErrors.Input(last_number_time_units=last_number_time_units, time_unit="minutes")
