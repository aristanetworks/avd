# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException, CVWorkspaceSynchronizationAttemptsExhausted

from .create_workspace_on_cv import create_workspace_on_cv
from .decommission_devices_on_cv import stage_devices_for_decommission_on_cv, wait_for_device_decommission_staging_on_cv
from .deploy_configs_to_cv import delete_configs_from_cv, delete_decommissioned_device_configlets_from_cv, deploy_configs_to_cv
from .deploy_cv_pathfinder_metadata_to_cv import deploy_cv_pathfinder_metadata_to_cv
from .deploy_static_config_studio_manifest_to_cv import deploy_static_config_studio_manifest_to_cv
from .deploy_studio_inputs_to_cv import deploy_studio_inputs_to_cv
from .deploy_tags_to_cv import deploy_tags_to_cv
from .finalize_change_control_on_cv import finalize_change_control_on_cv
from .finalize_workspace_on_cv import finalize_workspace_on_cv, rebase_workspace_on_cv
from .models import (
    CloudVision,
    CVChangeControl,
    CVDeviceDeployment,
    CVStudioInputs,
    CVTimeOuts,
    CVWorkspace,
    DeployToCvResult,
)
from .utils import extract_from_device_deployments
from .verify_devices_on_cv import verify_devices_in_cloudvision_inventory, verify_devices_on_cv
from .verify_inputs import verify_device_inputs

if TYPE_CHECKING:
    from .models import AvdManifest, CVDevice, CVDeviceTag, CVEosConfig, CVInterfaceTag, CVPathfinderMetadata

LOGGER = getLogger(__name__)


async def _execute_deployment_steps(
    result: DeployToCvResult,
    configs: list[CVEosConfig],
    device_tags: list[CVDeviceTag],
    interface_tags: list[CVInterfaceTag],
    cv_pathfinder_metadata: list[CVPathfinderMetadata],
    static_config_manifest: AvdManifest | None,
    studio_inputs: list[CVStudioInputs],
    device_deployments: list[CVDeviceDeployment],
    strict_tags: bool,
    cv_client: CVClient,
    decommission_devices: list[CVDevice],
    existing_decommission_devices: list[CVDevice],
) -> None:
    """Execute all deployment sub-workflows which rely on the state of the CloudVision mainline."""
    try:
        # Stage decommission before reconciling configs and containers. CloudVision removes device-specific containers and their parent references.
        if existing_decommission_devices:
            staged_decommission_devices = await stage_devices_for_decommission_on_cv(
                devices=existing_decommission_devices,
                workspace_id=result.workspace.id,
                result=result,
                cv_client=cv_client,
            )
            if staged_decommission_devices:
                await wait_for_device_decommission_staging_on_cv(
                    devices=staged_decommission_devices,
                    workspace_id=result.workspace.id,
                    result=result,
                    cv_client=cv_client,
                )

            successfully_staged_decommission_serials = {device.serial_number for device in result.removed_devices}
            await delete_decommissioned_device_configlets_from_cv(
                devices=[device for device in decommission_devices if device.serial_number in successfully_staged_decommission_serials],
                result=result,
                cv_client=cv_client,
            )

        # Deploy device tags
        await deploy_tags_to_cv(
            tags=device_tags,
            workspace=result.workspace,
            strict=strict_tags,
            skipped_tags=result.skipped_device_tags,
            deployed_tags=result.deployed_device_tags,
            removed_tags=result.removed_device_tags,
            cv_client=cv_client,
        )

        # Deploy interface tags
        await deploy_tags_to_cv(
            tags=interface_tags,
            workspace=result.workspace,
            strict=strict_tags,
            skipped_tags=result.skipped_interface_tags,
            deployed_tags=result.deployed_interface_tags,
            removed_tags=result.removed_interface_tags,
            cv_client=cv_client,
        )

        # Deploy configs
        # TODO: Check if we want to consolidate and use the new deploy_static_config_studio_manifest_to_cv
        #       by building a hierarchy from the CVEosConfig objects.
        await deploy_configs_to_cv(
            configs=[config for config in configs if config.device.action != "decommission"],
            result=result,
            cv_client=cv_client,
        )

        # Deploy Static Configuration Studio manifest
        # TODO: Update function docstring workflow to reflect this
        if static_config_manifest:
            await deploy_static_config_studio_manifest_to_cv(
                manifest=static_config_manifest,
                deployment_result=result,
                cv_client=cv_client,
            )

        # Deploy Studio Inputs
        await deploy_studio_inputs_to_cv(
            studio_inputs=studio_inputs,
            result=result,
            cv_client=cv_client,
        )

        # Deploy CV Pathfinder metadata
        await deploy_cv_pathfinder_metadata_to_cv(
            cv_pathfinder_metadata=cv_pathfinder_metadata,
            result=result,
            cv_client=cv_client,
        )

        # Delete any leftover device configs for devices managed by the static config manifest
        await delete_configs_from_cv(
            device_deployments=device_deployments,
            result=result,
            cv_client=cv_client,
        )

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True


