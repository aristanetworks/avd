# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import ssl
import tempfile
from logging import getLogger
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import aristaproto
import grpclib
import pytest
import pytest_asyncio

from pyavd._cv.client import CVClient
from pyavd._cv.client.versioning import CvVersion
from tests.pyavd.cv.mockery import mocked_cv_client_aenter, playback_unary_stream, playback_unary_unary, recording_unary_stream, recording_unary_unary

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")
CUSTOM_CA_CERTIFICATE_CONTENT = """-----BEGIN CERTIFICATE-----
MIIE9jCCA96gAwIBAgISBZgckzW9Me5jRE4ONmcia5XgMA0GCSqGSIb3DQEBCwUA
MDMxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQwwCgYDVQQD
EwNSMTAwHhcNMjUwODA1MDkwNjQ3WhcNMjUxMTAzMDkwNjQ2WjAYMRYwFAYDVQQD
Ew13d3cuYXJpc3RhLmlvMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA
vQadeQIzRhzMrmSZlZeu/aoz5ekpP2hhBgJH9LSEL6l3U91APlyd9GiU9vZJOcbB
t2yZxmpWCKqOAKivQILPPoqobb3LVy8orVtEClxBIfHhE8eo1EbCPPzz+RawQl5M
xN7knsUHv+pQ3rD3IgXTNDTVLBfHWXrXJQdFVMId3P+xE5Ddb8R49cMo4J8Ji3RJ
9OhT2HWK9j2NPRcY8cgdpMlhVVHzhIHVERHBF8MjGPucNzXX9KvuvTNVFbBLIbkl
CRnvs7boh4COpOr2XjKiupfdBFNMj240uyTqKt0pL4g/hrNkJULWKW1jfuFLBwqs
LOh1gnon5CymC5YwTj2UMwIDAQABo4ICHTCCAhkwDgYDVR0PAQH/BAQDAgWgMB0G
A1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAMBgNVHRMBAf8EAjAAMB0GA1Ud
DgQWBBQ4JhhvoR7fStS10HcWmZdWOYnMaTAfBgNVHSMEGDAWgBS7vMNHpeS8qcbD
pHIMEI2iNeHI6DAzBggrBgEFBQcBAQQnMCUwIwYIKwYBBQUHMAKGF2h0dHA6Ly9y
MTAuaS5sZW5jci5vcmcvMBgGA1UdEQQRMA+CDXd3dy5hcmlzdGEuaW8wEwYDVR0g
BAwwCjAIBgZngQwBAgEwLgYDVR0fBCcwJTAjoCGgH4YdaHR0cDovL3IxMC5jLmxl
bmNyLm9yZy85Ny5jcmwwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdgCkQsUGSWBh
VI8P1Oqc+3otJkVNh6l/L99FWfYnTzqEVAAAAZh5sUW5AAAEAwBHMEUCIBgSw6dI
xJmiM2clUYTotGrlD1gCcocICzPKhl1j+eXAAiEAm+oj5J3/Y3HnhpXFWCj20u6a
Hz+iq/rjU9qo/BVCSlMAdgDM+w9qhXEJZf6Vm1PO6bJ8IumFXA2XjbapflTA/kwN
sAAAAZh5sUXDAAAEAwBHMEUCIC+dYRM2P3eHpVIWBG31w/KHdQibl7WM0TglXaFG
XzwRAiEA7+ibWTr54BMbQoRco7RtGHzR0jTUiISR7kaHtMkJtOMwDQYJKoZIhvcN
AQELBQADggEBAHqdybdPGtNzjrTdmVEuT0UZIhQZnnywGVyWAZe7cE9ZSG8HsUSJ
IafNM7DLdyc0X8r2F9ChsTM4wS5w2k4wdA+KNSgxZTam70iaa0H5DcbbeeaIgo8g
WAkcXByKM8Ru82r6EydCUoj8MZhFCvLmeHJRCX0F+qKPMJP8L14pGJjktTMhUk8d
6vYad1GShXpeMjMe/v6bcgP1siykSI54DvP2bPlHsWPFVhiMe8AntQdbNxj31j7R
gSqeEowroTe0FeuyIA+8gPuKg7Yt4EeygGNL7qgObprtkQwTvGM9acP786RVDVSq
e445sY02djeaTMlqYHl4fxrKlRjAhOAda3w=
-----END CERTIFICATE-----"""
OS_CA_CERTIFICATE_CONTENT = """-----BEGIN CERTIFICATE-----
MIIDzTCCA3SgAwIBAgIQArMt1R3JovQOajLMdQ4c4DAKBggqhkjOPQQDAjA7MQsw
CQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYD
VQQDEwNXRTEwHhcNMjUwOTA1MTk1MDA5WhcNMjUxMjA0MjA1MDA0WjAkMSIwIAYD
VQQDExljdi1zdGFnaW5nLmNvcnAuYXJpc3RhLmlvMFkwEwYHKoZIzj0CAQYIKoZI
zj0DAQcDQgAEvKe9q9Yr/umXDAQaeGrWMYdK5DUoV7MWr5FBPgFP1YOA94z7phlL
477ekK3Qkyydh1OHK0RTKr36YE2mRhBIUKOCAm8wggJrMA4GA1UdDwEB/wQEAwIH
gDATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRa
JWXM56i7bK+r+SyIz11XPnT4EzAfBgNVHSMEGDAWgBSQd5I1Z8T/qMyp5nvZgHl7
zJP5ODBeBggrBgEFBQcBAQRSMFAwJwYIKwYBBQUHMAGGG2h0dHA6Ly9vLnBraS5n
b29nL3Mvd2UxL0FyTTAlBggrBgEFBQcwAoYZaHR0cDovL2kucGtpLmdvb2cvd2Ux
LmNydDBBBgNVHREEOjA4ghljdi1zdGFnaW5nLmNvcnAuYXJpc3RhLmlvghsqLmN2
LXN0YWdpbmcuY29ycC5hcmlzdGEuaW8wEwYDVR0gBAwwCjAIBgZngQwBAgEwNgYD
VR0fBC8wLTAroCmgJ4YlaHR0cDovL2MucGtpLmdvb2cvd2UxLzBiMDdsS3lTZ1Uw
LmNybDCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB3ABLxTjS9U3JMhAYZw48/ehP4
57Vih4icbTAFhOvlhiY6AAABmRukzioAAAQDAEgwRgIhANGfQVAHGqTJUqyjBTN5
hvwhrCwLfi+kaUH/f2DSoD3xAiEA+SXRzWW4AefCIu28sFMTXWIg1aBmxYXcKKm6
TaaJ+foAdQDM+w9qhXEJZf6Vm1PO6bJ8IumFXA2XjbapflTA/kwNsAAAAZkbpM6h
AAAEAwBGMEQCIGyp76ip7zB35IPM8MGnuZvvEwZtzkvZL3NTnBgOzPyRAiBGnShH
OxBpDhGdVXBckk4HvZ6UKWjhGhUTPoBeUbFp0jAKBggqhkjOPQQDAgNHADBEAiAF
Gh8pAgr85q5Lo8RtMiQahuvcZ8AGKY8sgA+ieMQJuAIgNT4c9lZvMB+AAQycSeD7
oOPcDSG1DcHKzbEtGwpwa0g=
-----END CERTIFICATE-----"""


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
async def test_cv_client_custom_ca_path() -> None:
    with tempfile.NamedTemporaryFile(delete=True, mode="w", encoding="utf-8") as custom_ca_path_temp_file:
        custom_ca_path_temp_file.write(CUSTOM_CA_CERTIFICATE_CONTENT)
        custom_ca_path_temp_file.flush()
        custom_ca_path_temp_file_path = custom_ca_path_temp_file.name

        with tempfile.NamedTemporaryFile(delete=True, mode="w", encoding="utf-8") as os_ca_path_temp_file:
            os_ca_path_temp_file.write(OS_CA_CERTIFICATE_CONTENT)
            os_ca_path_temp_file.flush()
            os_ca_path_temp_file_path = os_ca_path_temp_file.name

            with (
                patch("certifi.where", return_value=os_ca_path_temp_file_path),
                patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"),
            ):
                servers = "www.arista.io"
                token = "secret_access_token"  # noqa: S105
                proxy_host = "10.10.10.10"
                proxy_username = "avd_user"
                proxy_password = "avd_password"  # noqa: S105

                async with CVClient(
                    servers=servers,
                    token=token,
                    custom_ca_path=custom_ca_path_temp_file_path,
                    proxy_host=proxy_host,
                    proxy_username=proxy_username,
                    proxy_password=proxy_password,
                ) as cvclient:
                    with patch.object(cvclient, "_cv_version", CvVersion(version="CVaaS")):
                        assert cvclient._cv_version.version == "CVaaS"
                        assert cvclient._custom_ca_path == custom_ca_path_temp_file_path
                        assert cvclient._proxy_manager is not None
                        assert cvclient._proxy_manager.proxy_host == "10.10.10.10"
                        assert cvclient._proxy_manager.proxy_port == 8080
                        assert cvclient._proxy_manager.proxy_username == "avd_user"
                        assert cvclient._proxy_manager.proxy_password == "avd_password"  # noqa: S105
                        assert cvclient._proxy_manager.target_host == cvclient._servers[0]
                        assert cvclient._proxy_manager.target_port == 443
                        assert (
                            cvclient._proxy_manager.proxy_url == f"http://{proxy_username}:{proxy_password}@{proxy_host}:{cvclient._proxy_manager.proxy_port}"
                        )
                        assert cvclient._proxy_manager.get_requests_proxies()["http"] == cvclient._proxy_manager.proxy_url
                        assert cvclient._proxy_manager.get_requests_proxies()["https"] == cvclient._proxy_manager.proxy_url
                        # Assert gRPC channel via Proxy
                        assert cvclient._channel._host == cvclient._servers[0]
                        assert cvclient._channel._port == 443
                        assert cvclient._channel._loop.is_running() is True
                        assert cvclient._channel._loop.is_closed() is False
                        assert isinstance(cvclient._channel._ssl, ssl.SSLContext)
                        assert isinstance(cvclient._channel._codec, grpclib.encoding.proto.ProtoCodec)
                        assert cvclient._channel._scheme == "https"
                        assert cvclient._channel._authority == f"{cvclient._servers[0]}:443"
                        assert isinstance(cvclient._channel._connect_lock, asyncio.locks.Lock)
                        # Assert that state is Idle
                        assert cvclient._channel._state == 1
