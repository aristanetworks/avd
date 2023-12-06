# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ..api.arista.workspace.v1 import BuildState, WorkspaceState
from ..client import CVClient
from ..client.exceptions import CVResourceInvalidState, CVResourceNotFound, CVWorkspaceBuildFailed
from ..models import CVDeviceTag, CVWorkspace, DeployToCvResult, Device, EosConfig


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
    Finalize a Workspace from the given workspace object.
    Depending on the requested final_state the Workspace will be either built, built and submitted, abandoned or abandoned and deleted.
    In-place update the workspace state.
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
            workspace_config = await cv_client.submit_workspace(workspace_id=workspace.id)
            workspace.final_state = "submitted"

    # We can abort and delete even if we got some unexpected build state.
    if workspace.requested_state in ["abandoned", "deleted"]:
        await cv_client.abandon_workspace(workspace_id=workspace.id)
        workspace.final_state = "abandoned"

        if workspace.requested_state == "deleted":
            await cv_client.delete_workspace(workspace_id=workspace.id)
            workspace.final_state = "deleted"


def cv_deploy_config(config: EosConfig, workspace: CVWorkspace, cv_client: CVClient):
    """
    Deploy config for one device to CloudVison using "Static Configlet Studio"
    """


async def cv_verify_device(device: Device, cv_client: CVClient) -> bool:
    """
    Verify that the given Device is already present on CloudVision
    and in-place update the object with missing information like
    system MAC address, serial number and CloudVisions device ID (usually serial number but just in case).
    """
    if device._cv_device_id is not None:
        return True

    # TODO: Verify that device is present on CV and insert the inventory information.
    # Make sure to cache the inventory info if we pull the full thing.
    return False


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
    # No need to continue if we have no todo.
    if not device_tags:
        return

    # Creating a fresh list to avoid changing the given list.
    todo_device_tags = list(device_tags)

    # Verify devices exist and update Device objects with _cv_device_id. Depending on continue_on_errors we will raise or skip missing devices.
    # Since verify_devices will silently return if _cv_device_id is already set, we can just send all the items even if we have duplicate device objects.
    verification_results = [
        device_tag.device is None or await cv_verify_device(device=device_tag.device, cv_client=cv_client) for device_tag in todo_device_tags
    ]
    if not all(verification_results):
        length = len(verification_results)
        # Reversing twice. Inside enumerate to pop from the end to avoid messing up indexes. Outside to retain the original order.
        device_tags_with_missing_device = reversed(
            [
                todo_device_tags.pop(length - index)
                for index, res in enumerate(
                    reversed(verification_results),
                    start=1,
                )
                if not res
            ]
        )
        result.skipped_device_tags.extend(device_tags_with_missing_device)
        error = CVResourceNotFound("Missing devices on CloudVision", *[device_tag.device for device_tag in device_tags_with_missing_device])
        if not continue_on_errors:
            raise error
        result.warnings.append(error)

    # No need to continue if no todos left.
    if not todo_device_tags:
        return

    # Get existing device tags. Use this to only add the missing. We will *not* remove any tags*
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
    assignments_to_add = [tag for tag in todo_device_tags if (tag.label, tag.value, tag.device._cv_device_id) not in existing_assignments_tuples]
    if assignments_to_add:
        await cv_client.set_tag_assignments(
            workspace_id=result.workspace.id,
            tag_assignments=[(assignment.label, assignment.value, assignment.device._cv_device_id, None) for assignment in assignments_to_add],
            element_type="device",
        )

    # Move all todo to deployed.
    result.deployed_device_tags.extend(todo_device_tags)
