from __future__ import annotations

import re
from collections import ChainMap
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from .utils import UtilsMixin


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ethernet_interfaces(self) -> dict | None:
        """
        Return structured config for ethernet_interfaces
        """
        ethernet_interfaces = {}
        for connected_endpoint in self._filtered_connected_endpoints:
            for adapter in connected_endpoint["adapters"]:
                for node_index, node_name in enumerate(adapter["switches"]):
                    if node_name != self._hostname:
                        continue

                    ethernet_interface_name = adapter["switch_ports"][node_index]
                    ethernet_interfaces[ethernet_interface_name] = self._get_ethernet_interface_cfg(adapter, node_index, connected_endpoint)

        for network_port in self._filtered_network_ports:
            connected_endpoint = {
                "name": network_port.get("description"),
                "type": "network_port",
            }
            for ethernet_interface_name in range_expand(network_port["switch_ports"]):
                # Override switches and switch_ports to only render for a single interface
                tmp_network_port = ChainMap(
                    {
                        "switch_ports": [ethernet_interface_name],
                        "switches": [self._hostname],
                    },
                    network_port,
                )
                ethernet_interfaces[ethernet_interface_name] = self._get_ethernet_interface_cfg(tmp_network_port, 0, connected_endpoint)

        if ethernet_interfaces:
            return ethernet_interfaces

        return None

    def _get_ethernet_interface_cfg(self, adapter: dict, node_index: int, connected_endpoint: dict) -> dict:
        """
        Return structured_config for one ethernet_interface
        """
        peer = connected_endpoint["name"]
        endpoint_ports: list = default(
            adapter.get("endpoint_ports"),
            adapter.get("server_ports"),
            [],
        )
        peer_interface = endpoint_ports[node_index] if node_index < len(endpoint_ports) else None
        default_channel_group_id = int("".join(re.findall(r"\d", adapter["switch_ports"][0])))
        channel_group_id = get(adapter, "port_channel.channel_id", default=default_channel_group_id)
        short_esi = self._get_short_esi(adapter, channel_group_id)

        # Common ethernet_interface settings
        # TODO: avoid generating redundant structured config for port-channel members
        ethernet_interface = {
            "peer": peer,
            "peer_interface": peer_interface,
            "peer_type": connected_endpoint["type"],
            "description": self._avd_interface_descriptions.connected_endpoints_ethernet_interfaces(peer, peer_interface, adapter.get("description")),
            "speed": adapter.get("speed"),
            "mtu": adapter.get("mtu"),
            "l2_mtu": adapter.get("l2_mtu"),
            "type": "switched",
            "shutdown": not adapter.get("enabled", True),
            "mode": adapter.get("mode"),
            "vlans": adapter.get("vlans"),
            "trunk_groups": self._get_adapter_trunk_groups(adapter, connected_endpoint),
            "native_vlan_tag": adapter.get("native_vlan_tag"),
            "native_vlan": adapter.get("native_vlan"),
            "spanning_tree_portfast": adapter.get("spanning_tree_portfast"),
            "spanning_tree_bpdufilter": adapter.get("spanning_tree_bpdufilter"),
            "spanning_tree_bpduguard": adapter.get("spanning_tree_bpduguard"),
            "storm_control": self._get_adapter_storm_control(adapter),
            "service_profile": adapter.get("qos_profile"),
            "dot1x": adapter.get("dot1x"),
            "ptp": self._get_adapter_ptp(adapter),
            "eos_cli": adapter.get("raw_eos_cli"),
            "struct_cfg": adapter.get("structured_config"),
        }

        # Port-channel member
        if (port_channel_mode := get(adapter, "port_channel.mode")) is not None:
            ethernet_interface["channel_group"] = {
                "id": channel_group_id,
                "mode": port_channel_mode,
            }
            if get(adapter, "port_channel.lacp_fallback.mode") == "static":
                ethernet_interface["lacp_port_priority"] = 8192 if node_index == 0 else 32768

        # NOT a port-channel member
        else:
            ethernet_interface.update(
                {
                    "evpn_ethernet_segment": self._get_adapter_evpn_ethernet_segment_cfg(
                        adapter, short_esi, node_index, connected_endpoint, "auto", "single-active"
                    ),
                    "link_tracking_groups": self._get_adapter_link_tracking_groups(adapter),
                }
            )

        # More common ethernet_interface settings
        if (flowcontrol_received := get(adapter, "flowcontrol.received")) is not None:
            ethernet_interface["flowcontrol"] = {"received": flowcontrol_received}

        return strip_null_from_data(ethernet_interface)
