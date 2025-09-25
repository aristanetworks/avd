# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING, Any, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError
from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel
from pyavd._utils import default, get_v2

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigMetadataProtocol

CAMPUS_TOPOLOGY_NETWORK_TYPE = "campusV2"
INVALID_CUSTOM_DEVICE_TAGS = [
    "topology_type",
    "topology_datacenter",
    "topology_rack",
    "topology_pod",
    "eos",
    "eostrain",
    "ztp",
    "bgp",
    "container",
    "mpls",
    "topology_network_type",
    "model",
    "systype",
    "serialnumber",
    "tapagg",
    "hostname",
    "terminattr",
]
"""These tag names overlap with CV system tags."""
CAMPUS_LINK_TYPE_MAP = {
    "downlink": "Downlink",
    "egress": "Egress",
    "fabric": "Fabric",
    "mlag": "MLAG",
    "uplink": "Uplink",
}
"""Convert input tag values to the values compliant with the CloudVision."""


class CvTagsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _set_cv_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Set the data structure of `metadata.cv_tags`."""
        if not self.inputs.generate_cv_tags and not self.shared_utils.is_cv_pathfinder_router:
            return
        self._set_topology_hints()
        self._set_cv_pathfinder_device_tags()
        self._set_device_tags()
        self._set_interface_tags()

    @staticmethod
    def _tag_dict(name: str, value: Any) -> dict | None:
        if value is None:
            return None
        return {"name": name, "value": str(value)}

    def _set_topology_hints(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Set the data structure of topology_hint tags."""
        if not self.inputs.generate_cv_tags.topology_hints:
            return

        if self.shared_utils.is_campus_device:
            self._set_topology_hints_for_campus()
            return

        for name, value in [
            ("topology_hint_datacenter", self.inputs.dc_name),
            ("topology_hint_fabric", self.shared_utils.fabric_name),
            ("topology_hint_pod", self.inputs.pod_name),
            ("topology_hint_type", self.shared_utils.hint_type),
            ("topology_hint_rack", default(self.shared_utils.node_config.rack, self.shared_utils.group)),
        ]:
            tag = self._tag_dict(name, value)
            if tag:
                self.structured_config.metadata.cv_tags.device_tags.append_new(name=name, value=tag["value"])

    def _set_topology_hints_for_campus(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Set the data structure of topology_hint tags for Campus fabric devices."""
        for name, value in [
            ("topology_hint_network_type", CAMPUS_TOPOLOGY_NETWORK_TYPE),
            ("topology_hint_type", self.shared_utils.campus_hint_type),
            ("Role", self.shared_utils.campus_hint_type),
            ("Campus", default(self.shared_utils.node_config.campus, self.inputs.campus)),
            ("Campus-Pod", default(self.shared_utils.node_config.campus_pod, self.inputs.campus_pod)),
            (
                "Access-Pod",
                None
                if self.shared_utils.campus_hint_type == "Spine"
                else default(self.shared_utils.node_config.campus_access_pod, self.inputs.campus_access_pod),
            ),
        ]:
            tag = self._tag_dict(name, value)
            if tag:
                self.structured_config.metadata.cv_tags.device_tags.append_new(name=name, value=tag["value"])

    def _set_cv_pathfinder_device_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """
        Set the data structure of device_tags for cv_pathfinder solution.

        Example: [
            {"name": "Region", "value": <value copied from cv_pathfinder_region>},
            {"name": "Zone", "value": <"<region-name>-ZONE" for pathfinder clients>},
            {"name": "Site", "value": <value copied from cv_pathfinder_site for pathfinder clients>},
            {"name": "PathfinderSet", "value": <value copied from node group or default "PATHFINDERS" for pathfinder servers>},
            {"name": "Role", "value": <'pathfinder', 'edge', 'transit region' or 'transit zone'>}
        ].
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return

        region_name = self.shared_utils.wan_region.name if self.shared_utils.wan_region else None
        site_name = self.shared_utils.wan_site.name if self.shared_utils.wan_site else None

        for name, value in [
            ("Role", self.shared_utils.cv_pathfinder_role),
            ("Region", region_name),
            ("PathfinderSet", self.shared_utils.group or "PATHFINDERS" if self.shared_utils.is_cv_pathfinder_server else None),
            ("Zone", self.shared_utils.wan_zone.name if not self.shared_utils.is_cv_pathfinder_server else None),
            ("Site", site_name if not self.shared_utils.is_cv_pathfinder_server else None),
        ]:
            tag = self._tag_dict(name, value)
            if tag:
                self.structured_config.metadata.cv_tags.device_tags.append_new(name=name, value=tag["value"])

    def _set_device_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Set the data structure of device_tags."""
        if not (tags_to_generate := self.inputs.generate_cv_tags.device_tags):
            return

        for generate_tag in tags_to_generate:
            if generate_tag.name in INVALID_CUSTOM_DEVICE_TAGS:
                msg = (
                    f"The CloudVision tag name 'generate_cv_tags.device_tags[name={generate_tag.name}] is invalid. "
                    "System Tags cannot be overridden. Try using a different name for this tag."
                )
                raise AristaAvdError(msg)

            # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
            if generate_tag.value is not None:
                value = generate_tag.value
            elif generate_tag.data_path is not None:
                value = get_v2(self.structured_config, generate_tag.data_path)
                if isinstance(value, (AvdList, AvdIndexedList, AvdModel)):
                    msg = (
                        f"'generate_cv_tags.device_tags[name={generate_tag.name}].data_path' ({generate_tag.data_path}) "
                        f"points to a list or dict. This is not supported for cloudvision tag data_paths."
                    )
                    raise AristaAvdError(msg)
            else:
                msg = f"'generate_cv_tags.device_tags[name={generate_tag.name}]' is missing either a static 'value' or a dynamic 'data_path'"
                raise AristaAvdError(msg)

            # Silently ignoring empty values since structured config may vary between devices.
            if value:
                self.structured_config.metadata.cv_tags.device_tags.append_new(name=generate_tag.name, value=str(value))

    def _set_interface_tags(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Set the data structure of interface_tags."""
        if (
            not (tags_to_generate := self.inputs.generate_cv_tags.interface_tags)
            and not self.shared_utils.is_cv_pathfinder_router
            and not self.shared_utils.is_campus_device
        ):
            return

        tags_of_subif_parent_interfaces: dict[str, EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags] = defaultdict(
            EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags
        )
        for ethernet_interface in self.structured_config.ethernet_interfaces:
            tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
            for generate_tag in tags_to_generate:
                # Get value from either 'value' key, structured config based on the 'data_path' key or raise.
                if generate_tag.value is not None:
                    value = generate_tag.value
                elif generate_tag.data_path is not None:
                    value = get_v2(ethernet_interface, generate_tag.data_path)
                    if isinstance(value, (AvdList, AvdIndexedList, AvdModel)):
                        msg = (
                            f"'generate_cv_tags.interface_tags[name={generate_tag.name}].data_path' ({generate_tag.data_path}) "
                            f"points to a variable of type {type(value).__name__}. This is not supported for cloudvision tag data_paths."
                        )
                        raise AristaAvdError(msg)
                else:
                    msg = f"'generate_cv_tags.interface_tags[name={generate_tag.name}]' is missing either a static 'value' or a dynamic 'data_path'"
                    raise AristaAvdError(msg)

                # Silently ignoring empty values since structured config may vary between devices.
                if value:
                    tags.append(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name=generate_tag.name, value=str(value)))

            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(ethernet_interface))

            if self.inputs.generate_cv_tags.topology_hints and self.shared_utils.is_campus_device:
                interface_campus_tags, subif_parent_interface_name = self._get_campus_interface_tags(ethernet_interface)
                # Process parent interface of the tagged sub-interface and stage assignment of all proposed sub-interface tags to the parent interface instead.
                if subif_parent_interface_name:
                    # Loop through all currently calculated tags and stage those which are unique.
                    # Same physical interface may be processed multiple times because it can be a parent of multiple sub-interfaces.
                    # append_unique allows to avoid duplication of the same tags.
                    for tag in tags:
                        tags_of_subif_parent_interfaces[subif_parent_interface_name].append_unique(tag)
                    # Loop through all currently calculated Campus tags and stage those which are unique.
                    for tag in interface_campus_tags:
                        tags_of_subif_parent_interfaces[subif_parent_interface_name].append_unique(tag)
                    continue
                # Other parts of the AVD code will add physical interfaces for all sub-interfaces into the self.structured_config.ethernet_interfaces.
                # Sub-interfaces will be processed here first. Physical interfaces will follow their sub-interfaces.
                # Process physical interface (added to ethernet_interfaces by other AVD logic) which is as well a parent for at least one tagged sub-interface.
                if ethernet_interface.name in tags_of_subif_parent_interfaces:
                    for tag in tags:
                        tags_of_subif_parent_interfaces[ethernet_interface.name].append_unique(tag)
                    for tag in interface_campus_tags:
                        tags_of_subif_parent_interfaces[ethernet_interface.name].append_unique(tag)
                    continue
                # All other cases
                tags.extend(interface_campus_tags)

            if tags:
                self.structured_config.metadata.cv_tags.interface_tags.append_new(interface=ethernet_interface.name, tags=tags)

        # Render tags if any sub-interface tags were staged for the assignment to the physical parent.
        if tags_of_subif_parent_interfaces:
            for subif_parent_interface, subif_parent_interface_tags in tags_of_subif_parent_interfaces.items():
                self.structured_config.metadata.cv_tags.interface_tags.append_new(interface=subif_parent_interface, tags=subif_parent_interface_tags)

        # Handle tags for management interface
        if self.inputs.generate_cv_tags.topology_hints and self.shared_utils.is_campus_device:
            for management_interface in self.structured_config.management_interfaces:
                tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
                tags.append_new(name="Link-Type", value="AVD-Managed")
                tags.append_new(name="Link-Type", value="Management")
                self.structured_config.metadata.cv_tags.interface_tags.append_new(interface=management_interface.name, tags=tags)

        # handle tags for L3 port-channel interfaces (cv_pathfinder use case)
        for port_channel_intf in self.structured_config.port_channel_interfaces:
            tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
            if self.shared_utils.is_cv_pathfinder_router:
                tags.extend(self._get_cv_pathfinder_interface_tags(port_channel_intf))
            if tags:
                self.structured_config.metadata.cv_tags.interface_tags.append_new(interface=port_channel_intf.name, tags=tags)

    def _get_cv_pathfinder_interface_tags(
        self: AvdStructuredConfigMetadataProtocol, generic_interface: EosCliConfigGen.EthernetInterfacesItem | EosCliConfigGen.PortChannelInterfacesItem
    ) -> EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags:
        """
        Return list of interface tags for cv_pathfinder solution.

        generic_interface is either ethernet or port_channel interface.

        Example: [
            {"name": "Type", <"lan" or "wan">},
            {"name": "Carrier", <value copied from wan_carrier if this is a wan interface>},
            {"name": "Circuit", <value copied from wan_circuit_id if this is a wan interface>}
        ].
        """
        if generic_interface.name in self.shared_utils.wan_interfaces:
            wan_interface = self.shared_utils.wan_interfaces[generic_interface.name]
            return self._get_cv_pathfinder_wan_interface_tags(wan_interface)
        if generic_interface.name in self.shared_utils.wan_port_channels:
            wan_port_channel_intf = self.shared_utils.wan_port_channels[generic_interface.name]
            return self._get_cv_pathfinder_wan_interface_tags(wan_port_channel_intf)

        tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        # Set Type lan for all other interfaces except port-channel members.
        if not (isinstance(generic_interface, EosCliConfigGen.EthernetInterfacesItem) and generic_interface.channel_group.id):
            tags.append_new(name="Type", value="lan")
        return tags

    # Generate wan interface tags while accounting for wan interface to be either L3 interface or L3 Port-Channel type
    def _get_cv_pathfinder_wan_interface_tags(
        self: AvdStructuredConfigMetadataProtocol,
        wan_interface: (
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
            | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
        ),
    ) -> EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags:
        """Return list of wan interface tags for cv_pathfinder solution for a given wan interface."""
        tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        tags.append_new(name="Type", value="wan")
        tags.append_new(name="Carrier", value=str(wan_interface.wan_carrier))
        if wan_interface.wan_circuit_id:
            tags.append_new(name="Circuit", value=str(wan_interface.wan_circuit_id))
        return tags

    def _get_campus_interface_tags(
        self: AvdStructuredConfigMetadataProtocol, generic_interface: EosCliConfigGen.EthernetInterfacesItem | EosCliConfigGen.PortChannelInterfacesItem
    ) -> tuple[EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags, str | None]:
        """
        Return list of Campus interface tags for a given interface of a Campus device.

        If the interface is a sub-interface, also return the name of the parent interface where the tags should eventually be applied.
        """
        tags = EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.Tags()
        tags.append_new(name="Link-Type", value="AVD-Managed")

        if interface_peer := generic_interface.peer:
            if interface_peer in self.shared_utils.all_fabric_devices:
                tags.append_new(name="Link-Type", value="Fabric")

            if generic_interface.peer_type == "mlag_peer":
                tags.append_new(name="Link-Type", value="MLAG")
            elif self.facts.uplink_peers and interface_peer in self.facts.uplink_peers:
                tags.append_new(name="Link-Type", value="Uplink")
            elif self.facts.downlink_switches and interface_peer in self.facts.downlink_switches:
                tags.append_new(name="Link-Type", value="Downlink")

        if campus_link_types := get_v2(generic_interface._internal_data, "campus_link_type", []):
            for campus_link_type in campus_link_types:
                if campus_link_type := CAMPUS_LINK_TYPE_MAP.get(campus_link_type):
                    tags.append_unique(EosCliConfigGen.Metadata.CvTags.InterfaceTagsItem.TagsItem(name="Link-Type", value=campus_link_type))

        if "." in generic_interface.name:
            return tags, generic_interface.name.split(".", maxsplit=1)[0]
        return tags, None
