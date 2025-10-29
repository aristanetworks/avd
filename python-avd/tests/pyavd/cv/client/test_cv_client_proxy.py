# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl
from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ
from unittest.mock import patch

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


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
            assert cvclient._proxy_manager.proxy_url == f"http://{proxy_host}:{cvclient._proxy_manager.port}"


def unset_proxy_related_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unset all proxy-related env variables prior to the start of the tests."""
    for env_var in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY", "no_proxy", "NO_PROXY"]:
        monkeypatch.delenv(env_var, raising=False)


def form_proxy_string(
    proxy_schema: str | None, proxy_username: str | None, proxy_password: str | None, proxy_host: str | None, proxy_port: str | int | None
) -> str:
    if proxy_username and proxy_password:
        return f"{proxy_schema}://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port!s}"  # NOSONAR

    return f"{proxy_schema}://{proxy_host}:{proxy_port!s}"


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
    ("env_variable_name"),
    [
        pytest.param("https_proxy", id="LOWER_HTTPS_PROXY"),
        pytest.param("HTTPS_PROXY", id="UPPER_HTTPS_PROXY"),
        pytest.param("all_proxy", id="LOWER_ALL_PROXY"),
        pytest.param("ALL_PROXY", id="UPPER_ALL_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_auth"),
    [
        pytest.param(
            {
                "proxy_schema": "http",
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_AUTH_PORT"),
            },
            id="PROXY_AUTH",
        ),
        pytest.param(
            {
                "proxy_schema": "http",
                "proxy_username": None,
                "proxy_password": None,
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
async def test_cvclient_with_cvaas_via_proxy_env_vars(
    monkeypatch: pytest.MonkeyPatch,
    targeted_cv: dict[str, str],
    env_variable_name: str,
    proxy_auth: dict[str, str],
    verify_certs: bool,
) -> None:
    """Test ability to fetch data from CVaaS through HTTP CONNECT proxy server (discovered using env vars) using REST and gRPC."""
    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    proxy_string = form_proxy_string(
        proxy_auth["proxy_schema"], proxy_auth["proxy_username"], proxy_auth["proxy_password"], proxy_auth["proxy_host"], proxy_auth["proxy_port"]
    )
    monkeypatch.setenv(env_variable_name, proxy_string)

    with does_not_raise():
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
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
    ("env_variable_name"),
    [
        pytest.param("https_proxy", id="LOWER_HTTPS_PROXY"),
        pytest.param("HTTPS_PROXY", id="UPPER_HTTPS_PROXY"),
        pytest.param("all_proxy", id="LOWER_ALL_PROXY"),
        pytest.param("ALL_PROXY", id="UPPER_ALL_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_auth"),
    [
        pytest.param(
            {
                "proxy_schema": "http",
                "proxy_username": environ.get("CV_PROXY_USERNAME"),
                "proxy_password": environ.get("CV_PROXY_PASSWORD"),
                "proxy_host": environ.get("CV_PROXY_AUTH_HOST"),
                "proxy_port": environ.get("CV_PROXY_AUTH_PORT"),
            },
            id="PROXY_AUTH",
        ),
        pytest.param(
            {
                "proxy_schema": "http",
                "proxy_username": None,
                "proxy_password": None,
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
async def test_cvclient_with_onprem_via_proxy_env_vars(
    monkeypatch: pytest.MonkeyPatch,
    targeted_cv: dict[str, str],
    env_variable_name: str,
    proxy_auth: dict[str, str],
    verify_certs: bool,
    expected_exception: ExpectedExceptionContext,
) -> None:
    """Test ability to fetch data from on-prem CloudVision through HTTP CONNECT proxy server (discovered using env vars) using REST and gRPC."""
    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    proxy_string = form_proxy_string(
        proxy_auth["proxy_schema"], proxy_auth["proxy_username"], proxy_auth["proxy_password"], proxy_auth["proxy_host"], proxy_auth["proxy_port"]
    )
    monkeypatch.setenv(env_variable_name, proxy_string)

    with expected_exception:
        async with CVClient(
            servers=targeted_cv["cv_server"],
            token=targeted_cv["cv_access_token"],
            verify_certs=verify_certs,
        ) as cvclient_via_proxy:
            result = await cvclient_via_proxy.get_inventory_devices(devices=[(None, None, "nonexisting-avd-ci-hostname")])
        assert result == []


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("https_proxy"),
    [
        pytest.param(None, id="LOWER_HTTPS_SERVER_NONE"),
        pytest.param("http://127.0.0.1", id="LOWER_HTTPS_SERVER_MATCHING"),
        pytest.param("http://127.0.0.2", id="LOWER_HTTPS_SERVER_NONMATCHING"),
        pytest.param("http://new_user:new_password@127.0.0.2:8090", id="LOWER_HTTPS_SERVER_NONMATCHING_FULL"),
    ],
)
@pytest.mark.parametrize(
    ("HTTPS_PROXY"),
    [
        pytest.param(None, id="UPPER_HTTPS_SERVER_NONE"),
        pytest.param("http://127.0.0.1", id="UPPER_HTTPS_SERVER_MATCHING"),
        pytest.param("http://127.0.0.2", id="UPPER_HTTPS_SERVER_NONMATCHING"),
        pytest.param("http://new_user:new_password@127.0.0.2:8090", id="UPPER_HTTPS_SERVER_NONMATCHING_FULL"),
    ],
)
@pytest.mark.parametrize(
    ("all_proxy"),
    [
        pytest.param(None, id="LOWER_ALL_PROXY_NONE"),
        pytest.param("http://127.0.0.1", id="LOWER_ALL_PROXY_MATCHING"),
        pytest.param("http://127.0.0.2", id="LOWER_ALL_PROXY_NONMATCHING"),
        pytest.param("http://new_user:new_password@127.0.0.2:8090", id="LOWER_ALL_PROXY_NONMATCHING_FULL"),
    ],
)
@pytest.mark.parametrize(
    ("ALL_PROXY"),
    [
        pytest.param(None, id="UPPER_ALL_PROXY_NONE"),
        pytest.param("http://127.0.0.1", id="UPPER_ALL_PROXY_MATCHING"),
        pytest.param("http://127.0.0.2", id="UPPER_ALL_PROXY_NONMATCHING"),
        pytest.param("http://new_user:new_password@127.0.0.2:8090", id="UPPER_ALL_PROXY_NONMATCHING_FULL"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy"),
    [
        pytest.param(None, id="LOWER_NO_PROXY_NONE"),
        pytest.param("www.arista.io", id="LOWER_NO_PROXY_MATCHING"),
        pytest.param("www.arista.com", id="LOWER_NO_PROXY_NONMATCHING"),
    ],
)
@pytest.mark.parametrize(
    ("NO_PROXY"),
    [
        pytest.param(None, id="UPPER_NO_PROXY_NONE"),
        pytest.param("www.arista.io", id="UPPER_NO_PROXY_MATCHING"),
        pytest.param("www.arista.com", id="UPPER_NO_PROXY_NONMATCHING"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_username"),
    [
        pytest.param(None, id="PROXY_USERNAME_NONE"),
        pytest.param("avd_user", id="PROXY_USERNAME_SET"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_password"),
    [
        pytest.param(None, id="PROXY_PASSWORD_NONE"),
        pytest.param("avd_password", id="PROXY_PASSWORD_SET"),
    ],
)
async def test_cv_client_proxy_settings_explicit(
    monkeypatch: pytest.MonkeyPatch,
    https_proxy: str | None,
    HTTPS_PROXY: str | None,  # noqa: N803
    all_proxy: str | None,
    ALL_PROXY: str | None,  # noqa: N803
    no_proxy: str | None,
    NO_PROXY: str | None,  # noqa: N803
    proxy_username: str | None,
    proxy_password: str | None,
) -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy-related ENV Variables based on the pytest parametrize inputs
    if https_proxy is not None:
        monkeypatch.setenv("https_proxy", https_proxy)
    if HTTPS_PROXY is not None:
        monkeypatch.setenv("HTTPS_PROXY", HTTPS_PROXY)
    if all_proxy is not None:
        monkeypatch.setenv("all_proxy", all_proxy)
    if ALL_PROXY is not None:
        monkeypatch.setenv("ALL_PROXY", ALL_PROXY)
    if no_proxy is not None:
        monkeypatch.setenv("no_proxy", no_proxy)
    if NO_PROXY is not None:
        monkeypatch.setenv("NO_PROXY", NO_PROXY)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            pass

    assert cvclient._proxy_manager.use_proxy
    assert cvclient._proxy_manager.scheme == "http"
    assert cvclient._proxy_manager.host == proxy_host
    assert cvclient._proxy_manager.port == 8080
    assert cvclient._proxy_manager.username == proxy_username
    assert cvclient._proxy_manager.password == proxy_password
    assert cvclient._proxy_manager.target_host == servers
    assert cvclient._proxy_manager.target_port == 443


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"),
    [
        pytest.param(
            "http://new_user1:new_password1@127.0.0.1:8081",
            "http://new_user2:new_password2@127.0.0.2:8082",
            None,
            None,
            id="LOWER_HTTPS_SERVER_WINS",
        ),
        pytest.param(
            None,
            "http://new_user1:new_password1@127.0.0.1:8081",
            "http://new_user2:new_password2@127.0.0.2:8082",
            None,
            id="UPPER_HTTPS_SERVER_WINS",
        ),
        pytest.param(
            None,
            None,
            "http://new_user1:new_password1@127.0.0.1:8081",
            "http://new_user2:new_password2@127.0.0.2:8082",
            id="LOWER_ALL_PROXY_WINS",
        ),
        pytest.param(
            None,
            None,
            None,
            "http://new_user1:new_password1@127.0.0.1:8081",
            id="UPPER_ALL_PROXY_WINS",
        ),
    ],
)
@pytest.mark.parametrize(
    ("proxy_username"),
    [
        pytest.param(None, id="PROXY_USERNAME_NONE"),
        pytest.param("avd_user", id="PROXY_USERNAME_SET"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_password"),
    [
        pytest.param(None, id="PROXY_PASSWORD_NONE"),
        pytest.param("avd_password", id="PROXY_PASSWORD_SET"),
    ],
)
async def test_cv_client_proxy_settings_env_vars(
    monkeypatch: pytest.MonkeyPatch,
    https_proxy: str | None,
    HTTPS_PROXY: str | None,  # noqa: N803
    all_proxy: str | None,
    ALL_PROXY: str | None,  # noqa: N803
    proxy_username: str | None,
    proxy_password: str | None,
) -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy-related ENV Variables based on the pytest parametrize inputs
    if https_proxy is not None:
        monkeypatch.setenv("https_proxy", https_proxy)
    if HTTPS_PROXY is not None:
        monkeypatch.setenv("HTTPS_PROXY", HTTPS_PROXY)
    if all_proxy is not None:
        monkeypatch.setenv("all_proxy", all_proxy)
    if ALL_PROXY is not None:
        monkeypatch.setenv("ALL_PROXY", ALL_PROXY)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            pass

    assert cvclient._proxy_manager.use_proxy
    assert cvclient._proxy_manager.scheme == "http"
    assert cvclient._proxy_manager.host == "127.0.0.1"
    assert cvclient._proxy_manager.port == 8081
    assert cvclient._proxy_manager.username == "new_user1"
    assert cvclient._proxy_manager.password == "new_password1"  # noqa: S105
    assert cvclient._proxy_manager.target_host == servers
    assert cvclient._proxy_manager.target_port == 443


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("env_variable_name", "env_variable_value"),
    [
        pytest.param("https_proxy", "http://new_user1:new_password1@127.0.0.1:8081", id="LOWER_HTTPS_PROXY"),
        pytest.param("HTTPS_PROXY", "http://new_user1:new_password1@127.0.0.1:8081", id="UPPER_HTTPS_PROXY"),
        pytest.param("all_proxy", "http://new_user1:new_password1@127.0.0.1:8081", id="LOWER_ALL_PROXY"),
        pytest.param("ALL_PROXY", "http://new_user1:new_password1@127.0.0.1:8081", id="UPPER_ALL_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy_env_variable_name", "no_proxy_env_variable_value"),
    [
        pytest.param("no_proxy", "www.arista.io", id="LOWER_NO_PROXY_1"),
        pytest.param("no_proxy", "www.arista.io,www.arista.com", id="LOWER_NO_PROXY_2"),
        pytest.param("no_proxy", "www.arista.io:443", id="LOWER_NO_PROXY_3"),
        pytest.param("no_proxy", "www.arista.io:443,www.arista.com:443", id="LOWER_NO_PROXY_4"),
        pytest.param("NO_PROXY", "www.arista.io", id="UPPER_NO_PROXY_1"),
        pytest.param("NO_PROXY", "www.arista.io,www.arista.com", id="UPPER_NO_PROXY_2"),
        pytest.param("NO_PROXY", "www.arista.io:443", id="UPPER_NO_PROXY_3"),
        pytest.param("NO_PROXY", "www.arista.io:443,www.arista.com:443", id="UPPER_NO_PROXY_4"),
    ],
)
async def test_cv_client_proxy_settings_no_proxy_override(
    monkeypatch: pytest.MonkeyPatch,
    env_variable_name: str | None,
    env_variable_value: str | None,
    no_proxy_env_variable_name: str | None,
    no_proxy_env_variable_value: str | None,
) -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy-related ENV Variables based on the pytest parametrize inputs
    if env_variable_value is not None:
        monkeypatch.setenv(env_variable_name, env_variable_value)
    if no_proxy_env_variable_value is not None:
        monkeypatch.setenv(no_proxy_env_variable_name, no_proxy_env_variable_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
        ) as cvclient:
            pass

    assert not cvclient._proxy_manager.use_proxy
