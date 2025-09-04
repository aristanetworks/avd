# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import base64
import ssl
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING

import certifi

if TYPE_CHECKING:
    from requests import Session


class ProxyForwarder:
    """
    Unix socket forwarder for proxy tunneling.

    Creates a Unix domain socket server that forwards connections through an HTTP/HTTPS proxy
    using the CONNECT method. Supports both authenticated and IP-based proxy configurations.
    """

    proxy_host: str
    proxy_port: int
    proxy_username: str | None
    proxy_password: str | None
    custom_ca_path: str | None
    proxy_ssl: bool
    proxy_verify_certs: bool
    dest_host: str
    dest_port: int
    socket_path: Path | None
    server: asyncio.Server | None

    def __init__(
        self,
        proxy_host: str,
        proxy_port: int,
        dest_host: str,
        dest_port: int,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
        custom_ca_path: str | None = None,
        proxy_ssl: bool = True,
        proxy_verify_certs: bool = True,
    ) -> None:
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.proxy_username = proxy_username
        self.proxy_password = proxy_password
        self.custom_ca_path = custom_ca_path
        self.proxy_ssl = proxy_ssl
        self.proxy_verify_certs = proxy_verify_certs
        self.dest_host = dest_host
        self.dest_port = dest_port
        self.socket_path = None
        self.server = None

    async def start(self) -> str:
        """
        Start the proxy forwarder server.

        Returns:
            Unix socket path for gRPC client connections.
        """
        temp_dir = Path(tempfile.mkdtemp())
        self.socket_path = temp_dir / "grpc_proxy.sock"
        self.server = await asyncio.start_unix_server(self._handle_client, path=str(self.socket_path))
        return str(self.socket_path)

    async def stop(self) -> None:
        """Stop the proxy forwarder and clean up resources."""
        if self.server:
            self.server.close()
            await self.server.wait_closed()
        if self.socket_path and Path(self.socket_path).exists():
            try:
                socket_path = Path(self.socket_path)
                socket_path.unlink()  # Remove socket file
                socket_path.parent.rmdir()  # Remove temp directory
            except OSError:
                pass

    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """
        Handle a client connection through the proxy.

        Establishes a connection to the proxy server, sends a CONNECT request,
        and relays data bidirectionally between the client and proxy tunnel.

        Args:
            reader: Client connection reader stream.
            writer: Client connection writer stream.
        """
        try:
            # Connect to proxy and establish tunnel
            proxy_reader, proxy_writer = await self._connect_to_proxy()

            # Relay data bidirectionally between client and proxy
            await asyncio.gather(
                # client to proxy
                self._copy_data(reader, proxy_writer),
                # proxy to client
                self._copy_data(proxy_reader, writer),
                return_exceptions=True,
            )
        except Exception:
            # Connection failed or ended
            pass
        finally:
            # Clean up client connection
            try:
                writer.close()
                await writer.wait_closed()
            except:
                pass

    async def _connect_to_proxy(self) -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        """
        Connect to the proxy server and establish a tunnel.

        Returns:
            Tuple of (reader, writer) for the established proxy tunnel.

        Raises:
            ConnectionError: If the proxy CONNECT request fails.
        """
        if self.proxy_ssl:
            # HTTPS proxy
            ssl_context = ssl.create_default_context()
            if self.custom_ca_path:
                ssl_context.load_verify_locations(cafile=self.custom_ca_path)

            # Configure SSL certificate verification
            if not self.proxy_verify_certs:
                ssl_context.check_hostname = False
                ssl_context.verify_mode = ssl.CERT_NONE

            reader, writer = await asyncio.open_connection(
                self.proxy_host, self.proxy_port, ssl=ssl_context, server_hostname=self.proxy_host if self.proxy_verify_certs else None
            )
        else:
            # HTTP proxy
            reader, writer = await asyncio.open_connection(self.proxy_host, self.proxy_port)

        # Send CONNECT request
        connect_request = f"CONNECT {self.dest_host}:{self.dest_port} HTTP/1.1\r\n"
        connect_request += f"Host: {self.dest_host}:{self.dest_port}\r\n"

        # Add proxy authentication if credentials provided
        if self.proxy_username and self.proxy_password:
            auth = base64.b64encode(f"{self.proxy_username}:{self.proxy_password}".encode()).decode()
            connect_request += f"Proxy-Authorization: Basic {auth}\r\n"

        connect_request += "\r\n"

        writer.write(connect_request.encode("latin-1"))
        await writer.drain()

        # Read response
        response_line = await reader.readline()
        if not response_line.decode().startswith("HTTP/1.1 200"):
            raise ConnectionError(f"Proxy CONNECT failed: {response_line.decode().strip()}")

        # Skip remaining headers
        while True:
            line = await reader.readline()
            if line == b"\r\n" or not line:
                break

        return reader, writer

    async def _copy_data(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        """
        Copy data between reader and writer streams.

        Args:
            reader: Source stream to read from.
            writer: Destination stream to write to.
        """
        try:
            while True:
                data = await reader.read(8192)
                if not data:
                    break
                writer.write(data)
                await writer.drain()
        except Exception:
            pass
        finally:
            try:
                writer.close()
                await writer.wait_closed()
            except:
                pass


def configure_session_with_proxy(
    session: Session,
    proxy_host: str,
    proxy_port: int,
    proxy_username: str | None = None,
    proxy_password: str | None = None,
    custom_ca_path: str | None = None,
    proxy_ssl: bool = True,
    proxy_verify_certs: bool = True,
    dest_verify_certs: bool = True,
) -> str | None:
    """
    Configure a requests session to use a proxy server.

    Args:
        session: The requests Session object to configure.
        proxy_host: Proxy server hostname.
        proxy_port: Proxy server port.
        proxy_username: Proxy authentication username (optional).
        proxy_password: Proxy authentication password (optional).
        custom_ca_path: Path to custom CA certificate for proxy SSL verification (optional).
        proxy_ssl: Whether to use HTTPS for proxy connection.
        proxy_verify_certs: Whether to verify proxy SSL certificates.
        dest_verify_certs: Whether to verify destination SSL certificates.

    Returns:
        Path to temporary CA bundle file if created, None otherwise.
    """
    temp_ca_bundle_path = None

    # Configure CA bundle for destination verification
    if custom_ca_path and proxy_ssl and proxy_verify_certs:
        # Create mixed CA bundle: system CAs + custom proxy CA
        temp_ca_bundle_path = create_ca_bundle_with_custom_ca(custom_ca_path)
        session.verify = temp_ca_bundle_path
    else:
        # Use system CAs only or disable verification
        session.verify = dest_verify_certs

    # Configure proxy URL
    if proxy_ssl:
        scheme = "https"
    else:
        scheme = "http"

    if proxy_username and proxy_password:
        proxy_url = f"{scheme}://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
    else:
        proxy_url = f"{scheme}://{proxy_host}:{proxy_port}"

    session.proxies = {"https": proxy_url, "http": proxy_url}

    return temp_ca_bundle_path


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

    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8")
    temp_ca_bundle_path = temp_file.name

    # Copy system CAs
    temp_file.write(system_ca_path.read_text(encoding="UTF-8"))
    temp_file.write("\n")

    # Append custom CA
    temp_file.write(custom_ca_path_obj.read_text(encoding="UTF-8"))
    temp_file.close()

    return temp_ca_bundle_path


def configure_session_for_single_socket_proxy(
    session: Session, proxy_host: str, proxy_port: int, custom_ca_path: str | None = None, dest_verify_certs: bool = True
) -> str | None:
    """
    Configure a requests session for single socket proxy approach.

    This function configures the session for HTTP proxy without authentication,
    suitable for environments where Unix sockets are not available.

    Args:
        session: The requests Session object to configure.
        proxy_host: HTTP proxy server hostname.
        proxy_port: HTTP proxy server port.
        custom_ca_path: Path to custom CA certificate for destination SSL verification (optional).
        dest_verify_certs: Whether to verify destination SSL certificates.

    Returns:
        Path to temporary CA bundle file if created, None otherwise.
    """
    temp_ca_bundle_path = None

    # Configure CA bundle for destination verification only
    if custom_ca_path and dest_verify_certs:
        # Create mixed CA bundle: system CAs + custom CA for destination
        temp_ca_bundle_path = create_ca_bundle_with_custom_ca(custom_ca_path)
        session.verify = temp_ca_bundle_path
    else:
        # Use system CAs only or disable verification
        session.verify = dest_verify_certs

    # Configure HTTP proxy without authentication
    proxy_url = f"http://{proxy_host}:{proxy_port}"
    session.proxies = {"https": proxy_url, "http": proxy_url}

    return temp_ca_bundle_path
