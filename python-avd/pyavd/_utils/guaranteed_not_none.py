# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeVar

    # TODO: Once we drop 3.13 support this can be imported from typing.
    from typing_extensions import TypeIs

    T = TypeVar("T")


def guaranteed_not_none(value: T | None) -> TypeIs[T]:
    """
    Guarantee the value is not None.

    Args:
        value: Optional value to test

    Raises:
        RuntimeError: if the value is None.

    """
    if value is None:
        msg = "value is 'None' and was not expected to be."
        raise RuntimeError(msg)
    return True
