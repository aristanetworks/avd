# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns as AVDDesign

if TYPE_CHECKING:
    from collections.abc import Mapping

from .connected_endpoints import ConnectedEndpointsMixin
from .model import ConsolidatedAVDDesign
from .network_services import NetworkServicesMixin
from .node import NodeMixin


class AVDDesignConsolidatorProtocol(ConnectedEndpointsMixin, NetworkServicesMixin, NodeMixin, Protocol):
    """Protocol for mixins contributing to AVD design consolidation."""

    device_name: str
    inputs: AVDDesign
    consolidated: ConsolidatedAVDDesign


class AVDDesignConsolidator(AVDDesignConsolidatorProtocol):
    """Consolidate device-specific AVD design inputs."""

    def __init__(self, device_name: str, avd_design: AVDDesign) -> None:
        self.device_name = device_name
        self.inputs = avd_design
        self.consolidated = ConsolidatedAVDDesign()

    def consolidate(self) -> ConsolidatedAVDDesign:
        """Consolidate an AVD Design instance and return the device-local consolidated data."""
        self.set_type()
        self.set_node_type_keys_item()
        self.set_node_group_primary_and_peer()
        self.set_node_config()
        self.set_mlag()
        self.set_group()
        self.set_network_services()
        self.set_port_profile_names()
        self.set_connected_endpoints()
        self.set_network_ports()
        return self.consolidated


def consolidate_avd_design(device_name: str, avd_design: AVDDesign | Mapping) -> ConsolidatedAVDDesign:
    """Consolidate the AVD design for one device."""
    if not isinstance(avd_design, AVDDesign):
        avd_design = AVDDesign._from_dict(avd_design)

    return AVDDesignConsolidator(device_name, avd_design).consolidate()
