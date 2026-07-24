# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ
from unittest.mock import AsyncMock, patch

import pytest

from pyavd._cv.client import CVClient, PreparedCVConnection, ResolvedGRPCTLS
from pyavd._cv.client.exceptions import CVClientException
from pyavd._cv.client.versioning import CvVersion
from pyavd._cv.workflows.models import CloudVision, CVProxyConfiguration, CVTLSConfiguration

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]
PREPARED_CONNECTION = PreparedCVConnection(version=CvVersion("CVaaS"), grpc_tls=ResolvedGRPCTLS())


def _cloudvision(
    *,
    servers: tuple[str, ...] = ("www.arista.io",),
    token: str = "secret_access_token",  # noqa: S107
    tls_configuration: CVTLSConfiguration | None = None,
    proxy_configuration: CVProxyConfiguration | None = None,
) -> CloudVision:
    return CloudVision(
        servers=servers,
        token=token,
        username=None,
        password=None,
        tls_configuration=tls_configuration or CVTLSConfiguration(),
        proxy_configuration=proxy_configuration,
    )


@pytest.mark.asyncio
async def test_cv_client_authenticated_proxy_is_mapped_to_grpc_channel_options() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"
    proxy_username = "avd_user"
    proxy_password = "avd_password"  # noqa: S105

    with (
        patch("pyavd._cv.client.CVClient._prepare_cv_connection", return_value=PREPARED_CONNECTION),
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(
            cloudvision=_cloudvision(
                servers=(servers,),
                token=token,
                proxy_configuration=CVProxyConfiguration(
                    host=proxy_host,
                    username=proxy_username,
                    password=proxy_password,
                ),
            ),
        ) as cvclient:
            assert cvclient.grpc.proxy == CVProxyConfiguration(
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
    prepared_connection = PreparedCVConnection(
        version=CvVersion("CVaaS"),
        grpc_tls=ResolvedGRPCTLS(root_certificates=peer_certificate.encode(), target_name_override="cv.example.com"),
    )

    with (
        patch("pyavd._cv.client.CVClient._prepare_cv_connection", return_value=prepared_connection),
        patch("pyavd._cv.client.grpc.ssl_channel_credentials", return_value="tls-credentials") as mock_ssl_channel_credentials,
        patch("pyavd._cv.client.grpc.access_token_call_credentials", return_value="call-credentials") as mock_access_token_call_credentials,
        patch("pyavd._cv.client.grpc.composite_channel_credentials", return_value="channel-credentials") as mock_composite_channel_credentials,
        patch("pyavd._cv.client.secure_channel") as mock_secure_channel,
    ):
        mock_secure_channel.return_value.close = AsyncMock()
        async with CVClient(cloudvision=_cloudvision(servers=(servers,), token=token, tls_configuration=CVTLSConfiguration(verify_certs=False))):
            pass

    mock_ssl_channel_credentials.assert_called_once_with(root_certificates=peer_certificate.encode())
    mock_access_token_call_credentials.assert_called_once_with(token)
    mock_composite_channel_credentials.assert_called_once_with("tls-credentials", "call-credentials")
    assert mock_secure_channel.call_args.kwargs["credentials"] == "channel-credentials"
    grpc_options = dict(mock_secure_channel.call_args.kwargs["options"])
    assert grpc_options["grpc.ssl_target_name_override"] == "cv.example.com"


def test_cv_client_no_verify_certs_uses_first_dns_subject_alt_name() -> None:
    client = CVClient(cloudvision=_cloudvision())

    with patch.object(
        client._tls,
        "_decode_certificate",
        return_value={
            "subject": ((("commonName", "cn.example.com"),),),
            "subjectAltName": (("IP Address", "192.0.2.1"), ("DNS", "san.example.com"), ("DNS", "san2.example.com")),
        },
    ):
        assert client._tls.grpc_tls_from_unverified_peer_certificate("certificate").target_name_override == "san.example.com"


def test_cv_client_no_verify_certs_uses_ip_subject_alt_name_without_dns_name() -> None:
    client = CVClient(cloudvision=_cloudvision())

    with patch.object(
        client._tls,
        "_decode_certificate",
        return_value={
            "subject": ((("commonName", "cn.example.com"),),),
            "subjectAltName": (("IP Address", "192.0.2.1"),),
        },
    ):
        assert client._tls.grpc_tls_from_unverified_peer_certificate("certificate").target_name_override == "192.0.2.1"


def test_cv_client_no_verify_certs_falls_back_to_common_name() -> None:
    client = CVClient(cloudvision=_cloudvision())

    with patch.object(
        client._tls,
        "_decode_certificate",
        return_value={
            "subject": ((("countryName", "US"),), (("commonName", "cn.example.com"),)),
        },
    ):
        assert client._tls.grpc_tls_from_unverified_peer_certificate("certificate").target_name_override == "cn.example.com"


def test_cv_client_no_verify_certs_raises_for_certificate_without_identity() -> None:
    client = CVClient(cloudvision=_cloudvision())

    with (
        patch.object(client._tls, "_decode_certificate", return_value={"subject": ((("countryName", "US"),),)}),
        pytest.raises(CVClientException, match="Unable to determine certificate identity"),
    ):
        client._tls.grpc_tls_from_unverified_peer_certificate("certificate")


@pytest.mark.asyncio
async def test_cv_client_unauthenticated_proxy() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"

    with patch("pyavd._cv.client.CVClient._prepare_cv_connection", return_value=PREPARED_CONNECTION):
        async with CVClient(
            cloudvision=_cloudvision(servers=(servers,), token=token, proxy_configuration=CVProxyConfiguration(host=proxy_host)),
        ) as cvclient:
            assert cvclient.grpc.proxy == CVProxyConfiguration(host=proxy_host, port=8080)


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
            cloudvision=_cloudvision(
                servers=(targeted_cv["cv_server"],),
                token=targeted_cv["cv_access_token"],
                tls_configuration=CVTLSConfiguration(verify_certs=verify_certs),
                proxy_configuration=CVProxyConfiguration(
                    host=proxy_auth["proxy_host"],
                    port=int(proxy_auth["proxy_port"]),
                    username=proxy_auth["proxy_username"],
                    password=proxy_auth["proxy_password"],
                ),
            ),
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
            cloudvision=_cloudvision(
                servers=(targeted_cv["cv_server"],),
                token=targeted_cv["cv_access_token"],
                tls_configuration=CVTLSConfiguration(verify_certs=verify_certs),
                proxy_configuration=CVProxyConfiguration(
                    host=proxy_auth["proxy_host"],
                    port=int(proxy_auth["proxy_port"]),
                    username=proxy_auth["proxy_username"],
                    password=proxy_auth["proxy_password"],
                ),
            ),
        ) as cvclient_via_proxy:
            result = await cvclient_via_proxy.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []
