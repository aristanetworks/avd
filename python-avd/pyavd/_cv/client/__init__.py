# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import socket
import ssl
from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from grpclib.client import Channel
from requests import JSONDecodeError, Session

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .proxy import ProxyForwarder, configure_session_for_single_socket_proxy, configure_session_with_proxy, create_ca_bundle_with_custom_ca
from .studio import StudioMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .versioning import CvVersion
from .workspace import WorkspaceMixin

if TYPE_CHECKING:
    from types import TracebackType

    from typing_extensions import Self


class CVClientProtocol(
    ChangeControlMixin,
    ConfigletMixin,
    InventoryMixin,
    StudioMixin,
    SwgMixin,
    TagMixin,
    WorkspaceMixin,
    UtilsMixin,
    Protocol,
):
    """Protocol for the CVClient class."""

    _channel: Channel | None = None
    _metadata: dict
    _servers: list[str]
    _port: int
    _verify_certs: bool
    _token: str | None
    _username: str | None
    _password: str | None
    _cv_version: CvVersion | None = None
    _session: Session | None = None
    _temp_ca_bundle_path: str | None = None
    _proxy_forwarder: ProxyForwarder | None = None
    _proxy_socket_path: str | None = None
    _proxy_unix_socket_forwarder: bool

    async def __aenter__(self) -> Self:
        """Using asynchronous context manager since grpclib must be initialized inside an asyncio loop."""
        await self._connect()
        return self

    async def __aexit__(self, _exc_type: type[BaseException] | None, _exc_val: BaseException | None, _exc_tb: TracebackType | None) -> None:
        if self._channel is not None:
            self._channel.close()
            self._channel = None
        if self._proxy_forwarder is not None:
            await self._proxy_forwarder.stop()
            self._proxy_forwarder = None
            self._proxy_socket_path = None
        if self._session is not None:
            self._session.close()
            self._session = None
        if self._temp_ca_bundle_path and Path(self._temp_ca_bundle_path).exists():
            try:
                Path(self._temp_ca_bundle_path).unlink()
            except OSError:
                pass
            self._temp_ca_bundle_path = None

    async def _connect(self) -> None:
        # TODO: Verify connection
        # TODO: Handle multinode clusters

        # Configure requests session for REST calls
        self._session = Session()

        # Check if proxy is configured
        if self._proxy_host and self._proxy_port:
            # Tunnel gRPC via unix socket forwarder
            if self._proxy_unix_socket_forwarder:
                # Configure session with proxy and CA bundle (for REST calls)
                self._temp_ca_bundle_path = configure_session_with_proxy(
                    self._session,
                    self._proxy_host,
                    self._proxy_port,
                    self._proxy_username,
                    self._proxy_password,
                    self._custom_ca_path,
                    self._proxy_ssl,
                    self._proxy_verify_certs,
                    self._verify_certs,
                )

                # Start Unix socket forwarder (for gRPC calls)
                self._proxy_forwarder = ProxyForwarder(
                    self._proxy_host,
                    self._proxy_port,
                    self._servers[0],
                    self._port,
                    self._proxy_username,
                    self._proxy_password,
                    self._custom_ca_path,
                    self._proxy_ssl,
                    self._proxy_verify_certs,
                )
                self._proxy_socket_path = await self._proxy_forwarder.start()
            else:
                # Network socket approach (for environments without Unix socket support)
                # Force HTTP proxy without authentication for security
                if self._proxy_ssl or self._proxy_username or self._proxy_password:
                    msg = "Network socket proxy mode requires HTTP proxy without authentication (proxy_ssl=False, no proxy_username/proxy_password)"
                    raise CVClientException(msg)

                # Configure session with HTTP proxy (for REST calls)
                self._temp_ca_bundle_path = configure_session_for_single_socket_proxy(
                    self._session, self._proxy_host, self._proxy_port, self._custom_ca_path, self._verify_certs
                )
        else:
            # Direct connection - configure session normally
            self._session.verify = self._verify_certs

        # Ensure that the default ssl context is initialized before doing any requests.
        ssl_context = self._ssl_context()

        if not self._token:
            self._set_token()

        self._set_version()

        if self._channel is None:
            if self._proxy_host and self._proxy_port:
                if self._proxy_unix_socket_forwarder and self._proxy_forwarder:
                    # Use Unix socket forwarder for gRPC
                    self._channel = await self._create_unix_socket_channel(self._proxy_socket_path, ssl_context)
                elif not self._proxy_unix_socket_forwarder:
                    # Use network socket for gRPC
                    self._channel = await self._create_proxy_channel(ssl_context)
                else:
                    msg = "Proxy configuration error: forwarder not initialized"
                    raise CVClientException(msg)
            else:
                # Direct connection
                self._channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        self._metadata = {"authorization": "Bearer " + self._token}

    async def _create_unix_socket_channel(self, socket_path: str, ssl_context: ssl.SSLContext | bool) -> Channel:
        """
        Create a gRPC channel that connects through a Unix socket forwarder.

        Args:
            socket_path: Path to the Unix socket created by the proxy forwarder.
            ssl_context: SSL context for destination server connection.

        Returns:
            Configured gRPC Channel instance.
        """
        channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        # Override connection creation to use Unix socket
        async def unix_socket_connection():
            loop = asyncio.get_running_loop()
            unix_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            unix_sock.connect(socket_path)

            transport, protocol = await loop.create_connection(
                channel._protocol_factory,
                sock=unix_sock,
                ssl=ssl_context,
                server_hostname=self._servers[0] if ssl_context else None,
            )
            return protocol

        channel._create_connection = unix_socket_connection
        return channel

    async def _create_proxy_channel(self, ssl_context: ssl.SSLContext | bool) -> Channel:
        """
        Create a gRPC channel that connects through an HTTP proxy using a network socket.

        Suitable for environments where Unix sockets are not available.

        Args:
            ssl_context: SSL context for destination server connection.

        Returns:
            Configured gRPC Channel instance.
        """
        channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        # Create custom connector that reuses the proxy connection
        async def proxy_connection():
            loop = asyncio.get_running_loop()

            # Connect to HTTP proxy
            proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            proxy_sock.setblocking(False)
            await loop.sock_connect(proxy_sock, (self._proxy_host, self._proxy_port))

            # Send CONNECT request for gRPC endpoint
            connect_request = f"CONNECT {self._servers[0]}:{self._port} HTTP/1.1\r\n"
            connect_request += f"Host: {self._servers[0]}:{self._port}\r\n"
            connect_request += "\r\n"

            await loop.sock_sendall(proxy_sock, connect_request.encode("latin-1"))

            # Read response
            response = await loop.sock_recv(proxy_sock, 4096)
            response_str = response.decode("latin-1")

            if not response_str.startswith("HTTP/1.1 200"):
                proxy_sock.close()
                raise ConnectionError(f"Proxy CONNECT failed: {response_str.split('\\r\\n')[0]}")

            # Skip remaining headers until we find the end
            while b"\r\n\r\n" not in response:
                additional_data = await loop.sock_recv(proxy_sock, 4096)
                if not additional_data:
                    break
                response += additional_data

            # Create the gRPC protocol using the tunneled socket
            transport, protocol = await loop.create_connection(
                lambda: channel._protocol_factory(),
                sock=proxy_sock,
                ssl=ssl_context,
                server_hostname=self._servers[0] if ssl_context else None,
            )
            return protocol

        channel._create_connection = proxy_connection
        return channel

    def _ssl_context(self) -> ssl.SSLContext | bool:
        """
        Initialize SSL context for gRPC endpoint verification.

        Creates proper SSL context with custom CA support for gRPC connections.
        The return value will be passed to grpclib for endpoint verification.
        """
        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
            return context

        # Create SSL context with proper verification
        context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
        context.set_alpn_protocols(["h2"])

        # Load custom CA if provided (for gRPC endpoint verification)
        if self._custom_ca_path:
            # Create temporary CA bundle with system + custom CAs for gRPC
            temp_ca_bundle = create_ca_bundle_with_custom_ca(self._custom_ca_path)
            context.load_verify_locations(cafile=temp_ca_bundle)

        return context

    def _set_token(self) -> None:
        """
        Uses username/password for authenticating via REST.

        Sets the session token into self._token to be used for gRPC channel.

        TODO: Handle multinode clusters
        """
        if self._token:
            return

        if not self._username or not self._password:
            msg = "Unable to authenticate. Missing token or username/password."
            raise CVClientException(msg)

        try:
            response = self._session.post(
                "https://" + self._servers[0] + "/cvpservice/login/authenticate.do",
                auth=(self._username, self._password),
                json={},
            )

            self._token = response.json()["sessionId"]
        except (KeyError, JSONDecodeError) as e:
            msg = "Unable to get token from CloudVision server. Please supply service account token instead of username/password."
            raise CVClientException(msg) from e

    def _set_version(self) -> None:
        """
        Fetch the CloudVision version via REST and set self._cv_version.

        This version is used to decide which APIs to use later.

        TODO: Handle multinode clusters
        """
        if not self._token:
            msg = "Unable to get version from CloudVision server. Missing token."
            raise CVClientException(msg)

        try:
            response = self._session.get(
                "https://" + self._servers[0] + "/cvpservice/cvpInfo/getCvpInfo.do",
                headers={"Authorization": f"Bearer {self._token}"},
                json={},
            )

            self._cv_version = CvVersion(response.json()["version"])
        except (KeyError, JSONDecodeError) as e:
            msg = f"Unable to get version from CloudVision server. Got {response.text}"
            raise CVClientException(msg) from e


