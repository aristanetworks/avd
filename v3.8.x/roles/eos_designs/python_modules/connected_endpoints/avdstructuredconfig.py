from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.interface_descriptions import load_interfacedescriptions
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import load_ip_addressing

from .ethernet_interfaces import EthernetInterfacesMixin
from .monitor_sessions import MonitorSessionsMixin
from .port_channel_interfaces import PortChannelInterfacesMixin


class AvdStructuredConfig(
    AvdFacts,
    EthernetInterfacesMixin,
    PortChannelInterfacesMixin,
    MonitorSessionsMixin,
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
        - switch.connected_endpoints
        """
        if get(self._hostvars, "switch.connected_endpoints") is True:
            return super().render()
        return {}
