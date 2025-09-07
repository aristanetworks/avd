# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from logging import getLogger
from os import environ
from typing import TYPE_CHECKING
from unittest.mock import patch

import aristaproto
import pytest
import pytest_asyncio

from pyavd._cv.client import CVClient
from tests.pyavd.cv.mockery import mocked_cv_client_aenter, playback_unary_stream, playback_unary_unary, recording_unary_stream, recording_unary_unary

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

LOGGER = getLogger(__name__)

# Environment variables
# TODO: avoid having a default server and instead run tests to all recorded servers in offline mode.
CV_SERVER = environ.get("CV_SERVER") or "www.cv-prod-us-central1-c.arista.io"
CV_TOKEN = environ.get("CV_ACCESS_TOKEN")
RECORDING = environ.get("RECORDING")


@pytest_asyncio.fixture
async def cv_client() -> AsyncGenerator[CVClient, None]:
    """
    Instance of CVClient.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is not set,
    this will return a proper instance of CVClient connected to CloudVision with the token.

    If CV_ACCESS_TOKEN environment variable is set, but RECORDING environment variable is set,
    this will return an instance of CVClient connected to CloudVision with the token where all API calls will be recorded.

    Otherwise this will return an instance of CVClient where API calls are mocked using previously recorded API messages.
    """
    if CV_SERVER and CV_TOKEN:
        LOGGER.info("Running in online mode connecting to %s.", CV_SERVER)
        if RECORDING:
            LOGGER.info("Mocking ServiceStub to RecordingServiceStub")
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = recording_unary_unary
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = recording_unary_stream
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

            aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
            aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream

        else:
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

    else:
        LOGGER.info("Mocking ServiceStub to MockedServiceStub")
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._unary_stream
        aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = playback_unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = playback_unary_stream
        with patch("pyavd._cv.client.CVClient.__aenter__", new=mocked_cv_client_aenter):
            async with CVClient(servers=CV_SERVER, token=CV_TOKEN) as cv_client:
                yield cv_client

        aristaproto.grpc.grpclib_client.ServiceStub._unary_unary = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_unary
        aristaproto.grpc.grpclib_client.ServiceStub._unary_stream = aristaproto.grpc.grpclib_client.ServiceStub._org_unary_stream
        return


@pytest.mark.asyncio
async def test_get_inventory_devices(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices()
    assert len(result) > 0


@pytest.mark.asyncio
async def test_get_inventory_devices_with_filter(cv_client: CVClient) -> None:
    result = await cv_client.get_inventory_devices([(None, None, "avd-ci-spine1")])
    assert len(result) == 1
    assert hasattr(result[0], "hostname")
    assert result[0].hostname == "avd-ci-spine1"
