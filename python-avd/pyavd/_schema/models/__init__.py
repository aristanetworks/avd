# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TypeGuard

    from .type_vars import AvdDataClass


def is_avd_data_class(obj: object) -> TypeGuard[AvdDataClass]:
    return getattr(obj, "_is_avd_data_class", False)


def is_avd_data_class_type(typ: type[object]) -> TypeGuard[type[AvdDataClass]]:
    return getattr(typ, "_is_avd_data_class", False)
