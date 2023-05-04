from __future__ import annotations

from functools import cached_property

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
        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                # Ethernet interface
                ethernet_interface = self._get_common_interface_cfg(p2p_link)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                interface_name = p2p_link["data"]["interface"]
                ethernet_interfaces[interface_name] = ethernet_interface
                continue

            # Port-Channel members
            for member in p2p_link["data"]["port_channel_members"]:
                ethernet_interface = self._get_port_channel_member_cfg(p2p_link)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                interface_name = member["interface"]
                ethernet_interfaces[interface_name] = ethernet_interface

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
