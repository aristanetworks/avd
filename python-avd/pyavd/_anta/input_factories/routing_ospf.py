# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.routing.ospf import VerifyOSPFMaxLSA, VerifyOSPFNeighborState

from pyavd._anta.constants import StructuredConfigKey

from ._base_classes import AntaTestInputFactory
from ._decorators import skip_if_missing_config

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyOSPFMaxLSAInputFactory(AntaTestInputFactory[VerifyOSPFMaxLSA.Input]):
    """
    Input factory class for the `VerifyOSPFMaxLSA` test.

    Generate the test inputs only if `router_ospf` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.ROUTER_OSPF)
    def create(self) -> Iterator[VerifyOSPFMaxLSA.Input]:
        yield VerifyOSPFMaxLSA.Input()


class VerifyOSPFNeighborStateInputFactory(AntaTestInputFactory[VerifyOSPFNeighborState.Input]):
    """
    Input factory class for the `VerifyOSPFNeighborState` test.

    Generate the test inputs only if `router_ospf` is configured.
    """

    @skip_if_missing_config(StructuredConfigKey.ROUTER_OSPF)
    def create(self) -> Iterator[VerifyOSPFNeighborState.Input]:
        yield VerifyOSPFNeighborState.Input()
