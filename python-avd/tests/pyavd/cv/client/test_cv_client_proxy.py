# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ
from unittest.mock import AsyncMock, patch

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.workflows.models import CVGRPCChannelConfiguration, CVGRPCProxyConfiguration

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


@pytest.mark.asyncio
async def test_cv_client_authenticated_proxy_is_mapped_to_grpc_channel_options() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"
    proxy_username = "avd_user"
    proxy_password = "avd_password"  # noqa: S105

    with (
        patch("pyavd._cv.client.CVClient._init_version", return_value="CVaaS"),
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            assert cvclient.grpc.configuration.proxy == CVGRPCProxyConfiguration(
                host=proxy_host,
                port=8080,
                username=proxy_username,
                password=proxy_password,
            )

    grpc_options = dict(mock_secure_channel.call_args.kwargs["options"])
    assert grpc_options["grpc.http_proxy"] == f"http://{proxy_username}:{proxy_password}@{proxy_host}:8080"


@pytest.mark.asyncio
async def test_cv_client_no_verify_certs() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    peer_certificate = "-----BEGIN CERTIFICATE-----\ntest\n-----END CERTIFICATE-----\n"

    with (
        patch("pyavd._cv.client.CVClient._init_version", return_value="CVaaS"),
        patch("pyavd._cv.client.ssl.get_server_certificate", return_value=peer_certificate) as mock_get_server_certificate,
        patch("pyavd._cv.client.CVGRPCTransport._get_server_certificate_target_name", return_value="cv.example.com") as mock_get_server_certificate_target_name,
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials") as mock_ssl_channel_credentials,
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials") as mock_access_token_call_credentials,
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials") as mock_composite_channel_credentials,
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(servers=servers, token=token, verify_certs=False):
            pass

    mock_get_server_certificate.assert_called_once_with((servers, 443))
    mock_get_server_certificate_target_name.assert_called_once_with(peer_certificate)
    mock_ssl_channel_credentials.assert_called_once_with(root_certificates=peer_certificate.encode())
    mock_access_token_call_credentials.assert_called_once_with(token)
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")
    assert mock_secure_channel.call_args.kwargs["credentials"] == "channel-credentials"
    grpc_options = dict(mock_secure_channel.call_args.kwargs["options"])
    assert grpc_options["grpc.ssl_target_name_override"] == "cv.example.com"


def test_cv_client_no_verify_certs_uses_first_dns_subject_alt_name() -> None:
    client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    with patch.object(
        client.grpc,
        "_decode_certificate",
        return_value={
            "subject": ((("commonName", "cn.example.com"),),),
            "subjectAltName": (("IP Address", "192.0.2.1"), ("DNS", "san.example.com"), ("DNS", "san2.example.com")),
        },
    ):
        assert client.grpc._get_server_certificate_target_name("certificate") == "san.example.com"


def test_cv_client_no_verify_certs_uses_ip_subject_alt_name_without_dns_name() -> None:
    client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    with patch.object(
        client.grpc,
        "_decode_certificate",
        return_value={
            "subject": ((("commonName", "cn.example.com"),),),
            "subjectAltName": (("IP Address", "192.0.2.1"),),
        },
    ):
        assert client.grpc._get_server_certificate_target_name("certificate") == "192.0.2.1"


def test_cv_client_no_verify_certs_falls_back_to_common_name() -> None:
    client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    with patch.object(
        client.grpc,
        "_decode_certificate",
        return_value={
            "subject": ((("countryName", "US"),), (("commonName", "cn.example.com"),)),
        },
    ):
        assert client.grpc._get_server_certificate_target_name("certificate") == "cn.example.com"


def test_cv_client_no_verify_certs_raises_for_certificate_without_identity() -> None:
    client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    with (
        patch.object(client.grpc, "_decode_certificate", return_value={"subject": ((("countryName", "US"),),)}),
        pytest.raises(CVClientException, match="Unable to determine certificate identity"),
    ):
        client.grpc._get_server_certificate_target_name("certificate")


@pytest.mark.asyncio
async def test_cv_client_unauthenticated_proxy() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"

    with patch("pyavd._cv.client.CVClient._init_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
        ) as cvclient:
            assert cvclient.grpc.configuration.proxy == CVGRPCProxyConfiguration(host=proxy_host, port=8080)


def test_cv_client_legacy_proxy_and_channel_proxy_are_mutually_exclusive() -> None:
    with pytest.raises(ValueError, match=r"Cannot set both legacy proxy_\* arguments and grpc_channel_configuration\.proxy"):
        CVClient(
            servers="www.arista.io",
            token="secret_access_token",  # noqa: S106
            proxy_host="legacy-proxy.example.com",
            grpc_channel_configuration=CVGRPCChannelConfiguration(proxy=CVGRPCProxyConfiguration(host="config-proxy.example.com")),
        )


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy proxy tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("targeted_cv"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_PRD_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_PRD_SERVER", default=""),
            },
            id="CVAAS_PRD",
        ),
        pytest.param(
            {
                "cv_access_token": environ.get("CV_STG_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_STG_SERVER", default=""),
            },
            id="CVAAS_STG",
        ),
    ],
)
@pytest.mark.parametrize(
    ("proxy_auth"),
    [
        pytest.param(
            {
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_AUTH_PORT"),
            },
            id="PROXY_AUTH",
        ),
        pytest.param(
            {
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_NO_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_NO_AUTH_PORT"),
            },
            id="PROXY_NO_AUTH",
        ),
    ],
)
@pytest.mark.parametrize(
    ("verify_certs"),
    [
        pytest.param(True, id="VERIFY_CERTS_TRUE"),
        pytest.param(False, id="VERIFY_CERTS_FALSE"),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_with_cvaas_via_proxy(
    targeted_cv: dict[str, str],
    proxy_auth: dict[str, str],
    verify_certs: bool,
) -> None:
    """Test ability to fetch data from CVaaS through HTTP CONNECT proxy server using REST and gRPC."""
    with does_not_raise():
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
            proxy_host=proxy_auth["proxy_host"],
            proxy_port=int(proxy_auth["proxy_port"]),
            proxy_username=proxy_auth["proxy_username"],
            proxy_password=proxy_auth["proxy_password"],
        ) as cvclient_via_proxy:
            result = await cvclient_via_proxy.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []


@pytest.mark.skipif(environ.get("CV_LIVE_TEST") is None, reason="CV_LIVE_TEST env variable is not set. Live cv_deploy proxy tests are skipped.")
@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("targeted_cv"),
    [
        pytest.param(
            {
                "cv_access_token": environ.get("CV_ONPREM_ACCESS_TOKEN", default=""),
                "cv_server": environ.get("CV_ONPREM_SERVER", default=""),
            },
            id="CV_ONPREM",
        ),
    ],
)
@pytest.mark.parametrize(
    ("proxy_auth"),
    [
        pytest.param(
            {
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_AUTH_PORT"),
            },
            id="PROXY_AUTH",
        ),
        pytest.param(
            {
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_NO_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_NO_AUTH_PORT"),
            },
            id="PROXY_NO_AUTH",
        ),
    ],
)
@pytest.mark.parametrize(
    ("verify_certs", "expected_exception"),
    [
        pytest.param(True, pytest.raises(CVClientException, match="SSLCertVerificationError"), id="VERIFY_CERTS_TRUE"),
        pytest.param(False, does_not_raise(), id="VERIFY_CERTS_FALSE"),
    ],
)
@pytest.mark.filterwarnings("ignore:Unverified HTTPS request is being made to host")
async def test_cvclient_with_onprem_via_proxy(
    targeted_cv: dict[str, str], proxy_auth: dict[str, str], verify_certs: bool, expected_exception: ExpectedExceptionContext
) -> None:
    """Test ability to fetch data from on-prem CloudVision through HTTP CONNECT proxy server using REST and gRPC."""
    with expected_exception:
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
            proxy_host=proxy_auth["proxy_host"],
            proxy_port=int(proxy_auth["proxy_port"]),
            proxy_username=proxy_auth["proxy_username"],
            proxy_password=proxy_auth["proxy_password"],
        ) as cvclient_via_proxy:
            result = await cvclient_via_proxy.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []
