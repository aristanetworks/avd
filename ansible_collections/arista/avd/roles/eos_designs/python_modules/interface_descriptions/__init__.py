import importlib
from collections import ChainMap
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import AristaAvdError, get

DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE = "ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions"
DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME = "AvdInterfaceDescriptions"


class AvdInterfaceDescriptions(AvdFacts):

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

    @cached_property
    def _default_mpls_overlay_role(self) -> str:
        return get(self._hostvars, "switch.default_mpls_overlay_role")

    @cached_property
    def _mpls_lsr(self) -> str:
        return get(self._hostvars, "switch.mpls_lsr")

    @cached_property
    def _mlag_peer(self) -> str:
        return get(self._hostvars, "switch.mlag_peer", required=True)

    @cached_property
    def _mlag_port_channel_id(self) -> str:
        return get(self._hostvars, "switch.mlag_port_channel_id", required=True)

    def underlay_ethernet_interfaces(self, link_type: str, link_peer: str, link_peer_interface: str) -> str:
        if template_path := get(self._hostvars, "switch.interface_descriptions.underlay_ethernet_interfaces"):
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
        if template_path := get(
            self._hostvars,
            "switch.interface_descriptions.underlay_port_channel_interfaces",
        ):
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
        if template_path := get(self._hostvars, "switch.interface_descriptions.mlag_ethernet_interfaces"):
            return self._template(template_path, mlag_interface=mlag_interface)

        return f"MLAG_PEER_{self._mlag_peer}_{mlag_interface}"

    def mlag_port_channel_interfaces(self) -> str:
        if template_path := get(self._hostvars, "switch.interface_descriptions.mlag_port_channel_interfaces"):
            return self._template(template_path)

        return f"MLAG_PEER_{self._mlag_peer}_Po{self._mlag_port_channel_id}"

    def connected_endpoints_ethernet_interfaces(self, peer: str = None, peer_interface: str = None) -> str:
        if template_path := get(
            self._hostvars,
            "switch.interface_descriptions.connected_endpoints_ethernet_interfaces",
        ):
            return self._template(template_path, peer=peer, peer_interface=peer_interface)

        elements = [peer, peer_interface]
        return "_".join([str(element) for element in elements if element is not None])

    def connected_endpoints_port_channel_interfaces(self, peer: str = None, adapter_port_channel_description: str = None) -> str:
        if template_path := get(
            self._hostvars,
            "switch.interface_descriptions.connected_endpoints_port_channel_interfaces",
        ):
            return self._template(
                template_path,
                peer=peer,
                adapter_port_channel_description=adapter_port_channel_description,
            )

        elements = [peer, adapter_port_channel_description]
        return "_".join([str(element) for element in elements if element is not None])

    def overlay_loopback_interface(self, overlay_loopback_description) -> str:
        if template_path := get(self._hostvars, "switch.interface_descriptions.overlay_loopback_interface"):
            return self._template(template_path, overlay_loopback_description=overlay_loopback_description)

        if overlay_loopback_description is not None:
            return overlay_loopback_description

        if self._default_mpls_overlay_role in ["server", "client"]:
            return "MPLS_Overlay_peering"

        if self._mpls_lsr is True:
            return "LSR_Router_ID"

        return "EVPN_Overlay_Peering"

    def vtep_loopback_interface(self) -> str:
        if template_path := get(self._hostvars, "switch.interface_descriptions.vtep_loopback_interface"):
            return self._template(template_path)

        return "VTEP_VXLAN_Tunnel_Source"


def load_interfacedescriptions(hostvars, templar) -> AvdInterfaceDescriptions:
    """
    Load the python_module defined in `templates.interface_descriptions.python_module`
    Return the class defined by `templates.interface_descriptions.python_class_name`
    """
    module_path = get(
        hostvars,
        "switch.interface_descriptions.python_module",
        default=DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_MODULE,
    )
    class_name = get(
        hostvars,
        "switch.interface_descriptions.python_class_name",
        default=DEFAULT_AVD_INTERFACE_DESCRIPTIONS_PYTHON_CLASS_NAME,
    )
    try:
        cls = getattr(importlib.import_module(module_path), class_name)
    except ImportError as imp_exc:
        raise AristaAvdError(imp_exc) from imp_exc

    # if not isinstance(cls, AvdInterfaceDescriptions):
    if not issubclass(cls, AvdInterfaceDescriptions):
        raise AristaAvdError(f"{cls} is not a subclass of AvdInterfaceDescriptions class")

    return cls(hostvars=hostvars, templar=templar)
