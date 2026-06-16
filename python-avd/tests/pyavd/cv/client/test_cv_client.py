# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from unittest.mock import AsyncMock, Mock, patch

import pytest
from requests.exceptions import HTTPError, RequestException

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.workflows.models import CVGRPCChannelConfiguration, CVGRPCKeepalives

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
async def test_cv_client_get_token_init_version_requests_error(
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
    ("grpc_channel_configuration", "expected_keepalives_applied"),
    [
        pytest.param(None, False, id="NO_CHANNEL_CONFIG"),
        pytest.param(CVGRPCChannelConfiguration(), False, id="DEFAULT_CHANNEL_CONFIG_KEEPALIVES_DISABLED"),
        pytest.param(
            CVGRPCChannelConfiguration(grpc_keepalives=CVGRPCKeepalives(enabled=True)),
            True,
            id="KEEPALIVES_ENABLED_DEFAULTS",
        ),
        pytest.param(
            CVGRPCChannelConfiguration(
                grpc_keepalives=CVGRPCKeepalives(enabled=True, keepalive_time=45, keepalive_timeout=15, permit_without_calls=True),
            ),
            True,
            id="KEEPALIVES_ENABLED_CUSTOM",
        ),
    ],
)
async def test_cv_client_grpc_channel_configuration(
    grpc_channel_configuration: CVGRPCChannelConfiguration | None,
    expected_keepalives_applied: bool,
) -> None:
    """Tests that grpcio options computed from grpc_channel_configuration are passed to the gRPC Channel."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials") as mock_ssl_channel_credentials,
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials") as mock_access_token_call_credentials,
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials") as mock_composite_channel_credentials,
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(
            servers="127.0.0.1",
            token="test-token",  # noqa: S106
            grpc_channel_configuration=grpc_channel_configuration,
        ):
            pass

    mock_secure_channel.assert_called_once()
    _, kwargs = mock_secure_channel.call_args
    assert kwargs["target"] == "127.0.0.1:443"
    assert kwargs["credentials"] == "channel-credentials"
    mock_ssl_channel_credentials.assert_called_once_with()
    mock_access_token_call_credentials.assert_called_once_with("test-token")
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")
    grpc_options = dict(kwargs["options"])
    assert grpc_options["grpc.primary_user_agent"]

    if expected_keepalives_applied:
        assert grpc_channel_configuration is not None
        keepalives = grpc_channel_configuration.grpc_keepalives
        assert grpc_options["grpc.keepalive_time_ms"] == keepalives.keepalive_time * 1000
        assert grpc_options["grpc.keepalive_timeout_ms"] == keepalives.keepalive_timeout * 1000
        assert grpc_options["grpc.keepalive_permit_without_calls"] == int(keepalives.permit_without_calls)
        assert grpc_options["grpc.http2.max_pings_without_data"] == 0
    else:
        assert "grpc.keepalive_time_ms" not in grpc_options
        assert "grpc.http2.max_pings_without_data" not in grpc_options


@pytest.mark.asyncio
async def test_cv_client_verify_certs_clears_stale_ssl_target_name_override() -> None:
    """Tests that an internally computed TLS target override does not leak into verified channels."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}
    grpc_channel_configuration = CVGRPCChannelConfiguration()
    grpc_channel_configuration._ssl_target_name_override = "stale.example.com"

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials") as mock_ssl_channel_credentials,
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials") as mock_access_token_call_credentials,
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials") as mock_composite_channel_credentials,
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(
            servers="127.0.0.1",
            token="test-token",  # noqa: S106
            grpc_channel_configuration=grpc_channel_configuration,
        ):
            pass

    grpc_options = dict(mock_secure_channel.call_args.kwargs["options"])
    assert "grpc.ssl_target_name_override" not in grpc_options
    mock_ssl_channel_credentials.assert_called_once_with()
    mock_access_token_call_credentials.assert_called_once_with("test-token")
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")
