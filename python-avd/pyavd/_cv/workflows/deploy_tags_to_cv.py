# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client.models import CVTag, CVTagAssignment
from pyavd._cv.client.exceptions import CVClientException

from .models import AvdDeviceTag, AvdInterfaceTag, CVDeviceTag, CVInterfaceTag, CVWorkspace, InternalDevice

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

LOGGER = getLogger(__name__)


async def deploy_tags_to_cv(
    tags: list[CVDeviceTag | CVInterfaceTag],
    internal_devices: list[InternalDevice],
    workspace: CVWorkspace,
    strict: bool,
    skipped_tags: list[CVDeviceTag | CVInterfaceTag],
    deployed_tags: list[CVDeviceTag | CVInterfaceTag],
    removed_tags: list[CVDeviceTag | CVInterfaceTag],
    skipped_tags_internal_devices: dict[str, list[AvdDeviceTag | AvdInterfaceTag]],
    deployed_tags_internal_devices: dict[str, list[AvdDeviceTag | AvdInterfaceTag]],
    removed_tags_internal_devices: dict[str, list[AvdDeviceTag | AvdInterfaceTag]],
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
    LOGGER.info("deploy_tags_to_cv: input tags %s (using internal_devices) devices %s", len(tags), len(internal_devices))

    # No need to continue if we have nothing to do.
    if not tags or (not internal_devices):
        return

    # 'tag_type' to process could be one of the input arguments to hintvhandling of either
    # device vs interface tags in this routine. For now derive this hint from tag input arg.
    tag_type = "interface" if isinstance(tags[0], CVInterfaceTag) else "device"

    # using dictionary for tags in overall result as below.
    # These would be members of overall device result class that would be in-place updated here.
    # Tags would include device or interface tags.

    # 'deployed_tags_internal_devices' would include tags in AVD input that are already existing in CV
    # plus new tags present in AVD input but yet to be added to CV.

    # For 'skipped_tags_internal_devices' : dict key would be represented by device host name from AVD input
    # since we would be unable to fetch serial number for such device that is not present in CV inventory

    # build subset of internal devices (object references) that exist in CV inventory
    # and contain specified tag_type (device or interface)
    todo_devices_with_tags: list[InternalDevice] = []
    # InternalDevice object in CV Inventory accessible via referencing device serial number (used for updating tags)
    todo_devices_by_serial_number: dict[str, InternalDevice] = {}

    # using dictionary for tags in overall result as below.
    # These would be members of overall device result class that would be in-place updated here.
    # Tags would include device or interface tags.

    # 'deployed_tags_internal_devices' would include tags in AVD input that are already existing in CV
    # plus new tags present in AVD input but yet to be added to CV.

    # For 'skipped_tags_internal_devices' : dict key would be represented by device host name from AVD input
    # since we would be unable to fetch serial number for such device that is not present in CV inventory

    # build subset of internal devices (object references) that exist in CV inventory
    # and contain specified tag_type (device or interface)
    todo_devices_with_tags: list[InternalDevice] = []
    # InternalDevice object in CV Inventory accessible via referencing device serial number (used for updating tags)
    todo_devices_by_serial_number: dict[str, InternalDevice] = {}

    # Build todo tags with CVDevice/CVInterfaceTag objects that exist on CloudVision. Add the rest to skipped.
    skipped_tags.extend(tag for tag in tags if tag.device is not None and not tag.device._exists_on_cv)
    todo_tags = [tag for tag in tags if tag.device is None or tag.device._exists_on_cv]

    # populate skipped tags in overall result and identify devices to be examined further
    for device in internal_devices:
        tags_matching_tag_type = device.avd_device.device_tags if tag_type == "device" else device.avd_device.interface_tags
        if not device.in_cv_inventory:
            if len(tags_matching_tag_type) > 0:
                if device.avd_device.hostname in skipped_tags_internal_devices:
                    skipped_tags_internal_devices[device.avd_device.hostname].extend(list(tags_matching_tag_type))
                else:
                    skipped_tags_internal_devices[device.avd_device.hostname] = list(tags_matching_tag_type)
                device.result.device_tags.skipped.extend(list(tags_matching_tag_type))
        else:
            if not device.serial_number:
                # we expect device.serial_number to be already populated (fetched from CV Inventory) when we get here
                # TODO: log some warning, this is not expected!!
                # Should we bail out here? Else we would need to repeat such validation check in rest of the wrappers
                LOGGER.info("deploy_tags_to_cv: (using internal devices) device %s in CV inventory, but has no serial number!", device.avd_device.hostname)
                deploy_tags_err_msg = "deploy_tags_to_cv(): Detected device in CV Inventory, but unable to fetch serial number!"
                raise CVClientException(deploy_tags_err_msg)

            todo_devices_by_serial_number[device.serial_number] = device
            # device is in inventory, add to list only if contains tag_type being looked up
            if len(tags_matching_tag_type) > 0:
                # given checks above, todo_devices_with_tags` will always contain devices with serial number
                todo_devices_with_tags.append(device)

    # No need to continue if we have nothing to do.
    if not todo_tags or (not todo_devices_with_tags):
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
        for tag in tags_matching_tag_type:
            if (tag.label, tag.value) not in existing_tags_tuples:
                tags_to_add_from_internal_devices.extend([(tag.label, tag.value)])

    LOGGER.info("deploy_tags_to_cv: (based on internal devices) Creating %s tags_to_add", len(tags_to_add_from_internal_devices))

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
                # update corr. tags placeholder for overall result
                if device.serial_number in deployed_tags_internal_devices:
                    deployed_tags_internal_devices[device.serial_number].extend([tag])
                else:
                    deployed_tags_internal_devices[device.serial_number] = [tag]
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
        LOGGER.info("deploy_tags_to_cv: (using internal devices) Creating tag assignments: len %s", len(todo_tag_assignments))
        await cv_client.set_tag_assignments(
            workspace_id=workspace.id,
            tag_assignments=todo_tag_assignments,
            element_type=tag_type,
        )
        # post-set_tag_assignments() successful completion,
        # proceed to update per-device and overall result with tags that were added via set_tag
        # TODO: check if this is correct approach
        for device in todo_devices_with_tags:
            tags_to_add_for_device = device.device_tags.to_add if tag_type == "device" else device.interface_tags.to_add
            result_placeholder_tags_added = device.result.device_tags.added if tag_type == "device" else device.result.interface_tags.added
            if tags_to_add_for_device:
                result_placeholder_tags_added.extend(tags_to_add_for_device)
                if device.serial_number in deployed_tags_internal_devices:
                    deployed_tags_internal_devices[device.serial_number].extend(tags_to_add_for_device)
                else:
                    deployed_tags_internal_devices[device.serial_number] = tags_to_add_for_device

    # Move all TODO: to deployed.
    deployed_tags.extend(todo_assignments)
    # deployed_tags_internal_devices already updated with tags identified to be added

    # Now we start removing assignments depending on strict_tags or not.

    
    # Build set of tuples for deployed tags.
    deployed_tags_tuples = {
        (tag.label, tag.value, tag.device.serial_number, getattr(tag, "interface", None)) for tag in deployed_tags if tag.device is not None
    }

    # build deployed_tags_tuples_internal_devices - set of tuples for deployed tags
    deployed_tags_tuples_internal_devices = {
        (tag.label, tag.value, device_serial_number, getattr(tag, "interface", None))
        for device_serial_number, list_of_tags in deployed_tags_internal_devices.items()
        for tag in list_of_tags
        # tag could be either device or interface tag filtered earlier based on tag_type
    }

    # TODO: remove this for debug only
    if deployed_tags_tuples != deployed_tags_tuples_internal_devices:
        deploy_tags_err_msg = "deploy_tags_to_cv(): Mismatch detected in deployed_tags_tuples! raising exception during deploy_tags_to_cv() step"
        deploy_tags_err_msg += (
            f" deployed_tags_tuples len: {len(deployed_tags_tuples)} vs deployed_tags_tuples_internal_devices len: {len(deployed_tags_tuples_internal_devices)}"
        )
        raise CVClientException(deploy_tags_err_msg)

    # Build a mapping of device serial number to CVDevice.
    devices_by_serial_number = {
        tag.device.serial_number: tag.device for tag in deployed_tags if tag.device is not None and tag.device.serial_number is not None
    }
    # use deployed_tags_internal_devices dict - key is device serial number

    # If strict, we remove any assignments not specified in the inputs.
    # If not strict, we remove any assignments with the same labels but not specified in the inputs.
    assignments_to_unassign_internal_devices = []
    if strict:
        LOGGER.debug("deploy_tags_to_cv: STRICT tags validation ENABLED for removing unassigned tags")
        assignments_to_unassign = {
            assignment for assignment in existing_assignments if assignment.device_id in devices_by_serial_number and assignment not in desired_assignments
        }
        # logic for populating assignments_to_unassign_internal_devices
        for label, value, device_serial_number, interface in existing_assignments:
            if (
                device_serial_number in deployed_tags_internal_devices
                and (label, value, device_serial_number, interface) not in deployed_tags_tuples_internal_devices
            ):
                assignments_to_unassign_internal_devices.append((label, value, device_serial_number, interface))
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
                device_serial_number in deployed_tags_internal_devices
                and label in deployed_tags_labels_internal_devices
                and (label, value, device_serial_number, interface) not in deployed_tags_tuples_internal_devices
            ):
                assignments_to_unassign_internal_devices.append((label, value, device_serial_number, interface))
                if device_serial_number in todo_devices_by_serial_number:
                    if tag_type == "device":
                        todo_devices_by_serial_number[device_serial_number].device_tags.to_remove.extend([AvdDeviceTag(label=label, value=value)])
                    else:
                        todo_devices_by_serial_number[device_serial_number].interface_tags.to_remove.extend(
                            [AvdInterfaceTag(label=label, value=value, interface=interface)]
                        )

    LOGGER.info(
        "deploy_tags_to_cv: assignments_to_unassign len: %s, (using internal devices) assignments_to_unassign len: %s",
        len(assignments_to_unassign),
        len(assignments_to_unassign_internal_devices),
    )

    # TODO: remove this, added for debug
    if assignments_to_unassign != assignments_to_unassign_internal_devices:
        # TODO: remove this , only for comparing revised logic with existing one
        deploy_tags_err_msg = "deploy_tags_to_cv(): Mismatch detected in assignments_to_unassign, raising exception during deploy_tags_to_cv() step"
        raise CVClientException(deploy_tags_err_msg)

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
            if serial_number in removed_tags_internal_devices:
                removed_tags_internal_devices[serial_number].extend([interface_tag])
            else:
                removed_tags_internal_devices[serial_number] = [interface_tag]
            if serial_number in todo_devices_by_serial_number:
                todo_devices_by_serial_number[serial_number].result.interface_tags.removed.extend([interface_tag])
        else:
            removed_tags.extend(
                CVDeviceTag(label=assignment.label, value=assignment.value, device=devices_by_serial_number[assignment.device_id])
                for assignment in sorted_assignments_to_unassign
            )
        # update removed tags using internal_devices approach
        for label, value, serial_number, _ in assignments_to_unassign_internal_devices:
            device_tag = AvdDeviceTag(label=label, value=value)
            if serial_number in removed_tags_internal_devices:
                removed_tags_internal_devices[serial_number].extend([device_tag])
            else:
                removed_tags_internal_devices[serial_number] = [device_tag]
            if serial_number in todo_devices_by_serial_number:
                todo_devices_by_serial_number[serial_number].result.device_tags.removed.extend([device_tag])
