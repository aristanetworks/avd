# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from re import Pattern, error
from re import compile as re_compile
from typing import TYPE_CHECKING

from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus, WorkspaceBuildDetails, WorkspaceState
from pyavd._cv.client.exceptions import CVWorkspaceBuildFailed, CVWorkspaceSubmitFailed, CVWorkspaceSubmitFailedInactiveDevices
from pyavd._utils import get_v2

from .constants import EOS_CLI_WARNINGS
from .models import (
    CVDevice,
    CVWorkspaceBuildConfigValidationError,
    CVWorkspaceBuildConfigValidationResult,
    CVWorkspaceBuildConfigValidationWarning,
    CVWorkspaceDeviceBuildResult,
)

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient

    from .models import CVWorkspace

LOGGER = getLogger(__name__)

WORKSPACE_STATE_TO_FINAL_STATE_MAP = {
    WorkspaceState.ABANDONED: "abandoned",
    WorkspaceState.CONFLICTS: "build failed",
    WorkspaceState.PENDING: "pending",
    WorkspaceState.ROLLED_BACK: "pending",
    WorkspaceState.SUBMITTED: "submitted",
    WorkspaceState.UNSPECIFIED: None,
}


async def finalize_workspace_on_cv(workspace: CVWorkspace, cv_client: CVClient, devices: list[CVDevice], warnings: list) -> None:
    """
    Finalize a Workspace from the given result.CVWorkspace object.

    Depending on the requested state the Workspace will be left in pending, built, submitted, abandoned or deleted.
    In-place update the workspace state and creates/updates a ChangeControl object on the result object if applicable.
    """
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)

    if workspace.requested_state in (workspace.state, "pending"):
        return

    workspace_config = await cv_client.build_workspace(workspace_id=workspace.id)
    build_result, cv_workspace = await cv_client.wait_for_workspace_response(workspace_id=workspace.id, request_id=workspace_config.request_params.request_id)
    workspace.build_id = cv_workspace.last_build_id
    workspace.device_build_results = await _process_workspace_build_details(workspace=workspace, cv_client=cv_client, devices=devices, warnings=warnings)
    if build_result.status != ResponseStatus.SUCCESS:
        workspace.state = "build failed"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        if workspace.requested_state == "abandoned":
            await cv_client.abandon_workspace(workspace_id=workspace.id)
            workspace.state = "abandoned"
            LOGGER.info("finalize_workspace_on_cv: Workspace %s has been successfully abandoned.", workspace.id)
        msg = (
            f"Failed to build workspace {workspace.id}: {build_result}. "
            f"See details: https://{cv_client._servers[0]}/cv/provisioning/workspaces?ws={workspace.id}"
        )
        raise CVWorkspaceBuildFailed(msg)

    workspace.state = "built"
    LOGGER.info("finalize_workspace_on_cv: %s", workspace)
    if workspace.requested_state == "built":
        return

    # We can only submit if the build was successful
    if workspace.requested_state == "submitted" and workspace.state == "built":
        workspace_config = await cv_client.submit_workspace(workspace_id=workspace.id, force=workspace.force)
        submit_result, cv_workspace = await cv_client.wait_for_workspace_response(
            workspace_id=workspace.id,
            request_id=workspace_config.request_params.request_id,
        )
        # Form a list of known inactive existing devices
        if inactive_devices := [f"{device.hostname} ({device.serial_number})" for device in devices if device._streaming is False]:
            msg = f"Inactive devices present: {inactive_devices}"
            warnings.append(msg)
        if submit_result.status != ResponseStatus.SUCCESS:
            workspace.state = "submit failed"
            # Unforced Workspace submission failed due to inactive devices.
            if submit_result.code == ResponseCode.INACTIVE_DEVICES_EXIST:
                # Use case where some of the devices that we targeted were known to be inactive prior to Workspace submission
                if inactive_devices:
                    msg = (
                        f"Failed to submit CloudVision Workspace due to the presence of inactive devices: {inactive_devices}. "
                        f"Use `cv_submit_workspace_force: true` (if using role `cv_deploy`) or `workspace['force']: true` "
                        f"(if using action plugin `cv_workflow`) to override."
                    )
                    raise CVWorkspaceSubmitFailedInactiveDevices(msg)
                # Use case where all devices were actively streaming prior to Workspace submission
                msg = (
                    "Failed to submit CloudVision Workspace due to the presence of inactive devices. "
                    "Use `cv_submit_workspace_force: true` (if using role `cv_deploy`) or `workspace['force']: true` "
                    "(if using action plugin `cv_workflow`) to override."
                )
                raise CVWorkspaceSubmitFailedInactiveDevices(msg)

            # If Workspace submission failed for any other reason - raise general exception.
            LOGGER.info("finalize_workspace_on_cv: %s", workspace)
            msg = f"Failed to submit workspace {workspace.id}: {submit_result}"
            raise CVWorkspaceSubmitFailed(msg)

        workspace.state = "submitted"
        if cv_workspace.cc_ids.values:
            workspace.change_control_id = cv_workspace.cc_ids.values[0]
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    # We can abort or delete even if we got some unexpected build state.
    if workspace.requested_state == "abandoned":
        await cv_client.abandon_workspace(workspace_id=workspace.id)
        workspace.state = "abandoned"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    if workspace.requested_state == "deleted":
        await cv_client.delete_workspace(workspace_id=workspace.id)
        workspace.state = "deleted"
        LOGGER.info("finalize_workspace_on_cv: %s", workspace)
        return

    return


