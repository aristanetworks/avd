# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.system import VerifyReloadCause

from ._base_classes import AntaTestInputFactory


class VerifyReloadCauseInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyReloadCause` test.

    The following EOS reload causes are allowed:
    - ZTP: "System reloaded due to Zero Touch Provisioning"
    - USER: "Reload requested by the user."
    - FPGA: "Reload requested after FPGA upgrade"
    """

    def create(self) -> list[VerifyReloadCause.Input] | None:
        """Create a list of inputs for the `VerifyReloadCause` test."""
        return [VerifyReloadCause.Input(allowed_causes=["USER", "FPGA", "ZTP"])]
