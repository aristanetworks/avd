from __future__ import annotations

from functools import cached_property
from typing import NoReturn

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError

from .utils import UtilsMixin


class VlansMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def vlans(self) -> dict | None:
        """
        Return structured config for vlans.

        Consist of svis, mlag peering vlans and l2vlans from filtered tenants.

        This function also detects duplicate vlans and raise an error in case of duplicates between
        SVIs in all VRFs and L2VLANs deployed on this device.
        """

        if not self._network_services_l2:
            return None

        vlans = {}
        for tenant in self._filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in vrf["svis"]:
                    vlan_id = int(svi["id"])
                    if vlan_id in vlans:
                        self._raise_duplicate_vlan_error(vlan_id, f"SVI in VRF '{vrf['name']}'", tenant["name"], vlans[vlan_id])

                    vlans[vlan_id] = self._get_vlan_config(svi, tenant)

                # MLAG IBGP Peering VLANs per VRF
                # Continue to next VRF if mlag vlan_id is not set
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is None:
                    continue

                if vlan_id in vlans:
                    self._raise_duplicate_vlan_error(
                        vlan_id, f"MLAG Peering VLAN in vrf '{vrf['name']}' (check for duplicate VRF VNI/ID)", tenant["name"], vlans[vlan_id]
                    )

                vlans[vlan_id] = {
                    "tenant": tenant["name"],
                    "name": f"MLAG_iBGP_{vrf['name']}",
                    "trunk_groups": [self._trunk_groups_mlag_l3_name],
                }

            # L2 Vlans per Tenant
            for l2vlan in tenant["l2vlans"]:
                vlan_id = int(l2vlan["id"])
                if vlan_id in vlans:
                    self._raise_duplicate_vlan_error(vlan_id, "L2VLAN", tenant["name"], vlans[vlan_id])

                vlans[vlan_id] = self._get_vlan_config(l2vlan, tenant)

        if vlans:
            return vlans

        return None

    def _get_vlan_config(self, vlan, tenant) -> dict:
        """
        Return structured config for one given vlan

        Can be used for svis and l2vlans
        """
        vlans_vlan = {
            "tenant": tenant["name"],
            "name": vlan["name"],
        }
        if self._enable_trunk_groups:
            trunk_groups = vlan.get("trunk_groups", [])
            if self._only_local_vlan_trunk_groups:
                trunk_groups = list(self._local_endpoint_trunk_groups.intersection(trunk_groups))
            if self._mlag:
                trunk_groups.append(self._trunk_groups_mlag_name)
            if self._uplink_type == "port-channel":
                trunk_groups.append(self._trunk_groups_uplink_name)
            vlans_vlan["trunk_groups"] = trunk_groups

        return vlans_vlan

    def _raise_duplicate_vlan_error(self, vlan_id: int, context: str, tenant_name: str, duplicate_vlan_config: dict) -> NoReturn:
        msg = f"Duplicate VLAN ID '{vlan_id}' found in Tenant '{tenant_name}' during configuration of {context}."
        if (duplicate_vlan_tenant := duplicate_vlan_config["tenant"]) != tenant_name:
            msg = f"{msg} Other VLAN is in Tenant '{duplicate_vlan_tenant}'."

        raise AristaAvdError(msg)
