# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class KernelSettingsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def kernel_settings(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """Set the structured config for kernel settings."""
        if (not self.shared_utils.is_wan_router) or self.inputs.wan_use_agent_env_var_for_kernel_software_forwarding_ecmp:
            return
        self.structured_config.kernel.software_forwarding_ecmp = True
