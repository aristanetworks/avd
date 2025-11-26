# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from hashlib import sha1
from logging import getLogger
from os import environ
from pathlib import Path
from typing import TYPE_CHECKING, NoReturn

if TYPE_CHECKING:
    from collections.abc import AsyncIterator
    from typing import Any, TypeVar

    from aristaproto import Message
    from aristaproto.grpc.grpclib_client import MetadataLike, ServiceStub
    from grpclib._typing import IProtoMessage
    from grpclib.metadata import Deadline

    from pyavd._cv.client import CVClient

    T_Message = TypeVar("T_Message", bound=Message)

LOGGER = getLogger(__name__)
RECORDING_DIR = Path(__file__).parent / "api_recordings"


def get_recording_file(route: str, request: IProtoMessage, cv_server: str) -> Path:
    digest = sha1(str(request).encode("UTF-8"), usedforsecurity=False).hexdigest()
    recording_file = RECORDING_DIR / Path(route.strip("/")) / cv_server / f"{digest}.json"
    if environ.get("RECORDING"):
        recording_file.parent.mkdir(parents=True, exist_ok=True)
    return recording_file


async def recording_unary_unary(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    *,
    timeout: float | None = None,
    deadline: Deadline | None = None,
    metadata: MetadataLike | None = None,
) -> T_Message:
    LOGGER.info("Recording API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    result = await self._org_unary_unary(route, request, response_type, timeout=timeout, deadline=deadline, metadata=metadata)
    recording_file.write_text(result.to_json(indent=4))
    return result


async def recording_unary_stream(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    *,
    timeout: float | None = None,
    deadline: Deadline | None = None,
    metadata: MetadataLike | None = None,
) -> AsyncIterator[T_Message]:
    LOGGER.info("Recording API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    messages_as_json = []
    async for message in self._org_unary_stream(route, request, response_type, timeout=timeout, deadline=deadline, metadata=metadata):
        messages_as_json.append(message.to_json(indent=4))
        yield message

    result = f"[{', '.join(messages_as_json)}]"
    recording_file.write_text(result)


async def playback_unary_unary(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    **_kwargs: Any,
) -> T_Message:
    LOGGER.info("Playing back recording for API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    if not recording_file.exists():
        raise FileNotFoundError(recording_file, "for request", request)
    recording = recording_file.read_text()
    return response_type().from_json(recording)


async def playback_unary_stream(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    **_kwargs: Any,
) -> AsyncIterator[T_Message]:
    LOGGER.info("Playing back recording for API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    if not recording_file.exists():
        raise FileNotFoundError(recording_file, "for request", request)
    recording = recording_file.read_text()
    for message_as_dict in json.loads(recording):
        yield response_type().from_pydict(message_as_dict)


async def mocked_cv_client_aenter(self: CVClient) -> CVClient:
    class MockedChannel:
        def close(self) -> None:
            pass

        def request(self, *_args: tuple[Any, ...], **_kwargs: dict[str, Any]) -> NoReturn:
            msg = (
                "The MockedChannel instance was called from the regular ServiceStub which should never happen. "
                "Something went wrong with patching the aristaproto.ServiceStub."
            )
            raise NotImplementedError(msg)

    self._channel = MockedChannel()
    self._channel._host = self._servers[0]
    self._cv_version = None
    self._metadata = {}
    return self
