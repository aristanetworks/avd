# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.exceptions import CVDuplicatedDevices
from pyavd._utils import groupby_obj

from .models import DuplicatedDevices

if TYPE_CHECKING:
    from .models import CVDevice

LOGGER = getLogger(__name__)


def verify_device_inputs(devices: list[CVDevice], warnings: list[Exception], *, strict_system_mac_address: bool) -> None:
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

    # Deduplicate CVDevice objects as original `devices` list may contain duplicated items
    unique_devices = list({id(device): device for device in devices}.values())

    # Group devices based on <CVDevice>.serial_number as long as it's not None
    devices_grouped_by_serial_number = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.serial_number is not None], attr="serial_number", skip_singles=True
    )

    # Group devices based on <CVDevice>.system_mac_address as long as it's not None
    devices_grouped_by_system_mac_address = groupby_obj(
        list_of_objects=[device for device in unique_devices if device.system_mac_address is not None], attr="system_mac_address", skip_singles=True
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


def duplicated_devices_handler(
    duplicated_devices: DuplicatedDevices,
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
