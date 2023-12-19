# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json

from ..client import CVClient
from ..models import CVEosConfig, DeployToCvResult

CONFIGLET_ID_PREFIX = "avd-"
CONFIGLET_NAME_PREFIX = "AVD_"
CONFIGLET_CONTAINER_ID = f"{CONFIGLET_ID_PREFIX}configlets"
STATIC_CONFIGLET_STUDIO_ID = "studio-static-configlet"


async def deploy_configs_to_cv(configs: list[CVEosConfig], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given configs using "Static Configlet Studio"

    - Create/verify a single configuration container named "AVD Configurations".
    - Upload Configlets and assign to devices.

    TODO: See if this can be optimized to check if the configlets are already in place and correct. A hash would have been nice.
    TODO: Split long configs into multiple configlets for 990KB chunks. Need to figure out how to batch it.
    """

    if not configs:
        return

    # Build Todo with CVEosConfig objects that exist on CloudVision. Add the rest to skipped.
    result.skipped_configs.extend(config for config in configs if not config.device._exists_on_cv)
    todo_configs = [config for config in configs if config.device._exists_on_cv]

    # No need to continue if we have nothing to do.
    if not todo_configs:
        return

    # Get or create root level container for AVD configurations. Using the hardcoded id from CONFIGLET_CONTAINER_ID.
    cv_containers = await cv_client.get_configlet_containers(workspace_id=result.workspace.id, container_ids=[CONFIGLET_CONTAINER_ID])
    if not cv_containers:
        # Create the root level container
        await cv_client.set_configlet_container(
            workspace_id=result.workspace.id,
            container_id=CONFIGLET_CONTAINER_ID,
            display_name="AVD Configurations",
            description="Configurations created and uploaded by AVD",
            query="device:*",
        )
        # Add the root level container to the list of root level containers using the studio inputs API (!?!)
        root_containers: list = await cv_client.get_studio_inputs_with_path(
            studio_id=STATIC_CONFIGLET_STUDIO_ID, workspace_id=result.workspace.id, input_path=["configletAssignmentRoots"], default_value=[]
        )
        if CONFIGLET_CONTAINER_ID not in root_containers:
            root_containers.append(CONFIGLET_CONTAINER_ID)
            await cv_client.set_studio_inputs(
                studio_id=STATIC_CONFIGLET_STUDIO_ID,
                workspace_id=result.workspace.id,
                input_path=["configletAssignmentRoots"],
                inputs=json.dumps(root_containers),
            )
        cv_containers = await cv_client.get_configlet_containers(
            workspace_id=result.workspace.id,
            container_ids=[CONFIGLET_CONTAINER_ID],
        )

    existing_device_container_ids = cv_containers[0].child_assignment_ids.values
    update_device_container_ids = existing_device_container_ids.copy()

    # Bluntly setting everything like nothing was there.
    # Alternative would be to pull down all configlets and containers
    # to compare them with the target.
    for config in todo_configs:
        configlet_id = f"{CONFIGLET_ID_PREFIX}{config.device.serial_number}"
        await cv_client.set_configlet(
            workspace_id=result.workspace.id,
            configlet_id=configlet_id,
            display_name=config.configlet_name or f"{CONFIGLET_NAME_PREFIX}{config.device.hostname}",
            description=f"Configuration created and uploaded by AVD for {config.device.hostname}",
            body=config.config or "",
        )
        # Reusing configlet_id for container_id
        await cv_client.set_configlet_container(
            workspace_id=result.workspace.id,
            container_id=configlet_id,
            display_name=f"{config.device.hostname}",
            description=f"Configuration created and uploaded by AVD for {config.device.hostname}",
            query=f"device:{config.device.serial_number}",
            configlet_ids=[configlet_id],
        )
        if configlet_id not in update_device_container_ids:
            update_device_container_ids.append(f"{CONFIGLET_ID_PREFIX}{config.device.serial_number}")

        result.deployed_configs.append(config)

    # Update the device_container_ids on the root level container.
    if update_device_container_ids != existing_device_container_ids:
        await cv_client.set_configlet_container(
            workspace_id=result.workspace.id,
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=update_device_container_ids,
        )
