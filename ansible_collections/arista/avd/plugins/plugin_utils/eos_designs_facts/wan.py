# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .eos_designs_facts import EosDesignsFacts


class WanMixin:
    """
    Mixin Class providing a subset of EosDesignsFacts
    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_path_groups(self: EosDesignsFacts) -> list | None:
        """
        Return the list of WAN path_groups directly connected to this router, with a list of dictionaries
        containing the (interface, ip_address) in the path_group.
        """
        if not self.shared_utils.wan_mode:
            return None

        res = []
        for interface in self.shared_utils.wan_interfaces:
            pg_name = get(interface, "wan_path_group", required=True)
            if (pg_dict := get_item(res, "name", pg_name)) is None:
                res.append(
                    {
                        "name": pg_name,
                        "interfaces": [{"name": get(interface, "interface", required=True), "ip_address": get(interface, "ip", required=True)}],
                    }
                )
            else:
                pg_dict.append({"name": get(interface, "interface", required=True), "ip_address": get(interface, "ip", required=True)})

        return res
