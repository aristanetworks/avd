# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ssl

try:
    from grpclib.client import Channel
except ImportError:
    HAS_GRPCLIB = False
else:
    HAS_GRPCLIB = True

from .change_control import ChangeControlMixin
from .configlet import ConfigletMixin
from .inventory import InventoryMixin
from .studio import StudioMixin
from .tag import TagMixin
from .utils import UtilsMixin
from .workspace import WorkspaceMixin


class CVClient(
    ChangeControlMixin,
    ConfigletMixin,
    InventoryMixin,
    StudioMixin,
    TagMixin,
    UtilsMixin,
    WorkspaceMixin,
):
    _channel: Channel | None = None
    _metadata: dict
    _servers: list[str]
    _port: int
    _verify_certs: bool
    _token: str

    def __init__(self, servers: str | list[str], token: str, port: int = 443, verify_certs: bool = True) -> None:
        """
        CVClient is a high-level API library for using CloudVision Resource APIs.

        Use CVClient as an async context manager like:
            `async with CVClient(servers="myserver", token="mytoken") as cv_client:`

        Parameters:
            servers: A single FQDN for CVaaS or a list of FQDNs for one CVP cluster.
            token: Token defined in CloudVision under service-accounts.
            port: TCP port to use for the connection.
            verify_certs: Disables SSL certificate verification if set to False. Not recommended for production.
        """
        if isinstance(servers, list):
            self._servers = servers
        else:
            self._servers = [servers]

        self._port = port
        self._token = token
        self._verify_certs = verify_certs
        self._metadata = {"authorization": "Bearer " + self._token}

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
        if not self._verify_certs:
            context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
            context.check_hostname = False
            context.set_alpn_protocols(["h2"])
            context.verify_mode = ssl.CERT_NONE
        else:
            context = True

        if self._channel is None:
            self._channel = Channel(host=self._servers[0], port=self._port, ssl=context)
