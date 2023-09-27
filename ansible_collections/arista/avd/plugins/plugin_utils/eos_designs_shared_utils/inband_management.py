# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_network
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class InbandManagementMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def configure_inband_mgmt(self: SharedUtils) -> bool:
        return self.uplink_type == "port-channel" and self.inband_mgmt_ip

    @cached_property
    def configure_parent_for_inband_mgmt(self: SharedUtils) -> bool:
        return self.configure_inband_mgmt and get(self.switch_data_combined, "inband_mgmt_ip") is None

    @cached_property
    def inband_mgmt_subnet(self: SharedUtils) -> str | None:
        return default(get(self.switch_data_combined, "inband_mgmt_subnet"), get(self.switch_data_combined, "inband_management_subnet"))

    @cached_property
    def inband_mgmt_vlan(self: SharedUtils) -> int:
        return int(default(get(self.switch_data_combined, "inband_mgmt_vlan"), get(self.switch_data_combined, "inband_management_vlan"), 4092))

    @cached_property
    def inband_mgmt_description(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "inband_mgmt_description", default="Inband Management")

    @cached_property
    def inband_mgmt_mtu(self: SharedUtils) -> int | None:
        if not self.platform_settings_feature_support_per_interface_mtu:
            return None

        return get(self.switch_data_combined, "inband_mgmt_mtu", default=1500)

    @cached_property
    def inband_mgmt_vlan_name(self: SharedUtils) -> str:
        return get(self.switch_data_combined, "inband_mgmt_vlan_name", default="INBAND_MGMT")

    @cached_property
    def inband_mgmt_vrf(self: SharedUtils) -> str | None:
        if (inband_mgmt_vrf := get(self.switch_data_combined, "inband_mgmt_vrf")) != "default":
            return inband_mgmt_vrf

        return None

    @cached_property
    def inband_mgmt_gateway(self: SharedUtils) -> str | None:
        """
        Inband management gateway

        If inband_mgmt_ip is set but not via inband_mgmt_subnet we return the value of inband_mgmt_gateway.

        Otherwise if inband_mgmt_subnet is set we return the gateway derived from inband_mgmt_subnet (first IP)

        Otherwise return None
        """
        if self.inband_mgmt_ip is None:
            return None

        if not self.configure_parent_for_inband_mgmt:
            return get(self.switch_data_combined, "inband_mgmt_gateway")

        subnet = ip_network(self.inband_mgmt_subnet, strict=False)
        return f"{str(subnet[1])}"

    @cached_property
    def inband_mgmt_ip(self: SharedUtils) -> str | None:
        """
        Inband management IP
        Set to either:
          - Value of inband_mgmt_ip
          - deducted IP from inband_mgmt_subnet & id
          - None
        """
        if (inband_mgmt_ip := get(self.switch_data_combined, "inband_mgmt_ip")) is not None:
            return inband_mgmt_ip

        if self.inband_mgmt_subnet is None:
            return None

        if self.id is None:
            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to set inband_mgmt_ip from inband_mgmt_subnet")

        subnet = ip_network(self.inband_mgmt_subnet, strict=False)
        inband_mgmt_ip = str(subnet[3 + self.id])
        return f"{inband_mgmt_ip}/{subnet.prefixlen}"

    @cached_property
    def inband_mgmt_interface(self: SharedUtils) -> str | None:
        """
        Inband management Interface used only to set as source interface on various management protocols

        For L2 switches defaults to Vlan<inband_mgmt_vlan>
        For all other devices set to value of inband_mgmt_interface or None
        """
        if (inband_mgmt_interface := get(self.switch_data_combined, "inband_mgmt_interface")) is not None:
            return inband_mgmt_interface

        if self.configure_inband_mgmt:
            return f"Vlan{self.inband_mgmt_vlan}"

        return None
