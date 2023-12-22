# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger

from ..client import CVClient
from ..client.exceptions import CVResourceNotFound
from .models import CVDevice

LOGGER = getLogger(__name__)


async def verify_devices_on_cv(devices: list[CVDevice], workspace_id: str, skip_missing_devices: bool, warnings: list, cv_client: CVClient) -> None:
    """
    Verify that the given Devices are already present on CloudVision
    and in-place update the given objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where _exists_on_cv is already filled out on the device.

    Raises if skip_missing_devices is False. In-place appends to warnings if skip_missing_devices is True.

    TODO: Check for duplicate serial_numbers or system_mac_addresses in the input devices list.
    """
    LOGGER.info("verify_devices_on_cv: %s", len(devices))

    # Return if we have nothing to do.
    if not devices:
        return

    # Using set to only include a device once.
    device_tuples = set(
        (device.serial_number, device.system_mac_address, device.hostname if not any([device.serial_number, device.system_mac_address]) else None)
        for device in devices
        if device._exists_on_cv is None
    )
    found_devices = await cv_client.get_inventory_devices(devices=device_tuples)
    LOGGER.info("verify_devices_on_cv: got %s maching devices on CV.", len(found_devices))
    found_device_dict_by_serial = {found_device.key.device_id: found_device for found_device in found_devices}
    found_device_dict_by_system_mac = {found_device.system_mac_address: found_device for found_device in found_devices}
    found_device_dict_by_hostname = {found_device.hostname: found_device for found_device in found_devices}

    # We may have multiple entries of in the list that point to the same CVDevice object.
    # By updating the objects in-place, we will skip duplicates by checking if _exists_on_cv was already set.
    # This also helps if the same object is used in multiple lists (like interface_tags and device_tags).
    for device in devices:
        if device._exists_on_cv is not None:
            continue
        # Use serial_number as unique ID if set.
        if device.serial_number is not None:
            if device.serial_number not in found_device_dict_by_serial:
                device._exists_on_cv = False
                continue
            device._exists_on_cv = True
            device.system_mac_address = found_device_dict_by_serial[device.serial_number].system_mac_address
            continue

        # Use system_mac_address as unique ID if set.
        if device.system_mac_address is not None:
            if device.system_mac_address not in found_device_dict_by_system_mac:
                device._exists_on_cv = False
                continue
            device._exists_on_cv = True
            device.serial_number = found_device_dict_by_system_mac[device.system_mac_address].key.device_id
            continue

        # Finally use hostname as unique ID.
        if device.hostname not in found_device_dict_by_hostname:
            device._exists_on_cv = False
            continue
        device._exists_on_cv = True
        device.serial_number = found_device_dict_by_hostname[device.hostname].key.device_id
        device.system_mac_address = found_device_dict_by_hostname[device.hostname].system_mac_address

    # Now we know which devices are on CV, so we can dig deeper and check for them in I&T Studio
    # If a device is found, we will ensure hostname is correct and if not, update the hostname.
    # If a device is not found, we will set _exist_on_cv back to False.
    existing_devices = [device for device in devices if device._exists_on_cv]
    LOGGER.info("verify_devices_on_cv: %s existing devices in inventory", len(existing_devices))

    cv_topology_inputs = await cv_client.get_topology_studio_inputs(
        workspace_id=workspace_id,
        device_ids=[device.serial_number for device in existing_devices],
    )
    LOGGER.info("verify_devices_on_cv: got %s devices from I&T Studio.", len(cv_topology_inputs))
    topology_inputs_dict_by_serial = {topology_input.key.device_id: topology_input for topology_input in cv_topology_inputs}

    # List of tuples holding the info we need to update in I&T Studio
    # [(<device_id>, <hostname>)]
    update_topology_inputs = []

    for device in existing_devices:
        if device.serial_number not in topology_inputs_dict_by_serial:
            device._exists_on_cv = False
            continue
            # TODO: Onboard the device to I&T since we know we have it on CV.

        if device.hostname != topology_inputs_dict_by_serial[device.serial_number].device_info.hostname:
            update_topology_inputs.append((device.serial_number, device.hostname))

    LOGGER.info("verify_devices_on_cv: need hostname updates for %s devices in I&T Studio.", len(update_topology_inputs))
    if update_topology_inputs:
        await cv_client.set_topology_studio_inputs(workspace_id=workspace_id, device_inputs=update_topology_inputs)

    if missing_devices := [device for device in devices if not device._exists_on_cv]:
        LOGGER.warning("verify_devices_on_cv: %s missing devices: %s", len(missing_devices), missing_devices)
        error = CVResourceNotFound("Missing devices on CloudVision", *missing_devices)
        if not skip_missing_devices:
            raise error
        warnings.append(error)
