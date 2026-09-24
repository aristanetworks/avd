# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class SystemMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def system(self: AvdStructuredConfigBaseProtocol) -> None:
        """Set the EOS system MAC address."""
        if self.shared_utils.custom_system_mac_address is None:
            return

        self.structured_config.system.mac_address = self.shared_utils.system_mac_address
