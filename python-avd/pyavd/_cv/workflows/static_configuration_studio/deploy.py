# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from asyncio import gather
from logging import getLogger
from typing import TYPE_CHECKING, cast

from .models import DeploymentPlan, ExistingState

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient
    from pyavd._cv.workflows.models import DeployToCvResult

LOGGER = getLogger(__name__)


STATIC_CONFIGURATION_STUDIO_ID = "studio-static-configlet"


async def fetch_existing_state(cv_client: CVClient, workspace_id: str) -> ExistingState:
    """Fetch the current root container list, containers and configlets from CloudVision."""
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Fetching existing state from CloudVision...")

    existing_root_ids, existing_containers, existing_configlets = await gather(
        cv_client.get_studio_inputs_with_path(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            default_value=[],
        ),
        cv_client.get_configlet_containers(workspace_id=workspace_id),
        cv_client.get_configlets(workspace_id=workspace_id),
    )

    return ExistingState(
        root_ids=existing_root_ids,
        containers_by_id={cast("str", container.key.configlet_assignment_id): container for container in existing_containers},
        configlets_by_id={cast("str", configlet.key.configlet_id): configlet for configlet in existing_configlets},
    )


async def execute_plan(plan: DeploymentPlan, workspace_id: str, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """Execute the deployment plan and populate the deployment result."""
    if plan.configlets_to_upsert:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d configlets (create/update)...", len(plan.configlets_to_upsert))
        deployment_result.deployed_static_config_configlets.extend(configlet.avd_configlet for configlet in plan.configlets_to_upsert)
        await cv_client.set_configlets_from_files(workspace_id=workspace_id, configlets=[configlet.api_tuple for configlet in plan.configlets_to_upsert])
    else:
        LOGGER.debug("deploy_static_config_studio_manifest_to_cv: No configlet creations or updates are needed.")

    if plan.containers_to_upsert:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Applying changes for %d containers (create/update)...", len(plan.containers_to_upsert))
        deployment_result.deployed_static_config_containers.extend(container.avd_container for container in plan.containers_to_upsert)
        await cv_client.set_configlet_containers(workspace_id=workspace_id, containers=[container.api_tuple for container in plan.containers_to_upsert])
    else:
        LOGGER.debug("deploy_static_config_studio_manifest_to_cv: No container creations or updates are needed.")

    deployment_result.skipped_static_config_containers.extend(container.avd_container for container in plan.containers_unchanged)

    if plan.final_root_ids is not None:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Updating Studio root container assignment list...")
        await cv_client.set_studio_inputs(
            studio_id=STATIC_CONFIGURATION_STUDIO_ID,
            workspace_id=workspace_id,
            input_path=["configletAssignmentRoots"],
            inputs=plan.final_root_ids,
        )
    else:
        LOGGER.debug("deploy_static_config_studio_manifest_to_cv: Studio root container assignment list is already in the desired state.")

    if plan.containers_to_delete:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Deleting %d containers...", len(plan.containers_to_delete))
        deployment_result.removed_static_config_containers.extend(plan.containers_to_delete.values())
        # TODO: Build a 'delete_configlet_containers' gRPC API
        await gather(*[cv_client.delete_configlet_container(workspace_id=workspace_id, assignment_id=cid) for cid in plan.containers_to_delete])
    else:
        LOGGER.debug("deploy_static_config_studio_manifest_to_cv: No container deletions are needed.")

    if plan.configlets_to_delete:
        LOGGER.info("deploy_static_config_studio_manifest_to_cv: Deleting %d configlets...", len(plan.configlets_to_delete))
        deployment_result.removed_static_config_configlets.extend(plan.configlets_to_delete.values())
        await cv_client.delete_configlets(workspace_id=workspace_id, configlet_ids=list(plan.configlets_to_delete))
    else:
        LOGGER.debug("deploy_static_config_studio_manifest_to_cv: No configlet deletions are needed.")
