# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING
from warnings import warn

from .loader import loader
from .validator import validator

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T = TypeVar("T")


class AvdBase:
    _is_avd_class: bool = True
    _allow_other_keys: bool = False
    _fields: tuple[str, ...]
    _required_fields: tuple[str, ...]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        pass

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        attrs = [f"{key}={getattr(self, key, None)!r}" for key in (self._fields or ()) if getattr(self, key, None) is not None]
        return f"<{cls_name}({', '.join(attrs)})>"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, AvdBase):
            return repr(self) == repr(other)
        return super().__eq__(other)

    @classmethod
    def _validate_dict(cls, data: dict) -> bool:
        if warnings := validator(data, cls, []):
            for warning in warnings:
                warn(warning)  # noqa: B028
            return False
        return True

    @classmethod
    def _from_dict(cls: type[T], data: dict) -> T:
        return loader(cls, data)
