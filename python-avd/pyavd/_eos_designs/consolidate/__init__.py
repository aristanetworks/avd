# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass
from re import search
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns as AVDDesign
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._schema.models.eos_designs_root_model import EosDesignsRootModel
from pyavd._utils import default

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pyavd._schema.models.avd_model import AvdModel


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

    _consolidated_property_names = (
        "_type",
        "_node_type_keys_item",
        "_node_config",
        "_node_group_primary_and_peer",
        "_mlag",
        "_device_mlag_group",
        "_group",
        "_node_group_length",
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

        for property_name in cls._consolidated_property_names:
            instance._custom_data.pop(property_name, None)

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
            }
        )
        return data

    @classmethod
    def _from_avd_design(cls, device_name: str, avd_design: AVDDesign | Mapping) -> ConsolidatedAVDDesign:
        from pyavd._eos_designs.schema import EosDesigns as AVDDesign  # noqa: PLC0415

        if isinstance(avd_design, ConsolidatedAVDDesign):
            return avd_design

        if not isinstance(avd_design, AVDDesign):
            avd_design = AVDDesign._from_dict(avd_design)

        return _consolidate_avd_design(device_name, avd_design)


@dataclass
class _TmpConsolidationData:
    device_name: str
    device_config: AVDDesign.DevicesItem | None = None
    device_config_from_profile_only: bool | None = None
    node_type_config: AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes | None = None
    node_group_config: AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodeGroupsItem | None = None


def _unset_avd_model(avd_model: AvdModel, attributes: tuple[str, ...]) -> None:
    for attribute in attributes:
        if attribute in avd_model.__dict__:
            delattr(avd_model, attribute)


def _consolidate_avd_design(device_name: str, avd_design: AVDDesign) -> ConsolidatedAVDDesign:
    """
    Consolidate an AVD Design instance and return as ConsolidatedAVDDesign.

    Warning: The given avd_design is mutated in-place and should not be used afterwards.

    Consolidation will perform the following actions on the given model:
    - Consolidate 'type' from 'devices[].type', 'type' or 'default_node_types'
    - Resolve the full node_config into '_node_config' from either '<node_type_key>' or 'devices' model.
      This includes node type inheritance or application of device_profiles.
    - Remove consumed datamodels since the relevant data is now in '_node_config' and 'type'.
      - '_dynamic_keys.node_types'
      - 'device_profiles'
      - 'devices'
      - 'default_node_types'
    """
    avd_design = avd_design._cast_as(ConsolidatedAVDDesign)

    tmp_data = _TmpConsolidationData(device_name)
    _tmp_device_config(avd_design, tmp_data)
    _consolidate_type(avd_design, tmp_data)
    _consolidate_node_type_keys_item(avd_design)
    _tmp_node_type_config(avd_design, tmp_data)
    _tmp_node_group_config(tmp_data)
    _consolidate_node_group_primary_and_peer(avd_design, tmp_data)
    _consolidate_node_config(avd_design, tmp_data)
    _consolidate_mlag(avd_design, tmp_data)
    _consolidate_group(avd_design, tmp_data)
    return avd_design


