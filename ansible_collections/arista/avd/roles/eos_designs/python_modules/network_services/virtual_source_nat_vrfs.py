# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class VirtualSourceNatVrfsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    # Set type hints for Attributes of the main class as needed
    loopback_interfaces: dict

    @cached_property
    def virtual_source_nat_vrfs(self) -> list | None:
        """
        Return structured config for virtual_source_nat_vrfs

        Only used by VTEPs with L2 and L3 services
        Using data from _loopback_interfaces to avoid duplicating logic
        """
        if not (self.shared_utils.overlay_vtep and self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return None

        if (loopback_interfaces := self.loopback_interfaces) is None:
            return None

        virtual_source_nat_vrfs = []
        for loopback_interface in loopback_interfaces:
            virtual_source_nat_vrfs.append(
                {
                    "name": loopback_interface["vrf"],
                    "ip_address": loopback_interface["ip_address"].split("/", maxsplit=1)[0],
                }
            )

        if virtual_source_nat_vrfs:
            return virtual_source_nat_vrfs

        return None
