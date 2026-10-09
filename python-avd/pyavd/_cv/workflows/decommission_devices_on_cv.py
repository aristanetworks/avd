# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.studio_topology.v1 import DecommissionStatus

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVDevice, DeployToCvResult

LOGGER = getLogger(__name__)


async def stage_devices_for_decommission_on_cv(
    devices: list[CVDevice],
    workspace_id: str,
    result: DeployToCvResult,
    cv_client: CVClient,
) -> list[CVDevice]:
    """
    Stage the given devices for decommission in the CloudVision Workspace.

    CloudVision removes all device and interface tag assignments associated with successfully decommissioned devices.
    Tag definitions remain in CloudVision and are not deleted by AVD.

    Parameters:
        devices: Devices to decommission. Must have `serial_number` set and `exists_on_cv=True`.
        workspace_id: Workspace ID to stage the decommission in.
        result: Result object. Staging failures are appended to `result.warnings`.
        cv_client: CloudVision client instance.

    Returns:
        List of CVDevice objects for which staging succeeded.
    """
    serial_to_device = {device.serial_number: device for device in devices if device.serial_number is not None}

    if not (serial_numbers := list(serial_to_device)):
        return []

    LOGGER.info("stage_devices_for_decommission_on_cv: Staging %s device(s) for decommission.", len(serial_numbers))
    staging_errors = await cv_client.stage_devices_for_decommission(workspace_id=workspace_id, device_ids=serial_numbers)

    failed_serials: set[str] = set()
    for device_key, error_msg in staging_errors:
        serial = device_key.device_id
        msg = f"stage_devices_for_decommission_on_cv: Failed to stage device {serial} for decommission: {error_msg}"
        LOGGER.warning(msg)
        result.warnings.append(msg)
        if serial is not None:
            failed_serials.add(serial)

    successfully_staged = [device for device in devices if device.serial_number is not None and device.serial_number not in failed_serials]
    LOGGER.info("stage_devices_for_decommission_on_cv: Successfully staged %s device(s).", len(successfully_staged))
    return successfully_staged


async def wait_for_device_decommission_staging_on_cv(
    devices: list[CVDevice],
    workspace_id: str,
    result: DeployToCvResult,
    cv_client: CVClient,
) -> None:
    """
    Wait for decommission staging to reach a terminal state for all given devices.

    Must be called before building the Workspace to ensure decommission staging is complete.

    Devices that reach SUCCESS are appended to `result.removed_devices`. Failures are appended
    to `result.warnings`.

    Parameters:
        devices: List of CVDevices.
        workspace_id: Workspace ID to subscribe to.
        result: Result object updated in-place.
        cv_client: CloudVision client instance.
    """
    serial_to_device = {device.serial_number: device for device in devices if device.serial_number is not None}
    serial_numbers = list(serial_to_device)
    if not serial_numbers:
        return

    LOGGER.info("wait_for_device_decommission_staging_on_cv: Waiting for decommission staging for %s device(s).", len(serial_numbers))
    decommission_results = await cv_client.wait_for_device_decommission_staging(workspace_id=workspace_id, device_ids=serial_numbers)

    for decommission_result in decommission_results:
        serial = decommission_result.key.device_id
        device = serial_to_device.get(serial) if serial is not None else None
        if decommission_result.status == DecommissionStatus.SUCCESS:
            LOGGER.info("wait_for_device_decommission_staging_on_cv: Decommission staging succeeded for device %s.", serial)
            if device:
                result.removed_devices.append(device)
        else:
            warning = f"wait_for_device_decommission_staging_on_cv: Decommission staging failed for device {serial}: {decommission_result.status}"
            LOGGER.warning(warning)
            result.warnings.append(warning)
