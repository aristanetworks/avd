# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from logging import DEBUG
from typing import TYPE_CHECKING

import pytest

from pyavd._cv.client.exceptions import CVDeviceDecommissionFailed
from pyavd._cv.workflows.create_workspace_on_cv import create_workspace_on_cv
from pyavd._cv.workflows.models import CVWorkspace

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_decommission_devices_success(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test successful decommissioning of two actively streaming devices onboarded to I&T studio.

    This test only covers initiation of the decommission operations and awaiting for decommission status to be SUCCESS for both devices.
    This test does not cover following steps iof the decommissioning (building and submitting Workspace).

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
    workspace = CVWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION")
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of two test devices. This triggers backend operations (checks, etc) on CloudVision
        decommission_devices_response = await cv_client.decommission_devices(workspace_id=workspace.id, device_ids=target_devices)
        # decommission_devices method returns only failed responses
        assert len(decommission_devices_response) == 0

        # Subscribe for decommissining updates. They all must succeed prior to next steps (building Workspace, submitting Workspace)
        wait_for_decommission_devices_response = await cv_client.wait_for_devices_decommission(workspace_id=workspace.id, device_ids=target_devices)

    assert len(wait_for_decommission_devices_response) == len(target_devices)
    for response in wait_for_decommission_devices_response:
        assert response.key.device_id in target_devices
        assert response.key.workspace_id == workspace_id
        assert not response.error

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_devices_decommission: Got decommission update: Decommission\(key=DeviceKey\(device_id=None\), "
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
                re.compile(f"wait_for_devices_decommission: Decommissioning of device {target_device} succeeded"),
                str(record.message),
            )
            for record in caplog.records
        )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_decommission_devices_wait_for_failure(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test unsuccessful decommissioning of four devices where issues are faced when subscribing for decomm staging updates.

    Stating of decommissioning for the first device succeeds.
    Stating of decommissioning for the second device fails with FAILURE.
    # TODO: Confirm that UNSPECIFIED status in this case is still non-terminal.
    Stating of decommissioning for the third device stucks with a single UNSPECIFIED update without ever getting update with terminal status.
    Stating of decommissioning for the forth device fails due to not receiving any updates at all.

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
    expected_exception_msg = (
        "No decommission response received for the following devices: {'device_four_id_silent'}. "
        "Non-success decommission response received for the following devices:.*"
        "'device_two_id_failure':.*status=DecommissionStatus.FAILURE, error='error getting decommissioned device status'.*"
        "'device_three_id_unspecified':.*status=DecommissionStatus.UNSPECIFIED, error=''.*"
    )

    # create new workspace
    workspace_id = "ws-cbf7c7ea-a57c-481d-b96b-97c12856395e"
    workspace = CVWorkspace(id=workspace_id, name="MOCKED_WS_NAME", description="MOCKED_WS_DESCRIPTION")
    await create_workspace_on_cv(workspace=workspace, cv_client=cv_client)

    with caplog.at_level(DEBUG):
        # Initiate decommissioning of four test devices. This triggers backend operations (checks, etc) on CloudVision
        decommission_devices_response = await cv_client.decommission_devices(workspace_id=workspace.id, device_ids=target_devices)
        # decommission_devices method returns only failed responses
        assert len(decommission_devices_response) == 0

        with pytest.raises(CVDeviceDecommissionFailed, match=expected_exception_msg):
            # Subscribe for decommissining updates.
            _ = await cv_client.wait_for_devices_decommission(workspace_id=workspace.id, device_ids=target_devices)

    # Assert that initial INITIAL_SYNC_COMPLETE is received and logged
    assert any(
        re.search(
            re.compile(
                r"wait_for_devices_decommission: Got decommission update: Decommission\(key=DeviceKey\(device_id=None\), "
                r"status=DecommissionStatus.UNSPECIFIED\)"
            ),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.SUCCESS is received and logged for the first device
    assert any(
        re.search(
            re.compile("wait_for_devices_decommission: Decommissioning of device device_one_id_ok succeeded"),
            str(record.message),
        )
        for record in caplog.records
    )

    # Assert that DecommissionStatus.FAILURE is received and logged for the second device
    assert any(
        re.search(
            re.compile(
                "wait_for_devices_decommission: Decommissioning of device device_two_id_failure reached non-success terminal status FAILURE.*"
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
                "wait_for_devices_decommission: Got decommission update:.*"
                "device_id='device_three_id_unspecified'.*status=DecommissionStatus.UNSPECIFIED, error=''"
            ),
            str(record.message),
        )
        for record in caplog.records
    )
