# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger

from ...utils import batch
from ..client import CVClient
from .models import CVEosConfig, DeployToCvResult

LOGGER = getLogger(__name__)

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

    LOGGER.info("deploy_configs_to_cv: %s", len(configs))

    if not configs:
        return

    # Build Todo with CVEosConfig objects that exist on CloudVision. Add the rest to skipped.
    result.skipped_configs.extend(config for config in configs if not config.device._exists_on_cv)
    LOGGER.info("deploy_configs_to_cv: %s skipped configs because they devices are missing.", len(result.skipped_configs))
    todo_configs = [config for config in configs if config.device._exists_on_cv]
    LOGGER.info("deploy_configs_to_cv: %s todo configs.", len(todo_configs))

    # No need to continue if we have nothing to do.
    if not todo_configs:
        return

    # Get or create root level container for AVD configurations. Using the hardcoded id from CONFIGLET_CONTAINER_ID.
    cv_containers = await cv_client.get_configlet_containers(workspace_id=result.workspace.id, container_ids=[CONFIGLET_CONTAINER_ID])
    LOGGER.info("deploy_configs_to_cv: Got AVD root container? %s", bool(cv_containers))
    if not cv_containers:
        # Create the root level container
        LOGGER.info("deploy_configs_to_cv: Creating AVD root container '%s'", CONFIGLET_CONTAINER_ID)
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
        LOGGER.info("deploy_configs_to_cv: Found %s root containers.", len(root_containers))
        if CONFIGLET_CONTAINER_ID not in root_containers:
            LOGGER.info("deploy_configs_to_cv: AVD root container not assigned as root container in Static Config Studio. Fixing...")
            root_containers.append(CONFIGLET_CONTAINER_ID)
            await cv_client.set_studio_inputs(
                studio_id=STATIC_CONFIGLET_STUDIO_ID,
                workspace_id=result.workspace.id,
                input_path=["configletAssignmentRoots"],
                inputs=root_containers,
            )
        cv_containers = await cv_client.get_configlet_containers(
            workspace_id=result.workspace.id,
            container_ids=[CONFIGLET_CONTAINER_ID],
        )

    existing_device_container_ids = cv_containers[0].child_assignment_ids.values
    LOGGER.info("deploy_configs_to_cv: %s existing device containers under AVD root container.", len(existing_device_container_ids))
    update_device_container_ids = existing_device_container_ids.copy()

    # Bluntly setting everything like nothing was there.
    # Alternative would be to pull down all configlets and containers
    # to compare them with the target.
    configlet_coroutines = []
    container_coroutines = []
    for config in todo_configs:
        # For now we reuse configlet_id as container_id.
        container_id = configlet_id = f"{CONFIGLET_ID_PREFIX}{config.device.serial_number}"
        configlet_coroutines.append(
            cv_client.set_configlet_from_file(
                workspace_id=result.workspace.id,
                configlet_id=configlet_id,
                file=config.file,
                display_name=config.configlet_name or f"{CONFIGLET_NAME_PREFIX}{config.device.hostname}",
                description=f"Configuration created and uploaded by AVD for {config.device.hostname}",
            )
        )
        container_coroutines.append(
            cv_client.set_configlet_container(
                workspace_id=result.workspace.id,
                container_id=container_id,
                display_name=f"{config.device.hostname}",
                description=f"Configuration created and uploaded by AVD for {config.device.hostname}",
                query=f"device:{config.device.serial_number}",
                configlet_ids=[configlet_id],
            )
        )
        if container_id not in update_device_container_ids:
            update_device_container_ids.append(container_id)

        result.deployed_configs.append(config)

    # First create all configlets in parallel coroutines.
    LOGGER.info("deploy_configs_to_cv: Deploying %s configlets in batches of 20.", len(configlet_coroutines))
    for index, coroutines in enumerate(batch(configlet_coroutines, 20), start=1):
        LOGGER.info("deploy_configs_to_cv: Batch %s", index)
        await gather(*coroutines)
    # Next create all containers in parallel coroutines.
    LOGGER.info("deploy_configs_to_cv: Deploying %s configlet assignments / containers in batches of 20.", len(container_coroutines))
    for index, coroutines in enumerate(batch(container_coroutines, 20), start=1):
        LOGGER.info("deploy_configs_to_cv: Batch %s", index)
        await gather(*coroutines)

    # Update the device_container_ids on the root level container.
    if update_device_container_ids != existing_device_container_ids:
        LOGGER.info("deploy_configs_to_cv: Updating root container children.")
        await cv_client.set_configlet_container(
            workspace_id=result.workspace.id,
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=update_device_container_ids,
        )