def _prepare_build_warnings_suppress_patterns(
    workspace: CVWorkspace,
    warnings: list,
) -> list[Pattern]:
    """
    Process static and custom inputs for Build Warnings Suppression and return unified list of Regex patterns.

    Parameters:
        workspace: Active Workspace.
        warnings: List of warnings.

    Returns:
        Unified list of compiled Regex patterns describing Workspace Build warnings that we would like to suppress.
    """
    # Deduplicate list of patterns from user
    workspace_build_warnings_suppress_set = set(workspace.build_warnings.suppress_patterns)
    # Add predefined static patterns if requested
    if workspace.build_warnings.suppress_portfast:
        workspace_build_warnings_suppress_set.add(EOS_CLI_WARNINGS["portfast"])

    compiled_workspace_build_warnings_suppress_list: list[Pattern] = []
    for proposed_regex_pattern in workspace_build_warnings_suppress_set:
        try:
            compiled_workspace_build_warnings_suppress_list.append(re_compile(proposed_regex_pattern))
        except error as e:  # noqa: PERF203
            warning = (
                f"_prepare_build_warnings_suppress_patterns: Failed to process proposed regex pattern '{proposed_regex_pattern}'. "
                f"This incorrect pattern will not be used for warnings suppression. Error: '{e}'"
            )
            LOGGER.info(warning)
            warnings.append(warning)

    return compiled_workspace_build_warnings_suppress_list


def _warning_is_suppressed(warning_msg: str, compiled_workspace_build_warnings_suppress_list: list[Pattern]) -> bool:
    """
    Check if a warning message matches any of the suppression patterns.

    Parameters:
        warning_msg: Warning message to check.
        compiled_workspace_build_warnings_suppress_list: List of compiled Regex patterns for matching undesired warnings.

    Returns:
        True if the warning message matches any suppression pattern, False otherwise.
    """
    return any(pattern.fullmatch(warning_msg) for pattern in compiled_workspace_build_warnings_suppress_list)


def _has_unsuppressed_warnings(workspace_build_details_item: WorkspaceBuildDetails, compiled_workspace_build_warnings_suppress_list: list[Pattern]) -> bool:
    """
    Check if workspace build details item has at least one warning that is not suppressed.

    Parameters:
        workspace_build_details_item: WorkspaceBuildDetails object to check.
        compiled_workspace_build_warnings_suppress_list: List of compiled Regex patterns for matching undesired warnings.

    Returns:
        True if at least one warning is not suppressed, False otherwise.
    """
    # If no suppression patterns are provided, all warnings are unsuppressed
    if len(compiled_workspace_build_warnings_suppress_list) == 0:
        return True

    # Check if at least one warning is not matched by any suppression pattern
    warning_values = get_v2(workspace_build_details_item, "config_validation_result.warnings.values", [])
    return any(not _warning_is_suppressed(warning_value.error_msg, compiled_workspace_build_warnings_suppress_list) for warning_value in warning_values)


def _should_include_build_details(
    workspace_build_details_item: WorkspaceBuildDetails,
    workspace: CVWorkspace,
    compiled_workspace_build_warnings_suppress_list: list[Pattern],
) -> bool:
    """
    Check if workspace build details item contains errors or unsuppressed warnings and therefore should be included in the results.

    Parameters:
        workspace_build_details_item: WorkspaceBuildDetails object to check.
        workspace: Active Workspace.
        compiled_workspace_build_warnings_suppress_list: List of compiled Regex patterns for matching undesired warnings.

    Returns:
        True if the build details should be included, False otherwise.
    """
    # Always include if errors are present
    if workspace_build_details_item.config_validation_result.errors:
        return True

    # Include if build warnings are present and they are not requested to be suppressed
    return (
        workspace.build_warnings.enabled
        and workspace_build_details_item.config_validation_result.warnings
        and _has_unsuppressed_warnings(workspace_build_details_item, compiled_workspace_build_warnings_suppress_list)
    )


def _build_errors_list(workspace_build_details_item: WorkspaceBuildDetails) -> list[CVWorkspaceBuildConfigValidationError]:
    """
    Build list of CVWorkspaceBuildConfigValidationError objects from WorkspaceBuildDetails object.

    Parameters:
        workspace_build_details_item: WorkspaceBuildDetails object for one device.

    Returns:
        List of CVWorkspaceBuildConfigValidationError objects for one device.
    """
    return [
        CVWorkspaceBuildConfigValidationError(
            error_msg=config_validation_error.error_msg,
            line_num=config_validation_error.line_num,
            configlet_name=config_validation_error.configlet_name,
        )
        for config_validation_error in get_v2(workspace_build_details_item, "config_validation_result.errors.values", [])
    ]


