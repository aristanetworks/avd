# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import _ssl
import platform
import socket
import ssl
import sys
from base64 import b64encode
from importlib.metadata import PackageNotFoundError, version
from logging import getLogger
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import TYPE_CHECKING, Any, Protocol, TypeVar

import grpc
from aristaproto.grpcio import ServiceStub
from grpc.aio import Channel, secure_channel
from requests import JSONDecodeError, get, post
from requests.exceptions import HTTPError, RequestException

from pyavd._cv.workflows.models import CVGRPCChannelConfiguration, CVGRPCProxyConfiguration

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .studio import StudioMixin
from .studio_topology import StudioTopologyMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .versioning import CvVersion
from .workspace import WorkspaceMixin

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import TracebackType

    from typing_extensions import Self


StubT = TypeVar("StubT", bound=ServiceStub)


class CVGRPCTransport:
    """Manage CloudVision gRPC channel lifecycle, credentials, and stub creation."""

    def __init__(
        self,
        *,
        servers: list[str],
        port: int,
        verify_certs: bool,
        configuration: CVGRPCChannelConfiguration,
        get_user_agent: Callable[[], str],
    ) -> None:
        self.servers = servers
        self.port = port
        self.verify_certs = verify_certs
        self.configuration = configuration
        self._get_user_agent = get_user_agent
        self._channel: Channel | None = None

    @property
    def channel(self) -> Channel:
        """Return the connected gRPC channel."""
        if self._channel is None:
            msg = "CloudVision gRPC channel is not connected."
            raise CVClientException(msg)

        return self._channel

    @property
    def channel_options(self) -> tuple[tuple[str, str | int], ...]:
        """Build grpcio Channel options from the typed gRPC channel configuration."""
        return self.configuration.as_grpcio_channel_options(default_user_agent=self._get_user_agent())

    @property
    def requests_proxies(self) -> dict[str, str] | None:
        """Build requests proxy configuration from the typed gRPC channel configuration."""
        if self.configuration.proxy is None:
            return None

        return self.configuration.proxy.get_requests_proxies()

    async def close(self) -> None:
        """Close the gRPC channel if connected."""
        if self._channel is not None:
            channel = self._channel
            self._channel = None
            await channel.close()

    def connect(self, token: str) -> None:
        """Create the gRPC channel if needed."""
        if self._channel is None:
            self._channel = secure_channel(
                target=f"{self.servers[0]}:{self.port}",
                credentials=self._channel_credentials(token),
                options=self.channel_options,
            )

    def new_stub(self, stub_type: type[StubT]) -> StubT:
        """Create a generated API service stub using the connected channel."""
        return stub_type(self.channel)

    def _channel_credentials(self, token: str) -> grpc.ChannelCredentials:
        """Build grpcio channel credentials from TLS and token authentication credentials."""
        return grpc.composite_channel_credentials(self._transport_credentials(), grpc.access_token_call_credentials(token))

    def _transport_credentials(self) -> grpc.ChannelCredentials:
        """Build grpcio transport credentials from the configured certificate verification behavior."""
        self.configuration._ssl_target_name_override = None

        if self.verify_certs:
            return grpc.ssl_channel_credentials()

        peer_certificate = self._get_server_certificate()
        self.configuration._ssl_target_name_override = self._get_server_certificate_target_name(peer_certificate)
        return grpc.ssl_channel_credentials(root_certificates=peer_certificate.encode())

    def _get_server_certificate(self) -> str:
        """Fetch the peer certificate directly or through the configured HTTP CONNECT proxy."""
        proxy = self.configuration.proxy
        if proxy is None:
            return ssl.get_server_certificate((self.servers[0], self.port))

        proxy_headers = [
            f"CONNECT {self.servers[0]}:{self.port} HTTP/1.1",
            f"Host: {self.servers[0]}:{self.port}",
        ]
        if proxy.username and proxy.password:
            credentials = f"{proxy.username}:{proxy.password}".encode()
            proxy_headers.append(f"Proxy-Authorization: Basic {b64encode(credentials).decode()}")

        proxy_request = "\r\n".join([*proxy_headers, "", ""]).encode()
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        with (
            socket.create_connection((proxy.host, proxy.port)) as proxy_socket,
            proxy_socket.makefile("rwb", buffering=0) as proxy_file,
        ):
            proxy_file.write(proxy_request)
            status_line = proxy_file.readline().decode(errors="replace")
            while proxy_file.readline() not in (b"\r\n", b""):
                pass
            if " 200 " not in status_line:
                msg = f"Failed to fetch CloudVision certificate through proxy: {status_line.strip()}"
                raise CVClientException(msg)

            with ssl_context.wrap_socket(proxy_socket, server_hostname=self.servers[0]) as tls_socket:
                certificate = tls_socket.getpeercert(binary_form=True)

        if certificate is None:
            msg = "Failed to fetch CloudVision certificate through proxy: no peer certificate returned."
            raise CVClientException(msg)

        return ssl.DER_cert_to_PEM_cert(certificate)

    def _get_server_certificate_target_name(self, certificate: str) -> str:
        """Return a certificate identity suitable for grpc.ssl_target_name_override."""
        decoded_certificate = self._decode_certificate(certificate)

        subject_alt_names = decoded_certificate.get("subjectAltName", ())
        for target_name_type in ("DNS", "IP Address"):
            for subject_alt_name_type, subject_alt_name_value in subject_alt_names:
                if subject_alt_name_type == target_name_type:
                    return subject_alt_name_value

        for relative_distinguished_name in decoded_certificate.get("subject", ()):
            for attribute_name, attribute_value in relative_distinguished_name:
                if attribute_name == "commonName":
                    return attribute_value

        msg = "Unable to determine certificate identity for grpc.ssl_target_name_override."
        raise CVClientException(msg)

    @staticmethod
    def _decode_certificate(certificate: str) -> dict[str, Any]:
        """Decode a PEM certificate using the same parser as Python's ssl certificate helpers."""
        test_decode_cert = getattr(_ssl, "_test_decode_cert", None)
        if test_decode_cert is None:
            msg = "Unable to decode CloudVision certificate: Python ssl certificate decoder is unavailable."
            raise CVClientException(msg)

        with TemporaryDirectory() as temporary_directory:
            certificate_path = Path(temporary_directory, "certificate.pem")
            certificate_path.write_text(certificate, encoding="utf-8")
            return test_decode_cert(str(certificate_path))


