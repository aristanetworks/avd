# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate

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
        This function also detects duplicate vrfs and raise an error in case of duplicates
        """

        vrfs = []

        for p2p_link in self._filtered_p2p_links:
            if (vrf := p2p_link["data"]["vrf"]) is None or vrf == "default":
                continue

            new_vrf = {
                "name": vrf,
            }

            # Enables ip routing
            new_vrf["ip_routing"] = True
            if self._p2p_link_ipv6_enabled(p2p_link):
                new_vrf["ipv6_routing"] = True

            append_if_not_duplicate(
                list_of_dicts=vrfs,
                primary_key="name",
                new_dict=new_vrf,
                context="VRFs defined under l3_edge or core_interfaces",
                context_keys=["name"],
            )

        if vrfs:
            return vrfs

        return None
