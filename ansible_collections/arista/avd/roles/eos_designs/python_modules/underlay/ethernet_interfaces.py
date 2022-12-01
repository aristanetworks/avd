from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
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
        for link in natural_sort(self._underlay_links, "interface"):
            # common values
            ethernet_interface = {
                "peer": get(link, "peer"),
                "peer_interface": link["peer_interface"],
                "peer_type": link["peer_type"],
                "description": self._avd_interface_descriptions.underlay_ethernet_interfaces(get(link, "type"), get(link, "peer"), link["peer_interface"]),
                "speed": get(link, "speed"),
                "shutdown": self._shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
            }

            # L3 interface
            if get(link, "type") == "underlay_p2p":
                ethernet_interface.update(
                    {
                        "mtu": self._p2p_uplinks_mtu,
                        "service_profile": get(self._hostvars, "p2p_uplinks_qos_profile"),
                        "ptp": get(link, "ptp"),
                        "mac_security": get(link, "mac_security"),
                        "type": "routed",
                        "ipv6_enable": get(link, "ipv6_enable"),
                        "link_tracking_groups": get(link, "link_tracking_groups"),
                    }
                )

                # MPLS
                if self._mpls_lsr is True:
                    mpls_dict = {"ip": True}
                    if self._ldp is True:
                        mpls_dict["ldp"] = {"interface": True, "igp_sync": True}

                    ethernet_interface["mpls"] = mpls_dict

                # IP address
                if get(link, "ip_address") is not None:
                    if "unnumbered" in link["ip_address"].lower():
                        ethernet_interface["ip_address"] = link["ip_address"]
                    else:
                        ethernet_interface["ip_address"] = f"{link['ip_address']}/31"

                if self._underlay_routing_protocol == "ospf":
                    ethernet_interface["ospf_network_point_to_point"] = True
                    ethernet_interface["ospf_area"] = self._underlay_ospf_area

                if self._underlay_routing_protocol == "isis":
                    ethernet_interface.update(
                        {
                            "isis_enable": self._isis_instance_name,
                            "isis_metric": default(get(self._hostvars, "isis_default_metric"), 50),
                            "isis_network_point_to_point": True,
                            "isis_circuit_type": get(self._hostvars, "isis_default_circuit_type"),
                        }
                    )

                if get(link, "underlay_multicast") is True:
                    ethernet_interface["pim"] = {"ipv4": {"sparse_mode": True}}

            # L2 interface
            elif get(link, "type") == "underlay_l2":
                ethernet_interface.update(
                    {
                        "type": "switched",
                    }
                )

                if (channel_group_id := get(link, "channel_group_id")) is not None:
                    ethernet_interface["channel_group"] = {
                        "id": int(channel_group_id),
                        "mode": "active",
                    }
                else:
                    vlans = default(get(link, "vlans"), [])
                    ethernet_interface.update(
                        {
                            "vlans": list_compress(vlans),
                            "service_profile": get(self._hostvars, "p2p_uplinks_qos_profile"),
                            "link_tracking_groups": get(link, "link_tracking_groups"),
                        }
                    )

            # Structured Config
            ethernet_interface.update(default(get(link, "structured_config"), {}))

            # Remove None values
            ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

            ethernet_interfaces[get(link, "interface")] = ethernet_interface

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
