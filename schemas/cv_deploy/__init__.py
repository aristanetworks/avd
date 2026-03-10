# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel

if TYPE_CHECKING:
    from pyavd._utils import Undefined, UndefinedType


class CvDeploy(AvdModel):
    """Subclass of AvdModel."""

    class CvDeviceTagsItem(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {"name": {"type": str}, "value": {"type": str}}
        name: str
        value: str

        if TYPE_CHECKING:

            def __init__(self, *, name: str | UndefinedType = Undefined, value: str | UndefinedType = Undefined) -> None:
                """
                CvDeviceTagsItem.

                Subclass of AvdModel.

                Args:
                    name: name
                    value: value

                """

    class CvDeviceTags(AvdList[CvDeviceTagsItem]):
        """Subclass of AvdList with `CvDeviceTagsItem` items."""

    CvDeviceTags._item_type = CvDeviceTagsItem

    class CvInterfaceTagsItem(AvdModel):
        """Subclass of AvdModel."""

        class TagsItem(AvdModel):
            """Subclass of AvdModel."""

            _fields: ClassVar[dict] = {"name": {"type": str}, "value": {"type": str}}
            name: str
            value: str

            if TYPE_CHECKING:

                def __init__(self, *, name: str | UndefinedType = Undefined, value: str | UndefinedType = Undefined) -> None:
                    """
                    TagsItem.

                    Subclass of AvdModel.

                    Args:
                        name: name
                        value: value

                    """

        class Tags(AvdList[TagsItem]):
            """Subclass of AvdList with `TagsItem` items."""

        Tags._item_type = TagsItem

        _fields: ClassVar[dict] = {"interface": {"type": str}, "tags": {"type": Tags}}
        interface: str
        tags: Tags
        """Subclass of AvdList with `TagsItem` items."""

        if TYPE_CHECKING:

            def __init__(self, *, interface: str | UndefinedType = Undefined, tags: Tags | UndefinedType = Undefined) -> None:
                """
                CvInterfaceTagsItem.

                Subclass of AvdModel.

                Args:
                    interface: interface
                    tags: Subclass of AvdList with `TagsItem` items.

                """

    class CvInterfaceTags(AvdList[CvInterfaceTagsItem]):
        """Subclass of AvdList with `CvInterfaceTagsItem` items."""

    CvInterfaceTags._item_type = CvInterfaceTagsItem

    class Metadata(AvdModel):
        """Subclass of AvdModel."""

        _fields: ClassVar[dict] = {
            "is_deployed": {"type": bool},
            "serial_number": {"type": str},
            "system_mac_address": {"type": str},
            "cv_tags": {"type": EosCliConfigGen.Metadata.CvTags},
            "cv_pathfinder": {"type": EosCliConfigGen.Metadata.CvPathfinder},
        }
        _allow_other_keys: ClassVar[bool] = True
        is_deployed: bool | None
        """Key only used for documentation or validation purposes."""
        serial_number: str | None
        """
        Serial Number of the device.
        Used only for documentation and deployment purposes. It is used by the
        'cv_deploy' role.
        """
        system_mac_address: str | None
        cv_tags: EosCliConfigGen.Metadata.CvTags
        cv_pathfinder: EosCliConfigGen.Metadata.CvPathfinder
        """Metadata used for CV Pathfinder visualization on CloudVision."""

        if TYPE_CHECKING:

            def __init__(
                self,
                *,
                is_deployed: bool | None | UndefinedType = Undefined,
                serial_number: str | None | UndefinedType = Undefined,
                system_mac_address: str | None | UndefinedType = Undefined,
                cv_tags: EosCliConfigGen.Metadata.CvTags | UndefinedType = Undefined,
                cv_pathfinder: EosCliConfigGen.Metadata.CvPathfinder | UndefinedType = Undefined,
            ) -> None:
                """
                Metadata.

                Subclass of AvdModel.

                Args:
                    is_deployed: Key only used for documentation or validation purposes.
                    serial_number:
                       Serial Number of the device.
                       Used only for documentation and deployment purposes. It is used by the
                       'cv_deploy' role.
                    system_mac_address: system_mac_address
                    cv_tags: cv_tags
                    cv_pathfinder: Metadata used for CV Pathfinder visualization on CloudVision.

                """

    _fields: ClassVar[dict] = {
        "is_deployed": {"type": bool, "default": True},
        "serial_number": {"type": str},
        "system_mac_address": {"type": str},
        "cv_device_tags": {"type": CvDeviceTags},
        "cv_interface_tags": {"type": CvInterfaceTags},
        "cv_pathfinder_metadata": {"type": EosCliConfigGen.Metadata.CvPathfinder},
        "metadata": {"type": Metadata},
    }
    _allow_other_keys: ClassVar[bool] = True
    is_deployed: bool
    """
    When set to `false`, the device will be skipped from all operations performed by the `cv_deploy`
    role.

    Default value: `True`
    """
    serial_number: str | None
    """
    Serial number of the device used to identify the device in CloudVision.
    Takes precedence over
    `system_mac_address` and `inventory_hostname`.

    Device identification precedence:
      1.
    `serial_number` (highest priority)
      2. `system_mac_address`
      3. `inventory_hostname` (lowest
    priority, used only if neither of the above is set)
    """
    system_mac_address: str | None
    """
    System MAC address of the device used to identify the device in CloudVision.
    Should match the MAC
    address shown in "show version" on the device.
    Used when `serial_number` is not set.

    Device
    identification precedence:
      1. `serial_number` (highest priority)
      2. `system_mac_address`
      3.
    `inventory_hostname` (lowest priority, used only if neither of the above is set)
    """
    cv_device_tags: CvDeviceTags
    """
    List of CloudVision device tags to be assigned to this device.

    Subclass of AvdList with
    `CvDeviceTagsItem` items.
    """
    cv_interface_tags: CvInterfaceTags
    """
    List of CloudVision interface tags to be assigned to interfaces on this device.

    Subclass of AvdList
    with `CvInterfaceTagsItem` items.
    """
    cv_pathfinder_metadata: EosCliConfigGen.Metadata.CvPathfinder
    """Metadata used for CV Pathfinder visualization on CloudVision."""
    metadata: Metadata
    """Subclass of AvdModel."""

    if TYPE_CHECKING:

        def __init__(
            self,
            *,
            is_deployed: bool | UndefinedType = Undefined,
            serial_number: str | None | UndefinedType = Undefined,
            system_mac_address: str | None | UndefinedType = Undefined,
            cv_device_tags: CvDeviceTags | UndefinedType = Undefined,
            cv_interface_tags: CvInterfaceTags | UndefinedType = Undefined,
            cv_pathfinder_metadata: EosCliConfigGen.Metadata.CvPathfinder | UndefinedType = Undefined,
            metadata: Metadata | UndefinedType = Undefined,
        ) -> None:
            """
            CvDeploy.

            Subclass of AvdModel.

            Args:
                is_deployed:
                   When set to `false`, the device will be skipped from all operations performed by the `cv_deploy`
                   role.
                serial_number:
                   Serial number of the device used to identify the device in CloudVision.
                   Takes precedence over
                   `system_mac_address` and `inventory_hostname`.

                   Device identification precedence:
                     1.
                   `serial_number` (highest priority)
                     2. `system_mac_address`
                     3. `inventory_hostname` (lowest
                   priority, used only if neither of the above is set)
                system_mac_address:
                   System MAC address of the device used to identify the device in CloudVision.
                   Should match the MAC
                   address shown in "show version" on the device.
                   Used when `serial_number` is not set.

                   Device
                   identification precedence:
                     1. `serial_number` (highest priority)
                     2. `system_mac_address`
                     3.
                   `inventory_hostname` (lowest priority, used only if neither of the above is set)
                cv_device_tags:
                   List of CloudVision device tags to be assigned to this device.

                   Subclass of AvdList with
                   `CvDeviceTagsItem` items.
                cv_interface_tags:
                   List of CloudVision interface tags to be assigned to interfaces on this device.

                   Subclass of AvdList
                   with `CvInterfaceTagsItem` items.
                cv_pathfinder_metadata: Metadata used for CV Pathfinder visualization on CloudVision.
                metadata: Subclass of AvdModel.

            """
