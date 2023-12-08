# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ..api.arista.changecontrol.v1 import ChangeControl, ChangeControlStatus
from ..api.arista.workspace.v1 import BuildState, WorkspaceState
from ..client import CVClient
from ..client.exceptions import CVResourceInvalidState, CVResourceNotFound, CVWorkspaceBuildFailed
from ..models import CVChangeControl, CVDevice, CVDeviceTag, CVEosConfig, CVWorkspace, DeployToCvResult

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.WORKSPACE_STATE_ABANDONED: "abandoned",
    WorkspaceState.WORKSPACE_STATE_CONFLICTS: "build failed",
    WorkspaceState.WORKSPACE_STATE_PENDING: "pending",
    WorkspaceState.WORKSPACE_STATE_ROLLED_BACK: "pending",
    WorkspaceState.WORKSPACE_STATE_SUBMITTED: "submitted",
    WorkspaceState.WORKSPACE_STATE_UNSPECIFIED: None,
}

CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP = {
    ChangeControlStatus.CHANGE_CONTROL_STATUS_COMPLETED: "completed",
    ChangeControlStatus.CHANGE_CONTROL_STATUS_RUNNING: "running",
    ChangeControlStatus.CHANGE_CONTROL_STATUS_SCHEDULED: "scheduled",
    ChangeControlStatus.CHANGE_CONTROL_STATUS_UNSPECIFIED: None,
}

CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP = {True: "approved", False: None}


def get_change_control_final_state(cv_change_control: ChangeControl) -> str:
    return (
        CHANGE_CONTROL_STATUS_TO_FINAL_STATE_MAP[cv_change_control.status]
        or CHANGE_CONTROL_APPROVAL_TO_FINAL_STATE_MAP[cv_change_control.approve.value]
        or "failed"
        if cv_change_control.error is not None
        else "pending approval"
    )


async def cv_create_workspace(workspace: CVWorkspace, cv_client: CVClient) -> None:
    """
    Create or update a Workspace from the given workspace object.
    In-place update the workspace state.
    """
    try:
        existing_workspace = await cv_client.get_workspace(workspace_id=workspace.id)
        if existing_workspace.state == WorkspaceState.WORKSPACE_STATE_PENDING:
            workspace.final_state = "pending"
        else:
            raise CVResourceInvalidState("The requested workspace is not in state 'pending'")
    except CVResourceNotFound:
        await cv_client.create_workspace(workspace_id=workspace.id, display_name=workspace.name, description=workspace.description)
        workspace.final_state = "pending"


async def cv_set_final_state_workspace(workspace: CVWorkspace, cv_client: CVClient) -> None:
    """
    Finalize a Workspace from the given result.CVWorkspace object.
    Depending on the requested final_state the Workspace will be left in pending, built, submitted, abandoned or deleted.
    In-place update the workspace state and creates/updates a ChangeControl object on the result object if applicable.
    """
    if workspace.requested_state == workspace.final_state or workspace.requested_state == "pending":
        return

    workspace_config = await cv_client.build_workspace(workspace_id=workspace.id)
    try:
        build_result = await cv_client.wait_for_workspace_build(workspace_id=workspace.id, build_id=workspace_config.request_params.request_id)

    except CVWorkspaceBuildFailed as e:
        workspace.final_state = "build failed"
        raise e

    if build_result.state == BuildState.BUILD_STATE_SUCCESS:
        workspace.final_state = "built"

        # We can only submit if the build was successful
        if workspace.requested_state == "submitted":
            await cv_client.submit_workspace(workspace_id=workspace.id)

    # We can abort or delete even if we got some unexpected build state.
    if workspace.requested_state == "abandoned":
        await cv_client.abandon_workspace(workspace_id=workspace.id)

    elif workspace.requested_state == "deleted":
        await cv_client.delete_workspace(workspace_id=workspace.id)
        workspace.final_state = "deleted"
        return

    cv_workspace = await cv_client.wait_for_workspace_states(
        workspace_id=workspace.id, states=[WorkspaceState.WORKSPACE_STATE_CONFLICTS, WorkspaceState.WORKSPACE_STATE_SUBMITTED]
    )

    workspace.final_state = WORKSPACE_STATE_TO_FINAL_STATE_MAP.get(cv_workspace.state)
    if cv_workspace.cc_ids is not None and cv_workspace.cc_ids.values:
        # Workspaces only create a single CC so we just only the first value.
        workspace.change_control_id = cv_workspace.cc_ids.values[0]

    return


