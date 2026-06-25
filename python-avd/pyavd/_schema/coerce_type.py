# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from .constants import ACCEPTED_COERCION_MAP
from .models import is_avd_data_class_type

if TYPE_CHECKING:
    from typing import NoReturn

    from .models.type_vars import T_ItemType


def coerce_type(value: Any, target_type: type[T_ItemType]) -> T_ItemType:
    """
    Return a coerced variant of the given value to the target_type.

    If the value is already of the correct type the value will be returned untouched.

    If coercion cannot be done this will raise a TypeError.
    """
    if value is None:
        if is_avd_data_class_type(target_type):
            # None values are sometimes used to overwrite inherited profiles.
            return target_type._from_null()

        # Other None values are left untouched.
    elif target_type is Any or isinstance(value, target_type):
        # Avoid hitting the else block.
        pass

    elif target_type in ACCEPTED_COERCION_MAP and isinstance(value, ACCEPTED_COERCION_MAP[target_type]):
        try:
            return target_type(value)
        except ValueError as exception:
            raise_coerce_error(value, target_type, exception)

    elif is_avd_data_class_type(target_type):
        try:
            return cast("T_ItemType", target_type._load(data=value))
        except TypeError as exception:
            raise_coerce_error(value, target_type, exception)

    else:
        raise_coerce_error(value, target_type)

    # All the pass brings us here to return the original value.
    return cast("T_ItemType", value)


def raise_coerce_error(value: Any, target_type: type, exception: Exception | None = None) -> NoReturn:
    # Not possible to coerce value.
    msg = f"Invalid type '{type(value)}'. Unable to coerce to type '{target_type}' for the value: {value}"
    if exception is not None:
        raise TypeError(msg) from exception
    raise TypeError(msg)
