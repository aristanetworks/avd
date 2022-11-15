from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class IpVirtualRouterMacAddressMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_virtual_router_mac_address(self) -> str | None:
        """
        Return structured config for ip_virtual_router_mac_address
        """
        if self._network_services_l2 and self._network_services_l3:
            mac = get(self._hostvars, "switch.virtual_router_mac_address", required=True, org_key="virtual_router_mac_address")
            return str(mac).lower()

        return None
