# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from collections import ChainMap
from types import NoneType, UnionType
from typing import TYPE_CHECKING, Annotated, Any, Optional, Union, get_args, get_origin, get_type_hints

from .constants import ACCEPTED_COERCION_MAP
from .loader import coerce_type, get_csc_items_as_dicts, get_dynamic_keys_as_dict, key_to_attr
from .types import (
    Format,
    InvalidKey,
    InvalidLength,
    InvalidPattern,
    InvalidType,
    InvalidValue,
    Lower,
    Max,
    MaxLen,
    Min,
    MinLen,
    MissingKey,
    Pattern,
    ValidValues,
)

if TYPE_CHECKING:
    from .models import AvdBase


def annotated_validator(value: Any, type_hint: type[Annotated[type, Any]], path: list[str | int]) -> set[UserWarning] | None:
    args = get_args(type_hint)

    # First perform basic type validation. If this fails we don't have to check all the annotations.
    if arg_warnings := validator(value, args[0], path):
        return arg_warnings

    # Basic type validation succeeded so we can dig deeper into the annotations and validate each.

    # First coerce the value to the correct.
    value = coerce_type(value, args[0])

    warnings = set()
    for arg in args[1:]:
        # Special handling of Lower since we need to modify the value used in subsequent validation.
        if arg is Lower:
            value = str(value).lower()
            continue
        if arg_warnings := validator(value, arg, path):
            warnings.update(arg_warnings)

    return warnings or None


def none_validator(value: Any, _type_hint: type[NoneType], path: list[str | int]) -> set[UserWarning] | None:
    if value is None:
        return None

    return {InvalidType(type(value), NoneType, path)}


def union_validator(value: Any, type_hint: type[UnionType | Any], path: list[str | int]) -> set[UserWarning] | None:
    warnings = set()
    for arg in get_args(type_hint):
        if not (arg_warnings := validator(value, arg, path)):
            return None

        # Ignore warnings for NoneType since we always have another type in the union
        if arg is not NoneType:
            warnings.update(arg_warnings)

    return warnings or None


def str_validator(value: Any, _type_hint: type[str], path: list[str | int]) -> set[UserWarning] | None:
    if isinstance(value, str):
        return None

    if isinstance(value, ACCEPTED_COERCION_MAP[str]):
        try:
            str(value)
        except ValueError:
            pass
        else:
            return None

    return {InvalidType(type(value), str, path)}


def int_validator(value: Any, _type_hint: type[int], path: list[str | int]) -> set[UserWarning] | None:
    if isinstance(value, int):
        return None

    if isinstance(value, ACCEPTED_COERCION_MAP[int]):
        try:
            int(value)
        except ValueError:
            pass
        else:
            return None

    return {InvalidType(type(value), int, path)}


def bool_validator(value: Any, _type_hint: type[bool], path: list[str | int]) -> set[UserWarning] | None:
    if isinstance(value, bool):
        return None

    if isinstance(value, ACCEPTED_COERCION_MAP[bool]):
        try:
            bool(value)
        except ValueError:
            pass
        else:
            return None

    return {InvalidType(type(value), bool, path)}


def dict_validator(value: Any, _type_hint: type[dict], path: list[str | int]) -> set[UserWarning] | None:
    if isinstance(value, dict):
        return None

    return {InvalidType(type(value), dict, path)}


def list_validator(value: Any, type_hint: type[list | list[Any]], path: list[str | int]) -> set[UserWarning] | None:
    if not isinstance(value, list):
        return {InvalidType(type(value), list, path)}

    if not (args := get_args(type_hint)):
        # We know it's a list and we have no further information
        return None

    warnings = set()
    for index, item_value in enumerate(value):
        if item_warnings := validator(item_value, args[0], [*path, index]):
            warnings.update(item_warnings)

    return warnings or None


