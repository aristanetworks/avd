# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from anta.input_models.routing.bgp import BgpPeer
from anta.tests.routing.bgp import VerifyBGPPeerSession

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from collections.abc import Iterator


class VerifyBGPPeerSessionInputFactory(AntaTestInputFactory[VerifyBGPPeerSession.Input]):
    """
    Input factory class for the `VerifyBGPPeerSession` test.

    Generates inputs for BGP peer session verification. For all VRFs, collects BGP neighbors and
    neighbor interfaces (RFC5549) that are neither directly shutdown nor part of a shutdown peer group.

    It also considers the `metadata.validate_state` knob and when `metadata.peer` is provided,
    ensures that the peer is available (`is_deployed: true`) before including it in the test inputs.
    """

    def create(self) -> Iterator[VerifyBGPPeerSession.Input]:
        """Generate the inputs for the `VerifyBGPPeerSession` test."""
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

        if not bgp_peers:
            self.logger_adapter.debug(LogMessage.NO_INPUTS_GENERATED)
            return

        yield VerifyBGPPeerSession.Input(bgp_peers=bgp_peers)
