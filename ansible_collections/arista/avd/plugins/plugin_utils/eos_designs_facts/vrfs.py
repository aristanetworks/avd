# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate

if TYPE_CHECKING:
    from .eos_designs_facts import EosDesignsFacts


class VrfsMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vrfs(self: EosDesignsFacts) -> list:
        """
        Exposed in avd_switch_facts

        Raise an error if the same VRF in two different tenants has conflicting `vrf_id`

        Return the list of vrfs to be defined on this switch

        Ex. ["default", "prod"]
        """
        vrfs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                # TODO confirm the logic with reviewers.
                append_if_not_duplicate(
                    list_of_dicts=vrfs,
                    primary_key="name",
                    new_dict={"name": vrf["name"], "vrf_id": vrf.get("vrf_id")},
                    context="VRFs in multiple tenants",
                    context_keys=["name"],
                )
        return natural_sort(vrf["name"] for vrf in vrfs)
