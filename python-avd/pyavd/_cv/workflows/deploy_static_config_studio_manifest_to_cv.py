# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from collections import defaultdict, deque
from logging import getLogger
from typing import TYPE_CHECKING, cast

from pyavd._cv.client.exceptions import CVManifestError

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
    TODO: Replace the existing_containers / existing_managed_containers_by_id pair carried between sync functions with an
          ExistingState dataclass holding pre-computed mappings (containers_by_id, parents_by_child_id, etc.).
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
    existing_containers, existing_managed_containers_by_id, unmanaged_orphan_container_ids = await _sync_containers(
        cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client
    )
    await _sync_configlets(
        cv_manifest=cv_manifest,
        existing_containers=existing_containers,
        existing_managed_containers_by_id=existing_managed_containers_by_id,
        unmanaged_orphan_container_ids=unmanaged_orphan_container_ids,
        deployment_result=deployment_result,
        cv_client=cv_client,
    )
    await _sync_studio_roots(cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client)

    # Done.
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Completed manifest deployment for workspace '%s'.", workspace_id)


async def _sync_containers(
    cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient
) -> tuple[list[ConfigletAssignment], dict[str, str], set[str]]:
    """
    Synchronize containers. Fetch existing ones and push any required creates or updates.

    TODO: Split into multiple functions.
    """
    workspace_id = deployment_result.workspace.id

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching all existing configlet containers from CloudVision...")
    existing_containers = await cv_client.get_configlet_containers(workspace_id=workspace_id)

    existing_containers_by_id: dict[str, ConfigletAssignment] = {}
    existing_parents_by_child_id: dict[str, ConfigletAssignment] = {}
    existing_children_by_parent_id: dict[str, list[str]] = {}
    existing_managed_containers_by_id: dict[str, str] = {}

    for container in existing_containers:
        container_id = cast("str", container.key.configlet_assignment_id)
        existing_containers_by_id[container_id] = container
        existing_children_by_parent_id[container_id] = list(container.child_assignment_ids.values)
        if container_id.startswith(AVD_ENTITY_PREFIX):
            existing_managed_containers_by_id[container_id] = cast("str", container.display_name)
        for child_id in container.child_assignment_ids.values:
            existing_parents_by_child_id[child_id] = container

    containers_to_push: list[CVContainer] = []
    containers_to_skip: list[CVContainer] = []
    containers_to_delete: dict[str, str] = {}
    unmanaged_orphan_container_ids: set[str] = set()

    for desired_container in cv_manifest.containers:
        existing_container = existing_containers_by_id.get(desired_container.id)

        if not existing_container:
            # Container is new.
            containers_to_push.append(desired_container)
            continue

        if not desired_container.matches_configlet_assignment(existing_container):
            # Container has changed.
            containers_to_push.append(desired_container)
        else:
            # Container is unchanged.
            containers_to_skip.append(desired_container)

        # Existing unmanaged children unassigned by the manifest become orphans.
        existing_children = set(existing_container.child_assignment_ids.values)
        desired_children = set(desired_container.child_ids)
        unmanaged_orphan_container_ids.update(child_id for child_id in (existing_children - desired_children) if not child_id.startswith(AVD_ENTITY_PREFIX))

    # Managed containers no longer in the manifest are deleted. Their unmanaged children also become orphans and are deleted.
    desired_container_ids = {container.id for container in cv_manifest.containers}
    for container_id, container_name in existing_managed_containers_by_id.items():
        if container_id in desired_container_ids:
            continue
        containers_to_delete[container_id] = container_name
        unmanaged_orphan_container_ids.update(
            child_id for child_id in existing_children_by_parent_id.get(container_id, []) if not child_id.startswith(AVD_ENTITY_PREFIX)
        )

    # Walk the unmanaged orphans to pull in their descendants.
    # Managed descendants are skipped because they are either re-parented by the push or already in containers_to_delete.
    queue = deque(unmanaged_orphan_container_ids)
    while queue:
        container_id = queue.popleft()
        for child_id in existing_children_by_parent_id.get(container_id, []):
            if child_id.startswith(AVD_ENTITY_PREFIX) or child_id in unmanaged_orphan_container_ids:
                continue
            unmanaged_orphan_container_ids.add(child_id)
            queue.append(child_id)

    # Merge unmanaged orphan IDs into containers_to_delete with their CV display names.
    for orphan_id in unmanaged_orphan_container_ids:
        containers_to_delete[orphan_id] = cast("str", existing_containers_by_id[orphan_id].display_name)

    # Validate that no managed container was manually reassigned to a parent this deploy will not touch.
    violations: list[tuple[str, str, str, str]] = []
    for child_id, child_name in existing_managed_containers_by_id.items():
        parent = existing_parents_by_child_id.get(child_id)
        if parent is None:
            # No existing parent means it's in the Studio root list which _sync_studio_roots will reconcile,
            # or it's an orphan which will get reassigned or deleted by this deploy.
            continue
        parent_id = cast("str", parent.key.configlet_assignment_id)
        if parent_id in existing_managed_containers_by_id or parent_id in unmanaged_orphan_container_ids:
            # Parent is managed and will be handled by this deploy, or is unmanaged and scheduled for orphan deletion.
            continue

        # Parent is out of our control.
        violations.append((cast("str", parent.display_name), parent_id, child_name, child_id))

    if violations:
        violations.sort()
        violations_text = "; ".join(
            f"'{child_name}' (id={child_id}) is currently a child of '{parent_name}' (id={parent_id})"
            for parent_name, parent_id, child_name, child_id in violations
        )
        msg = (
            "The following manifest-managed containers were manually reassigned to parents that this manifest does not control. "
            f"Remove these parent assignments and re-run: {violations_text}"
        )
        raise CVManifestError(msg)

    deployment_result.skipped_static_config_containers.extend(container.avd_container for container in containers_to_skip)

    if containers_to_push:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d containers (create/update)...", len(containers_to_push))
        deployment_result.deployed_static_config_containers.extend(container.avd_container for container in containers_to_push)
        container_tuples = [container.api_tuple for container in containers_to_push]
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=container_tuples)
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No container creations or updates are needed.")

    if containers_to_delete:
        LOGGER.info(
            "deploy_static_config_studio_manifest_to_cv: Removing %d manifest-managed and %d unmanaged orphan containers which are no longer used.",
            len(containers_to_delete) - len(unmanaged_orphan_container_ids),
            len(unmanaged_orphan_container_ids),
        )
        deployment_result.removed_static_config_containers.extend(containers_to_delete.values())
        # TODO: Build a 'delete_configlet_containers' gRPC API
        await gather(*[cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id) for container_id in containers_to_delete])
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No container deletions are needed.")

    return existing_containers, existing_managed_containers_by_id, unmanaged_orphan_container_ids


