# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Literal

if TYPE_CHECKING:
    from typing_extensions import Self


class UndefinedType:
    """Singleton used instead of None to detect fields that are not set specifically."""

    _instance: Self

    def __new__(cls, *_args: Any, **_kwargs: Any) -> Self:
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __bool__(self) -> Literal[False]:
        return False


Undefined = UndefinedType()
