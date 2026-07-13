# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import json
from asyncio.exceptions import TimeoutError as AsyncioTimeoutError
from hashlib import sha1
from logging import getLogger
from os import environ
from pathlib import Path
from typing import TYPE_CHECKING, NoReturn

from grpclib import GRPCError, Status
from grpclib.exceptions import ProtocolError, StreamTerminatedError

from pyavd._cv.workflows.models import AvdDevice, CVDevice
from pyavd._utils import get_v2

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


def mocked_cvdevices(hostnames: list[str] | None = None, device_count: int | None = None) -> list[CVDevice]:
    """
    Generate mocked CVDevice instances.

    Parameters:
        hostnames (list[str]): List of device hostnames.
        device_count (int): Number of CVDevice instances to generate.

    Returns:
        list[CVDevice]: List of CVDevice instances.
    """
    if hostnames:
        return [CVDevice(avd_device=AvdDevice(hostname=item)) for item in hostnames]
    if device_count:
        return [CVDevice(avd_device=AvdDevice(hostname=str(item), serial_number=str(item), system_mac_address=str(item))) for item in range(device_count)]
    return [CVDevice(avd_device=AvdDevice(hostname=str(item), serial_number=str(item), system_mac_address=str(item))) for item in range(1000000)]


def get_recording_file(route: str, request: IProtoMessage, cv_server: str, recording_dir: Path = RECORDING_DIR) -> Path:
    digest = sha1(str(request).encode("UTF-8"), usedforsecurity=False).hexdigest()
    recording_file = recording_dir / Path(route.strip("/")) / cv_server / f"{digest}.json"
    LOGGER.debug("get_recording_file:\nRoute: '%s'\nRequest: '%s'\nRecording file: '%s'", route, request, recording_file)
    if environ.get("RECORDING"):
        recording_file.parent.mkdir(parents=True, exist_ok=True)
    return recording_file


