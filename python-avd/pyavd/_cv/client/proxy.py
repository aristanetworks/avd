# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from os import environ
from typing import TYPE_CHECKING
from urllib.parse import urlparse

from python_socks.async_.asyncio import Proxy

from pyavd._cv.workflows.models import CVProxyServerCandidate

if TYPE_CHECKING:
    import socket
    from urllib.parse import ParseResult


class HTTPProxyManager:
    """
    HTTP proxy manager for CloudVision connections.

    This class provides basic HTTP proxy support for both REST API calls
    and gRPC connections without authentication or SSL to the proxy.
    """

    scheme: str
    host: str | None
    port: int | None
    username: str | None
    password: str | None
    target_host: str
    target_port: int

    def __init__(
        self,
        scheme: str,
        host: str | None,
        port: int | None,
        username: str | None,
        password: str | None,
        target_host: str,
        target_port: int,
    ) -> None:
        """
        Initialize the proxy manager.

        Args:
            scheme: Proxy server scheme (http/https).
            host: Proxy server hostname or IP address.
            port: Proxy server port.
            username: Proxy authentication username.
            password: Proxy authentication password.
            target_host: Target CloudVision server hostname.
            target_port: Target CloudVision server port.
        """
        self.scheme = scheme
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.target_host = target_host
        self.target_port = target_port

    @cached_property
    def proxy_url(self) -> str:
        """
        Generate proxy URL.

        Returns:
            HTTP proxy URL.
        """
        if self.username and self.password:
            # Excempting the lines below from Sonar since we cannot use HTTPS here.
            return f"http://{self.username}:{self.password}@{self.host}:{self.port}"  # NOSONAR
        return f"http://{self.host}:{self.port}"  # NOSONAR

    @cached_property
    def get_requests_proxies(self) -> dict[str, str]:
        """
        Generate proxy configuration for requests library.

        When proxy server is used we explicitly pass `"no_proxy": "_"` to prevent `requests`/`urllib` from reading `no_proxy`/`NO_PROXY`
        again as we already did this.
        When proxy server is not used we pass `"no_proxy": self.target_host` to make sure `requests`/`urllib` don't fallback to using proxy for cv_deploy flows.

        Returns:
            Dictionary with proxy configuration for requests.
        """
        return {"http": self.proxy_url, "https": self.proxy_url, "no_proxy": "_"} if self.use_proxy else {"no_proxy": self.target_host}

    async def create_socket_for_grpc(self) -> socket.socket:
        """
        Create a socket for gRPC connections through the proxy.

        Returns:
            Raw socket connected to target through proxy.
        """
        # Create proxy using python-socks
        proxy = Proxy.from_url(self.proxy_url)

        # Connect through proxy to target
        return await proxy.connect(dest_host=self.target_host, dest_port=self.target_port)

    @cached_property
    def use_proxy(self) -> bool:
        """Boolean defining if proxy server should be used for CloudVision (both REST and gRPC) or not."""
        # First check if usable proxy-related settings were passed to CVClient explicitly
        if self.proxy_candidate_is_usable(
            CVProxyServerCandidate(
                scheme=self.scheme,
                host=self.host,
                port=self.port,
                username=self.username,
                password=self.password,
            )
        ):
            return True

        # Fallback to the proxy-related settings passed via environment variables
        return self.proxy_set_via_env and not self.bypass_proxy

    @cached_property
    def bypass_proxy(self) -> bool:
        """Checks if target CloudVision server is included in environment variables `no_proxy` or `NO_PROXY` forcing proxy bypass."""
        for env_variable_candidate in ["no_proxy", "NO_PROXY"]:
            if isinstance(no_proxy_candidate := environ.get(env_variable_candidate), str) and len(no_proxy_candidate) > 0:
                return bool({f"{self.target_host}", f"{self.target_host + ':' + str(self.target_port)}"} & set(no_proxy_candidate.split(",")))
        # No interesting environment variables are set
        return False

    @cached_property
    def proxy_set_via_env(self) -> bool:
        """
        Verifies if usable proxy-related settings are set via either `https_proxy`, `HTTPS_PROXY`, `all_proxy` or `ALL_PROXY` environment variables.

        Parses value of the `https_proxy`, `HTTPS_PROXY`, `all_proxy` and `ALL_PROXY` environment variables to obtain Proxy server parameters.
        Order of preference: `https_proxy` else `HTTPS_PROXY` else `all_proxy` else `ALL_PROXY`.
        Updates HTTPProxyManager if usable Proxy server is found.

        Returns:
            True if usable Proxy server has been identified via interesting environment variables, otherwise False.
        """
        for env_variable_candidate in ["https_proxy", "HTTPS_PROXY", "all_proxy", "ALL_PROXY"]:
            if isinstance(proxy_candidate := environ.get(env_variable_candidate), str) and len(proxy_candidate) > 0:
                parsed_proxy_candidate = self.parse_https_proxy_uri(proxy_candidate)
                if self.proxy_candidate_is_usable(parsed_proxy_candidate):
                    self.update_proxy_manager(parsed_proxy_candidate)
                    return True
        return False

    @staticmethod
    def parse_https_proxy_uri(https_proxy_uri: str) -> CVProxyServerCandidate:
        """Parses string representing discovered proxy URI."""
        urlparse_result: ParseResult = urlparse(https_proxy_uri)
        return CVProxyServerCandidate(
            scheme=urlparse_result.scheme,
            host=urlparse_result.hostname,
            port=urlparse_result.port,
            username=urlparse_result.username,
            password=urlparse_result.password,
        )

    @staticmethod
    def proxy_candidate_is_usable(proxy_candidate: CVProxyServerCandidate) -> bool:
        """Verifies that mandatory proxy settings are set in Proxy server candidate."""
        return all(
            [
                proxy_candidate.scheme == "http",
                isinstance(proxy_candidate.host, str) and len(proxy_candidate.host) > 0,
                isinstance(proxy_candidate.port, int) and (0 < proxy_candidate.port < 65536),
            ]
        )

    def update_proxy_manager(self, proxy_candidate: CVProxyServerCandidate) -> None:
        """Updates proxy-related attributes once usable proxy candidate is found."""
        self.scheme = proxy_candidate.scheme
        self.host = proxy_candidate.host
        self.port = proxy_candidate.port
        self.username = proxy_candidate.username
        self.password = proxy_candidate.password
