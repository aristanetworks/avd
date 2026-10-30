# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ
from typing import Any
from unittest.mock import patch

import pytest
from requests import Request, Session
from requests.adapters import HTTPAdapter

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]
PROXY_ENV_VARS = ("http_proxy", "HTTP_PROXY", "https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY", "no_proxy", "NO_PROXY")
CVP_CLUSTER_SERVERS = ["cvp.cluster.local", "cvp1a.cluster.local", "cvp1b.cluster.local", "cvp1c.cluster.local"]
PROXY_ENV_SETTINGS = (
    pytest.param("http_proxy", "http://http-connect-proxy.local:3128", id="HTTP_PROXY_LOWER"),
    pytest.param("HTTP_PROXY", "http://http-connect-proxy.local:3128", id="HTTP_PROXY_UPPER"),
    pytest.param("https_proxy", "http://http-connect-proxy.local:3128", id="HTTPS_PROXY_LOWER"),
    pytest.param("HTTPS_PROXY", "http://http-connect-proxy.local:3128", id="HTTPS_PROXY_UPPER"),
    pytest.param("all_proxy", "http://http-connect-proxy.local:3128", id="ALL_PROXY_LOWER"),
    pytest.param("ALL_PROXY", "http://http-connect-proxy.local:3128", id="ALL_PROXY_UPPER"),
)
NO_PROXY_ENV_SETTINGS = (
    pytest.param("no_proxy", "www.arista.io", id="NO_PROXY_LOWER_MATCHING"),
    pytest.param("no_proxy", "www.arista.com", id="NO_PROXY_LOWER_NONMATCHING"),
    pytest.param("NO_PROXY", "www.arista.io", id="NO_PROXY_UPPER_MATCHING"),
    pytest.param("NO_PROXY", "www.arista.com", id="NO_PROXY_UPPER_NONMATCHING"),
)


def _unset_proxy_environment_variables(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unsets all proxy-related environment variables prior to the start of the proxy tests."""
    for env_var in PROXY_ENV_VARS:
        monkeypatch.delenv(env_var, raising=False)


def _set_proxy_environment_variable(monkeypatch: pytest.MonkeyPatch, env_var: str, value: str) -> None:
    """Set one proxy environment variable to the value under test."""
    monkeypatch.setenv(env_var, value)


def _get_proxy_managers(url: str, proxies: dict[str, str], verify: bool | str) -> dict[str, Any]:
    """Return proxy manager selected without a connection across supported Requests versions."""
    adapter = HTTPAdapter()
    # Requests added get_connection_with_tls_context in 2.32.2.
    if hasattr(adapter, "get_connection_with_tls_context"):
        adapter.get_connection_with_tls_context(Request("GET", url).prepare(), verify=verify, proxies=proxies)
    else:
        adapter.get_connection(url, proxies=proxies)
    return adapter.proxy_manager


@pytest.mark.parametrize(("env_var", "value"), PROXY_ENV_SETTINGS + NO_PROXY_ENV_SETTINGS)
def test_cv_client_ignores_proxy_environment_variables(env_var: str, value: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that REST calls connect directly when no proxy was explicitly configured."""
    _unset_proxy_environment_variables(monkeypatch)
    _set_proxy_environment_variable(monkeypatch, env_var, value)
    cv_client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    with patch("requests.utils.getproxies") as getproxies:
        settings = Session().merge_environment_settings("https://www.arista.io", cv_client._requests_proxies, None, cv_client._tls.requests_verify, None)

    getproxies.assert_not_called()
    proxies = settings["proxies"]
    assert proxies == {
        "http": "",
        "https": "",
        "all": "",
        "no_proxy": "www.arista.io",
    }
    assert _get_proxy_managers("https://www.arista.io", proxies, cv_client._tls.requests_verify) == {}


@pytest.mark.parametrize("cv_server", CVP_CLUSTER_SERVERS)
def test_cv_client_ignores_proxy_environment_variables_for_all_cluster_servers(cv_server: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that every configured CloudVision server bypasses proxy environment lookup."""
    _unset_proxy_environment_variables(monkeypatch)
    _set_proxy_environment_variable(monkeypatch, "https_proxy", "http://http-connect-proxy.local:3128")
    cv_client = CVClient(servers=CVP_CLUSTER_SERVERS, token="secret_access_token")  # noqa: S106

    with patch("requests.utils.getproxies") as getproxies:
        settings = Session().merge_environment_settings(f"https://{cv_server}", cv_client._requests_proxies, None, cv_client._tls.requests_verify, None)

    getproxies.assert_not_called()
    proxies = settings["proxies"]
    assert proxies == {
        "http": "",
        "https": "",
        "all": "",
        "no_proxy": ",".join(CVP_CLUSTER_SERVERS),
    }
    assert _get_proxy_managers(f"https://{cv_server}", proxies, cv_client._tls.requests_verify) == {}


@pytest.mark.parametrize(("env_var", "value"), PROXY_ENV_SETTINGS + NO_PROXY_ENV_SETTINGS)
def test_cv_client_explicit_proxy_overrides_proxy_environment_variables(env_var: str, value: str, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test that REST calls use the explicitly configured proxy."""
    _unset_proxy_environment_variables(monkeypatch)
    _set_proxy_environment_variable(monkeypatch, env_var, value)
    cv_client = CVClient(servers="www.arista.io", token="secret_access_token", proxy_host="user-proxy.local")  # noqa: S106

    settings = Session().merge_environment_settings("https://www.arista.io", cv_client._requests_proxies, None, cv_client._tls.requests_verify, None)
    proxies = settings["proxies"]

    # Requests may retain ambient "all" and "no" entries. Proxy selection considers the scheme before "all" and never considers "no"
    assert {key: proxies[key] for key in ("http", "https")} == {
        "http": "http://user-proxy.local:8080",
        "https": "http://user-proxy.local:8080",
    }
    assert set(_get_proxy_managers("https://www.arista.io", proxies, cv_client._tls.requests_verify)) == {"http://user-proxy.local:8080"}


@pytest.mark.parametrize(("env_var", "value"), PROXY_ENV_SETTINGS)
def test_cv_client_without_explicit_proxy_ignores_environment_proxy_when_following_http_redirect(
    env_var: str, value: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test that an HTTP redirect does not use an environment proxy without explicit proxy configuration."""
    _unset_proxy_environment_variables(monkeypatch)
    _set_proxy_environment_variable(monkeypatch, env_var, value)
    cv_client = CVClient(servers="www.arista.io", token="secret_access_token")  # noqa: S106

    redirect_url = "https://www.arista.com"
    redirect_request = Request("GET", redirect_url).prepare()
    proxies = Session().rebuild_proxies(redirect_request, cv_client._requests_proxies)

    assert proxies == {
        "http": "",
        "https": "",
        "all": "",
        "no_proxy": "www.arista.io",
    }
    assert _get_proxy_managers(redirect_url, proxies, cv_client._tls.requests_verify) == {}


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
            ssl_context = cvclient._tls.grpc_ssl
            assert ssl_context.check_hostname is False
            assert ssl_context.verify_mode == ssl.CERT_NONE
            assert cvclient._tls.requests_verify is False


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
