from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand

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

        All the vlans come from the vlan_trunk
        """

        vlans = {}
        # TODO - can probably do this with sets but need list in the end so not sure it is worth it
        for vlan_trunk_group in self._underlay_vlan_trunk_groups:
            for vlan in range_expand(vlan_trunk_group["vlan_list"]):
                vlans.setdefault(int(vlan), {"trunk_groups": []})["trunk_groups"].extend(vlan_trunk_group["trunk_groups"])

        for vlan, vlan_dict in vlans.items():
            vlan_dict["trunk_groups"] = list(set(vlan_dict["trunk_groups"]))

        if vlans:
            return vlans

        return None
