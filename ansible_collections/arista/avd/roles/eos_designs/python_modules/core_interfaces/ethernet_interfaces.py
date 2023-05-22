from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_item

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

        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                # Ethernet interface
                ethernet_interface = self._get_common_interface_cfg(p2p_link)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                if (found_eth_interface := get_item(ethernet_interfaces, "name", ethernet_interface["name"])) is None:
                    ethernet_interfaces.append(ethernet_interface)
                else:
                    if found_eth_interface == ethernet_interface:
                        # Same ethernet_interface information twice in the input data. So not duplicate interface name.
                        continue

                    raise AristaAvdError(
                        f"Duplicate interface name {ethernet_interface['name']} found while generating ethernet_interface for core_interfaces peer:"
                        f" {ethernet_interface['peer']}, peer_interface: {ethernet_interface['peer_interface']}. Description on duplicate interface:"
                        f" {found_eth_interface['description']}"
                    )

            # Port-Channel members
            for member in p2p_link["data"]["port_channel_members"]:
                ethernet_interface = self._get_port_channel_member_cfg(p2p_link, member["interface"])
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                if (found_eth_interface := get_item(ethernet_interfaces, "name", ethernet_interface["name"])) is None:
                    ethernet_interfaces.append(ethernet_interface)
                else:
                    if found_eth_interface == ethernet_interface:
                        # Same ethernet_interface information twice in the input data. So not duplicate interface name.
                        continue

                    raise AristaAvdError(
                        f"Duplicate interface name {ethernet_interface['name']} found while generating ethernet_interfaces for core_interfaces with"
                        f" port-channel members, peer: {ethernet_interface['peer']}, peer_interface: {ethernet_interface['peer_interface']}. Description on"
                        f" duplicate interface: {found_eth_interface['description']}"
                    )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
