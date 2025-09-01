# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING
from uuid import NAMESPACE_DNS, uuid5

from .models import CVConfiglet, CVContainer

if TYPE_CHECKING:
    from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment
    from pyavd._cv.client import CVClient

    from .models import DeployToCvResult
    from .schemas import StaticConfigurationContainer, StaticConfigurationHierarchy

LOGGER = getLogger(__name__)


MANAGED_ROOT_CONTAINER_ID = "avd-hierarchy"
MANAGED_ROOT_CONTAINER_NAME = "AVD Hierarchy"
STATIC_CONFIGURATION_STUDIO_ID = "studio-static-configlet"

MATCH_POLICY_MAP = {
    0: "unspecified",
    1: "match_first",
    2: "match_all",
}

AVD_NAMESPACE = uuid5(NAMESPACE_DNS, "avd.arista.com")


def generate_id(key: str) -> str:
    """Generate an ID from AVD_NAMESPACE and the provided key."""
    return str(uuid5(AVD_NAMESPACE, key))


async def sync_config_hierarchy_to_cv(desired_hierarchy: StaticConfigurationHierarchy, result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Synchronize a declarative container hierarchy to CloudVision using the "Static Configuration" Studio.

    TODO: Implement strict mode to remove any containers/configlets not managed by AVD from the Studio.
    TODO: Implement configlet body diff - digest/checksum.
    TODO: Split into functions.
    """
    workspace_id = result.workspace.id
    LOGGER.info("sync_config_hierarchy_to_cv: Starting config hierarchy sync for workspace '%s'.", workspace_id)

    # Build desired state from the input hierarchy.
    desired_containers, desired_configlets = build_desired_state_from_hierarchy(hierarchy=desired_hierarchy)
    LOGGER.info(
        "sync_config_hierarchy_to_cv: Calculated desired state: %d containers and %d unique configlets.", len(desired_containers), len(desired_configlets)
    )

    # Build existing state from CloudVision.
    LOGGER.info("sync_config_hierarchy_to_cv: Fetching all existing configlet containers from CloudVision...")
    all_cv_assignments = await cv_client.get_configlet_containers(workspace_id=result.workspace.id)
    existing_containers = build_existing_containers_from_cv(configlet_assignments=all_cv_assignments)
    LOGGER.info("sync_config_hierarchy_to_cv: Found %d existing AVD-managed containers.", len(existing_containers))

    # Ensure the root container is registered with the Studio.
    await ensure_root_container_is_in_studio(workspace_id=workspace_id, cv_client=cv_client)

    # Compare containers desired state with existing state to find differences.
    containers_to_push: list[CVContainer] = []
    for container in desired_containers:
        existing_container = existing_containers.get(container.id)
        # If container doesn't exist or is different from what's desired, add it to our push list.
        if existing_container != container:
            containers_to_push.append(container)
        else:
            result.skipped_static_config_containers.append(container)

    # Apply changes to CloudVision if any.
    if containers_to_push:
        LOGGER.info("sync_config_hierarchy_to_cv: Applying changes for %d containers (create/update)...", len(containers_to_push))
        result.deployed_static_config_containers.extend(containers_to_push)
        container_tuples = [
            (
                container.id,
                container.name,
                container.description,
                list(container.configlet_ids) or None,
                container.query,
                list(container.child_ids) or None,
                container.match_policy,
            )
            for container in containers_to_push
        ]
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=container_tuples)
    else:
        LOGGER.info("sync_config_hierarchy_to_cv: No container creations or updates are needed.")

    # Push configlets to CloudVision.
    if desired_configlets:
        LOGGER.info("sync_config_hierarchy_to_cv: Applying changes for %d configlets (create/update)...", len(desired_configlets))
        result.deployed_static_config_configlets.extend(desired_configlets)
        configlet_tuples = [(configlet.id, configlet.name, configlet.description, configlet.file) for configlet in desired_configlets]
        await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=configlet_tuples)
    else:
        LOGGER.info("sync_config_hierarchy_to_cv: No configlet creations or updates are needed.")

    # Delete unused AVD-managed configlets.
    # TODO: Add deleted configlet names to DeployToCvResult when we implement configlet body diff detection
    existing_configlet_ids = {configlet_id for container in existing_containers.values() for configlet_id in container.configlet_ids}
    desired_configlet_ids = {configlet.id for configlet in desired_configlets}
    if unused_configlets_ids := existing_configlet_ids.difference(desired_configlet_ids):
        LOGGER.info("sync_config_hierarchy_to_cv: Removing %d no longer used configlets.", len(unused_configlets_ids))
        await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(unused_configlets_ids))
    else:
        LOGGER.info("sync_config_hierarchy_to_cv: No configlet deletions are needed.")

    # Done.
    LOGGER.info("sync_config_hierarchy_to_cv: Configuration hierarchy sync complete for workspace '%s'.", workspace_id)


async def ensure_root_container_is_in_studio(workspace_id: str, cv_client: CVClient) -> None:
    """Check if the AVD root container is registered as an input to the Static Configuration Studio and add it if missing."""
    LOGGER.info("sync_config_hierarchy_to_cv: Ensuring root container is registered with the Static Config Studio.")

    # Get the current list of root containers from the Studio inputs.
    root_containers: list = await cv_client.get_studio_inputs_with_path(
        studio_id=STATIC_CONFIGURATION_STUDIO_ID,
        workspace_id=workspace_id,
        input_path=["configletAssignmentRoots"],
        default_value=[],
    )

    if MANAGED_ROOT_CONTAINER_ID not in root_containers:
        LOGGER.info(
            "sync_config_hierarchy_to_cv: AVD root container not assigned as root container in Static Config Studio. Inserting AVD container at the top."
        )
        # Inserting our container first, to allow reconcile and other static config containers to override the AVD hierarchy configs.
        root_containers.insert(0, MANAGED_ROOT_CONTAINER_ID)
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=root_containers,
        )
    else:
        LOGGER.info("sync_config_hierarchy_to_cv: AVD root container is already registered with the Studio.")


def build_desired_state_from_hierarchy(hierarchy: StaticConfigurationHierarchy) -> tuple[list[CVContainer], list[CVConfiglet]]:
    """Parse the user-defined hierarchy, instantiate all objects and return flat lists of the desired state."""
    all_containers: list[CVContainer] = []
    all_configlets: dict[str, CVConfiglet] = {}

    def traverse(container_def: StaticConfigurationContainer, parent_path: str) -> str:
        """Recursively traverse the container tree, creating objects and returning the container generated ID."""
        current_path = f"{parent_path}/{container_def.name}"

        # Process sub-containers.
        child_ids = [traverse(child_def, current_path) for child_def in container_def.sub_containers]

        # Process configlets attached to this container.
        configlet_ids = []
        for configlet_def in container_def.configlets:
            configlet_id = generate_id(configlet_def.name)
            if configlet_id not in all_configlets:
                all_configlets[configlet_id] = CVConfiglet(
                    id=configlet_id,
                    name=configlet_def.name,
                    file=configlet_def.file,
                    description="Configlet created and uploaded by AVD.",
                )
            # Prevents duplicate configlets on the container, though CloudVision also handles this.
            if configlet_id not in configlet_ids:
                configlet_ids.append(configlet_id)

        # Generate the container ID, create the object and add it to the final list.
        container_id = generate_id(current_path)
        all_containers.append(
            CVContainer(
                id=container_id,
                name=container_def.name,
                description=container_def.description or "",
                query=container_def.device_tag,
                hierarchy_path=current_path,
                match_policy=container_def.match_policy,
                configlet_ids=tuple(configlet_ids),
                child_ids=tuple(child_ids),
            )
        )
        return container_id

    # The entire user-defined hierarchy is parented under our single managed root.
    root_child_ids = [traverse(container_def, MANAGED_ROOT_CONTAINER_NAME) for container_def in hierarchy.containers]

    # Add the root container itself to the desired state.
    all_containers.append(
        CVContainer(
            id=MANAGED_ROOT_CONTAINER_ID,
            name=MANAGED_ROOT_CONTAINER_NAME,
            description="Root container for all configuration managed by AVD.",
            hierarchy_path=MANAGED_ROOT_CONTAINER_NAME,
            query="device:*",
            match_policy="match_all",
            child_ids=tuple(root_child_ids),
        )
    )

    # The order of containers matters, so we reverse to get parent-first with the root at the beginning.
    return list(reversed(all_containers)), list(all_configlets.values())


def build_existing_containers_from_cv(configlet_assignments: list[ConfigletAssignment]) -> dict[str, CVContainer]:
    """
    Parse a list of gRPC ConfigletAssignment objects from CloudVision into a flat dictionary.

    Traverses the AVD-managed hierarchy to reconstruct the hierarchy_path for each container,
    returning a dictionary mapping container IDs to the CVContainer objects.
    """
    assignments_by_id = {assignment.key.configlet_assignment_id: assignment for assignment in configlet_assignments}
    existing_containers: dict[str, CVContainer] = {}

    if MANAGED_ROOT_CONTAINER_ID not in assignments_by_id:
        # If the root doesn't exist, then no AVD-managed hierarchy exists.
        return {}

    def traverse(container_id: str, parent_path: str) -> None:
        """Recursively traverse the tree and build the container objects with the proper paths."""
        assignment = assignments_by_id.get(container_id)
        if not assignment or container_id in existing_containers:
            return

        current_path = parent_path if container_id == MANAGED_ROOT_CONTAINER_ID else f"{parent_path}/{assignment.display_name}"

        existing_containers[container_id] = CVContainer(
            id=container_id,
            name=assignment.display_name,
            description=assignment.description,
            query=assignment.query,
            hierarchy_path=current_path,
            match_policy=MATCH_POLICY_MAP.get(assignment.match_policy.value),
            configlet_ids=tuple(assignment.configlet_ids.values),
            child_ids=tuple(assignment.child_assignment_ids.values),
        )

        for child_id in assignment.child_assignment_ids.values:
            traverse(child_id, current_path)

    # Start traversal from the root.
    traverse(MANAGED_ROOT_CONTAINER_ID, MANAGED_ROOT_CONTAINER_NAME)

    return existing_containers
