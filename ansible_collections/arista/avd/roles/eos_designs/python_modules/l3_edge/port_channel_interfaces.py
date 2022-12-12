from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class PortChannelInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def port_channel_interfaces(self) -> dict | None:
        """
        Return structured config for port_channel_interfaces
        """
        port_channel_interfaces = {}
        for p2p_link in self._filtered_p2p_links:
            if p2p_link["data"]["port_channel_id"] is None:
                continue

            # Port-Channel interface
            port_channel_interface = self._get_common_interface_cfg(p2p_link)

            # Remove None values
            port_channel_interface = {key: value for key, value in port_channel_interface.items() if value is not None}

            interface_name = p2p_link["data"]["interface"]
            port_channel_interfaces[interface_name] = port_channel_interface
            continue

        if port_channel_interfaces:
            return port_channel_interfaces

        return None