async def cv_set_final_state_change_control(change_control: CVChangeControl, cv_client: CVClient) -> None:
    """
    Update and finalize a Change Control on CloudVision from the given result.CVChangeControl object.
    Depending on the requested final_state the Change Control will be left in pending approval, approved, started, completed or canceled.
    In-place update the CVChangeControl object.
    """

    cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)

    # Update missing fields on our local model with data from the CloudVision object.
    change_control.final_state = get_change_control_final_state(cv_change_control=cv_change_control)
    if change_control.description is None:
        change_control.name = cv_change_control.change.name
    if change_control.description is None:
        change_control.description = cv_change_control.change.notes

    # TODO: Add CC template

    # Update the change control with name, description etc from our local object if needed.
    if change_control.name != cv_change_control.change.name or change_control.description != cv_change_control.change.notes:
        await cv_client.set_change_control(change_control_id=change_control.id, name=change_control.name, description=change_control.description)
        # Update the local copy to get the exact "last updated" timestamp needed for approval.
        cv_change_control = await cv_client.get_change_control(change_control_id=change_control.id)
        change_control.final_state = get_change_control_final_state(cv_change_control=cv_change_control)

    # If requested state is "pending approval" we are done
    if change_control.requested_state == "pending approval":
        return

    # TODO: Add cancel/delete

    # For all other requested states we first need to approve.
    if not change_control.final_state == "approved":
        await cv_client.approve_chance_control(
            change_control_id=change_control.id, timestamp=cv_change_control.change.time, description="Automatic approval by AVD"
        )
        change_control.final_state = "approved"

    # If requested state is "approved" we are done.
    if change_control.requested_state == "approved":
        return

    await cv_client.start_change_control(change_control_id=change_control.id, description="Automatically started by AVD")
    change_control.final_state = "running"

    # If requested state is "running" we are done.
    if change_control.requested_state == "running":
        return


def cv_deploy_config(config: CVEosConfig, workspace: CVWorkspace, cv_client: CVClient):
    """
    Deploy config for one device to CloudVison using "Static Configlet Studio"
    """


async def cv_verify_devices(devices: list[CVDevice], cv_client: CVClient) -> None:
    """
    Verify that the given Devices are already present on CloudVision
    and in-place update the objects with missing information like
    system MAC address and serial number.

    Hostname is always set for a device, but to support initial rollout, the hostname will not
    be used for search *if* either serial_number or system_mac_address is set.

    Skip checks for devices where _exists_on_cv is already filled out on the device.

    TODO: Implement caching instead of checking a device multiple times.
    """
    # Using set to only include a device once.
    device_tuples = set(
        (device.serial_number, device.system_mac_address, device.hostname if not any([device.serial_number, device.system_mac_address]) else None)
        for device in devices
        if device._exists_on_cv is None
    )
    found_devices = await cv_client.get_inventory_devices(devices=device_tuples)
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


async def cv_deploy_device_tags(
    device_tags: list[CVDeviceTag],
    result: DeployToCvResult,
    continue_on_errors: bool,
    strict: bool,
    cv_client: CVClient,
) -> None:
    """
    Deploy Device Tags updating result with success, skipped, errors, warnings.

    If "strict" == True:
      - Any other device tag associations will be removed from the devices.
      - Remove deassociated tags if they are no longer associated with any device.
    """
    # No need to continue if we have nothing to do.
    if not device_tags:
        return

    # Verify devices exist and update CVDevice objects with _exists_on_cv. Depending on continue_on_errors we will raise or skip missing devices.
    # Since verify_devices will silently return if _exists_on_cv is already set, we can just send all the items even if we have duplicate device objects.
    await cv_verify_devices(devices=[device_tag.device for device_tag in device_tags if device_tag.device is not None], cv_client=cv_client)

    # Build Todo with DeviceTag objects that exist on CloudVision. Add the rest to skipped.
    result.skipped_device_tags.extend(device_tag for device_tag in device_tags if device_tag.device is not None and not device_tag.device._exists_on_cv)
    todo_device_tags = [device_tag for device_tag in device_tags if device_tag.device is None or device_tag.device._exists_on_cv]

    if result.skipped_device_tags:
        error = CVResourceNotFound("Missing devices on CloudVision", *[device_tag.device for device_tag in result.skipped_device_tags])
        if not continue_on_errors:
            raise error
        result.warnings.append(error)

    # No need to continue if we have nothing to do.
    if not todo_device_tags:
        return

    # Get existing device tags. Use this to only add the missing. We will *not* remove any tags.
    existing_tags = await cv_client.get_tags(workspace_id=result.workspace.id, element_type="device", creator_type="user")
    existing_tags_tuples = [(tag.key.label, tag.key.value) for tag in existing_tags]
    tags_to_add = [tag for tag in todo_device_tags if (tag.label, tag.value) not in existing_tags_tuples]
    if tags_to_add:
        await cv_client.set_tags(
            workspace_id=result.workspace.id,
            tags=[(tag.label, tag.value) for tag in tags_to_add],
            element_type="device",
        )

    # Remove entries with no assignment from todo and add to deployed.
    result.deployed_device_tags.extend(device_tag for device_tag in todo_device_tags if device_tag.device is None)
    todo_device_tags = [device_tag for device_tag in todo_device_tags if device_tag.device is not None]

    # At this point we know that all device tags are present in the workspace, so we can start assigning them where we need it.
    existing_assignments = await cv_client.get_tag_assignments(workspace_id=result.workspace.id, element_type="device", creator_type="user")
    existing_assignments_tuples = [(tag.key.label, tag.key.value, tag.key.device_id) for tag in existing_assignments]
    assignments_to_add = [tag for tag in todo_device_tags if (tag.label, tag.value, tag.device.serial_number) not in existing_assignments_tuples]
    if assignments_to_add:
        await cv_client.set_tag_assignments(
            workspace_id=result.workspace.id,
            tag_assignments=[(assignment.label, assignment.value, assignment.device.serial_number, None) for assignment in assignments_to_add],
            element_type="device",
        )

    # Move all todo to deployed.
    result.deployed_device_tags.extend(todo_device_tags)
