# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.input_models.routing.bgp import BgpPeer
from anta.tests.routing.bgp import VerifyBGPPeerSession

from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyBGPPeerSessionInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyBGPPeerSession` test.

    This factory generates test inputs for BGP peer session verification.

    It collects BGP neighbors and neighbor interfaces (RFC5549) that are not directly
    shutdown or not in shutdown peer groups from the default VRF. If `allow_bgp_vrfs`
    is enabled in the input factory settings, it will also include BGP neighbors in VRFs.

    When a fabric `peer` is provided in the neighbor structured config, the factory verifies
    that the peer is available (`is_deployed: true`) before including it in the test inputs.
    """

    def create(self) -> list[VerifyBGPPeerSession.Input] | None:
        """Create a list of inputs for the `VerifyBGPPeerSession` test."""
        bgp_peers = natural_sort(
            [
                BgpPeer(
                    peer_address=neighbor.ip_address,
                    vrf=neighbor.vrf,
                )
                for neighbor in self.device.bgp_neighbors
            ],
            sort_key="peer_address",
        )

        # Add the RFC5549 peers
        bgp_peers.extend(
            natural_sort(
                [
                    BgpPeer(
                        interface=neighbor_intf.interface,
                        vrf=neighbor_intf.vrf,
                    )
                    for neighbor_intf in self.device.bgp_neighbor_interfaces
                ],
                sort_key="interface",
            )
        )

        return [VerifyBGPPeerSession.Input(bgp_peers=bgp_peers)] if bgp_peers else None
