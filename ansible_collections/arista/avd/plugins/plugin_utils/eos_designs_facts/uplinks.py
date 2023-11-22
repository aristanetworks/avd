# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, unique

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
            default(
                get(self.shared_utils.switch_data_combined, "uplink_interfaces"),
                get(self.shared_utils.cv_topology_config, "uplink_interfaces"),
                get(self.shared_utils.default_interfaces, "uplink_interfaces"),
                [],
            )
        )

    @cached_property
    def _uplink_port_channel_id(self: EosDesignsFacts) -> int:
        """
        For MLAG secondary get the uplink_port_channel_id from the peer's facts.
        We don't need to validate it (1-2000), since it will be validated on the peer.

        For MLAG primary or none MLAG, take the value of 'uplink_port_channel_id' if set,
        or use the numbers from the first interface in 'uplink_interfaces'.

        For MLAG primary validate that the port-channel id falls within 1-2000 since we also use this ID as MLAG ID.
        """
        uplink_port_channel_id = get(self.shared_utils.switch_data_combined, "uplink_port_channel_id")

        if self.shared_utils.mlag_role == "secondary":
            # MLAG Secondary
            peer_uplink_port_channel_id = self.shared_utils.mlag_peer_facts._uplink_port_channel_id
            # check that port-channel IDs are the same as on primary
            if uplink_port_channel_id is not None:
                if uplink_port_channel_id != peer_uplink_port_channel_id:
                    raise AristaAvdError(
                        f"'uplink_port_channel_id' on '{self.shared_utils.hostname}' is set to {uplink_port_channel_id} and is not matching"
                        f" {peer_uplink_port_channel_id} set on MLAG peer."
                        " The 'uplink_port_channel_id' must be matching on MLAG peers."
                    )
            return peer_uplink_port_channel_id

        # MLAG Primary or not MLAG.
        if uplink_port_channel_id is None:
            # Overwriting uplink_port_channel_id
            uplink_port_channel_id = int("".join(re.findall(r"\d", self._uplink_interfaces[0])))

        # produce an error if the switch is MLAG and port-channel ID is above 2000
        if self.shared_utils.mlag:
            if not (1 <= uplink_port_channel_id <= 2000):
                raise AristaAvdError(
                    f"'uplink_port_channel_id' must be between 1 and 2000 for MLAG switches. Got '{uplink_port_channel_id}' on '{self.shared_utils.hostname}'."
                )

        return uplink_port_channel_id

    @cached_property
    def _uplink_switch_port_channel_id(self: EosDesignsFacts) -> int:
        """
        For MLAG secondary get the uplink_switch_port_channel_id from the peer's facts.
        We don't need to validate it (1-2000), since it will be validated on the peer.

        For MLAG primary or none MLAG, take the value of 'uplink_switch_port_channel_id' if set,
        or use the numbers from the first interface in 'uplink_switch_interfaces'.

        If the *uplink_switch* is in MLAG,  validate that the port-channel id falls within 1-2000
        since we also use this ID as MLAG ID on the *uplink switch*.
        """
        uplink_switch_port_channel_id = get(self.shared_utils.switch_data_combined, "uplink_switch_port_channel_id")

        if self.shared_utils.mlag_role == "secondary":
            # MLAG Secondary
            peer_uplink_switch_port_channel_id = self.shared_utils.mlag_peer_facts._uplink_switch_port_channel_id
            # check that port-channel IDs are the same as on primary
            if uplink_switch_port_channel_id is not None:
                if uplink_switch_port_channel_id != peer_uplink_switch_port_channel_id:
                    raise AristaAvdError(
                        f"'uplink_switch_port_channel_id'expected_error_message on '{self.shared_utils.hostname}' is set to {uplink_switch_port_channel_id} and"
                        f" is not matching {peer_uplink_switch_port_channel_id} set on MLAG peer. The 'uplink_switch_port_channel_id' must be matching on MLAG"
                        " peers."
                    )
            return peer_uplink_switch_port_channel_id

        # MLAG Primary or not MLAG.
        if uplink_switch_port_channel_id is None:
            # Overwriting uplink_switch_port_channel_id
            uplink_switch_port_channel_id = int("".join(re.findall(r"\d", self._uplink_switch_interfaces[0])))

        # produce an error if the uplink switch is MLAG and port-channel ID is above 2000
        uplink_switch_facts: EosDesignsFacts = self.shared_utils.get_peer_facts(self.shared_utils.uplink_switches[0], required=True)

        if uplink_switch_facts.shared_utils.mlag:
            if not (1 <= uplink_switch_port_channel_id <= 2000):
                raise AristaAvdError(
                    f"'uplink_switch_port_channel_id' must be between 1 and 2000 for MLAG switches. Got '{uplink_switch_port_channel_id}' on"
                    f" '{self.shared_utils.hostname}'."
                )

        return uplink_switch_port_channel_id

    @cached_property
    def _uplink_switch_interfaces(self: EosDesignsFacts) -> list:
        uplink_switch_interfaces = default(
            get(self.shared_utils.switch_data_combined, "uplink_switch_interfaces"),
            get(self.shared_utils.cv_topology_config, "uplink_switch_interfaces"),
        )
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

                if self.shared_utils.uplink_switch_interface_speed is not None:
                    uplink["peer_speed"] = self.shared_utils.uplink_switch_interface_speed

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

                if self.shared_utils.uplink_switch_interface_speed is not None:
                    uplink["peer_speed"] = self.shared_utils.uplink_switch_interface_speed

                if self.shared_utils.uplink_ptp is not None:
                    uplink["ptp"] = self.shared_utils.uplink_ptp
                elif self.shared_utils.ptp_enabled:
                    uplink["ptp"] = {"enable": True}

                if uplink_switch_facts.shared_utils.mlag is True or self._short_esi is not None:
                    # Override our description on port-channel to be peer's group name if they are mlag pair or A/A #}
                    uplink["channel_description"] = uplink_switch_facts.shared_utils.group

                if self.shared_utils.mlag is True:
                    # Override the peer's description on port-channel to be our group name if we are mlag pair #}
                    uplink["peer_channel_description"] = self.shared_utils.group

                uplink["channel_group_id"] = str(self._uplink_port_channel_id)
                uplink["peer_channel_group_id"] = str(self._uplink_switch_port_channel_id)

                # Remove vlans if upstream switch does not have them #}
                if self.shared_utils.enable_trunk_groups:
                    uplink["trunk_groups"] = ["UPLINK"]
                    if self.shared_utils.mlag is True:
                        uplink["peer_trunk_groups"] = [self.shared_utils.group]
                    else:
                        uplink["peer_trunk_groups"] = [self.shared_utils.hostname]

                uplink_vlans = set(self._vlans)
                uplink_vlans = uplink_vlans.intersection(uplink_switch_facts._vlans)

                if self.shared_utils.configure_inband_mgmt:
                    # Always add inband_mgmt_vlan even if the uplink switch does not have this vlan defined
                    uplink_vlans.add(self.shared_utils.inband_mgmt_vlan)

                if uplink_vlans:
                    uplink["vlans"] = list_compress(list(uplink_vlans))
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

        List of all **unique** uplink peers

        These are used to generate the "avd_topology_peers" fact covering downlinks for all devices.
        """
        uplink_switches = self.shared_utils.uplink_switches
        # Making sure each peer is unique
        return natural_sort(unique(uplink_switch for uplink_switch in uplink_switches if uplink_switch in self.shared_utils.all_fabric_devices))

    @cached_property
    def _default_downlink_interfaces(self: EosDesignsFacts) -> list:
        """
        internal _default_downlink_interfaces set based on default_interfaces.
        Parsed by downstream switches during eos_designs_facts phase
        """
        return range_expand(get(self.shared_utils.default_interfaces, "downlink_interfaces", default=[]))
