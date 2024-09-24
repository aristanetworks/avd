# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class StandardAccessListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def standard_access_lists(self: AvdStructuredConfigUnderlay) -> list | None:
        """
        return structured config for standard_access_lists.

        Used for to configure ACLs used by multicast RPs for the underlay
        """
        if self.shared_utils.underlay_multicast_rps is None:
            return None

        standard_access_lists = []
        for rp_entry in self.shared_utils.underlay_multicast_rps:
            if rp_entry.get("groups") is None or rp_entry.get("access_list_name") is None:
                continue

            standard_access_lists.append(
                {
                    "name": rp_entry["access_list_name"],
                    "sequence_numbers": [
                        {
                            "sequence": (index + 1) * 10,
                            "action": f"permit {group}",
                        }
                        for index, group in enumerate(rp_entry["groups"])
                    ],
                },
            )

        if standard_access_lists:
            return standard_access_lists

        return None
