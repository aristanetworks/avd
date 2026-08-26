# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import tempfile
from contextlib import nullcontext as does_not_raise
from logging import DEBUG
from os import environ
from typing import TYPE_CHECKING, Literal
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4

import pytest

from pyavd._cv.api.arista.workspace.v1 import ResponseCode, ResponseStatus
from pyavd._cv.client import CVClient
from pyavd._cv.client.constants import DEFAULT_API_TIMEOUT
from pyavd._cv.client.exceptions import CVResourceNotFound, CVWorkspaceSubmitFailedInactiveDevices, CVWorkspaceSynchronizationAttemptsExhausted
from pyavd._cv.client.models import CVTagAssignment
from pyavd._cv.workflows.deploy_to_cv import _finalize_change_control, deploy_to_cv
from pyavd._cv.workflows.models import (
    AvdDevice,
    AvdWorkspace,
    CloudVision,
    CVChangeControl,
    CVDeployFuture,
    CVDevice,
    CVDeviceDeployment,
    CVDeviceTag,
    CVEosConfig,
    CVGRPCChannelConfiguration,
    CVGRPCKeepalives,
    CVWorkspace,
    DeployToCvResult,
)
from tests.pyavd.cv.constants import (
    MOCKED_WORKSPACE_DESCRIPTION,
    MOCKED_WORKSPACE_ID,
    MOCKED_WORKSPACE_NAME,
    MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS,
    MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS,
    MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
)
from tests.pyavd.cv.mockery import mocked_cvdevices

