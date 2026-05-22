# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from collections import defaultdict, deque
from dataclasses import dataclass
from logging import getLogger
from typing import TYPE_CHECKING, Any, cast

from pyavd._cv.client.configlet import ASSIGNMENT_MATCH_POLICY_MAP
from pyavd._cv.client.exceptions import CVManifestError

from .models import AVD_ENTITY_PREFIX, CVManifest

if TYPE_CHECKING:
    from pyavd._cv.api.arista.configlet.v1 import ConfigletAssignment
    from pyavd._cv.client import CVClient

    from .models import AvdManifest, CVContainer, DeployToCvResult

LOGGER = getLogger(__name__)


STATIC_CONFIGURATION_STUDIO_ID = "studio-static-configlet"
STUDIO_ROOT_PARENT_ID = "<Static Configuration Studio roots>"
"""Synthetic parent ID representing the Static Configuration Studio root list."""


@dataclass
class _ExistingContainerState:
    """
    Existing Static Configuration Studio container graph.

    Studio roots are modeled as parent edges from STUDIO_ROOT_PARENT_ID, so parent validation can use the
    same logic for root assignments and regular container child assignments.
    """

    containers: list[ConfigletAssignment]
    root_ids: list[str]
    containers_by_id: dict[str, ConfigletAssignment]
    children_by_parent_id: dict[str, list[str]]
    parent_ids_by_child_id: dict[str, list[str]]
    manifest_managed_container_ids: set[str]

    def container_name(self, container_id: str) -> str:
        container = self.containers_by_id.get(container_id)
        if container is None:
            return container_id
        return cast("str", container.display_name)

    def parent_display(self, parent_id: str) -> str:
        if parent_id == STUDIO_ROOT_PARENT_ID:
            return "Static Configuration Studio root list"
        return f"'{self.container_name(parent_id)}' (id={parent_id})"


@dataclass
class _PlannedContainer:
    """
    Desired container with the effective child list to push/compare.

    For containers with preserve_existing_sub_containers enabled, child_ids preserves the existing CV child
    order and appends newly declared manifest sub-containers.
    """

    container: CVContainer
    child_ids: tuple[str, ...]

    @property
    def api_tuple(self) -> tuple[Any, ...]:
        return (
            self.container.id,
            self.container.name,
            self.container.description or "",
            list(self.container.configlet_ids),
            self.container.tag_query,
            list(self.child_ids),
            self.container.match_policy,
        )

    def matches_configlet_assignment(self, configlet_assignment: ConfigletAssignment) -> bool:
        return self.api_tuple == _configlet_assignment_api_tuple(configlet_assignment)


@dataclass
class _ContainerPlan:
    """
    Planned container and root mutations.

    containers_to_delete can include manual containers, but only when they are below a manifest-managed branch
    that this deploy updates/deletes and would otherwise leave them orphaned in CV.
    """

    containers_to_push: list[_PlannedContainer]
    containers_to_skip: list[_PlannedContainer]
    containers_to_delete: dict[str, str]
    preserved_container_ids: set[str]
    new_root_ids: list[str]
    root_ids_changed: bool

    @property
    def container_ids_to_delete(self) -> set[str]:
        return set(self.containers_to_delete)

    @property
    def touched_container_ids(self) -> set[str]:
        return {planned_container.container.id for planned_container in self.containers_to_push} | self.container_ids_to_delete


def _configlet_assignment_api_tuple(configlet_assignment: ConfigletAssignment) -> tuple[Any, ...]:
    """Return the comparable API tuple for an existing configlet assignment."""
    reversed_match_policy_map = {enum_member.value: str_key for str_key, enum_member in ASSIGNMENT_MATCH_POLICY_MAP.items()}
    return (
        configlet_assignment.key.configlet_assignment_id,
        configlet_assignment.display_name,
        configlet_assignment.description,
        configlet_assignment.configlet_ids.values,
        configlet_assignment.query,
        configlet_assignment.child_assignment_ids.values,
        reversed_match_policy_map.get(configlet_assignment.match_policy.value),
    )


