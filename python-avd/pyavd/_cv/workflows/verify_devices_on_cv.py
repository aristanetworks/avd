# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.inventory.v1 import StreamingStatus
from pyavd._cv.client.exceptions import CVResourceNotFound

from .models import CVDevice, DeviceInventoryResult, InternalDevice

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def verify_devices_on_cv(
    *,
    devices: list[CVDevice],
    internal_devices: list[InternalDevice],
    workspace_id: str,
    skip_missing_devices: bool,
    warnings: list[Exception],
    cv_client: CVClient,
) -> None:
    """Verify that the given Devices are already present in the CloudVision Inventory & I&T Studio."""
    LOGGER.info("verify_devices_on_cv: %s", len(devices))

    # Return if we have nothing to do.
    if not devices:
        return
    # duplicating a few logs and checks to track avd_devices
    # Return if we have nothing to do.
    if not internal_devices:
        return
    LOGGER.info("verify_devices_on_cv: avd_devices len: %s", len(internal_devices))

    existing_devices = await verify_devices_in_cloudvision_inventory(
        devices=devices, skip_missing_devices=skip_missing_devices, warnings=warnings, cv_client=cv_client
    )
    # duplicate check using internal_devices
    existing_internal_devices = await verify_devices_in_cloudvision_inventory2(
        internal_devices=internal_devices, skip_missing_devices=skip_missing_devices, warnings=warnings, cv_client=cv_client
    )

    await verify_devices_in_topology_studio(existing_devices, workspace_id, cv_client)
    # duplicate check using internal_devices for those present in CV Inventory
    await verify_devices_in_topology_studio2(existing_internal_devices, workspace_id, cv_client)


async def verify_devices_in_cloudvision_inventory(
    *,
    devices: list[CVDevice],
    skip_missing_devices: bool,
    warnings: list[Exception],
    cv_client: CVClient,
) -> list[CVDevice]:
    """
    Verify that the given Devices are already present in the CloudVision Inventory.

    Then in-place update the given objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where _exists_on_cv is already filled out on the device.

    Populate current streaming status for all existing devices.

    Returns list of CVDevice objects found on CloudVision.
    """
    # Using set to only include a device once.
    device_tuples = {
        (device.serial_number, device.system_mac_address, device.hostname if not any([device.serial_number, device.system_mac_address]) else None)
        for device in devices
        if device._exists_on_cv is None
    }
    LOGGER.info("verify_devices_in_cloudvision_inventory: %s unique devices.", len(device_tuples))

    found_devices = await cv_client.get_inventory_devices(devices=device_tuples)
    LOGGER.info("verify_devices_in_cloudvision_inventory: got %s matching devices on CV.", len(found_devices))
    found_device_dict_by_serial = {found_device.key.device_id: found_device for found_device in found_devices}
    found_device_dict_by_system_mac = {found_device.system_mac_address: found_device for found_device in found_devices}
    found_device_dict_by_hostname = {found_device.hostname: found_device for found_device in found_devices}

    existing_devices: list[CVDevice] = []
    for device in devices:
        # Use serial_number as unique ID if set.
        if device.serial_number is not None:
            if device.serial_number not in found_device_dict_by_serial:
                device._exists_on_cv = False
                continue
            device._exists_on_cv = True
            device.system_mac_address = found_device_dict_by_serial[device.serial_number].system_mac_address
            # Update streaming status
            device._streaming = found_device_dict_by_serial[device.serial_number].streaming_status == StreamingStatus.ACTIVE
            existing_devices.append(device)
            continue

        # Use system_mac_address as unique ID if set.
        if device.system_mac_address is not None:
            if device.system_mac_address not in found_device_dict_by_system_mac:
                device._exists_on_cv = False
                continue
            device._exists_on_cv = True
            device.serial_number = found_device_dict_by_system_mac[device.system_mac_address].key.device_id
            # Update streaming status
            device._streaming = found_device_dict_by_system_mac[device.system_mac_address].streaming_status == StreamingStatus.ACTIVE
            existing_devices.append(device)
            continue

        # Finally use hostname as unique ID.
        if device.hostname not in found_device_dict_by_hostname:
            device._exists_on_cv = False
            continue
        device._exists_on_cv = True
        device.serial_number = found_device_dict_by_hostname[device.hostname].key.device_id
        device.system_mac_address = found_device_dict_by_hostname[device.hostname].system_mac_address
        # Update streaming status
        device._streaming = found_device_dict_by_hostname[device.hostname].streaming_status == StreamingStatus.ACTIVE
        existing_devices.append(device)

    # Now we know which devices are on CV, so we can dig deeper and check for them in I&T Studio
    # If a device is found, we will ensure hostname is correct and if not, update the hostname.
    existing_device_tuples = {(device.serial_number, device.system_mac_address, device.hostname) for device in existing_devices}

    LOGGER.info(
        "verify_devices_in_cloudvision_inventory: %s existing device objects for %s unique devices in inventory",
        len(existing_devices),
        len(existing_device_tuples),
    )

    if missing_devices := [device for device in devices if not device._exists_on_cv]:
        warnings.append(
            missing_devices_handler(missing_devices=missing_devices, skip_missing_devices=skip_missing_devices, context="CloudVision Device Inventory")
        )

    return existing_devices