if TYPE_CHECKING:
    from pyavd._cv.api.arista.workspace.v1 import Response, Workspace, WorkspaceConfig


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "CVaaS"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(("workspace_force_submission"), [pytest.param(False, id="UNFORCED"), pytest.param(True, id="FORCED")])
async def test_deploy_to_cv(
    caplog: pytest.LogCaptureFixture,
    cv_client: CVClient,
    workspace_force_submission: bool,
) -> None:
    """
    Test full functionality of the deploy_to_cv by building and submitting (both forced and unforced) Workspace with a single streaming device.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Wait for Workspace to become ready (PENDING)
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Fetch device status
        request: 'DeviceStreamRequest(partial_eq_filter=[Device(key=DeviceKey(device_id=None), hostname='avd-ci-leaf2', system_mac_address=None)],
            time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.inventory.v1.DeviceService/GetAll/www.cv-prod-us-central1-c.arista.io/effc85b759a4d35ba98ae7c22bcef828c070752d.json'

    -   description: Fetch I&T Studio inputs
        request: 'InputsStreamRequest(partial_eq_filter=[Inputs(key=InputsKey(studio_id='TOPOLOGY', workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))],
            time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetAll/www.cv-prod-us-central1-c.arista.io/0ab698a68a7f9f86eeda70fba362f57cb2f07fc4.json'

    -   description: Create configlet
        request: 'ConfigletConfigSetSomeRequest(values=[ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME', description='Configuration created and
            uploaded by AVD for avd-ci-leaf2', body='alias test test')])'
        targeted_file: 'arista.configlet.v1.ConfigletConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/9928854663237cf59f5710079cb64befccffd7cc.json'

    -   description: Fetch Configlet assignments
        request: 'ConfigletAssignmentStreamRequest(partial_eq_filter=[ConfigletAssignment(key=ConfigletAssignmentKey(workspace_id=
            'ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', configlet_assignment_id='avd-configlets'))], time=TimeBounds(start=None, end=None))'
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/0462b04aed494937b07702371f123831a4e81036.json'

    -   description: Fetch Configlet assignments
        request: 'InputsRequest(key=InputsKey(studio_id='studio-static-configlet', workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            path=RepeatedString(values=['configletAssignmentRoots'])), time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetOne/www.cv-prod-us-central1-c.arista.io/218b79449463543915f8e63e66bdbbbd249333d3.json'

    -   description: Fetch Configlet assignments
        request: 'InputsConfigStreamRequest(partial_eq_filter=InputsConfig(key=InputsKey(studio_id='studio-static-configlet',
            workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', path=RepeatedString(values=['configletAssignmentRoots'])), remove=True), time=None)'
        targeted_file: 'arista.studio.v1.InputsConfigService/GetAll/www.cv-prod-us-central1-c.arista.io/1fbe2ebb45ada87974e6a6228efcce717950d89d.json'

    -   description: Fetch Configlet assignments
        request: 'InputsRequest(key=InputsKey(studio_id='studio-static-configlet', workspace_id='', path=RepeatedString(values=['configletAssignmentRoots'])),
            time=None)'
        targeted_file: 'arista.studio.v1.InputsService/GetOne/www.cv-prod-us-central1-c.arista.io/b45e9b96ea9c215914828995f6c62354ae80296f.json'

    -   description: Fetch configlets assignments
        request: Too long. Please consult JSON file for details.
        targeted_file: 'arista.configlet.v1.ConfigletAssignmentService/GetAll/www.cv-prod-us-central1-c.arista.io/15b2c867c1abf9b0d425ca76fa4327294c18c376.json'

    -   description: Build Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.START_BUILD, request_params=RequestParams(request_id='req-914310f3-08dd-4239-bd42-6d78bf781229')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/1fdd6fcd02728621447eeb8a1d8c9cbfdd9201c9.json'

    -   description: Fetch build results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Fetch Workspace build results
        request: 'WorkspaceBuildDetailsStreamRequest(partial_eq_filter=[WorkspaceBuildDetails(key=WorkspaceBuildDetailsKey(
            workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', build_id='req-914310f3-08dd-4239-bd42-6d78bf781229'))], time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceBuildDetailsService/GetAll/www.cv-prod-us-central1-c.arista.io/
            f451562f4f8c0dc37965a23121bb11dd6efc0f6a.json'

    -   description: Submit Workspace (UNFORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ba83e98eab07691e8b079958618ab2973822bfe8.json'

    -   description: Submit Workspace (FORCED use case)
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            request=Request.SUBMIT_FORCE, request_params=RequestParams(request_id='req-b8f4e511-58de-4afe-99f0-b75abf980131')))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/47049c8a6b520f110540f81bcd892ba0e4954908.json'

    -   description: Fetch submit results
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'
    """
    with (
        caplog.at_level(DEBUG),
        does_not_raise(),
        patch(
            "pyavd._cv.client.workspace.uuid4",
            side_effect=[
                MOCKED_WORKSPACE_REQUEST_ID_BUILD_SUCCESS["id"].removeprefix("req-"),
                MOCKED_WORKSPACE_REQUEST_ID_SUBMIT_SUCCESS["id"].removeprefix("req-"),
            ],
        ),
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=cv_client),
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file,
    ):
        temp_configlet_file.write("alias test test")
        temp_configlet_file.flush()

        device = next(iter(mocked_cvdevices(hostnames=["avd-ci-leaf2"])))
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=None,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(
                avd_workspace=AvdWorkspace(
                    name=MOCKED_WORKSPACE_NAME,
                    description=MOCKED_WORKSPACE_DESCRIPTION,
                    id=MOCKED_WORKSPACE_ID,
                    requested_state=MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED,
                    force=workspace_force_submission,
                )
            ),
            device_deployments=[
                CVDeviceDeployment(
                    device=device,
                    eos_config=CVEosConfig(file=temp_configlet_file.name, device=device, configlet_name="TEST_CONFIGLET_NAME"),
                )
            ],
        )

    # Assess result
    assert not result.failed

    # Assert number of returned warnings
    assert len(result.warnings) == 0

    # Assert number of returned errors
    assert len(result.errors) == 0

    # Assert returned workspace object
    assert result.workspace.name == MOCKED_WORKSPACE_NAME
    assert result.workspace.description == MOCKED_WORKSPACE_DESCRIPTION
    assert result.workspace.id == MOCKED_WORKSPACE_ID
    assert result.workspace.requested_state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED
    assert result.workspace.force == workspace_force_submission
    assert result.workspace.state == MOCKED_WORKSPACE_REQUESTED_STATE_SUBMITTED


