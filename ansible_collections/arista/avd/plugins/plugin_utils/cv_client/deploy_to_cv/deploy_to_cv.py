# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ..client import CVClient
from ..client.exceptions import CVClientException
from ..models import CloudVision, CVChangeControl, CVDeviceTag, CVInterfaceTag, CVWorkspace, DeployToCvResult, EosConfig, TimeOuts
from .utils import cv_create_workspace, cv_deploy_device_tags, cv_set_final_state_workspace


async def deploy_to_cv(
    cloudvision: CloudVision,
    workspace: CVWorkspace | None = None,
    change_control: CVChangeControl | None = None,
    configs: list[EosConfig] | None = None,
    device_tags: list[CVDeviceTag] | None = None,
    interface_tags: list[CVInterfaceTag] | None = None,
    continue_on_errors: bool = False,
    strict_configs: bool = True,
    strict_tags: bool = True,
    timeouts: TimeOuts | None = None,
) -> DeployToCvResult:
    """
    Deploy various objects to CloudVision.

    For any device referred under `configs`, `device_tags` and `interface_tags` the device:
    - The device must be present in the CloudVision Inventory and the "Inventory & Topology Studio".
        - TODO: See if we can relax the I&T requirement and add the device if it is missing.
        - TODO: See if we can onboard ZTP devices and/or preprovision.
    - The hostname will we updated in the I&T Studio.
    - The `serial_number` and `system_mac_address` properties will be inplace updated in the given Device objects.

    TODO: Add something for generic studio inputs.

    Parameters:
        cloudvision: CloudVision instance to deploy to.
        workspace: CloudVision Workspace to create or use for the deployment. \
            If the Workspace already exists, it must be in 'pending' state.
            The `final_state` property will be inplace updated in the given CVWorkSpace object.
        change_control: CloudVision Change Control to create for the deployment. \
            It is not supported to reuse an existing Change Control, so the `id` field should not be set in the given CVChangeControl object. \
            The `id` and `final_state` properties will be inplace updated in the given CVChangeControl object.
        configs: Configs to be deployed using the "Static Configlet Studio".
        device_tags: Device Tags to be deployed and assigned.
        interface_tags: Interface Tags to be deployed and assigned.
        continue_on_errors: If `True` anything that can be deployed will get deployed. \
            Otherwise the Workspace will be abandoned on any issue.
        strict_configs: If `True` other configs associated with the devices will get removed. \
            Otherwise other configs will be left as-is.
        strict_tags: If `True` other tags associated with the devices will get removed. \
            Otherwise other tags will be left as-is. \
            Other Tags with the same label are always removed.

    Returns:
        Object containing the results of the deployment including all associated objects.

    TODO: Workflow:
        + Create result object.
            + Add workspace object to result if given otherwise create a new workspace object we can return.
            - Add objects to result.deployed_x/skipped_x as we go through each of the following steps.
        + Initialize CVClient
        - Gather all devices from the given lists.
        - On CV Identify all devices based on hostname, serial number or System MAC address.
            - In-place update device objects.
        - On CV Create or update existing Workspace with name and description.
            - In-place update workspace object.
        - On CV in "Inventory & Topology Studio" set/verify hostnames.
        - On CV in "Static Configlet Studio" upload configlets and assign to devices.
            - TODO: Decide if we should create a hierarchy or just a single folder for AVD?
        - On CV add and assign device tags and interface tags.
        - On CV build, submit, abandon, delete the Workspace as applicable based on requested state.
            - In-place update workspace and result object.
        - If not submitting the Workspace return the result object. Otherwise continue.
        - Wait for Workspace submission to return a change control id.
            - Update or create a CVChangeControl object and add to result.
        - On CV set description on the created change control and apply the template if given.
        - On CV approve, submit, cancel the Change Control as applicable based on requested state.
        - Return result object.
    """
    result = DeployToCvResult(workspace=workspace, change_control=change_control)
    if result.workspace is None:
        result.workspace = CVWorkspace()

    try:
        async with CVClient(servers=cloudvision.servers, token=cloudvision.token, verify_certs=cloudvision.verify_certs) as cv_client:
            # Create workspace
            await cv_create_workspace(workspace=result.workspace, cv_client=cv_client)

            try:
                # Deploy device tags
                await cv_deploy_device_tags(
                    device_tags=device_tags, result=result, continue_on_errors=continue_on_errors, strict=strict_tags, cv_client=cv_client
                )
            except CVClientException as e:
                result.errors.append(e)
                result.failed = True

            # Build, submit or abandon workspace. If failed, we always abandon.
            if result.failed:
                await cv_client.abandon_workspace(workspace_id=workspace.id)
                workspace.final_state = "abandoned"
            else:
                await cv_set_final_state_workspace(workspace=result.workspace, cv_client=cv_client)

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True

    return result
