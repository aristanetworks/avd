from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.esi_management import generate_esi, generate_lacp_id, generate_route_target
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from .utils import UtilsMixin


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def port_channel_interfaces(self) -> dict | None:
        """
        Return structured config for port_channel_interfaces
        """
        port_channel_interfaces = {}
        port_channel_list = []
        for link in self._underlay_links:
            if get(link, "type") != "underlay_l2":
                continue

            if (channel_group_id := get(link, "channel_group_id")) in port_channel_list:
                continue

            port_channel_list.append(channel_group_id)

            port_channel_interface = {
                "description": self._avd_interface_descriptions.underlay_port_channel_interfaces(
                    get(link, "peer"), get(link, "peer_channel_group_id"), get(link, "channel_description")
                ),
                "speed": get(link, "speed"),
                "type": "switched",
                "shutdown": False,
                "mode": "trunk",
                "service_profile": get(self._hostvars, "p2p_uplinks_qos_profile"),
                "link_tracking_groups": get(link, "link_tracking_groups"),
            }

            if (trunk_groups := get(link, "trunk_groups")) is not None:
                port_channel_interface["trunk_groups"] = trunk_groups
            elif (vlans := get(link, "vlans")) is not None:
                port_channel_interface["vlans"] = vlans

            if self._mlag is True:
                port_channel_interface["mlag"] = int(get(link, "channel_group_id"))
            # TODO - why is it elif in original Jinja template
            if (short_esi := get(link, "short_esi")) is not None:
                port_channel_interface["evpn_ethernet_segment"] = {
                    "identifier": generate_esi(short_esi, self._evpn_short_esi_prefix),
                    "route_target": generate_route_target(short_esi),
                }
                port_channel_interface["lacp_id"] = generate_lacp_id(short_esi)

            # Structured Config
            port_channel_interface.update(default(get(link, "structured_config"), {}))

            # Remove None values
            port_channel_interface = {key: value for key, value in port_channel_interface.items() if value is not None}

            port_channel_interfaces[f"Port-Channel{link['channel_group_id']}"] = port_channel_interface

        if port_channel_interfaces:
            return port_channel_interfaces

        return None
