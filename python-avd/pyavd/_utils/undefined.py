# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any, Literal

# TypeIs was added to python in 3.13
from typing_extensions import TypeIs


class UndefinedType:
    """Singleton used instead of None to detect fields that are not set specifically."""

    _instance: "UndefinedType"

    def __new__(cls, *_args: Any, **_kwargs: Any) -> "UndefinedType":
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance

    def __bool__(self) -> Literal[False]:
        return False


Undefined = UndefinedType()


def is_undefined(val: Any | UndefinedType) -> TypeIs[UndefinedType]:
    return val is Undefined
