# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from collections import deque
from dataclasses import replace
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

    Workflow:
        + Sync configlets.
            - Create or update all configlets declared in the manifest.
            - Delete any AVD-managed configlets not in the manifest.
        + Sync containers.
            - Fetch existing state (containers + root list) from CloudVision.
            - Compute the final state by layering the manifest on top of the existing state.
                - For each container, `child_policy` controls how its children are resolved:
                    - "strict": Replace children entirely with what is declared. Both AVD-managed and manual
                      children not in the manifest are removed. A warning is logged for unassigned manual children.
                    - "selective": Only undeclared AVD-managed children are removed. Manual children are preserved.
                    - "loose": Desired children are merged into existing children. Nothing is removed.
                - `root_policy` controls how the Studio root container list is resolved:
                    - "strict": Replace the root list entirely with what is declared.
                    - "selective": Only undeclared AVD-managed roots are removed. Manual roots are preserved.
                    - "loose": Desired roots are prepended to the existing list. Nothing is removed.
            - Determine which containers are reachable from the final roots.
            - Diff final vs existing and apply changes (push, delete, update root list).
                - Any AVD-managed container unreachable from the final root list (orphan) is always deleted.

    TODO: Implement strict mode to remove any configlets not managed by AVD from the Studio.
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
    await _sync_containers(cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client)

    # Done.
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Completed manifest deployment for workspace '%s'.", workspace_id)


async def _sync_containers(cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """Synchronize containers. Fetch existing ones and push any required creates or updates."""
    workspace_id = deployment_result.workspace.id

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching all existing configlet containers from CloudVision...")
    existing_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id)
    existing_containers_by_id = {cast("str", container.key.configlet_assignment_id): container for container in existing_containers}

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching the existing list of root container IDs from the Studio inputs...")
    existing_root_ids: list[str] = await cv_client.get_studio_inputs_with_path(
        studio_id=STATIC_CONFIGURATION_STUDIO_ID,
        workspace_id=workspace_id,
        input_path=["configletAssignmentRoots"],
        default_value=[],
    )

    # Compute the final state.
    final_child_ids_by_container_id, final_root_ids = _get_final_container_state(cv_manifest, existing_containers_by_id, existing_root_ids)

    # Determine which containers are reachable from the final roots.
    reachable_container_ids = _get_reachable_container_ids(final_child_ids_by_container_id, final_root_ids)

    LOGGER.info(
        "deploy_static_config_studio_manifest_to_cv: Final state: %d reachable containers, %d root containers.",
        len(reachable_container_ids),
        len(final_root_ids),
    )

    # Determine which desired containers need to be pushed (created or updated).
    containers_to_push: list[CVContainer] = []
    for desired_container in cv_manifest.containers:
        final_child_ids = tuple(final_child_ids_by_container_id.get(desired_container.id, desired_container.child_ids))
        final_container = replace(desired_container, child_ids=final_child_ids)
        existing_container = existing_containers_by_id.get(desired_container.id)

        # Container is new or has changed, so it needs to be pushed.
        if not existing_container or not final_container.matches_configlet_assignment(existing_container):
            containers_to_push.append(final_container)
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

    # Delete unused AVD-managed containers.
    containers_to_delete = {
        container_id: cast("str", container.display_name)
        for container_id, container in existing_containers_by_id.items()
        if container_id.startswith(AVD_ENTITY_PREFIX) and container_id not in reachable_container_ids
    }

    if containers_to_delete:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Removing %d AVD-managed containers which are no longer used.", len(containers_to_delete))
        deployment_result.removed_static_config_containers.extend(containers_to_delete.values())
        # TODO: Build a 'delete_configlet_containers' gRPC API
        await gather(*[cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id) for container_id in containers_to_delete])
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No AVD-managed container deletions are needed.")

    # Update the Studio root list if it has changed.
    if final_root_ids != existing_root_ids:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Updating Studio root container assignment list...")
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=final_root_ids,
        )
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Studio root container assignments are already in the desired state.")


def _get_final_container_state(
    cv_manifest: CVManifest,
    existing_containers_by_id: dict[str, ConfigletAssignment],
    existing_root_ids: list[str],
) -> tuple[dict[str, list[str]], list[str]]:
    """
    Compute the final (post-deployment) container state by layering the manifest on top of the existing state.

    See `deploy_static_config_studio_manifest_to_cv` docstring for details on `child_policy` and `root_policy` behavior.

    Returns the final child_ids for every container and the final root list.
    """
    # Start with existing children as the baseline for all known containers.
    final_child_ids_by_container_id = {
        container_id: list(container.child_assignment_ids.values) for container_id, container in existing_containers_by_id.items()
    }

    for desired_container in cv_manifest.containers:
        existing_container = existing_containers_by_id.get(desired_container.id)
        existing_child_ids = list(existing_container.child_assignment_ids.values) if existing_container else []

        if desired_container.child_policy == "strict":
            final_child_ids_by_container_id[desired_container.id] = list(desired_container.child_ids)

            # Log a warning if a strict container is about to unassign manually managed children.
            # TODO: Consider moving this block to a helper.
            desired_child_ids = set(desired_container.child_ids)
            orphaned_manual_child_ids = {
                child_id for child_id in existing_child_ids if child_id not in desired_child_ids and not child_id.startswith(AVD_ENTITY_PREFIX)
            }
            if orphaned_manual_child_ids:
                # Build human-readable details with both display name and ID for each orphaned manual child.
                orphaned_details = {
                    f"{cast('str', existing_containers_by_id[child_id].display_name)} ({child_id})" if child_id in existing_containers_by_id else child_id
                    for child_id in orphaned_manual_child_ids
                }
                LOGGER.warning(
                    "Container '%s' (%s) has child_policy='strict'. The following manually managed child containers will be unassigned from the hierarchy: %s",
                    desired_container.name,
                    desired_container.id,
                    ", ".join(orphaned_details),
                )

        elif desired_container.child_policy == "selective":
            preserved_manual_child_ids = [child_id for child_id in existing_child_ids if not child_id.startswith(AVD_ENTITY_PREFIX)]
            final_child_ids_by_container_id[desired_container.id] = list(dict.fromkeys(list(desired_container.child_ids) + preserved_manual_child_ids))

        else:
            final_child_ids_by_container_id[desired_container.id] = list(dict.fromkeys(list(desired_container.child_ids) + existing_child_ids))

    # Compute the final root list based on root_policy.
    desired_root_ids = [container.id for container in cv_manifest.containers if container.is_root]

    if cv_manifest.root_policy == "strict":
        final_root_ids = desired_root_ids
    elif cv_manifest.root_policy == "selective":
        manual_root_ids = [root_id for root_id in existing_root_ids if not root_id.startswith(AVD_ENTITY_PREFIX)]
        final_root_ids = desired_root_ids + manual_root_ids
    else:
        final_root_ids = list(dict.fromkeys(desired_root_ids + existing_root_ids))

    return final_child_ids_by_container_id, final_root_ids


def _get_reachable_container_ids(final_child_ids_by_container_id: dict[str, list[str]], final_root_ids: list[str]) -> set[str]:
    """BFS traversal from the final roots to find all reachable container IDs."""
    reachable_container_ids: set[str] = set()
    traversal_queue: deque[str] = deque(final_root_ids)

    while traversal_queue:
        container_id = traversal_queue.popleft()
        if container_id in reachable_container_ids:
            continue
        reachable_container_ids.add(container_id)
        traversal_queue.extend(final_child_ids_by_container_id.get(container_id, []))

    return reachable_container_ids


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
