# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVDuplicatedDevices
from pyavd._utils import groupby_obj

from .models import (
    AvdDeviceTag,
    AvdDuplicatedDevices,
    AvdEosConfig,
    AvdInterfaceTag,
    AvdPathfinderMetadata,
    DeviceInventoryResult,
    DeviceResult,
    DuplicatedDevices,
    InternalDevice,
    MiscComponentResult,
    Tags,
    TagsResult,
)

if TYPE_CHECKING:
    from .models import AvdDevice, CVDevice

LOGGER = getLogger(__name__)


def verify_device_inputs(devices: list[CVDevice], avd_devices: list[AvdDevice] | None, warnings: list[Exception], *, strict_system_mac_address: bool) -> None:
    """
    Verify device inputs from structured config files.

    Check for presence of the duplicated `serial_number` or `system_mac_address` values.
    Raise an exception and terminate execution if:
      - two or more devices have the same `serial_number` (values of `system_mac_address` are not important in this case)
      - two or more devices have the same `system_mac_address` and at least one of these devices has an unset `serial_number` value
      - two or more targeted devices have the same `system_mac_address`, unique `serial_number` and `strict_system_mac_address` is `True`
    Warn user (with log message and updated `cv_deploy_results.warnings`) if:
      - two or more targeted devices have the same `system_mac_address`, unique `serial_number` and `strict_system_mac_address` is `False`
    """
    if avd_devices and (duplicated_devices := identify_duplicated_avd_devices(avd_devices)).detected():
        duplicated_devices_handler(
            duplicated_devices,
            warnings,
            strict_system_mac_address=strict_system_mac_address,
        )
    if (duplicated_devices := identify_duplicated_devices(devices)).detected():
        duplicated_devices_handler(
            duplicated_devices,
            warnings,
            strict_system_mac_address=strict_system_mac_address,
        )


def identify_duplicated_devices(devices: list[CVDevice]) -> DuplicatedDevices:
    """
    Process list of CVDevice instances to identify those with overlapping serial_number or system_mac_address.

    Return DuplicatedDevices object containing:
      - Information about CVDevices with overlapping serial_number.
      - Information about CVDevices with overlapping system_mac_address where at least one of these devices has an unset `serial_number` value.
      - Information about CVDevices with overlapping system_mac_address and set serial_number.
    """
    duplicated_devices = DuplicatedDevices()

    # Group devices based on <CVDevice>.serial_number as long as it's not None
    devices_grouped_by_serial_number = groupby_obj(
        list_of_objects=[device for device in devices if device.serial_number is not None], attr="serial_number", skip_singles=True
    )

    # Group devices based on <CVDevice>.system_mac_address as long as it's not None
    devices_grouped_by_system_mac_address = groupby_obj(
        list_of_objects=[device for device in devices if device.system_mac_address is not None], attr="system_mac_address", skip_singles=True
    )

    # Populate list of CVDevice with duplicated serial_number values
    for current_serial_number, device_iterator_object in devices_grouped_by_serial_number:
        duplicated_devices.serial_number[current_serial_number] = list(device_iterator_object)

    # Populate list of CVDevice with duplicated system_mac_address values
    for current_system_mac_address, device_iterator_object in devices_grouped_by_system_mac_address:
        devices_with_current_system_mac_address = list(device_iterator_object)
        # Safe case where all devices with duplicated current_system_mac_address have a serial_number set
        if all(device.serial_number for device in devices_with_current_system_mac_address):
            duplicated_devices.system_mac_address.set_serial_number[current_system_mac_address] = devices_with_current_system_mac_address
        # Unsafe case where at least one device among those with the same duplicated current_system_mac_address does not have a serial_number set
        else:
            duplicated_devices.system_mac_address.unset_or_mixed_serial_number[current_system_mac_address] = devices_with_current_system_mac_address

    return duplicated_devices


