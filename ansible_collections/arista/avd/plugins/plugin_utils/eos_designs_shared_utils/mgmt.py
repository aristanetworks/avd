from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class MgmtMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mgmt_interface(self: SharedUtils) -> str | None:
        """
        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface
        """
        return default(
            get(self.switch_data_combined, "mgmt_interface"),
            self.platform_settings.get("management_interface"),
            get(self.hostvars, "mgmt_interface"),
        )

    @cached_property
    def ipv6_mgmt_ip(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "ipv6_mgmt_ip")

    @cached_property
    def mgmt_ip(self: SharedUtils) -> str | None:
        return get(self.switch_data_combined, "mgmt_ip")

    @cached_property
    def mgmt_interface_vrf(self: SharedUtils) -> str | None:
        return get(self.hostvars, "mgmt_interface_vrf")

    @cached_property
    def mgmt_gateway(self: SharedUtils) -> str | None:
        return get(self.hostvars, "mgmt_gateway")

    @cached_property
    def ipv6_mgmt_gateway(self: SharedUtils) -> str | None:
        return get(self.hostvars, "ipv6_mgmt_gateway")
