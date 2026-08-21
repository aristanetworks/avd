# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._schema.models.eos_designs_root_model import EosDesignsRootModel

from .models import ConsolidatedConnectedEndpointGroups, ConsolidatedNetworkPorts, ConsolidatedNetworkServices, ConsolidatedPortProfileNames

if TYPE_CHECKING:
    from collections.abc import Mapping


class ConsolidatedAVDDesign(AVDDesign):
    _type: str
    """Guaranteed type as string."""

    _node_type_keys_item: AVDDesign.NodeTypeKeysItem
    _node_config: AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem
    _node_group_primary_and_peer: tuple[bool, str] | None
    _mlag: bool
    _device_mlag_group: str | None
    """mlag_group set under devices model."""

    _group: str | None
    _node_group_length: int
    _connected_endpoints: ConsolidatedConnectedEndpointGroups
    _network_ports: ConsolidatedNetworkPorts
    _port_profile_names: ConsolidatedPortProfileNames
    _network_services: ConsolidatedNetworkServices

    _consolidated_property_names = (
        "_type",
        "_node_type_keys_item",
        "_node_config",
        "_node_group_primary_and_peer",
        "_mlag",
        "_device_mlag_group",
        "_group",
        "_node_group_length",
        "_connected_endpoints",
        "_network_ports",
        "_port_profile_names",
        "_network_services",
    )

    @classmethod
    def _from_dict(cls, data: Mapping, load_custom_structured_config: bool = True) -> ConsolidatedAVDDesign:
        """Load previously consolidated AVD Design inputs."""
        # The serialized data already contains normalized dynamic keys and custom structured configurations,
        # so bypass EosDesignsRootModel preprocessing for raw inputs.
        model_data = data
        if not load_custom_structured_config:
            model_data = {key: value for key, value in data.items() if key != "_custom_structured_configurations"}
        instance = super(EosDesignsRootModel, cls)._from_dict(model_data)

        instance._type = data["_type"]
        instance._node_type_keys_item = AVDDesign.NodeTypeKeysItem._from_dict(data["_node_type_keys_item"])
        instance._node_config = AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem._from_dict(data["_node_config"])
        node_group_primary_and_peer = data["_node_group_primary_and_peer"]
        instance._node_group_primary_and_peer = tuple(node_group_primary_and_peer) if node_group_primary_and_peer is not None else None
        instance._mlag = data["_mlag"]
        instance._device_mlag_group = data["_device_mlag_group"]
        instance._group = data["_group"]
        instance._node_group_length = data["_node_group_length"]
        instance._connected_endpoints = ConsolidatedConnectedEndpointGroups._from_list(data["_connected_endpoints"])
        instance._network_ports = ConsolidatedNetworkPorts._from_list(data["_network_ports"])
        instance._port_profile_names = ConsolidatedPortProfileNames._from_list(data["_port_profile_names"])
        instance._network_services = ConsolidatedNetworkServices._from_list(data["_network_services"])

        # Consolidated root models do not retain arbitrary custom data. Nested models retain theirs.
        instance._custom_data.clear()

        return instance

    def _dump(self, include_default_values: bool = False) -> dict:
        """Dump consolidated AVD Design inputs, including private consolidated properties."""
        data = self._cast_as(AVDDesign, ignore_extra_keys=True)._dump(include_default_values=include_default_values)
        data.update(
            {
                "_type": self._type,
                "_node_type_keys_item": self._node_type_keys_item._dump(include_default_values=include_default_values),
                "_node_config": self._node_config._dump(include_default_values=include_default_values),
                "_node_group_primary_and_peer": self._node_group_primary_and_peer,
                "_mlag": self._mlag,
                "_device_mlag_group": self._device_mlag_group,
                "_group": self._group,
                "_node_group_length": self._node_group_length,
                "_connected_endpoints": self._connected_endpoints._dump(include_default_values=include_default_values),
                "_network_ports": self._network_ports._dump(include_default_values=include_default_values),
                "_port_profile_names": self._port_profile_names._dump(include_default_values=include_default_values),
                "_network_services": self._network_services._dump(include_default_values=include_default_values),
            }
        )
        return data

    @classmethod
    def _from_avd_design(cls, device_name: str, avd_design: AVDDesign | Mapping) -> ConsolidatedAVDDesign:
        from pyavd._eos_designs.schema import EosDesigns as AVDDesign  # noqa: PLC0415

        from .consolidator import consolidate_avd_design  # noqa: PLC0415

        if isinstance(avd_design, ConsolidatedAVDDesign):
            return avd_design

        if not isinstance(avd_design, AVDDesign):
            avd_design = AVDDesign._from_dict(avd_design)

        return consolidate_avd_design(device_name, avd_design)
