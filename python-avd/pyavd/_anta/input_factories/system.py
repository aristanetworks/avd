# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.tests.system import VerifyReloadCause

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyReloadCauseInputFactory(AntaTestInputFactory[VerifyReloadCause.Input]):
    """
    Input factory class for the `VerifyReloadCause` test.

    The following EOS reload causes are allowed:
    - ZTP: "System reloaded due to Zero Touch Provisioning"
    - USER: "Reload requested by the user."
    - USER_HITLESS: "Hitless reload requested by the user."
    - FPGA: "Reload requested after FPGA upgrade"
    """

    def create(self) -> Iterator[VerifyReloadCause.Input]:
        """Generate the inputs for the `VerifyReloadCause` test."""
        yield VerifyReloadCause.Input(allowed_causes=["USER", "FPGA", "ZTP", "USER_HITLESS"])
