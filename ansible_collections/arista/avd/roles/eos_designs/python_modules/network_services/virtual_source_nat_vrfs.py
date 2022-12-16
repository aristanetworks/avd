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
    def virtual_source_nat_vrfs(self) -> dict | None:
        """
        Return structured config for virtual_source_nat_vrfs

        Only used by VTEPs with L2 and L3 services
        Using data from _loopback_interfaces to avoid duplicating logic
        """
        if not (self._overlay_vtep and self._network_services_l2 and self._network_services_l3):
            return None

        if (loopback_interfaces := self.loopback_interfaces) is None:
            return None

        virtual_source_nat_vrfs = {}
        for loopback_interface in loopback_interfaces.values():
            vrf_name = loopback_interface["vrf"]
            virtual_source_nat_vrfs[vrf_name] = {
                "ip_address": loopback_interface["ip_address"].split("/", maxsplit=1)[0],
            }

        if virtual_source_nat_vrfs:
            return virtual_source_nat_vrfs

        return None
