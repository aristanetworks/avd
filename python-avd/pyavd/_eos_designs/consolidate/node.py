# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from .consolidator import AVDDesignConsolidatorProtocol


class NodeMixin(Protocol):
    """Mixin consolidating node identity, inheritance, grouping, and MLAG settings."""

    @cached_property
    def device_config(self: AVDDesignConsolidatorProtocol) -> AVDDesign.DevicesItem | None:
        """Return this device's config with device profiles inherited."""
        if self.device_name not in self.consolidated_design.devices and not self.consolidated_design.device_profile:
            return None

        if (device_config := self.consolidated_design.devices.get(self.device_name, None)) is None:
            device_config = AVDDesign.DevicesItem()

        if device_profile_name := default(device_config.profile, self.consolidated_design.device_profile):
            if not (device_profile := self.consolidated_design.device_profiles.get(device_profile_name)):
                msg = f"The Device Profile '{device_profile_name}' applied for the device '{self.device_name}' does not exist under `device_profiles`."
                raise AristaAvdInvalidInputsError(msg)

            device_config._deepinherit(device_profile._cast_as(AVDDesign.DevicesItem, ignore_extra_keys=True))

            if device_profile.parent_profile:
                if not (parent_profile := self.consolidated_design.device_profiles.get(device_profile.parent_profile)):
                    msg = (
                        f"Device Profile '{device_profile.parent_profile}' applied as 'parent_profile' on the profile '{device_profile.name}' "
                        "does not exist under 'device_profiles'."
                    )
                    raise AristaAvdInvalidInputsError(msg, host=self.device_name)

                device_config._deepinherit(parent_profile._cast_as(AVDDesign.DevicesItem, ignore_extra_keys=True))

        return device_config

    @cached_property
    def device_config_from_profile_only(self: AVDDesignConsolidatorProtocol) -> bool:
        """Return whether device_config was created exclusively from the root device_profile."""
        return self.device_config is not None and self.device_name not in self.consolidated_design.devices

    @cached_property
    def type(self: AVDDesignConsolidatorProtocol) -> str:
        """Resolve the device type."""
        if self.device_config is not None and self.device_config.type is not None:
            return self.device_config.type

        if self.consolidated_design.type is not None:
            return self.consolidated_design.type

        for default_node_type in self.consolidated_design.default_node_types:
            for hostname_regex in default_node_type.match_hostnames:
                if search(f"^{hostname_regex}$", self.device_name):
                    return default_node_type.node_type

        msg = "No device type found. Either set 'type' or 'default_node_types'."
        raise AristaAvdInvalidInputsError(msg, host=self.device_name)

    def set_type(self: AVDDesignConsolidatorProtocol) -> None:
        """Set the consolidated device type."""
        self.consolidated_design._type = self.type

    @cached_property
    def node_type_keys_item(self: AVDDesignConsolidatorProtocol) -> AVDDesign.NodeTypeKeysItem:
        """Resolve the node_type_keys item matching the device type."""
        for node_type_key in self.consolidated_design.custom_node_type_keys:
            if node_type_key.type == self.type:
                return node_type_key._cast_as(AVDDesign.NodeTypeKeysItem)

        for node_type_key in self.consolidated_design.node_type_keys:
            if node_type_key.type == self.type:
                return node_type_key

        # This should never happen, as it should be caught during validation.
        msg = f"Could not find the given type '{self.type}' in node_type_keys or custom_node_type_keys."
        raise AristaAvdInvalidInputsError(msg)

    def set_node_type_keys_item(self: AVDDesignConsolidatorProtocol) -> None:
        """Set the relevant node_type_keys item."""
        self.consolidated_design._node_type_keys_item = self.node_type_keys_item

    @cached_property
    def node_type_config(self: AVDDesignConsolidatorProtocol) -> AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes | None:
        """Return the node type model selected by node_type_keys_item."""
        node_type_key = self.node_type_keys_item.key

        if node_type_key in self.consolidated_design._dynamic_keys.custom_node_types:
            return self.consolidated_design._dynamic_keys.custom_node_types[node_type_key].value._cast_as(AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes)

        if node_type_key in self.consolidated_design._dynamic_keys.node_types:
            return self.consolidated_design._dynamic_keys.node_types[node_type_key].value

        return None

    @cached_property
    def node_group_config(
        self: AVDDesignConsolidatorProtocol,
    ) -> AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem | None:
        """Return the node group containing this device, if any."""
        if self.node_type_config is None:
            return None

        node_group_config = None
        for node_group in self.node_type_config.node_groups:
            if self.device_name in node_group.nodes:
                node_group_config = node_group

        return node_group_config

    @cached_property
    def node_group_primary_and_peer(self: AVDDesignConsolidatorProtocol) -> tuple[bool, str] | None:
        """Return primary status and peer for a two-device node group."""
        if self.node_group_config is None or len(self.node_group_config.nodes) != 2:
            return None

        nodes = list(self.node_group_config.nodes.keys())
        index = nodes.index(self.device_name)
        peer_index = not index  # (0->1 and 1->0)
        return index == 0, nodes[peer_index]

    def set_node_group_primary_and_peer(self: AVDDesignConsolidatorProtocol) -> None:
        """Set node group position, peer, and length."""
        self.consolidated_design._node_group_primary_and_peer = self.node_group_primary_and_peer
        self.consolidated_design._node_group_length = len(self.node_group_config.nodes) if self.node_group_config is not None else 0

    @cached_property
    def node_config(self: AVDDesignConsolidatorProtocol) -> AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem:
        """Return the fully inherited node configuration."""
        if self.device_config is not None:
            if self.node_type_config is not None and (self.device_name in self.node_type_config.nodes or self.node_group_config is not None):
                if not self.device_config_from_profile_only:
                    msg = (
                        f"Found the device '{self.device_name}' under both '{self.node_type_keys_item.key}' and 'devices'. "
                        "Remove the device from one of the models."
                    )
                else:
                    msg = (
                        f"Found the device '{self.device_name}' under '{self.node_type_keys_item.key}' but it also has 'device_profile' set. "
                        "Those two models are mutually exclusive one of them must be removed for this device."
                    )
                raise AristaAvdInvalidInputsError(msg, host=self.device_name)

            return self.device_config._cast_as(AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)

        if self.node_type_config is None:
            msg = (
                f"'type' is set to '{self.type}', for which node configs should use the key '{self.node_type_keys_item.key}'"
                f"but '{self.node_type_keys_item.key}' was not found."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.device_name)

        node_config = self.node_type_config.nodes.get(
            self.device_name,
            default=AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem(),
        )

        if self.node_group_config is not None:
            node_config._deepinherit(
                self.node_group_config.nodes[self.device_name]._cast_as(
                    AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem,
                    ignore_extra_keys=True,
                )
            )
            node_config._deepinherit(
                self.node_group_config._cast_as(
                    AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem,
                    ignore_extra_keys=True,
                )
            )

        node_config._deepinherit(
            self.node_type_config.defaults._cast_as(
                AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem,
                ignore_extra_keys=True,
            )
        )
        return node_config

    def set_node_config(self: AVDDesignConsolidatorProtocol) -> None:
        """Set the fully inherited node configuration."""
        self.consolidated_design._node_config = self.node_config

    @cached_property
    def device_mlag_group(self: AVDDesignConsolidatorProtocol) -> str | None:
        """Return the devices-model MLAG group when node groups do not provide the peer."""
        if not self.node_type_keys_item.mlag_support or not self.node_config.mlag or self.node_group_primary_and_peer is not None:
            return None

        return self.device_config.mlag_group if self.device_config is not None else None

    @cached_property
    def mlag(self: AVDDesignConsolidatorProtocol) -> bool:
        """Return whether MLAG is enabled for this device."""
        if not self.node_type_keys_item.mlag_support or not self.node_config.mlag:
            return False

        return self.node_group_primary_and_peer is not None or self.device_mlag_group is not None

    def set_mlag(self: AVDDesignConsolidatorProtocol) -> None:
        """Set consolidated MLAG properties."""
        self.consolidated_design._mlag = self.mlag
        self.consolidated_design._device_mlag_group = self.device_mlag_group

    @cached_property
    def group(self: AVDDesignConsolidatorProtocol) -> str | None:
        """Return the node group or devices-model MLAG group name."""
        if self.node_group_config is not None:
            return self.node_group_config.group
        if self.device_config is not None:
            return self.device_config.mlag_group
        return None

    def set_group(self: AVDDesignConsolidatorProtocol) -> None:
        """Set the consolidated group."""
        self.consolidated_design._group = self.group

    def prune_node_inputs(self: AVDDesignConsolidatorProtocol) -> None:
        """Remove node input models consumed during consolidation."""
        self._unset_avd_model(
            self.consolidated_design,
            ("devices", "device_profiles", "device_profile", "default_node_types", "type", "node_type_keys"),
        )
        self._unset_avd_model(self.consolidated_design._dynamic_keys, ("custom_node_types", "node_types"))
