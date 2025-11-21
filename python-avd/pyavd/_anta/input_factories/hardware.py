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

    Generates test inputs to verify that the expected quantity of hardware components are installed.
    Uses the `hardware_requirements.min_<component>` keys from metadata to define the requirements for each component.

    For each component:
      - Undefined (Default): Validate that all available slots are inserted.
      - Positive Integer: Validate that the number of components inserted is at least the specified minimum.
      - 0: Skip the validation for this specific component.
    """

    def _get_hardware_requirement(self, requirement: int | None) -> int | Literal["all"] | None:
        """
        Normalize a hardware requirement value.

        Args:
            requirement: The raw requirement value from metadata.

        Returns:
            "all" if the input is None (implies validating all available slots), None if the input is 0
            (implies skipping validation), otherwise the original requirement value.
        """
        if requirement is None:
            return "all"
        if requirement == 0:
            return None
        return requirement

    def create(self) -> list[VerifyInventory.Input] | None:
        """Create a list of inputs for the `VerifyInventory` test."""
        hardware_requirements = self.structured_config.metadata.hardware_requirements
        input_req = HardwareInventory(
            power_supplies=self._get_hardware_requirement(hardware_requirements.min_power_supplies),
            fan_trays=self._get_hardware_requirement(hardware_requirements.min_fans),
            fabric_cards=self._get_hardware_requirement(hardware_requirements.min_fabric_cards),
            line_cards=self._get_hardware_requirement(hardware_requirements.min_line_cards),
            supervisors=self._get_hardware_requirement(hardware_requirements.min_supervisors),
        )
        return [VerifyInventory.Input(requirements=input_req)]