async def deploy_static_config_studio_manifest_to_cv(manifest: AvdManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy a manifest (configlets/containers) to CloudVision using the "Static Configuration" Studio.

    TODO: Implement strict mode to remove any containers/configlets not managed by the manifest from the Studio.
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
    existing_containers, touched_container_ids = await _sync_containers(cv_manifest=cv_manifest, deployment_result=deployment_result, cv_client=cv_client)
    await _sync_configlets(
        cv_manifest=cv_manifest,
        existing_containers=existing_containers,
        touched_container_ids=touched_container_ids,
        deployment_result=deployment_result,
        cv_client=cv_client,
    )

    # Done.
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Completed manifest deployment for workspace '%s'.", workspace_id)


async def _sync_containers(cv_manifest: CVManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> tuple[list[ConfigletAssignment], set[str]]:
    """
    Synchronize containers and Static Configuration Studio roots.

    The function builds one graph covering regular parent-child assignments and Studio root assignments,
    validates the existing graph, then applies the calculated container/root plan.
    """
    workspace_id = deployment_result.workspace.id

    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching existing Static Configuration Studio container state from CloudVision...")
    existing_containers, existing_root_ids = await gather(
        cv_client.get_configlet_containers(workspace_id=workspace_id),
        cv_client.get_studio_inputs_with_path(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            default_value=[],
        ),
    )

    existing_state = _build_existing_container_state(existing_containers, existing_root_ids)
    container_plan = _build_container_plan(cv_manifest, existing_state)
    _validate_existing_container_state(existing_state, container_plan)
    await _apply_container_plan(container_plan, deployment_result, cv_client)

    return existing_state.containers, container_plan.touched_container_ids


def _build_existing_container_state(existing_containers: list[ConfigletAssignment], existing_root_ids: list[str]) -> _ExistingContainerState:
    """Index existing containers and model Studio root assignments as synthetic parent edges."""
    containers_by_id: dict[str, ConfigletAssignment] = {}
    children_by_parent_id: dict[str, list[str]] = {}
    parent_ids_by_child_id: defaultdict[str, list[str]] = defaultdict(list)
    manifest_managed_container_ids: set[str] = set()

    for container in existing_containers:
        container_id = cast("str", container.key.configlet_assignment_id)
        containers_by_id[container_id] = container
        children_by_parent_id[container_id] = list(container.child_assignment_ids.values)
        if container_id.startswith(AVD_ENTITY_PREFIX):
            manifest_managed_container_ids.add(container_id)
        for child_id in container.child_assignment_ids.values:
            parent_ids_by_child_id[child_id].append(container_id)

    for root_id in existing_root_ids:
        parent_ids_by_child_id[root_id].append(STUDIO_ROOT_PARENT_ID)

    return _ExistingContainerState(
        containers=existing_containers,
        root_ids=existing_root_ids,
        containers_by_id=containers_by_id,
        children_by_parent_id=children_by_parent_id,
        parent_ids_by_child_id=dict(parent_ids_by_child_id),
        manifest_managed_container_ids=manifest_managed_container_ids,
    )


def _build_container_plan(cv_manifest: CVManifest, existing_state: _ExistingContainerState) -> _ContainerPlan:
    """
    Build the desired container/root diff from the existing state.

    Manifest-managed containers are identified by their generated ID prefix. The rest of the workflow uses
    "manifest-managed" terminology since users may run this workflow outside the broader AVD fabric model.
    """
    containers_to_push: list[_PlannedContainer] = []
    containers_to_skip: list[_PlannedContainer] = []
    containers_to_delete: dict[str, str] = {}
    preserved_container_ids: set[str] = set()
    manual_delete_roots: list[str] = []
    desired_container_ids = {container.id for container in cv_manifest.containers}

    def add_preserved_container_subtree(container_id: str) -> None:
        """Mark an existing child and its descendants as intentionally outside this manifest's ownership boundary."""
        queue = deque([container_id])
        while queue:
            queued_container_id = queue.popleft()
            if queued_container_id in desired_container_ids or queued_container_id in preserved_container_ids:
                continue
            preserved_container_ids.add(queued_container_id)
            queue.extend(existing_state.children_by_parent_id.get(queued_container_id, []))

    def add_container_subtree_to_delete(container_id: str) -> None:
        """Add an existing non-desired container and its non-desired descendants to the deletion plan."""
        queue = deque([container_id])
        while queue:
            queued_container_id = queue.popleft()
            if queued_container_id in desired_container_ids or queued_container_id in preserved_container_ids or queued_container_id in containers_to_delete:
                continue
            container = existing_state.containers_by_id.get(queued_container_id)
            if container is None:
                continue

            containers_to_delete[queued_container_id] = cast("str", container.display_name)
            queue.extend(existing_state.children_by_parent_id.get(queued_container_id, []))

    # Create planned desired containers. Containers with preserve_existing_sub_containers keep any
    # existing children not declared in this manifest, enabling partial sibling-branch deployments.
    for desired_container in cv_manifest.containers:
        existing_container = existing_state.containers_by_id.get(desired_container.id)
        desired_child_ids = desired_container.child_ids
        if existing_container and desired_container.avd_container.preserve_existing_sub_containers:
            existing_child_ids = tuple(existing_container.child_assignment_ids.values)
            existing_child_ids_set = set(existing_child_ids)
            desired_child_ids_set = set(desired_child_ids)
            preserved_child_ids = tuple(child_id for child_id in existing_child_ids if child_id not in desired_child_ids_set)
            for child_id in preserved_child_ids:
                add_preserved_container_subtree(child_id)
            new_desired_child_ids = tuple(child_id for child_id in desired_child_ids if child_id not in existing_child_ids_set)
            effective_child_ids = (*existing_child_ids, *new_desired_child_ids)
        else:
            effective_child_ids = desired_child_ids

        planned_container = _PlannedContainer(container=desired_container, child_ids=effective_child_ids)

        if not existing_container:
            # Container is new.
            containers_to_push.append(planned_container)
            continue

        if not planned_container.matches_configlet_assignment(existing_container):
            # Container has changed.
            containers_to_push.append(planned_container)
        else:
            # Container is unchanged.
            containers_to_skip.append(planned_container)

        # Existing manual children unassigned by the manifest become orphans caused by this deploy.
        existing_children = set(existing_container.child_assignment_ids.values)
        desired_children = set(effective_child_ids)
        manual_delete_roots.extend(child_id for child_id in existing_children - desired_children if not child_id.startswith(AVD_ENTITY_PREFIX))

    for container_id in manual_delete_roots:
        add_container_subtree_to_delete(container_id)

    # Manifest-managed containers no longer in the manifest are deleted together with their non-desired descendants.
    for container_id in existing_state.manifest_managed_container_ids - desired_container_ids - preserved_container_ids:
        add_container_subtree_to_delete(container_id)

    desired_root_ids = [container.id for container in cv_manifest.containers if container.is_root]
    desired_root_ids_set = set(desired_root_ids)
    existing_root_ids_set = set(existing_state.root_ids)
    missing_root_ids = desired_root_ids_set - existing_root_ids_set

    if missing_root_ids:
        # This preserves the documented behavior: when new manifest roots are introduced, managed roots
        # are placed first and existing manual roots are kept after them.
        manual_root_ids = [container_id for container_id in existing_state.root_ids if not container_id.startswith(AVD_ENTITY_PREFIX)]
        new_root_ids = desired_root_ids + manual_root_ids
    else:
        # If no managed roots are added, preserve the existing root order and only filter removed managed roots.
        new_root_ids = [
            container_id for container_id in existing_state.root_ids if container_id in desired_root_ids_set or not container_id.startswith(AVD_ENTITY_PREFIX)
        ]

    return _ContainerPlan(
        containers_to_push=containers_to_push,
        containers_to_skip=containers_to_skip,
        containers_to_delete=containers_to_delete,
        preserved_container_ids=preserved_container_ids,
        new_root_ids=new_root_ids,
        root_ids_changed=new_root_ids != existing_state.root_ids,
    )


def _validate_existing_container_state(existing_state: _ExistingContainerState, container_plan: _ContainerPlan) -> None:
    """
    Validate manifest-managed container ownership before applying the plan.

    CloudVision can tolerate orphaned containers, so this validation intentionally does not reject unrelated
    manual orphans or other manual-only graph inconsistencies. It only blocks manifest-managed containers
    currently parented by manual containers this deploy will not update/delete.
    """
    violations: list[str] = []
    container_ids_to_delete = container_plan.container_ids_to_delete

    for container_id in existing_state.manifest_managed_container_ids - container_plan.preserved_container_ids:
        container = existing_state.containers_by_id[container_id]
        parent_ids = existing_state.parent_ids_by_child_id.get(container_id, [])
        parent_ids_set = set(parent_ids)
        manual_parent_ids = [
            parent_id
            for parent_id in parent_ids_set
            if parent_id != STUDIO_ROOT_PARENT_ID and not parent_id.startswith(AVD_ENTITY_PREFIX) and parent_id not in container_ids_to_delete
        ]
        violations.extend(
            f"Manifest-managed container '{container.display_name}' (id={container_id}) is currently a child of {existing_state.parent_display(parent_id)}"
            for parent_id in manual_parent_ids
        )

    if violations:
        violations.sort()
        violations_text = "; ".join(violations)
        msg = f"The existing Static Configuration Studio container state is inconsistent. Resolve these issues and re-run: {violations_text}"
        raise CVManifestError(msg)


async def _apply_container_plan(container_plan: _ContainerPlan, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """Apply an already validated container/root plan to CloudVision."""
    workspace_id = deployment_result.workspace.id

    deployment_result.skipped_static_config_containers.extend(
        planned_container.container.avd_container for planned_container in container_plan.containers_to_skip
    )

    if container_plan.containers_to_push:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d containers (create/update)...", len(container_plan.containers_to_push))
        deployment_result.deployed_static_config_containers.extend(
            planned_container.container.avd_container for planned_container in container_plan.containers_to_push
        )
        container_tuples = [planned_container.api_tuple for planned_container in container_plan.containers_to_push]
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=container_tuples)
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No container creations or updates are needed.")

    if container_plan.containers_to_delete:
        manifest_managed_delete_count = sum(1 for container_id in container_plan.containers_to_delete if container_id.startswith(AVD_ENTITY_PREFIX))
        manual_delete_count = len(container_plan.containers_to_delete) - manifest_managed_delete_count
        LOGGER.info(
            "deploy_static_config_studio_manifest_to_cv: Removing %d manifest-managed and %d manual containers which are no longer used.",
            manifest_managed_delete_count,
            manual_delete_count,
        )
        deployment_result.removed_static_config_containers.extend(container_plan.containers_to_delete.values())
        # TODO: Build a 'delete_configlet_containers' gRPC API
        await gather(
            *[
                cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=container_id)
                for container_id in container_plan.containers_to_delete
            ]
        )
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No container deletions are needed.")

    if container_plan.root_ids_changed:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Updating Studio root container assignment list...")
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=container_plan.new_root_ids,
        )
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Studio root container assignments are already in the desired state.")


