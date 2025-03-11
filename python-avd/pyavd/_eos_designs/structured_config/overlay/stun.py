# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import itertools
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class StunMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def stun(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for stun."""
        if not self.shared_utils.is_wan_router:
            return

        if self.shared_utils.is_wan_server:
            self.structured_config.stun.server.ssl_profile = self.shared_utils.wan_stun_dtls_profile_name
            for wan_interface in self.shared_utils.wan_interfaces:
                self.structured_config.stun.server.local_interfaces.append(wan_interface.name)
            for wan_port_channel in self.shared_utils.wan_port_channels:
                self.structured_config.stun.server.local_interfaces.append(wan_port_channel.name)

        if self.shared_utils.is_wan_client:
            self.structured_config.stun.client.server_profiles = EosCliConfigGen.Stun.Client.ServerProfiles(
                itertools.chain.from_iterable(self._stun_server_profiles.values())
            )
