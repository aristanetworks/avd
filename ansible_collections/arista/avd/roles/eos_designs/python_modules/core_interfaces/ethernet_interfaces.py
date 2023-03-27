from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ethernet_interfaces(self) -> list | None:
        """
        Return structured config for ethernet_interfaces
        """
        ethernet_interfaces = []
        interface_names = []

        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                # Ethernet interface
                ethernet_interface = self._get_common_interface_cfg(p2p_link)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}
                if p2p_link["data"]["interface"] in interface_names:
                    for idx, eth_int in enumerate(ethernet_interfaces):
                        if eth_int["name"] == p2p_link["data"]["interface"]:
                            ethernet_interfaces[idx] = ethernet_interface
                else:
                    ethernet_interfaces.append(ethernet_interface)
                    interface_names.append(p2p_link["data"]["interface"])
                continue

            # Port-Channel members
            for member in p2p_link["data"]["port_channel_members"]:
                ethernet_interface = self._get_port_channel_member_cfg(p2p_link, member)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                if member["interface"] in interface_names:
                    for idx, eth_int in enumerate(ethernet_interfaces):
                        if eth_int["name"] == member["interface"]:
                            ethernet_interfaces[idx] = ethernet_interface
                else:
                    ethernet_interfaces.append(ethernet_interface)
                    interface_names.append(member["interface"])

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
