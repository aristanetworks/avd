# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.routing.generic import VerifyRoutingProtocolModel

from ._base_classes import AntaTestInputFactory


class VerifyRoutingProtocolModelInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyRoutingProtocolModel` test.

    The test input `model` is collected from the value of `service_routing_protocols_model`
    of the device structured config.
    """

    def create(self) -> list[VerifyRoutingProtocolModel.Input] | None:
        """Create a list of inputs for the `VerifyRoutingProtocolModel` test."""
        model = self.structured_config.service_routing_protocols_model
        return [VerifyRoutingProtocolModel.Input(model=model)] if model else None
