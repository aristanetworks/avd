# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger

from ..api.arista.inventory.v1 import Device  # , DeviceKey
from ..client import CVClient
from ..client.exceptions import CVDuplicateInfo, CVResourceNotFound
from .models import CVDevice

LOGGER = getLogger(__name__)


# XXX: check dups on inventory and error out
async def verify_devices_on_cv(devices: list[CVDevice], workspace_id: str, skip_missing_devices: bool, warnings: list[Exception], cv_client: CVClient) -> None:
    """
    Verify that the given Devices are already present in the CloudVision Inventory & I&T Studio.
    """
    LOGGER.info("verify_devices_on_cv: %s", len(devices))

    # Return if we have nothing to do.
    if not devices:
        return

    exp = return_duplicates(devices)
    exception_mac = "Same System MAC found for "
    exception_serial = "Same serial number found for "
    if exp:
        # exp[0] --> duplicate system mac
        # exp[1] --> duplicate serial number
        # Both serial and mac are duplicates
        if exp[0]["MAC"] and exp[1]["serial"]:
            raise CVDuplicateInfo(exception_mac, exp[0]["MAC"], exception_serial, exp[1]["serial"])
        # duplicate mac address only
        if exp[0]["MAC"]:
            raise CVDuplicateInfo(exception_mac, exp[0]["MAC"])
        # duplicate serial number only
        if exp[1]["serial"]:
            raise CVDuplicateInfo(exception_serial, exp[1]["serial"])

    existing_devices = await verify_devices_in_cloudvision_inventory(devices, skip_missing_devices, warnings, cv_client)
    await verify_devices_in_topology_studio(existing_devices, workspace_id, cv_client)
    return


def convert_to_cv_device(found_devices: list[Device]) -> list[CVDevice]:
    converted_devices = [
        CVDevice(hostname=device.hostname, serial_number=device.key.device_id, system_mac_address=device.system_mac_address) for device in found_devices
    ]
    return converted_devices


def return_duplicates(devices: list[CVDevice], check_serial: bool = True) -> list:
    return_exception = []
    # Finding entries with same serialNum or same mac address
    sys_mac_to_hostname = {}
    serial_num_to_hostname = {}
    for device in devices:
        if device.system_mac_address:
            if device.system_mac_address in sys_mac_to_hostname:
                sys_mac_to_hostname[device.system_mac_address].add(device.hostname)
            else:
                sys_mac_to_hostname.setdefault(device.system_mac_address, set()).add(device.hostname)

        if check_serial and device.serial_number:
            if device.serial_number in serial_num_to_hostname:
                serial_num_to_hostname[device.serial_number].add(device.hostname)
            else:
                serial_num_to_hostname.setdefault(device.serial_number, set()).add(device.hostname)
    hostnames_same_mac = [list(hostnames) for mac, hostnames in sys_mac_to_hostname.items() if len(hostnames) > 1]
    hostnames_with_same_serial = [list(hostnames) for serial, hostnames in serial_num_to_hostname.items() if len(hostnames) > 1]
    return_exception.append({"MAC": hostnames_same_mac})
    return_exception.append({"serial": hostnames_with_same_serial})
    return return_exception