def _raise_configlet_holder_violations(violations: list[tuple[str, str, str, str]]) -> None:
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


async def _sync_configlets(
    cv_manifest: CVManifest,
    existing_containers: list[ConfigletAssignment],
    touched_container_ids: set[str],
    deployment_result: DeployToCvResult,
    cv_client: CVClient,
) -> None:
    """
    Synchronize configlets. Create/update new ones and delete unused manifest-managed ones.

    touched_container_ids comes from the container plan and identifies holders whose stale configlet
    assignments will disappear because the holder is being rewritten or deleted by this deploy.
    """
    workspace_id = deployment_result.workspace.id

    # Create or update configlets.
    if cv_manifest.configlets:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d configlets (create/update)...", len(cv_manifest.configlets))
        deployment_result.deployed_static_config_configlets.extend(configlet.avd_configlet for configlet in cv_manifest.configlets)
        configlet_tuples = [configlet.api_tuple for configlet in cv_manifest.configlets]
        await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=configlet_tuples)
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No configlet creations or updates are needed.")

    # Delete unused manifest-managed configlets.
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
                if holder_id in touched_container_ids:
                    # Holder is rewritten or deleted by this deploy.
                    continue

                # Holder is out of our control.
                violations.append((cast("str", holder.display_name), holder_id, configlet_name, configlet_id))

        if violations:
            _raise_configlet_holder_violations(violations)

        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Removing %d manifest-managed configlets which are no longer used.", len(configlets_to_delete))
        deployment_result.removed_static_config_configlets.extend(configlets_to_delete.values())
        await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(configlets_to_delete.keys()))
    else:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: No manifest-managed configlet deletions are needed.")
