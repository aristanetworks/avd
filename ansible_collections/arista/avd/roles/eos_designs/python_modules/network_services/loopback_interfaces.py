# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get

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
                if (loopback_interface := self._get_vtep_diagnostic_loopback_for_vrf(vrf)) is not None:
                    append_if_not_duplicate(
                        list_of_dicts=loopback_interfaces,
                        primary_key="name",
                        new_dict=loopback_interface,
                        context="VTEP Diagnostic Loopback Interfaces",
                        context_keys=["name", "vrf", "tenant"],
                        ignore_keys={"tenant"},
                    )

                # The loopback_interfaces have already been filtered in _filtered_tenants
                # to only contain entries with our hostname
                for loopback_interface in vrf["loopback_interfaces"]:
                    interface = {
                        "name": loopback_interface.get("interface"),
                        "ip_address": loopback_interface.get("ip_address"),
                        "shutdown": not loopback_interface.get("enabled", True),
                        "description": loopback_interface.get("description"),
                        "eos_cli": loopback_interface.get("raw_eos_cli"),
                    }

                    if vrf["name"] != "default":
                        interface["vrf"] = vrf["name"]

                    if get(loopback_interface, "ospf.enabled") is True and get(vrf, "ospf.enabled") is True:
                        interface["ospf_area"] = loopback_interface["ospf"].get("area", "0")

                    # Strip None values from interface before adding to list
                    interface = {key: value for key, value in interface.items() if value is not None}
                    append_if_not_duplicate(
                        list_of_dicts=loopback_interfaces,
                        primary_key="name",
                        new_dict=interface,
                        context="Loopback Interfaces defined under loopback_interfaces",
                        context_keys=["name", "vrf"],
                    )

        if loopback_interfaces:
            return loopback_interfaces

        return None
