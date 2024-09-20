# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, short_esi_to_route_target, strip_null_from_data
from pyavd.api.interface_descriptions import InterfaceDescriptionData

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def port_channel_interfaces(self: AvdStructuredConfigUnderlay) -> list | None:
        """Return structured config for port_channel_interfaces."""
        port_channel_interfaces = []
        port_channel_list = []
        for link in self._underlay_links:
            if link["type"] != "underlay_l2" or link.get("channel_group_id") is None:
                continue

            if (channel_group_id := link.get("channel_group_id")) in port_channel_list:
                continue

            port_channel_list.append(channel_group_id)

            port_channel_name = f"Port-Channel{link['channel_group_id']}"

            port_channel_interface = {
                "name": port_channel_name,
                "description": self.shared_utils.interface_descriptions.underlay_port_channel_interface(
                    InterfaceDescriptionData(
                        shared_utils=self.shared_utils,
                        interface=port_channel_name,
                        peer=link["peer"],
                        peer_channel_group_id=link["peer_channel_group_id"],
                        port_channel_id=link["channel_group_id"],
                        port_channel_description=link.get("channel_description"),
                    ),
                ),
                "switchport": {
                    "enabled": True,
                    "mode": "trunk",
                    "trunk": {
                        "native_vlan": link.get("native_vlan"),
                    },
                },
                "shutdown": False,
                "service_profile": self.shared_utils.p2p_uplinks_qos_profile,
                "link_tracking_groups": link.get("link_tracking_groups"),
                "sflow": link.get("sflow"),
                "flow_tracker": link.get("flow_tracker"),
                "spanning_tree_portfast": link.get("spanning_tree_portfast"),
            }

            if (trunk_groups := link.get("trunk_groups")) is not None:
                port_channel_interface["switchport"]["trunk"]["groups"] = trunk_groups
            elif (vlans := link.get("vlans")) is not None:
                port_channel_interface["switchport"]["trunk"]["allowed_vlan"] = vlans

            # Configure MLAG on MLAG switches if either 'mlag_on_orphan_port_channel_downlink' or 'link.mlag' is True
            if self.shared_utils.mlag is True and any([get(self._hostvars, "mlag_on_orphan_port_channel_downlink", default=False), link.get("mlag", True)]):
                port_channel_interface["mlag"] = int(link.get("channel_group_id"))

            if (short_esi := link.get("short_esi")) is not None:
                port_channel_interface["evpn_ethernet_segment"] = {
                    "identifier": f"{self.shared_utils.evpn_short_esi_prefix}{short_esi}",
                    "route_target": short_esi_to_route_target(short_esi),
                }
                port_channel_interface["lacp_id"] = short_esi.replace(":", ".")

            # PTP
            if get(link, "ptp.enable") is True:
                ptp_config = {}

                # Apply PTP profile config if using the new ptp config style
                if self.shared_utils.ptp_enabled:
                    ptp_config.update(self.shared_utils.ptp_profile)

                ptp_config["enable"] = True
                ptp_config.pop("profile", None)

                port_channel_interface["ptp"] = ptp_config

            # Inband ZTP Port-Channel LACP Fallback
            if get(link, "inband_ztp_vlan"):
                port_channel_interface["lacp_fallback_mode"] = "individual"
                port_channel_interface["lacp_fallback_timeout"] = get(link, "inband_ztp_lacp_fallback_delay")

            # Structured Config
            port_channel_interface["struct_cfg"] = link.get("structured_config")

            # Remove None values
            port_channel_interface = strip_null_from_data(port_channel_interface, strip_values_tuple=(None, "", {}))

            port_channel_interfaces.append(port_channel_interface)

        if port_channel_interfaces:
            return port_channel_interfaces

        return None
