from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class InbandManagementMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    """

    hostname: str
    hostvars: dict
    id: int
    switch_data_combined: dict
    uplink_type: str

    @cached_property
    def inband_management_subnet(self) -> str | None:
        return get(self.switch_data_combined, "inband_management_subnet")

    @cached_property
    def inband_management_vlan(self) -> int | None:
        if self.inband_management_subnet is not None and self.uplink_type == "port-channel":
            return int(get(self.switch_data_combined, "inband_management_vlan", default=4092))
        return None

    @cached_property
    def inband_management_gateway(self) -> str:
        subnet = ip_network(self.inband_management_subnet, strict=False)
        hosts = list(subnet.hosts())
        return str(hosts[0])

    @cached_property
    def inband_management_ip(self) -> str:
        if self.id is None:
            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to set inband_management_ip")

        subnet = ip_network(self.inband_management_subnet, strict=False)
        hosts = list(subnet.hosts())
        inband_management_ip = str(hosts[2 + self.id])
        inband_management_prefix = str(subnet.prefixlen)
        return f"{inband_management_ip}/{inband_management_prefix}"

    @cached_property
    def inband_management_interface(self) -> str | None:
        return f"Vlan{self.inband_management_vlan}"