def identify_duplicated_avd_devices(devices: list[AvdDevice]) -> AvdDuplicatedDevices:
    """
    Process list of AvdDevice instances to identify those with overlapping serial_number or system_mac_address.

    Return DuplicatedDevices object containing:
      - Information about AvdDevice with overlapping serial_number.
      - Information about AvdDevice with overlapping system_mac_address where at least one of these devices has an unset `serial_number` value.
      - Information about AvdDevice with overlapping system_mac_address and set serial_number.
    """
    duplicated_devices = AvdDuplicatedDevices()

    # Check if deduplication needed when working on list[AvdDevice]?
    unique_devices = list({id(device): device for device in devices}.values())
    LOGGER.debug("identify_duplicated_avd_devices() avd_devices: len %s unique_devices: len %s", len(devices), len(unique_devices))

    # Group devices based on <AvdDevice>.serial_number as long as it's not None
    devices_grouped_by_serial_number = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.serial_number is not None], attr="serial_number", skip_singles=True
    )

    # Group devices based on <AvdDevice>.system_mac_address as long as it's not None
    devices_grouped_by_system_mac_address = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.system_mac_address is not None], attr="system_mac_address", skip_singles=True
    )

    # Populate list of AvdDevice with duplicated serial_number values
    for current_serial_number, device_iterator_object in devices_grouped_by_serial_number:
        LOGGER.debug("identify_duplicated_avd_devices() serial_number: %s has more than one device associated", current_serial_number)
        duplicated_devices.serial_number[current_serial_number] = list(device_iterator_object)

    # Populate list of AvdDevice with duplicated system_mac_address values
    for current_system_mac_address, device_iterator_object in devices_grouped_by_system_mac_address:
        devices_with_current_system_mac_address = list(device_iterator_object)
        # Safe case where all devices with duplicated current_system_mac_address have a serial_number set
        if all(device.serial_number for device in devices_with_current_system_mac_address):
            LOGGER.debug(
                "identify_duplicated_avd_devices() system_mac_address: %s has more than one device associated with serial number set",
                current_system_mac_address,
            )
            duplicated_devices.system_mac_address.set_serial_number[current_system_mac_address] = devices_with_current_system_mac_address
        # Unsafe case where at least one device among those with the same duplicated current_system_mac_address does not have a serial_number set
        else:
            LOGGER.debug(
                "identify_duplicated_avd_devices() system_mac_address: %s has more than one device associated with serial number unset",
                current_system_mac_address,
            )
            duplicated_devices.system_mac_address.unset_or_mixed_serial_number[current_system_mac_address] = devices_with_current_system_mac_address

    return duplicated_devices


def duplicated_devices_handler(
    duplicated_devices: DuplicatedDevices | AvdDuplicatedDevices,
    warnings: list[Exception],
    *,
    strict_system_mac_address: bool,
) -> None:
    """
    Handle input devices with duplicated `serial_number`s or `system_mac_address`es.

    Raise an exception if (match-any):
        - duplicated_devices.serial_number is not empty
        - duplicated_devices.system_mac_address.unset_or_mixed_serial_number is not empty
        - duplicated_devices.system_mac_address.set_serial_number is not empty and strict_system_mac_address set to True
    Raise warning if (match-any):
        - duplicated_devices.system_mac_address.set_serial_number is not empty and strict_system_mac_address set to False
    """
    # For now allow this handler to work on both DuplicatedDevices, AvdDuplicatedDevices till we converge
    if (
        duplicated_devices.serial_number
        or duplicated_devices.system_mac_address.unset_or_mixed_serial_number
        or (duplicated_devices.system_mac_address.set_serial_number and strict_system_mac_address)
    ):
        exception = CVDuplicatedDevices(
            "Duplicated devices found in inventory",
            *[
                item
                for item in (
                    duplicated_devices.serial_number,
                    duplicated_devices.system_mac_address.unset_or_mixed_serial_number,
                    duplicated_devices.system_mac_address.set_serial_number if strict_system_mac_address else None,
                )
                if item
            ],
        )
        raise exception

    LOGGER.warning(
        "verify_inputs: Devices with duplicated system_mac_address and unique serial_number discovered in inventory (structured config): %s",
        duplicated_devices.system_mac_address.set_serial_number,
    )
    warnings.append(CVDuplicatedDevices("Duplicated devices found in inventory", duplicated_devices.system_mac_address.set_serial_number))


def build_internal_device_inputs(avd_devices: list[AvdDevice] | None) -> list[InternalDevice]:
    """
    Build list of InternalDevice objects from specified list of AvdDevice.

    Subsequent wrappers to in-place update InternalDevice object as they work on each device.
    """
    internal_devices: list[InternalDevice] = []
    if not avd_devices:
        return internal_devices
    for avd_device in avd_devices:
        # Device result members are initialized with respective members with empty values.
        # This will make it easier for subsequent wrappers to access and update these members.
        device_result = DeviceResult(
            inventory=DeviceInventoryResult.MISSING,
            device_tags=TagsResult[AvdDeviceTag](),
            interface_tags=TagsResult[AvdInterfaceTag](),
            config=MiscComponentResult[AvdEosConfig](),
            pathfinder_metadata=MiscComponentResult[AvdPathfinderMetadata](),
        )

        # serial_number, system_mac_address members of InternalDevice set to None (by default)
        # These will be populated with revised values upon querying CV Inventory.
        # device_tags, interface_tags are initialized with empty values.
        # Subsequent wrappers working on InternalDevice object would be able to update these easily.
        curr_internal_device = InternalDevice(
            avd_device=avd_device, result=device_result, device_tags=Tags[AvdDeviceTag](), interface_tags=Tags[AvdInterfaceTag]()
        )
        internal_devices.append(curr_internal_device)
    return internal_devices
