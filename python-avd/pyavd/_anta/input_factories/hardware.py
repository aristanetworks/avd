# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyTransceiversManufacturers

from ._base_classes import AntaTestInputFactory


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory[VerifyEnvironmentCooling.Input]):
    """Input factory class for the `VerifyEnvironmentCooling` test."""

    def create(self) -> list[VerifyEnvironmentCooling.Input] | None:
        """Create a list of inputs for the `VerifyEnvironmentCooling` test."""
        return [VerifyEnvironmentCooling.Input(states=["ok"])]


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory[VerifyEnvironmentPower.Input]):
    """Input factory class for the `VerifyEnvironmentPower` test."""

    def create(self) -> list[VerifyEnvironmentPower.Input] | None:
        """Create a list of inputs for the `VerifyEnvironmentPower` test."""
        return [VerifyEnvironmentPower.Input(states=["ok"])]


class VerifyTransceiversManufacturersInputFactory(AntaTestInputFactory[VerifyTransceiversManufacturers.Input]):
    """
    Input factory class for the `VerifyTransceiversManufacturers` test.

    Generates test inputs to verify transceivers are from approved manufacturers. Uses
    `hardware_requirements.transceiver_manufacturers` from metadata, defaulting to
    ['Arista Networks', 'Arastra, Inc.'] if not specified.
    """

    def create(self) -> list[VerifyTransceiversManufacturers.Input] | None:
        """Create a list of inputs for the `VerifyTransceiversManufacturers` test."""
        return [VerifyTransceiversManufacturers.Input(manufacturers=list(self.structured_config.metadata.hardware_requirements.transceiver_manufacturers))]
