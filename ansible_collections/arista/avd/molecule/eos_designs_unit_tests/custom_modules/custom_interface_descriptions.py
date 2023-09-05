# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import AvdInterfaceDescriptions


class CustomAvdInterfaceDescriptions(AvdInterfaceDescriptions):
    @cached_property
    def _custom_description_prefix(self):
        return get(self._hostvars, "description_prefix", "")

    @cached_property
    def _switch_type(self):
        return get(self._hostvars, "switch.type", "")

    def underlay_ethernet_interfaces(self, link_type: str, link_peer: str, link_peer_interface: str) -> str:
        """
        Implementation of custom code similar to jinja in
        custom_templates/interface_descriptions/underlay/ethernet-interfaces.j2
        """
        link_peer = str(link_peer).upper()
        if link_type == "underlay_p2p":
            return f"{self._custom_description_prefix}_P2P_LINK_TO_{link_peer}_{link_peer_interface}"

        if link_type == "underlay_l2":
            return f"{self._custom_description_prefix}_{link_peer}_{link_peer_interface}"

        return ""

    def underlay_port_channel_interfaces(self, link_peer: str, link_peer_channel_group_id: int, link_channel_description: str) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/underlay/port-channel-interfaces.j2
        """
        if link_channel_description is not None:
            link_channel_description = str(link_channel_description).upper()
            return f"{self._custom_description_prefix}_{link_channel_description}_Po{link_peer_channel_group_id}"

        link_peer = str(link_peer).upper()
        return f"{self._custom_description_prefix}_{link_peer}_Po{link_peer_channel_group_id}"

    def mlag_ethernet_interfaces(self, mlag_interface: str) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/mlag/ethernet-interfaces.j2
        """
        return f"{self._custom_description_prefix}_MLAG_PEER_{self._mlag_peer}_{mlag_interface}"

    def mlag_port_channel_interfaces(self) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/mlag/port-channel-interfaces.j2
        """
        return f"{self._custom_description_prefix}_MLAG_PEER_{self._mlag_peer}_Po{self._mlag_port_channel_id}"

    def connected_endpoints_ethernet_interfaces(self, peer: str = None, peer_interface: str = None) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/connected-endpoints/ethernet-interfaces.j2
        """
        elements = [peer, peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interfaces(self, peer: str = None, adapter_port_channel_description: str = None) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/connected-endpoints/port-channel-interfaces.j2
        """
        elements = [self._custom_description_prefix, peer, adapter_port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def overlay_loopback_interface(self, overlay_loopback_description: str = None) -> str:
        """
        Implementation of custom code similar to jinja:
        custom_templates/interface_descriptions/loopbacks/overlay-loopback.j2
        """
        switch_type = str(self._switch_type).upper()
        return f"{self._custom_description_prefix}_EVPN_Overlay_Peering_{switch_type}"

    def vtep_loopback_interface(self) -> str:
        """
        Implementation of custom code similar to jinja:
        """
        switch_type = str(self._switch_type).upper()
        return f"{self._custom_description_prefix}_VTEP_VXLAN_Tunnel_Source_{switch_type}"
