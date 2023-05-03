from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .eos_designs_facts import EosDesignsFacts


class UplinksMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def max_parallel_uplinks(self: EosDesignsFacts) -> int:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.max_parallel_uplinks

    @cached_property
    def max_uplink_switches(self: EosDesignsFacts) -> int:
        """
        Exposed in avd_switch_facts
        """
        return self.shared_utils.max_uplink_switches

    @cached_property
    def _uplink_interfaces(self: EosDesignsFacts) -> list:
        return range_expand(
            default(get(self.shared_utils.switch_data_combined, "uplink_interfaces"), get(self.shared_utils.default_interfaces, "uplink_interfaces"), [])
        )

    @cached_property
    def _uplink_switch_interfaces(self: EosDesignsFacts) -> list:
        uplink_switch_interfaces = get(self.shared_utils.switch_data_combined, "uplink_switch_interfaces")
        if uplink_switch_interfaces is not None:
            return uplink_switch_interfaces

        if not self.shared_utils.uplink_switches:
            return []

        if self.shared_utils.id is None:
            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}'")

        uplink_switch_interfaces = []
        uplink_switch_counter = {}
        for uplink_switch in self.shared_utils.uplink_switches:
            uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)

            # Count the number of instances the current switch was processed
            uplink_switch_counter[uplink_switch] = uplink_switch_counter.get(uplink_switch, 0) + 1
            index_of_parallel_uplinks = uplink_switch_counter[uplink_switch] - 1

            # Add uplink_switch_interface based on this switch's ID (-1 for 0-based) * max_parallel_uplinks + index_of_parallel_uplinks.
            # For max_parallel_uplinks: 2 this would assign downlink interfaces like this:
            # spine1 downlink-interface mapping: [ leaf-id1, leaf-id1, leaf-id2, leaf-id2, leaf-id3, leaf-id3, ... ]
            downlink_index = (self.id - 1) * self.shared_utils.max_parallel_uplinks + index_of_parallel_uplinks
            if len(uplink_switch_facts._default_downlink_interfaces) > downlink_index:
                uplink_switch_interfaces.append(uplink_switch_facts._default_downlink_interfaces[downlink_index])
            else:
                raise AristaAvdError(
                    f"'uplink_switch_interfaces' is not set on '{self.shared_utils.hostname}' and 'uplink_switch' '{uplink_switch}' "
                    f"does not have 'downlink_interfaces[{downlink_index}]' set under 'default_interfaces'"
                )

        return uplink_switch_interfaces

    @cached_property
    def uplinks(self: EosDesignsFacts) -> list:
        """
        Exposed in avd_switch_facts

        List of uplinks with all parameters

        These facts are leveraged by templates for this device when rendering uplinks
        and by templates for peer devices when rendering downlinks
        """
        uplinks = []

        if self.shared_utils.uplink_type == "p2p":
            uplink_interfaces = self._uplink_interfaces
            uplink_switches = self.shared_utils.uplink_switches
            uplink_switch_interfaces = self._uplink_switch_interfaces
            for uplink_index, uplink_interface in enumerate(uplink_interfaces):
                if len(uplink_switches) <= uplink_index or len(uplink_switch_interfaces) <= uplink_index:
                    # Invalid length of input variables. Skipping
                    continue

                uplink_switch = uplink_switches[uplink_index]
                if uplink_switch is None or uplink_switch not in self.shared_utils.all_fabric_devices:
                    # Invalid uplink_switch. Skipping.
                    continue

                uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
                uplink = {}
                uplink["interface"] = uplink_interface
                uplink["peer"] = uplink_switch
                uplink["peer_interface"] = uplink_switch_interfaces[uplink_index]
                uplink["peer_type"] = uplink_switch_facts.type
                uplink["peer_is_deployed"] = uplink_switch_facts.is_deployed
                uplink["peer_bgp_as"] = uplink_switch_facts.bgp_as
                uplink["type"] = "underlay_p2p"
                if self.shared_utils.uplink_interface_speed is not None:
                    uplink["speed"] = self.shared_utils.uplink_interface_speed
                if self.shared_utils.uplink_bfd:
                    uplink["bfd"] = True
                if self.shared_utils.uplink_ptp is not None:
                    uplink["ptp"] = self.shared_utils.uplink_ptp
                elif self.shared_utils.ptp_enabled:
                    uplink["ptp"] = {"enable": True}
                if self.shared_utils.uplink_macsec is not None:
                    uplink["mac_security"] = self.shared_utils.uplink_macsec
                if self.shared_utils.underlay_multicast is True and uplink_switch_facts.shared_utils.underlay_multicast is True:
                    uplink["underlay_multicast"] = True
                if self.shared_utils.underlay_rfc5549:
                    uplink["ipv6_enable"] = True
                else:
                    uplink["ip_address"] = self.shared_utils.ip_addressing.p2p_uplinks_ip(uplink_index)
                    uplink["peer_ip_address"] = self.shared_utils.ip_addressing.p2p_uplinks_peer_ip(uplink_index)

                if self.shared_utils.link_tracking_groups is not None:
                    uplink["link_tracking_groups"] = []
                    for lt_group in self.shared_utils.link_tracking_groups:
                        uplink["link_tracking_groups"].append({"name": lt_group["name"], "direction": "upstream"})

                if self.shared_utils.uplink_structured_config is not None:
                    uplink["structured_config"] = self.shared_utils.uplink_structured_config

                uplinks.append(uplink)
            return uplinks

        elif self.shared_utils.uplink_type == "port-channel":
            uplink_interfaces = self._uplink_interfaces
            uplink_switches = self.shared_utils.uplink_switches
            uplink_switch_interfaces = self._uplink_switch_interfaces
            for uplink_index, uplink_interface in enumerate(uplink_interfaces):
                if len(uplink_switches) <= uplink_index or len(uplink_switch_interfaces) <= uplink_index:
                    # Invalid length of input variables. Skipping
                    continue

                uplink_switch = uplink_switches[uplink_index]
                if uplink_switch is None or uplink_switch not in self.shared_utils.all_fabric_devices:
                    # Invalid uplink_switch. Skipping.
                    continue

                uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(uplink_switch, required=True)
                uplink = {}
                uplink["interface"] = uplink_interface
                uplink["peer"] = uplink_switch
                uplink["peer_interface"] = uplink_switch_interfaces[uplink_index]
                uplink["peer_type"] = uplink_switch_facts.type
                uplink["peer_is_deployed"] = uplink_switch_facts.is_deployed
                uplink["type"] = "underlay_l2"

                if self.shared_utils.uplink_interface_speed is not None:
                    uplink["speed"] = self.shared_utils.uplink_interface_speed

                if uplink_switch_facts.shared_utils.mlag is True or self._short_esi is not None:
                    # Override our description on port-channel to be peer's group name if they are mlag pair or A/A #}
                    uplink["channel_description"] = uplink_switch_facts.shared_utils.group

                if self.shared_utils.mlag is True:
                    # Override the peer's description on port-channel to be our group name if we are mlag pair #}
                    uplink["peer_channel_description"] = self.shared_utils.group

                if self.shared_utils.mlag_role == "secondary":
                    mlag_peer_switch_facts: EosDesignsFacts = self.shared_utils.mlag_peer_facts
                    uplink["channel_group_id"] = "".join(re.findall(r"\d", mlag_peer_switch_facts._uplink_interfaces[0]))
                    uplink["peer_channel_group_id"] = "".join(re.findall(r"\d", mlag_peer_switch_facts._uplink_switch_interfaces[0]))
                else:
                    uplink["channel_group_id"] = "".join(re.findall(r"\d", uplink_interfaces[0]))
                    uplink["peer_channel_group_id"] = "".join(re.findall(r"\d", uplink_switch_interfaces[0]))

                # Remove vlans if upstream switch does not have them #}
                if self.shared_utils.enable_trunk_groups:
                    uplink["trunk_groups"] = ["UPLINK"]
                    if self.shared_utils.mlag is True:
                        uplink["peer_trunk_groups"] = [self.shared_utils.group]
                    else:
                        uplink["peer_trunk_groups"] = [self.shared_utils.hostname]

                switch_vlans = self._vlans
                uplink_switch_vlans = uplink_switch_facts._vlans
                uplink_vlans = list(set(switch_vlans).intersection(uplink_switch_vlans))

                if self.shared_utils.inband_management_vlan is not None:
                    uplink_vlans.append(self.shared_utils.inband_management_vlan)

                if uplink_vlans:
                    uplink["vlans"] = list_compress(uplink_vlans)
                else:
                    uplink["vlans"] = "none"

                if uplink_native_vlan := get(self.shared_utils.switch_data_combined, "uplink_native_vlan"):
                    uplink["native_vlan"] = uplink_native_vlan

                if self._short_esi is not None:
                    uplink["peer_short_esi"] = self._short_esi

                if self.shared_utils.link_tracking_groups is not None:
                    uplink["link_tracking_groups"] = []
                    for lt_group in self.shared_utils.link_tracking_groups:
                        uplink["link_tracking_groups"].append({"name": lt_group["name"], "direction": "upstream"})

                if self.shared_utils.uplink_structured_config is not None:
                    uplink["structured_config"] = self.shared_utils.uplink_structured_config

                uplinks.append(uplink)
        return uplinks

    @cached_property
    def uplink_peers(self: EosDesignsFacts) -> list:
        """
        Exposed in avd_switch_facts

        List of all uplink peers

        These are used to generate the "avd_topology_peers" fact covering downlinks for all devices.
        """
        uplink_switches = self.shared_utils.uplink_switches
        return [uplink_switch for uplink_switch in uplink_switches if uplink_switch in self.shared_utils.all_fabric_devices]

    @cached_property
    def _default_downlink_interfaces(self: EosDesignsFacts) -> list:
        """
        internal _default_downlink_interfaces set based on default_interfaces.
        Parsed by downstream switches during eos_designs_facts phase
        """
        return range_expand(get(self.shared_utils.default_interfaces, "downlink_interfaces", default=[]))
