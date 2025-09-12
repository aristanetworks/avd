# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from python_socks.async_.asyncio import Proxy

if TYPE_CHECKING:
    import socket


class HTTPProxyManager:
    """
    HTTP proxy manager for CloudVision connections.

    This class provides basic HTTP proxy support for both REST API calls
    and gRPC connections without authentication or SSL to the proxy.
    """

    proxy_host: str
    proxy_port: int
    proxy_username: str | None
    proxy_password: str | None
    target_host: str
    target_port: int

    def __init__(
        self,
        proxy_host: str,
        proxy_port: int,
        proxy_username: str | None,
        proxy_password: str | None,
        target_host: str,
        target_port: int,
    ) -> None:
        """
        Initialize the proxy manager.

        Args:
            proxy_host: Proxy server hostname or IP address.
            proxy_port: Proxy server port.
            proxy_username: Proxy authentication username.
            proxy_password: Proxy authentication password.
            target_host: Target server hostname.
            target_port: Target server port.
        """
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.target_host = target_host
        self.target_port = target_port

    @property
    def proxy_url(self) -> str:
        """
        Generate proxy URL.

        Returns:
            HTTP proxy URL.
        """
        if self.proxy_username and self.proxy_password:
            # Excempting the lines below from Sonar since we cannot use HTTPS here.
            return f"http://{self.proxy_username}:{self.proxy_password}@{self.proxy_host}:{self.proxy_port}"  # NOSONAR
        return f"http://{self.proxy_host}:{self.proxy_port}"  # NOSONAR

    def get_requests_proxies(self) -> dict[str, str]:
        """
        Generate proxy configuration for requests library.

        Returns:
            Dictionary with proxy configuration for requests.
        """
        return {
            "http": self.proxy_url,
            "https": self.proxy_url,
        }

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
