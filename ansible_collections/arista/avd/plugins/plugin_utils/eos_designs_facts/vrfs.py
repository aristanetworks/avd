# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .eos_designs_facts import EosDesignsFacts


class VrfsMixin:
    """
    Mixin Class used to generate some of the EosDesignsFacts.
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vrfs(self: EosDesignsFacts) -> str:
        """
        Exposed in avd_switch_facts

        Return the list of vrfs to be defined on this switch

        Ex. "[default, prod,]"
        """
        return natural_sort(set(vrf["name"] for tenant in self.shared_utils.filtered_tenants for vrf in tenant["vrfs"]))