def _tmp_device_config(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """
    Sets 'device_config' under tmp_data.

    Find this device under 'devices' and apply any profile (and parent profile).
    A device may not be under devices, but can still be be created if device_profile is set.
    """

    def prune() -> None:
        _unset_avd_model(avd_design, ("devices", "device_profiles", "device_profile"))

    if tmp_data.device_name not in avd_design.devices and not avd_design.device_profile:
        return prune()

    if (device_config := avd_design.devices.get(tmp_data.device_name, None)) is None:
        tmp_data.device_config_from_profile_only = True
        device_config = AVDDesign.DevicesItem()
    else:
        tmp_data.device_config_from_profile_only = False

    if device_profile_name := default(device_config.profile, avd_design.device_profile):
        if not (device_profile := avd_design.device_profiles.get(device_profile_name)):
            msg = f"The Device Profile '{device_profile_name}' applied for the device '{tmp_data.device_name}' does not exist under `device_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        device_config._deepinherit(device_profile._cast_as(AVDDesign.DevicesItem, ignore_extra_keys=True))

        if device_profile.parent_profile:
            if not (parent_profile := avd_design.device_profiles.get(device_profile.parent_profile)):
                msg = (
                    f"Device Profile '{device_profile.parent_profile}' applied as 'parent_profile' on the profile '{device_profile.name}' "
                    "does not exist under 'device_profiles'."
                )
                raise AristaAvdInvalidInputsError(msg, host=tmp_data.device_name)

            device_config._deepinherit(parent_profile._cast_as(AVDDesign.DevicesItem, ignore_extra_keys=True))

    tmp_data.device_config = device_config
    return prune()


def _consolidate_type(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """
    Sets '_type' if unset and 'default_node_types' is set and working.

    Raises:
        AristaAvdInvalidInputsError: if neither 'type' or 'default_node_types' resolved.
    """

    def prune() -> None:
        _unset_avd_model(avd_design, ("default_node_types", "type"))

    type_from_device_config = tmp_data.device_config.type if tmp_data.device_config is not None else None
    if type_from_device_config is not None:
        avd_design._type = type_from_device_config
        return prune()

    if avd_design.type is not None:
        avd_design._type = avd_design.type
        return prune()

    for default_node_type in avd_design.default_node_types:
        for hostname_regex in default_node_type.match_hostnames:
            if search(f"^{hostname_regex}$", tmp_data.device_name):
                avd_design._type = default_node_type.node_type
                return prune()

    msg = "No device type found. Either set 'type' or 'default_node_types'."
    raise AristaAvdInvalidInputsError(msg, host=tmp_data.device_name)


def _consolidate_node_type_keys_item(avd_design: ConsolidatedAVDDesign) -> None:
    """Sets '_node_type_keys_item' with the relevant item from 'node_type_keys'."""

    def prune() -> None:
        _unset_avd_model(avd_design, ("node_type_keys",))

    for node_type_key in avd_design.custom_node_type_keys:
        if node_type_key.type == avd_design._type:
            avd_design._node_type_keys_item = node_type_key._cast_as(AVDDesign.NodeTypeKeysItem)
            return prune()

    node_type_keys = avd_design.node_type_keys
    for node_type_key in node_type_keys:
        if node_type_key.type == avd_design._type:
            avd_design._node_type_keys_item = node_type_key
            return prune()

    # This should never happen, as it should be caught during validation
    msg = f"Could not find the given type '{avd_design._type}' in node_type_keys or custom_node_type_keys."
    raise AristaAvdInvalidInputsError(msg)


def _tmp_node_type_config(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """
    The object representing the `<node_type_key like l3leaf, spine etc>:` containing the `defaults`, `nodes`, `node_groups` etc.

    The relevant dynamic key is found in avd_design._dynamic_keys which is populated by the _from_dict() loader on the EosDesigns class.
    """

    def prune() -> None:
        _unset_avd_model(avd_design._dynamic_keys, ("custom_node_types", "node_types"))

    node_type_key = avd_design._node_type_keys_item.key

    if node_type_key in avd_design._dynamic_keys.custom_node_types:
        tmp_data.node_type_config = avd_design._dynamic_keys.custom_node_types[node_type_key].value._cast_as(
            AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes
        )
        return prune()

    if node_type_key in avd_design._dynamic_keys.node_types:
        tmp_data.node_type_config = avd_design._dynamic_keys.node_types[node_type_key].value
        return prune()

    # We did not find a matching node type key. Either this was forgotten or we are using the new `devices` model.
    # This is caught inside _consolidate_node_config.
    return prune()


def _tmp_node_group_config(tmp_data: _TmpConsolidationData) -> None:
    """
    The object representing the `<node_type_key like l3leaf, spine etc>.node_groups[]` where this node is found.

    Used by MLAG and WAN HA logic to find out who our MLAG / WAN HA peer is.
    """
    if tmp_data.node_type_config is not None:
        for node_group in tmp_data.node_type_config.node_groups:
            if tmp_data.device_name in node_group.nodes:
                tmp_data.node_group_config = node_group


def _consolidate_node_group_primary_and_peer(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """
    Node group position and peer used for MLAG and WAN HA.

    Sets None if the device is not in a node_group with exactly two devices.
    Sets True, <peer> if this device is the first one in the node_group.
    Sets False, <peer> if this device is the second one in the node_group.
    """
    if (node_group_config := tmp_data.node_group_config) is None:
        avd_design._node_group_primary_and_peer = None
        avd_design._node_group_length = 0
        return

    node_group_length = len(node_group_config.nodes)
    avd_design._node_group_length = node_group_length

    if node_group_length != 2:
        avd_design._node_group_primary_and_peer = None
        return

    nodes = list(node_group_config.nodes.keys())
    index = nodes.index(tmp_data.device_name)
    peer_index = not index  # (0->1 and 1>0)
    avd_design._node_group_primary_and_peer = index == 0, nodes[peer_index]


def _consolidate_node_config(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """
    Sets '_node_config' as a NodesItem object containing the fully inherited node config.

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
    if tmp_data.device_config is not None:
        # Detect if the device is _also_ defined under the node type model. If so raise an error.
        if tmp_data.node_type_config is not None and (tmp_data.device_name in tmp_data.node_type_config.nodes or tmp_data.node_group_config is not None):
            if not tmp_data.device_config_from_profile_only:
                msg = (
                    f"Found the device '{tmp_data.device_name}' under both '{avd_design._node_type_keys_item.key}' and 'devices'. "
                    "Remove the device from one of the models."
                )
            else:
                # Device config was created only from the device_profile key.
                msg = (
                    f"Found the device '{tmp_data.device_name}' under '{avd_design._node_type_keys_item.key}' but it also has 'device_profile' set. "
                    "Those two models are mutually exclusive one of them must be removed for this device."
                )
            raise AristaAvdInvalidInputsError(
                msg,
                host=tmp_data.device_name,
            )

        # Casting as NodesItem so all the code relying on this does not have to care which model the input came from.
        avd_design._node_config = tmp_data.device_config._cast_as(AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
        return

    if tmp_data.node_type_config is None:
        msg = (
            f"'type' is set to '{avd_design._type}', for which node configs should use the key '{avd_design._node_type_keys_item.key}'"
            f"but '{avd_design._node_type_keys_item.key}' was not found."
        )
        raise AristaAvdInvalidInputsError(msg, host=tmp_data.device_name)

    node_config = tmp_data.node_type_config.nodes.get(tmp_data.device_name, default=AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem())

    if tmp_data.node_group_config is not None:
        node_config._deepinherit(
            tmp_data.node_group_config.nodes[tmp_data.device_name]._cast_as(
                AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True
            )
        )
        node_config._deepinherit(tmp_data.node_group_config._cast_as(AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True))

    node_config._deepinherit(
        tmp_data.node_type_config.defaults._cast_as(AVDDesign._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem, ignore_extra_keys=True)
    )

    avd_design._node_config = node_config
    return


def _consolidate_mlag(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    if not avd_design._node_type_keys_item.mlag_support or not avd_design._node_config.mlag:
        avd_design._device_mlag_group = None
        avd_design._mlag = False
        return

    # Node groups used for mlag peer.
    if avd_design._node_group_primary_and_peer:
        avd_design._device_mlag_group = None
        avd_design._mlag = True
        return

    # devices[].mlag_group used for mlag peer.
    avd_design._device_mlag_group = tmp_data.device_config.mlag_group if tmp_data.device_config is not None else None
    avd_design._mlag = bool(avd_design._device_mlag_group)


def _consolidate_group(avd_design: ConsolidatedAVDDesign, tmp_data: _TmpConsolidationData) -> None:
    """Group set to "node_group" name or None."""
    if tmp_data.node_group_config is not None:
        avd_design._group = tmp_data.node_group_config.group
    elif tmp_data.device_config is not None:
        avd_design._group = tmp_data.device_config.mlag_group
    else:
        avd_design._group = None
