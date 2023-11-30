# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class BgpPeerGroupsMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def bgp_peer_groups(self: SharedUtils):
        """
        Get bgp_peer_groups configurations or fallback to defaults

        Supporting legacy uppercase keys as well.
        """
        if not self.underlay_router:
            return None

        BGP_PEER_GROUPS = [
            # (key, default_name, default_bfd)
            # Default BFD is set to None when not True, to avoid generating config for disabling BFD
            ("ipv4_underlay_peers", "IPv4-UNDERLAY-PEERS", None),
            ("mlag_ipv4_underlay_peer", "MLAG-IPv4-UNDERLAY-PEER", None),
            ("evpn_overlay_peers", "EVPN-OVERLAY-PEERS", True),
            ("evpn_overlay_core", "EVPN-OVERLAY-CORE", True),
            ("mpls_overlay_peers", "MPLS-OVERLAY-PEERS", True),
            ("rr_overlay_peers", "RR-OVERLAY-PEERS", True),
            ("ipvpn_gateway_peers", "IPVPN-GATEWAY-PEERS", True),
            ("wan_overlay_peers", "WAN-OVERLAY-PEERS", None),
        ]

        bgp_peer_groups = {}
        for key, default_name, default_bfd in BGP_PEER_GROUPS:
            bgp_peer_groups[key] = {
                "name": get(self.hostvars, f"bgp_peer_groups.{key}.name", default=default_name),
                "password": get(self.hostvars, f"bgp_peer_groups.{key}.password"),
                "bfd": get(self.hostvars, f"bgp_peer_groups.{key}.bfd", default=default_bfd),
                "structured_config": get(self.hostvars, f"bgp_peer_groups.{key}.structured_config"),
            }

        return bgp_peer_groups
