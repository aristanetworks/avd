# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
import tempfile
from logging import ERROR
from typing import TYPE_CHECKING

import pytest

from pyavd._cv.client.exceptions import CVClientBulkAPIError, CVClientException
from tests.pyavd.cv.constants import (
    MOCKED_CONFIGLET_BODY,
    MOCKED_CONFIGLET_DESCRIPTION,
    MOCKED_CONFIGLET_ID,
    MOCKED_CONFIGLET_NAME,
    MOCKED_EMPTY_CONFIGLET_ID,
    MOCKED_MISSING_WORKSPACE_ID,
    MOCKED_WORKSPACE_ID,
)

if TYPE_CHECKING:
    from pyavd._cv.client import CVClient


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS_CVAAS"], indirect=True)
async def test_set_configlet_from_file_success(cv_client: CVClient) -> None:
    """
    Test successful creation of the Static Studio configlet.

    Successful processing of the `arista.configlet.v1.ConfigletConfigServiceStub.Set` request on CV returns
    ConfigletConfigSetResponse object containing ConfigletConfig object and a timestamp.

    Details of the call:
    -   description: Create configlet
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/54b572019b907d0f7be0d563fd68bb1831b47c49.json'
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        response = await cv_client.set_configlet_from_file(
            workspace_id=MOCKED_WORKSPACE_ID,
            configlet_id=MOCKED_CONFIGLET_ID,
            file=temp_configlet_file.name,
            display_name=MOCKED_CONFIGLET_NAME,
            description=MOCKED_CONFIGLET_DESCRIPTION,
        )

    assert response.key.workspace_id == MOCKED_WORKSPACE_ID
    assert response.key.configlet_id == MOCKED_CONFIGLET_ID
    assert response.display_name == MOCKED_CONFIGLET_NAME
    assert response.description == MOCKED_CONFIGLET_DESCRIPTION
    assert response.body == MOCKED_CONFIGLET_BODY


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
@pytest.mark.parametrize(
    ("workspace_id", "configlet_id", "expected_exception_msg"),
    [
        pytest.param(MOCKED_MISSING_WORKSPACE_ID, MOCKED_CONFIGLET_ID, "workspace does not exist: ws-missing-workspace-id", id="WRONG_WORKSPACE_ID"),
        pytest.param(MOCKED_WORKSPACE_ID, MOCKED_EMPTY_CONFIGLET_ID, "static configlet ID cannot be empty", id="WRONG_CONFIGLET_ID"),
    ],
)
async def test_set_configlet_from_file_failure(
    cv_client: CVClient,
    workspace_id: str,
    configlet_id: str,
    expected_exception_msg: str,
) -> None:
    """
    Test failing creation of the Static Studio configlet.

    Specific use cases:
    1. Attempt to create new configlet referencing non-existing workspace.
        Exact test steps:
        -   description: Create configlet
            request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-missing-workspace-id',
                configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
                description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
            targeted_file: 'arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/27ad4c9d8b0846010836c7e20128d46c79e64887.json'

    2. Attempt to create new configlet with configlet_id being an empty string.
        Exact test steps:
        -   description: Create configlet
            request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
                configlet_id=''), display_name='TEST_CONFIGLET_NAME',
                description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
            targeted_file: 'arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/10ca64d1b48d1bd7d931422ea6a17f4e3af541d9.json'
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        with pytest.raises(CVClientException, match=expected_exception_msg):
            _ = await cv_client.set_configlet_from_file(
                workspace_id=workspace_id,
                configlet_id=configlet_id,
                file=temp_configlet_file.name,
                display_name=MOCKED_CONFIGLET_NAME,
                description=MOCKED_CONFIGLET_DESCRIPTION,
            )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_set_configlets_from_files_cvaas_success(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test successful creation of the Static Studio Configlet using the `arista.configlet.v1.ConfigletConfigServiceStub.SetSome` API.

    arista.configlet.v1.ConfigletConfigServiceStub.SetSome:
        - returns no responses for configlets that were successfully created/updated.
        - returns ConfigletConfigSetSomeResponse object containing ConfigletKey and error (<str>) message for configlets that failed to be created/updated.

    Exact test steps:
    -   description: Create configlet
        request: 'ConfigletConfigSetSomeRequest(values=[ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test')])'
        targeted_file: 'arista.configlet.v1.ConfigletConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/9928854663237cf59f5710079cb64befccffd7cc.json'
    """
    with (
        caplog.at_level(ERROR),
        tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file,
    ):
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        response = await cv_client.set_configlets_from_files(
            workspace_id=MOCKED_WORKSPACE_ID,
            configlets=[
                (
                    MOCKED_CONFIGLET_ID,
                    MOCKED_CONFIGLET_NAME,
                    MOCKED_CONFIGLET_DESCRIPTION,
                    temp_configlet_file.name,
                ),
            ],
        )

    assert len(response) == 0
    # Assert that no ERROR-level logs were emitted by decorator
    assert len(caplog.records) == 0


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_set_configlets_from_files_cvaas_failure(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test attempt to create two Static Studio Configlets with second confilet having an empty ID.

    First configlet gets successfully created inside target Workspace and therefore we are not receiving any response for it.
    Second configlet fails to be created due to empty configlet ID and we receive response with error message for it.

    Exact test steps:
    -   description: Create two configlets
        request: 'ConfigletConfigSetSomeRequest(values=[ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'),
            ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', configlet_id=''),
            display_name='TEST_CONFIGLET_NAME', description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test')])'
        targeted_file: 'arista.configlet.v1.ConfigletConfigService/SetSome/www.cv-prod-us-central1-c.arista.io/8e8300f8e318258406abd987d2ad34e8ac52f114.json'
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        with (
            caplog.at_level(ERROR),
            pytest.raises(
                CVClientBulkAPIError,
                match=(
                    r"One or more server-side errors happened during the execution of the bulk gRPC call for 'set_configlets_from_files'. "
                    r"Please check execution logs for a full list of the failed items."
                ),
            ),
        ):
            _ = await cv_client.set_configlets_from_files(
                workspace_id=MOCKED_WORKSPACE_ID,
                configlets=[
                    (
                        MOCKED_CONFIGLET_ID,
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        temp_configlet_file.name,
                    ),
                    (
                        MOCKED_EMPTY_CONFIGLET_ID,
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        temp_configlet_file.name,
                    ),
                ],
            )

    assert len(caplog.records) == 1
    assert caplog.records[0].message == (
        "GRPCRequestHandler: Execution of the gRPC call for 'set_configlets_from_files' for list_field 'configlets' failed for the following item: "
        "'(ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e', configlet_id=''), 'static configlet ID cannot be empty')'."
    )


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "2024.1.99"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_set_configlets_from_files_max_2024_1_99_success(cv_client: CVClient) -> None:
    """
    Test successful creation of the Static Studio configlets on Cloudvision <= 2024.1.99 using the `arista.configlet.v1.ConfigletConfigServiceStub.Set` API.

    This test generates two calls towards the `arista.configlet.v1.ConfigletConfigServiceStub.Set` API.
    Received responses are identical to those seen when calling self.set_configlet_from_file().

    Details of the call:
    -   description: Create configlet #1
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/54b572019b907d0f7be0d563fd68bb1831b47c49.json'


    -   description: Create configlet #2
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438-2'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/67921e934c74597cacfd4a2b347f6fa8345adcf5.json'
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        response = await cv_client.set_configlets_from_files(
            workspace_id=MOCKED_WORKSPACE_ID,
            configlets=[
                (
                    MOCKED_CONFIGLET_ID,
                    MOCKED_CONFIGLET_NAME,
                    MOCKED_CONFIGLET_DESCRIPTION,
                    temp_configlet_file.name,
                ),
                (
                    MOCKED_CONFIGLET_ID + "-2",
                    MOCKED_CONFIGLET_NAME,
                    MOCKED_CONFIGLET_DESCRIPTION,
                    temp_configlet_file.name,
                ),
            ],
        )

    # Making sure that old version of the method is not returning any responses for successfully created configlets, just like the new one.
    assert len(response) == 0


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "2024.1.99"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_set_configlets_from_files_max_2024_1_99_failure(caplog: pytest.LogCaptureFixture, cv_client: CVClient) -> None:
    """
    Test creation of the Static Studio configlets on Cloudvision <= 2024.1.99 with second configlet having an empty ID.

    This test generates two calls towards the `arista.configlet.v1.ConfigletConfigServiceStub.Set` API.
    Received responses are identical to those seen when calling self.set_configlet_from_file().

    Details of the call:
    -   description: Create configlet #1
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/54b572019b907d0f7be0d563fd68bb1831b47c49.json'


    -   description: Create configlet #2
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id=''), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/10ca64d1b48d1bd7d931422ea6a17f4e3af541d9.json'
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        with (
            caplog.at_level(ERROR),
            pytest.raises(
                CVClientBulkAPIError,
                match=(
                    r"One or more server-side errors happened during the execution of the bulk gRPC call for 'set_configlets_from_files'. "
                    r"Please check execution logs for a full list of the failed items."
                ),
            ),
        ):
            _ = await cv_client.set_configlets_from_files(
                workspace_id=MOCKED_WORKSPACE_ID,
                configlets=[
                    (
                        MOCKED_CONFIGLET_ID,
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        temp_configlet_file.name,
                    ),
                    (
                        MOCKED_EMPTY_CONFIGLET_ID,
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        temp_configlet_file.name,
                    ),
                ],
            )

    assert len(caplog.records) == 1
    expected_log_pattern = (
        r"GRPCRequestHandler: Execution of the gRPC call for 'set_configlets_from_files'.*"
        r"workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e'.*"
        r"static configlet ID cannot be empty"
    )

    assert re.search(expected_log_pattern, caplog.records[0].message)


@pytest.mark.asyncio
@pytest.mark.parametrize("cv_client", [{"static_recording": True, "cv_version": "2024.1.99"}], ids=["CV_CLIENT_STATIC_RECORDINGS"], indirect=True)
async def test_set_configlets_from_files_max_2024_1_99_failure_raise(cv_client: CVClient) -> None:
    """
    Test creation of the Static Studio configlets on Cloudvision <= 2024.1.99 with second configlet referencing non-existing path.

    This test generates two calls towards the `arista.configlet.v1.ConfigletConfigServiceStub.Set` API.
    Received responses are identical to those seen when calling self.set_configlet_from_file().

    Details of the call:
    -   description: Create configlet #1
        request: 'ConfigletConfigSetRequest(value=ConfigletConfig(key=ConfigletKey(workspace_id='ws-cbf7c7ea-a57c-481d-b96b-97c12856395e',
            configlet_id='avd-B51AA89B6E51E89E1422107EDE3A9438'), display_name='TEST_CONFIGLET_NAME',
            description='Configuration created and uploaded by AVD for avd-ci-leaf2', body='alias test test'))'
        targeted_file: '/arista.configlet.v1.ConfigletConfigService/Set/www.cv-prod-us-central1-c.arista.io/54b572019b907d0f7be0d563fd68bb1831b47c49.json'


    -   description: Create configlet #2
        Raises CVClientException from PathNotFoundError
    """
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as temp_configlet_file:
        temp_configlet_file.write(MOCKED_CONFIGLET_BODY)
        temp_configlet_file.flush()

        with pytest.raises(CVClientException, match="No such file or directory"):
            _ = await cv_client.set_configlets_from_files(
                workspace_id=MOCKED_WORKSPACE_ID,
                configlets=[
                    (
                        MOCKED_CONFIGLET_ID,
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        temp_configlet_file.name,
                    ),
                    (
                        MOCKED_CONFIGLET_ID + "-2",
                        MOCKED_CONFIGLET_NAME,
                        MOCKED_CONFIGLET_DESCRIPTION,
                        "broken_path_to_file",
                    ),
                ],
            )
