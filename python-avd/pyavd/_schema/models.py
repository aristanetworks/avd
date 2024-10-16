# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from typing import TYPE_CHECKING, ClassVar, Literal

from pyavd._utils import Undefined

from .loader import loader

if TYPE_CHECKING:
    from typing import Any, TypeVar

    T_AvdBase = TypeVar("T_AvdBase", bound="AvdBase")


class AvdBase:
    _is_avd_class: bool = True
    _allow_other_keys: bool = False
    _fields: ClassVar[dict[str, dict]]
    _required_fields: tuple[str, ...]

    @classmethod
    def _from_dict(cls: type[T_AvdBase], data: dict) -> T_AvdBase:
        """Returns a new instance loaded with the data from the given dict."""
        return loader(cls, data)

    def __getattr__(self, name: str) -> Any:
        """
        Resolves the default value for a field, set the default value on the attribute and return the value.

        We only get here if the attribute is not set already, and next call will skip this since the attribute is set.

        We check for a default value in the _fields information and if something is there we return that.
        - For lists, dicts and AvdBase subclasses the default value is a callable to generate a new instance to avoid reusing a mutable object.
        - For other types, which are immutable, the default value is taken directly.

        If there is no default value in the field info, we return the default-default depending on type.
        - For lists and dicts we return new empty list / dict.
        - For AvdBase subclasses we return a new empty instance of the class.
        - For other types we return None.
        """
        if name not in self._fields:
            raise AttributeError("'" + self.__class__.__name__ + "' object has no attribute '" + name + "'")
        field_info = self._fields[name]
        field_type: type = field_info["type"]
        if field_type is list:
            # Callable default value.
            new_default_value = default_function(field_info["items"]) if (default_function := field_info.get("default")) else []
        elif issubclass(field_type, AvdBase) or field_type is dict:
            new_default_value = default_function(field_type) if (default_function := field_info.get("default")) else field_type()
        else:
            new_default_value = field_info.get("default")

        setattr(self, name, new_default_value)
        return new_default_value

    def _get_defined_attr(self, name: str) -> Any | Undefined:
        """
        Get attribute or Undefined.

        Avoids the overridden __getattr__ to avoid default values.
        """
        if name not in self._fields:
            raise AttributeError("'" + self.__class__.__name__ + "' object has no attribute '" + name + "'")
        try:
            return self.__getattribute__(name)
        except AttributeError:
            return Undefined

    def __repr__(self) -> str:
        """Returns a repr with all the fields that a set including any nested models."""
        cls_name = self.__class__.__name__
        attrs = [f"{key}={getattr(self, key)!r}" for key in (self._fields or ()) if self._get_defined_attr(key) is not Undefined]
        return f"<{cls_name}({', '.join(attrs)})>"

    def __bool__(self) -> bool:
        """
        Boolean check on the class to quickly determine if any parameter is set.

        The check includes the default values and is performed recursively on any nested models.
        """
        # Consider if we should also add "if self._get_defined_attr(key) is not Undefined" to ignore default values.
        return any(getattr(self, key, None) for key in (self._fields or ()))

    def __eq__(self, other: object) -> bool:
        """Compare two instances of AvdBase by comparing their repr."""
        if isinstance(other, AvdBase):
            return repr(self) == repr(other)
        return super().__eq__(other)

    def _as_dict(self) -> dict:
        """Returns a dict with all the data from this model and any nested models."""
        as_dict = {}
        for field, field_info in self._fields.items() or ():
            if (value := self._get_defined_attr(field)) is Undefined:
                continue
            if issubclass(field_info["type"], AvdBase) and isinstance(value, AvdBase):
                as_dict[field] = value._as_dict()
                continue
            if field_info["type"] is list and issubclass(field_info["items"], AvdBase) and isinstance(value, list):
                as_dict[field] = [item._as_dict() for item in value if isinstance(item, AvdBase)]
                continue

            as_dict[field] = value

        return as_dict

    def _update(self: T_AvdBase, other: T_AvdBase) -> None:
        """Update instance by shallow merging the other instance in."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        for field in cls._fields:
            if new_value := other._get_defined_attr(field) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value:
                continue
            setattr(self, field, new_value)

    def _deepcopy(self: T_AvdBase) -> T_AvdBase:
        """Return a copy including all nested models."""
        return deepcopy(self)

    def _deepmerge(self: T_AvdBase, other: T_AvdBase, list_merge: Literal["append", "replace"] = "append") -> None:
        """Update instance by deepmerging the other instance in."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to merge type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field, field_info in cls._fields.items():
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value:
                continue

            if not isinstance(old_value, type(new_value)) or getattr(new_value, "_is_nullified", False):
                # Different type so we can just replace
                setattr(self, field, new_value)
                continue

            # Merge new value
            field_type = field_info["type"]
            if field_type is list and list_merge == "append":
                setattr(self, field, old_value + new_value)
            elif issubclass(field_type, AvdBase) and isinstance(old_value, field_type):
                # Merge in to the existing object
                old_value._deepmerge(new_value, list_merge=list_merge)
            else:
                setattr(self, field, new_value)

    def _deepmerged(self: T_AvdBase, other: T_AvdBase, list_merge: Literal["append", "replace"] = "append") -> T_AvdBase:
        """Return new instance with the result of the deepmerge of "other" on this instance."""
        new_instance = self._deepcopy()
        new_instance._deepmerge(other=other, list_merge=list_merge)
        return new_instance

    def _inherit(self: T_AvdBase, other: T_AvdBase) -> None:
        """Update unset fields on this instance with fields from other instance. No merging."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field in cls._fields:
            if self._get_defined_attr(field) is not Undefined:
                continue
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue

            setattr(self, field, new_value)

    def _deepinherit(self: T_AvdBase, other: T_AvdBase) -> None:
        """Update instance by recursively inheriting unset fields from other instance. Lists are not merged."""
        cls = type(self)
        if not isinstance(other, cls):
            msg = f"Unable to inherit from type '{type(other)}' into '{cls}'"
            raise TypeError(msg)

        copy_of_other = other._deepcopy()
        for field, field_info in cls._fields.items():
            if (new_value := copy_of_other._get_defined_attr(field)) is Undefined:
                continue
            old_value = self._get_defined_attr(field)
            if old_value == new_value or getattr(old_value, "_is_nullified", False):
                continue

            # Merge new value if it is a class.
            field_type = field_info["type"]
            if issubclass(field_type, AvdBase) and isinstance(old_value, field_type):
                # Inherit into the existing object.
                old_value._deepinherit(new_value)

            # Inherit the field only if the old value is Undefined, otherwise ignore.
            if old_value is Undefined:
                setattr(self, field, new_value)

    def _deepinherited(self: T_AvdBase, other: T_AvdBase) -> T_AvdBase:
        """Return new instance with the result of recursively inheriting unset fields from other instance. Lists are not merged."""
        new_instance = self._deepcopy()
        new_instance._deepinherit(other=other)
        return new_instance

    def _cast_as(self, new_type: type[T_AvdBase], ignore_extra_keys: bool = False) -> T_AvdBase:
        """
        Recast a class instance as another AvdBase subclass if they are compatible.

        The classes are compatible if the fields of the new class is a superset of the current class.
        Unset fields are ignored when evaluating compatibility.

        Useful when inheriting from profiles.
        """
        cls = type(self)
        if not issubclass(new_type, AvdBase):
            msg = f"Unable to cast '{cls}' as type '{new_type}' since '{new_type}' is not an AvdBase subclass."
            raise TypeError(msg)

        new_args = {}
        for field, field_info in cls._fields.items():
            if (value := self._get_defined_attr(field)) is Undefined:
                continue
            if field not in new_type._fields:
                if ignore_extra_keys:
                    continue
                msg = f"Unable to cast '{cls}' as type '{new_type}' since the field '{field}' is missing from the new class. "
                raise TypeError(msg)
            if field_info != new_type._fields[field]:
                if field_info["type"] is list and issubclass(field_info["items"], AvdBase) and isinstance(value, list):
                    # TODO: Consider using the TypeError we raise below to ensure we know the outer type.
                    # TODO: with suppress(TypeError):
                    new_args[field] = [item._cast_as(new_type._fields[field]["items"]) for item in value if isinstance(item, AvdBase)]
                    continue
                if issubclass(field_info["type"], AvdBase) and isinstance(value, AvdBase):
                    # TODO: Consider using the TypeError we raise below to ensure we know the outer type.
                    # TODO: with suppress(TypeError):
                    new_args[field] = value._cast_as(new_type._fields[field]["type"])
                    continue

                msg = f"Unable to cast '{cls}' as type '{new_type}' since the field '{field}' is incompatible. Value {value}"
                raise TypeError(msg)

            new_args[field] = value
            continue

        return new_type(**new_args)