async def verify_devices_in_cloudvision_inventory(
    devices: list[CVDevice], skip_missing_devices: bool, warnings: list[Exception], cv_client: CVClient
) -> list[CVDevice]:
    """
    Verify that the given Devices are already present in the CloudVision Inventory
    and in-place update the given objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where _exists_on_cv is already filled out on the device.

    Returns a list of CVDevice objects found to exist on CloudVision.
    """

    # Using set to only include a device once.
    device_tuples = set(
        (device.serial_number, device.system_mac_address, device.hostname if not any([device.serial_number, device.system_mac_address]) else None)
        for device in devices
        if device._exists_on_cv is None
    )
    LOGGER.info("verify_devices_in_cloudvision_inventory: %s unique devices.", len(device_tuples))

    found_devices = await cv_client.get_inventory_devices(devices=device_tuples)
    # found_devices = [
    #     Device(key=DeviceKey(device_id='avd-ci-leaf3'), software_version='4.31.1F', model_name='cEOSLab',
    #           hardware_revision='', fqdn='avd-ci-leaf3', hostname='avd-ci-leaf3', domain_name='', system_mac_address='00:1c:73:c0:c4:03'),
    #     Device(key=DeviceKey(device_id='avd-ci-leaf2'), software_version='4.31.1F', model_name='cEOSLab',
    #            hardware_revision='', fqdn='avd-ci-leaf2', hostname='avd-ci-leaf2', domain_name='', system_mac_address='00:1c:73:c0:c4:03'),
    #     Device(key=DeviceKey(device_id='avd-ci-leaf1'), software_version='4.31.1F', model_name='cEOSLab',
    #           hardware_revision='', fqdn='avd-ci-leaf1', hostname='avd-ci-leaf1', domain_name='', system_mac_address='00:1c:73:c0:c4:03'),
    #     Device(key=DeviceKey(device_id='avd-ci-leaf4'), software_version='4.31.1F', model_name='cEOSLab',
    #           hardware_revision='', fqdn='avd-ci-leaf1', hostname='avd-ci-leaf4', domain_name='', system_mac_address='00:1c:73:c0:c4:06'),
    #     Device(key=DeviceKey(device_id='avd-ci-leaf5'), software_version='4.31.1F', model_name='cEOSLab',
    #           hardware_revision='', fqdn='avd-ci-leaf1', hostname='avd-ci-leaf5', domain_name='', system_mac_address='00:1c:73:c0:c4:06'),
    #     Device(key=DeviceKey(device_id='avd-ci-leaf6'), software_version='4.31.1F', model_name='cEOSLab',
    #           hardware_revision='', fqdn='avd-ci-leaf1', hostname='avd-ci-leaf6', domain_name='', system_mac_address='00:1c:73:c0:c4:06')
    # ]
    LOGGER.info("verify_devices_in_cloudvision_inventory: got %s matching devices on CV.", len(found_devices))
    found_device_dict_by_serial = {found_device.key.device_id: found_device for found_device in found_devices}
    found_device_dict_by_system_mac = {found_device.system_mac_address: found_device for found_device in found_devices}
    found_device_dict_by_hostname = {found_device.hostname: found_device for found_device in found_devices}

    # XXX: quick check to find the duplicates
    if not (len(found_device_dict_by_serial) == len(found_device_dict_by_system_mac) == len(found_device_dict_by_hostname)):
        # XXX: check for the duplicates
        exp = return_duplicates(convert_to_cv_device(found_devices))
        if exp:
            # CVP can only have duplicate MAC entry, hence directly reference the '0'th element
            raise CVDuplicateInfo("Same MAC address found for ", exp[0]["MAC"])

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
    # Using set to only include a device once.
    existing_device_tuples = set((device.serial_number, device.system_mac_address, device.hostname) for device in existing_devices)

    LOGGER.info(
        "verify_devices_in_cloudvision_inventory: %s existing device objects for %s unique devices in inventory",
        len(existing_devices),
        len(existing_device_tuples),
    )

    if missing_devices := [device for device in devices if not device._exists_on_cv]:
        warnings.append(missing_devices_handler(missing_devices, skip_missing_devices, "CloudVision Device Inventory"))

    return existing_devices


async def verify_devices_in_topology_studio(existing_devices: list[CVDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Insert and/or update given Devices in the Inventory & Topology Studio.

    Since we only get devices which are already verified to be in the inventory, we can trust the given information.

    Existing devices are updated with hostname and system mac address.
    Missing devices are added with device id, hostname, system mac address.
    """

    existing_device_tuples = set((device.serial_number, device.hostname, device.system_mac_address) for device in existing_devices)

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
        if serial_number not in topology_inputs_dict_by_serial:
            update_topology_inputs.append((serial_number, hostname, system_mac_address))
        elif (
            hostname != topology_inputs_dict_by_serial[serial_number]["hostname"]
            or system_mac_address != topology_inputs_dict_by_serial[serial_number]["mac_address"]
        ):
            update_topology_inputs.append((serial_number, hostname, system_mac_address))

    if update_topology_inputs:
        LOGGER.info("verify_devices_in_topology_studio: need updates for %s unique devices in I&T Studio.", len(update_topology_inputs))
        await cv_client.set_topology_studio_inputs(workspace_id=workspace_id, device_inputs=update_topology_inputs)


def missing_devices_handler(missing_devices: list[CVDevice], skip_missing_devices: bool, context: str) -> Exception:
    """
    Handle missing devices:
      - Raises if skip_missing_devices is False.
      - Return Exception if skip_missing_devices is True.
    """
    # Using set to only include a device once.
    missing_device_tuples = set((device.serial_number, device.system_mac_address, device.hostname) for device in missing_devices)
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
