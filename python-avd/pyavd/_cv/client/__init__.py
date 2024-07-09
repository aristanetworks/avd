# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl

from grpclib.client import Channel
from requests import JSONDecodeError, post

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .exceptions import CVClientException
from .inventory import InventoryMixin
from .studio import StudioMixin
from .swg import SwgMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .workspace import WorkspaceMixin


class CVClient(
    ChangeControlMixin,
    ConfigletMixin,
    InventoryMixin,
    StudioMixin,
    SwgMixin,
    TagMixin,
    UtilsMixin,
    WorkspaceMixin,
):
    _channel: Channel | None = None
    _metadata: dict
    _servers: list[str]
    _port: int
    _verify_certs: bool
    _token: str | None
    _username: str | None
    _password: str | None

    def __init__(
        self,
        servers: str | list[str],
        token: str | None = None,
        username: str | None = None,
        password: str | None = None,
        port: int = 443,
        verify_certs: bool = True,
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

    async def __aenter__(self) -> CVClient:
        """
        Using asynchronous context manager since grpclib must be initialized inside an asyncio loop.
        """
        self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        self._channel.close()
        self._channel = None

    def _connect(self) -> None:
        # TODO:
        # - Verify connection
        # - Handle multinode clusters
        # - Detect supported API versions and set instance properties accordingly.
        if not self._token:
            self._set_token()

        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.set_alpn_protocols(["h2"])
        else:
            context = True

        if self._channel is None:
            self._channel = Channel(host=self._servers[0], port=self._port, ssl=context)

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
            raise CVClientException("Unable to authenticate. Missing token or username/password.")

        if not self._verify_certs:
            # Accepting SonarLint issue: We are purposely implementing no verification of certs.
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)  # NOSONAR
            context.verify_mode = ssl.CERT_NONE  # NOSONAR
            context.check_hostname = False
        else:
            # None means default context which will verify certs.
            context = None

        try:
            response = post(
                "https://" + self._servers[0] + "/cvpservice/login/authenticate.do", auth=(self._username, self._password), verify=self._verify_certs, json={}
            )

            self._token = response.json()["sessionId"]
        except (KeyError, JSONDecodeError) as e:
            raise CVClientException("Unable to get token from CloudVision server. Please supply service account token instead of username/password.") from e
