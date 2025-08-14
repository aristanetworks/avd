# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Literal

from pyavd._cv.client.models import CVTag, CVTagAssignment
from pyavd._cv.client.exceptions import CVClientException

from .models import AvdDeviceTag, AvdInterfaceTag, CVDeviceTag, CVInterfaceTag, CVWorkspace, InternalDevice

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def deploy_tags_to_cv(
    tag_type: Literal["device", "interface"],
    internal_devices: list[InternalDevice],
    workspace: CVWorkspace,
    strict: bool,
    skipped_tags: list[CVDeviceTag | CVInterfaceTag],
    deployed_tags: list[CVDeviceTag | CVInterfaceTag],
    removed_tags: list[CVDeviceTag | CVInterfaceTag],
    cv_client: CVClient,
) -> None:
    """
    Deploy Tags updating result with skipped, deployed and removed tags.

    Tag type is either "device" or "interface".
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
    LOGGER.info("deploy_tags_to_cv: %s devices to check for %s tag type", len(internal_devices), tag_type)

    # No need to continue if we have nothing to do.
    if not internal_devices:
        return

    # 'deployed_tags' would include tags in AVD input that are already existing in CV
    # plus new tags present in AVD input that are yet to be added to CV.
    # 'skipped_tags' would include tags in AVD input but corresponding
    # device is not present in CV inventory

    # build subset of internal device objects that exist in CV inventory containing tag_type being queried
    todo_devices_with_tags: list[InternalDevice] = []
    # InternalDevice object in CV Inventory accessible via referencing device serial number (used for updating tags)
    todo_devices_by_serial_number: dict[str, InternalDevice] = {}

    # Build TODO: with CVDevice/CVInterfaceTag objects that exist on CloudVision. Add the rest to skipped.
    skipped_tags.extend(tag for tag in tags if tag.device is not None and not tag.device._exists_on_cv)
    todo_tags = [tag for tag in tags if tag.device is None or tag.device._exists_on_cv]

    # populate skipped tags in overall result and identify devices to be examined further
    for device in internal_devices:
        tags_matching_tag_type = device.avd_device.device_tags if tag_type == "device" else device.avd_device.interface_tags
        if not device.in_cv_inventory:
            if len(tags_matching_tag_type) > 0:
                skipped_tags.extend(device.get_one_cv_tag(tag) for tag in tags_matching_tag_type)
                device.result.device_tags.skipped.extend(list(tags_matching_tag_type))
            continue
        if not device.serial_number:
            # TODO: Check if logic below to raise exception is fine
            # We expect device.serial_number to be already populated (i.e. fetched from CV Inventory) when we get here
            # Bail out here else we would need to repeat such checks for rest of the wrappers.
            LOGGER.info("deploy_tags_to_cv: device %s in CV inventory, but no serial number found to be assigned in CV!", device.avd_device.hostname)
            deploy_tags_err_msg = "deploy_tags_to_cv(): Detected device in CV Inventory, but unable to fetch serial number!"
            raise CVClientException(deploy_tags_err_msg)
        todo_devices_by_serial_number[device.serial_number] = device
        # device is in inventory, add to list only if contains tag_type being queried
        if len(tags_matching_tag_type) > 0:
            # given checks above, todo_devices_with_tags will always contain devices with valid serial number set
            todo_devices_with_tags.append(device)

    # No need to continue if we have nothing to do.
    if not todo_devices_with_tags:
        return

    # Get existing device or tags. Use this to only add the missing. We will *not* remove any tags. Assignments are removed later.
    LOGGER.info("deploy_tags_to_cv: Getting existing tags of type: %s in CV", tag_type)
    existing_tags = {CVTag.from_api(tag) for tag in await cv_client.get_tags(workspace_id=workspace.id, element_type=tag_type, creator_type="user")}
    existing_tags_tuples = [(tag.label, tag.value) for tag in existing_tags]
    LOGGER.info("deploy_tags_to_cv: Got %s tags", len(existing_tags))

    desired_tags = {tag.as_cv_tag() for tag in todo_tags}
    tags_to_add = desired_tags.difference(existing_tags)

    # Compute candidate tags to be added based on internal_devices (present in CV inventory)
    # and depending upon tag_type specified
    tags_to_add_from_internal_devices = []
    for device in todo_devices_with_tags:
        tags_matching_tag_type = device.avd_device.device_tags if tag_type == "device" else device.avd_device.interface_tags
        tags_to_add.extend((tag.label, tag.value) for tag in tags_matching_tag_type if (tag.label, tag.value) not in existing_tags_tuples)

    LOGGER.info("deploy_tags_to_cv: Creating %s tags to add", len(tags_to_add))

    if tags_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tags", len(tags_to_add))
        await cv_client.set_tags(workspace_id=workspace.id, tags=tags_to_add)

    # set_tags for tags derived from internal_devices
    if tags_to_add_from_internal_devices:
        await cv_client.set_tags(workspace_id=workspace.id, tags=tags_to_add_from_internal_devices, element_type=tag_type)

    # Remove entries with no assignment from todo tags and add to deployed.
    deployed_tags.extend(tag for tag in todo_tags if tag.device is None)
    todo_assignments = [tag for tag in todo_tags if tag.device is not None]

    # `deployed_tags_internal_devices`` is empty when we get here.
    # At this point we know that all tags are present in the workspace, so we can start assigning them where we need it.
    LOGGER.info("deploy_tags_to_cv: Getting existing tag assignments")
    existing_assignments = {
        CVTagAssignment.from_api(tag_assignment)
        for tag_assignment in await cv_client.get_tag_assignments(workspace_id=workspace.id, element_type=tag_type, creator_type="user")
    }
    LOGGER.info("deploy_tags_to_cv: Got %s tag assignments", len(existing_assignments))
    desired_assignments = {cv_tag_assignment for assignment in todo_assignments if (cv_tag_assignment := assignment.as_cv_tag_assignment()) is not None}
    assignments_to_add = desired_assignments.difference(existing_assignments)
    # using filtered list of internal devices
    # Build list of tuple for tag assignment
    todo_tag_assignments = []
    for device in todo_devices_with_tags:
        tags_matching_tag_type = device.avd_device.device_tags if tag_type == "device" else device.avd_device.interface_tags
        tags_placeholder_to_add = device.device_tags.to_add if tag_type == "device" else device.interface_tags.to_add
        result_placeholder_verified = device.result.device_tags.verified if tag_type == "device" else device.result.interface_tags.verified

        for tag in tags_matching_tag_type:
            if (tag.label, tag.value, device.serial_number, getattr(tag, "interface", None)) not in existing_assignments:
                todo_tag_assignments.append((tag.label, tag.value, device.serial_number, getattr(tag, "interface", None)))
                # update per-device tags we intend to add to CV
                tags_placeholder_to_add.append(tag)
            else:
                # tag is found to be already present within existing tag assignments in CV
                # update corr. tags placeholder for overall result, count this towards deployed_tags
                deployed_tags.extend([device.get_one_cv_tag(tag)])
                result_placeholder_verified.extend([tag])

    # TODO: remove this, added for validation
    if todo_tags != todo_tag_assignments:
        deploy_tags_err_msg = "deploy_tags_to_cv(): Mismatch detected in todo_tag_assignments! raising exception during deploy_tags_to_cv() step"
        deploy_tags_err_msg += f" todo_tags len:{len(todo_tags)} vs todo_tag_assignments len:{len(todo_tag_assignments)}"
        raise CVClientException(deploy_tags_err_msg)

    if assignments_to_add:
        LOGGER.info("deploy_tags_to_cv: Creating %s tag assignments", len(assignments_to_add))
        await cv_client.set_tag_assignments(workspace_id=workspace.id, tag_assignments=assignments_to_add)

    # call set_tag_assignments() based on tags gathered from internal_devices
    if todo_tag_assignments:
        LOGGER.info("deploy_tags_to_cv: Creating %s tag assignments", len(todo_tag_assignments))
        await cv_client.set_tag_assignments(
            workspace_id=workspace.id,
            tag_assignments=todo_tag_assignments,
            element_type=tag_type,
        )
        # Upon successful completion of set_tag_assignments(),
        # proceed to update per-device and overall result with tags that were added via set_tag.
        # Count tags identified to be added towards deployed_tags.
        for device in todo_devices_with_tags:
            tags_to_add_for_device = device.device_tags.to_add if tag_type == "device" else device.interface_tags.to_add
            result_placeholder_tags_added = device.result.device_tags.added if tag_type == "device" else device.result.interface_tags.added
            if tags_to_add_for_device:
                result_placeholder_tags_added.extend(tags_to_add_for_device)
                deployed_tags.extend(device.get_one_cv_tag(tag) for tag in tags_to_add_for_device)

    # Now we start removing assignments depending on strict_tags or not.

    
    # Build set of tuples for deployed tags.
    deployed_tags_tuples = {
        (tag.label, tag.value, tag.device.serial_number, getattr(tag, "interface", None)) for tag in deployed_tags if tag.device is not None
    }

    # Build a mapping of device serial number to CVDevice.
    devices_by_serial_number = {
        tag.device.serial_number: tag.device for tag in deployed_tags if tag.device is not None and tag.device.serial_number is not None
    }

    # If strict, we remove any assignments not specified in the inputs.
    # If not strict, we remove any assignments with the same labels but not specified in the inputs.
    assignments_to_unassign = []
    if strict:
        LOGGER.debug("deploy_tags_to_cv: STRICT tags validation ENABLED for removing unassigned tags")
        assignments_to_unassign = {
            assignment for assignment in existing_assignments if assignment.device_id in devices_by_serial_number and assignment not in desired_assignments
        }
        # logic for populating assignments_to_unassign_internal_devices
        for label, value, device_serial_number, interface in existing_assignments:
            if device_serial_number in devices_by_serial_number and (label, value, device_serial_number, interface) not in deployed_tags_tuples:
                assignments_to_unassign.append((label, value, device_serial_number, interface))
                if device_serial_number in todo_devices_by_serial_number:
                    if tag_type == "device":
                        todo_devices_by_serial_number[device_serial_number].device_tags.to_remove.extend([AvdDeviceTag(label=label, value=value)])
                    else:
                        todo_devices_by_serial_number[device_serial_number].interface_tags.to_remove.extend(
                            [AvdInterfaceTag(label=label, value=value, interface=interface)]
                        )
    else:
        # Build set of tag labels we have assigned so we know which ones to remove.
        desired_tags_labels = {assignment.label for assignment in desired_assignments}
        # build deployed_tags_labels_internal_devices
        deployed_tags_labels_internal_devices = {tag_tuple[0] for tag_tuple in deployed_tags_tuples_internal_devices}

        assignments_to_unassign = {
            assignment
            for assignment in existing_assignments
            if assignment.device_id in devices_by_serial_number and assignment.label in desired_tags_labels and assignment not in desired_assignments
        }
        # logic for populating assignments_to_unassign_internal_devices
        for label, value, device_serial_number, interface in existing_assignments:
            if (
                device_serial_number in devices_by_serial_number
                and label in deployed_tags_labels
                and (label, value, device_serial_number, interface) not in deployed_tags_tuples
            ):
                assignments_to_unassign.append((label, value, device_serial_number, interface))
                if device_serial_number in todo_devices_by_serial_number:
                    if tag_type == "device":
                        todo_devices_by_serial_number[device_serial_number].device_tags.to_remove.extend([AvdDeviceTag(label=label, value=value)])
                    else:
                        todo_devices_by_serial_number[device_serial_number].interface_tags.to_remove.extend(
                            [AvdInterfaceTag(label=label, value=value, interface=interface)]
                        )

    if assignments_to_unassign:
        LOGGER.info("deploy_tags_to_cv: Deleting %s tag assignments", len(assignments_to_unassign))
        await cv_client.delete_tag_assignments(workspace_id=workspace.id, tag_assignments=assignments_to_unassign)

        # Sort the assignments for deterministic output for testing.
        sorted_assignments_to_unassign = sorted(
            assignments_to_unassign,
            key=lambda assignment: (assignment.label, assignment.value, assignment.device_id, assignment.interface_id or "", assignment.element_type),
        )

    # working with internal devices
    if assignments_to_unassign_internal_devices:
        LOGGER.info("deploy_tags_to_cv: (using internal devices) Deleting %s tag assignments", len(assignments_to_unassign_internal_devices))
        await cv_client.delete_tag_assignments(workspace_id=workspace.id, tag_assignments=assignments_to_unassign_internal_devices, element_type=tag_type)

        if tag_type == "interface":
            removed_tags.extend(
                CVInterfaceTag(
                    label=assignment.label, value=assignment.value, device=devices_by_serial_number[assignment.device_id], interface=assignment.interface_id
                )
                for assignment in sorted_assignments_to_unassign
            )
        # update removed tags using internal_devices approach
        for label, value, serial_number, interface in assignments_to_unassign_internal_devices:
            interface_tag = AvdInterfaceTag(label=label, value=value, interface=interface)
            if serial_number in todo_devices_by_serial_number:
                removed_tags.extend([todo_devices_by_serial_number[serial_number].get_one_cv_tag(interface_tag)])
                todo_devices_by_serial_number[serial_number].result.interface_tags.removed.extend([interface_tag])
        else:
            removed_tags.extend(
                CVDeviceTag(label=assignment.label, value=assignment.value, device=devices_by_serial_number[assignment.device_id])
                for assignment in sorted_assignments_to_unassign
            )
        # update removed tags using internal_devices approach
        for label, value, serial_number, _ in assignments_to_unassign_internal_devices:
            device_tag = AvdDeviceTag(label=label, value=value)
            if serial_number in todo_devices_by_serial_number:
                removed_tags.extend([todo_devices_by_serial_number[serial_number].get_one_cv_tag(device_tag)])
                todo_devices_by_serial_number[serial_number].result.device_tags.removed.extend([device_tag])
