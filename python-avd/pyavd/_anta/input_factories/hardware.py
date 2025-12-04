# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from anta.input_models.hardware import HardwareInventory
from anta.tests.hardware import (
    VerifyEnvironmentCooling,
    VerifyEnvironmentPower,
    VerifyEnvironmentSystemCooling,
    VerifyInventory,
    VerifyTemperature,
    VerifyTransceiversManufacturers,
    VerifyTransceiversTemperature,
)

from ._base_classes import AntaTestInputFactory
from ._decorators import skip_if_hardware_validation_disabled

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory[VerifyEnvironmentCooling.Input]):
    """Input factory class for the `VerifyEnvironmentCooling` test."""

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyEnvironmentCooling.Input]:
        """Generate the inputs for the `VerifyEnvironmentCooling` test."""
        yield VerifyEnvironmentCooling.Input(states=["ok"])


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory[VerifyEnvironmentPower.Input]):
    """Input factory class for the `VerifyEnvironmentPower` test."""

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyEnvironmentPower.Input]:
        """Generate the inputs for the `VerifyEnvironmentPower` test."""
        yield VerifyEnvironmentPower.Input(states=["ok"])


class VerifyEnvironmentSystemCoolingInputFactory(AntaTestInputFactory[VerifyEnvironmentSystemCooling.Input]):
    """Input factory class for the `VerifyEnvironmentSystemCooling` test."""

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyEnvironmentSystemCooling.Input]:
        """Generate the inputs for the `VerifyEnvironmentSystemCooling` test."""
        yield VerifyEnvironmentSystemCooling.Input()


class VerifyTemperatureInputFactory(AntaTestInputFactory[VerifyTemperature.Input]):
    """Input factory class for the `VerifyTemperature` test."""

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyTemperature.Input]:
        """Generate the inputs for the `VerifyTemperature` test."""
        yield VerifyTemperature.Input()


class VerifyTransceiversTemperatureInputFactory(AntaTestInputFactory[VerifyTransceiversTemperature.Input]):
    """Input factory class for the `VerifyTransceiversTemperature` test."""

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyTransceiversTemperature.Input]:
        """Generate the inputs for the `VerifyTransceiversTemperature` test."""
        yield VerifyTransceiversTemperature.Input()


class VerifyTransceiversManufacturersInputFactory(AntaTestInputFactory[VerifyTransceiversManufacturers.Input]):
    """
    Input factory class for the `VerifyTransceiversManufacturers` test.

    Generates test inputs to verify transceivers are from approved manufacturers. Uses
    `validate_hardware.transceiver_manufacturers` from metadata, defaulting to
    ['Arista Networks', 'Arastra, Inc.'] if not specified.
    """

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyTransceiversManufacturers.Input]:
        """Generate the inputs for the `VerifyTransceiversManufacturers` test."""
        yield VerifyTransceiversManufacturers.Input(manufacturers=list(self.structured_config.metadata.validate_hardware.transceiver_manufacturers))


class VerifyInventoryInputFactory(AntaTestInputFactory[VerifyInventory.Input]):
    """
    Input factory class for the `VerifyInventory` test.

    Generates test inputs to verify that the expected quantity of hardware components are installed.
    Uses the `validate_hardware.min_<component>` keys from metadata to define the requirements for each component.

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

    @skip_if_hardware_validation_disabled
    def create(self) -> Iterator[VerifyInventory.Input]:
        """Generate the inputs for the `VerifyInventory` test."""
        validate_hardware = self.structured_config.metadata.validate_hardware
        input_req = HardwareInventory(
            power_supplies=self._get_hardware_requirement(validate_hardware.min_power_supplies),
            fan_trays=self._get_hardware_requirement(validate_hardware.min_fans),
            fabric_cards=self._get_hardware_requirement(validate_hardware.min_fabric_cards),
            line_cards=self._get_hardware_requirement(validate_hardware.min_line_cards),
            supervisors=self._get_hardware_requirement(validate_hardware.min_supervisors),
        )
        yield VerifyInventory.Input(requirements=input_req)
