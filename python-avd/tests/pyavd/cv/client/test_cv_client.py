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
    """Tests that the grpclib Configuration computed from grpc_channel_configuration is correctly passed to the gRPC Channel."""
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
            grpc_channel_configuration=grpc_channel_configuration,
        ):
            pass

    # Assert class was instantiated once
    mock_channel_cls.assert_called_once()
    # Fetch positional args and kwargs during instantiation
    _, kwargs = mock_channel_cls.call_args
    grpc_config = kwargs.get("config")
    assert isinstance(grpc_config, Configuration)

    if expected_keepalives_applied:
        assert grpc_channel_configuration is not None
        keepalives = grpc_channel_configuration.grpc_keepalives
        assert grpc_config._keepalive_time == keepalives.keepalive_time
        assert grpc_config._keepalive_timeout == keepalives.keepalive_timeout
        assert grpc_config._keepalive_permit_without_calls == keepalives.permit_without_calls
        assert grpc_config._http2_max_pings_without_data == 0
        assert grpc_config._http2_min_sent_ping_interval_without_data == keepalives.keepalive_time
    else:
        # _http2_max_pings_without_data should be set to 0 only when keepalives are enabled
        assert grpc_config._http2_max_pings_without_data != 0