class CVClient(CVClientProtocol):
    def __init__(
        self,
        servers: str | list[str],
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify_certs: bool = True,
        proxy_host: str | None = None,
        proxy_port: int | None = None,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
        proxy_ssl: bool = True,
        proxy_verify_certs: bool = True,
        proxy_unix_socket_forwarder: bool = True,
        custom_ca_path: str | None = None,
    ) -> None:
        """
        CVClient is a high-level API library for using CloudVision Resource APIs.

        Use CVClient as an async context manager like:
            `async with CVClient(servers="myserver", token="mytoken") as cv_client:`

        Parameters:
            servers: A single FQDN for CVaaS or a list of FQDNs for one CVP cluster.
            token: Token defined in CloudVision under service-accounts.
            username: Username to use for authentication if token is not set.
            password: Password to use for authentication if token is not set.
            port: TCP port to use for the connection.
            verify_certs: Disables SSL certificate verification if set to False. Not recommended for production.
            proxy_host: Proxy hostname (HTTP or HTTPS).
            proxy_port: Proxy port.
            proxy_username: Proxy authentication username (optional for IP-based auth).
            proxy_password: Proxy authentication password (optional for IP-based auth).
            proxy_ssl: Use HTTPS proxy (True) or HTTP proxy (False). Default: True.
            proxy_verify_certs: Verify proxy SSL certificates. Only applies when proxy_ssl=True. Default: True.
            proxy_unix_socket_forwarder: Use Unix socket forwarder (True) or network socket approach (False) for gRPC. Default: True.
            custom_ca_path: Path to custom CA certificate for proxy or REST/gRPC endpoint SSL verification (optional).
        """
        if isinstance(servers, list):
            self._servers = servers
        else:
            self._servers = [servers]

        self._port = port
        self._token = token
        self._username = username
        self._password = password
        self._verify_certs = verify_certs
        self._proxy_host = proxy_host
        self._proxy_port = proxy_port
        self._proxy_username = proxy_username
        self._proxy_password = proxy_password
        self._proxy_ssl = proxy_ssl
        self._proxy_verify_certs = proxy_verify_certs
        self._proxy_unix_socket_forwarder = proxy_unix_socket_forwarder
        self._custom_ca_path = custom_ca_path
        self._proxy_forwarder = None
        self._proxy_socket_path = None
