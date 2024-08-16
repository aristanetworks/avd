# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pyavd._eos_designs.avdfacts import AvdFacts

from .agents import AgentsMixin
from .as_path import AsPathMixin
from .dhcp_server import DhcpServerMixin
from .ethernet_interfaces import EthernetInterfacesMixin
from .ip_access_lists import IpAccesslistsMixin
from .loopback_interfaces import LoopbackInterfacesMixin
from .mpls import MplsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .prefix_lists import PrefixListsMixin
from .route_maps import RouteMapsMixin
from .router_bgp import RouterBgpMixin
from .router_isis import RouterIsisMixin
from .router_msdp import RouterMsdpMixin
from .router_ospf import RouterOspfMixin
from .router_pim_sparse_mode import RouterPimSparseModeMixin
from .standard_access_lists import StandardAccessListsMixin
from .static_routes import StaticRoutesMixin
from .vlans import VlansMixin


class AvdStructuredConfigUnderlay(
    AvdFacts,
    VlansMixin,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    LoopbackInterfacesMixin,
    RouterBgpMixin,
    AsPathMixin,
    RouterOspfMixin,
    PrefixListsMixin,
    RouteMapsMixin,
    RouterIsisMixin,
    RouterMsdpMixin,
    RouterPimSparseModeMixin,
    StandardAccessListsMixin,
    StaticRoutesMixin,
    MplsMixin,
    AgentsMixin,
    IpAccesslistsMixin,
    DhcpServerMixin,
):
    """
    The AvdStructuredConfig Class is imported used "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more manageable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """
