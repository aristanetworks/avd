# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class AddressLockingMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def address_locking(self: AvdStructuredConfigBaseProtocol) -> None:
        if self.inputs.avd_design_future.only_configure_address_locking_when_used:
            return

        self.structured_config_utils.set_once_address_locking()
