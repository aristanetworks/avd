# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.mlag import VerifyMlagDualPrimary, VerifyMlagReloadDelay

from ._base_classes import AntaTestInputFactory


class VerifyMlagDualPrimaryInputFactory(AntaTestInputFactory):
    """Input factory class for the `VerifyMlagDualPrimary` test."""

    def create(self) -> list[VerifyMlagDualPrimary.Input] | None:
        """Create a list of inputs for the `VerifyMlagDualPrimary` test."""
        if self.structured_config.mlag_configuration.dual_primary_detection_delay is None:
            return None

        return [
            VerifyMlagDualPrimary.Input(
                detection_delay=self.structured_config.mlag_configuration.dual_primary_detection_delay,
                errdisabled=True,
                recovery_delay=self.structured_config.mlag_configuration.dual_primary_recovery_delay_mlag or 0,
                recovery_delay_non_mlag=self.structured_config.mlag_configuration.dual_primary_recovery_delay_non_mlag or 0,
            )
        ]


class VerifyMlagReloadDelayInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyMlagReloadDelay` test.

    The test inputs `reload_delay` and `reload_delay_non_mlag` are collected from
    the values of `mlag_configuration.reload_delay_mlag` and `mlag_configuration.reload_delay_non_mlag`
    of the device structured config.
    """

    def create(self) -> list[VerifyMlagReloadDelay.Input] | None:
        """Create a list of inputs for the `VerifyMlagReloadDelay` test."""
        if self.structured_config.mlag_configuration.reload_delay_mlag is None or self.structured_config.mlag_configuration.reload_delay_non_mlag is None:
            return None

        return [
            VerifyMlagReloadDelay.Input(
                reload_delay=self.structured_config.mlag_configuration.reload_delay_mlag,
                reload_delay_non_mlag=self.structured_config.mlag_configuration.reload_delay_non_mlag,
            )
        ]
