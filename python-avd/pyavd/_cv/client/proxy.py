# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import certifi
from python_socks.async_.asyncio import Proxy

if TYPE_CHECKING:
    import socket


class HTTPProxyManager:
    """
    HTTP proxy manager for CloudVision connections.

    This class provides basic HTTP proxy support for both REST API calls
    and gRPC connections without authentication or SSL to the proxy.
    """

    def __init__(
        self,
        proxy_host: str,
        proxy_port: str,
        target_host: str,
        target_port: int,
    ) -> None:
        """
        Initialize the proxy manager.

        Args:
            proxy_host: Proxy server hostname or IP address.
            proxy_port: Proxy server port.
            target_host: Target server hostname.
            target_port: Target server port.

        Raises:
            ImportError: If python-socks is not available.
        """
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.target_host = target_host
        self.target_port = target_port

    @property
    def proxy_url(self) -> str:
        """
        Generate proxy URL for python-socks.

        Returns:
            HTTP proxy URL for python-socks library.
        """
        return f"http://{self.proxy_host}:{self.proxy_port}"

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


def create_ca_bundle_with_custom_ca(custom_ca_path: str) -> str:
    """
    Create a temporary CA bundle file combining system CAs with custom CA.

    Args:
        custom_ca_path: Path to custom CA certificate file.

    Returns:
        Path to temporary CA bundle file.
    """
    system_ca_path = Path(certifi.where())
    custom_ca_path_obj = Path(custom_ca_path)

    with tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8") as temp_file:
        temp_ca_bundle_path = temp_file.name

        # Copy system CAs
        temp_file.write(system_ca_path.read_text(encoding="UTF-8"))
        temp_file.write("\n")

        # Append custom CA
        temp_file.write(custom_ca_path_obj.read_text(encoding="UTF-8"))

    return temp_ca_bundle_path
