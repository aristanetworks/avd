# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate

from .utils import UtilsMixin


class IpAccesslistsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_access_lists(self) -> list | None:
        """
        Return structured config for ip_access_lists.
        """
        ip_access_lists = []
        if self._svi_acls:
            for interface_acls in self._svi_acls.values():
                for acl in interface_acls.values():
                    append_if_not_duplicate(ip_access_lists, "name", acl, context="IPv4 Access lists for SVI", context_keys=["name"])

        if self._filtered_internet_exit_policies:
            ip_access_lists.append(
                {
                    "name": "ALLOW-ALL",
                    "entries": [
                        {
                            "sequence": 10,
                            "action": "permit",
                            "protocol": "ip",
                            "source": "any",
                            "destination": "any",
                        }
                    ],
                }
            )

        return natural_sort(ip_access_lists, "name") or None
