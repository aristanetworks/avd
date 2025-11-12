# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class Dot1xMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfigBase class.
    """

    @structured_config_contributor
    def dot1x(self: AvdStructuredConfigBaseProtocol) -> None:
        """Configure dot1x settings based on the `dot1x_settings` data model."""
        if not self.inputs.dot1x_settings.enabled:
            return

        self.structured_config.dot1x = EosCliConfigGen.Dot1x(
            system_auth_control=True,
            protocol_bpdu_bypass=self.inputs.dot1x_settings.bypass_bpdu,
            protocol_lldp_bypass=self.inputs.dot1x_settings.bypass_lldp,
            dynamic_authorization=self.inputs.dot1x_settings.dynamic_authorization.enabled,
            radius_av_pair=EosCliConfigGen.Dot1x.RadiusAvPair(service_type=True),
            radius_av_pair_username_format=EosCliConfigGen.Dot1x.RadiusAvPairUsernameFormat(
                delimiter=self.inputs.dot1x_settings.mac_based_authentication.username_delimiter,
                mac_string_case=self.inputs.dot1x_settings.mac_based_authentication.username_letter_case,
            ),
        )
