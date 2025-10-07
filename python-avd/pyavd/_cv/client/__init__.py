# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import ssl
from typing import TYPE_CHECKING, Protocol

from grpclib.client import Channel
from requests import JSONDecodeError, get, post
from requests.exceptions import HTTPError, RequestException

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .proxy import HTTPProxyManager
from .studio import StudioMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .versioning import CvVersion
from .workspace import WorkspaceMixin

if TYPE_CHECKING:
    from types import TracebackType

    from grpclib.protocol import H2Protocol
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
    _proxy_manager: HTTPProxyManager | None = None

    async def __aenter__(self) -> Self:
        """Using asynchronous context manager since grpclib must be initialized inside an asyncio loop."""
        await self._connect()
        return self

    async def __aexit__(self, _exc_type: type[BaseException] | None, _exc_val: BaseException | None, _exc_tb: TracebackType | None) -> None:
        if self._channel is not None:
            self._channel.close()
            self._channel = None

    async def _connect(self) -> None:
        # TODO: Verify connection
        # TODO: Handle multinode clusters

        # Ensure that the default ssl context is initialized before doing any requests.
        ssl_context = self._ssl_context()

        if not self._token:
            self._set_token()

        self._set_version()

        if self._channel is None:
            if self._proxy_manager is not None:
                self._channel = await self._create_proxy_channel(ssl_context)
            else:
                self._channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        self._metadata = {"authorization": "Bearer " + self._token}

    async def _create_proxy_channel(self, ssl_context: ssl.SSLContext | bool) -> Channel:
        """
        Create a gRPC channel using the proxy manager.

        Args:
            ssl_context: SSL context for destination server connection.

        Returns:
            Configured gRPC Channel instance.
        """
        # Create the channel first
        channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context)

        # Create custom connector that uses proxy
        async def proxy_connection() -> H2Protocol:
            loop = asyncio.get_running_loop()

            try:
                # Create socket through proxy using python-socks
                proxy_sock = await self._proxy_manager.create_socket_for_grpc()

                # Create the gRPC protocol using the proxy socket
                _, protocol = await loop.create_connection(
                    lambda: channel._protocol_factory(),
                    sock=proxy_sock,
                    ssl=channel._ssl,
                    server_hostname=self._servers[0] if ssl_context else None,
                )

            except Exception as e:
                msg = f"Failed to create proxy connection: {type(e).__name__}: {e}"
                raise CVClientException(msg) from e

            return protocol

        # Override the standard method from grpclib with our proxy variant.
        channel._create_connection = proxy_connection
        return channel

    def _ssl_context(self) -> ssl.SSLContext | bool:
        """
        Initialize the default SSL context with relaxed verification if needed.

        Otherwise we just return True.
        The return value (The default ssl context or True) will be passed to grpclib.
        Requests will pick it up from ssl lib itself.
        """
        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
        else:
            context = True
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
            response = post(  # noqa: S113 TODO: Add configurable timeout
                "https://" + self._servers[0] + "/cvpservice/login/authenticate.do",
                auth=(self._username, self._password),
                verify=self._verify_certs,
                proxies=self._proxy_manager.get_requests_proxies() if self._proxy_manager is not None else None,
                json={},
            )
            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            msg = f"Unable to get token from CloudVision server due to the following error: {e.args}."
            raise CVClientException(msg) from e

        try:
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
            response = get(  # noqa: S113 TODO: Add configurable timeout
                "https://" + self._servers[0] + "/cvpservice/cvpInfo/getCvpInfo.do",
                headers={"Authorization": f"Bearer {self._token}"},
                verify=self._verify_certs,
                proxies=self._proxy_manager.get_requests_proxies() if self._proxy_manager is not None else None,
                json={},
            )
            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            msg = f"Unable to get version from CloudVision server due to the following error: {e.args}."
            raise CVClientException(msg) from e

        try:
            self._cv_version = CvVersion(response.json()["version"])
        except (KeyError, JSONDecodeError) as e:
            msg = f"Unable to get version from CloudVision server. Got {response.text if response else 'No response'}"
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
        proxy_port: int = 8080,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
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
            proxy_host: HTTP proxy hostname.
            proxy_port: HTTP proxy port.
            proxy_username: Proxy authentication username.
            proxy_password: Proxy authentication password.
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
        self._proxy_manager = None

        # Initialize proxy manager if proxy is configured
        if proxy_host is not None:
            self._proxy_manager = HTTPProxyManager(
                proxy_host=proxy_host,
                proxy_port=proxy_port,
                proxy_username=proxy_username,
                proxy_password=proxy_password,
                target_host=self._servers[0],
                target_port=self._port,
            )
