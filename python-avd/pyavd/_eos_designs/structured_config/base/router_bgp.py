# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class RouterBgpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_bgp(self: AvdStructuredConfigBaseProtocol) -> None:
        """
        Set the structured config for router_bgp.

        router_bgp set based on switch.bgp_as, switch.bgp_defaults, router_id facts and aggregating the values of bgp_maximum_paths and bgp_ecmp variables.
        """
        if self.shared_utils.bgp_as is None:
            return

        # Keeping None since EOS default is asplain.
        self.structured_config.router_bgp.as_notation = "asdot" if self.shared_utils.bgp_as_notation == "asdot" else None

        platform_bgp_update_wait_for_convergence = self.shared_utils.platform_settings.feature_support.bgp_update_wait_for_convergence
        platform_bgp_update_wait_install = self.shared_utils.platform_settings.feature_support.bgp_update_wait_install

        default_maximum_paths = 16 if self.shared_utils.is_wan_router else 4

        self.structured_config.router_bgp._update(
            router_id=self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None,
            field_as=self.shared_utils.formatted_bgp_as,
        )

        if bgp_defaults := self.shared_utils.node_config.bgp_defaults:
            self.structured_config.router_bgp.bgp_defaults = bgp_defaults._cast_as(EosCliConfigGen.RouterBgp.BgpDefaults)

        if bgp_distance := self.inputs.bgp_distance:
            self.structured_config.router_bgp.distance = bgp_distance

        self.structured_config.router_bgp.bgp.default.ipv4_unicast = self.inputs.bgp_default_ipv4_unicast
        self.structured_config.router_bgp.maximum_paths._update(paths=self.inputs.bgp_maximum_paths or default_maximum_paths, ecmp=self.inputs.bgp_ecmp)

        if self.inputs.bgp_update_wait_for_convergence and platform_bgp_update_wait_for_convergence:
            self.structured_config.router_bgp.updates.wait_for_convergence = True

        if self.inputs.bgp_update_wait_install and platform_bgp_update_wait_install:
            self.structured_config.router_bgp.updates.wait_install = True

        if self.inputs.bgp_graceful_restart.enabled:
            self.structured_config.router_bgp.graceful_restart._update(enabled=True, restart_time=self.inputs.bgp_graceful_restart.restart_time)

        # Add IPv4 neighbors
        self.structured_config.router_bgp.neighbors.extend(self.shared_utils.l3_bgp_neighbors)
        for neighbor in self.shared_utils.l3_bgp_neighbors:
            self.structured_config.router_bgp.address_family_ipv4.neighbors.append_new(ip_address=neighbor.ip_address, activate=True)

        # Add IPv6 neighbors
        self.structured_config.router_bgp.neighbors.extend(self.shared_utils.l3_bgp_ipv6_neighbors)
        for neighbor in self.shared_utils.l3_bgp_ipv6_neighbors:
            self.structured_config.router_bgp.address_family_ipv6.neighbors.append_new(ip_address=neighbor.ip_address, activate=True)
