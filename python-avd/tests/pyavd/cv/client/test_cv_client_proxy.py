# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise
from os import environ
from unittest.mock import patch

import pytest

from pyavd._cv.client import CVClient
from pyavd._cv.client.exceptions import CVClientException
from pyavd._errors import AristaAvdInvalidInputsError

ExpectedExceptionContext = AbstractContextManager[pytest.ExceptionInfo | None]


USER: str = "user1"
PASS: str = "pass1"  # noqa: S105
USER_SS: str = "u:s@e/r.1"
PASS_SS: str = "p:a@s/s.1"  # noqa: S105
USER_SS_QUOTED: str = "u%3As%40e%2Fr.1"
PASS_SS_QUOTED: str = "p%3Aa%40s%2Fs.1"  # noqa: S105


######################
## Helper functions ##
######################
def unset_proxy_related_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """Unsets all proxy-related environment variables prior to the start of the proxy tests."""
    for env_var in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY", "no_proxy", "NO_PROXY"]:
        monkeypatch.delenv(env_var, raising=False)


def form_proxy_string(
    proxy_schema: str | None, proxy_username: str | None, proxy_password: str | None, proxy_host: str | None, proxy_port: str | int | None
) -> str:
    """Forms proxy server URL based on the input variables."""
    if proxy_username and proxy_password:
        return f"{proxy_schema}://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port!s}"  # NOSONAR

    return f"{proxy_schema}://{proxy_host}:{proxy_port!s}"


#########################
## Offline proxy tests ##
#########################
@pytest.mark.asyncio
async def test_cv_client_proxy_socket_error() -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "127.0.0.1"

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
        ) as cvclient:
            with pytest.raises(CVClientException) as exception_info:
                await cvclient.get_inventory_devices({(None, None, "spine1")})

            assert "Failed to create proxy connection" in str(exception_info.value)


