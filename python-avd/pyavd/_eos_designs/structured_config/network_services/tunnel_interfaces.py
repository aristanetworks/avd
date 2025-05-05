# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class TunnelInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def set_zscaler_ie_tunnel_interface(
        self: AvdStructuredConfigNetworkServicesProtocol,
        tunnel_id: int,
        description: str,
        source_interface: str,
        destination: str,
        ipsec_profile: str,
    ) -> None:
        """
        Set structured config for one tunnel_interface for a Zscaler Internet Exit connection.

        Only used for CV Pathfinder edge routers today
        """
        tunnel_interface = EosCliConfigGen.TunnelInterfacesItem(
            name=f"Tunnel{tunnel_id}",
            description=description,
            mtu=1394,  # TODO: do not hardcode
            # Using Loopback0 as source interface as using the WAN interface causes issues for DPS.
            ip_address="unnumbered Loopback0",
            tunnel_mode="ipsec",  # TODO: do not hardcode
            source_interface=source_interface,
            destination=destination,
            ipsec_profile=ipsec_profile,
        )

        tunnel_interface.nat_profile = self.INTERNET_EXIT_ZSCALER_NAT_PROFILE_NAME

        self.structured_config.tunnel_interfaces.append(tunnel_interface)
