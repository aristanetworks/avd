# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.inventory.v1 import StreamingStatus
from pyavd._cv.client.exceptions import CVResourceNotFound

from .models import CVDevice, WorkflowDevice

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def verify_devices_on_cv(
    *,
    workflow_devices: list[WorkflowDevice],
    workspace_id: str,
    skip_missing_devices: bool,
    warnings: list[Exception],
    cv_client: CVClient,
) -> None:
    """Verify that the given devices are already present in the CloudVision Inventory & I&T Studio."""
    LOGGER.info("verify_devices_on_cv: %s devices representing workflow", len(workflow_devices))

    # Return if we have nothing to do.
    if not workflow_devices:
        return

    existing_devices = await verify_devices_in_cloudvision_inventory(
        workflow_devices=workflow_devices, skip_missing_devices=skip_missing_devices, warnings=warnings, cv_client=cv_client
    )

    await verify_devices_in_topology_studio(existing_devices, workspace_id, cv_client)


async def verify_devices_in_cloudvision_inventory(
    *,
    workflow_devices: list[WorkflowDevice],
    skip_missing_devices: bool,
    warnings: list[Exception],
    cv_client: CVClient,
) -> list[WorkflowDevice]:
    """
    Verify that the given devices are already present in the CloudVision Inventory.

    Then in-place update the given objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where `in_cv_inventory` is already filled out on the device.

    Populate current streaming status for all existing devices.

    Returns filtered list of WorkflowDevice objects found in CloudVision.
    """
    # Using set to only include a device once.
    # Each device will have in_cv_inventory member set to False initially until it is reviewed.
    device_tuples = {
        (
            device.input.serial_number,
            device.input.system_mac_address,
            device.input.hostname if not any([device.input.serial_number, device.input.system_mac_address]) else None,
        )
        for device in workflow_devices
    }
    LOGGER.info("verify_devices_in_cloudvision_inventory: %s unique devices.", len(device_tuples))
    found_devices = await cv_client.get_inventory_devices(devices=device_tuples)
    LOGGER.info("verify_devices_in_cloudvision_inventory: got %s matching devices on CV.", len(found_devices))
    found_device_dict_by_serial = {found_device.key.device_id: found_device for found_device in found_devices}
    found_device_dict_by_system_mac = {found_device.system_mac_address: found_device for found_device in found_devices}
    found_device_dict_by_hostname = {found_device.hostname: found_device for found_device in found_devices}

    # Iterate thru each device and in-place update members such as in_cv_inventory, serial_number and system_mac_address.
    # Also update result placeholder with serial number,system mac address derived from CV Inventory.
    missing_devices: list[WorkflowDevice] = []
    existing_devices: list[WorkflowDevice] = []
    for device in workflow_devices:
        # Use serial_number as unique ID if set.
        if device.input.serial_number is not None:
            if device.input.serial_number not in found_device_dict_by_serial:
                device.in_cv_inventory = False  # should be already set to False (default)
                missing_devices.append(device)
                continue
            device.in_cv_inventory = True
            device.serial_number = device.input.serial_number
            device.system_mac_address = found_device_dict_by_serial[device.serial_number].system_mac_address
            # Update streaming status
            device.streaming = found_device_dict_by_serial[device.serial_number].streaming_status == StreamingStatus.ACTIVE
            existing_devices.append(device)
            continue

        # Use system_mac_address as unique ID if set.
        if device.input.system_mac_address is not None:
            if device.input.system_mac_address not in found_device_dict_by_system_mac:
                device.in_cv_inventory = False  # should be already set to False (default)
                missing_devices.append(device)
                continue
            device.in_cv_inventory = True
            device.system_mac_address = device.input.system_mac_address
            device.serial_number = found_device_dict_by_system_mac[device.system_mac_address].key.device_id
            # Update streaming status
            device.streaming = found_device_dict_by_system_mac[device.system_mac_address].streaming_status == StreamingStatus.ACTIVE
            existing_devices.append(device)
            continue

        # Finally use hostname as unique ID.
        if device.input.hostname not in found_device_dict_by_hostname:
            device.in_cv_inventory = False  # should be already set to False (default)
            missing_devices.append(device)
            continue
        device.in_cv_inventory = True
        device.serial_number = found_device_dict_by_hostname[device.input.hostname].key.device_id
        device.system_mac_address = found_device_dict_by_hostname[device.input.hostname].system_mac_address
        # Update streaming status
        device.streaming = found_device_dict_by_hostname[device.input.hostname].streaming_status == StreamingStatus.ACTIVE
        existing_devices.append(device)

    # Now we know which devices are on CV, so we can dig deeper and check for them in I&T Studio
    # If a device is found, we will ensure hostname is correct and if not, update the hostname.
    # Using set to only include a device once.
    existing_device_tuples = {(device.serial_number, device.system_mac_address, device.input.hostname) for device in existing_devices}

    LOGGER.info(
        "verify_devices_in_cloudvision_inventory: %s device objects for %s unique devices in inventory",
        len(existing_devices),
        len(existing_device_tuples),
    )

    if missing_devices:
        warnings.append(
            missing_devices_handler(missing_devices=missing_devices, skip_missing_devices=skip_missing_devices, context="CloudVision Device Inventory")
        )

    return existing_devices


async def verify_devices_in_topology_studio(existing_devices: list[WorkflowDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Insert and/or update given Devices in the Inventory & Topology Studio.

    Since we only get devices which are already verified to be in the inventory, we can trust the given information.

    Existing devices are updated with hostname and system mac address.
    Missing devices are added with device id, hostname, system mac address.
    """
    existing_device_tuples = {(device.serial_number, device.input.hostname, device.system_mac_address) for device in existing_devices}

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

    update_topology_inputs = [
        (device.serial_number, device.input.hostname, device.system_mac_address)
        for device in existing_devices
        if device.serial_number not in topology_inputs_dict_by_serial
        or (
            device.input.hostname != topology_inputs_dict_by_serial[device.serial_number]["hostname"]
            or device.system_mac_address != topology_inputs_dict_by_serial[device.serial_number]["mac_address"]
        )
    ]

    if update_topology_inputs:
        LOGGER.info("verify_devices_in_topology_studio: need updates for %s unique devices in I&T Studio.", len(update_topology_inputs))
        await cv_client.set_topology_studio_inputs(workspace_id=workspace_id, device_inputs=update_topology_inputs)


def missing_devices_handler(*, missing_devices: list[WorkflowDevice], skip_missing_devices: bool, context: str) -> Exception:
    """
    Handle missing devices.

      - Raises if skip_missing_devices is False.
      - Return Exception if skip_missing_devices is True.
    """
    # Using set to only include a device once.
    missing_device_tuples = {(device.serial_number, device.system_mac_address, device.input.hostname) for device in missing_devices}
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