def avd_class_validator(value: dict | ChainMap, cls: type[AvdBase], path: list[str | int]) -> set[UserWarning] | None:
    if not isinstance(value, (cls, dict, ChainMap)):
        return {InvalidType(type(value), dict, path)}  # TODO: reconsider which type we should use as expected type (or types?)

    # Insert dynamic values, so they can be validated towards the class.
    if hasattr(cls, "_custom_structured_configurations"):
        value = ChainMap(value, {"_custom_structured_configurations": list(get_csc_items_as_dicts(cls, value))})
    if hasattr(cls, "_dynamic_keys"):
        value = ChainMap(value, {"_dynamic_keys": get_dynamic_keys_as_dict(cls, value)})

    warnings = set()
    allow_other_keys = cls._allow_other_keys
    cls_type_hints = get_type_hints(cls, include_extras=True)
    has_custom_data = "_custom_data" in cls_type_hints

    # Validate the given data key by key
    for key in value:
        if has_custom_data and str(key).startswith("_") and key not in ("_custom_structured_configurations", "_dynamic_keys"):
            # Skip validation for custom keys.
            continue

        if not (attr := key_to_attr(cls, key)):
            if allow_other_keys:
                # Ignore unknown keys.
                # This also covers the case for custom_structured_configuration keys and dynamic keys,
                # since the root dirs always allow other keys.
                continue
            warnings.add(InvalidKey([*path, key]))
            continue

        if attr_warnings := validator(value[key], cls_type_hints[attr], [*path, key]):
            warnings.update(attr_warnings)

    # Validate if all required keys have been given
    if missing_keys := set(getattr(cls, "_required_fields", ())).difference(value):
        for missing_key in missing_keys:
            warnings.add(MissingKey([*path, missing_key]))

    return warnings or None


def optional_validator(value: Any, type_hint: type[Any | None], path: list[str | int]) -> set[UserWarning] | None:
    if value is None:
        return None
    return validator(value, get_args(type_hint)[0], path)


def valid_values_validator(value: Any, type_hint: type[ValidValues[Any]], path: list[str | int]) -> set[UserWarning] | None:
    valid_values = get_args(type_hint)
    if value in valid_values:
        return None

    return {InvalidValue(value, valid_values, path)}


def format_validator(_value: Any, _type_hint: type[Format[str]], _path: list[str | int]) -> set[UserWarning] | None:
    # TODO: Implement this
    pass


def max_len_validator(value: Any, type_hint: type[MaxLen[int]], path: list[str | int]) -> set[UserWarning] | None:
    max_len = get_args(type_hint)[0]
    if (length := len(value)) <= max_len:
        return None
    return {InvalidLength(length, f"<={max_len}", path)}


def min_len_validator(value: Any, type_hint: type[MinLen[int]], path: list[str | int]) -> set[UserWarning] | None:
    min_len = get_args(type_hint)[0]
    if (length := len(value)) >= min_len:
        return None
    return {InvalidLength(length, f">={min_len}", path)}


def pattern_validator(value: Any, type_hint: type[Pattern[str]], path: list[str | int]) -> set[UserWarning] | None:
    pattern = get_args(type_hint)[0]
    if re.fullmatch(pattern, value):
        return None

    return {InvalidPattern(value, pattern, path)}


def max_validator(value: Any, type_hint: type[Max[int]], path: list[str | int]) -> set[UserWarning] | None:
    max_value = get_args(type_hint)[0]
    if value <= max_value:
        return None
    return {InvalidValue(value, f"<={max_value}", path)}


def min_validator(value: Any, type_hint: type[Min[int]], path: list[str | int]) -> set[UserWarning] | None:
    min_value = get_args(type_hint)[0]
    if value >= min_value:
        return None
    return {InvalidValue(value, f">={min_value}", path)}


VALIDATORS = {
    Annotated: annotated_validator,
    NoneType: none_validator,
    UnionType: union_validator,
    Union: union_validator,
    Optional: optional_validator,
    str: str_validator,
    int: int_validator,
    bool: bool_validator,
    list: list_validator,
    dict: dict_validator,
    "avd_class": avd_class_validator,
    ValidValues: valid_values_validator,
    Format: format_validator,
    MaxLen: max_len_validator,
    MinLen: min_len_validator,
    Max: max_validator,
    Min: min_validator,
    Pattern: pattern_validator,
}


def validator(value: Any, type_hint: type, path: list[str | int]) -> set[UserWarning] | None:
    # Identify subclass of AvdBase without importing AvdBase (circular import)
    if hasattr(type_hint, "_is_avd_class"):
        origin = "avd_class"

    # Identify Validation types without importing the base type (circular import)
    elif hasattr(type_hint, "_is_validation_annotation") and hasattr(type_hint, "__origin__"):
        origin = type_hint.__origin__

    # Workaround to avoid warning about required keys inside structured_config.
    elif value is None and "structured_config" in path:
        return None
    elif not (origin := get_origin(type_hint)):
        origin = type_hint

    try:
        return VALIDATORS[origin](value, type_hint, path)
    except KeyError as e:
        msg = f"Unable to validate type {origin} for path {path} from type hint {type_hint}"
        raise TypeError(msg) from e
