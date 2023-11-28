# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, default, get, get_item

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

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=ethernet_interface,
                    context=f"Ethernet Interfaces defined under {self.data_model} p2p_link",
                    context_keys=["name", "peer", "peer_interface"],
                )

                if (subinterfaces := p2p_link.get("subinterfaces")) is not None:
                    for subinterface_data in subinterfaces:
                        subinterface = self._render_subinterface(subinterface_data, ethernet_interface)
                        append_if_not_duplicate(
                            list_of_dicts=ethernet_interfaces,
                            primary_key="name",
                            new_dict=subinterface,
                            context=f"Ethernet Interfaces defined under {self.data_model} p2p_link",
                            context_keys=["name", "peer", "peer_interface"],
                        )

            # Port-Channel members
            for member in p2p_link["data"]["port_channel_members"]:
                ethernet_interface = self._get_port_channel_member_cfg(p2p_link, member)
                ethernet_interface.update(self._get_ethernet_cfg(p2p_link))

                # Remove None values
                ethernet_interface = {key: value for key, value in ethernet_interface.items() if value is not None}

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=ethernet_interface,
                    context=f"Ethernet Interfaces defined under {self.data_model} p2p_link port-Channel members",
                    context_keys=["name", "peer", "peer_interface"],
                )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None

    def _valid_vrfs(self) -> list[dict]:
        """
        Return all the valid VRF on this device based on network_services configuration
        """
        # TODO check as we could end up with duplicates here
        return [vrf for tenant in self.shared_utils.filtered_tenants for vrf in tenant.get("vrfs", [])]

    def _get_vrf_id(self) -> list:
        """ """
        # need to find the vrf

    def _render_subinterface(self, subif_data: dict, ethernet_interface: dict) -> dict:
        """
        Return a dictionary to render the subinterface under the main ethernet_interface passed as input
        """
        # Maybe use required instead
        if not (vrf := get_item(self._valid_vrfs(), "name", subif_data.get("vrf"))):
            # TODO makes this message better
            raise AristaAvdError("Trying to configure a non present VRF for subinterface")

        if not (subif_id := default(get(subif_data, "subinterface_id"), vrf.get("vrf_id"), vrf.get("vrf_vni"))):
            raise AristaAvdError("TODO fix me subif_id MUST be defined")

        # TODO add ip address
        # TODO - is the VLAN already created??
        # TODO - what if the subif_id > 4096 ?
        # TODO - clash possibility?
        subif = {
            "name": f"{ethernet_interface['name']}.{subif_id}",
            "description": get(subif_data, "description", ethernet_interface.get("description")),
            "type": "l3dot1q",
            "vrf": vrf.get("name"),
            "shutdown": False,
            "encapsulation_dot1q_vlan": subif_id,
            "struct_cfg": get(subif_data, "structured_config"),
        }
        return {key: value for key, value in subif.items() if value is not None}