@pytest.mark.asyncio
async def test_deploy_to_cv_abandons_workspace_when_device_is_missing() -> None:
    """Test that a missing-device failure abandons the Workspace."""
    mock_cv_client = AsyncMock()
    mock_cv_client.__aenter__.return_value = mock_cv_client
    error = CVResourceNotFound("Missing devices on CloudVision")

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock(side_effect=error)),
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(avd_workspace=AvdWorkspace(id="test-workspace")),
        )

    assert result.failed
    assert result.errors == [error]
    assert result.workspace.state == "abandoned"
    mock_cv_client.abandon_workspace.assert_called_once_with(workspace_id="test-workspace")


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("grpc_channel_configuration"),
    [
        pytest.param(CVGRPCChannelConfiguration(), id="KEEPALIVES_DISABLED_DEFAULTS"),
        pytest.param(CVGRPCChannelConfiguration(grpc_keepalives=CVGRPCKeepalives(enabled=True)), id="KEEPALIVES_ENABLED_DEFAULTS"),
        pytest.param(
            CVGRPCChannelConfiguration(
                grpc_keepalives=CVGRPCKeepalives(enabled=True, keepalive_time=45, keepalive_timeout=15, permit_without_calls=True),
            ),
            id="KEEPALIVES_ENABLED_CUSTOM",
        ),
    ],
)
async def test_deploy_to_cv_grpc_channel_configuration(
    grpc_channel_configuration: CVGRPCChannelConfiguration,
) -> None:
    """Tests that deploy_to_cv passes cloudvision.grpc_channel_configuration to CVClient unchanged."""
    mock_cv_client = AsyncMock()

    with patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client) as mocked_cv_client_cls:
        await deploy_to_cv(
            cloudvision=CloudVision(
                servers="www.arista.io",
                token="test-token",  # noqa: S106
                username=None,
                password=None,
                verify_certs=True,
                proxy_host=None,
                proxy_port=None,
                proxy_username=None,
                proxy_password=None,
                grpc_channel_configuration=grpc_channel_configuration,
            ),
        )

    mocked_cv_client_cls.assert_called_once()
    _, kwargs = mocked_cv_client_cls.call_args
    assert kwargs.get("grpc_channel_configuration") is grpc_channel_configuration


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("deploy_future", "expected_use_system_certs"),
    [
        pytest.param(CVDeployFuture(), False, id="DEPLOY_FUTURE_DEFAULTS"),
        pytest.param(CVDeployFuture(use_system_certs=False), False, id="USE_SYSTEM_CERTS_FALSE_EXPLICIT"),
        pytest.param(CVDeployFuture(use_system_certs=True), True, id="USE_SYSTEM_CERTS_TRUE"),
    ],
)
async def test_deploy_to_cv_deploy_future_use_system_certs(
    deploy_future: CVDeployFuture,
    expected_use_system_certs: bool,
) -> None:
    """Tests that `cloudvision.deploy_future.use_system_certs` is unpacked and passed to `CVClient(use_system_certs=...)`."""
    mock_cv_client = AsyncMock()
    with patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client) as mocked_cv_client_cls:
        await deploy_to_cv(
            cloudvision=CloudVision(
                servers="www.arista.io",
                token="test-token",  # noqa: S106
                username=None,
                password=None,
                verify_certs=True,
                proxy_host=None,
                proxy_port=None,
                proxy_username=None,
                proxy_password=None,
                deploy_future=deploy_future,
            ),
        )

    mocked_cv_client_cls.assert_called_once()
    _, kwargs = mocked_cv_client_cls.call_args
    assert kwargs.get("use_system_certs") == expected_use_system_certs


@pytest.mark.asyncio
async def test_finalize_change_control_with_id(mock_cv_client: MagicMock) -> None:
    """Tests that _finalize_change_control calls finalize_change_control_on_cv when change_control.id is set."""
    result = DeployToCvResult(workspace=CVWorkspace(), change_control=CVChangeControl(id="cc-123"))

    mock_finalize = AsyncMock()
    with patch("pyavd._cv.workflows.deploy_to_cv.finalize_change_control_on_cv", mock_finalize):
        await _finalize_change_control(result, mock_cv_client)

    mock_finalize.assert_called_once_with(change_control=result.change_control, cv_client=mock_cv_client)


@pytest.mark.asyncio
async def test_deploy_to_cv_workspace_sync_retry() -> None:
    """Tests that deploy_to_cv rebuilds the result and replays deployment steps when workspace synchronization is required."""
    mock_cv_client = AsyncMock()
    mock_execute = AsyncMock()
    finalize_workspace_on_cv_call_count = 0

    def _finalize_workspace_on_cv(workspace: CVWorkspace, **_kwargs: object) -> None:
        """Set workspace.synchronization_required to True at first call only."""
        # Refer finalize_workspace_on_cv_call_count variable in test_deploy_to_cv_workspace_sync_retry's scope
        nonlocal finalize_workspace_on_cv_call_count
        finalize_workspace_on_cv_call_count += 1
        if finalize_workspace_on_cv_call_count == 1:
            workspace.synchronization_required = True

    def _rebase_workspace_on_cv(workspace: CVWorkspace, **_kwargs: object) -> None:
        workspace.synchronization_required = False

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv._execute_deployment_steps", mock_execute),
        patch("pyavd._cv.workflows.deploy_to_cv.finalize_workspace_on_cv", AsyncMock(side_effect=_finalize_workspace_on_cv)) as mock_finalize,
        patch("pyavd._cv.workflows.deploy_to_cv.rebase_workspace_on_cv", AsyncMock(side_effect=_rebase_workspace_on_cv)) as mock_rebase,
        patch("pyavd._cv.workflows.deploy_to_cv._finalize_change_control", AsyncMock()),
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(avd_workspace=AvdWorkspace(max_sync_retries=1)),
        )

    assert not result.failed
    assert mock_finalize.call_count == 2
    assert mock_rebase.call_count == 1
    assert mock_execute.call_count == 2


