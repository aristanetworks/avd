# Copyright (c) 2025-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from .static_configuration_studio.deploy import execute_plan, fetch_existing_state
from .static_configuration_studio.models import DeploymentPlan, DesiredState, ResolvedState

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import AvdManifest, DeployToCvResult

LOGGER = getLogger(__name__)


# TODO: Move this to the workflows/static_configuration_studio package.
async def deploy_static_config_studio_manifest_to_cv(manifest: AvdManifest, deployment_result: DeployToCvResult, cv_client: CVClient) -> None:
    """
    Deploy a manifest (configlets/containers) to CloudVision using the "Static Configuration" Studio.

    TODO: Implement strict mode to remove any containers/configlets not managed by AVD from the Studio.
    TODO: Implement configlet body diff - digest/checksum.
    """
    workspace_id = deployment_result.workspace.id
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Starting manifest deployment for workspace '%s'.", workspace_id)

    # Build the desired state from the AVD manifest.
    desired = DesiredState.from_avd_manifest(manifest)

    LOGGER.info(
        "deploy_static_config_studio_manifest_to_cv: Calculated desired state: %d containers and %d unique configlets.",
        len(desired.containers_by_id),
        len(desired.configlets_by_id),
    )
    if not desired.configlets_by_id and not desired.containers_by_id:
        return

    existing = await fetch_existing_state(cv_client, workspace_id)
    resolved = ResolvedState.build(desired, existing)
    plan = DeploymentPlan.build(desired, existing, resolved)
    await execute_plan(plan, workspace_id, deployment_result, cv_client)

    # Done.
    LOGGER.info("deploy_static_config_studio_manifest_to_cv: Completed manifest deployment for workspace '%s'.", workspace_id)