LOGGER = getLogger(__name__)


class CVClientProtocol(
    ChangeControlMixin,
    ConfigletMixin,
    InventoryMixin,
    StudioMixin,
    StudioTopologyMixin,
    SwgMixin,
    TagMixin,
    WorkspaceMixin,
    UtilsMixin,
    Protocol,
):
    """Protocol for the CVClient class."""

    _servers: list[str]
    _verify_certs: bool
    _use_system_certs: bool
    _token: str | None
    _username: str | None
    _password: str | None
    _cv_version: CvVersion | None = None
    grpc: CVGRPCTransport

    def new_stub(self, stub_type: type[StubT]) -> StubT:
        """Create a generated API service stub using the connected channel."""
        return self.grpc.new_stub(stub_type)

    @property
    def _requests_proxies(self) -> dict[str, str] | None:
        """Build requests proxy configuration from the gRPC transport configuration."""
        return self.grpc.requests_proxies

    async def __aenter__(self) -> Self:
        """Using asynchronous context manager since grpcio aio channels must be initialized inside an asyncio loop."""
        await self._connect()
        return self

    async def __aexit__(self, _exc_type: type[BaseException] | None, _exc_val: BaseException | None, _exc_tb: TracebackType | None) -> None:
        await self.grpc.close()

    async def _connect(self) -> None:
        # TODO: Verify connection
        # TODO: Handle multinode clusters

        token = self._get_token()

        self._init_version()

        self.grpc.connect(token)

    def _get_token(self) -> str:
        """
        Uses username/password for authenticating via REST.

        Returns the session token to be used for the gRPC channel.

        TODO: Handle multinode clusters
        """
        if self._token:
            return self._token

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
            token = response.json()["sessionId"]
        except (KeyError, TypeError, JSONDecodeError) as e:
            msg = "Unable to get token from CloudVision server. Please supply service account token instead of username/password."
            raise CVClientException(msg) from e

        if not isinstance(token, str) or not token:
            msg = "Unable to get token from CloudVision server. Received an invalid session token."
            raise CVClientException(msg)

        self._token = token
        return token

    def _init_version(self) -> None:
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

    def _get_user_agent(self) -> str:
        """
        Build a user agent string with enriched version information.

        Format: python/x.y.z pyavd/x.y.z aristaproto/x.y.z grpcio/x.y.z requests/x.y.z
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
        for dependent_package in ["aristaproto", "grpcio", "requests"]:
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
            use_system_certs: Use system certificates and honor overrides with `SSL_CERT_FILE` and
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

        self._token = token
        self._username = username
        self._password = password
        self._verify_certs = verify_certs
        grpc_channel_configuration = grpc_channel_configuration or CVGRPCChannelConfiguration()

        # Normalize legacy proxy arguments into the typed gRPC channel configuration.
        if proxy_host is not None:
            if grpc_channel_configuration.proxy is not None:
                msg = "Cannot set both legacy proxy_* arguments and grpc_channel_configuration.proxy."
                raise ValueError(msg)

            grpc_channel_configuration.proxy = CVGRPCProxyConfiguration(
                host=proxy_host,
                port=proxy_port,
                username=proxy_username,
                password=proxy_password,
            )

        self.grpc = CVGRPCTransport(
            servers=self._servers,
            port=port,
            verify_certs=verify_certs,
            configuration=grpc_channel_configuration,
            get_user_agent=self._get_user_agent,
        )
