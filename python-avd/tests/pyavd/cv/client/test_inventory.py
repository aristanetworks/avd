# Copyright (c) 2024-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from json import loads
from typing import TYPE_CHECKING

import pytest

from pyavd._cv.client.inventory import InventoryMixin

if TYPE_CHECKING:
    from pyavd._cv.api.arista.inventory.v1 import DeviceStreamRequest
    from pyavd._cv.client import CVClient


class _EmptyAsyncIterator:
    def __aiter__(self) -> _EmptyAsyncIterator:
        return self

    async def __anext__(self) -> None:
        raise StopAsyncIteration


class _RecordingDeviceServiceStub:
    request: DeviceStreamRequest | None = None
    timeout: float | None = None

    def get_all(self, request: DeviceStreamRequest, timeout: float) -> _EmptyAsyncIterator:
        self.request = request
        self.timeout = timeout
        return _EmptyAsyncIterator()


class _InventoryClient(InventoryMixin):
    def __init__(self) -> None:
        self.device_service_stub = _RecordingDeviceServiceStub()

    def new_stub(self, _stub_class: type) -> _RecordingDeviceServiceStub:
        return self.device_service_stub


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


@pytest.mark.asyncio
async def test_get_inventory_devices_only_sets_provided_filter_fields() -> None:
    cv_client = _InventoryClient()

    result = await cv_client.get_inventory_devices(
        [
            (None, None, "avd-ci-spine1"),
            ("serial-number", None, None),
            (None, "00:1c:73:00:00:01", None),
        ],
    )

    assert result == []
    assert cv_client.device_service_stub.request is not None
    filters = loads(cv_client.device_service_stub.request.to_json())["partialEqFilter"]
    assert filters == [
        {"hostname": "avd-ci-spine1"},
        {"key": {"deviceId": "serial-number"}},
        {"systemMacAddress": "00:1c:73:00:00:01"},
    ]
