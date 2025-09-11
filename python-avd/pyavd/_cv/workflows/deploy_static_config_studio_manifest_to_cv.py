# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger
from typing import TYPE_CHECKING, cast

from .models import AVD_ENTITY_PREFIX, CVManifest

if TYPE_CHECKING:
    from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment
    from pyavd._cv.client import CVClient

    from .models import AvdManifest, CVContainer, DeployToCvResult

LOGGER = getLogger(__name__)


STATIC_CONFIGURATION_STUDIO_ID = "studio-static-configlet"


async def deploy_static_config_studio_manifest_to_cv(manifest: AvdManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy a manifest (configlets/containers) to CloudVision using the "Static Configuration" Studio.

    TODO: Implement strict mode to remove any containers/configlets not managed by AVD from the Studio.
    TODO: Implement configlet body diff - digest/checksum.
    """
    workspace_id = deployment_result.workspace.id
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Starting manifest deployment for workspace '%s'.", workspace_id)

    # Build the desired CloudVision manifest from the AVD manifest.
    cv_manifest = CVManifest.from_avd_manifest(manifest)

    LOGGER.info(
        "deploy_static_config_studio_manifest_to_cv: Calculated desired state: %d containers and %d unique configlets.",
        len(cv_manifest.containers),
        len(cv_manifest.configlets),
    )
    if not cv_manifest.configlets and not cv_manifest.containers:
        return

    # Perform synchronization tasks.
    await _sync_configlets(cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client)
    existing_containers_by_id = await _sync_containers(cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client)
    await _sync_studio_roots(
        cv_manifest=cv_manifest,
        deployment_result=deployment_result,
        cv_client=cv_client,
        existing_containers_by_id=existing_containers_by_id,
    )

    # Done.
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Completed manifest deployment for workspace '%s'.", workspace_id)


async def _sync_containers(cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> dict[str, ConfigletAssignment]:
    """Synchronize containers. Fetch existing ones and push any required creates or updates."""
    workspace_id = deployment_result.workspace.id

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching all existing configlet containers from CloudVision...")
    existing_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id)
    existing_containers_by_id = {cast("str", container.key.configlet_assignment_id): container for container in existing_containers}

    containers_to_push: list[CVContainer] = []
    for desired_container in cv_manifest.containers:
        existing_container = existing_containers_by_id.get(desired_container.id)

        # Container is new or has changed, so it needs to be pushed.
        if not existing_container or not desired_container.matches_configlet_assignment(existing_container):
            containers_to_push.append(desired_container)
        else:
            # Container is unchanged.
            deployment_result.skipped_static_config_containers.append(desired_container.avd_container)

    if containers_to_push:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d containers (create/update)...", len(containers_to_push))
        deployment_result.deployed_static_config_containers.extend(container.avd_container for container in containers_to_push)
        container_tuples = [container.api_tuple for container in containers_to_push]
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=container_tuples)
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No container creations or updates are needed.")

    # Return all existing containers from CloudVision to be further processed if needed.
    return existing_containers_by_id


async def _sync_configlets(cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """Synchronize configlets. Create/update new ones and delete unused AVD-managed ones."""
    workspace_id = deployment_result.workspace.id

    # Create or update configlets.
    if cv_manifest.configlets:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d configlets (create/update)...", len(cv_manifest.configlets))
        deployment_result.deployed_static_config_configlets.extend(configlet.avd_configlet for configlet in cv_manifest.configlets)
        configlet_tuples = [configlet.api_tuple for configlet in cv_manifest.configlets]
        await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=configlet_tuples)
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No configlet creations or updates are needed.")

    # Delete unused AVD-managed configlets.
    existing_configlets = await cv_client.get_configlets(workspace_id=workspace_id)
    desired_configlet_ids = {configlet.id for configlet in cv_manifest.configlets}
    configlets_to_delete = {
        configlet_id: cast("str", configlet.display_name)
        for configlet in existing_configlets
        if (configlet_id := cast("str", configlet.key.configlet_id)).startswith(AVD_ENTITY_PREFIX) and configlet_id not in desired_configlet_ids
    }

    if configlets_to_delete:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Removing %d AVD-managed configlets which are no longer used.", len(configlets_to_delete))
        deployment_result.removed_static_config_configlets.extend(configlets_to_delete.values())
        await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(configlets_to_delete.keys()))
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No AVD-managed configlet deletions are needed.")


async def _sync_studio_roots(
    cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient, existing_containers_by_id: dict[str, ConfigletAssignment]
) -> None:
    """
    Synchronize Studio root containers. Update root container assignments and delete unused AVD-managed ones.

    Note:
        During an update, this function reorders root containers. All AVD-managed
        containers are placed first, followed by any existing manually-added containers.
    """
    workspace_id = deployment_result.workspace.id

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Syncing Static Config Studio root container assignments...")

    # Get the existing list of root container IDs from the Studio inputs.
    existing_root_ids: list[str] = await cv_client.get_studio_inputs_with_path(
        studio_id=STATIC_CONFIGURATION_STUDIO_ID,
        workspace_id=workspace_id,
        input_path=["configletAssignmentRoots"],
        default_value=[],
    )

    # Calculate which desired roots are missing and which existing AVD-managed roots are stale.
    desired_root_ids = [container.id for container in cv_manifest.containers if container.is_root]
    desired_root_ids_set = set(desired_root_ids)
    existing_root_ids_set = set(existing_root_ids)
    missing_ids = desired_root_ids_set - existing_root_ids_set
    stale_avd_ids = {
        container_id for container_id in existing_root_ids_set if container_id.startswith(AVD_ENTITY_PREFIX) and container_id not in desired_root_ids_set
    }

    # Update the Studio root container list if necessary, preserving any manually added (non-AVD) root containers.
    if missing_ids or stale_avd_ids:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Updating Studio root container assignment list...")
        manual_ids = [container_id for container_id in existing_root_ids if not container_id.startswith(AVD_ENTITY_PREFIX)]
        new_ordered_ids = desired_root_ids + manual_ids

        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=new_ordered_ids,
        )
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Studio root container assignments are already in the desired state.")

    # Delete stale AVD-managed root containers that are no longer needed.
    if stale_avd_ids:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Removing %d stale AVD-managed root containers...", len(stale_avd_ids))
        deployment_result.removed_static_config_root_containers.extend(
            [
                cast("str", existing_container.display_name)
                for container_id in stale_avd_ids
                if (existing_container := existing_containers_by_id.get(container_id)) is not None
            ]
        )

        # TODO: Build a 'delete_configlet_containers' gRPC API
        await gather(*[cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id) for container_id in stale_avd_ids])
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No AVD-managed root container deletions are needed.")
