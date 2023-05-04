from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import load_interfacedescriptions
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import load_ip_addressing

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
from .static_routes import StaticRoutesMixin
from .struct_cfg import StructCfgMixin
from .virtual_source_nat_vrfs import VirtualSourceNatVrfsMixin
from .vlan_interfaces import VlanInterfacesMixin
from .vlans import VlansMixin
from .vrfs import VrfsMixin
from .vxlan_interface import VxlanInterfaceMixin


class AvdStructuredConfig(
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
    StructCfgMixin,
    PrefixListsMixin,
    VxlanInterfaceMixin,
    VirtualSourceNatVrfsMixin,
    RouterIsisMixin,
    RouterMulticastMixin,
    RouterPimSparseModeMixin,
):
    """
    The AvdStructuredConfig Class is imported by "yaml_templates_to_facts" to render parts of the structured config.

    "yaml_templates_to_facts" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to inherit the _hostvars, keys and other attributes.
    All other methods are included as "Mixins" to make the files more managable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def __init__(self, hostvars, templar):
        super().__init__(hostvars, templar)
        self._avd_ip_addressing = load_ip_addressing(hostvars, templar)
        self._avd_interface_descriptions = load_interfacedescriptions(hostvars, templar)

    def render(self) -> dict:
        """
        Wrap class render function with a check if one of the following vars are True
        - switch.network_services_l2
        - switch.network_services_l3
        - switch.network_services_l1
        """
        if self._any_network_services:
            return super().render()
        return {}
