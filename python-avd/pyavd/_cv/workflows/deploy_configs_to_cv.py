# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVDeviceDeployment, CVEosConfig, DeployToCvResult

LOGGER = getLogger(__name__)

CONFIGLET_ID_PREFIX = "avd-"
CONFIGLET_NAME_PREFIX = "AVD_"
CONFIGLET_CONTAINER_ID = f"{CONFIGLET_ID_PREFIX}configlets"
STATIC_CONFIGLET_STUDIO_ID = "studio-static-configlet"


async def deploy_configs_to_cv(configs: list[CVEosConfig], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy given configs using "Static Configlet Studio".

    - Create/verify a single configuration container named "AVD Configurations".
    - Upload Configlets and assign to devices.

    TODO: See if this can be optimized to check if the configlets are already in place and correct. A hash would have been nice.
    """
    LOGGER.info("deploy_configs_to_cv: %s", len(configs))

    if not configs:
        return

    # Build todo with CVEosConfig objects that exist on CloudVision. Add the rest to skipped.
    result.skipped_configs.extend(config for config in configs if not config.device.exists_on_cv)
    LOGGER.info("deploy_configs_to_cv: %s skipped configs because the devices are missing from CloudVision.", len(result.skipped_configs))
    todo_configs = [config for config in configs if config.device.exists_on_cv]
    LOGGER.info("deploy_configs_to_cv: %s todo configs.", len(todo_configs))

    # No need to continue if we have nothing to do.
    if not todo_configs:
        return

    # First create all configlets in parallel coroutines.
    await deploy_configlets_to_cv(todo_configs, result.workspace.id, cv_client)
    # Next create all containers in parallel coroutines.
    await deploy_configlet_containers_to_cv(todo_configs, result.workspace.id, cv_client)

    result.deployed_configs.extend(todo_configs)


async def deploy_configlets_to_cv(configs: list[CVEosConfig], workspace_id: str, cv_client: CVClient) -> None:
    """
    Bluntly setting configs like nothing was there. Only create missing containers.

    TODO: Fetch config checksums for existing configs and only upload what is needed.
    """
    configlets = [
        (
            f"{CONFIGLET_ID_PREFIX}{config.device.serial_number}",
            config.configlet_name or f"{CONFIGLET_NAME_PREFIX}{config.device.hostname}",
            f"Configuration created and uploaded by AVD for {config.device.hostname}",
            config.file,
        )
        for config in configs
    ]
    LOGGER.info("deploy_configs_to_cv: Deploying %s configlets.", len(configlets))
    await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=configlets)


async def get_existing_device_container_ids_from_root_container(workspace_id: str, cv_client: CVClient) -> list[str]:
    """
    Get or create root level container for AVD configurations. Using the hardcoded id from CONFIGLET_CONTAINER_ID.

    Always make sure that AVD root level container is a part of the configletAssignmentRoots.

    Then return the list of existing device container ids. (Always empty if we just created the root container).
    """
    root_cv_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id, container_ids=[CONFIGLET_CONTAINER_ID])
    LOGGER.info("get_or_create_configlet_root_container: Got AVD root container? %s", bool(root_cv_containers))

    child_assignment_ids: list[str] = []
    if root_cv_containers:
        child_assignment_ids = root_cv_containers[0].child_assignment_ids.values
    else:
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
    return child_assignment_ids


async def deploy_configlet_containers_to_cv(configs: list[CVEosConfig], workspace_id: str, cv_client: CVClient) -> None:
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
    for config in configs:
        # For now we reuse configlet_id as container_id.
        container_id = configlet_id = f"{CONFIGLET_ID_PREFIX}{config.device.serial_number}"
        display_name = f"{config.device.hostname}"
        description = f"Configuration created and uploaded by AVD for {config.device.hostname}"
        query = f"device:{config.device.serial_number}"
        configlet_ids = [configlet_id]
        if existing_device_containers_by_id.get(container_id) != (display_name, description, query, configlet_ids):
            update_device_container_ids.add(container_id)
            update_device_containers.append((container_id, display_name, description, configlet_ids, query, None, None))

    if update_device_containers:
        LOGGER.info("deploy_configs_to_cv: Deploying %s configlet assignments.", len(update_device_containers))
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=update_device_containers)

    # Update any missing update_device_container_ids on the root level container.
    if not update_device_container_ids.issubset(existing_device_containers_by_id):
        LOGGER.info("deploy_configs_to_cv: Updating root container children.")
        await cv_client.set_configlet_container(
            workspace_id=workspace_id,
            container_id=CONFIGLET_CONTAINER_ID,
            child_assignment_ids=list(update_device_container_ids.union(existing_device_containers_by_id)),
        )


async def delete_configs_from_cv(device_deployments: list[CVDeviceDeployment], result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Delete leftovers device configurations from a previous `deploy_configs_to_cv` run.

    For devices with `use_static_config_manifest=True`, the device configuration is expected to be deployed
    via the static config manifest instead of the flat "AVD Configurations" layout. This function removes
    the corresponding container (avd-<serial>) and configlet for these devices if they exist.

    If all children are removed, the root container itself is deleted and unregistered from the Studio
    """
    workspace_id = result.workspace.id

    # Build a stable list of target IDs from manifest-opted devices.
    target_ids = [
        f"{CONFIGLET_ID_PREFIX}{device_deployment.device.serial_number}"
        for device_deployment in device_deployments
        if device_deployment.use_static_config_manifest and device_deployment.device.serial_number
    ]
    if not target_ids:
        return
    target_ids_set = set(target_ids)

    # Find what actually exists on CV for our targets and the root container.
    existing_configlets, existing_containers = await gather(
        cv_client.get_configlets(workspace_id=workspace_id, configlet_ids=target_ids),
        cv_client.get_configlet_containers(workspace_id=workspace_id, container_ids=[*target_ids, CONFIGLET_CONTAINER_ID]),
    )

    configlets_by_id = {cast("str", configlet.key.configlet_id): configlet for configlet in existing_configlets}
    containers_by_id = {cast("str", container.key.configlet_assignment_id): container for container in existing_containers}
    root_cv_container = containers_by_id.pop(CONFIGLET_CONTAINER_ID, None)

    # Delete leftover per-device containers and configlets in parallel.
    delete_coroutines = [cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id) for container_id in containers_by_id]
    if configlets_by_id:
        delete_coroutines.append(cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(configlets_by_id)))

    if delete_coroutines:
        LOGGER.info(
            "delete_configs_from_cv: Removing %s device containers and %s configlets.",
            len(containers_by_id),
            len(configlets_by_id),
        )
        await gather(*delete_coroutines)

    result.removed_configs.extend(cast("str", configlet.display_name) for configlet in configlets_by_id.values())

    # Reconcile the root "AVD Configurations" container if it exists.
    if root_cv_container is None:
        return

    existing_child_ids = root_cv_container.child_assignment_ids.values
    remaining_child_ids = [child_id for child_id in existing_child_ids if child_id not in target_ids_set]

    if remaining_child_ids:
        # Root still has non-target children. Update its child list only if we actually removed something.
        if remaining_child_ids != list(existing_child_ids):
            LOGGER.info("delete_configs_from_cv: Updating root container children (%s remaining).", len(remaining_child_ids))
            await cv_client.set_configlet_container(
                workspace_id=workspace_id,
                container_id=CONFIGLET_CONTAINER_ID,
                child_assignment_ids=remaining_child_ids,
            )
        return

    # No remaining children, delete the root container and unregister from studio roots.
    LOGGER.info("delete_configs_from_cv: All device containers removed. Cleaning up root container.")
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
