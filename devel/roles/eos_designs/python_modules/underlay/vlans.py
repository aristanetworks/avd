from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class VlansMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def vlans(self) -> dict | None:
        """
        Return structured config for vlans

        This function goes through all the underlay trunk groups and returns an
        inverted dict where the key is the vlan ID and the value is the list of
        the unique trunk groups that should be configured under this vlan.

        The function also creates uplink_native_vlan for this switch or downstream switches.
        """

        vlans = {}
        # TODO - can probably do this with sets but need list in the end so not sure it is worth it
        for vlan_trunk_group in self._underlay_vlan_trunk_groups:
            for vlan in range_expand(vlan_trunk_group["vlan_list"]):
                vlans.setdefault(int(vlan), {"trunk_groups": []})["trunk_groups"].extend(vlan_trunk_group["trunk_groups"])

        for vlan, vlan_dict in vlans.items():
            vlan_dict["trunk_groups"] = natural_sort(set(vlan_dict["trunk_groups"]))

        # Add configuration for uplink or peer's uplink_native_vlan if it is not defined as part of network services
        switch_vlans = range_expand(get(self._hostvars, "switch.vlans"))
        uplink_native_vlans = set(
            link["native_vlan"] for link in self._underlay_links if "native_vlan" in link and str(link["native_vlan"]) not in switch_vlans
        )
        for peer_uplink_native_vlan in uplink_native_vlans:
            vlans.setdefault(int(peer_uplink_native_vlan), {}).update(
                {
                    "name": "NATIVE",
                    "state": "suspend",
                }
            )

        if vlans:
            return vlans

        return None
