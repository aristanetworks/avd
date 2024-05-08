# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from functools import cached_property

from .utils import UtilsMixin


class IpNatMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def ip_nat(self) -> dict | None:
        """
        Returns structured config for ip_nat
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        ip_nat = defaultdict(list)

        # TODO: Make NAT configuration more centralized
        if any(internet_exit_policy["type"] == "zscaler" for internet_exit_policy in self._filtered_internet_exit_policies):
            ip_nat["pools"] = [
                {
                    "name": "PORT-ONLY-POOL",
                    "type": "port-only",
                    "ranges": [
                        {
                            "first_port": 1500,
                            "last_port": 65535,
                        }
                    ],
                }
            ]
            ip_nat["profiles"].append(
                {
                    "name": "PORT-ONLY-VRF-AWARE-NAT",
                    "source": {
                        "dynamic": [
                            {
                                "access_list": "ALLOW-ALL",
                                "pool_name": "PORT-ONLY-POOL",
                                "nat_type": "pool",
                            }
                        ]
                    },
                }
            )

        if any(internet_exit_policy["type"] == "direct" for internet_exit_policy in self._filtered_internet_exit_policies):
            ip_nat["profiles"].append(
                {
                    "name": "VRF-AWARE-NAT",
                    "source": {
                        "dynamic": [
                            {
                                "access_list": "ALLOW-ALL",
                                "nat_type": "overload",
                            }
                        ]
                    },
                }
            )

        if ip_nat:
            return ip_nat

        return None
