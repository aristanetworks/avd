# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException

from .helpers import form_proxy_string, unset_proxy_related_env_vars

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]

USER: str = "user1"
PASS: str = "pass1"  # noqa: S105
USER_SS: str = "u:s@e/r.1"
PASS_SS: str = "p:a@s/s.1"  # noqa: S105
USER_SS_QUOTED: str = "u%3As%40e%2Fr.1"
PASS_SS_QUOTED: str = "p%3Aa%40s%2Fs.1"  # noqa: S105


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
            result = await cvclient_via_proxy.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
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
            result = await cvclient_via_proxy.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
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
            result = await cvclient_via_proxy.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
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
            result = await cvclient_via_proxy.get_inventory_devices(devices={(None, None, "nonexisting-avd-ci-hostname")})
        assert result == []
