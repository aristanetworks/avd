# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.input_models.hardware import HardwareInventory
from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyInventory

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


class VerifyInventoryInputFactory(AntaTestInputFactory[VerifyInventory.Input]):
    """
    Input factory class for the `VerifyInventory` test.

    Generates test inputs for verifying the following:
    - If no hardware requirements provided:
        * By default, this test checks that all slots for the following component types
    are populated: `power supply`, `fan tray`, `fabric card`, `line card` and `supervisor`.
    - If specific requirements provided:
        * Strictly check that all provided slots are filled.
    """

    def create(self) -> list[VerifyInventory.Input] | None:
        """Create a list of inputs for the `VerifyInventory` test."""
        if not (hardware_requirements := self.structured_config.metadata.hardware_requirements):
            return [VerifyInventory.Input()]

        power_supply = hardware_requirements.min_power_supplies
        fans = hardware_requirements.min_fans
        fabric_cards = hardware_requirements.min_fabric_cards
        line_cards = hardware_requirements.min_line_cards
        supervisors = hardware_requirements.min_supervisors
        input_req = HardwareInventory(
            power_supplies="all" if power_supply is None else (None if power_supply == 0 else power_supply),
            fan_trays="all" if fans is None else (None if fans == 0 else fans),
            fabric_cards="all" if fabric_cards is None else (None if fabric_cards == 0 else fabric_cards),
            line_cards="all" if line_cards is None else (None if line_cards == 0 else line_cards),
            supervisors="all" if supervisors is None else (None if supervisors == 0 else supervisors),
        )
        return [VerifyInventory.Input(requirements=input_req)]
