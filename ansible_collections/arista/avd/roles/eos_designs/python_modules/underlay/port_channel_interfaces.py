from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.esi_management import generate_esi, generate_lacp_id, generate_route_target

from .utils import UtilsMixin


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def port_channel_interfaces(self) -> list | None:
        """
        Return structured config for port_channel_interfaces
        """
        port_channel_interfaces = []
        port_channel_list = []
        for link in self._underlay_links:
            if link["type"] != "underlay_l2":
                continue

            if (channel_group_id := link.get("channel_group_id")) in port_channel_list:
                continue

            port_channel_list.append(channel_group_id)

            port_channel_name = f"Port-Channel{link['channel_group_id']}"

            port_channel_interface = {
                "name": port_channel_name,
                "description": self.shared_utils.interface_descriptions.underlay_port_channel_interfaces(
                    link["peer"], link["peer_channel_group_id"], link.get("channel_description")
                ),
                "type": "switched",
                "shutdown": False,
                "mode": "trunk",
                "service_profile": self.shared_utils.p2p_uplinks_qos_profile,
                "link_tracking_groups": link.get("link_tracking_groups"),
                "native_vlan": link.get("native_vlan"),
            }

            if (trunk_groups := link.get("trunk_groups")) is not None:
                port_channel_interface["trunk_groups"] = trunk_groups
            elif (vlans := link.get("vlans")) is not None:
                port_channel_interface["vlans"] = vlans

            if self.shared_utils.mlag is True:
                port_channel_interface["mlag"] = int(link.get("channel_group_id"))

            if (short_esi := link.get("short_esi")) is not None:
                port_channel_interface["evpn_ethernet_segment"] = {
                    "identifier": generate_esi(short_esi, self.shared_utils.evpn_short_esi_prefix),
                    "route_target": generate_route_target(short_esi),
                }
                port_channel_interface["lacp_id"] = generate_lacp_id(short_esi)

            # Structured Config
            port_channel_interface["struct_cfg"] = link.get("structured_config")

            # Remove None values
            port_channel_interface = {key: value for key, value in port_channel_interface.items() if value is not None}

            port_channel_interfaces.append(port_channel_interface)

        if port_channel_interfaces:
            return port_channel_interfaces

        return None
