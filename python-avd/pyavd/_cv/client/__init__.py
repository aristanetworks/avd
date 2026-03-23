# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from requests import JSONDecodeError, get, post
from requests.exceptions import HTTPError, RequestException

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .proxy import CVConnectionManager
from .studio import StudioMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .versioning import CvVersion
from .workspace import WorkspaceMixin

if TYPE_CHECKING:
    from types import TracebackType

    from grpclib.client import Channel
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
    _cv_connection_manager: CVConnectionManager

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
        ssl_context = self._cv_connection_manager.get_ssl_context(self._verify_certs)

        if not self._token:
            self._set_token()

        self._set_version()

        if self._channel is None:
            self._channel = self._cv_connection_manager.create_proxy_channel(ssl_context)

        self._metadata = {"authorization": "Bearer " + self._token}

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
                proxies=self._requests_proxies,
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
                proxies=self._requests_proxies,
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

    @property
    def _use_proxy(self) -> bool:
        return self._cv_connection_manager.use_proxy

    @property
    def _requests_proxies(self) -> dict[str, str]:
        return self._cv_connection_manager.requests_proxies


class CVClient(CVClientProtocol):
    def __init__(
        self,
        servers: str | list[str],
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify_certs: bool = True,
        proxy_scheme: str = "http",
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
            proxy_scheme: Proxy server scheme (http/https).
            proxy_host: Proxy server hostname.
            proxy_port: Proxy server port.
            proxy_username: Proxy server authentication username.
            proxy_password: Proxy server authentication password.
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

        # Initialize connection manager
        self._cv_connection_manager = CVConnectionManager(
            target_host=self._servers[0],
            target_port=self._port,
            proxy_scheme=proxy_scheme,
            proxy_host=proxy_host,
            proxy_port=proxy_port,
            proxy_username=proxy_username,
            proxy_password=proxy_password,
        )