async def verify_devices_in_cloudvision_inventory2(
    *,
    internal_devices: list[InternalDevice],
    skip_missing_devices: bool,
    warnings: list[Exception],
    cv_client: CVClient,
) -> list[InternalDevice]:
    """
    Verify that the given InternalDevice objects are already present in the CloudVision Inventory.

    Then in-place update the given objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where `in_cv_inventory` is already filled out on the device.

    Returns a filtered list of InternalDevice objects found to exist on CloudVision.
    """
    # Using set to only include a device once.
    # To start with each device will have `in_cv_inventory` member set to False (by default)
    internal_device_tuples = {
        (device.serial_number, device.system_mac_address, device.avd_device.hostname if not any([device.serial_number, device.system_mac_address]) else None)
        for device in internal_devices
        if device.in_cv_inventory is False  # This conditional check may be redundant?
    }
    LOGGER.info("verify_devices_in_cloudvision_inventory2: %s unique internal devices.", len(internal_device_tuples))

    found_devices2 = await cv_client.get_inventory_devices(devices=internal_device_tuples)
    LOGGER.info("verify_devices_in_cloudvision_inventory2: got %s matching devices on CV (using internal_devices).", len(found_devices2))
    found_device_dict_by_serial2 = {found_device.key.device_id: found_device for found_device in found_devices2}
    found_device_dict_by_system_mac2 = {found_device.system_mac_address: found_device for found_device in found_devices2}
    found_device_dict_by_hostname2 = {found_device.hostname: found_device for found_device in found_devices2}

    # With revised approach of passing list of InternalDevice, given device will appear only once
    # in this list. No duplicates or revisiting given device object multiple times.
    # TODO: Revise comments below since they may no longer apply
    #
    # We may have multiple entries of in the list that point to the same CVDevice object.
    # By updating the objects in-place, we will skip duplicates by checking if _exists_on_cv was already set.
    # This also helps if the same object is used in multiple lists (like interface_tags and device_tags).

    # Iterate thru each device within internal_devices and
    # in-place update members - in_cv_inventory, serial_number and system_mac_address
    for device in internal_devices:
        if device.in_cv_inventory:
            # unlikely since we would be visiting device member only once (no duplication)
            continue
        # Use serial_number as unique ID if set.
        if device.serial_number is not None:
            if device.serial_number not in found_device_dict_by_serial2:
                device.in_cv_inventory = False  # should be already set to False (default)
                continue
            device.in_cv_inventory = True
            device.result.inventory = DeviceInventoryResult.VERIFIED
            device.system_mac_address = found_device_dict_by_serial2[device.serial_number].system_mac_address
            continue

        # Use system_mac_address as unique ID if set.
        if device.system_mac_address is not None:
            if device.system_mac_address not in found_device_dict_by_system_mac2:
                device.in_cv_inventory = False  # should be already set to False (default)
                continue
            device.in_cv_inventory = True
            device.result.inventory = DeviceInventoryResult.VERIFIED
            device.serial_number = found_device_dict_by_system_mac2[device.system_mac_address].key.device_id
            continue

        # Finally use hostname as unique ID.
        if device.avd_device.hostname not in found_device_dict_by_hostname2:
            device.in_cv_inventory = False  # should be already set to False (default)
            continue
        device.in_cv_inventory = True
        device.result.inventory = DeviceInventoryResult.VERIFIED
        device.serial_number = found_device_dict_by_hostname2[device.avd_device.hostname].key.device_id
        device.system_mac_address = found_device_dict_by_hostname2[device.avd_device.hostname].system_mac_address

    # Now we know which devices are on CV, so we can dig deeper and check for them in I&T Studio
    # If a device is found, we will ensure hostname is correct and if not, update the hostname.
    existing_internal_devices = [device for device in internal_devices if device.in_cv_inventory]
    # Using set to only include a device once.
    existing_device_tuples2 = {(device.serial_number, device.system_mac_address, device.avd_device.hostname) for device in existing_internal_devices}

    LOGGER.info(
        "verify_devices_in_cloudvision_inventory2: %s existing internal device objects for %s unique devices in inventory",
        len(existing_internal_devices),
        len(existing_device_tuples2),
    )

    if missing_devices2 := [device for device in internal_devices if not device.in_cv_inventory]:
        warnings.append(
            missing_devices_handler2(missing_devices=missing_devices2, skip_missing_devices=skip_missing_devices, context="CloudVision Device Inventory")
        )

    return existing_internal_devices


