# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap
from types import NoneType, UnionType
from typing import TYPE_CHECKING, Optional, TypeVar, Union, get_args, get_origin, get_type_hints

from pyavd._utils import get_all

from .constants import ACCEPTED_COERCION_MAP

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import TypeVar

    from pyavd._eos_designs.schema import EosDesigns

    from .models import AvdBase

    T = TypeVar("T")
    TT = TypeVar("TT")
    TTT = TypeVar("TTT", AvdBase)


def coerce_type(value: T, target_type: type[TT]) -> T | TT:
    # Special handling for lists since isinstance won't handle a list[<type>] type hint.
    if get_origin(target_type) is list or target_type is list:
        if not isinstance(value, list):
            # Wrong type so we cannot coerce.
            return value
        if not (args := get_args(target_type)):
            # Just expecting a plain list so nothing to coerce.
            return value

        # We got a type arg like list[str] so we coerce every list item accordingly and return as a new list.
        return [coerce_type(item_value, args[0]) for item_value in value]

    if isinstance(value, target_type):
        return value

    if target_type in ACCEPTED_COERCION_MAP and isinstance(value, ACCEPTED_COERCION_MAP[target_type]):
        try:
            return target_type(value)
        except ValueError:
            return value

    # Identify subclass of AvdBase without importing AvdBase (circular import)
    if hasattr(target_type, "_is_avd_class") and isinstance(value, (dict, ChainMap)):
        return loader(target_type, value)

    # Giving up and just returning the original value.
    return value


def key_to_attr(cls: type[AvdBase], key: str) -> str | None:
    """Returning attribute name for the given key or None if the key is invalid."""
    if key in cls._fields:
        return key
    if f"field_{key}" in cls._fields:
        return f"field_{key}"
    return None


def get_base_type(type_hints: type) -> type:
    while True:
        origin = get_origin(type_hints)
        if origin is UnionType or origin is Union:
            args = tuple(arg for arg in get_args(type_hints) if arg is not NoneType)
            if len(args) > 1:
                msg = "Unable to remove union since this field has more non-NonType than one"
                raise TypeError(msg)
            type_hints = args[0]
            continue

        if origin is Optional:
            args = get_args(type_hints)
            if len(args) > 1:
                msg = "Unable to remove Optional since this field has types inside than one"
                raise TypeError(msg)
            type_hints = args[0]
            continue

        break

    return type_hints


def get_csc_items_as_dicts(cls: EosDesigns, data: dict) -> Generator[dict, None, None]:
    """
    Find any keys starting with any prefix defined under "custom_structured_configuration_prefix" and yield them as dicts.

    This is used by both the loader and the validator
    ```yaml
    [{
        "key": <full key ex. "custom_structured_configuration_router_bgp">
        "value": <structured config including the suffix part of the key>
    }]
    ```
    """
    prefixes = data.get("custom_structured_configuration_prefix", cls.custom_structured_configuration_prefix)
    if not isinstance(prefixes, list):
        # Invalid prefix format.
        return

    for prefix in prefixes:
        if not isinstance(prefix, str):
            # Invalid prefix format.
            continue

        if not (matching_keys := [key for key in data if str(key).startswith(prefix)]):
            continue

        prefix_length = len(prefix)
        for key in matching_keys:
            yield {
                "key": key,
                "value": {key[prefix_length:]: data[key]},
            }


def get_csc_items(cls: EosDesigns, data: dict) -> list[EosDesigns._CustomStructuredConfigurationsItem]:
    # We do not have access to the target model directly (to avoid circular imports) so we will get it from the given class.
    custom_structured_configurations_item_cls = cls._CustomStructuredConfigurationsItem

    return coerce_type(list(get_csc_items_as_dicts(cls, data)), list[custom_structured_configurations_item_cls])


def get_dynamic_keys_as_dict(cls: EosDesigns, data: dict) -> dict[str, list[dict]] | None:
    """
    Extract content of dynamic keys and return them in a dict matching the _DynamicKeys model.

    {<model_key ex. "node_type_keys">: [{"key": <dynamic_key ex. "l3leaf">, "value": <value of dynamic key>}]}

    This is used by both the loader and the validator.

    The corresponding data models are auto created by the conversion from schemas, which also sets "_dynamic_key_maps" on the class:
    ```python
    _dynamic_key_maps: list[dict] = [{"dynamic_keys_path": "connected_endpoints_keys.key", "model_key": "connected_endpoints_keys"}, ...]
    ```

    Here we parse "_dynamic_key_maps" and for entry  find all values for the dynamic_keys_path (ex "node_type_keys.key") in the input data
    to identify all dynamic keys (ex "l3leaf", "spine" ...)
    """
    if getattr(cls, "_DynamicKeys", None) is None:
        return None

    dynamic_keys_dict = {}

    for dynamic_key_map in cls._DynamicKeys._dynamic_key_maps:
        dynamic_keys_path: str = dynamic_key_map["dynamic_keys_path"]
        model_key_list = []

        dynamic_keys = get_all(data, dynamic_keys_path)
        for dynamic_key in dynamic_keys:
            # dynamic_key is one key like "l3leaf".
            if (value := data.get(dynamic_key)) is None:
                # Do not add missing key or None.
                continue

            model_key_list.append({"key": dynamic_key, "value": value})

        dynamic_keys_dict[dynamic_key_map["model_key"]] = model_key_list

    return dynamic_keys_dict


def get_dynamic_keys(cls: EosDesigns, data: dict) -> EosDesigns._DynamicKeys:
    # We do not have access to the target model directly (to avoid circular imports) so we will get it from the given class.
    dynamic_keys_cls = cls._DynamicKeys

    return coerce_type(get_dynamic_keys_as_dict(cls, data), dynamic_keys_cls)


def loader(cls: type[TTT], data: dict | ChainMap) -> TTT:
    # Using hasattr to avoid importing the BaseClass which would lead to circular imports.
    if not hasattr(cls, "_is_avd_class"):
        msg = f"'cls' must be a subclass of 'AvdBase'. Got '{type(cls)}'"
        raise TypeError(msg)

    if not isinstance(data, (dict, ChainMap)):
        msg = f"Expecting 'data' as dict or ChainMap. Got '{type(data)}"
        raise TypeError(msg)

    allow_other_keys = cls._allow_other_keys
    cls_type_hints = get_type_hints(cls)
    has_custom_data = "_custom_data" in cls_type_hints
    cls_args = {}

    if hasattr(cls, "_custom_structured_configurations"):
        cls_args["_custom_structured_configurations"] = get_csc_items(cls, data)

    if hasattr(cls, "_dynamic_keys"):
        cls_args["_dynamic_keys"] = get_dynamic_keys(cls, data)

    for key in data:
        if has_custom_data and str(key).startswith("_"):
            cls_args.setdefault("_custom_data", {})[key] = data[key]
            continue

        if not (attr := key_to_attr(cls, key)):
            if allow_other_keys:
                # Ignore unknown keys.
                # This also covers the case for custom_structured_configuration keys and dynamic keys,
                # since the root dirs always allow other keys.
                continue
            msg = f"Invalid key '{key}'. Not available on '{cls.__name__}'."
            raise KeyError(msg, has_custom_data)

        base_type = get_base_type(cls_type_hints[attr])
        value = coerce_type(data[key], base_type)

        if get_origin(base_type) is list:
            # the isinstance check below does not work with args like list[str]
            base_type = list

        # Raise for wrong type.
        if not isinstance(value, (base_type, NoneType)):
            msg = f"Invalid type '{type(value)}. Expected '{base_type}'"
            raise TypeError(msg)

        cls_args[attr] = value

    return cls(**cls_args)