@pytest.mark.asyncio
async def test_deploy_to_cv_attempt_warnings_retained_on_success() -> None:
    """Tests that warnings from a synchronized attempt are discarded while earlier and final-attempt warnings are retained."""
    mock_cv_client = AsyncMock()
    finalize_workspace_on_cv_call_count = 0

    def _verify_devices_on_cv(warnings: list, **_kwargs: object) -> None:
        warnings.append("verification-warning")

    def _finalize_workspace_on_cv(workspace: CVWorkspace, warnings: list, **_kwargs: object) -> None:
        """Append warning at each call and set workspace.synchronization_required to True (only at first call)."""
        # Refer finalize_workspace_on_cv_call_count variable in test_deploy_to_cv_workspace_sync_retry's scope
        nonlocal finalize_workspace_on_cv_call_count
        finalize_workspace_on_cv_call_count += 1
        warnings.append("build-warning")
        if finalize_workspace_on_cv_call_count == 1:
            workspace.synchronization_required = True

    def _rebase_workspace_on_cv(workspace: CVWorkspace, **_kwargs: object) -> None:
        workspace.synchronization_required = False

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock(side_effect=_verify_devices_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv._execute_deployment_steps", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.finalize_workspace_on_cv", AsyncMock(side_effect=_finalize_workspace_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv.rebase_workspace_on_cv", AsyncMock(side_effect=_rebase_workspace_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv._finalize_change_control", AsyncMock()),
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(avd_workspace=AvdWorkspace(max_sync_retries=1)),
        )

    # finalize_workspace_on_cv runs twice (once per attempt) but the first attempt's warning is discarded on sync.
    assert result.warnings == ["verification-warning", "build-warning"]


@pytest.mark.asyncio
async def test_deploy_to_cv_attempt_warnings_from_execute_steps_not_duplicated_on_retry() -> None:
    """Tests that deployment-step warnings from a synchronized attempt are discarded before retrying."""
    mock_cv_client = AsyncMock()
    finalize_workspace_on_cv_call_count = 0

    def _execute_deployment_steps(result: DeployToCvResult, **_kwargs: object) -> None:
        result.warnings.append("deploy-step-warning")

    def _finalize_workspace_on_cv(workspace: CVWorkspace, **_kwargs: object) -> None:
        """Set workspace.synchronization_required to True at first call only."""
        # Refer finalize_workspace_on_cv_call_count variable in test_deploy_to_cv_workspace_sync_retry's scope
        nonlocal finalize_workspace_on_cv_call_count
        finalize_workspace_on_cv_call_count += 1
        if finalize_workspace_on_cv_call_count == 1:
            workspace.synchronization_required = True

    def _rebase_workspace_on_cv(workspace: CVWorkspace, **_kwargs: object) -> None:
        workspace.synchronization_required = False

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv._execute_deployment_steps", AsyncMock(side_effect=_execute_deployment_steps)),
        patch("pyavd._cv.workflows.deploy_to_cv.finalize_workspace_on_cv", AsyncMock(side_effect=_finalize_workspace_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv.rebase_workspace_on_cv", AsyncMock(side_effect=_rebase_workspace_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv._finalize_change_control", AsyncMock()),
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(avd_workspace=AvdWorkspace(max_sync_retries=1)),
        )

    # _execute_deployment_steps runs twice. First attempt's warning is expected to be flushed.
    assert result.warnings == ["deploy-step-warning"]


