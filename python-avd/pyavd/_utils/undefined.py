# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any


class Undefined:
    """Singleton used instead of None to detect fields that are not set specifically."""

    _instance: "Undefined"

    def __new__(cls, *_args: Any, **_kwargs: Any) -> "Undefined":
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance


UndefinedType = type[Undefined]
