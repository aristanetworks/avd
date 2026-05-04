# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from unittest.mock import Mock, patch

import pytest
from grpclib.config import Configuration
from requests.exceptions import HTTPError, RequestException

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("cv_token", "exception_to_raise", "expected_cv_exception"),
    [
        pytest.param(
            None,
            HTTPError,
            pytest.raises(CVClientException, match="Unable to get token from CloudVision server due to the following error"),
            id="SET_TOKEN_HTTPERROR",
        ),
        pytest.param(
            None,
            RequestException,
            pytest.raises(CVClientException, match="Unable to get token from CloudVision server due to the following error"),
            id="SET_TOKEN_REQUESTEXCEPTION",
        ),
        pytest.param(
            "cv_token",
            HTTPError,
            pytest.raises(CVClientException, match="Unable to get version from CloudVision server due to the following error"),
            id="SET_VERSION_HTTPERROR",
        ),
        pytest.param(
            "cv_token",
            RequestException,
            pytest.raises(CVClientException, match="Unable to get version from CloudVision server due to the following error"),
            id="SET_VERSION_REQUESTEXCEPTION",
        ),
    ],
)
async def test_cv_client_set_token_set_version_requests_error(
    cv_token: str | None,
    exception_to_raise: Exception,
    expected_cv_exception: ExpectedExceptionContext,
) -> None:
    mocked_response = Mock()
    mocked_response.raise_for_status.side_effect = exception_to_raise

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.post", return_value=mocked_response),
        expected_cv_exception,
    ):
        async with CVClient(
            servers="127.0.0.1",
            token=cv_token,
            username="avd_user",
            password="avd_password",  # noqa: S106
        ) as cvclient:
            await cvclient.get_inventory_devices([("", "", "spine1")])


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("grpc_config"),
    [
        pytest.param(None, id="NO_GRPC_CONFIG"),
        pytest.param(
            Configuration(_keepalive_time=50, _keepalive_timeout=20, _keepalive_permit_without_calls=False),
            id="PARTIAL_GRPC_CONFIG_1",
        ),
        pytest.param(
            Configuration(_keepalive_time=60, _keepalive_timeout=30, _keepalive_permit_without_calls=False),
            id="PARTIAL_GRPC_CONFIG_2",
        ),
        pytest.param(
            Configuration(_keepalive_time=60, _keepalive_timeout=20, _keepalive_permit_without_calls=True),
            id="PARTIAL_GRPC_CONFIG_3",
        ),
        pytest.param(
            Configuration(_keepalive_time=60, _keepalive_timeout=20, _keepalive_permit_without_calls=False),
            id="FULL_GRPC_CONFIG",
        ),
    ],
)
async def test_cv_client_grpc_config(
    grpc_config: Configuration | None,
) -> None:
    """Tests that grpc_config is correctly passed to the gRPC Channel on connect."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.Channel") as mock_channel_cls,
    ):
        async with CVClient(
            servers="127.0.0.1",
            token="test-token",  # noqa: S106
            grpc_config=grpc_config,
        ):
            pass

    # Assert class was instantiated once
    mock_channel_cls.assert_called_once()
    # Fetch positional args and kwargs during instantiation
    _, kwargs = mock_channel_cls.call_args
    assert kwargs.get("config") == grpc_config