@pytest.mark.asyncio
async def test_deploy_to_cv_attempt_warnings_retained_when_finalize_raises() -> None:
    """Tests that warnings from the finalization attempt are retained when finalization raises."""
    mock_cv_client = AsyncMock()

    def _finalize_workspace_on_cv(warnings: list, **_kwargs: object) -> None:
        warnings.append("finalize-warning")
        msg = "finalize-error"
        raise CVWorkspaceSubmitFailedInactiveDevices(msg)

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv._execute_deployment_steps", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.finalize_workspace_on_cv", AsyncMock(side_effect=_finalize_workspace_on_cv)),
        patch("pyavd._cv.workflows.deploy_to_cv._finalize_change_control", AsyncMock()) as mock_finalize_change_control,
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(),
        )

    assert result.failed
    assert result.warnings == ["finalize-warning"]
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], CVWorkspaceSubmitFailedInactiveDevices)
    mock_finalize_change_control.assert_not_called()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "max_sync_retries",
    [
        pytest.param(0, id="ZERO_RETRIES"),
        pytest.param(5, id="FIVE_RETRIES"),
    ],
)
async def test_deploy_to_cv_workspace_sync_exhausted(max_sync_retries: int) -> None:
    """Tests that when sync retries are exhausted, deploy_to_cv returns with failed=True and CVWorkspaceSynchronizationAttemptsExhausted in errors."""
    mock_cv_client = AsyncMock()

    def _finalize_workspace_on_cv(workspace: CVWorkspace, warnings: list, **_kwargs: object) -> None:
        warnings.append("sync-required-warning")
        workspace.synchronization_required = True

    with (
        patch("pyavd._cv.workflows.deploy_to_cv.CVClient", return_value=mock_cv_client),
        patch("pyavd._cv.workflows.deploy_to_cv.create_workspace_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_device_inputs"),
        patch("pyavd._cv.workflows.deploy_to_cv.verify_devices_on_cv", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv._execute_deployment_steps", AsyncMock()),
        patch("pyavd._cv.workflows.deploy_to_cv.finalize_workspace_on_cv", AsyncMock(side_effect=_finalize_workspace_on_cv)) as mock_finalize,
        patch("pyavd._cv.workflows.deploy_to_cv.rebase_workspace_on_cv", AsyncMock()) as mock_rebase,
        patch("pyavd._cv.workflows.deploy_to_cv._finalize_change_control", AsyncMock()),
    ):
        result = await deploy_to_cv(
            cloudvision=CloudVision(
                servers="",
                token=None,
                username=None,
                password=None,
                verify_certs=False,
                proxy_host=None,
                proxy_port=8080,
                proxy_username=None,
                proxy_password=None,
            ),
            workspace=CVWorkspace(avd_workspace=AvdWorkspace(id="ws-test-id", name="test-workspace", max_sync_retries=max_sync_retries)),
        )

    assert result.failed
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], CVWorkspaceSynchronizationAttemptsExhausted)
    exc = result.errors[0]
    assert exc.max_sync_retries == max_sync_retries
    assert exc.workspace_name == "test-workspace"
    assert exc.workspace_id == "ws-test-id"
    assert result.warnings == ["sync-required-warning"]
    assert mock_finalize.call_count == max_sync_retries + 1
    assert mock_rebase.call_count == max_sync_retries


