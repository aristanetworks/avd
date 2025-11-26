# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Callable
from functools import wraps
from typing import TypeVar

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory

F = TypeVar("F", bound=AntaTestInputFactory)
R = TypeVar("R")


def skip_if_hardware_validation_disabled(func: Callable[[F], R]) -> Callable[[F], R | None]:
    """Decorator to skip execution of the input factory create method if hardware validation is disabled."""

    @wraps(func)
    def wrapper(self: F) -> R | None:
        if not self.structured_config.metadata.validate_hardware.enabled:
            self.logger_adapter.debug(LogMessage.HARDWARE_VALIDATION_DISABLED)
            return None
        return func(self)

    return wrapper
