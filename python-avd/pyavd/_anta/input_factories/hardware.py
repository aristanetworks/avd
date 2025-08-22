# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower

from ._base_classes import AntaTestInputFactory


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyEnvironmentCooling` test."""

    def create(self) -> list[VerifyEnvironmentCooling.Input] | None:
        """Create a list of inputs for the `VerifyEnvironmentCooling` test."""
        return [VerifyEnvironmentCooling.Input(states=["ok"])]


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyEnvironmentPower` test."""

    def create(self) -> list[VerifyEnvironmentPower.Input] | None:
        """Create a list of inputs for the `VerifyEnvironmentPower` test."""
        return [VerifyEnvironmentPower.Input(states=["ok"])]
