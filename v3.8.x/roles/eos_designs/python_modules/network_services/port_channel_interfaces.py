from __future__ import annotations

import re
from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.esi_management import generate_esi, generate_lacp_id, generate_route_target
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

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

        Only used with L1 network services
        """

        if not self._network_services_l1:
            return None

        # Using temp variables to keep the order of interfaces from Jinja
        port_channel_interfaces = {}
        subif_parent_interfaces = {}

        for tenant in self._filtered_tenants:
            if "point_to_point_services" not in tenant:
                continue

            for point_to_point_service in natural_sort(tenant["point_to_point_services"], "name"):
                if subifs := point_to_point_service.get("subinterfaces", []):
                    subifs = [subif for subif in subifs if subif.get("number") is not None]
                for endpoint in point_to_point_service.get("endpoints", []):
                    if self._hostname not in endpoint.get("nodes", []):
                        continue

                    node_index = list(endpoint["nodes"]).index(self._hostname)
                    interface_name = endpoint["interfaces"][node_index]
                    if (port_channel_mode := get(endpoint, "port_channel.mode")) not in ["active", "on"]:
                        continue

                    channel_group_id = "".join(re.findall(r"\d", interface_name))
                    interface_name = f"Port-Channel{channel_group_id}"
                    if subifs:
                        # This is a subinterface so we need to ensure that the parent is created
                        parent_interface = {
                            "type": "routed",
                            "peer_type": "l3_interface",
                            "shutdown": False,
                        }
                        if (short_esi := get(endpoint, "port_channel.short_esi")) is not None:
                            if len(short_esi.split(":")) == 3:
                                parent_interface["esi"] = generate_esi(short_esi, self._evpn_short_esi_prefix)
                                parent_interface["rt"] = generate_route_target(short_esi)
                                if port_channel_mode == "active":
                                    parent_interface["lacp_id"] = generate_lacp_id(short_esi)

                        subif_parent_interfaces[interface_name] = parent_interface

                        for subif in subifs:
                            key = f"{interface_name}.{subif['number']}"
                            port_channel_interfaces[key] = {
                                "type": "l2dot1q",
                                "encapsulation_vlan": {
                                    "client": {
                                        "dot1q": {
                                            "vlan": subif["number"],
                                        },
                                    },
                                    "network": {
                                        "client": True,
                                    },
                                },
                                "peer_type": "l3_interface",
                                "shutdown": False,
                            }
                    else:
                        interface = {
                            "type": "routed",
                            "peer_type": "l3_interface",
                            "shutdown": False,
                        }
                        if point_to_point_service.get("lldp_disable") is True:
                            interface["lldp"] = {
                                "transmit": False,
                                "receive": False,
                            }

                        if (short_esi := get(endpoint, "port_channel.short_esi")) is not None:
                            if len(short_esi.split(":")) == 3:
                                interface["esi"] = generate_esi(short_esi, self._evpn_short_esi_prefix)
                                interface["rt"] = generate_route_target(short_esi)
                                if port_channel_mode == "active":
                                    interface["lacp_id"] = generate_lacp_id(short_esi)
                        port_channel_interfaces[interface_name] = interface

            subif_parent_interfaces = {key: value for key, value in subif_parent_interfaces.items() if key not in port_channel_interfaces}
            if subif_parent_interfaces:
                port_channel_interfaces.update(subif_parent_interfaces)

        if port_channel_interfaces:
            return port_channel_interfaces

        return None
