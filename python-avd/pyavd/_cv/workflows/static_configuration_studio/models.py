# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field, replace
from typing import TYPE_CHECKING, cast

from pyavd._cv.workflows.models import CVManifest

from .ids import AvdId

if TYPE_CHECKING:
    from pyavd._cv.api.arista.configlet.v1 import Configlet, ConfigletAssignment
    from pyavd._cv.workflows.models import CVConfiglet, CVContainer

DesiredState = CVManifest


@dataclass(frozen=True)
class ExistingState:
    """Snapshot of the current state on CloudVision, fetched once at the start of a deployment."""

    root_ids: list[str]
    containers_by_id: dict[str, ConfigletAssignment]
    configlets_by_id: dict[str, Configlet]


@dataclass(frozen=True)
class ResolvedState:
    """
    The final container hierarchy after applying the desired state on top of the existing state.

    Container reachability and assigned configlets are pre-computed for the deployment plan to consume.
    """

    root_ids: list[str]
    child_ids_by_container_id: dict[str, list[str]]
    reachable_container_ids: set[str]
    assigned_configlet_ids: set[str]

    @classmethod
    def build(cls, desired: DesiredState, existing: ExistingState) -> ResolvedState:
        """Build the resolved state."""
        root_ids = cls._compute_root_ids(desired, existing)
        child_ids_by_container_id = cls._compute_child_map(desired, existing)
        reachable_container_ids = cls._compute_reachable_container_ids(root_ids, child_ids_by_container_id)
        assigned_configlet_ids = cls._compute_assigned_configlet_ids(reachable_container_ids, desired, existing)
        return cls(
            root_ids=root_ids,
            child_ids_by_container_id=child_ids_by_container_id,
            reachable_container_ids=reachable_container_ids,
            assigned_configlet_ids=assigned_configlet_ids,
        )

    @staticmethod
    def _compute_root_ids(desired: DesiredState, existing: ExistingState) -> list[str]:
        """
        Compute the final root container list.

        Note:
            When new manifest root container IDs are introduced, all manifest containers are placed first,
            followed by any existing root containers.
            When only removing manifest root containers, the existing order is preserved and removed entries
            are filtered out, keeping existing root containers in their current positions.
        """
        # TODO: Add root_policy handling here in the future.
        declared_root_ids_set = set(desired.root_ids)
        existing_root_ids_set = set(existing.root_ids)
        missing_ids = declared_root_ids_set - existing_root_ids_set

        if missing_ids:
            non_manifest_root_ids = [root_id for root_id in existing.root_ids if not AvdId.is_managed(root_id)]
            return list(desired.root_ids) + non_manifest_root_ids

        return [root_id for root_id in existing.root_ids if root_id in declared_root_ids_set or not AvdId.is_managed(root_id)]

    @staticmethod
    def _compute_child_map(desired: DesiredState, existing: ExistingState) -> dict[str, list[str]]:
        """
        Compute the parent-to-children mapping for the final hierarchy, using the existing CloudVision relationships as the baseline.

        Manifest containers replace their existing children.
        """
        # TODO: Add sub_container_policy handling here in the future.
        child_map = {container_id: list(container.child_assignment_ids.values) for container_id, container in existing.containers_by_id.items()}
        for container_id, desired_container in desired.containers_by_id.items():
            child_map[container_id] = list(desired_container.child_ids)
        return child_map

    @staticmethod
    def _compute_reachable_container_ids(root_ids: list[str], child_ids_by_container_id: dict[str, list[str]]) -> set[str]:
        """
        Compute the set of container IDs still attached to a Studio root in the final hierarchy.

        Containers not in this set are orphans and become deletion candidates if AVD-managed.
        """
        reachable_container_ids: set[str] = set()
        traversal_queue: deque[str] = deque(root_ids)

        while traversal_queue:
            container_id = traversal_queue.popleft()
            if container_id in reachable_container_ids:
                continue
            reachable_container_ids.add(container_id)
            traversal_queue.extend(child_ids_by_container_id.get(container_id, []))

        return reachable_container_ids

    @staticmethod
    def _compute_assigned_configlet_ids(reachable_container_ids: set[str], desired: DesiredState, existing: ExistingState) -> set[str]:
        """Compute the set of configlet IDs assigned to any reachable container in the final hierarchy."""
        assigned: set[str] = set()

        for container_id in reachable_container_ids:
            if container_id in desired.containers_by_id:
                # Container is in the new manifest. Use its proposed configlets.
                assigned.update(desired.containers_by_id[container_id].configlet_ids)
            elif container_id in existing.containers_by_id:
                # Container exists but isn't in the current manifest. Keep its existing configlets.
                assigned.update(existing.containers_by_id[container_id].configlet_ids.values)

        return assigned