def _serialize_exception(e: Exception) -> str:
    """Serialize a known exception raised by the grpclib to a JSON string for recording."""
    # non-OK gRPC status (e.g. NOT_FOUND, UNAVAILABLE)
    if isinstance(e, GRPCError):
        raise_dict = {"type": "GRPCError", "status": str(e.args[0]).removeprefix("Status."), "message": e.args[1]}
    # RST_STREAM from server, TCP connection lost, GOAWAY frame, or HTTP/2 protocol error.
    elif isinstance(e, StreamTerminatedError):
        raise_dict = {"type": "StreamTerminatedError", "message": e.args[0]}
    # Local grpc-timeout deadline expired
    elif isinstance(e, AsyncioTimeoutError):
        raise_dict = {"type": "AsyncioTimeoutError", "message": e.args[0]}
    # Client code violated the gRPC protocol (e.g. double recv, send after end).
    elif isinstance(e, ProtocolError):
        raise_dict = {"type": "ProtocolError", "message": e.args[0]}
    # Unknown/new exception - serialize dynamically.
    else:
        raise_dict = {"type": type(e).__name__}
        if e.args:
            raise_dict["message"] = e.args[0]
    return json.dumps({"raise": raise_dict}, indent=4)


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
    LOGGER.info("recording_unary_unary: Recording API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    try:
        result = await self._org_unary_unary(route, request, response_type, timeout=timeout, deadline=deadline, metadata=metadata)
    # Catch returned gRPC Exception (like Workspace is not found, etc.)
    except Exception as e:
        LOGGER.debug("recording_unary_unary: Got exception executing request '%s': %s", request, e)
        # Dump exception details into the recording file so that it can be easily replayed
        recording_file.write_text(_serialize_exception(e))
        # Re-raise exception so that it is passed to and processed by our gRPC decorator
        raise
    else:
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
    LOGGER.info("recording_unary_stream: Recording API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    messages_as_json = []
    exception_only = False
    try:
        async for message in self._org_unary_stream(route, request, response_type, timeout=timeout, deadline=deadline, metadata=metadata):
            messages_as_json.append(message.to_json(indent=4))
            yield message
    # Catch returned gRPC Exception
    except Exception as e:
        LOGGER.debug("recording_unary_stream: Got exception executing request '%s': %s", request, e)
        # If no messages were yet recorded - just dump exception details into the recording file so that exception can be re-raised.
        if not messages_as_json:
            recording_file.write_text(_serialize_exception(e))
            exception_only = True
        # If some messages were already recorded - dump exception into the list of messages.
        else:
            messages_as_json.append(_serialize_exception(e))
        # Re-raise exception so that it is passed to and processed by our gRPC decorator
        raise
    finally:
        if not exception_only:
            # Write messages together with stringified exception if some messages were recorded prior to exception
            if messages_as_json:
                recording_file.write_text(f"[{', '.join(messages_as_json)}]")
            # No messages were received. Write an empty list
            else:
                recording_file.write_text("[]")


async def playback_unary_unary(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    **_kwargs: Any,
) -> T_Message:
    LOGGER.info("playback_unary_unary: Playing back recording for API request: %s", request)
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
    LOGGER.info("playback_unary_stream: Playing back recording for API request: %s", request)
    recording_file = get_recording_file(route, request, cv_server=self.channel._host)
    if not recording_file.exists():
        raise FileNotFoundError(recording_file, "for request", request)
    recording = recording_file.read_text()
    for message_as_dict in json.loads(recording):
        yield response_type.from_dict(message_as_dict)


# General recordings are those that are natively received from CV and dumped as is.
# Static recordings are the same recordings but wrapped into 'payload' and 'raise'
# that are used during the tests like in mockery.py::playback_static_recording_unary_stream.
# These static recordings are not updated/impacted by RECORDING env var and must be changed manually (when needed).
async def playback_static_recording_unary_unary(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    **_kwargs: Any,
) -> T_Message:
    LOGGER.info("playback_static_recording_unary_unary: Playing back static recording for API request: %s", request)
    recording_dir = Path(__file__).parent / "mocked_api_recordings"
    recording_file = get_recording_file(route, request, cv_server=self.channel._host, recording_dir=recording_dir)
    if not recording_file.exists():
        raise FileNotFoundError(recording_file, "for request", request)
    recording = json.loads(recording_file.read_text())
    if recorded_exception := get_v2(recording, "raise"):
        raise_recorded_exception(recorded_exception)
    return response_type().from_dict(recording["payload"])


async def playback_static_recording_unary_stream(
    self: ServiceStub,
    route: str,
    request: IProtoMessage,
    response_type: type[T_Message],
    **_kwargs: Any,
) -> AsyncIterator[T_Message]:
    LOGGER.info("playback_static_recording_unary_stream: Playing back static recording for API request: %s", request)
    recording_dir = Path(__file__).parent / "mocked_api_recordings"
    recording_file = get_recording_file(route, request, cv_server=self.channel._host, recording_dir=recording_dir)
    if not recording_file.exists():
        raise FileNotFoundError(recording_file, "for request", request)
    recording = json.loads(recording_file.read_text())
    # Raise if recording file only contains exception
    if recorded_exception := get_v2(recording, "raise"):
        raise_recorded_exception(recorded_exception)
    # Replay messages
    for message_as_dict in recording["payload"]:
        # If exception was sent between messages during recording - raise it the same way it was raised during recording
        if recorded_exception := get_v2(message_as_dict, "raise"):
            raise_recorded_exception(recorded_exception)
        yield response_type().from_dict(message_as_dict)


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
    self._metadata = {}
    return self


# Helper function to raise exception based on the previously recorded (in a form of stringified json) exception
def raise_recorded_exception(recorded_exception: dict[str, Any]) -> None:
    exception_type = get_v2(recorded_exception, "type")
    exception_status = get_v2(recorded_exception, "status")
    exception_message = get_v2(recorded_exception, "message")

    match exception_type:
        case "GRPCError":
            raise GRPCError(Status[exception_status], exception_message)
        case "StreamTerminatedError":
            raise StreamTerminatedError(exception_message)
        case "AsyncioTimeoutError":
            raise AsyncioTimeoutError(exception_message)
        case "ProtocolError":
            raise ProtocolError(exception_message)
        case _:
            msg = f"Unknown recorded exception type '{exception_type}'"
            if exception_message:
                msg += f": {exception_message}"
            msg += ". Update mockery.py."
            raise NotImplementedError(msg)
