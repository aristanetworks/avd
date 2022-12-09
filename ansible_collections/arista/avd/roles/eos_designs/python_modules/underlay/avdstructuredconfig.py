from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import load_interfacedescriptions

from .ethernet_interfaces import EthernetInterfacesMixin
from .loopback_interfaces import LoopbackInterfacesMixin
from .mpls import MplsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .prefix_lists import PrefixListsMixin
from .route_maps import RouteMapsMixin
from .router_bgp import RouterBgpMixin
from .router_isis import RouterIsisMixin
from .router_ospf import RouterOspfMixin
from .vlans import VlansMixin


class AvdStructuredConfig(
    AvdFacts,
    VlansMixin,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    LoopbackInterfacesMixin,
    RouterBgpMixin,
    RouterOspfMixin,
    PrefixListsMixin,
    RouteMapsMixin,
    RouterIsisMixin,
    MplsMixin,
):
    """
    The AvdStructuredConfig Class is imported used "yaml_templates_to_facts" to render parts of the structured config.

    "yaml_templates_to_facts" imports, instantiates and run the .render() method on the class.
    .render() runs all class methods not starting with _ and of type @cached property and inserts the returned data into
    a dict with the name of the method as key. This means that each key in the final dict corresponds to a method.

    The Class uses AvdFacts, as the base class, to get the render, keys and other attributes.
    All other methods are included as "Mixins" to make the files more managable.

    The order of the @cached_properties methods imported from Mixins will also control the order in the output.
    """

    def __init__(self, hostvars, templar):
        super().__init__(hostvars, templar)
        self._avd_interface_descriptions = load_interfacedescriptions(hostvars, templar)
