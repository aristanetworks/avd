# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections.abc import Mapping, Sequence
from types import NoneType
from typing import TYPE_CHECKING, Any, ClassVar, TypeVar

from pyavd._utils import get_all

from .constants import ACCEPTED_COERCION_MAP
from .store import create_store
from .utils import get_instance_with_defaults

if TYPE_CHECKING:
    from collections.abc import Generator
    from typing import TypeVar

    from pyavd._eos_designs.schema import EosDesigns

    from .models import AvdIndexedList, AvdModel

    T = TypeVar("T")
    TT = TypeVar("TT")
    T_AvdModel = TypeVar("T_AvdModel", bound=AvdModel)
    T_AvdIndexedList = TypeVar("T_AvdIndexedList", bound=AvdIndexedList)


def nullifiy_class(cls: type) -> type:
    """
    Returns a subclass of the given class which has the extra attribute '_is_nullified'.

    This class is used when the input for a dict or a list is None/null/none,
    to be able to signal to the deepmerge/inherit methods that this is not the same as an unset variable.
    """

    class NullifiedCls(cls):
        _is_nullified: ClassVar[bool] = True

    return NullifiedCls


def coerce_type(value: Any, target_type: type[T], list_items_type: type[TT] | None = None) -> T | list[TT]:
    """
    Return a coerced variant of the given value to the target_type or for lists a list of the the list_items_type.

    If the value is already of the correct type the value will be returned untouched.

    If coercion cannot be done, the original value will be returned. The calling function should catch the wrong type if necessary.
    """
    if value is None and (target_type is list or hasattr(target_type, "_is_avd_class")):
        # None values are sometimes used to overwrite inherited profiles.
        # This ensures we still follow the type hint of the class.
        return nullifiy_class(target_type)()

    # Special handling for lists since we need to check every item
    if target_type is list:
        if not isinstance(value, list) or list_items_type is None:
            # Wrong type so we cannot coerce or just expecting a plain list so nothing to coerce.
            return value

        # We got a type with items types like list[str] so we coerce every list item accordingly and return as a new list.
        return [coerce_type(item_value, list_items_type) for item_value in value]

    if target_type is Any or isinstance(value, target_type):
        pass

    elif target_type in ACCEPTED_COERCION_MAP and isinstance(value, ACCEPTED_COERCION_MAP[target_type]):
        try:
            return target_type(value)
        except ValueError:
            # Returns original value (too many returns triggers linting violation)
            pass

    # Identify subclass of AvdModel without importing AvdModel (circular import)
    elif hasattr(target_type, "_is_avd_model") and isinstance(value, Mapping):
        return load_model(target_type, value)

    # Identify subclass of AvdIndexedList without importing AvdIndexedList (circular import)
    elif hasattr(target_type, "_is_avd_collection") and isinstance(value, Sequence):
        return load_collection(target_type, value)

    # Giving up and just returning the original value.
    return value


def key_to_attr(cls: type[AvdModel], key: str) -> str | None:
    """Returning attribute name for the given key or None if the key is invalid."""
    if key in cls._fields:
        return key
    if f"field_{key}" in cls._fields:
        return f"field_{key}"
    return None


def get_csc_items_as_dicts(_cls: type[EosDesigns], data: dict) -> Generator[dict, None, None]:
    """
    Find any keys starting with any prefix defined under "custom_structured_configuration_prefix" and yield them as dicts.

    ```yaml
    [{
        "key": <full key ex. "custom_structured_configuration_router_bgp">
        "value": <structured config including the suffix part of the key>
    }]
    ```
    """
    # TODO: Improve the fetch of default. We need to store the default value somewhere, since this is executed before __init__ of EosDesigns.
    data_with_default = get_instance_with_defaults(data, "custom_structured_configuration_prefix", create_store()["eos_designs"])
    prefixes = data_with_default["custom_structured_configuration_prefix"]
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
        # TODO: Just create to proper data models instead of using coerce type.
        for key in matching_keys:
            yield {
                "key": key,
                "value": {key[prefix_length:]: data[key]},
            }


def get_csc_items(cls: type[EosDesigns], data: dict) -> list[EosDesigns._CustomStructuredConfigurationsItem]:
    """Returns a list of _CustomStructuredConfigurationsItem objects containing each custom structured configuration extracted from the inputs."""
    # We do not have access to the target model directly (to avoid circular imports) so we will get it from the given class.
    custom_structured_configurations_item_cls = cls._CustomStructuredConfigurationsItem

    return coerce_type(list(get_csc_items_as_dicts(cls, data)), target_type=list, list_items_type=custom_structured_configurations_item_cls)


def get_dynamic_keys_as_dict(cls: type[EosDesigns], data: Mapping) -> dict[str, list[dict]] | None:
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

    schema = create_store()["eos_designs"]

    dynamic_keys_dict = {}

    for dynamic_key_map in cls._DynamicKeys._dynamic_key_maps:
        dynamic_keys_path: str = dynamic_key_map["dynamic_keys_path"]
        model_key_list = dynamic_keys_dict.setdefault(dynamic_key_map["model_key"], [])

        # TODO: Improve the fetch of default. We need to store the default value somewhere, since this is executed before __init__ of EosDesigns.
        data_with_default = get_instance_with_defaults(data, dynamic_keys_path, schema)
        dynamic_keys = get_all(data_with_default, dynamic_keys_path)
        for dynamic_key in dynamic_keys:
            # dynamic_key is one key like "l3leaf".
            if (value := data.get(dynamic_key)) is None:
                # Do not add missing key or None.
                continue

            model_key_list.append({"key": dynamic_key, "value": value})

    return dynamic_keys_dict


def get_dynamic_keys(cls: type[EosDesigns], data: Mapping) -> EosDesigns._DynamicKeys:
    """
    Returns the DynamicKeys object which holds a list for each dynamic key.

    The lists contain an entry for each dynamic key found in the inputs and the content of that key conforming to the schema.
    """
    # We do not have access to the target model directly (to avoid circular imports) so we will get it from the given class.
    dynamic_keys_cls = cls._DynamicKeys

    # TODO: Just create to proper data models instead of using coerce type.
    return coerce_type(get_dynamic_keys_as_dict(cls, data), dynamic_keys_cls)


def loader(cls: type[T_AvdModel | T_AvdIndexedList], data: Mapping | Sequence) -> T_AvdData:
    # Using hasattr to avoid importing the BaseClass which would lead to circular imports.
    if hasattr(cls, "_is_avd_class"):
        if hasattr(cls, "_is_avd_model"):
            return load_model(cls, data)
        if hasattr(cls, "_is_avd_collection"):
            return load_collection(cls, data)

    msg = f"'cls' must be a subclass of 'AvdModel' or 'AvdIndexedList'. Got '{type(cls)}'"
    raise TypeError(msg)


def load_model(cls: type[T_AvdModel], data: Mapping) -> T_AvdModel:
    if not isinstance(data, Mapping):
        msg = f"Expecting 'data' as a 'Mapping' when loading data into '{cls.__name__}'. Got '{type(data)}"
        raise TypeError(msg)

    allow_other_keys = cls._allow_other_keys
    cls_fields = cls._fields
    has_custom_data = "_custom_data" in cls_fields
    has_csc = "_custom_structured_configurations" in cls_fields
    has_dynamic_keys = "_dynamic_keys" in cls_fields
    cls_args = {}

    if has_csc:
        cls_args["_custom_structured_configurations"] = get_csc_items(cls, data)

    if has_dynamic_keys:
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

        cls_field_data = cls_fields[attr]

        base_type = cls_field_data["type"]
        value = coerce_type(data[key], base_type, list_items_type=cls_field_data.get("items"))

        # Raise for wrong type ignoring None values - we expect the validation to have sorted out required fields.
        if not isinstance(value, (base_type, NoneType)):
            msg = f"Invalid type '{type(value)}. Expected '{base_type}'. Value '{value}"
            raise TypeError(msg)

        cls_args[attr] = value

    return cls(**cls_args)


def load_collection(cls: type[T_AvdIndexedList], data: Sequence) -> T_AvdIndexedList:
    if not isinstance(data, Sequence):
        msg = f"Expecting 'data' as a 'Sequence' when loading data into '{cls.__name__}'. Got '{type(data)}"
        raise TypeError(msg)

    item_type = cls._item_type
    cls_items = []
    for item in data:
        value = coerce_type(item, item_type)

        # Raise for wrong type ignoring None values - we expect the validation to have sorted out required fields.
        if not isinstance(value, (item_type, NoneType)):
            msg = f"Invalid type '{type(value)}. Expected '{item_type}'. Value '{value}"
            raise TypeError(msg)

        cls_items.append(value)
    return cls(cls_items)
