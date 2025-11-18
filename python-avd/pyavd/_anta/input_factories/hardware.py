# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Literal

from anta.input_models.hardware import HardwareInventory
from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyInventory, VerifyTransceiversManufacturers

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


class VerifyInventoryInputFactory(AntaTestInputFactory[VerifyInventory.Input]):
    """
    Input factory class for the `VerifyInventory` test.

    Generates test inputs for verifying the following:
    - If no hardware requirements provided:
        * By default, this test checks that all slots for the following component types
    are populated: `power supply`, `fan tray`, `fabric card`, `line card` and `supervisor`.
    - If specific requirements provided:
        * If the specified requirement is set to 0, the test skips the check. Otherwise, it strictly verifies that all provided slots are filled.
    """

    def _get_hardware_requirement(self, requirement: int | None) -> int | Literal["all"] | None:
        """Helper to determine the hardware requirements."""
        # Returns "all" if requirement is None, None If requirement == 0. Otherwise, returns the requirement.
        if requirement is None:
            return "all"
        if requirement == 0:
            return None
        return requirement

    def create(self) -> list[VerifyInventory.Input] | None:
        """Create a list of inputs for the `VerifyInventory` test."""
        if not (hardware_requirements := self.structured_config.metadata.hardware_requirements):
            return [VerifyInventory.Input()]

        input_req = HardwareInventory(
            power_supplies=self._get_hardware_requirement(hardware_requirements.min_power_supplies),
            fan_trays=self._get_hardware_requirement(hardware_requirements.min_fans),
            fabric_cards=self._get_hardware_requirement(hardware_requirements.min_fabric_cards),
            line_cards=self._get_hardware_requirement(hardware_requirements.min_line_cards),
            supervisors=self._get_hardware_requirement(hardware_requirements.min_supervisors),
        )
        return [VerifyInventory.Input(requirements=input_req)]
