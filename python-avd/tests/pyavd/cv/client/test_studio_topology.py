# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from logging import DEBUG, ERROR
from typing import TYPE_CHECKING

import pytest

from pyavd._cv.client.exceptions import CVClientBulkAPIError, CVTimeoutError
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import AvdWorkspace, CVWorkspace

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_stage_devices_for_decommission_success(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test successful staging of two devices (actively streaming devices, onboarded to I&T studio) for decommissionning.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Initiate decommissioning of two actively streaming devices
        request: 'DecommissionConfigSetSomeRequest(values=['
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='1207F35678E44BD8E7C7EC8BB18DDB8C')), '
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='D60EC473E29C51A45C50D84B9D89F756'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/'
            'f4729b49a5e4423ea28d9eabe6625cbd217fbe6a.json'

    -   description: Await to stage decommissioning of two actively streaming devices to succeed
        request: 'DecommissionStreamRequest(partial_eq_filter=['
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='1207F35678E44BD8E7C7EC8BB18DDB8C')), '
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='D60EC473E29C51A45C50D84B9D89F756'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionService/Subscribe/www.cv-prod-us-central1-c.arista.io/'
            '4fef58599c5ce79fb6eafc626297b251af9a1afc.json'
    """
    target_devices = ["1207F35678E44BD8E7C7EC8BB18DDB8C", "D60EC473E29C51A45C50D84B9D89F756"]
    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION"))
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of two test devices. This triggers backend operations (checks, etc) on CloudVision
        stage_devices_for_decommission_response = await cv_client.stage_devices_for_decommission(workspace_id=workspace.id, device_ids=target_devices)
        # stage_devices_for_decommission method returns only failed responses
        assert len(stage_devices_for_decommission_response) == 0

        # Subscribe for decommissining updates. They all must succeed prior to next steps (building Workspace, submitting Workspace)
        wait_for_device_decommission_staging_response = await cv_client.wait_for_device_decommission_staging(
            workspace_id=workspace.id, device_ids=target_devices
        )

    assert len(wait_for_device_decommission_staging_response) == len(target_devices)
    for response in wait_for_device_decommission_staging_response:
        assert response.key.device_id in target_devices
        assert response.key.workspace_id == workspace_id
        assert not response.error

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_device_decommission_staging: Received decommission staging response: Decommission\(key=DeviceKey\(device_id=None\), "
                r"status=DecommissionStatus.UNSPECIFIED\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.SUCCESS is received and logged for both devices
    for target_device in target_devices:
        assert any(
            re.search(
                re.compile(f"wait_for_device_decommission_staging: Staging device {target_device} for decommission completed"),
                str(record.message),
            )
            for record in caplog.records
        )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_stage_devices_for_decommission_failure(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test failed staging of a single device (inactive Recorder node) for decommissioning.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Initiate decommissioning of one inactive Recorder node device which has already been successfully staged for decomm in the same Workspace.
        request: 'DecommissionConfigSetSomeRequest(values=[DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', "
            "device_id='87b21e181f36dd527521a21794ee8e231d591541'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/"
            "604bfd44e7e8a3b397200d3c8bd6139810d295c1.json'
    """
    target_devices = ["87b21e181f36dd527521a21794ee8e231d591541"]
    expected_exception_msg = (
        r"1 server-side error\(s\) was returned from the 'stage_devices_for_decommission' bulk API call. "
        "Please check logs for the failed items and error messages."
    )

    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION"))
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(ERROR), pytest.raises(CVClientBulkAPIError, match=expected_exception_msg):
        _ = await cv_client.stage_devices_for_decommission(workspace_id=workspace.id, device_ids=target_devices)

    # Assert that error message is logged
    assert any(
        re.search(
            re.compile(
                r"stage_devices_for_decommission: API Call failed 'rpc error: code = InvalidArgument desc = notification 0: empty' for "
                r"'DeviceKey\(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='87b21e181f36dd527521a21794ee8e231d591541'\)'"
            ),
            str(record.message),
        )
        for record in caplog.records
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_stage_devices_for_decommission_wait_for_failure(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test unsuccessful decommissioning of four devices where issues are faced when subscribing for decomm staging updates.

    Staging for decommission for the first device succeeds.
    Staging for decommission for the second device fails with FAILURE.
    Staging for decommission for the third device stucks with a single UNSPECIFIED update without ever getting update with terminal status.
    Staging for decommission for the forth device fails due to not receiving any updates at all.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Initiate decommissioning of four devices
        request: 'DecommissionConfigSetSomeRequest(values=['
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_one_id_ok')), '
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_two_id_failure')), '
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_three_id_unspecified')), '
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_four_id_silent'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/'
            'b3e60e1cbdf9dcce704bfbc7ac843c0d35635c4d.json'

    # TODO: Recording file below is handcrafted. Find out a way to hit all these negative cases live on CloudVision
    -   description: Await to stage decommissioning of four devices
        request: 'DecommissionStreamRequest(partial_eq_filter=['
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_one_id_ok')), '
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_two_id_failure')), '
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_three_id_unspecified')), '
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_four_id_silent'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionService/Subscribe/www.cv-prod-us-central1-c.arista.io/'
            'aff03f31ff54008136884a1dbfdaa0f0fc791774.json'
    """
    target_devices = ["device_one_id_ok", "device_two_id_failure", "device_three_id_unspecified", "device_four_id_silent"]

    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION"))
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of four test devices. This triggers backend operations (checks, etc) on CloudVision
        stage_devices_for_decommission_response = await cv_client.stage_devices_for_decommission(workspace_id=workspace.id, device_ids=target_devices)
        # stage_devices_for_decommission method returns only failed responses
        assert len(stage_devices_for_decommission_response) == 0

        with pytest.raises(CVTimeoutError) as exc_info:
            # Subscribe for decommissining updates.
            _ = await cv_client.wait_for_device_decommission_staging(workspace_id=workspace.id, device_ids=target_devices)

    assert "Decommission staging timed out for the following devices:" in str(exc_info.value)
    assert "device_three_id_unspecified" in str(exc_info.value)
    assert "device_four_id_silent" in str(exc_info.value)

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_device_decommission_staging: Received decommission staging response: Decommission\(key=DeviceKey\(device_id=None\), "
                r"status=DecommissionStatus.UNSPECIFIED\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.SUCCESS is received and logged for the first device
    assert any(
        re.search(
            re.compile("wait_for_device_decommission_staging: Staging device device_one_id_ok for decommission completed"),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.FAILURE is received and logged for the second device
    assert any(
        re.search(
            re.compile(
                "wait_for_device_decommission_staging: Staging device device_two_id_failure for decommission completed.*"
                "status=DecommissionStatus.FAILURE, error='error getting decommissioned device status'"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.UNSPECIFIED is received and logged for the third device
    assert any(
        re.search(
            re.compile(
                "wait_for_device_decommission_staging: Received decommission staging response:.*"
                "device_id='device_three_id_unspecified'.*status=DecommissionStatus.UNSPECIFIED, error=''"
            ),
            str(record.message),
        )
        for record in caplog.records
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_stage_devices_for_decommission_wait_for_mixed_terminal(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test partially successful decommissioning where every device reaches a terminal status, but not all of them succeed.

    All terminal responses are returned regardless of status — the caller decides how to handle failures.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Initiate decommissioning of two devices
        request: 'DecommissionConfigSetSomeRequest(values=['
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_one_id_ok')), '
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_two_id_failure')), '
        targeted_file: 'arista.studio_topology.v1.DecommissionConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/'
            '2ac3a7cdafdec8558d8560e3f7d76b9f6ea00d49.json'

    -   description: Await to stage decommissioning of two devices
        request: 'DecommissionStreamRequest(partial_eq_filter=['
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_one_id_ok')), '
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_two_id_failure')), '
        targeted_file: 'arista.studio_topology.v1.DecommissionService/Subscribe/www.cv-prod-us-central1-c.arista.io/'
            'f086a8e34b692a31f83fb9899081a798a4adcda6.json'
    """
    target_devices = ["device_one_id_ok", "device_two_id_failure"]

    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION"))
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of two test devices. This triggers backend operations (checks, etc) on CloudVision
        stage_devices_for_decommission_response = await cv_client.stage_devices_for_decommission(workspace_id=workspace.id, device_ids=target_devices)
        # stage_devices_for_decommission method returns only failed responses
        assert len(stage_devices_for_decommission_response) == 0

        # Both devices reach terminal status. No exception is raised.
        wait_for_device_decommission_staging_response = await cv_client.wait_for_device_decommission_staging(
            workspace_id=workspace.id, device_ids=target_devices
        )

    assert {r.key.device_id for r in wait_for_device_decommission_staging_response} == set(target_devices)

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_device_decommission_staging: Received decommission staging response: Decommission\(key=DeviceKey\(device_id=None\), "
                r"status=DecommissionStatus.UNSPECIFIED\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.SUCCESS is received and logged for the first device
    assert any(
        re.search(
            re.compile("wait_for_device_decommission_staging: Staging device device_one_id_ok for decommission completed"),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.FAILURE is received and logged for the second device
    assert any(
        re.search(
            re.compile(
                "wait_for_device_decommission_staging: Staging device device_two_id_failure for decommission completed.*"
                "status=DecommissionStatus.FAILURE, error='error getting decommissioned device status'"
            ),
            str(record.message),
        )
        for record in caplog.records
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_stage_devices_for_decommission_wait_for_all_silent(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test unsuccessful decommissioning where the stream closes after INITIAL_SYNC_COMPLETE without any per-device update.

    Specific use case to test loop exiting naturally and raising with only the `no response` section in the error message.

    Exact test steps:
    -   description: Fetch Workspace status
        request: 'WorkspaceRequest(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'), time=None)'
        targeted_file: 'arista.workspace.v1.WorkspaceService/GetOne/www.cv-prod-us-central1-c.arista.io/a996cf0f4bc694971e5d4069f481faaba80f68b2.json'

    -   description: Create Workspace
        request: 'WorkspaceConfigSetRequest(value=WorkspaceConfig(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'),
            display_name='MOCKED_WS_NAME', description='MOCKED_WS_DESCRIPTION'))'
        targeted_file: 'arista.workspace.v1.WorkspaceConfigService/Set/www.cv-prod-us-central1-c.arista.io/ce73310ec5154d57ac888fc8f93d69893962d804.json'

    -   description: Await until Workspace reaches PENDING state
        request: 'WorkspaceStreamRequest(partial_eq_filter=[Workspace(key=WorkspaceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'))])'
        targeted_file: 'arista.workspace.v1.WorkspaceService/Subscribe/www.cv-prod-us-central1-c.arista.io/1560c66d73da2be39448d710f15853fb124b2548.json'

    -   description: Initiate decommissioning of one device
        request: 'DecommissionConfigSetSomeRequest(values=['
            'DecommissionConfig(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_four_id_silent'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/'
            '0ae5e9edd17647dee9d0dd0cc7312f4ace15b856.json'

    -   description: Await to stage decommissioning of one device
        request: 'DecommissionStreamRequest(partial_eq_filter=['
            'Decommission(key=DeviceKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', device_id='device_four_id_silent'))])'
        targeted_file: 'arista.studio_topology.v1.DecommissionService/Subscribe/www.cv-prod-us-central1-c.arista.io/'
            '83d945b70ef4fc507f316bfbdf25a7fc17c47ca6.json'
    """
    target_devices = ["device_four_id_silent"]
    expected_exception_msg = r"Decommission staging timed out for the following devices: \{'device_four_id_silent'\}\."

    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(avd_workspace=AvdWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION"))
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of a test device. This triggers backend operations (checks, etc) on CloudVision
        stage_devices_for_decommission_response = await cv_client.stage_devices_for_decommission(workspace_id=workspace.id, device_ids=target_devices)
        # stage_devices_for_decommission method returns only failed responses
        assert len(stage_devices_for_decommission_response) == 0

        with pytest.raises(CVTimeoutError, match=expected_exception_msg):
            # Subscribe for decommissining updates.
            _ = await cv_client.wait_for_device_decommission_staging(workspace_id=workspace.id, device_ids=target_devices)

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_device_decommission_staging: Received decommission staging response: Decommission\(key=DeviceKey\(device_id=None\), "
                r"status=DecommissionStatus.UNSPECIFIED\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )
