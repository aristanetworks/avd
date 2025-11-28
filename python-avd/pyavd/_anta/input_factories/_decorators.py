# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Callable, Iterator
from functools import wraps
from typing import TypeVar

from anta.models import AntaTest

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory

F = TypeVar("F", bound=AntaTestInputFactory)
R = TypeVar("R", bound=AntaTest.Input)


def skip_if_hardware_validation_disabled(func: Callable[[F], Iterator[R]]) -> Callable[[F], Iterator[R]]:
    """Decorator to skip execution of the input factory create method if hardware validation is disabled."""

    @wraps(func)
    def wrapper(self: F) -> Iterator[R]:
        if not self.structured_config.metadata.validate_hardware.enabled:
            self.logger_adapter.debug(LogMessage.HARDWARE_VALIDATION_DISABLED)
            return
        yield from func(self)

    return wrapper


def skip_if_extra_fabric_validation_disabled(func: Callable[[F], Iterator[R]]) -> Callable[[F], Iterator[R]]:
    """Decorator to skip execution of the input factory create method if extra fabric validation is disabled."""

    @wraps(func)
    def wrapper(self: F) -> Iterator[R]:
        if not self.device.settings.extra_fabric_validation:
            self.logger_adapter.debug(LogMessage.EXTRA_FABRIC_VALIDATION_DISABLED)
            return
        yield from func(self)

    return wrapper


def skip_if_wan_router(func: Callable[[F], Iterator[R]]) -> Callable[[F], Iterator[R]]:
    """Decorator to skip execution of the input factory create method if the device is a WAN router."""

    @wraps(func)
    def wrapper(self: F) -> Iterator[R]:
        if self.device.is_wan_router:
            self.logger_adapter.debug(LogMessage.DEVICE_IS_WAN_ROUTER)
            return
        yield from func(self)

    return wrapper