@pytest.mark.asyncio
@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy tests are skipped.")
@pytest.mark.parametrize(
    ("targeted_cv", "verify_certs"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_PRD_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_PRD_SERVER", default=""),
            },
            True,
            id="CVAAS_PRD",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_STG_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_STG_SERVER", default=""),
            },
            True,
            id="CVAAS_STG",
        ),
    ],
)
@pytest.mark.parametrize(
    ("pre_build_change_count", "pre_submit_change_count"),
    [pytest.param(1, 1, id="ONE_PRE-BUILD_ONE_PRE-SUBMIT")],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_workspace_synchronization_during_build_and_submit(
    targeted_cv: dict[str, str], verify_certs: bool, pre_build_change_count: int, pre_submit_change_count: int
) -> None:
    """
    Test Workspace synchronization during build and submit against a live CloudVision tenant.

    - Submit and verify baseline tag values for the inactive test device.
    - Deploy tags through a forced Workspace while injecting configured mainline changes.
    - Verify build-time synchronization performs build, rebase, and rebuild.
      - Initial CloudVision state observed by ``deploy_to_cv``: ``NeedsBuild=True``, ``NeedsRebase=False``.
      - After mainline change, CloudVision has ``NeedsBuild=True``, while ``NeedsRebase`` may be ``True`` or ``False`` depending on
        the environment. ``deploy_to_cv`` has not observed the change.
      - After build, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, ``NeedsBuild=False``, ``NeedsRebase=True``.
      - After rebase, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, ``NeedsBuild=True``, ``NeedsRebase=False``.
      - After rebuild, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, ``NeedsBuild=False``, ``NeedsRebase=False``.
    - Verify submit-time synchronization performs submit, rebase, rebuild, and submit retry.
      - Initial CloudVision state observed by ``deploy_to_cv``: ``NeedsBuild=False``, ``NeedsRebase=False``.
      - After mainline change, CloudVision has ``NeedsBuild=False``, while ``NeedsRebase`` may be ``True`` or ``False`` depending on
        the environment. ``deploy_to_cv`` has not observed the change.
      - After submit, ``deploy_to_cv`` observes response status ``FAIL``, code ``SYNCHRONIZATION_REQUIRED``, and ``NeedsRebase=True``.
      - After rebase, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, ``NeedsBuild=True``, ``NeedsRebase=False``.
      - After rebuild, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, ``NeedsBuild=False``, ``NeedsRebase=False``.
      - After submit retry, ``deploy_to_cv`` observes response status ``SUCCESS``, code ``UNSPECIFIED``, and the submitted Workspace.
    - Verify the API responses, event sequence, and final tag values.
    - Restore and verify the baseline tag values.
    """
    live_test_device = "avd-ci-core1"
    tag_labels = (
        "avd-live-ws-sync-test",
        "avd-live-ws-sync-pre-build-change",
        "avd-live-ws-sync-pre-submit-change",
    )
    cloudvision = CloudVision(
        servers=targeted_cv["cv_server"],
        token=targeted_cv["cv_access_token"],
        username=None,
        password=None,
        verify_certs=verify_certs,
        proxy_host=None,
        proxy_port=None,
        proxy_username=None,
        proxy_password=None,
    )
    workspace_api_trace: list[tuple[str, str, str, object | None]] = []
    # Correlate each WUT request ID with the operation that produced it.
    wut_request_operations: dict[str, Literal["build", "rebase", "submit"]] = {}
    # Store terminal WUT responses by operation for synchronization-specific assertions.
    wut_terminal_responses: dict[str, list[tuple[Response, Workspace]]] = {"build": [], "rebase": [], "submit": []}

    async def _deploy_device_tags(
        workspace_id: str,
        workspace_name: str,
        tags: dict[str, str],
        requested_state: Literal["pending", "submitted"],
        max_sync_retries: int = 5,
    ) -> DeployToCvResult:
        """Deploy device tags for the live test device through the deploy_to_cv workflow."""
        device = CVDevice(avd_device=AvdDevice(hostname=live_test_device))
        return await deploy_to_cv(
            cloudvision=cloudvision,
            workspace=CVWorkspace(
                avd_workspace=AvdWorkspace(
                    id=workspace_id,
                    name=workspace_name,
                    requested_state=requested_state,
                    force=True,
                    max_sync_retries=max_sync_retries,
                )
            ),
            device_deployments=[
                CVDeviceDeployment(
                    device=device,
                    device_tags=[CVDeviceTag(label=label, value=value, device=device) for label, value in tags.items()],
                )
            ],
            strict_tags=False,
        )

    def _assert_successful_result(result: DeployToCvResult, expected_state: str, failure_context: str = "Workspace deployment failed") -> None:
        """Assert that a deployment succeeded and reached the expected Workspace state."""
        failure_message = f"{failure_context}. Errors: {result.errors}. Workspace API trace: {workspace_api_trace}"
        assert not result.failed, failure_message
        assert result.errors == [], failure_message
        assert result.workspace is not None, failure_message
        assert result.workspace.state == expected_state, failure_message

    async def _get_mainline_test_tag_values(device_id: str) -> set[tuple[str, str]]:
        """Return the test-owned tag label and value pairs assigned to a device on mainline."""
        async with CVClient(servers=targeted_cv["cv_server"], token=targeted_cv["cv_access_token"], verify_certs=verify_certs) as cv_client:
            assignments = {
                CVTagAssignment.from_api(assignment)
                for assignment in await cv_client.get_tag_assignments(workspace_id="", element_type="device", creator_type="user")
            }
        return {(assignment.label, assignment.value) for assignment in assignments if assignment.label in tag_labels and assignment.device_id == device_id}

    run_id = uuid4().hex[:4]
    baseline_workspace_id = f"ws-avd-live-sync-baseline-{run_id}"
    test_workspace_id = f"ws-avd-live-sync-test-{run_id}"
    cleanup_workspace_id = f"ws-avd-live-sync-cleanup-{run_id}"
    baseline_device_id: str | None = None
    test_tag = {tag_labels[0]: "test"}
    # Track the WUT (Workspace Under Test) lifecycle to verify synchronization during both build and submit.
    events: list[str] = []
    # Track how many mainline changes have been injected for each synchronization phase.
    injected_change_counts = {"build": 0, "submit": 0}

    async def _inject_mainline_change(phase: Literal["build", "submit"]) -> None:
        """Submit one numbered tag change to mainline before a WUT build or submit attempt."""
        injected_change_counts[phase] += 1
        attempt = injected_change_counts[phase]
        tag_label = tag_labels[1] if phase == "build" else tag_labels[2]
        change_result = await _deploy_device_tags(
            workspace_id=f"ws-avd-live-sync-pre-{phase}-change-{attempt}-{run_id}",
            workspace_name=f"AVD live WS sync pre-{phase} change {attempt} {run_id}",
            tags={tag_label: f"attempt-{attempt}"},
            requested_state="submitted",
        )
        _assert_successful_result(change_result, "submitted")
        events.append(f"mainline-change-before-{phase}-{attempt}")

    original_build_workspace = CVClient.build_workspace
    original_rebase_workspace = CVClient.rebase_workspace
    original_submit_workspace = CVClient.submit_workspace
    original_wait_for_workspace_response = CVClient.wait_for_workspace_response

    async def tracked_build_workspace(self: CVClient, workspace_id: str, timeout: float = DEFAULT_API_TIMEOUT) -> WorkspaceConfig:
        """Inject requested pre-build changes and call build_workspace while recording the interaction."""
        if workspace_id == test_workspace_id:
            if injected_change_counts["build"] < pre_build_change_count:
                await _inject_mainline_change("build")
            events.append("build")
        workspace_api_trace.append(("build", "request", workspace_id, None))
        reply = await original_build_workspace(self, workspace_id, timeout)
        workspace_api_trace.append(("build", "reply", workspace_id, reply))
        if workspace_id == test_workspace_id:
            request_id = reply.request_params.request_id
            assert request_id is not None, f"Build reply did not include a request ID. Workspace API trace: {workspace_api_trace}"
            wut_request_operations[request_id] = "build"
        return reply

    async def tracked_rebase_workspace(self: CVClient, workspace_id: str, timeout: float = DEFAULT_API_TIMEOUT) -> WorkspaceConfig:
        """Call rebase_workspace while recording its request, reply, and Test Workspace event."""
        workspace_api_trace.append(("rebase", "request", workspace_id, None))
        if workspace_id == test_workspace_id:
            events.append("rebase")
        reply = await original_rebase_workspace(self, workspace_id, timeout)
        workspace_api_trace.append(("rebase", "reply", workspace_id, reply))
        if workspace_id == test_workspace_id:
            request_id = reply.request_params.request_id
            assert request_id is not None, f"Rebase reply did not include a request ID. Workspace API trace: {workspace_api_trace}"
            wut_request_operations[request_id] = "rebase"
        return reply

    async def submit_workspace_with_mainline_change(
        self: CVClient, workspace_id: str, force: bool = False, timeout: float = DEFAULT_API_TIMEOUT
    ) -> WorkspaceConfig:
        """Inject requested pre-submit mainline changes and call submit_workspace while recording the interaction."""
        if workspace_id == test_workspace_id:
            if injected_change_counts["submit"] < pre_submit_change_count:
                await _inject_mainline_change("submit")
            events.append("submit")
        workspace_api_trace.append(("submit", "request", workspace_id, {"force": force}))
        reply = await original_submit_workspace(self, workspace_id, force, timeout)
        workspace_api_trace.append(("submit", "reply", workspace_id, reply))
        if workspace_id == test_workspace_id:
            request_id = reply.request_params.request_id
            assert request_id is not None, f"Submit reply did not include a request ID. Workspace API trace: {workspace_api_trace}"
            wut_request_operations[request_id] = "submit"
        return reply

    async def tracked_wait_for_workspace_response(
        self: CVClient,
        workspace_id: str,
        request_id: str,
        timeout: float = 3600.0,
    ) -> tuple[Response, Workspace]:
        """Call wait_for_workspace_response while recording and classifying its request and terminal reply."""
        workspace_api_trace.append(("wait_for_response", "request", workspace_id, {"request_id": request_id}))
        reply = await original_wait_for_workspace_response(self, workspace_id, request_id, timeout)
        workspace_api_trace.append(("wait_for_response", "reply", workspace_id, reply))
        if workspace_id == test_workspace_id:
            wut_terminal_responses[wut_request_operations[request_id]].append(reply)
        return reply

    try:
        with (
            patch.object(CVClient, "build_workspace", tracked_build_workspace),
            patch.object(CVClient, "rebase_workspace", tracked_rebase_workspace),
            patch.object(CVClient, "submit_workspace", submit_workspace_with_mainline_change),
            patch.object(CVClient, "wait_for_workspace_response", tracked_wait_for_workspace_response),
        ):
            # Enforce correct initial state for the test (device is associated with cleanup tags)
            baseline_result = await _deploy_device_tags(
                workspace_id=baseline_workspace_id,
                workspace_name=f"AVD live WS sync baseline {run_id}",
                tags=dict.fromkeys(tag_labels, "cleanup"),
                requested_state="submitted",
            )
            _assert_successful_result(baseline_result, "submitted")
            baseline_tag = baseline_result.deployed_device_tags[0]
            assert baseline_tag.device is not None, workspace_api_trace
            assert baseline_tag.device.serial_number is not None, workspace_api_trace
            baseline_device_id = baseline_tag.device.serial_number
            assert await _get_mainline_test_tag_values(baseline_device_id) == {(label, "cleanup") for label in tag_labels}, (
                f"Failed to enforce cleanup tag values on {live_test_device} before the test. Workspace API trace: {workspace_api_trace}"
            )

            submitted_result = await _deploy_device_tags(
                workspace_id=test_workspace_id,
                workspace_name=f"AVD live WS sync test {run_id}",
                tags=test_tag,
                requested_state="submitted",
                max_sync_retries=pre_build_change_count + pre_submit_change_count,
            )
            _assert_successful_result(submitted_result, "submitted")
            deployed_test_tag = submitted_result.deployed_device_tags[0]
            assert deployed_test_tag.device is not None
            assert deployed_test_tag.device.serial_number is not None
            device_id = deployed_test_tag.device.serial_number

        expected_events: list[str] = []
        for attempt in range(1, pre_build_change_count + 1):
            expected_events.extend([f"mainline-change-before-build-{attempt}", "build", "rebase"])
        expected_events.append("build")
        for attempt in range(1, pre_submit_change_count + 1):
            expected_events.extend([f"mainline-change-before-submit-{attempt}", "submit", "rebase", "build"])
        expected_events.append("submit")
        assert events == expected_events, f"Unexpected event sequence. Workspace API trace: {workspace_api_trace}"

        build_responses = wut_terminal_responses["build"]
        # Build after each pre-build chamge + final build + build after each pre-submit build
        assert len(build_responses) == pre_build_change_count + 1 + pre_submit_change_count, workspace_api_trace
        # Attempt to build WS requiring SYNC returns `response.status == ResponseStatus.SUCCESS` and `workspace.needs_rebase == True`
        assert all(response.status == ResponseStatus.SUCCESS for response, _workspace in build_responses), workspace_api_trace
        assert [workspace.needs_rebase for _response, workspace in build_responses] == [True] * pre_build_change_count + [False] * (
            pre_submit_change_count + 1
        ), workspace_api_trace

        rebase_responses = wut_terminal_responses["rebase"]
        # Rebase after each pre-build change and each pre-submit change
        assert len(rebase_responses) == pre_build_change_count + pre_submit_change_count, workspace_api_trace
        assert all(response.status == ResponseStatus.SUCCESS for response, _workspace in rebase_responses), workspace_api_trace

        submit_responses = wut_terminal_responses["submit"]
        # Submit per every pre-submit change + final submit
        assert len(submit_responses) == 1 + pre_submit_change_count, workspace_api_trace
        # Attempt to submit WS requiring SYNC returns `response.status == ResponseStatus.FAIL`` and `response.code == ResponseCode.SYNCHRONIZATION_REQUIRED`
        assert all(
            response.status == ResponseStatus.FAIL and response.code == ResponseCode.SYNCHRONIZATION_REQUIRED for response, _workspace in submit_responses[:-1]
        ), workspace_api_trace
        # Final submit simply returns SUCCESS
        assert submit_responses[-1][0].status == ResponseStatus.SUCCESS, workspace_api_trace

        expected_tag_values = {
            (tag_labels[0], "test"),
            (tag_labels[1], f"attempt-{pre_build_change_count}" if pre_build_change_count else "cleanup"),
            (tag_labels[2], f"attempt-{pre_submit_change_count}" if pre_submit_change_count else "cleanup"),
        }
        assert await _get_mainline_test_tag_values(device_id) == expected_tag_values
    finally:
        if any(injected_change_counts.values()):
            cleanup_result = await _deploy_device_tags(
                workspace_id=cleanup_workspace_id,
                workspace_name=f"AVD live WS sync cleanup {run_id}",
                tags=dict.fromkeys(tag_labels, "cleanup"),
                requested_state="submitted",
            )
            _assert_successful_result(
                cleanup_result,
                "submitted",
                failure_context=(
                    f"Failed to reset test tag assignments on {live_test_device}. Test values may remain assigned to labels {tag_labels} on mainline"
                ),
            )
            assert baseline_device_id is not None, f"Failed to identify {live_test_device} before verifying cleanup. Workspace API trace: {workspace_api_trace}"
            assert await _get_mainline_test_tag_values(baseline_device_id) == {(label, "cleanup") for label in tag_labels}, (
                f"Failed to verify cleanup tag values on {live_test_device}. Workspace API trace: {workspace_api_trace}"
            )
