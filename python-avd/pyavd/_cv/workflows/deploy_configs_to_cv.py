# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import DeployToCvResult, InternalDevice

LOGGER = getLogger(__name__)

CONFIGLET_ID_PREFIX = "avd-"
CONFIGLET_NAME_PREFIX = "AVD_"
CONFIGLET_CONTAINER_ID = f"{CONFIGLET_ID_PREFIX}configlets"
STATIC_CONFIGLET_STUDIO_ID = "studio-static-configlet"


async def deploy_configs_to_cv(internal_devices: list[InternalDevice], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given configs using "Static Configlet Studio".

    - Create/verify a single configuration container named "AVD Configurations".
    - Upload Configlets and assign to devices.

    TODO: See if this can be optimized to check if the configlets are already in place and correct. A hash would have been nice.
    """
    LOGGER.info("deploy_configs_to_cv: %s devices to check for config", len(internal_devices))

    if not internal_devices:
        return

    # Build todo with InternalDevice objects that exist on CloudVision. Add the rest to skipped.
    todo_devices_with_configs: list[InternalDevice] = []
    for device in internal_devices:
        if not device.in_cv_inventory:
            result.skipped_configs.extend([device.get_cv_eos_config()])
            device.result.config.skipped.extend([device.avd_device.config])
            LOGGER.info("deploy_configs_to_cv: Skipping config for device %s missing in CloudVision Inventory", device.avd_device.hostname)
        else:
            todo_devices_with_configs.append(device)

    LOGGER.info("deploy_configs_to_cv: %s skipped configs because the devices are missing from CloudVision.", len(result.skipped_configs))
    LOGGER.debug("deploy_configs_to_cv: %s devices with config", len(todo_devices_with_configs))

    # No need to continue if we have nothing to do.
    if not todo_devices_with_configs:
        return

    # First create all configlets in parallel coroutines.
    await deploy_configlets_to_cv(todo_devices_with_configs, result.workspace.id, cv_client)
    # Next create all containers in parallel coroutines.
    await deploy_configlet_containers_to_cv(todo_devices_with_configs, result.workspace.id, cv_client)

    # consider all candidate configs as added/deployed and update result
    for device in todo_devices_with_configs:
        LOGGER.debug("deploy_configs_to_cv: config deployed for device: %s serial_num: %s", device.avd_device.hostname, device.serial_number)
        result.deployed_configs.extend([device.get_cv_eos_config()])
        device.result.config.added.extend([device.avd_device.config])


async def deploy_configlets_to_cv(internal_devices: list[InternalDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Bluntly setting configs like nothing was there. Only create missing containers.

    TODO: Fetch config checksums for existing configs and only upload what is needed.
    """
    configlets_devices = [
        (
            f"{CONFIGLET_ID_PREFIX}{device.serial_number}",
            device.avd_device.config.configlet_name or f"{CONFIGLET_NAME_PREFIX}{device.avd_device.hostname}",
            f"Configuration created and uploaded by AVD for {device.avd_device.hostname}",
            device.avd_device.config.file,
        )
        for device in internal_devices
    ]

    LOGGER.info("deploy_configlets_to_cv: Deploying %s configlets", len(configlets_devices))

    await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=configlets_devices)


async def get_existing_device_container_ids_from_root_container(workspace_id: str, cv_client: CVClient) -> list[str]:
    """
    Get or create root level container for AVD configurations. Using the hardcoded id from CONFIGLET_CONTAINER_ID.

    Then return the list of existing device container ids. (Always empty if we just created the root container).
    """
    root_cv_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id, container_ids=[CONFIGLET_CONTAINER_ID])
    LOGGER.info("get_or_create_configlet_root_container: Got AVD root container? %s", bool(root_cv_containers))
    if root_cv_containers:
        return root_cv_containers[0].child_assignment_ids.values

    # Create the root level container
    LOGGER.info("deploy_configs_to_cv: Creating AVD root container '%s'", CONFIGLET_CONTAINER_ID)
    await cv_client.set_configlet_container(
        workspace_id=workspace_id,
        container_id=CONFIGLET_CONTAINER_ID,
        display_name="AVD Configurations",
        description="Configurations created and uploaded by AVD",
        query="device:*",
    )
    # Add the root level container to the list of root level containers using the studio inputs API (!?!)
    root_containers: list = await cv_client.get_studio_inputs_with_path(
        studio_id=STATIC_CONFIGLET_STUDIO_ID,
        workspace_id=workspace_id,
        input_path=["configletAssignmentRoots"],
        default_value=[],
    )
    LOGGER.info("deploy_configs_to_cv: Found %s root containers.", len(root_containers))
    if CONFIGLET_CONTAINER_ID not in root_containers:
        LOGGER.info("deploy_configs_to_cv: AVD root container not assigned as root container in Static Config Studio. Inserting AVD container at the top.")
        # Inserting our container first, to allow reconcile and other static config containers to override the AVD config.
        root_containers.insert(0, CONFIGLET_CONTAINER_ID)
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGLET_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=root_containers,
        )
    return []


async def deploy_configlet_containers_to_cv(internal_devices: list[InternalDevice], workspace_id: str, cv_client: CVClient) -> None:
    """
    Identify existing containers and ensure they have the correct configuration.

    Then update/create as needed.

    TODO: Refactor to set_some on supported CV versions
    """
    if existing_device_container_ids := await get_existing_device_container_ids_from_root_container(workspace_id, cv_client):
        existing_device_containers = await cv_client.get_configlet_containers(
            workspace_id=workspace_id,
            container_ids=existing_device_container_ids,
        )
        LOGGER.info("deploy_configs_to_cv: %s existing device containers under AVD root container.", len(existing_device_containers))
        # Create dict keyed by container id with value of tuple containing key container parameters. Used later to detect changes.
        existing_device_containers_by_id = {
            cv_container.key.configlet_assignment_id: (
                cv_container.display_name,
                cv_container.description,
                cv_container.query,
                cv_container.configlet_ids.values,
            )
            for cv_container in existing_device_containers
        }
    else:
        existing_device_containers = []
        existing_device_containers_by_id = {}

    update_device_containers = []
    update_device_container_ids = set()
    for device in internal_devices:
        # For now we reuse configlet_id as container_id.
        container_id = configlet_id = f"{CONFIGLET_ID_PREFIX}{device.serial_number}"
        display_name = f"{device.avd_device.hostname}"
        description = f"Configuration created and uploaded by AVD for {device.avd_device.hostname}"
        query = f"device:{device.serial_number}"
        configlet_ids = [configlet_id]
        if existing_device_containers_by_id.get(container_id) != (display_name, description, query, configlet_ids):
            update_device_container_ids.add(container_id)
            update_device_containers.append((container_id, display_name, description, configlet_ids, query, None, None))

    LOGGER.info(
        "deploy_configlet_containers_to_cv: update_device_containers: %s, update_device_container_ids: %s",
        len(update_device_containers),
        len(update_device_container_ids),
    )
    if update_device_containers:
        LOGGER.info("deploy_configlet_containers_to_cv: Deploying %s configlet assignments.", len(update_device_containers))
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=update_device_containers)

    # Update any missing update_device_container_ids on the root level container.
    if not update_device_container_ids.issubset(existing_device_containers_by_id):
        LOGGER.info("deploy_configlet_containers_to_cv: Updating root container children.")
        await cv_client.set_configlet_container(
            workspace_id=workspace_id,
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=list(update_device_container_ids.union(existing_device_containers_by_id)),
        )
