# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeVar

    T = TypeVar("T")


def guaranteed_not_none(value: T | None) -> T:
    """
    Guarantee the value is not None.

    Args:
        value: Optional value to test

    Raises:
        ValueError: if the value is None.

    """
    if value is None:
        msg = "Value should never be None here."
        raise RuntimeError(msg)
    return value