@pytest.mark.parametrize(
    ("proxy_related_attribute"),
    [
        pytest.param("use_proxy", id="USE_PROXY"),
        pytest.param("_requests_proxies", id="_REQUESTS_PROXIES"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_requested"),
    [
        pytest.param(True, id="PROXY"),
        pytest.param(False, id="NO_PROXY"),
    ],
)
def test_cv_client_proxy_early_access(proxy_related_attribute: str, proxy_requested: bool) -> None:
    """Test ability to safely access proxy-related properties of the CVClient instance at any time."""
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105
    proxy_host = "proxy1.domain.local"

    if proxy_requested:
        cv_client = CVClient(servers=servers, token=token, proxy_host=proxy_host)
    else:
        cv_client = CVClient(servers=servers, token=token)
    
    _ = getattr(cv_client, proxy_related_attribute)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("proxy_host", "proxy_username", "proxy_password", "expected_proxy_url"),
    [
        pytest.param(None, None, None, "", id="NOTHING"),
        pytest.param(None, None, PASS, "", id="PASS"),
        pytest.param(None, None, PASS_SS, "", id="PASS_SS"),
        pytest.param(None, USER, None, "", id="USER"),
        pytest.param(None, USER_SS, None, "", id="USER_SS"),
        pytest.param(None, USER, PASS, "", id="USER_PASS"),
        pytest.param(None, USER_SS, PASS_SS, "", id="USER_SS_PASS_SS"),
        pytest.param("10.10.10.10", None, None, "http://10.10.10.10:8080", id="IPV4"),
        pytest.param("10.10.10.10", None, PASS, "http://10.10.10.10:8080", id="IPV4_PASS"),
        pytest.param("10.10.10.10", None, PASS_SS, "http://10.10.10.10:8080", id="IPV4_PASS_SS"),
        pytest.param("10.10.10.10", USER, None, "http://10.10.10.10:8080", id="IPV4_USER"),
        pytest.param("10.10.10.10", USER_SS, None, "http://10.10.10.10:8080", id="IPV4_USER_SS"),
        pytest.param("10.10.10.10", USER, PASS, f"http://{USER}:{PASS}@10.10.10.10:8080", id="IPV4_USER_PASS"),
        pytest.param("10.10.10.10", USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@10.10.10.10:8080", id="IPV4_USER_SS_PASS_SS"),
        pytest.param("2002::20", None, None, "http://[2002::20]:8080", id="IPV6"),
        pytest.param("2002::20", None, PASS, "http://[2002::20]:8080", id="IPV6_PASS"),
        pytest.param("2002::20", None, PASS_SS, "http://[2002::20]:8080", id="IPV6_PASS_SS"),
        pytest.param("2002::20", USER, None, "http://[2002::20]:8080", id="IPV6_USER"),
        pytest.param("2002::20", USER_SS, None, "http://[2002::20]:8080", id="IPV6_USER_SS"),
        pytest.param("2002::20", USER, PASS, f"http://{USER}:{PASS}@[2002::20]:8080", id="IPV6_USER_PASS"),
        pytest.param("2002::20", USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@[2002::20]:8080", id="IPV6_USER_SS_PASS_SS"),
        pytest.param("proxy1", None, None, "http://proxy1:8080", id="NAME"),
        pytest.param("proxy1", None, PASS, "http://proxy1:8080", id="NAME_PASS"),
        pytest.param("proxy1", None, PASS_SS, "http://proxy1:8080", id="NAME_PASS_SS"),
        pytest.param("proxy1", USER, None, "http://proxy1:8080", id="NAME_USER"),
        pytest.param("proxy1", USER_SS, None, "http://proxy1:8080", id="NAME_USER_SS"),
        pytest.param("proxy1", USER, PASS, f"http://{USER}:{PASS}@proxy1:8080", id="NAME_USER_PASS"),
        pytest.param("proxy1", USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:8080", id="NAME_USER_SS_PASS_SS"),
        pytest.param("proxy1.local.domain", None, None, "http://proxy1.local.domain:8080", id="FQDN"),
        pytest.param("proxy1.local.domain", None, PASS, "http://proxy1.local.domain:8080", id="FQDN_PASS"),
        pytest.param("proxy1.local.domain", None, PASS_SS, "http://proxy1.local.domain:8080", id="FQDN_PASS_SS"),
        pytest.param("proxy1.local.domain", USER, None, "http://proxy1.local.domain:8080", id="FQDN_USER"),
        pytest.param("proxy1.local.domain", USER_SS, None, "http://proxy1.local.domain:8080", id="FQDN_USER_SS"),
        pytest.param("proxy1.local.domain", USER, PASS, f"http://{USER}:{PASS}@proxy1.local.domain:8080", id="FQDN_USER_PASS"),
        pytest.param("proxy1.local.domain", USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1.local.domain:8080", id="FQDN_USER_PASS"),
    ],
)
async def test_cv_client_proxy_explicit(proxy_host: str | None, proxy_username: str | None, proxy_password: str | None, expected_proxy_url: str) -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            assert cvclient.cv_connection_manager.cv_proxy_manager.get_proxy_url() == expected_proxy_url


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("proxy_host", "proxy_port", "proxy_username", "proxy_password", "expected_proxy_url"),
    [
        pytest.param(None, 3128, None, None, "", id="NOTHING"),
        pytest.param(None, 3128, None, PASS, "", id="PASS"),
        pytest.param(None, 3128, None, PASS_SS, "", id="PASS_SS"),
        pytest.param(None, 3128, USER, None, "", id="USER"),
        pytest.param(None, 3128, USER_SS, None, "", id="USER_SS"),
        pytest.param(None, 3128, USER, PASS, "", id="USER_PASS"),
        pytest.param(None, 3128, USER_SS, PASS_SS, "", id="USER_SS_PASS_SS"),
        pytest.param("10.10.10.10", 3128, None, None, "http://10.10.10.10:3128", id="IPV4"),
        pytest.param("10.10.10.10", 3128, None, PASS, "http://10.10.10.10:3128", id="IPV4_PASS"),
        pytest.param("10.10.10.10", 3128, None, PASS_SS, "http://10.10.10.10:3128", id="IPV4_PASS_SS"),
        pytest.param("10.10.10.10", 3128, USER, None, "http://10.10.10.10:3128", id="IPV4_USER"),
        pytest.param("10.10.10.10", 3128, USER_SS, None, "http://10.10.10.10:3128", id="IPV4_USER_SS"),
        pytest.param("10.10.10.10", 3128, USER, PASS, f"http://{USER}:{PASS}@10.10.10.10:3128", id="IPV4_USER_PASS"),
        pytest.param("10.10.10.10", 8080, USER, PASS, f"http://{USER}:{PASS}@10.10.10.10:8080", id="IPV4_DEFPORT_USER_PASS"),
        pytest.param("10.10.10.10", 3128, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@10.10.10.10:3128", id="IPV4_USER_SS_PASS_SS"),
        pytest.param("10.10.10.10", 8080, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@10.10.10.10:8080", id="IPV4_DEFPORT_USER_SS_PASS_SS"),
        pytest.param("2002::20", 3128, None, None, "http://[2002::20]:3128", id="IPV6"),
        pytest.param("2002::20", 3128, None, PASS, "http://[2002::20]:3128", id="IPV6_PASS"),
        pytest.param("2002::20", 3128, None, PASS_SS, "http://[2002::20]:3128", id="IPV6_PASS_SS"),
        pytest.param("2002::20", 3128, USER, None, "http://[2002::20]:3128", id="IPV6_USER"),
        pytest.param("2002::20", 3128, USER_SS, None, "http://[2002::20]:3128", id="IPV6_USER_SS"),
        pytest.param("2002::20", 3128, USER, PASS, f"http://{USER}:{PASS}@[2002::20]:3128", id="IPV6_USER_PASS"),
        pytest.param("2002::20", 8080, USER, PASS, f"http://{USER}:{PASS}@[2002::20]:8080", id="IPV6_DEFPORT_USER_PASS"),
        pytest.param("2002::20", 3128, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@[2002::20]:3128", id="IPV6_USER_SS_PASS_SS"),
        pytest.param("2002::20", 8080, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@[2002::20]:8080", id="IPV6_DEFPORT_USER_SS_PASS_SS"),
        pytest.param("proxy1", 3128, None, None, "http://proxy1:3128", id="NAME"),
        pytest.param("proxy1", 3128, None, PASS, "http://proxy1:3128", id="NAME_PASS"),
        pytest.param("proxy1", 3128, None, PASS_SS, "http://proxy1:3128", id="NAME_PASS_SS"),
        pytest.param("proxy1", 3128, USER, None, "http://proxy1:3128", id="NAME_USER"),
        pytest.param("proxy1", 3128, USER_SS, None, "http://proxy1:3128", id="NAME_USER_SS"),
        pytest.param("proxy1", 3128, USER, PASS, f"http://{USER}:{PASS}@proxy1:3128", id="NAME_USER_PASS"),
        pytest.param("proxy1", 8080, USER, PASS, f"http://{USER}:{PASS}@proxy1:8080", id="NAME_DEFPORT_USER_PASS"),
        pytest.param("proxy1", 3128, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:3128", id="NAME_USER_SS_PASS_SS"),
        pytest.param("proxy1", 8080, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:8080", id="NAME_DEFPORT_USER_SS_PASS_SS"),
        pytest.param("proxy1.local.domain", 3128, None, None, "http://proxy1.local.domain:3128", id="FQDN"),
        pytest.param("proxy1.local.domain", 3128, None, PASS, "http://proxy1.local.domain:3128", id="FQDN_PASS"),
        pytest.param("proxy1.local.domain", 3128, None, PASS_SS, "http://proxy1.local.domain:3128", id="FQDN_PASS_SS"),
        pytest.param("proxy1.local.domain", 3128, USER, None, "http://proxy1.local.domain:3128", id="FQDN_USER"),
        pytest.param("proxy1.local.domain", 3128, USER_SS, None, "http://proxy1.local.domain:3128", id="FQDN_USER_SS"),
        pytest.param("proxy1.local.domain", 3128, USER_SS, None, "http://proxy1.local.domain:3128", id="FQDN_DEFPORT_USER_SS"),
        pytest.param("proxy1.local.domain", 3128, USER, PASS, f"http://{USER}:{PASS}@proxy1.local.domain:3128", id="FQDN_USER_PASS"),
        pytest.param("proxy1.local.domain", 8080, USER, PASS, f"http://{USER}:{PASS}@proxy1.local.domain:8080", id="FQDN_DEFPORT_USER_PASS"),
        pytest.param(
            "proxy1.local.domain", 3128, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1.local.domain:3128", id="FQDNHOST_USER_PASS"
        ),
        pytest.param(
            "proxy1.local.domain", 8080, USER_SS, PASS_SS, f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1.local.domain:8080", id="FQDNHOST_DEFPORT_USER_PASS"
        ),
    ],
)
async def test_cv_client_proxy_explicit_with_port(
    proxy_host: str | None, proxy_port: int, proxy_username: str | None, proxy_password: str | None, expected_proxy_url: str
) -> None:
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            assert cvclient.cv_connection_manager.cv_proxy_manager.get_proxy_url() == expected_proxy_url


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("servers"),
    [
        pytest.param("www.arista.io", id="FQDN"),
        pytest.param("192.168.10.10", id="IPV4"),
        pytest.param("2001::10", id="IPV6"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_env_var_value"),
    [
        pytest.param(None, id="PROXY_NONE"),
        pytest.param("http://10.10.10.10", id="PROXY_MATCHING"),
        pytest.param("http://11.11.11.11", id="PROXY_NONMATCHING"),
        pytest.param("http://11.11.11.11:8090", id="PROXY_NONMATCHING_WITH_PORT"),
        pytest.param("http://new_user:new_password@11.11.11.11:8090", id="PROXY_NONMATCHING_FULL"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy_env_var_value"),
    [
        pytest.param(None, id="NO_PROXY_NONE"),
        pytest.param("www.arista.io", id="NO_PROXY_MATCHING"),
        pytest.param("www.arista.io:443", id="NO_PROXY_MATCHING_WITH_PORT"),
        pytest.param(".arista.io", id="NO_PROXY_WILDCARD_DOMAIN"),
        pytest.param("*", id="NO_PROXY_STAR"),
        pytest.param("192.168.10.10", id="NO_PROXY_IPV4"),
        pytest.param("192.168.10.10/32", id="NO_PROXY_IPV4_CIDR_32"),
        pytest.param("192.168.10.0/24", id="NO_PROXY_IPV4_CIDR_24"),
        pytest.param("2001::10", id="NO_PROXY_IPV6"),
        pytest.param("2001::10/128", id="NO_PROXY_IPV6_CIDR_128"),
        pytest.param("2001::/64", id="NO_PROXY_IPV6_CIDR_64"),
        pytest.param("www.arista.com", id="NO_PROXY_NONMATCHING"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_username"),
    [
        pytest.param(None, id="PROXY_USERNAME_NONE"),
        pytest.param(USER, id="PROXY_USERNAME_SET"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_password"),
    [
        pytest.param(None, id="PROXY_PASSWORD_NONE"),
        pytest.param(PASS, id="PROXY_PASSWORD_SET"),
    ],
)
async def test_cv_client_proxy_explicit_override(
    monkeypatch: pytest.MonkeyPatch,
    servers: str,
    proxy_env_var_value: str | None,
    no_proxy_env_var_value: str | None,
    proxy_username: str | None,
    proxy_password: str | None,
) -> None:
    """Test ability of explicitly-passed (to `cv_deploy`) proxy settings to override any proxy-related environment variables."""
    token = "secret_access_token"  # noqa: S105
    proxy_host = "10.10.10.10"

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    if proxy_env_var_value is not None:
        for proxy_env_var_name in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]:
            monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    # Set proxy bypass ENV Variables based on the pytest parametrize inputs
    if no_proxy_env_var_value is not None:
        for no_proxy_env_var_name in ["no_proxy", "NO_PROXY"]:
            monkeypatch.setenv(no_proxy_env_var_name, no_proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
            proxy_host=proxy_host,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        ) as cvclient:
            pass

    assert cvclient.cv_connection_manager.cv_proxy_manager.use_proxy
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_scheme == "http"
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_host == proxy_host
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_port == 8080
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_username == proxy_username
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_password == proxy_password
    assert cvclient.cv_connection_manager.cv_proxy_manager._target_host == servers
    assert cvclient.cv_connection_manager.cv_proxy_manager._target_port == 443


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("proxy_env_var_name"),
    [
        pytest.param("https_proxy", id="LOWER_HTTPS_PROXY"),
        pytest.param("HTTPS_PROXY", id="UPPER_HTTPS_PROXY"),
        pytest.param("all_proxy", id="LOWER_ALL_PROXY"),
        pytest.param("ALL_PROXY", id="UPPER_ALL_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_env_var_value"),
    [
        pytest.param("http://proxy1:8090", id="PROXY_NAME_PORT"),
        pytest.param(f"http://{USER}:{PASS}@proxy1:8090", id="PROXY_NAME_PORT_CREDS"),
        pytest.param(f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:8090", id="PROXY_NAME_PORT_QUOTED_CREDS"),
        pytest.param("http://proxy1.domain.local:8090", id="PROXY_FQDN_PORT"),
        pytest.param(f"http://{USER}:{PASS}@proxy1.domain.local:8090", id="PROXY_FQDN_PORT_CREDS"),
        pytest.param(f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1.domain.local:8090", id="PROXY_FQDN_PORT_QUOTED_CREDS"),
        pytest.param("http://11.11.11.11:8090", id="PROXY_IPV4_PORT"),
        pytest.param(f"http://{USER}:{PASS}@11.11.11.11:8090", id="PROXY_IPV4_PORT_CREDS"),
        pytest.param(f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@11.11.11.11:8090", id="PROXY_IPV4_PORT_QUOTED_CREDS"),
        pytest.param("http://[2002::20]:8090", id="PROXY_IPV6_PORT"),
        pytest.param(f"http://{USER}:{PASS}@[2002::20]:8090", id="PROXY_IPV6_PORT_CREDS"),
        pytest.param(f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@[2002::20]:8090", id="PROXY_IPV6_PORT_QUOTED_CREDS"),
    ],
)
async def test_cv_client_proxy_env_vars(monkeypatch: pytest.MonkeyPatch, proxy_env_var_name: str, proxy_env_var_value: str | None) -> None:
    """Test ability to read and properly process environment variable based proxy settings."""
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    if proxy_env_var_value is not None:
        monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
        ) as cvclient:
            assert cvclient.cv_connection_manager.cv_proxy_manager.get_proxy_url() == proxy_env_var_value


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("proxy_env_var_name"),
    [
        pytest.param("https_proxy", id="LOWER_HTTPS_PROXY"),
        pytest.param("HTTPS_PROXY", id="UPPER_HTTPS_PROXY"),
        pytest.param("all_proxy", id="LOWER_ALL_PROXY"),
        pytest.param("ALL_PROXY", id="UPPER_ALL_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_env_var_value", "expected_exception"),
    [
        pytest.param("https://proxy1:8090", pytest.raises(AristaAvdInvalidInputsError, match=r"Scheme 'https'.*is not supported"), id="PROXY_INVALID_SCHEMA_1"),
        pytest.param(
            f"https://{USER}:{PASS}@proxy1:8090",
            pytest.raises(AristaAvdInvalidInputsError, match=r"Scheme 'https'.*is not supported"),
            id="PROXY_INVALID_SCHEMA_2",
        ),
        pytest.param(
            f"https://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:8090",
            pytest.raises(AristaAvdInvalidInputsError, match=r"Scheme 'https'.*is not supported"),
            id="PROXY_INVALID_SCHEMA_3",
        ),
        pytest.param("http://:8090", pytest.raises(AristaAvdInvalidInputsError, match=r"Host 'None'.*is not supported"), id="PROXY_EMPTY_HOST_1"),
        pytest.param(
            f"http://{USER}:{PASS}@:8090", pytest.raises(AristaAvdInvalidInputsError, match=r"Host 'None'.*is not supported"), id="PROXY_EMPTY_HOST_2"
        ),
        pytest.param(
            f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@:8090",
            pytest.raises(AristaAvdInvalidInputsError, match=r"Host 'None'.*is not supported"),
            id="PROXY_EMPTY_HOST_3",
        ),
        pytest.param("http://proxy1:", pytest.raises(AristaAvdInvalidInputsError, match=r"Port 'None'.*is not supported"), id="PROXY_NO_PORT_1"),
        pytest.param(f"http://{USER}:{PASS}@proxy1:", pytest.raises(AristaAvdInvalidInputsError, match=r"Port 'None'.*is not supported"), id="PROXY_NO_PORT_2"),
        pytest.param(
            f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:",
            pytest.raises(AristaAvdInvalidInputsError, match=r"Port 'None'.*is not supported"),
            id="PROXY_NO_PORT_3",
        ),
        pytest.param("http://proxy1:0", pytest.raises(AristaAvdInvalidInputsError, match=r"Port '0'.*is not supported"), id="PROXY_INVALID_PORT_1"),
        pytest.param(
            f"http://{USER}:{PASS}@proxy1:0", pytest.raises(AristaAvdInvalidInputsError, match=r"Port '0'.*is not supported"), id="PROXY_INVALID_PORT_2"
        ),
        pytest.param(
            f"http://{USER_SS_QUOTED}:{PASS_SS_QUOTED}@proxy1:0",
            pytest.raises(AristaAvdInvalidInputsError, match=r"Port '0'.*is not supported"),
            id="PROXY_INVALID_PORT_3",
        ),
    ],
)
async def test_cv_client_proxy_env_vars_invalid(
    monkeypatch: pytest.MonkeyPatch, proxy_env_var_name: str, proxy_env_var_value: str | None, expected_exception: ExpectedExceptionContext
) -> None:
    """Test ability to read incorrect environment variable based proxy settings and raise an exception."""
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    if proxy_env_var_value is not None:
        monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"), expected_exception:
        async with CVClient(
            servers=servers,
            token=token,
        ):
            pass


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"),
    [
        pytest.param(
            "http://new_user1:new_password1@10.10.10.10:8081",
            "http://new_user2:new_password2@11.11.11.11:8082",
            None,
            None,
            id="LOWER_HTTPS_PROXY_WINS",
        ),
        pytest.param(
            None,
            "http://new_user1:new_password1@10.10.10.10:8081",
            "http://new_user2:new_password2@11.11.11.11:8082",
            None,
            id="UPPER_HTTPS_PROXY_WINS",
        ),
        pytest.param(
            None,
            None,
            "http://new_user1:new_password1@10.10.10.10:8081",
            "http://new_user2:new_password2@11.11.11.11:8082",
            id="LOWER_ALL_PROXY_WINS",
        ),
        pytest.param(
            None,
            None,
            None,
            "http://new_user1:new_password1@10.10.10.10:8081",
            id="UPPER_ALL_PROXY_WINS",
        ),
    ],
)
@pytest.mark.parametrize(
    ("proxy_username"),
    [
        pytest.param(None, id="PROXY_USERNAME_NONE"),
        pytest.param(USER, id="PROXY_USERNAME_SET"),
    ],
)
@pytest.mark.parametrize(
    ("proxy_password"),
    [
        pytest.param(None, id="PROXY_PASSWORD_NONE"),
        pytest.param(PASS, id="PROXY_PASSWORD_SET"),
    ],
)
async def test_cv_client_proxy_env_vars_preference(
    monkeypatch: pytest.MonkeyPatch,
    https_proxy: str | None,
    HTTPS_PROXY: str | None,  # noqa: N803
    all_proxy: str | None,
    ALL_PROXY: str | None,  # noqa: N803
    proxy_username: str | None,
    proxy_password: str | None,
) -> None:
    """Test order of preference for proxy-related environment variables (`https_proxy` -> `HTTPS_PROXY` -> `all_proxy` -> `ALL_PROXY`)."""
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

    assert cvclient.cv_connection_manager.cv_proxy_manager.use_proxy
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_scheme == "http"
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_host == "10.10.10.10"
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_port == 8081
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_username == "new_user1"
    assert cvclient.cv_connection_manager.cv_proxy_manager._proxy_password == "new_password1"  # noqa: S105
    assert cvclient.cv_connection_manager.cv_proxy_manager._target_host == servers
    assert cvclient.cv_connection_manager.cv_proxy_manager._target_port == 443


@pytest.mark.asyncio
@pytest.mark.parametrize(("proxy_env_var_value"), [pytest.param("http://user1:pass1@10.10.10.10:8081", id="PROXY")])
@pytest.mark.parametrize(
    ("no_proxy_env_var_name"),
    [
        pytest.param("no_proxy", id="LOWER_NO_PROXY"),
        pytest.param("NO_PROXY", id="UPPER_NO_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy_env_var_value"),
    [
        pytest.param("www.arista.io", id="NO_PROXY_FQDN_1"),
        pytest.param("www.arista.io,www.arista.com", id="NO_PROXY_FQDN_2"),
        pytest.param("www.arista.io:443", id="NO_PROXY_FQDN_WITH_PORT_1"),
        pytest.param("www.arista.io:443,www.arista.com:443", id="NO_PROXY_FQDN_WITH_PORT_2"),
        pytest.param(".arista.io", id="NO_PROXY_WILDCARD_DOMAIN"),
        pytest.param(".arista.io:443", id="NO_PROXY_WILDCARD_DOMAIN_WITH_PORT"),
        pytest.param("*", id="NO_PROXY_STAR"),
    ],
)
async def test_cv_client_proxy_settings_no_proxy_override_fqdn(
    monkeypatch: pytest.MonkeyPatch,
    proxy_env_var_value: str,
    no_proxy_env_var_name: str,
    no_proxy_env_var_value: str,
) -> None:
    """Test ability of proxy bypass vars to override proxy vars for fqdn-based CloudVision host."""
    servers = "www.arista.io"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    for proxy_env_var_name in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]:
        monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    # Set proxy bypass ENV Variables based on the pytest parametrize inputs
    monkeypatch.setenv(no_proxy_env_var_name, no_proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
        ) as cvclient:
            pass

    assert not cvclient.cv_connection_manager.use_proxy


@pytest.mark.asyncio
@pytest.mark.parametrize(("proxy_env_var_value"), [pytest.param("http://user1:pass1@10.10.10.10:8081", id="PROXY")])
@pytest.mark.parametrize(
    ("no_proxy_env_var_name"),
    [
        pytest.param("no_proxy", id="LOWER_NO_PROXY"),
        pytest.param("NO_PROXY", id="UPPER_NO_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy_env_var_value"),
    [
        pytest.param("192.168.10.10", id="NO_PROXY_IPV4"),
        pytest.param("192.168.10.10/32", id="NO_PROXY_IPV4_CIDR_32"),
        pytest.param("192.168.10.0/24", id="NO_PROXY_IPV4_CIDR_24"),
        pytest.param("*", id="NO_PROXY_STAR"),
    ],
)
async def test_cv_client_proxy_settings_no_proxy_override_ipv4(
    monkeypatch: pytest.MonkeyPatch,
    proxy_env_var_value: str,
    no_proxy_env_var_name: str,
    no_proxy_env_var_value: str,
) -> None:
    """Test ability of proxy bypass vars to override proxy vars for ipv4-based CloudVision host."""
    servers = "192.168.10.10"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    for proxy_env_var_name in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]:
        monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    # Set proxy bypass ENV Variables based on the pytest parametrize inputs
    monkeypatch.setenv(no_proxy_env_var_name, no_proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
        ) as cvclient:
            pass

    assert not cvclient.cv_connection_manager.use_proxy


@pytest.mark.asyncio
@pytest.mark.parametrize(("proxy_env_var_value"), [pytest.param("http://user1:pass1@[2002::20]:8081", id="PROXY")])
@pytest.mark.parametrize(
    ("no_proxy_env_var_name"),
    [
        pytest.param("no_proxy", id="LOWER_NO_PROXY"),
        pytest.param("NO_PROXY", id="UPPER_NO_PROXY"),
    ],
)
@pytest.mark.parametrize(
    ("no_proxy_env_var_value"),
    [
        pytest.param("2001::10", id="NO_PROXY_IPV6"),
        pytest.param("2001::10/128", id="NO_PROXY_IPV6_CIDR_128"),
        pytest.param("2001::/64", id="NO_PROXY_IPV6_CIDR_64"),
        pytest.param("*", id="NO_PROXY_STAR"),
    ],
)
async def test_cv_client_proxy_settings_no_proxy_override_ipv6(
    monkeypatch: pytest.MonkeyPatch,
    proxy_env_var_value: str,
    no_proxy_env_var_name: str,
    no_proxy_env_var_value: str,
) -> None:
    """Test ability of proxy bypass vars to override proxy vars for ipv6-based CloudVision host."""
    servers = "2001::10"
    token = "secret_access_token"  # noqa: S105

    # Unset all relevant ENV Variables in case they are set in testing environment
    unset_proxy_related_env_vars(monkeypatch)

    # Set proxy ENV Variables based on the pytest parametrize inputs
    for proxy_env_var_name in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]:
        monkeypatch.setenv(proxy_env_var_name, proxy_env_var_value)

    # Set proxy bypass ENV Variables based on the pytest parametrize inputs
    monkeypatch.setenv(no_proxy_env_var_name, no_proxy_env_var_value)

    with patch("pyavd._cv.client.CVClient._set_version", return_value="CVaaS"):
        async with CVClient(
            servers=servers,
            token=token,
        ) as cvclient:
            pass

    assert not cvclient.cv_connection_manager.use_proxy


######################
## Live proxy tests ##
######################
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
