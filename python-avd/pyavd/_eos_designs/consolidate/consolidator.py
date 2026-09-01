# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from .connected_endpoints import ConnectedEndpointsMixin
from .models import ConsolidatedData
from .network_services import NetworkServicesMixin
from .node import NodeMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns as AVDDesign
    from pyavd._schema.models.avd_model import AvdModel


class AVDDesignConsolidatorProtocol(ConnectedEndpointsMixin, NetworkServicesMixin, NodeMixin, Protocol):
    """Protocol for mixins contributing to AVD design consolidation."""

    device_name: str
    inputs: AVDDesign
    consolidated: ConsolidatedData

    @staticmethod
    def _unset_avd_model(avd_model: AvdModel, attributes: tuple[str, ...]) -> None: ...


class AVDDesignConsolidator(AVDDesignConsolidatorProtocol):
    """Consolidate device-specific AVD design inputs."""

    def __init__(self, device_name: str, avd_design: AVDDesign) -> None:
        self.device_name = device_name
        self.inputs = avd_design
        self.consolidated = ConsolidatedData()

    @staticmethod
    def _unset_avd_model(avd_model: AvdModel, attributes: tuple[str, ...]) -> None:
        for attribute in attributes:
            if attribute in avd_model.__dict__:
                delattr(avd_model, attribute)

    def consolidate(self) -> ConsolidatedData:
        """
        Consolidate an AVD Design instance and return the device-local consolidated data.

        Warning: The given avd_design is mutated in-place and should not be used afterwards.
        """
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
        self.prune_connected_endpoint_inputs()
        self.prune_network_services_inputs()
        self.prune_node_inputs()
        self.inputs._custom_data.clear()
        return self.consolidated


def consolidate_avd_design(device_name: str, avd_design: AVDDesign) -> ConsolidatedData:
    """Consolidate the AVD design for one device."""
    return AVDDesignConsolidator(device_name, avd_design).consolidate()