async def _sync_configlets(
    cv_manifest: CVManifest,
    existing_containers: list[ConfigletAssignment],
    existing_managed_containers_by_id: dict[str, str],
    unmanaged_orphan_container_ids: set[str],
    deployment_result: DeployToCvResult,
    cv_client: CVClient,
) -> None:
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
        # A configlet can be assigned to multiple containers (holders).
        existing_holders_by_configlet_id: defaultdict[str, list[ConfigletAssignment]] = defaultdict(list)
        for container in existing_containers:
            for configlet_id in container.configlet_ids.values:
                existing_holders_by_configlet_id[configlet_id].append(container)

        # Validate that no managed configlet scheduled for deletion was assigned to containers this deploy will not touch.
        violations: list[tuple[str, str, str, str]] = []
        for configlet_id, configlet_name in configlets_to_delete.items():
            for holder in existing_holders_by_configlet_id.get(configlet_id, []):
                holder_id = cast("str", holder.key.configlet_assignment_id)
                if holder_id in existing_managed_containers_by_id or holder_id in unmanaged_orphan_container_ids:
                    # Holder is managed and will be handled by this deploy, or is unmanaged and scheduled for orphan deletion.
                    continue

                # Holder is out of our control.
                violations.append((cast("str", holder.display_name), holder_id, configlet_name, configlet_id))

        if violations:
            violations.sort()
            violations_text = "; ".join(
                f"'{configlet_name}' (id={configlet_id}) is still assigned to '{holder_name}' (id={holder_id})"
                for holder_name, holder_id, configlet_name, configlet_id in violations
            )
            msg = (
                "The following manifest-managed configlets are scheduled for deletion "
                "but are still assigned to containers that this manifest does not control. "
                f"Unassign the configlets manually (or keep them in the manifest) and re-run: {violations_text}"
            )
            raise CVManifestError(msg)

        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Removing %d manifest-managed configlets which are no longer used.", len(configlets_to_delete))
        deployment_result.removed_static_config_configlets.extend(configlets_to_delete.values())
        await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(configlets_to_delete.keys()))
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No AVD-managed configlet deletions are needed.")


async def _sync_studio_roots(cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Synchronize Studio root containers. Update root container assignments.

    Note:
        When new manifest root container IDs are introduced, all manifest containers are placed first,
        followed by any existing root containers.
        When only removing manifest root containers, the existing order is preserved and removed entries
        are filtered out, keeping existing root containers in their current positions.
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

    # Calculate which desired roots are missing.
    desired_root_ids = [container.id for container in cv_manifest.containers if container.is_root]
    desired_root_ids_set = set(desired_root_ids)
    existing_root_ids_set = set(existing_root_ids)
    missing_ids = desired_root_ids_set - existing_root_ids_set

    if missing_ids:
        non_manifest_root_ids = [container_id for container_id in existing_root_ids if not container_id.startswith(AVD_ENTITY_PREFIX)]
        new_ordered_ids = desired_root_ids + non_manifest_root_ids
    else:
        new_ordered_ids = [
            container_id for container_id in existing_root_ids if container_id in desired_root_ids_set or not container_id.startswith(AVD_ENTITY_PREFIX)
        ]

    if new_ordered_ids != existing_root_ids:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Updating Studio root container assignment list...")
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=new_ordered_ids,
        )
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Studio root container assignments are already in the desired state.")
