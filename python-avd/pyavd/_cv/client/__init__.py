# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import asyncio
import platform
import ssl
import sys
from importlib.metadata import PackageNotFoundError, version
from logging import getLogger
from os import environ
from typing import TYPE_CHECKING, Protocol

from grpclib.client import Channel
from grpclib.config import Configuration
from requests import JSONDecodeError, get, post
from requests.exceptions import HTTPError, RequestException

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .models import CVTLSSettings
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

    from pyavd._cv.workflows.models import CVGRPCChannelConfiguration

LOGGER = getLogger(__name__)


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
    _use_system_certs: bool
    _token: str | None
    _username: str | None
    _password: str | None
    _cv_version: CvVersion | None = None
    _proxy_manager: HTTPProxyManager | None = None
    _grpc_channel_configuration: CVGRPCChannelConfiguration | None = None
    _tls: CVTLSSettings

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

        if not self._token:
            self._set_token()

        self._set_version()

        if self._channel is None:
            if self._proxy_manager is not None:
                self._channel = await self._create_proxy_channel(self._tls.grpc_ssl)
            else:
                self._channel = Channel(host=self._servers[0], port=self._port, ssl=self._tls.grpc_ssl, config=self._grpclib_channel_config)

        self._metadata = {"authorization": "Bearer " + self._token}

    async def _create_proxy_channel(self, ssl_context: ssl.SSLContext | ssl.DefaultVerifyPaths | bool) -> Channel:
        """
        Create a gRPC channel using the proxy manager.

        Args:
            ssl_context: SSL context for destination server connection.

        Returns:
            Configured gRPC Channel instance.
        """
        # Create the channel first
        channel = Channel(host=self._servers[0], port=self._port, ssl=ssl_context, config=self._grpclib_channel_config)

        # Create custom connector that uses proxy
        async def proxy_connection() -> H2Protocol:
            loop = asyncio.get_running_loop()

            try:
                # Create socket through proxy using python-socks
                proxy_sock = await self._proxy_manager.create_socket_for_grpc()

                # Create the gRPC protocol using the proxy socket
                _, protocol = await loop.create_connection(
                    channel._protocol_factory,
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

    @property
    def _grpclib_channel_config(self) -> Configuration:
        """Build the grpclib Channel `config` from the optional gRPC channel configuration."""
        if self._grpc_channel_configuration is None:
            return Configuration()
        return self._grpc_channel_configuration.as_grpclib_configuration()

    def _resolve_tls_settings(self) -> CVTLSSettings:
        """
        Resolve TLS settings for grpclib and requests based on `verify_certs` and `use_system_certs`.

        `verify_certs=False`: No verification on either transport.
            grpclib gets a permissive SSLContext (CERT_NONE, no hostname check).
            requests gets `verify=False`.

        `verify_certs=True`, `use_system_certs=False`: certifi.
            grpclib gets `True` and resolves to certifi internally.
            requests gets `verify=True`. If `REQUESTS_CA_BUNDLE` or `CURL_CA_BUNDLE` is set, requests uses that bundle instead of certifi (this override only
                applies when `verify is True`, never when it is an explicit path).

        `verify_certs=True`, `use_system_certs=True`: OS trust store via `ssl.get_default_verify_paths()`, which already reads
            `SSL_CERT_FILE` / `SSL_CERT_DIR` and falls back to compiled-in defaults.

            grpclib gets the full `DefaultVerifyPaths` and loads both `cafile` and `capath`. The result is additive (OS defaults plus any user env overrides).

            requests takes a single path. Default rule: `cafile or capath`. Override: when user sets `SSL_CERT_DIR` -> return `capath` instead,
                otherwise the OS-default cafile overrides it. This is the reason why resolver reads env vars even though `get_default_verify_paths()`
                already does it behind the scene.

            On systems with no usable trust store (distroless) -> warn and fall back to certifi for both transports.
        """
        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
            return CVTLSSettings(grpc_ssl=context, requests_verify=False)

        if self._use_system_certs:
            verify_paths = ssl.get_default_verify_paths()
            user_set_capath_only = "SSL_CERT_DIR" in environ and "SSL_CERT_FILE" not in environ
            if user_set_capath_only and verify_paths.capath:
                return CVTLSSettings(grpc_ssl=verify_paths, requests_verify=verify_paths.capath)
            if path := (verify_paths.cafile or verify_paths.capath):
                return CVTLSSettings(grpc_ssl=verify_paths, requests_verify=path)
            # No usable OS trust store — warn and fall through to the certifi default.
            self._warn_no_system_trust_store()

        return CVTLSSettings(grpc_ssl=True, requests_verify=True)

    def _warn_no_system_trust_store(self) -> None:
        """Log a warning when `use_system_certs` was requested but no OS trust store was found."""
        LOGGER.warning(
            "CVClient: 'use_system_certs' is enabled but no system trust store was found "
            "(neither SSL_CERT_FILE/SSL_CERT_DIR nor OpenSSL's compiled-in default paths "
            "resolve to a readable file or directory). Falling back to the 'certifi' bundle for "
            "both gRPC and REST. To use the OS trust store, install a CA bundle package "
            "(e.g. 'ca-certificates') or set SSL_CERT_FILE / SSL_CERT_DIR explicitly."
        )

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
                verify=self._tls.requests_verify,
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
                headers={"Authorization": f"Bearer {self._token}", "User-Agent": self._get_user_agent()},
                verify=self._tls.requests_verify,
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

    def _get_user_agent(self) -> str:
        """
        Build a user agent string with enriched version information.

        Format: python/x.y.z pyavd/x.y.z aristaproto/x.y.z grpclib/x.y.z python-socks/x.y.z requests/x.y.z
        """
        user_agent_parts: list[str] = []

        # Process Python version
        if python_version := platform.python_version():
            user_agent_parts.append(f"python/{python_version}")

        # Process pyavd version
        try:
            pyavd_version = version("pyavd")
        # Fallback to __version__ avoiding cyclic import
        except PackageNotFoundError:
            pyavd_version = getattr(sys.modules.get("pyavd"), "__version__", None)

        if pyavd_version:
            user_agent_parts.append(f"pyavd/{pyavd_version}")

        # Process optional Python dependencies
        for dependent_package in ["aristaproto", "grpclib", "python-socks", "requests"]:
            try:
                user_agent_parts.append(f"{dependent_package}/{version(dependent_package)}")
            except PackageNotFoundError:  # noqa: PERF203
                continue

        return " ".join(user_agent_parts)


class CVClient(CVClientProtocol):
    def __init__(
        self,
        servers: str | list[str],
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify_certs: bool = True,
        use_system_certs: bool = False,
        proxy_host: str | None = None,
        proxy_port: int = 8080,
        proxy_username: str | None = None,
        proxy_password: str | None = None,
        grpc_channel_configuration: CVGRPCChannelConfiguration | None = None,
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
            use_system_certs: Use system certificate and honor overrides with `SSL_CERT_FILE` and
                `SSL_CERT_DIR`. Prefer the OS trust store over the bundled `certifi` Python package
                (certifi is only used as a fallback when the OS provides no usable trust store).
                Applied to both the gRPC channel and the REST calls. Ignored when `verify_certs=False`.
            proxy_host: HTTP proxy hostname.
            proxy_port: HTTP proxy port.
            proxy_username: Proxy authentication username.
            proxy_password: Proxy authentication password.
            grpc_channel_configuration: Optional gRPC channel configuration settings.
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
        self._use_system_certs = use_system_certs
        self._grpc_channel_configuration = grpc_channel_configuration
        self._proxy_manager = None
        # Resolve TLS settings.
        self._tls = self._resolve_tls_settings()

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
