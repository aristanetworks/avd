# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from dataclasses import dataclass
from typing import Literal, TypeVar, cast, overload

from typing_extensions import Self

from pyavd._cv.api.arista.tag.v2 import ElementType, Tag, TagAssignment

from .exceptions import CVIncompleteObjectError

T = TypeVar("T")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
T3 = TypeVar("T3")
T4 = TypeVar("T4")

STRING_TO_ELEMENT_TYPE_MAP = {
    "device": ElementType.DEVICE,
    "interface": ElementType.INTERFACE,
    "unspecified": ElementType.UNSPECIFIED,
}

ELEMENT_TYPE_TO_STRING_MAP: dict[ElementType, Literal["device", "interface", "unspecified"]] = {
    ElementType.DEVICE: "device",
    ElementType.INTERFACE: "interface",
    ElementType.UNSPECIFIED: "unspecified",
}


@dataclass(frozen=True)
class CVTag:
    """Represent the input model for a CloudVision Tag."""

    element_type: Literal["device", "interface", "unspecified"]
    """The type of network element the tag applies to."""
    label: str
    """The label of the tag."""
    value: str
    """The value of the tag."""

    def get_element_type(self) -> ElementType:
        """Get the API ElementType object from this CVTag instance."""
        return STRING_TO_ELEMENT_TYPE_MAP.get(self.element_type, ElementType.UNSPECIFIED)

    @classmethod
    def from_api(cls, tag: Tag) -> Self:
        """Create a CVTag from a raw API Tag object."""
        key = get_required_field(tag, "key", tag.key)
        label, value = get_required_fields(key, ("label", "value"), (key.label, key.value))
        element_type = ELEMENT_TYPE_TO_STRING_MAP.get(key.element_type, "unspecified")

        return cls(
            element_type=element_type,
            label=label,
            value=value,
        )


@dataclass(frozen=True)
class CVTagAssignment:
    """Represent the input model for a CloudVision Tag Assignment."""

    element_type: Literal["device", "interface", "unspecified"]
    """The type of network element the tag is assigned to."""
    label: str
    """The label of the tag."""
    value: str
    """The value of the tag."""
    device_id: str
    """The serial number of the device for the assignment."""
    interface_id: str | None = None
    """The name of the interface for interface assignments."""

    def get_element_type(self) -> ElementType:
        """Get the API ElementType object from this CVTagAssignment instance."""
        return STRING_TO_ELEMENT_TYPE_MAP.get(self.element_type, ElementType.UNSPECIFIED)

    @classmethod
    def from_api(cls, tag_assignment: TagAssignment) -> Self:
        """Create a CVTagAssignment from a raw API TagAssignment object."""
        # The API may return a complex interface ID like 'Ethernet1@<serial>', so we parse it to get just the interface name.
        key = get_required_field(tag_assignment, "key", tag_assignment.key)
        label, value, device_id = get_required_fields(key, ("label", "value", "device_id"), (key.label, key.value, key.device_id))
        element_type = ELEMENT_TYPE_TO_STRING_MAP[key.element_type]
        interface_id = key.interface_id.rsplit("@", maxsplit=1)[0] if key.interface_id is not None else None

        return cls(
            element_type=element_type,
            label=label,
            value=value,
            device_id=device_id,
            interface_id=interface_id,
        )


def get_required_field(cv_object: object, required_field: str, value: T | None) -> T:
    """
    Return a presence-guaranteed property from a CV API object.

    This only narrows fields from optional to present. It does not validate
    runtime types, since those are guaranteed by gRPC decoding.

    Raises:
        CVIncompleteObjectError: If the required field is missing.
    """
    if value is None:
        raise CVIncompleteObjectError(cv_object_type=cv_object.__class__.__name__, missing_fields=(required_field,))
    return value


@overload
def get_required_fields(cv_object: object, required_fields: tuple[str], values: tuple[T1 | None]) -> tuple[T1]: ...


@overload
def get_required_fields(cv_object: object, required_fields: tuple[str, str], values: tuple[T1 | None, T2 | None]) -> tuple[T1, T2]: ...


@overload
def get_required_fields(
    cv_object: object,
    required_fields: tuple[str, str, str],
    values: tuple[T1 | None, T2 | None, T3 | None],
) -> tuple[T1, T2, T3]: ...


@overload
def get_required_fields(
    cv_object: object,
    required_fields: tuple[str, str, str, str],
    values: tuple[T1 | None, T2 | None, T3 | None, T4 | None],
) -> tuple[T1, T2, T3, T4]: ...


def get_required_fields(cv_object: object, required_fields: tuple[str, ...], values: tuple[object | None, ...]) -> tuple[object, ...]:
    """
    Return presence-guaranteed properties from a CV API object.

    This only narrows fields from optional to present. It does not validate
    runtime types, since those are guaranteed by gRPC decoding.

    Raises:
        CVIncompleteObjectError: If any required fields are missing.
    """
    missing_fields = tuple(required_field for required_field, value in zip(required_fields, values, strict=True) if value is None)

    if missing_fields:
        raise CVIncompleteObjectError(
            cv_object_type=cv_object.__class__.__name__,
            missing_fields=missing_fields,
        )

    return cast("tuple[object, ...]", values)
