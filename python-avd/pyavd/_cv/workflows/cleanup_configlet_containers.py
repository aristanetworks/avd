# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger
from typing import TYPE_CHECKING

from .deploy_configs_to_cv import CONFIGLET_CONTAINER_ID, CONFIGLET_ID_PREFIX, STATIC_CONFIGLET_STUDIO_ID

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVDeviceDeployment, DeployToCvResult

LOGGER = getLogger(__name__)


async def cleanup_configlet_containers(device_deployments: list[CVDeviceDeployment], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Clean up configlet containers and configlets created by the `deploy_configs_to_cv` workflow.

    For devices with `use_static_config_manifest=True`, the device configuration is expected to be deployed
    via the static config manifest instead of the flat "AVD Configurations" layout. This function removes
    the corresponding container (avd-<serial>) and configlet from the "AVD Configurations" root container
    if they exist.

    If all children are removed, the root container itself is deleted and unregistered from the Studio.
    """
    # Build a stable list of target IDs from manifest-opted devices.
    target_ids = [
        f"{CONFIGLET_ID_PREFIX}{device_deployment.device.serial_number}"
        for device_deployment in device_deployments
        if device_deployment.use_static_config_manifest and device_deployment.device.serial_number
    ]
    if not target_ids:
        return

    workspace_id = result.workspace.id

    # Fetch the root container to get existing child IDs.
    root_cv_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id, container_ids=[CONFIGLET_CONTAINER_ID])
    if not root_cv_containers:
        # Root container doesn't exist, nothing to clean up.
        return

    existing_child_ids = root_cv_containers[0].child_assignment_ids.values
    existing_child_ids_set = set(existing_child_ids)

    # Only remove containers that actually exist on CV, preserving order from target_ids.
    containers_to_remove = [cid for cid in target_ids if cid in existing_child_ids_set]
    if not containers_to_remove:
        return

    LOGGER.info("cleanup_configlet_containers: Removing %s device containers.", len(containers_to_remove))

    # Delete the containers and their associated configlets (same avd-<serial> IDs).
    await gather(*[cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id) for container_id in containers_to_remove])
    await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=containers_to_remove)

    result.removed_configs.extend(containers_to_remove)

    # Update root container child list, preserving the original order.
    containers_to_remove_set = set(containers_to_remove)
    remaining_child_ids = [cid for cid in existing_child_ids if cid not in containers_to_remove_set]

    if remaining_child_ids:
        # Update the root container with the reduced child list.
        LOGGER.info("cleanup_configlet_containers: Updating root container children (%s remaining).", len(remaining_child_ids))
        await cv_client.set_configlet_container(
            workspace_id=workspace_id,
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=remaining_child_ids,
        )
    else:
        # All children removed, delete the root container and unregister from studio roots.
        LOGGER.info("cleanup_configlet_containers: All device containers removed. Cleaning up root container.")
        await cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=CONFIGLET_CONTAINER_ID)

        root_containers: list = await cv_client.get_studio_inputs_with_path(
            studio_id=STATIC_CONFIGLET_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            default_value=[],
        )
        if CONFIGLET_CONTAINER_ID in root_containers:
            root_containers.remove(CONFIGLET_CONTAINER_ID)
            await cv_client.set_studio_inputs(
                studio_id=STATIC_CONFIGLET_STUDIO_ID,
                workspace_id=workspace_id,
                input_path=["configletAssignmentRoots"],
                inputs=root_containers,
            )
