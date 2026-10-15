# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol
    from .utils import T_P2pLinksItem


class TunnelInterfacesMixin(Protocol):
    """Mixin Class used to generate structured config for tunnel_interfaces."""

    @structured_config_contributor
    def tunnel_interfaces(self: AvdStructuredConfigCoreInterfacesAndL3EdgeProtocol) -> None:
        """Set the structured config for tunnel_interfaces."""
        for p2p_link, p2p_link_data in self._filtered_p2p_links:
            if not p2p_link_data.get("is_tunnel"):
                continue

            tunnel_interface = EosCliConfigGen.TunnelInterfacesItem(
                name=p2p_link_data["interface"],
                shutdown=False,
                mtu=p2p_link._get("mtu", self.shared_utils.p2p_uplinks_mtu),
                tunnel_mode=p2p_link_data["tunnel_mode"],
                source_interface=p2p_link_data["source_interface"],
                destination=p2p_link_data["peer_source_ip"],
                eos_cli=p2p_link.raw_eos_cli,
            )

            if p2p_link.tunnel.path_mtu_discovery is not None:
                tunnel_interface.path_mtu_discovery = p2p_link.tunnel.path_mtu_discovery

            if p2p_link_data["tunnel_mode"] == "ipsec" and p2p_link.tunnel.ipsec_profile:
                tunnel_interface.ipsec_profile = p2p_link.tunnel.ipsec_profile

            if p2p_link_data["ip"]:
                tunnel_interface.ip_address = p2p_link_data["ip"]

            if p2p_link_data["ipv6"]:
                tunnel_interface.ipv6_addresses.append(p2p_link_data["ipv6"])
                self.structured_config.ipv6_unicast_routing = True

            if p2p_link.include_in_underlay_protocol:
                self._apply_underlay_ospf_config(p2p_link, p2p_link_data, tunnel_interface)
                self._apply_underlay_isis_config(p2p_link, tunnel_interface)

            self._apply_underlay_mpls_config(p2p_link, tunnel_interface)

            if p2p_link.tunnel_structured_config:
                self.custom_structured_configs.nested.tunnel_interfaces.obtain(tunnel_interface.name)._deepmerge(
                    p2p_link.tunnel_structured_config,
                    list_merge=self.custom_structured_configs.list_merge_strategy,
                )

            self.structured_config.tunnel_interfaces.append(tunnel_interface)
