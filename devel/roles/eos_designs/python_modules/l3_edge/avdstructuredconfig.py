from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts

from .ethernet_interfaces import EthernetInterfacesMixin
from .port_channel_interfaces import PortChannelInterfacesMixin
from .router_bgp import RouterBgpMixin
from .router_ospf import RouterOspfMixin


class AvdStructuredConfig(
    AvdFacts,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    RouterBgpMixin,
    RouterOspfMixin,
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

    def render(self) -> dict:
        """
        Wrap class render function with a check if l3_edge is set
        """
        if self._l3_edge is not None:
            return super().render()
        return {}
