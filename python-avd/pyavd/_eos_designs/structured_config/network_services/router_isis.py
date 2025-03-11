# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterIsisMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_isis(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for router_isis.

        Used for non-EVPN where underlay_routing_protocol is ISIS,
        static routes in VRF "default" should be redistributed into ISIS
        unless specifically disabled under the vrf.
        """
        if (
            self.shared_utils.network_services_l3
            and self._vrf_default_ipv4_static_routes["redistribute_in_underlay"]
            and self.shared_utils.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]
        ):
            self.structured_config.router_isis.redistribute_routes.append_new(source_protocol="static")
