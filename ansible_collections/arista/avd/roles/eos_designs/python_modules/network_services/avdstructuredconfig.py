# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts

from .eos_cli import EosCliMixin
from .ethernet_interfaces import EthernetInterfacesMixin
from .ip_igmp_snooping import IpIgmpSnoopingMixin
from .ip_virtual_router_mac_address import IpVirtualRouterMacAddressMixin
from .ipv6_static_routes import Ipv6StaticRoutesMixin
from .loopback_interfaces import LoopbackInterfacesMixin
from .patch_panel import PatchPanelMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .prefix_lists import PrefixListsMixin
from .route_maps import RouteMapsMixin
from .router_bgp import RouterBgpMixin
from .router_isis import RouterIsisMixin
from .router_multicast import RouterMulticastMixin
from .router_ospf import RouterOspfMixin
from .router_pim_sparse_mode import RouterPimSparseModeMixin
from .standard_access_lists import StandardAccessListsMixin
from .static_routes import StaticRoutesMixin
from .struct_cfgs import StructCfgsMixin
from .virtual_source_nat_vrfs import VirtualSourceNatVrfsMixin
from .vlan_interfaces import VlanInterfacesMixin
from .vlans import VlansMixin
from .vrfs import VrfsMixin
from .vxlan_interface import VxlanInterfaceMixin


class AvdStructuredConfigNetworkServices(
    AvdFacts,
    PatchPanelMixin,
    VlansMixin,
    IpIgmpSnoopingMixin,
    IpVirtualRouterMacAddressMixin,
    VlanInterfacesMixin,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    LoopbackInterfacesMixin,
    RouteMapsMixin,
    Ipv6StaticRoutesMixin,
    StaticRoutesMixin,
    RouterBgpMixin,
    RouterOspfMixin,
    VrfsMixin,
    EosCliMixin,
    StructCfgsMixin,
    PrefixListsMixin,
    VxlanInterfaceMixin,
    VirtualSourceNatVrfsMixin,
    RouterIsisMixin,
    RouterMulticastMixin,
    RouterPimSparseModeMixin,
    StandardAccessListsMixin,
):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more managable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def render(self) -> dict:
        """
        Wrap class render function with a check if one of the following vars are True
        - node_type_keys.[].network_services_l2
        - node_type_keys.[].network_services_l3
        - node_type_keys.[].network_services_l1
        """
        if self.shared_utils.any_network_services:
            return super().render()
        return {}