@dataclass
class DeploymentPlan:
    """All decisions for a single deployment, computed from the desired state, the existing state, and the resolved state."""

    configlets_to_upsert: list[CVConfiglet] = field(default_factory=list)
    containers_to_upsert: list[CVContainer] = field(default_factory=list)
    containers_unchanged: list[CVContainer] = field(default_factory=list)
    final_root_ids: list[str] | None = None
    """None means the root list is unchanged and no API call is needed."""
    containers_to_delete: dict[str, str] = field(default_factory=dict)
    """Mapping of container_id to display_name."""
    configlets_to_delete: dict[str, str] = field(default_factory=dict)
    """Mapping of configlet_id to display_name."""
    containers_preserved: dict[str, str] = field(default_factory=dict)
    """Mapping of container_id to display_name for AVD-managed containers preserved because they are reachable through non-manifest containers."""
    configlets_preserved: dict[str, str] = field(default_factory=dict)
    """Mapping of configlet_id to display_name for AVD-managed configlets preserved because they are still assigned to non-manifest containers."""

    @classmethod
    def build(cls, desired: DesiredState, existing: ExistingState, resolved: ResolvedState) -> DeploymentPlan:
        """Build the deployment plan from the desired state, the existing CloudVision state, and the resolved state."""
        plan = cls()

        # Always push configlets for now.
        plan.configlets_to_upsert = list(desired.configlets_by_id.values())

        for container_id, desired_container in desired.containers_by_id.items():
            # Rebuild the container with resolved children from the final hierarchy.
            resolved_children = resolved.child_ids_by_container_id[container_id]
            proposed_container = replace(desired_container, child_ids=tuple(resolved_children))

            existing_container = existing.containers_by_id.get(container_id)
            if not existing_container or not proposed_container.matches_configlet_assignment(existing_container):
                # Container is new or has changed, so it needs to be pushed.
                plan.containers_to_upsert.append(proposed_container)
            else:
                # Container is unchanged.
                plan.containers_unchanged.append(proposed_container)

        if resolved.root_ids != existing.root_ids:
            plan.final_root_ids = resolved.root_ids

        # Classify each AVD-managed existing container as deletable (unreachable) or preserved (still reachable through non-manifest containers).
        for container_id, container in existing.containers_by_id.items():
            if not AvdId.is_managed(container_id):
                continue
            display_name = cast("str", container.display_name)
            if container_id not in resolved.reachable_container_ids:
                plan.containers_to_delete[container_id] = display_name
            elif container_id not in desired.containers_by_id:
                plan.containers_preserved[container_id] = display_name

        # In "managed" mode, classify each AVD-managed existing configlet not in this manifest as deletable (unassigned) or preserved (still assigned).
        # In "additive" mode, don't delete any configlets.
        if desired.configlet_policy == "managed":
            for configlet_id, configlet in existing.configlets_by_id.items():
                if not AvdId.is_managed(configlet_id) or configlet_id in desired.configlets_by_id:
                    continue
                display_name = cast("str", configlet.display_name)
                if configlet_id in resolved.assigned_configlet_ids:
                    plan.configlets_preserved[configlet_id] = display_name
                else:
                    plan.configlets_to_delete[configlet_id] = display_name

        return plan
