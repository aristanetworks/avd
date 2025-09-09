# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.tag.v2 import ElementType
from pyavd._cv.client.models import CVTag, CVTagAssignment

from .models import AvdDeviceTag, AvdInterfaceTag, DeploymentStatus, WorkflowDevice, WorkflowTag

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def deploy_tags_to_cv(
    workflow_devices: list[WorkflowDevice],
    workspace_id: str,
    strict: bool,
    cv_client: CVClient,
) -> None:
    """
    Deploy device and interface tags while updating workflow tag status as skipped, deployed or removed.

    If "strict" == True:
      - Any other tag associations will be removed from the devices.
      - TODO: Remove deassociated tags if they are no longer associated with any device.
    Else:
      - Always remove other tag assignments with the same label as given tags.
      - TODO: Remove deassociated tags if they are no longer associated with any device.

    TODO: Refactor CVDeviceTag / CVInterfaceTag to produce a stable hash so we can use it with set() methods.
          Then improve logic below using sets.
    """
    LOGGER.info("deploy_tags_to_cv: %s devices to check for tags", len(workflow_devices))

    # No need to continue if we have nothing to do.
    if not workflow_devices:
        return
    # In case of "user" created types, we have "device" or "interface" tag types that are of interest.

    # Build flat list of Workflow tags (device and interface) across all devices existing in CV inventory.
    # Update deployment status for the rest as "skipped".
    todo_tags: list[WorkflowTag] = []
    for device in workflow_devices:
        device_tags = device.device_tags
        interface_tags = device.interface_tags
        if not device.in_cv_inventory:
            for tag in device_tags + interface_tags:
                tag.status = DeploymentStatus.SKIPPED
            continue
        # device is guaranteed to be present in CV inventory
        # Also given the validation checks in verify_devices_in_cv, device serial_number is valid.
        todo_tags.extend(device_tags)
        todo_tags.extend(interface_tags)

    # No need to continue if we have nothing to do.
    if not todo_tags:
        return

    # Get all - device plus interface tags in CV.
    # Use this to only add the missing tags for each type.
    # We will *not* remove any tags. (Assignments are removed later)
    LOGGER.info("deploy_tags_to_cv: Getting all user created tags existing in CV")
    existing_tags = {CVTag.from_api(tag) for tag in await cv_client.get_tags(workspace_id=workspace_id, element_type=None, creator_type="user")}
    LOGGER.info("deploy_tags_to_cv: Got %s user created tags overall", len(existing_tags))

    desired_tags = {tag.as_cv_tag() for tag in todo_tags}
    tags_to_add = desired_tags.difference(existing_tags)

    if tags_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tags", len(tags_to_add))
        await cv_client.set_tags(workspace_id=workspace_id, tags=tags_to_add)

    # At this point we know that all tags are present in the workspace, so we can start assigning them where we need it.
    todo_assignments = todo_tags
    LOGGER.info("deploy_tags_to_cv: Getting existing tag assignments")
    existing_assignments = {
        CVTagAssignment.from_api(tag_assignment)
        for tag_assignment in await cv_client.get_tag_assignments(workspace_id=workspace_id, element_type=None, creator_type="user")
    }
    LOGGER.info("deploy_tags_to_cv: Got %s tag assignments", len(existing_assignments))
    desired_assignments = {cv_tag_assignment for assignment in todo_assignments if (cv_tag_assignment := assignment.as_cv_tag_assignment()) is not None}
    assignments_to_add = desired_assignments.difference(existing_assignments)

    if assignments_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tag assignments", len(assignments_to_add))
        await cv_client.set_tag_assignments(workspace_id=workspace_id, tag_assignments=assignments_to_add)

    # Build list of deployed tags (device and interface) across all devices.
    # This is later needed for identifying tags to unassign.
    deployed_tags: list[WorkflowTag] = []
    # Update status of all todo_tags (device and interface tags) as deployed.
    for tag in todo_tags:
        if tag.as_cv_tag_assignment() is not None:
            tag.status = DeploymentStatus.DEPLOYED
            deployed_tags.append(tag)

    # Now we start removing assignments depending on strict_tags or not.
    # Build separate dict of serial number mapping to WorkflowDevice object - one for device tags and another for interface tags.
    # This is needed to determine tags to be unassigned to support workflows that may be deploying
    # *only* device vs *only* interface tags based on AVD input provided for a given device.
    devices_by_serial_number_for_device_tags: dict[str, WorkflowDevice] = {}
    devices_by_serial_number_for_interface_tags: dict[str, WorkflowDevice] = {}

    for tag in deployed_tags:
        if isinstance(tag.input, AvdDeviceTag):
            devices_by_serial_number_for_device_tags[tag.parent_device.serial_number] = tag.parent_device
        else:
            devices_by_serial_number_for_interface_tags[tag.parent_device.serial_number] = tag.parent_device

    # If strict, we remove any assignments not specified in the inputs.
    # If not strict, we remove any assignments with the same labels but not specified in the inputs.
    assignments_to_unassign = set()
    if strict:
        LOGGER.debug("deploy_tags_to_cv: STRICT tags validation enabled")
        for assignment in existing_assignments:
            if assignment not in desired_assignments and (
                (assignment.get_element_type() == ElementType.DEVICE and assignment.device_id in devices_by_serial_number_for_device_tags)
                or (assignment.get_element_type() == ElementType.INTERFACE and assignment.device_id in devices_by_serial_number_for_interface_tags)
            ):
                assignments_to_unassign.add(assignment)
    else:
        # Build set of tag labels we have assigned so we know which ones to remove.
        desired_device_tags_labels = {assignment.label for assignment in desired_assignments if assignment.get_element_type() == ElementType.DEVICE}
        desired_interface_tags_labels = {assignment.label for assignment in desired_assignments if assignment.get_element_type() == ElementType.INTERFACE}
        for assignment in existing_assignments:
            if assignment not in desired_assignments and (
                (
                    assignment.get_element_type() == ElementType.DEVICE
                    and assignment.device_id in devices_by_serial_number_for_device_tags
                    and assignment.label in desired_device_tags_labels
                )
                or (
                    assignment.get_element_type() == ElementType.INTERFACE
                    and assignment.device_id in devices_by_serial_number_for_interface_tags
                    and assignment.label in desired_interface_tags_labels
                )
            ):
                assignments_to_unassign.add(assignment)
    if assignments_to_unassign:
        LOGGER.info("deploy_tags_to_cv: Deleting %s tag assignments", len(assignments_to_unassign))
        await cv_client.delete_tag_assignments(workspace_id=workspace_id, tag_assignments=assignments_to_unassign)
        for assignment in assignments_to_unassign:
            if assignment.get_element_type() == ElementType.DEVICE:
                # construct WorkflowTag for each device tag being removed. It will be gathered in the results later.
                device_tag = AvdDeviceTag(label=assignment.label, value=assignment.value)
                workflow_device = devices_by_serial_number_for_device_tags[assignment.device_id]
                workflow_device.device_tags.append(WorkflowTag(input=device_tag, parent_device=workflow_device, status=DeploymentStatus.REMOVED))
            elif assignment.get_element_type() == ElementType.INTERFACE:
                # construct WorkflowTag for each interface tag being removed. It will be gathered in the results later.
                interface_tag = AvdInterfaceTag(label=assignment.label, value=assignment.value, interface=assignment.interface_id)
                workflow_device = devices_by_serial_number_for_interface_tags[assignment.device_id]
                workflow_device.interface_tags.append(WorkflowTag(input=interface_tag, parent_device=workflow_device, status=DeploymentStatus.REMOVED))
