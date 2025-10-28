# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.models import CVTag, CVTagAssignment

from .models import CVDeviceTag, CVInterfaceTag, CVWorkspace

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def deploy_tags_to_cv(
    tags: list[CVDeviceTag | CVInterfaceTag],
    workspace: CVWorkspace,
    strict: bool,
    skipped_tags: list[CVDeviceTag | CVInterfaceTag],
    deployed_tags: list[CVDeviceTag | CVInterfaceTag],
    removed_tags: list[CVDeviceTag | CVInterfaceTag],
    cv_client: CVClient,
) -> None:
    """
    Deploy Tags updating result with skipped, deployed and removed tags.

    Tags can be either Device Tags or Interface Tags but *not* a combination.

    If "strict" == True:
      - Any other tag associations will be removed from the devices.
      - TODO: Remove deassociated tags if they are no longer associated with any device.
    Else:
      - Always remove other tag assignments with the same label as given tags.
      - TODO: Remove deassociated tags if they are no longer associated with any device.

    TODO: Refactor CVDeviceTag / CVInterfaceTag to produce a stable hash so we can use it with set() methods.
          Then improve logic below using sets.


    In-place updates skipped_tags, deployed_tags and removed_tags so they can be given directly from the results object.
    """
    LOGGER.info("deploy_tags_to_cv: %s", len(tags))

    # No need to continue if we have nothing to do.
    if not tags:
        return

    tag_type = "interface" if isinstance(tags[0], CVInterfaceTag) else "device"

    # Build todo tags with CVDevice/CVInterfaceTag objects that exist on CloudVision. Add the rest to skipped.
    skipped_tags.extend(tag for tag in tags if tag.device is not None and not tag.device._exists_on_cv)
    todo_tags = [tag for tag in tags if tag.device is None or tag.device._exists_on_cv]

    # No need to continue if we have nothing to do.
    if not todo_tags:
        return

    # Get existing tags. Use this to only add the missing. We will *not* remove any tags. Assignments are removed later.
    LOGGER.info("deploy_tags_to_cv: Getting existing tags")
    existing_tags = {CVTag.from_api(tag) for tag in await cv_client.get_tags(workspace_id=workspace.id, element_type=tag_type, creator_type="user")}
    LOGGER.info("deploy_tags_to_cv: Got %s tags", len(existing_tags))
    desired_tags = {tag.as_cv_tag() for tag in todo_tags}
    tags_to_add = desired_tags.difference(existing_tags)
    if tags_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tags", len(tags_to_add))
        await cv_client.set_tags(workspace_id=workspace.id, tags=tags_to_add)

    # Remove entries with no assignment from todo tags and add to deployed.
    deployed_tags.extend(tag for tag in todo_tags if tag.device is None)
    todo_assignments = [tag for tag in todo_tags if tag.device is not None]

    # At this point we know that all tags are present in the workspace, so we can start assigning them where we need it.
    LOGGER.info("deploy_tags_to_cv: Getting existing tag assignments")
    existing_assignments = {
        CVTagAssignment.from_api(tag_assignment)
        for tag_assignment in await cv_client.get_tag_assignments(workspace_id=workspace.id, element_type=tag_type, creator_type="user")
    }
    LOGGER.info("deploy_tags_to_cv: Got %s tag assignments", len(existing_assignments))
    desired_assignments = {cv_tag_assignment for assignment in todo_assignments if (cv_tag_assignment := assignment.as_cv_tag_assignment()) is not None}
    assignments_to_add = desired_assignments.difference(existing_assignments)
    if assignments_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tag assignments", len(assignments_to_add))
        await cv_client.set_tag_assignments(workspace_id=workspace.id, tag_assignments=assignments_to_add)

    # Move all todo assignments to deployed.
    deployed_tags.extend(todo_assignments)

    # Now we start removing assignments depending on strict_tags or not.

    # Build a mapping of device serial number to CVDevice.
    devices_by_serial_number = {
        tag.device.serial_number: tag.device for tag in deployed_tags if tag.device is not None and tag.device.serial_number is not None
    }

    # If strict, we remove any assignments not specified in the inputs.
    # If not strict, we remove any assignments with the same labels but not specified in the inputs.
    if strict:
        assignments_to_unassign = {
            assignment for assignment in existing_assignments if assignment.device_id in devices_by_serial_number and assignment not in desired_assignments
        }
    else:
        # Build set of tag labels we have assigned so we know which ones to remove.
        desired_tags_labels = {assignment.label for assignment in desired_assignments}
        assignments_to_unassign = {
            assignment
            for assignment in existing_assignments
            if assignment.device_id in devices_by_serial_number and assignment.label in desired_tags_labels and assignment not in desired_assignments
        }

    if assignments_to_unassign:
        LOGGER.info("deploy_tags_to_cv: Deleting %s tag assignments", len(assignments_to_unassign))
        await cv_client.delete_tag_assignments(workspace_id=workspace.id, tag_assignments=assignments_to_unassign)

        # Sort the assignments for deterministic output for testing.
        sorted_assignments_to_unassign = sorted(
            assignments_to_unassign,
            key=lambda assignment: (assignment.label, assignment.value, assignment.device_id, assignment.interface_id or "", assignment.element_type),
        )

        if tag_type == "interface":
            removed_tags.extend(
                CVInterfaceTag(
                    label=assignment.label, value=assignment.value, device=devices_by_serial_number[assignment.device_id], interface=assignment.interface_id
                )
                for assignment in sorted_assignments_to_unassign
            )
        else:
            removed_tags.extend(
                CVDeviceTag(label=assignment.label, value=assignment.value, device=devices_by_serial_number[assignment.device_id])
                for assignment in sorted_assignments_to_unassign
            )
