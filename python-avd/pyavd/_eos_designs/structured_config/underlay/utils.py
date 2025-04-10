# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol, overload

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFacts
from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError
from pyavd._utils import Undefined, default, get_ip_from_ip_prefix
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class UtilsMixin(Protocol):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _avd_peers(self: AvdStructuredConfigUnderlayProtocol) -> list[str]:
        """
        Returns a list of peers.

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return natural_sort(self.facts.downlink_switches)

    @cached_property
    def _underlay_links(self: AvdStructuredConfigUnderlayProtocol) -> EosDesignsFacts.Uplinks:
        """Returns the list of underlay links for this device."""
        underlay_links = self.facts.uplinks._deepcopy()

        for uplink in underlay_links:
            uplink.sflow_enabled = self.inputs.fabric_sflow.uplinks
            uplink.flow_tracking = self.inputs.fabric_flow_tracking.uplinks

        downlinks_flow_tracking = (
            # Cast as uplink model since that is used in the facts' uplink which we reuse below model
            self.inputs.fabric_flow_tracking.downlinks._cast_as(EosDesigns.FabricFlowTracking.Uplinks)
        )

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer)
            for uplink in peer_facts.uplinks:
                if uplink.peer != self.shared_utils.hostname:
                    continue

                downlink = EosDesignsFacts.UplinksItem(
                    interface=uplink.peer_interface,
                    peer=peer,
                    peer_interface=uplink.interface,
                    peer_type=peer_facts.type,
                    peer_is_deployed=peer_facts.is_deployed,
                    peer_bgp_as=peer_facts.bgp_as,
                    type=uplink.type,
                    speed=uplink.peer_speed or uplink.speed,
                    ip_address=uplink.peer_ip_address,
                    peer_ip_address=uplink.ip_address,
                    prefix_length=uplink.prefix_length,
                    channel_group_id=uplink.peer_channel_group_id,
                    peer_channel_group_id=uplink.channel_group_id,
                    peer_node_group=uplink.node_group,
                    vlans=uplink.vlans,
                    native_vlan=uplink.native_vlan,
                    trunk_groups=uplink.peer_trunk_groups._cast_as(EosDesignsFacts.UplinksItem.TrunkGroups),
                    bfd=uplink.bfd,
                    ptp=uplink.ptp,
                    mac_security=uplink.mac_security,
                    short_esi=uplink.peer_short_esi,
                    mlag=uplink.peer_mlag,
                    underlay_multicast=uplink.underlay_multicast,
                    ipv6_enable=uplink.ipv6_enable,
                    sflow_enabled=self.inputs.fabric_sflow.downlinks,
                    flow_tracking=downlinks_flow_tracking,
                    spanning_tree_portfast=uplink.peer_spanning_tree_portfast,
                    structured_config=uplink.structured_config,
                )
                if peer_facts.inband_ztp:
                    # l2 inband ztp
                    downlink.inband_ztp_vlan = peer_facts.inband_ztp_vlan
                    downlink.inband_ztp_lacp_fallback_delay = peer_facts.inband_ztp_lacp_fallback_delay
                    # l3 inband ztp
                    downlink.dhcp_server = True

                if uplink.subinterfaces:
                    for subinterface in uplink.subinterfaces:
                        downlink_subinterface = subinterface._deepcopy()
                        # Swap own and peer interface and ip.
                        downlink_subinterface._update(
                            interface=subinterface.peer_interface,
                            peer_interface=subinterface.interface,
                            ip_address=subinterface.peer_ip_address,
                            peer_ip_address=subinterface.ip_address,
                        )
                        downlink.subinterfaces.append(downlink_subinterface)
                underlay_links.append(downlink)

        return underlay_links._natural_sorted()

    # These overloads are just here to help the type checker enforce that input type x gives output type y
    @overload
    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem: ...

    @overload
    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem,
    ) -> EosCliConfigGen.PortChannelInterfacesItem: ...

    def _get_l3_common_interface_cfg(
        self: AvdStructuredConfigUnderlayProtocol,
        l3_generic_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
        | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem | EosCliConfigGen.PortChannelInterfacesItem:
        """Returns common structured_configuration for L3 interface or L3 Port-Channel."""
        # variables being set for constructing appropriate validation error
        if isinstance(l3_generic_interface, EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem):
            interface = EosCliConfigGen.EthernetInterfacesItem()
            schema_key = "l3_interfaces"
        else:
            # implies interface is "L3 Port-Channel"
            interface = EosCliConfigGen.PortChannelInterfacesItem()
            schema_key = "l3_port_channels"

        # logic below is common to l3_interface and l3_port_channel interface types

        # TODO: catch if ip_address is not valid or not dhcp
        if not l3_generic_interface.ip_address:
            msg = f"{self.shared_utils.node_type_key_data.key}.nodes[name={self.shared_utils.hostname}].{schema_key}"
            msg += f"[name={l3_generic_interface.name}].ip_address"
            raise AristaAvdMissingVariableError(msg)

        is_subinterface = "." in l3_generic_interface.name
        interface._update(
            name=l3_generic_interface.name,
            peer=l3_generic_interface.peer,
            ip_address=l3_generic_interface.ip_address,
            shutdown=not l3_generic_interface.enabled,
            service_profile=l3_generic_interface.qos_profile,
            eos_cli=l3_generic_interface.raw_eos_cli,
            flow_tracker=self.shared_utils.get_flow_tracker(l3_generic_interface.flow_tracking, interface.FlowTracker),
        )
        interface.switchport.enabled = False if "." not in l3_generic_interface.name else None

        if is_subinterface:
            interface.encapsulation_dot1q.vlan = default(
                l3_generic_interface.encapsulation_dot1q_vlan, int(l3_generic_interface.name.split(".", maxsplit=1)[-1])
            )

        if l3_generic_interface.ip_address == "dhcp" and l3_generic_interface.dhcp_accept_default_route:
            interface.dhcp_client_accept_default_route = True

        return interface

    def _get_l3_uplink_with_l2_as_subint(
        self: AvdStructuredConfigUnderlayProtocol, link: EosDesignsFacts.UplinksItem
    ) -> tuple[EosCliConfigGen.EthernetInterfacesItem, EosCliConfigGen.EthernetInterfaces]:
        """Return a tuple with main uplink interface, list of subinterfaces representing each SVI."""
        vlans = set(map(int, range_expand(link.vlans or "")))

        # Main interface
        # Routed interface with no config unless there is an SVI matching the native-vlan, then it will contain the config for that SVI

        interfaces = EosCliConfigGen.EthernetInterfaces()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    # Skip any vlans not part of the link
                    if svi.id not in vlans:
                        continue

                    interfaces.append(self._get_l2_as_subint(link, svi, vrf))

        # If we have the main interface covered, we can just remove it from the list and return as main interface.
        # Otherwise we return an almost empty dict as the main interface since it was already covered by the calling function.
        if link.interface in interfaces:
            main_interface = interfaces[link.interface]
            del main_interface.description
            del interfaces[link.interface]
        else:
            main_interface = EosCliConfigGen.EthernetInterfacesItem(
                switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False), mtu=self.shared_utils.p2p_uplinks_mtu
            )

        if (mtu := default(main_interface.mtu, 1500)) != self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' conflicts with MTU '{mtu}' "
                f"set on SVI for uplink_native_vlan '{link.native_vlan}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu or change/remove the uplink_native_vlan setting."
            )
            raise AristaAvdError(msg)
        return main_interface, interfaces

    def _get_l2_as_subint(
        self: AvdStructuredConfigUnderlayProtocol,
        link: EosDesignsFacts.UplinksItem,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> EosCliConfigGen.EthernetInterfacesItem:
        """
        Return structured config for one subinterface representing the given SVI.

        Only supports static IPs or VRRP.
        """
        is_native = svi.id == link.native_vlan
        interface_name = link.interface if is_native else f"{link.interface}.{svi.id}"
        subinterface = EosCliConfigGen.EthernetInterfacesItem(
            name=interface_name,
            peer=link.peer,
            peer_interface=f"{link.peer_interface} VLAN {svi.id}",
            peer_type=link.peer_type,
            description=default(svi.description, svi.name),
            shutdown=not default(svi.enabled, False),  # noqa: FBT003
            switchport=EosCliConfigGen.EthernetInterfacesItem.Switchport(enabled=False) if is_native else Undefined,
            encapsulation_dot1q=EosCliConfigGen.EthernetInterfacesItem.EncapsulationDot1q(vlan=svi.id) if not is_native else Undefined,
            vrf=vrf.name if vrf.name != "default" else None,
            ip_address=svi.ip_address,
            ipv6_address=svi.ipv6_address,
            ipv6_enable=svi.ipv6_enable,
            mtu=svi.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            eos_cli=svi.raw_eos_cli,
        )

        if flow_tracker := self.shared_utils.get_flow_tracker(link.flow_tracking, EosCliConfigGen.EthernetInterfacesItem.FlowTracker):
            subinterface.flow_tracker = flow_tracker

        if svi.structured_config:
            self.custom_structured_configs.nested.ethernet_interfaces.obtain(interface_name)._deepmerge(
                svi.structured_config._cast_as(EosCliConfigGen.EthernetInterfacesItem, ignore_extra_keys=True),
                list_merge=self.custom_structured_configs.list_merge_strategy,
            )

        if subinterface.mtu and self.shared_utils.p2p_uplinks_mtu and subinterface.mtu > self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' must be larger or equal to MTU '{subinterface.mtu}' "
                f"set on the SVI '{svi.id}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu."
            )
            raise AristaAvdError(msg)

        # Only set VRRPv4 if ip_address is set
        if subinterface.ip_address:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Only set VRRPv6 if ipv6_address is set
        if subinterface.ipv6_address:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Adding IP helpers and OSPF via a common function also used for SVIs on L3 switches.
        self.shared_utils.get_additional_svi_config(subinterface, svi, vrf)

        return subinterface

    def _get_acl_for_l3_generic_interface(
        self: AvdStructuredConfigUnderlayProtocol,
        acl_name: str,
        interface: (
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
            | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3PortChannelsItem
        ),
    ) -> EosDesigns.Ipv4AclsItem:
        interface_ip = interface.dhcp_ip if (ip_address := interface.ip_address) == "dhcp" else ip_address
        if interface_ip is not None and "/" in interface_ip:
            interface_ip = get_ip_from_ip_prefix(interface_ip)

        return self.shared_utils.get_ipv4_acl(
            name=acl_name,
            interface_name=interface.name,
            interface_ip=interface_ip,
            peer_ip=interface.peer_ip,
        )
