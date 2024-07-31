# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD eos_designs base module to generate interface descriptions.
Can be subclassed to customize interface descriptions on a per need basis.
"""

from __future__ import annotations

from collections import ChainMap
from typing import TYPE_CHECKING, Any

from pyavd._eos_designs.avdfacts import AvdFacts

from ..avdfacts import AvdFacts
from .models import InterfaceDescriptionData

if TYPE_CHECKING:
    from .models import InterfaceDescriptionData


class AvdInterfaceDescriptions(AvdFacts):
    """
    Class used to render Interface Descriptions either from custom Jinja2 templates or using default Python Logic.

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

    def _template(self, template_path: str, **kwargs: Any) -> str:
        template_vars = ChainMap(kwargs, self._hostvars)
        return self.shared_utils.template_var(template_path, template_vars)

    def underlay_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Called for each underlay ethernet interface.

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
            - wan_circuit_id.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_ethernet_interfaces"):
            return self._template(
                template_path,
                link={
                    "type": data.link_type,
                    "peer": data.peer,
                    "peer_interface": data.peer_interface,
                },
            )

        if data.link_type == "underlay_p2p":
            # TODO should we keep this upper?
            if data.peer:
                link_peer = str(data.peer).upper()
            desc = f"P2P_LINK_TO_{link_peer}_{data.peer_interface}"
        elif data.link_type == "underlay_l2":
            desc = f"{data.peer}_{data.peer_interface}"
        else:
            elems = [data.wan_carrier, data.wan_circuit_id, data.peer, data.peer_interface]
            desc = "_".join([elem for elem in elems if elem])

        return f"{desc}_vrf_{data.vrf}" if data.vrf is not None else desc

    def underlay_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Called for each underlay port-channel interface.

        Available data:
            - peer
            - peer_channel_group_id
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("underlay_port_channel_interfaces"):
            return self._template(
                template_path,
                link={
                    "peer": data.peer,
                    "peer_channel_group_id": data.peer_channel_group_id,
                    "channel_description": data.port_channel_description,
                },
            )

        if data.port_channel_description is not None:
            data.port_channel_description = str(data.port_channel_description).upper()
            return f"{data.port_channel_description}_Po{data.peer_channel_group_id}"

        data.peer = str(data.peer).upper()
        return f"{data.peer}_Po{data.peer_channel_group_id}"

    def mlag_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Called for each mlag ethernet interface.

        Available data:
            - peer
            - peer_interface
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_ethernet_interfaces"):
            return self._template(template_path, mlag_interface=data.peer_interface)

        return f"MLAG_PEER_{data.peer}_{data.peer_interface}"

    def mlag_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Called for each mlag port-channel interface.

        Available data:
            - peer
            - peer_channel_group_id
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("mlag_port_channel_interfaces"):
            return self._template(template_path)

        return f"MLAG_PEER_{data.peer}_Po{data.peer_channel_group_id}"

    def connected_endpoints_ethernet_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build a connected endpoint Ethernet interface description.

        If a jinja template is configured, use it.
        If not, use the adapter.description or default to <PEER>_<PEER_INTERFACE>

        Available data:
            - peer
            - peer_interface
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_ethernet_interfaces"):
            return self._template(template_path, peer=data.peer, peer_interface=data.peer_interface, adapter_description=data.description)

        if data.description:
            return data.description

        elements = [data.peer, data.peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build a connected endpoint Port-channel description.

        If a jinja template is configured, use it.
        If not, return the <adapter.description>_<port_channel_description> or
        default to <PEER>_<adapter_port_channel_description>

        Available data:
            - peer
            - description
            - port_channel_description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("connected_endpoints_port_channel_interfaces"):
            return self._template(
                template_path,
                peer=data.peer,
                adapter_port_channel_description=data.port_channel_description,
                adapter_description=data.description,
            )

        elements = [data.description or data.peer, data.port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def router_id_loopback_interface(self, data: InterfaceDescriptionData) -> str:
        """
        Build Router ID loopback interface description.

        Available data:
            - description
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type.
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("overlay_loopback_interface"):
            return self._template(template_path, overlay_loopback_description=data.description)

        if data.description is not None:
            return data.description

        if data.mpls_overlay_role in ["server", "client"]:
            return "MPLS_Overlay_peering"

        if data.mpls_lsr is True:
            return "LSR_Router_ID"

        if self.shared_utils.is_wan_router:
            return "Router_ID"

        # Covers L2LS
        if data.overlay_routing_protocol == "none":
            return "Router_ID"

        # Note that the current code will render this for HER and others
        return "EVPN_Overlay_Peering"

    def vtep_loopback_interface(
        self,
        data: InterfaceDescriptionData,  # pylint: disable=unused-argument # NOSONAR # noqa: ARG002
    ) -> str:
        """
        Build Router ID loopback interface description.

        Available data:
            - mpls_overlay_role
            - mpls_lsr
            - overlay_routing_protocol
            - type
        """
        if template_path := self.shared_utils.interface_descriptions_templates.get("vtep_loopback_interface"):
            return self._template(template_path)

        return "VTEP_VXLAN_Tunnel_Source"
