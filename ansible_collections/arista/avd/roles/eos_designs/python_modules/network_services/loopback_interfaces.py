# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get, get_item

from .utils import UtilsMixin


class LoopbackInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def loopback_interfaces(self) -> list | None:
        """
        Return structured config for loopback_interfaces

        Used for Tenant vrf loopback interfaces
        This function is also called from virtual_source_nat_vrfs to avoid duplicate logic
        """

        if not (self.shared_utils.network_services_l3):
            return None

        loopback_interfaces = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                if (loopback := get(vrf, "vtep_diagnostic.loopback")) is None:
                    continue

                if (loopback_ipv4_pool := get(vrf, "vtep_diagnostic.loopback_ip_range")) is None:
                    if (pod_name := self.shared_utils.pod_name) is None:
                        # Skip this vrf since we have no loopback_ip_range and pod_name
                        continue

                    if (loopback_ip_pools := get(vrf, "vtep_diagnostic.loopback_ip_pools")) is None:
                        # Skip this vrf since we have no pools either
                        continue

                    if (loopback_ipv4_pool := get_item(loopback_ip_pools, "pod", pod_name, default={}).get("ipv4_pool")) is None:
                        # Skip this vrf since we cannot find our pod_name in the pools or the pool is missing the ipv4_pool
                        continue

                # If we ended up here, it means we have a loopback_ipv4_pool set
                interface_name = f"Loopback{loopback}"
                loopback_interface = {
                    "name": interface_name,
                    "description": get(vrf, "vtep_diagnostic.loopback_description", default=f"{vrf['name']}_VTEP_DIAGNOSTICS"),
                    "shutdown": False,
                    "vrf": vrf["name"],
                    "ip_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ip(loopback_ipv4_pool)}/32",
                }
                append_if_not_duplicate(
                    list_of_dicts=loopback_interfaces,
                    primary_key="name",
                    new_dict=loopback_interface,
                    context="VTEP Diagnostic Loopback Interfaces",
                    context_keys=["name", "vrf", "tenant"],
                    ignore_keys={"tenant"},
                )
        if loopback_interfaces:
            return loopback_interfaces

        return None
