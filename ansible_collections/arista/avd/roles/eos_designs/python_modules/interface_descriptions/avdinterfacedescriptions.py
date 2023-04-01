from collections import ChainMap

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class AvdInterfaceDescriptions(AvdFacts, UtilsMixin):

    """
    Class used to render Interface Descriptions either from custom Jinja2 templates or using default Python Logic

    Since some templates might contain certain legacy variables (switch_*),
    those are mapped from the switch.* model

    This class is imported adhoc based on the variable `templates.interface_descriptions.python_module` so it can
    be overridden by a custom python class.
    """

    def _template(self, template_path, **kwargs):
        template_vars = ChainMap(kwargs, self._hostvars)
        return self.template_var(template_path, template_vars)

    def underlay_ethernet_interfaces(self, link_type: str, link_peer: str, link_peer_interface: str) -> str:
        if template_path := self._interface_descriptions_templates.get("underlay_ethernet_interfaces"):
            return self._template(
                template_path,
                link={
                    "type": link_type,
                    "peer": link_peer,
                    "peer_interface": link_peer_interface,
                },
            )

        link_peer = str(link_peer).upper()
        if link_type == "underlay_p2p":
            return f"P2P_LINK_TO_{link_peer}_{link_peer_interface}"

        if link_type == "underlay_l2":
            return f"{link_peer}_{link_peer_interface}"

        return ""

    def underlay_port_channel_interfaces(
        self,
        link_peer: str,
        link_peer_channel_group_id: int,
        link_channel_description: str,
    ) -> str:
        if template_path := self._interface_descriptions_templates.get("underlay_port_channel_interfaces"):
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

    def mlag_ethernet_interfaces(self, mlag_interface: str) -> str:
        if template_path := self._interface_descriptions_templates.get("mlag_ethernet_interfaces"):
            return self._template(template_path, mlag_interface=mlag_interface)

        return f"MLAG_PEER_{self._mlag_peer}_{mlag_interface}"

    def mlag_port_channel_interfaces(self) -> str:
        if template_path := self._interface_descriptions_templates.get("mlag_port_channel_interfaces"):
            return self._template(template_path)

        return f"MLAG_PEER_{self._mlag_peer}_Po{self._mlag_port_channel_id}"

    def connected_endpoints_ethernet_interfaces(self, peer: str = None, peer_interface: str = None) -> str:
        if template_path := self._interface_descriptions_templates.get("connected_endpoints_ethernet_interfaces"):
            return self._template(template_path, peer=peer, peer_interface=peer_interface)

        elements = [peer, peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interfaces(self, peer: str = None, adapter_port_channel_description: str = None) -> str:
        if template_path := self._interface_descriptions_templates.get("connected_endpoints_port_channel_interfaces"):
            return self._template(
                template_path,
                peer=peer,
                adapter_port_channel_description=adapter_port_channel_description,
            )

        elements = [peer, adapter_port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def overlay_loopback_interface(self, overlay_loopback_description: str = None) -> str:
        if template_path := self._interface_descriptions_templates.get("overlay_loopback_interface"):
            return self._template(template_path, overlay_loopback_description=overlay_loopback_description)

        if overlay_loopback_description is not None:
            return overlay_loopback_description

        if self._default_mpls_overlay_role in ["server", "client"]:
            return "MPLS_Overlay_peering"

        if self._mpls_lsr is True:
            return "LSR_Router_ID"

        # Covers L2LS
        if get(self._hostvars, "switch.overlay_routing_protocol") == "none":
            return "Router_ID"

        # Note that the current code will render this for HER and others
        return "EVPN_Overlay_Peering"

    def vtep_loopback_interface(self) -> str:
        if template_path := self._interface_descriptions_templates.get("vtep_loopback_interface"):
            return self._template(template_path)

        return "VTEP_VXLAN_Tunnel_Source"
