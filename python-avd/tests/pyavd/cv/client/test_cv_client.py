# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from contextlib import AbstractContextManager
from unittest.mock import AsyncMock, Mock, patch

import pytest
from requests.exceptions import HTTPError, RequestException

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.workflows.models import CloudVision, CVGRPCConfiguration, CVGRPCKeepalives, CVTLSConfiguration

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


def _cloudvision(
    *,
    servers: tuple[str, ...] = ("127.0.0.1",),
    token: str | None = "test-token",  # noqa: S107
    username: str | None = None,
    password: str | None = None,
    port: int = 443,
    tls_configuration: CVTLSConfiguration | None = None,
    grpc_configuration: CVGRPCConfiguration | None = None,
) -> CloudVision:
    return CloudVision(
        servers=servers,
        token=token,
        username=username,
        password=password,
        port=port,
        tls_configuration=tls_configuration or CVTLSConfiguration(),
        grpc_configuration=grpc_configuration or CVGRPCConfiguration(),
    )


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
            cloudvision=_cloudvision(
                token=cv_token,
                username="avd_user",
                password="avd_password",  # noqa: S106
            ),
        ) as cvclient:
            await cvclient.get_inventory_devices([("", "", "spine1")])


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("grpc_configuration", "expected_keepalives_applied"),
    [
        pytest.param(None, False, id="NO_CHANNEL_CONFIG"),
        pytest.param(CVGRPCConfiguration(), False, id="DEFAULT_CHANNEL_CONFIG_KEEPALIVES_DISABLED"),
        pytest.param(
            CVGRPCConfiguration(grpc_keepalives=CVGRPCKeepalives(enabled=True)),
            True,
            id="KEEPALIVES_ENABLED_DEFAULTS",
        ),
        pytest.param(
            CVGRPCConfiguration(
                grpc_keepalives=CVGRPCKeepalives(enabled=True, keepalive_time=45, keepalive_timeout=15, permit_without_calls=True),
            ),
            True,
            id="KEEPALIVES_ENABLED_CUSTOM",
        ),
    ],
)
async def test_cv_client_grpc_configuration(
    grpc_configuration: CVGRPCConfiguration | None,
    expected_keepalives_applied: bool,
) -> None:
    """Tests that grpcio options computed from grpc_configuration are passed to the gRPC Channel."""
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
            cloudvision=_cloudvision(grpc_configuration=grpc_configuration or CVGRPCConfiguration()),
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
        assert grpc_configuration is not None
        keepalives = grpc_configuration.grpc_keepalives
        assert grpc_options["grpc.keepalive_time_ms"] == keepalives.keepalive_time * 1000
        assert grpc_options["grpc.keepalive_timeout_ms"] == keepalives.keepalive_timeout * 1000
        assert grpc_options["grpc.keepalive_permit_without_calls"] == int(keepalives.permit_without_calls)
        assert grpc_options["grpc.http2.max_pings_without_data"] == 0
    else:
        assert "grpc.keepalive_time_ms" not in grpc_options
        assert "grpc.http2.max_pings_without_data" not in grpc_options


@pytest.mark.asyncio
async def test_cv_client_uses_cloudvision_port_for_grpc_target() -> None:
    """Tests that CVClient reads the connection port from the CloudVision model."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials"),
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials"),
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials"),
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(cloudvision=_cloudvision(port=8443)):
            pass

    assert mock_secure_channel.call_args.kwargs["target"] == "127.0.0.1:8443"


@pytest.mark.asyncio
async def test_cv_client_verify_certs_clears_stale_ssl_target_name_override() -> None:
    """Tests that an internally computed TLS target override does not leak into verified channels."""
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
            cloudvision=_cloudvision(),
        ):
            pass

    grpc_options = dict(mock_secure_channel.call_args.kwargs["options"])
    assert "grpc.ssl_target_name_override" not in grpc_options
    mock_ssl_channel_credentials.assert_called_once_with()
    mock_access_token_call_credentials.assert_called_once_with("test-token")
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")


def test_cv_client_prepare_cv_connection_no_verify_uses_response_peer_certificate() -> None:
    """Tests that no-verify gRPC TLS is built from the peer certificate on the streamed REST response."""
    der_certificate = b"peer-certificate"
    pem_certificate = ssl.DER_cert_to_PEM_cert(der_certificate)
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}
    mocked_response.raw.connection.sock.getpeercert.return_value = der_certificate

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response) as mock_get,
        patch("pyavd._cv.client.CVTLS._get_certificate_target_name", return_value="cv.example.com") as mock_get_certificate_target_name,
    ):
        prepared_connection = CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(verify_certs=False)))._prepare_cv_connection()

    assert prepared_connection.grpc_tls.root_certificates == pem_certificate.encode()
    assert prepared_connection.grpc_tls.target_name_override == "cv.example.com"
    mock_get_certificate_target_name.assert_called_once_with(pem_certificate)
    assert mock_get.call_args.kwargs["verify"] is False
    assert mock_get.call_args.kwargs["stream"] is True
    mocked_response.raw.connection.sock.getpeercert.assert_called_once_with(binary_form=True)
    mocked_response.close.assert_called_once_with()


def test_cv_client_prepare_cv_connection_no_verify_raises_when_response_socket_has_no_peer_certificate() -> None:
    """Tests that no-verify gRPC setup fails clearly if the REST response does not expose a peer certificate."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.raw.connection.sock.getpeercert.return_value = None

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        pytest.raises(CVClientException, match="Unable to capture CloudVision peer certificate"),
    ):
        CVClient(cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(verify_certs=False)))._prepare_cv_connection()

    mocked_response.close.assert_called_once_with()


@pytest.mark.asyncio
async def test_cv_client_use_system_certs_passes_resolved_roots_to_grpc_credentials() -> None:
    """Tests that roots resolved from the system trust store are passed to grpcio channel credentials."""
    mocked_response = Mock()
    mocked_response.raise_for_status.return_value = None
    mocked_response.json.return_value = {"version": "CVaaS"}

    with (
        patch("pyavd._cv.client.get", return_value=mocked_response),
        patch("pyavd._cv.client._read_root_certificates", return_value=b"root-certificates"),
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials") as mock_ssl_channel_credentials,
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials") as mock_access_token_call_credentials,
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials") as mock_composite_channel_credentials,
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(
            cloudvision=_cloudvision(tls_configuration=CVTLSConfiguration(use_system_certs=True)),
        ):
            pass

    mock_ssl_channel_credentials.assert_called_once_with(root_certificates=b"root-certificates")
    mock_access_token_call_credentials.assert_called_once_with("test-token")
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")
