# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import as_path_list_match_from_bgp_asns, default
from pyavd._utils.password_utils.password import simple_7_encrypt
from pyavd._utils.run_once import run_once_method
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.api.pool_manager import PoolManager
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from pyavd._eos_designs.structured_config.structured_config_generator import StructCfgs

    from . import SharedUtilsProtocol


class MiscMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def all_fabric_devices(self: SharedUtilsProtocol) -> list[str]:
        return list(self.peer_facts.keys())

    @cached_property
    def id(self: SharedUtilsProtocol) -> int | None:
        """
        Node ID.

        Will be sourced from different places depending on the context.

        If running under eos_designs_structured_config:
            Use 'id' from EosDesignsFacts or None

        If running under eos_designs_facts and pool manager is activated:
            Use pool manager requesting the value of 'self.node_config.id' if set.
            If the 'id' field is set but not available in the pool, an error will be raised.

        If running under eos_designs_facts and pool manager is _not_ activated:
            Use 'self.node_config.id' which is the ID defined in the node type config or None.
        """
        # Check if we are running from eos_designs_structured_config (facts is an instance of EosDesignsFacts and not EosDesignsFactsGenerator)
        if isinstance(self.switch_facts, EosDesignsFacts):
            # Return id or None
            return self.switch_facts.id

        # We are running from eos_designs_facts.
        # Check if pool manager is activated.
        node_id = self.node_config.id
        if self.inputs.fabric_numbering.node_id.algorithm == "pool_manager":
            if not isinstance(self.pool_manager, PoolManager):
                msg = "'fabric_numbering.id.algorithm' is set to 'pool_manager' but no PoolManager instance is available."
                raise AristaAvdError(msg)

            id_from_pool = self.pool_manager.get_assignment(pool_type="node_id_pools", shared_utils=self, requested_value=node_id)

            if node_id is not None and node_id != id_from_pool:
                pool = self.pool_manager.get_pool(pool_type="node_id_pools", shared_utils=self)
                msg = "When 'fabric_numbering.node_id.algorithm' is set to 'pool_manager', any 'id' set for the node will be reserved in the pool if possible."
                if (assignment := pool.get_assignment_by_value(node_id)) is None:
                    msg += f" The given 'id: {node_id}' is not a valid Node ID for the Pool Manager."
                else:
                    msg += f" The given 'id: {node_id}' is already assigned to '{assignment.key}'."
                msg += (
                    f" The 'id' setting must either be removed or changed. If you prefer to keep the 'id' setting, the next available value is {id_from_pool}."
                )
                raise AristaAvdInvalidInputsError(msg)

            return id_from_pool

        # Pool manager is not activated. Return 'id' from node settings or None.
        return node_id

    @cached_property
    def filter_tags(self: SharedUtilsProtocol) -> list:
        """Return filter.tags + group if defined."""
        filter_tags = list(self.node_config.filter.tags)
        if self.group is not None:
            filter_tags.append(self.group)
        return filter_tags

    @cached_property
    def igmp_snooping_enabled(self: SharedUtilsProtocol) -> bool:
        return default(self.node_config.igmp_snooping_enabled, self.inputs.default_igmp_snooping_enabled)

    @cached_property
    def only_local_vlan_trunk_groups(self: SharedUtilsProtocol) -> bool:
        return self.inputs.enable_trunk_groups and self.inputs.only_local_vlan_trunk_groups

    @cached_property
    def system_mac_address(self: SharedUtilsProtocol) -> str | None:
        """
        system_mac_address.

        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->.
        """
        return default(self.node_config.system_mac_address, self.inputs.system_mac_address)

    @cached_property
    def uplink_switches(self: SharedUtilsProtocol) -> list[str]:
        return self.node_config.uplink_switches._as_list() or self.cv_topology_config.uplink_switches._as_list()

    @cached_property
    def uplink_interfaces(self: SharedUtilsProtocol) -> list[str]:
        if uplink_interface_candidates := range_expand(self.node_config.uplink_interfaces or self.cv_topology_config.uplink_interfaces):
            if len(uplink_interface_candidates) != len(self.uplink_switches):
                msg = (
                    f"Length of 'uplink_interfaces': {len(uplink_interface_candidates)} does not match the length of 'uplink_switches':"
                    f" {len(self.uplink_switches)}"
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)
            return uplink_interface_candidates

        uplink_interface_candidates = range_expand(self.default_interfaces.uplink_interfaces)
        if len(uplink_interface_candidates) < len(self.uplink_switches):
            msg = (
                f"Length of 'default_interfaces.uplink_interfaces': {len(uplink_interface_candidates)} is less than the length of 'uplink_switches': "
                f"{len(self.uplink_switches)}."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        return uplink_interface_candidates[: len(self.uplink_switches)]

    @cached_property
    def uplink_switch_interfaces(self: SharedUtilsProtocol) -> list[str]:
        return list(self.switch_facts.uplink_switch_interfaces)

    @cached_property
    def serial_number(self: SharedUtilsProtocol) -> str | None:
        """
        serial_number.

        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number.
        """
        return default(self.node_config.serial_number, self.inputs.serial_number)

    @cached_property
    def max_uplink_switches(self: SharedUtilsProtocol) -> int:
        """max_uplink_switches will default to the length of uplink_switches."""
        return default(self.node_config.max_uplink_switches, len(self.uplink_switches))

    @cached_property
    def p2p_uplinks_mtu(self: SharedUtilsProtocol) -> int | None:
        p2p_uplinks_mtu = default(self.platform_settings.p2p_uplinks_mtu, self.inputs.p2p_uplinks_mtu)
        return default(self.node_config.uplink_mtu, p2p_uplinks_mtu)

    @cached_property
    def fabric_name(self: SharedUtilsProtocol) -> str:
        if not self.inputs.fabric_name:
            msg = "fabric_name"
            raise AristaAvdMissingVariableError(msg)

        return self.inputs.fabric_name

    @cached_property
    def uplink_interface_speed(self: SharedUtilsProtocol) -> EosCliConfigGen.EthernetInterfacesItem.Speed | None:
        return default(self.node_config.uplink_interface_speed, self.default_interfaces.uplink_interface_speed)

    @cached_property
    def uplink_switch_interface_speed(self: SharedUtilsProtocol) -> EosCliConfigGen.EthernetInterfacesItem.Speed | None:
        # Keeping since we will need it when adding speed support under default interfaces.
        return self.node_config.uplink_switch_interface_speed

    @cached_property
    def default_interface_mtu(self: SharedUtilsProtocol) -> int | None:
        return default(self.platform_settings.default_interface_mtu, self.inputs.default_interface_mtu)

    @cached_property
    def evpn_multicast(self: SharedUtilsProtocol) -> bool:
        return self.switch_facts.evpn_multicast is True

    def get_interface_mtu(self: SharedUtilsProtocol, interface_name: str, configured_mtu: int | None) -> int | None:
        """Returns MTU value for the interface."""
        if not self.platform_settings.feature_support.per_interface_mtu:
            return None
        if "." in interface_name and not self.platform_settings.feature_support.subinterface_mtu:
            return None
        return configured_mtu

    def get_interface_sflow(self: SharedUtilsProtocol, interface: str, configured_sflow: bool | None) -> bool | None:
        """
        Get the configured sFlow state if the interface supports it based on platform settings.

        Considers global sFlow support and specific support for subinterfaces.

        Returns:
            The configured_sflow value if supported, otherwise None.
        """
        sflow_supported_on_interface = self.platform_settings.feature_support.sflow and (
            "." not in interface or self.platform_settings.feature_support.sflow_subinterfaces
        )

        return configured_sflow if sflow_supported_on_interface else None

    def get_ipv4_acl(
        self: SharedUtilsProtocol, name: str, interface_name: str, *, interface_ip: str | None = None, peer_ip: str | None = None
    ) -> EosDesigns.Ipv4AclsItem:
        """
        Get one IPv4 ACL from "ipv4_acls" where fields have been substituted.

        If any substitution is done, the ACL name will get "_<interface_name>" appended.
        """
        if name not in self.inputs.ipv4_acls:
            msg = f"ipv4_acls[name={name}]"
            raise AristaAvdMissingVariableError(msg)
        org_ipv4_acl = self.inputs.ipv4_acls[name]
        # deepcopy to avoid inplace updates below from modifying the original.
        ipv4_acl = org_ipv4_acl._deepcopy()
        ip_replacements = {
            "interface_ip": interface_ip,
            "peer_ip": peer_ip,
        }
        changed = False
        for index, entry in enumerate(ipv4_acl.entries):
            if entry._get("remark"):
                continue

            err_context = f"ipv4_acls[name={name}].entries[{index}]"
            if not entry.source:
                msg = f"{err_context}.source"
                raise AristaAvdMissingVariableError(msg)
            if not entry.destination:
                msg = f"{err_context}.destination"
                raise AristaAvdMissingVariableError(msg)

            entry.source = self._get_ipv4_acl_field_with_substitution(entry.source, ip_replacements, f"{err_context}.source", interface_name)
            entry.destination = self._get_ipv4_acl_field_with_substitution(entry.destination, ip_replacements, f"{err_context}.destination", interface_name)
            if entry.source != org_ipv4_acl.entries[index].source or entry.destination != org_ipv4_acl.entries[index].destination:
                changed = True

        if changed:
            ipv4_acl.name += f"_{self.sanitize_interface_name(interface_name)}"
        return ipv4_acl

    @staticmethod
    def _get_ipv4_acl_field_with_substitution(field_value: str, replacements: dict[str, str | None], field_context: str, interface_name: str) -> str:
        """
        Checks one field if the value can be substituted.

        The given "replacements" dict will be parsed as:
          key: substitution field to look for
          value: replacement value to set.

        If a replacement is done, but the value is None, an error will be raised.
        """
        if field_value not in replacements:
            return field_value

        if (replacement_value := replacements[field_value]) is None:
            msg = (
                f"Unable to perform substitution of the value '{field_value}' defined under '{field_context}', "
                f"since no substitution value was found for interface '{interface_name}'. "
                "Make sure to set the appropriate fields on the interface."
            )
            raise AristaAvdError(msg)

        return replacement_value

    def get_prefix_list(self: SharedUtilsProtocol, name: str) -> EosCliConfigGen.PrefixListsItem:
        """Retrieve prefix list from self.inputs.ipv4_prefix_list_catalog."""
        if name not in self.inputs.ipv4_prefix_list_catalog:
            msg = f"ipv4_prefix_list_catalog[name={name}]"
            raise AristaAvdMissingVariableError(msg)
        return self.inputs.ipv4_prefix_list_catalog[name]._cast_as(EosCliConfigGen.PrefixListsItem)

    def get_l3_bgp_route_map_in(self: SharedUtilsProtocol, name: str, prefix_list_name: str, *, no_advertise: bool = False) -> EosCliConfigGen.RouteMapsItem:
        """
        Generate the inbound route-map for the Router BGP neighbors for node_config.l3_interfaces or node_config.l3_port_channels.

        Args:
            name: the route-map name RM-BGP-<PEER-IP>-IN
            prefix_list_name: the prefix-list name to use for the sequence 10 permit match entry.
            no_advertise: if True, set the community no-advertise on the sequence 10 entry.
        """
        route_map = EosCliConfigGen.RouteMapsItem(name=name)
        sequence_number = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem(
            sequence=10, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"ip address prefix-list {prefix_list_name}"])
        )
        # set no advertise is set only for WAN neighbors, which will also have prefix_list_in
        if no_advertise:
            sequence_number.set.append("community no-advertise additive")

        route_map.sequence_numbers.append(sequence_number)
        return route_map

    def get_l3_bgp_route_map_out(self: SharedUtilsProtocol, name: str, prefix_list_name: str | None = None) -> EosCliConfigGen.RouteMapsItem:
        """
        Generate the outbound route-map for the Router BGP neighbors for node_config.l3_interfaces or node_config.l3_port_channels.

        Args:
            name: the route-map name RM-BGP-<PEER-IP>-OUT
            prefix_list_name: the prefix-list name to use for the sequence 10 permit match entry,
        """
        route_map = EosCliConfigGen.RouteMapsItem(name=name)
        if prefix_list_name:
            route_map.sequence_numbers.append_new(
                sequence=10, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"ip address prefix-list {prefix_list_name}"])
            )
            route_map.sequence_numbers.append_new(sequence=20, type="deny")
        else:
            route_map.sequence_numbers.append_new(
                sequence=10,
                type="deny",
            )
        return route_map

    def update_l3_generic_interface_bgp_objects(
        self: SharedUtilsProtocol,
        interface: (
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
            | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
        ),
        neighbors: EosCliConfigGen.RouterBgp.Neighbors,
        prefix_lists: EosCliConfigGen.PrefixLists,
        route_maps: EosCliConfigGen.RouteMaps,
    ) -> None:
        if isinstance(interface, EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem):
            schema_key = "l3_interfaces"
            description_function = self.interface_descriptions.underlay_ethernet_interface
            peer_interface = interface.peer_interface
        else:
            schema_key = "l3_port_channels"
            description_function = self.interface_descriptions.underlay_port_channel_interface
            peer_interface = interface.peer_port_channel

        context = f"{schema_key}[{interface.name}]"

        if not (interface.peer_ip and interface.bgp):
            return

        is_wan_interface = bool(interface.wan_carrier)

        if is_wan_interface and not interface.bgp.ipv4_prefix_list_in:
            # TODO: Use source here when available.
            msg = f"BGP is enabled but 'bgp.ipv4_prefix_list_in' is not configured for '{context}'."
            raise AristaAvdInvalidInputsError(msg)

        description = (
            interface.description
            or description_function(
                InterfaceDescriptionData(
                    shared_utils=self,
                    interface=interface.name,
                    peer=interface.peer,
                    peer_interface=peer_interface,
                    wan_carrier=interface.wan_carrier,
                    wan_circuit_id=interface.wan_circuit_id,
                ),
            )
            or None
        )

        neighbor = EosCliConfigGen.RouterBgp.NeighborsItem(
            ip_address=interface.peer_ip,
            remote_as=interface.bgp.peer_as,
            description=description,
        )

        if interface.bgp.ipv4_prefix_list_in:
            if interface.bgp.ipv4_prefix_list_in not in prefix_lists:
                prefix_lists.append(self.get_prefix_list(interface.bgp.ipv4_prefix_list_in))
            rm_in_name = f"RM-BGP-{neighbor.ip_address}-IN"
            neighbor.route_map_in = rm_in_name
            route_maps.append(self.get_l3_bgp_route_map_in(rm_in_name, interface.bgp.ipv4_prefix_list_in, no_advertise=is_wan_interface))

        if interface.bgp.ipv4_prefix_list_out and interface.bgp.ipv4_prefix_list_out not in prefix_lists:
            prefix_lists.append(self.get_prefix_list(interface.bgp.ipv4_prefix_list_out))

        rm_out_name = f"RM-BGP-{neighbor.ip_address}-OUT"
        neighbor.route_map_out = rm_out_name
        route_maps.append(self.get_l3_bgp_route_map_out(rm_out_name, interface.bgp.ipv4_prefix_list_out))

        neighbors.append(neighbor)

    @cached_property
    def l3_bgp_objects(self: SharedUtilsProtocol) -> tuple[EosCliConfigGen.RouterBgp.Neighbors, EosCliConfigGen.PrefixLists, EosCliConfigGen.RouteMaps]:
        """Generates the EosCliConfigGen Router BGP Neighbors and their associated PrefixListsItem and RouteMapsItem."""
        neighbors = EosCliConfigGen.RouterBgp.Neighbors()
        prefix_lists = EosCliConfigGen.PrefixLists()
        route_maps = EosCliConfigGen.RouteMaps()

        for interface in self.l3_interfaces:
            self.update_l3_generic_interface_bgp_objects(interface, neighbors, prefix_lists, route_maps)
        for interface in self.node_config.l3_port_channels:
            self.update_l3_generic_interface_bgp_objects(interface, neighbors, prefix_lists, route_maps)

        return neighbors, prefix_lists, route_maps

    @property
    def l3_bgp_neighbors(self: SharedUtilsProtocol) -> EosCliConfigGen.RouterBgp.Neighbors:
        return self.l3_bgp_objects[0]

    @property
    def l3_bgp_prefix_lists(self: SharedUtilsProtocol) -> EosCliConfigGen.PrefixLists:
        return self.l3_bgp_objects[1]

    @property
    def l3_bgp_route_maps(self: SharedUtilsProtocol) -> EosCliConfigGen.RouteMaps:
        return self.l3_bgp_objects[2]

    @cached_property
    def is_sfe_interface_profile_supported(self: SharedUtilsProtocol) -> bool:
        """Returns bool indicating whether platform SFE interface profile is supported."""
        return self.platform_settings.feature_support.platform_sfe_interface_profile.supported

    @cached_property
    def max_rx_queues(self: SharedUtilsProtocol) -> int:
        """
        Returns maximum value allowed for rx_queue count configured under L3 interface or L3 Port-Channel interface.

        This is used for building SFE interface profile.
        """
        if not self.is_sfe_interface_profile_supported:
            return 0
        return self.platform_settings.feature_support.platform_sfe_interface_profile.max_rx_queues

    @cached_property
    def all_connected_endpoints(
        self: SharedUtilsProtocol,
    ) -> EosDesigns._DynamicKeys.DynamicConnectedEndpoints:
        """Emit the complete list of connected_endpoints and custom_connected_endpoints, prioritizing custom_connected_endpoints."""
        all_connected_endpoints = EosDesigns._DynamicKeys.DynamicConnectedEndpoints()
        if self.inputs.connected_endpoints:
            dyn_connected_endpoints_item = EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem(
                key="connected_endpoints",
                value=self.inputs.connected_endpoints._cast_as(EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpoints),
            )
            dyn_connected_endpoints_item._internal_data.description = None
            dyn_connected_endpoints_item._internal_data.type = None
            all_connected_endpoints.append(dyn_connected_endpoints_item)

        for dyn_connected_endpoints in self.inputs._dynamic_keys.custom_connected_endpoints:
            dyn_connected_endpoints_item = dyn_connected_endpoints._cast_as(EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem)
            dyn_connected_endpoints_item._internal_data.description = self.inputs.custom_connected_endpoints_keys[dyn_connected_endpoints.key].description
            dyn_connected_endpoints_item._internal_data.type = self.inputs.custom_connected_endpoints_keys[dyn_connected_endpoints.key].type
            all_connected_endpoints.append(dyn_connected_endpoints_item)

        for dyn_connected_endpoints in self.inputs._dynamic_keys.connected_endpoints:
            if dyn_connected_endpoints.key not in all_connected_endpoints:
                dyn_connected_endpoints._internal_data.description = self.inputs.connected_endpoints_keys[dyn_connected_endpoints.key].description
                dyn_connected_endpoints._internal_data.type = self.inputs.connected_endpoints_keys[dyn_connected_endpoints.key].type
                all_connected_endpoints.append(dyn_connected_endpoints)

        return all_connected_endpoints

    def get_ipsec_key(self: SharedUtilsProtocol, cleartext_key: str, profile_name: str) -> str:
        """
        Return a type 7 encrypted shared key for IPsec.

        Args:
            cleartext_key: The cleartext key to encrypt
            profile_name: The profile name to derive a salt deterministically

        Returns:
            str: type 7 encrypted key.
        """
        # Need to compute it deterministically
        salt = sum(bytearray(profile_name, "ascii")) % 16

        return simple_7_encrypt(cleartext_key, salt)

    @cached_property
    def is_campus_device(self: SharedUtilsProtocol) -> bool:
        """Return True if generation of the Campus tags is globally enabled and current device is a Campus device."""
        return bool(self.inputs.generate_cv_tags.campus_fabric and default(self.node_config.campus, self.inputs.campus))

    @run_once_method
    def set_once_ip_extcommunity_list_evpn_soo(self: SharedUtilsProtocol, structured_config: EosCliConfigGen) -> None:
        """Set ip extcommunity-list ECL-EVPN-SOO."""
        ip_extcommunity_list = EosCliConfigGen.IpExtcommunityListsItem(name="ECL-EVPN-SOO")
        ip_extcommunity_list.entries.append_new(type="permit", extcommunities=f"soo {self.evpn_soo}")
        structured_config.ip_extcommunity_lists.append(ip_extcommunity_list)

    @run_once_method
    def set_once_peer_group_ipv4_underlay_peers(self: SharedUtilsProtocol, structured_config: EosCliConfigGen, custom_structured_configs: StructCfgs) -> None:
        """
        Add IPv4 underlay peer group to structured_config.

        Also adds required route-maps and prefix-lists.
        """
        af_type = "ipv4" if not self.underlay_ipv6_numbered else "ipv6"

        peer_group = EosCliConfigGen.RouterBgp.PeerGroupsItem(
            name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
            password=self.get_bgp_password(self.inputs.bgp_peer_groups.ipv4_underlay_peers),
            bfd=self.inputs.bgp_peer_groups.ipv4_underlay_peers.bfd or None,
            maximum_routes=self.inputs.bgp_peer_groups.ipv4_underlay_peers.maximum_routes,
            send_community="all",
        )
        peer_group.metadata.type = af_type
        if self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config:
            custom_structured_configs.nested.router_bgp.peer_groups.obtain(self.inputs.bgp_peer_groups.ipv4_underlay_peers.name)._deepmerge(
                self.inputs.bgp_peer_groups.ipv4_underlay_peers.structured_config, list_merge=custom_structured_configs.list_merge_strategy
            )

        if self.is_cv_pathfinder_router:
            peer_group.route_map_in = "RM-BGP-UNDERLAY-PEERS-IN"
            self.set_once_route_map_bgp_underlay_peers_in(structured_config)
            if self.wan_ha:
                peer_group.route_map_out = "RM-BGP-UNDERLAY-PEERS-OUT"
                self.set_once_route_map_bgp_underlay_peers_out(structured_config)
                if self.use_uplinks_for_wan_ha:
                    # For HA need to add allowas_in 1
                    peer_group.allowas_in._update(enabled=True, times=1)

        structured_config.router_bgp.peer_groups.append(peer_group)

        # Address Families
        # TODO: - see if it makes sense to extract logic in method
        if not self.underlay_ipv6_numbered:
            address_family_ipv4_peer_group = EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem(
                name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True
            )
            if self.inputs.underlay_rfc5549 is True:
                address_family_ipv4_peer_group.next_hop.address_family_ipv6._update(enabled=True, originate=True)

            structured_config.router_bgp.address_family_ipv4.peer_groups.append(address_family_ipv4_peer_group)

        if self.underlay_ipv6:
            structured_config.router_bgp.address_family_ipv6.peer_groups.append_new(name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name, activate=True)

    @run_once_method
    def set_once_route_map_bgp_underlay_peers_in(self: SharedUtilsProtocol, structured_config: EosCliConfigGen) -> None:
        """Set route-map RM-BGP-UNDERLAY-PEERS-IN."""
        # RM-BGP-UNDERLAY-PEERS-IN
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(
            sequence=40,
            type="permit",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.evpn_soo} additive"]),
            description="Mark prefixes originated from the LAN",
        )
        if self.wan_ha and self.use_uplinks_for_wan_ha:
            sequence_numbers.append_new(
                sequence=10,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-WAN-HA-PEER-PREFIXES"]),
                description="Allow WAN HA peer interface prefixes",
            )
            # Create the prefix-list.
            self.set_once_prefix_list_wan_ha_peer_prefixes(structured_config)

            sequence_numbers.append_new(
                sequence=20,
                type="deny",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["as-path ASPATH-WAN"]),
                description="Deny other routes from the HA peer",
            )
            # Create AS Path ACL
            self.set_once_as_path_acl_aspath_wan(structured_config)

        structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-IN", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_route_map_bgp_underlay_peers_out(self: SharedUtilsProtocol, structured_config: EosCliConfigGen) -> None:
        """Set route-map RM-BGP-UNDERLAY-PEERS-OUT."""
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(
            sequence=10,
            type="permit",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["tag 50", "route-type internal"]),
            description="Make routes learned from WAN HA peer less preferred on LAN routers",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["metric 50"]),
        )
        sequence_numbers.append_new(sequence=20, type="permit")

        structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-OUT", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_prefix_list_wan_ha_peer_prefixes(self: SharedUtilsProtocol, structured_config: EosCliConfigGen) -> None:
        """Set prefix-list PL-WAN-HA-PEER-PREFIXES."""
        sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
        for index, ip_address in enumerate(self.wan_ha_peer_ip_addresses, start=1):
            sequence_numbers.append_new(sequence=10 * index, action=f"permit {ipaddress.ip_network(ip_address, strict=False)}")
        structured_config.prefix_lists.append_new(name="PL-WAN-HA-PEER-PREFIXES", sequence_numbers=sequence_numbers)

    @run_once_method
    def set_once_as_path_acl_aspath_wan(self: SharedUtilsProtocol, structured_config: EosCliConfigGen) -> None:
        """Set as-path access-list ASPATH-WAN."""
        entries = EosCliConfigGen.AsPath.AccessListsItem.Entries()
        entries.append_new(type="permit", match=as_path_list_match_from_bgp_asns((self.bgp_as,)))  # pyright: ignore[reportArgumentType]
        structured_config.as_path.access_lists.append_new(name="ASPATH-WAN", entries=entries)
