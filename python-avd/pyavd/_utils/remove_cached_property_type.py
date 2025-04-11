# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from functools import cached_property
    from typing import TypeVar

    T = TypeVar("T")


def remove_cached_property_type(func: cached_property[T]) -> T:
    """
    This function should be used as a decorator on class methods decorated with @cached_property.

    It will change the typehint of the method from cached_property[T] to T.
    This is required when a class implements a protocol describing types as regular class attributes.
    Without this the type checkers complain about the implementation being incompatible when it is really not.
    """
    return cast("T", func)
