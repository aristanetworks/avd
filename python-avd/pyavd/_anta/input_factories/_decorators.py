# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections.abc import Callable, Iterator
from functools import wraps
from typing import TypeVar

from anta.models import AntaTest

from pyavd._anta.constants import StructuredConfigKey
from pyavd._anta.logs import LogMessage
from pyavd._utils import get_v2

from ._base_classes import AntaTestInputFactory

F = TypeVar("F", bound=AntaTestInputFactory)
R = TypeVar("R")

T_AntaTestInputFactoryMethod = Callable[[F], Iterator[R]]


def skip_if_hardware_validation_disabled(func: T_AntaTestInputFactoryMethod) -> T_AntaTestInputFactoryMethod:
    """Decorator to skip execution of an input factory method if hardware validation is disabled."""

    @wraps(func)
    def wrapper(self: AntaTestInputFactory) -> Iterator[AntaTest.Input]:
        if not self.structured_config.metadata.validate_hardware.enabled:
            self.logger_adapter.debug(LogMessage.HARDWARE_VALIDATION_DISABLED)
            return
        yield from func(self)

    return wrapper


def skip_if_extra_fabric_validation_disabled(func: T_AntaTestInputFactoryMethod) -> T_AntaTestInputFactoryMethod:
    """Decorator to skip execution of an input factory method if extra fabric validation is disabled."""

    @wraps(func)
    def wrapper(self: AntaTestInputFactory) -> Iterator[AntaTest.Input]:
        if not self.data_source.extra_fabric_validation:
            self.logger_adapter.debug(LogMessage.EXTRA_FABRIC_VALIDATION_DISABLED)
            return
        yield from func(self)

    return wrapper


def skip_if_wan_router(func: T_AntaTestInputFactoryMethod) -> T_AntaTestInputFactoryMethod:
    """Decorator to skip execution of an input factory method if the device is a WAN router."""

    @wraps(func)
    def wrapper(self: AntaTestInputFactory) -> Iterator[AntaTest.Input]:
        if self.data_source.is_wan_router:
            self.logger_adapter.debug(LogMessage.DEVICE_IS_WAN_ROUTER)
            return
        yield from func(self)

    return wrapper


def skip_if_missing_config(*keys: StructuredConfigKey) -> Callable[[T_AntaTestInputFactoryMethod], T_AntaTestInputFactoryMethod]:
    """Decorator to skip execution of an input factory method if specific keys are missing in the structured configuration."""

    def decorator(func: T_AntaTestInputFactoryMethod) -> T_AntaTestInputFactoryMethod:
        key_values = [k.value for k in keys]

        @wraps(func)
        def wrapper(self: AntaTestInputFactory) -> Iterator[AntaTest.Input]:
            # Check if all keys resolve to a truthy value in the config
            if not all(get_v2(self.structured_config, value) for value in key_values):
                self.logger_adapter.debug(LogMessage.INPUT_NO_DATA_MODELS, data_models=", ".join(key_values))
                return
            yield from func(self)

        return wrapper

    return decorator


def skip_if_not_vtep(func: T_AntaTestInputFactoryMethod) -> T_AntaTestInputFactoryMethod:
    """Decorator to skip execution of an input factory method if the device is NOT a VTEP."""

    @wraps(func)
    def wrapper(self: AntaTestInputFactory) -> Iterator[AntaTest.Input]:
        if not self.data_source.is_vtep:
            self.logger_adapter.debug(LogMessage.DEVICE_IS_NOT_VTEP)
            return
        yield from func(self)

    return wrapper