async def _rebase_workspace_on_cv_or_raise(
    result: DeployToCvResult,
    cv_client: CVClient,
    workspace_sync_attempt: int,
) -> None:
    """Rebase the Workspace unless synchronization attempts are exhausted."""
    LOGGER.info("deploy_to_cv: Workspace %s (%s) requires synchronization/rebase.", result.workspace.name, result.workspace.id)
    if workspace_sync_attempt >= result.workspace.max_sync_retries:
        await cv_client.abandon_workspace(workspace_id=result.workspace.id)
        result.workspace.state = "abandoned"
        raise CVWorkspaceSynchronizationAttemptsExhausted(result.workspace.max_sync_retries, result.workspace.name, result.workspace.id)
    LOGGER.info(
        "deploy_to_cv: Performing synchronization/rebase attempt %d/%d for Workspace %s (%s).",
        workspace_sync_attempt + 1,
        result.workspace.max_sync_retries,
        result.workspace.name,
        result.workspace.id,
    )
    await rebase_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)


async def _finalize_change_control(result: DeployToCvResult, cv_client: CVClient) -> None:
    # Create/update CVChangeControl object with ID created by workspace.
    if result.workspace.change_control_id is not None:
        if result.change_control is None:
            result.change_control = CVChangeControl()
        result.change_control.id = result.workspace.change_control_id

    # This is a separate "if" to allow to test stuff on a change control not created by the workspace.
    # You can run this by setting "id" directly in the given change control object.
    # TODO: Remove once we are done with testing (?)
    # Run, Delete or run and wait for Change Control if the workspace created one.
    if result.change_control is not None and result.change_control.id is not None:
        await finalize_change_control_on_cv(change_control=result.change_control, cv_client=cv_client)


async def deploy_to_cv(
    cloudvision: CloudVision,
    workspace: CVWorkspace | None = None,
    change_control: CVChangeControl | None = None,
    device_deployments: list[CVDeviceDeployment] | None = None,
    static_config_manifest: AvdManifest | None = None,
    studio_inputs: list[CVStudioInputs] | None = None,
    skip_missing_devices: bool = False,
    strict_system_mac_address: bool = False,
    strict_tags: bool = True,
    timeouts: CVTimeOuts | None = None,  # pylint: disable=unused-argument # noqa: ARG001
) -> DeployToCvResult:
    """
    Deploy various objects to CloudVision.

    For any device referred under `device_deployments`:
    - The device must be present in the CloudVision Inventory and onboarded to the "Inventory & Topology Studio".
        - TODO: See if we can onboard ZTP devices and/or preprovision.
    - The hostname will we updated in the I&T Studio.
    - The `serial_number` and `system_mac_address` properties will be inplace updated in the given CVDevice objects.

    TODO: Respect timeouts and add more.

    Parameters:
        cloudvision: CloudVision instance to deploy to.
        workspace: CloudVision Workspace to create or use for the deployment. \
            If the Workspace already exists, it must be in 'pending' state. \
            The `state` property will be inplace updated in the given CVWorkSpace object.
        change_control: CloudVision Change Control to create for the deployment. \
            It is not supported to reuse an existing Change Control, so the `id` field should not be set in the given CVChangeControl object. \
            The `id` and `state` properties will be inplace updated in the given CVChangeControl object.
        device_deployments: Per-device deployment objects containing configs, tags, and metadata to be deployed.
        static_config_manifest: Static Configuration Studio manifest to deploy.
        studio_inputs: Studio Inputs to be deployed. \
            It is not supported to update overlapping input paths for the same studio in the same deployment.
        cv_pathfinder_metadata: Special metadata for CV Pathfinder solution. Metadata will be combined and deployed to the hidden metadata studio.
        skip_missing_devices: If `True` anything that can be deployed will get deployed. \
            Otherwise the Workspace will be abandoned on any issue.
        strict_system_mac_address: If `True` - raise error if devices with duplicated `system_mac_address` but unique `serial_number` are present.
        strict_tags: If `True` other tags associated with the devices will get removed. \
            Otherwise other tags will be left as-is. \
            Other Tags with the same label are always removed.
    TODO: Consider implementing "strict configs".
          Very hard to implement since configs can now come from various studios and tag queries we have little control over.
            strict_configs: If `True` other configs associated with the devices will get removed. \
                Otherwise other configs will be left as-is.
          We could decide to just remove config assignments under our main container to devices not mentioned in the run.

    If CloudVision requires the Workspace to be synchronized/rebased (due to concurrent mainline changes), all mutable states computed against the previous
    CloudVision mainline are reset and all deployment steps are repeated from the scratch.
    The number of retry attempts is controlled by the `workspace.max_sync_retries`.
    `CVWorkspaceSynchronizationAttemptsExhausted` exception is raised if limit is reached but Workspace still requires synchronization.

    Returns:
        Object containing the results of the deployment including all associated objects.

    TODO: Workflow:
        + Create result object.
            + Add workspace object to result if given otherwise create a new workspace object we can return.
            - Add objects to result.deployed_x/skipped_x as we go through each of the following steps.
        + Initialize CVClient
        + Gather all devices from the given lists.
        + Verify that device inputs have no overlapping serial numbers or System MAC addresses.
        + On CV Identify all devices based on hostname, serial number or System MAC address.
            + In-place update device objects.
        + On CV verify that decommission devices (device.action="decommission") exist in the CV inventory.
            + In-place update device objects. Devices not found are silently skipped (nothing to decommission).
        + On CV Create or update existing Workspace with name and description.
            + In-place update workspace object.
        The following steps are executed inside the sync retry loop and repeated if CloudVision requires Workspace synchronization:
        + Stage decommission for decommission devices that exist on CV.
        + Wait for decommission staging to reach terminal state.
        + Delete flat-layout configlets left behind for successfully staged decommission devices. CloudVision removes device-specific containers.
        + On CV in "Inventory & Topology Studio" set/verify hostnames.
        + On CV in "Static Configlet Studio" upload configlets and assign to devices.
            - TODO: Consider if we should create a hierarchy of configuration containers.
                    For now a single folder "AVD Configurations".
        + On CV deploy device tags. Tags for decommission devices are excluded because CloudVision removes their assignments automatically.
          Tag definitions are retained and are not deleted by AVD.
        + On CV deploy interface tags. The same behavior applies.
        + On CV deploy studio inputs
        + On CV deploy cv_pathfinder_metadata
        + On CV delete flat-layout configlets and containers for devices transitioning to the manifest layout.
        + On CV build, submit, abandon, delete the Workspace as applicable based on requested state.
            + In-place update workspace and result object.
        + If not submitting the Workspace return the result object. Otherwise continue.
        + Wait for Workspace submission to return a change control id.
            + Update or create a CVChangeControl object and add to result.
        + On CV set description on the created change control
            - TODO: apply the CC template if given.
        + On CV approve, submit the Change Control as applicable based on requested state.
            - TODO: Support Deleting the CC
        + Return result object.
    """
    LOGGER.info("deploy_to_cv:")
    result = DeployToCvResult(workspace=workspace or CVWorkspace(), change_control=change_control)
    if device_deployments is None:
        device_deployments = []
    if studio_inputs is None:
        studio_inputs = []

    # Split device_deployments into deploy and decommission sub-lists.
    deploy_devices = [device_deployment.device for device_deployment in device_deployments if device_deployment.device.action != "decommission"]
    decommission_devices = [device_deployment.device for device_deployment in device_deployments if device_deployment.device.action == "decommission"]

    # Extract sub-lists from device deployments.
    # TODO: Refactor sub-workflows to accept list[CVDeviceDeployment] directly and extract what they need internally.
    configs, device_tags, interface_tags, cv_pathfinder_metadata = extract_from_device_deployments(device_deployments)

    # Warn if devices are opted into the manifest but no manifest is provided.
    if static_config_manifest is None and any(device_deployment.use_static_config_manifest for device_deployment in device_deployments):
        manifest_device_count = sum(1 for device_deployment in device_deployments if device_deployment.use_static_config_manifest)
        result.warnings.append(
            f"{manifest_device_count} device(s) have 'cv_use_static_config_manifest' set to 'true' but no static config manifest was provided. "
            "These devices will not have their configuration deployed to CloudVision."
        )

    try:
        async with CVClient(
            servers=cloudvision.servers,
            token=cloudvision.token,
            username=cloudvision.username,
            password=cloudvision.password,
            verify_certs=cloudvision.verify_certs,
            use_system_certs=cloudvision.deploy_future.use_system_certs,
            proxy_host=cloudvision.proxy_host,
            proxy_port=cloudvision.proxy_port,
            proxy_username=cloudvision.proxy_username,
            proxy_password=cloudvision.proxy_password,
            grpc_channel_configuration=cloudvision.grpc_channel_configuration,
        ) as cv_client:
            # Create workspace
            await create_workspace_on_cv(workspace=result.workspace, cv_client=cv_client)

            # Check all targeted devices for overlapping `serial_number`s or `system_mac_address`es.
            verify_device_inputs([*deploy_devices, *decommission_devices], result.warnings, strict_system_mac_address=strict_system_mac_address)

            try:
                # Verify that devices targeted for deployment exist and update CVDevice objects with exists_on_cv.
                # Depending on skip_missing_devices we will raise or skip missing devices.
                await verify_devices_on_cv(
                    devices=deploy_devices,
                    workspace_id=result.workspace.id,
                    skip_missing_devices=skip_missing_devices,
                    warnings=result.warnings,
                    cv_client=cv_client,
                )

                # Verify that decommission devices exist on CV (inventory lookup only).
                if decommission_devices:
                    await verify_devices_in_cloudvision_inventory(
                        devices=decommission_devices,
                        # If a device is already gone from CV there is nothing to decommission.
                        skip_missing_devices=True,
                        warnings=result.warnings,
                        cv_client=cv_client,
                        warn_on_missing_devices=False,
                    )
                existing_decommission_devices = [decommission_device for decommission_device in decommission_devices if decommission_device.exists_on_cv]

            except CVClientException as e:
                result.errors.append(e)
                result.failed = True

            if result.failed:
                await cv_client.abandon_workspace(workspace_id=result.workspace.id)
                result.workspace.state = "abandoned"
                return result

            for workspace_sync_attempt in range(result.workspace.max_sync_retries + 1):
                if workspace_sync_attempt > 0:
                    result.reset()

                # Track where warnings from this attempt start so they can be discarded if the Workspace requires synchronization.
                loop_warnings_start = len(result.warnings)

                await _execute_deployment_steps(
                    result=result,
                    configs=configs,
                    device_tags=device_tags,
                    interface_tags=interface_tags,
                    cv_pathfinder_metadata=cv_pathfinder_metadata,
                    static_config_manifest=static_config_manifest,
                    studio_inputs=studio_inputs,
                    device_deployments=device_deployments,
                    strict_tags=strict_tags,
                    cv_client=cv_client,
                    decommission_devices=decommission_devices,
                    existing_decommission_devices=existing_decommission_devices,
                )

                # Build, submit or abandon Workspace. If failed, we always abandon.
                if result.failed:
                    await cv_client.abandon_workspace(workspace_id=result.workspace.id)
                    result.workspace.state = "abandoned"
                    return result

                await finalize_workspace_on_cv(workspace=result.workspace, cv_client=cv_client, devices=deploy_devices, warnings=result.warnings)

                if result.workspace.synchronization_required:
                    await _rebase_workspace_on_cv_or_raise(
                        result=result,
                        cv_client=cv_client,
                        workspace_sync_attempt=workspace_sync_attempt,
                    )
                    # Workspace has been synchronized on CloudVision. We need to replay all changes.
                    del result.warnings[loop_warnings_start:]
                    continue
                # Break for-loop as there was no need to synchronize Workspace on CloudVision. All populated states are up-to-date.
                break

            await _finalize_change_control(result, cv_client)

    except CVClientException as e:
        result.errors.append(e)
        result.failed = True

    return result
