# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections import ChainMap

from ..avdfacts import AvdFacts
from .models import InterfaceDescriptionData
from .utils import UtilsMixin


class AvdInterfaceDescriptions(AvdFacts, UtilsMixin):
    """
    Class used to render Interface Descriptions either from custom Jinja2 templates or using default Python Logic

    Since some templates might contain certain legacy variables (switch_*),
    those are mapped from the switch.* model

    This class is imported adhoc based on the variable `templates.interface_descriptions.python_module` so it can
    be overridden by a custom python class.

    Attributes starting with _ are internal and may change at any time.

    Other attributes are "stable" and changes follow semver practices:
    - Existing attributes will not be changed in terms of type and value, but the underlying code for cached_properties may change.
    - New attributes may be added in minor releases.
    - The __init__ method may change between minor versions as the data may need to be consumed from other sources.
    - Breaking changes may happen between major releases or in rare cases for bug fixes.
    """

    def _template(self, template_path, **kwargs):
        template_vars = ChainMap(kwargs, self._hostvars)
        return self.shared_utils.template_var(template_path, template_vars)

    def underlay_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - link_type
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
            - vrf
            - wan_carrier
            - wan_circuit_id
        """
        desc = self.underlay_ethernet_interfaces(
            link_type=data.link_type,
            link_peer=data.peer,
            link_peer_interface=data.peer_interface,
        )

        if not desc:
            elems = [data.wan_carrier, data.wan_circuit_id, data.peer, data.peer_interface]
            desc = "_".join([elem for elem in elems if elem])

        return f"{desc}_vrf_{data.vrf}" if data.vrf is not None else desc

    def underlay_ethernet_interfaces(self, link_type: str, link_peer: str, link_peer_interface: str) -> str:
        """TODO: AVD5.0.0 move this to the new function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_ethernet_interfaces"):
            return self._template(
                template_path,
                link={
                    "type": link_type,
                    "peer": link_peer,
                    "peer_interface": link_peer_interface,
                },
            )

        if link_peer:
            link_peer = str(link_peer).upper()
        if link_type == "underlay_p2p":
            return f"P2P_LINK_TO_{link_peer}_{link_peer_interface}"

        if link_type == "underlay_l2":
            return f"{link_peer}_{link_peer_interface}"

        return ""

    def underlay_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - peer
            - peer_channel_group_id
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.underlay_port_channel_interfaces(
            link_peer=data.peer, link_peer_channel_group_id=data.peer_channel_group_id, link_channel_description=data.port_channel_description
        )

    def underlay_port_channel_interfaces(self, link_peer: str, link_peer_channel_group_id: int, link_channel_description: str) -> str:
        """TODO: AVD5.0.0 move this to the new function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_port_channel_interfaces"):
            return self._template(
                template_path,
                link={
                    "peer": link_peer,
                    "peer_channel_group_id": link_peer_channel_group_id,
                    "channel_description": link_channel_description,
                },
            )

        if link_channel_description is not None:
            link_channel_description = str(link_channel_description).upper()
            return f"{link_channel_description}_Po{link_peer_channel_group_id}"

        link_peer = str(link_peer).upper()
        return f"{link_peer}_Po{link_peer_channel_group_id}"

    def mlag_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.mlag_ethernet_interfaces(mlag_interface=data.peer_interface)

    def mlag_ethernet_interfaces(self, mlag_interface: str) -> str:
        """TODO: AVD5.0.0 move this to the new function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_ethernet_interfaces"):
            return self._template(template_path, mlag_interface=mlag_interface)

        return f"MLAG_PEER_{self._mlag_peer}_{mlag_interface}"

    def mlag_port_channel_interface(
        self,
        data: InterfaceDescriptionData,  # pylint: disable=unused-argument
    ) -> str:
        """
        Available data:
            - mlag_peer
            - peer_channel_group_id
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.mlag_port_channel_interfaces()

    def mlag_port_channel_interfaces(self) -> str:
        """TODO: AVD5.0.0 move this to the new function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_port_channel_interfaces"):
            return self._template(template_path)

        return f"MLAG_PEER_{self._mlag_peer}_Po{self._mlag_port_channel_id}"

    def connected_endpoints_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - peer
            - peer_interface
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.connected_endpoints_ethernet_interfaces(peer=data.peer, peer_interface=data.peer_interface, adapter_description=data.description)

    def connected_endpoints_ethernet_interfaces(self, peer: str = None, peer_interface: str = None, adapter_description: str = None) -> str:
        """
        If a jinja template is configured, use it.
        If not, use the adapter.description or default to <PEER>_<PEER_INTERFACE>
        TODO: AVD5.0.0 move this to the new function.
        """

        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_ethernet_interfaces"):
            return self._template(template_path, peer=peer, peer_interface=peer_interface, adapter_description=adapter_description)

        if adapter_description:
            return adapter_description

        elements = [peer, peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - peer
            - description
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.connected_endpoints_port_channel_interfaces(
            peer=data.peer, adapter_description=data.description, adapter_port_channel_description=data.port_channel_description
        )

    def connected_endpoints_port_channel_interfaces(
        self, peer: str = None, adapter_description: str = None, adapter_port_channel_description: str = None
    ) -> str:
        """If a jinja template is configured, use it.
        If not, return the <adapter.description>_<port_channel_description> or
        default to <PEER>_<adapter_port_channel_description>
        TODO: AVD5.0.0 move this to the new function.
        """

        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_port_channel_interfaces"):
            return self._template(
                template_path,
                peer=peer,
                adapter_port_channel_description=adapter_port_channel_description,
                adapter_description=adapter_description,
            )

        elements = [adapter_description or peer, adapter_port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def router_id_loopback_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Available data:
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        return self.overlay_loopback_interface(overlay_loopback_description=data.description)

    def overlay_loopback_interface(self, overlay_loopback_description: str = None) -> str:
        """TODO: AVD5.0.0 move this to the new function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("overlay_loopback_interface"):
            return self._template(template_path, overlay_loopback_description=overlay_loopback_description)

        if overlay_loopback_description is not None:
            return overlay_loopback_description

        if self._mpls_overlay_role in ["server", "client"]:
            return "MPLS_Overlay_peering"

        if self._mpls_lsr is True:
            return "LSR_Router_ID"

        if self.shared_utils.is_wan_router:
            return "Router_ID"

        # Covers L2LS
        if self._overlay_routing_protocol == "none":
            return "Router_ID"

        # Note that the current code will render this for HER and others
        return "EVPN_Overlay_Peering"

    def vtep_loopback_interface(self) -> str:
        """TODO: AVD5.0.0 add data: InterfaceDescriptionData to the function."""
        if template_path := self.shared_utils.interface_descriptions_templates.get("vtep_loopback_interface"):
            return self._template(template_path)

        return "VTEP_VXLAN_Tunnel_Source"
