from __future__ import annotations

from functools import cached_property
from typing import NoReturn

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_item

from .utils import UtilsMixin


class VrfsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def vrfs(self) -> list | None:
        """
        Return structured config for vrfs.

        Used for creating VRFs except VRF "default".

        This function also detects duplicate vrfs and raise an error in case of duplicates between
        all Tenants deployed on this device.
        """

        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        vrf_names = []
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                vrf_name = vrf["name"]
                if vrf_name == "default":
                    continue

                if vrf_name in vrf_names:
                    self._raise_duplicate_vrf_error(vrf_name, tenant["name"], get_item(vrfs, "name", vrf_name))

                vrf_names.append(vrf_name)

                new_vrf = {
                    "name": vrf_name,
                    "tenant": tenant["name"],
                }

                # MLAG IBGP Peering VLANs per VRF
                if self.shared_utils.overlay_mlag_rfc5549 and self._mlag_ibgp_peering_enabled(vrf, tenant):
                    new_vrf["ip_routing_ipv6_interfaces"] = True
                else:
                    new_vrf["ip_routing"] = True

                if self._has_ipv6(vrf):
                    new_vrf["ipv6_routing"] = True

                if "description" in vrf:
                    new_vrf["description"] = vrf["description"]

                vrfs.append(new_vrf)

        if vrfs:
            return vrfs

        return None

    def _has_ipv6(self, vrf) -> bool:
        """
        Return bool if IPv6 is configured in the given VRF.

        Expects a VRF definition coming from _filtered_tenants, where all keys have been set and filtered
        """
        for svi in vrf["svis"]:
            if svi.get("ipv6_address_virtual") is not None:
                return True

            if len(svi.get("ipv6_address_virtuals", [])) > 0:
                return True

            if svi.get("ipv6_address") is not None:
                return True

        return False

    def _raise_duplicate_vrf_error(self, vrf_name: str, tenant_name: str, duplicate_vrf_config: dict) -> NoReturn:
        msg = f"Duplicate VRF '{vrf_name}' found in Tenant '{tenant_name}'."
        if (duplicate_vlan_tenant := duplicate_vrf_config["tenant"]) != tenant_name:
            msg = f"{msg} Other VRF is in Tenant '{duplicate_vlan_tenant}'."

        raise AristaAvdError(msg)