async def verify_devices_in_topology_studio(existing_devices: list[CVDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Insert and/or update given Devices in the Inventory & Topology Studio.

    Since we only get devices which are already verified to be in the inventory, we can trust the given information.

    Existing devices are updated with hostname and system mac address.
    Missing devices are added with device id, hostname, system mac address.
    """
    existing_device_tuples = {(device.serial_number, device.hostname, device.system_mac_address) for device in existing_devices}

    cv_topology_inputs = await cv_client.get_topology_studio_inputs(
        workspace_id=workspace_id,
        device_ids=list({device.serial_number for device in existing_devices}),
    )
    LOGGER.info("verify_devices_in_topology_studio: %s unique devices for %s device objects.", len(existing_device_tuples), len(existing_devices))
    LOGGER.info("verify_devices_in_topology_studio: got %s devices from I&T Studio.", len(cv_topology_inputs))
    topology_inputs_dict_by_serial = {topology_input["device_id"]: topology_input for topology_input in cv_topology_inputs}

    # List of tuples holding the info we need to update in I&T Studio
    # [(<device_id>, <hostname>, <system_mac>)]
    update_topology_inputs = []

    for serial_number, hostname, system_mac_address in existing_device_tuples:
        if serial_number not in topology_inputs_dict_by_serial or (
            hostname != topology_inputs_dict_by_serial[serial_number]["hostname"]
            or system_mac_address != topology_inputs_dict_by_serial[serial_number]["mac_address"]
        ):
            update_topology_inputs.append((serial_number, hostname, system_mac_address))

    if update_topology_inputs:
        LOGGER.info("verify_devices_in_topology_studio: need updates for %s unique devices in I&T Studio.", len(update_topology_inputs))
        await cv_client.set_topology_studio_inputs(workspace_id=workspace_id, device_inputs=update_topology_inputs)


async def verify_devices_in_topology_studio2(existing_devices: list[InternalDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Insert and/or update given Devices in the Inventory & Topology Studio.

    Since we only get devices which are already verified to be in the inventory, we can trust the given information.

    Existing devices are updated with hostname and system mac address.
    Missing devices are added with device id, hostname, system mac address.
    """
    # variation of verify_devices_in_topology_studio() that works on list[InternalDevice]
    # This list only contains devices that have `in_cv_inventory` flag set (confirmed to be present in CV Inventory)
    # Includes logic to SET `in_cv_studios` flag for device when found to be already present in CV Studios.

    existing_device_tuples = {(device.serial_number, device.avd_device.hostname, device.system_mac_address) for device in existing_devices}

    cv_topology_inputs = await cv_client.get_topology_studio_inputs(
        workspace_id=workspace_id,
        device_ids=list({device.serial_number for device in existing_devices}),
    )
    LOGGER.info("verify_devices_in_topology_studio2: %s unique devices for %s device objects.", len(existing_device_tuples), len(existing_devices))
    LOGGER.info("verify_devices_in_topology_studio2: got %s devices from I&T Studio.", len(cv_topology_inputs))
    topology_inputs_dict_by_serial = {topology_input["device_id"]: topology_input for topology_input in cv_topology_inputs}

    # List of tuples holding the info we need to update in I&T Studio
    # [(<device_id>, <hostname>, <system_mac>)]
    update_topology_inputs = []

    # for serial_number, hostname, system_mac_address in existing_device_tuples:
    for device in existing_devices:
        if device.serial_number not in topology_inputs_dict_by_serial or (
            device.avd_device.hostname != topology_inputs_dict_by_serial[device.serial_number]["hostname"]
            or device.system_mac_address != topology_inputs_dict_by_serial[device.serial_number]["mac_address"]
        ):
            update_topology_inputs.append((device.serial_number, device.avd_device.hostname, device.system_mac_address))
        else:
            # device found to be already present within CV Studio Inputs, set flag
            device.in_cv_studios = True

    if update_topology_inputs:
        LOGGER.info("verify_devices_in_topology_studio2: need updates for %s unique devices in I&T Studio.", len(update_topology_inputs))
        await cv_client.set_topology_studio_inputs(workspace_id=workspace_id, device_inputs=update_topology_inputs)


def missing_devices_handler(*, missing_devices: list[CVDevice], skip_missing_devices: bool, context: str) -> Exception:
    """
    Handle missing devices.

      - Raises if skip_missing_devices is False.
      - Return Exception if skip_missing_devices is True.
    """
    # Using set to only include a device once.
    missing_device_tuples = {(device.serial_number, device.system_mac_address, device.hostname) for device in missing_devices}
    # Notice these are new objects only used for the exception.
    unique_missing_devices = [CVDevice(hostname, serial_number, system_mac_address) for serial_number, system_mac_address, hostname in missing_device_tuples]
    LOGGER.warning(
        "verify_devices_on_cv: %s is %s missing device objects for %s unique missing devices: %s",
        context,
        len(missing_devices),
        len(missing_device_tuples),
        unique_missing_devices,
    )
    exception = CVResourceNotFound("Missing devices on CloudVision", *unique_missing_devices)
    if not skip_missing_devices:
        raise exception

    return exception


def missing_devices_handler2(*, missing_devices: list[InternalDevice], skip_missing_devices: bool, context: str) -> Exception:
    """
    Handle missing devices.

      - Raises if skip_missing_devices is False.
      - Return Exception if skip_missing_devices is True.
    """
    # variation that handles list of InternalDevice for generating warning/exception as per input
    # Using set to only include a device once.
    missing_device_tuples = {(device.serial_number, device.system_mac_address, device.avd_device.hostname) for device in missing_devices}
    # Notice these are new objects only used for the exception.
    # device.result.inventory is already set to DeviceInventoryResult.MISSING as initial state (no change needed for missing devices)
    unique_missing_devices = [CVDevice(hostname, serial_number, system_mac_address) for serial_number, system_mac_address, hostname in missing_device_tuples]
    LOGGER.warning(
        "verify_devices_on_cv: %s is %s missing device objects for %s unique missing devices: %s",
        context,
        len(missing_devices),
        len(missing_device_tuples),
        unique_missing_devices,
    )
    exception = CVResourceNotFound("Missing devices on CloudVision", *unique_missing_devices)
    if not skip_missing_devices:
        raise exception

    return exception
