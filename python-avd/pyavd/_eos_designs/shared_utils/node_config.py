# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class NodeConfigMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes | None:
        """
        The object representing the `<node_type_key like l3leaf, spine etc>:` containing the `defaults`, `nodes`, `node_groups` etc.

        The relevant dynamic key is found in self.inputs._dynamic_keys which is populated by the _from_dict() loader on the EosDesigns class.
        """
        node_type_key = self.node_type_key_data.key

        if node_type_key in self.inputs._dynamic_keys.custom_node_types:
            return self.inputs._dynamic_keys.custom_node_types[node_type_key].value._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes)

        if node_type_key in self.inputs._dynamic_keys.node_types:
            return self.inputs._dynamic_keys.node_types[node_type_key].value

        # We did not find a matching node type key. Either this was forgotten or we are using the new `devices` model.
        # This is caught inside self.node_config.
        return None

    @cached_property
    def node_group_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem | None:
        """
        The object representing the `<node_type_key like l3leaf, spine etc>.node_groups[]` where this node is found.

        Used by MLAG and WAN HA logic to find out who our MLAG / WAN HA peer is.
        """
        if self.node_type_config is not None:
            for node_group in self.node_type_config.node_groups:
                if self.hostname in node_group.nodes:
                    return node_group

        return None

    @cached_property
    def node_config(self: SharedUtilsProtocol) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
        """
        NodesItem object containing the fully inherited node config.

        This is coming from either node_type_config (like 'l3leaf:') or from the new 'devices'/'device_profiles' models.

        For node_type_config vars are inherited like (first one wins):
        <node_type_key>.nodes.[<node>] ->
            <node_type_key>.node_groups.[<node_group>].nodes.[<node>] ->
                <node_type_key>.node_groups.[<node_group>] ->
                    <node_type_key>.defaults

        For 'devices' vars are already inherited in self.device_config (first one wins):
        devices[name=hostname] ->
            profile[name=profile] ->
                parent_profiles[name=parent_profile]
        """
        if self.device_config is not None:
            # Detect if the device is _also_ defined under the node type model. If so raise an error.
            if self.node_type_config is not None and (self.hostname in self.node_type_config.nodes or self.node_group_config is not None):
                if self.hostname in self.inputs.devices:
                    msg = (
                        f"Found the device '{self.hostname}' under both '{self.node_type_key_data.key}' and 'devices'. "
                        "Remove the device from one of the models."
                    )
                else:
                    # Device config was created only from the device_profile key.
                    msg = (
                        f"Found the device '{self.hostname}' under '{self.node_type_key_data.key}' but it also has 'device_profile' set. "
                        "Those two models are mutually exclusive one of them must be removed for this device."
                    )
                raise AristaAvdInvalidInputsError(
                    msg,
                    host=self.hostname,
                )

            # Casting as NodesItem so all the code relying on this does not have to care which model the input came from.
            return self.device_config._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)

        if self.node_type_config is None:
            msg = (
                f"'type' is set to '{self.type}', for which node configs should use the key '{self.node_type_key_data.key}'"
                f"but '{self.node_type_key_data.key}' was not found."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        node_config = self.node_type_config.nodes.get(self.hostname, default=EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem())

        if self.node_group_config is not None:
            node_config._deepinherit(
                self.node_group_config.nodes[self.hostname]._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
            )
            node_config._deepinherit(self.node_group_config._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True))

        node_config._deepinherit(
            self.node_type_config.defaults._cast_as(EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
        )

        return node_config

    @cached_property
    def node_group_is_primary_and_peer_hostname(self: SharedUtilsProtocol) -> tuple[bool, str] | None:
        """
        Node group position and peer used for MLAG and WAN HA.

        Returns None if the device is not in a node_group with exactly two devices.
        Returns True, <peer> if this device is the first one in the node_group.
        Returns False, <peer> if this device is the second one in the node_group.
        """
        if self.node_group_config is None or len(self.node_group_config.nodes) != 2:
            return None

        nodes = list(self.node_group_config.nodes.keys())
        index = nodes.index(self.hostname)
        peer_index = not index  # (0->1 and 1>0)
        return index == 0, nodes[peer_index]
