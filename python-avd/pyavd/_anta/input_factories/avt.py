# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.input_models.avt import AVTPath
from anta.tests.avt import VerifyAVTSpecificPath

from pyavd._anta.logs import LogMessage
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyAVTSpecificPathInputFactory(AntaTestInputFactory):
    """
    Input factory class for the `VerifyAVTSpecificPath` test.

    It constructs a list of static peer addresses for each device by searching through
    `router_path_selection.path_groups.static_peers`.
    """

    def create(self) -> list[VerifyAVTSpecificPath.Input] | None:
        """Create a list of inputs for the `VerifyAVTSpecificPath` test."""
        avt_vrfs = self.structured_config.router_adaptive_virtual_topology.vrfs
        path_groups = self.structured_config.router_path_selection.path_groups
        static_peers: set[str] = set()

        for path_group in path_groups:
            if not path_group.static_peers:
                self.logger_adapter.debug(LogMessage.PATH_GROUP_NO_STATIC_PEERS, path_group=path_group.name)
                continue
            for static_peer in path_group.static_peers:
                static_peers.add(static_peer.router_ip)

        if not static_peers:
            self.logger_adapter.debug(LogMessage.NO_STATIC_PEERS)
            return None

        avt_paths: list[AVTPath] = [
            AVTPath(avt_name=avt_profile.name, vrf=vrf.name, destination=dst_address, next_hop=dst_address)
            for vrf in avt_vrfs
            for avt_profile in vrf.profiles
            if avt_profile.name
            for dst_address in static_peers
        ]

        return [VerifyAVTSpecificPath.Input(avt_paths=natural_sort(avt_paths, sort_key="avt_name"))] if avt_paths else None
