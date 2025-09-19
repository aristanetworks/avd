# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from logging import getLogger
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import aristaproto
import pytest
import pytest_asyncio
import requests

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from tests.pyavd.cv.mockery import mocked_cv_client_aenter, playback_unary_stream, playback_unary_unary, recording_unary_stream, recording_unary_unary

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")


ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


@pytest_asyncio.fixture
async def cv_client() -> AsyncGenerator[CVClient, None]:
    """
    Instance of CVClient.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is not set,
    this will return a proper instance of CVClient connected to CloudVision with the token.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is set,
    this will return an instance of CVClient connected to CloudVision with the token where all API calls will be recorded.

    Otherwise this will return an instance of CVClient where API calls are mocked using previously recorded API messages.
    """
    if CV_SERVER and CV_TOKEN:
        LOGGER.info("Running in online mode connecting to %s.", CV_SERVER)
        if RECORDING:
            LOGGER.info("Mocking ServiceStub to RecordingServiceStub")
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = recording_unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = recording_unary_stream
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream

        else:
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

    else:
        LOGGER.info("Mocking ServiceStub to MockedServiceStub")
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
        aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = playback_unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = playback_unary_stream
        with patch("pyavd._cv.client.CVClient.__aenter__", new=mocked_cv_client_aenter):
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

        aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
        return


@pytest.mark.asyncio
async def test_get_inventory_devices(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices()
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_inventory_devices_with_filter(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices([(None, None, "avd-ci-spine1")])
    assert len(result) == 1
    assert hasattr(result[0], "hostname")
    assert result[0].hostname == "avd-ci-spine1"


@pytest.mark.asyncio
async def test_cv_client_proxy_socket_error() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"
    proxy_username = "avd_user"
    proxy_password = "avd_password"  # noqa: S105

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            with pytest.raises(CVClientException) as exception_info:
                await cvclient.get_inventory_devices([(None, None, "spine1")])

            assert "Failed to create proxy connection" in str(exception_info.value)


@pytest.mark.asyncio
async def test_cv_client_no_verify_certs() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(servers=servers, token=token, verify_certs=False) as cvclient:
            ssl_context = cvclient._ssl_context()
            assert ssl_context.check_hostname is False
            assert ssl_context.verify_mode == ssl.CERT_NONE


@pytest.mark.asyncio
async def test_cv_client_unauthenticated_proxy() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
        ) as cvclient:
            assert cvclient._proxy_manager.proxy_url == f"http://{proxy_host}:{cvclient._proxy_manager.proxy_port}"


@pytest.mark.skipif(environ.get("CV_LIVE_PROXY_TEST") is None, reason="CV_LIVE_PROXY_TEST env variable is not set. Live cv_deploy proxy tests are skipped.")
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


@pytest.mark.skipif(environ.get("CV_LIVE_PROXY_TEST") is None, reason="CV_LIVE_PROXY_TEST env variable is not set. Live cv_deploy proxy tests are skipped.")
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
        pytest.param(True, pytest.raises(requests.exceptions.SSLError, match="SSLCertVerificationError"), id="VERIFY_CERTS_TRUE"),
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