def _build_warnings_list(
    workspace_build_details_item: WorkspaceBuildDetails,
    workspace: CVWorkspace,
    compiled_workspace_build_warnings_suppress_list: list[Pattern],
) -> list[CVWorkspaceBuildConfigValidationWarning]:
    """
    Build list of CVWorkspaceBuildConfigValidationWarning objects from WorkspaceBuildDetails object.

    Filter out warnings that match any suppression pattern.

    Parameters:
        workspace_build_details_item: WorkspaceBuildDetails object for one device.
        workspace: Active Workspace.
        compiled_workspace_build_warnings_suppress_list: List of compiled Regex patterns for matching undesired warnings.

    Returns:
        List of CVWorkspaceBuildConfigValidationWarning objects for one device.
    """
    if not workspace.build_warnings.enabled:
        return []

    return [
        CVWorkspaceBuildConfigValidationWarning(
            warning_msg=config_validation_warning.error_msg,
            line_num=config_validation_warning.line_num,
            configlet_name=config_validation_warning.configlet_name,
        )
        for config_validation_warning in get_v2(workspace_build_details_item, "config_validation_result.warnings.values", [])
        if not _warning_is_suppressed(config_validation_warning.error_msg, compiled_workspace_build_warnings_suppress_list)
    ]


def _produce_cvworkspace_build_result(
    workspace: CVWorkspace,
    workspace_build_details: list[WorkspaceBuildDetails],
    compiled_workspace_build_warnings_suppress_list: list[Pattern],
    devices: list[CVDevice],
) -> list[CVWorkspaceDeviceBuildResult]:
    """
    Process list of WorkspaceBuildDetails to generate list of CVWorkspaceDeviceBuildResult suppressing undesired warnings (when requested).

    Parameters:
        workspace: Active Workspace.
        workspace_build_details: List of WorkspaceBuildDetails objects.
        compiled_workspace_build_warnings_suppress_list: List of compiled Regex patterns for matching undesired warnings.
        devices: List of CVDevice objects representing existing CV devices.

    Returns:
        List of CVWorkspaceDeviceBuildResult objects defining details of the Workspace build.
    """
    results = []

    for workspace_build_details_item in workspace_build_details:
        # Skip items that don't have errors or unsuppressed warnings
        if not _should_include_build_details(workspace_build_details_item, workspace, compiled_workspace_build_warnings_suppress_list):
            continue

        # Get the device for this build details item. Return None if device ID is not found in the list of targeted devices
        # TODO: Can there be a case where no device is found here? Example: Tag changes leading to the config change for the device we have not targeted.
        device = next((device for device in devices if device.serial_number == workspace_build_details_item.key.device_id), None)

        # Continue if device is not in the list of devices targeted by this deployment
        if device is None:
            LOGGER.warning(
                "_produce_cvworkspace_build_result: Returned WorkspaceBuildDetails object references device '%s' not targeted by our deployment: '%s'",
                workspace_build_details_item.key.device_id,
                workspace_build_details_item,
            )
            continue

        # Build errors and warnings lists
        errors = _build_errors_list(workspace_build_details_item)
        warnings = _build_warnings_list(workspace_build_details_item, workspace, compiled_workspace_build_warnings_suppress_list)

        # Create and append the result
        results.append(
            CVWorkspaceDeviceBuildResult(
                device=device,
                config_validation=CVWorkspaceBuildConfigValidationResult(
                    errors=errors,
                    warnings=warnings,
                ),
            )
        )

    return results


async def _process_workspace_build_details(
    workspace: CVWorkspace,
    cv_client: CVClient,
    devices: list[CVDevice],
    warnings: list,
) -> list[CVWorkspaceDeviceBuildResult]:
    """
    Get and parse Workspace Build Details.

    Extracts (with ability to suppress warnings based on the pre-defined use-cases or custom regex pattern(s)):
    - Config validation errors.
    - Config validation warnings.

    Parameters:
        workspace: Active Workspace.
        cv_client: CVClient.
        devices: List of CVDevice objects representing existing CV devices.
        warnings: List of warnings.

    Returns:
        List of 'CVWorkspaceDeviceBuildResult's describing observed Workspace build validation errors and warnings per targeted device.
    """
    if not workspace.build_id:
        return []
    workspace_build_details = await cv_client.get_workspace_build_details(workspace_id=workspace.id, build_id=workspace.build_id)
    if not workspace_build_details:
        return []

    # Process list of warning suppress patterns if build warnings were requested to be part of the build results.
    compiled_workspace_build_warnings_suppress_list = []
    if workspace.build_warnings.enabled:
        compiled_workspace_build_warnings_suppress_list = _prepare_build_warnings_suppress_patterns(workspace=workspace, warnings=warnings)

    return _produce_cvworkspace_build_result(
        workspace=workspace,
        workspace_build_details=workspace_build_details,
        compiled_workspace_build_warnings_suppress_list=compiled_workspace_build_warnings_suppress_list,
        devices=devices,
    )
