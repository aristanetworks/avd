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

        Covers ipv4_acl_in/out defined under node l3_interfaces.
        """
        if not self._l3_interface_acls:
            return None

        ip_access_lists = []

        for interface_acls in self._l3_interface_acls.values():
            for acl in interface_acls.values():
                append_if_not_duplicate(ip_access_lists, "name", acl, context="IPv4 Access lists for node l3_interfaces", context_keys=["name"])

        return natural_sort(ip_access_lists, "name")
