# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from dataclasses import dataclass
from typing import Literal

from typing_extensions import Self

from pyavd._cv.api.arista.tag.v2 import ElementType, Tag, TagAssignment

STRING_TO_ELEMENT_TYPE_MAP = {
    "device": ElementType.DEVICE,
    "interface": ElementType.INTERFACE,
    "unspecified": ElementType.UNSPECIFIED,
}

ELEMENT_TYPE_TO_STRING_MAP = {
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
        element_type = ELEMENT_TYPE_TO_STRING_MAP.get(tag.key.element_type, "unspecified")

        return cls(
            element_type=element_type,
            label=tag.key.label,
            value=tag.key.value,
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
        interface_id = str(tag_assignment.key.interface_id).rsplit("@", maxsplit=1)[0] if tag_assignment.key.interface_id is not None else None

        element_type = ELEMENT_TYPE_TO_STRING_MAP.get(tag_assignment.key.element_type, "unspecified")

        return cls(
            element_type=element_type,
            label=tag_assignment.key.label,
            value=tag_assignment.key.value,
            device_id=tag_assignment.key.device_id,
            interface_id=interface_id,
        )
