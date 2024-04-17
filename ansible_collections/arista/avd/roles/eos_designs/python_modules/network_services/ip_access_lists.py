# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

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
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        # Curently only needed for Zscaler
        if not (any(internet_exit_policy["type"] == "zscaler" for internet_exit_policy in self._filtered_internet_exit_policies)):
            return None

        return [{"name": "ALLOW_ALL", "entries": [{"sequence": 10, "action": "permit", "protocol": "ip", "source": "any", "destination": "any"}]}]
