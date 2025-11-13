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
    Input factory class for the `VerifyEnvironmentPower` test.

    Generates test inputs for verifying the following:
    - If no hardware requirements provided:
        * By default, this test checks that all slots for the following component types
    are populated: **power supply**, **fan tray**, **fabric card**,
    **line card** and **supervisor**.
    - If specific requirements provided:
        * Strictly check that all provided slots are filled.
    """

    def create(self) -> list[VerifyInventory.Input] | None:
        """Create a list of inputs for the `VerifyInventory` test."""
        if not (hardware_requirements := self.structured_config.metadata.hardware_requirements):
            return [VerifyInventory.Input()]

        input_req = HardwareInventory(
            power_supplies=hardware_requirements.min_power_supplies,
            fan_trays=hardware_requirements.min_fans,
            fabric_cards=hardware_requirements.min_fabric_cards,
            line_cards=hardware_requirements.min_line_cards,
            supervisors=hardware_requirements.min_supervisors,
        )
        return [VerifyInventory.Input(requirements=input_req)]
