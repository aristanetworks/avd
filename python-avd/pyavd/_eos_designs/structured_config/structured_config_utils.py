# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils.run_once import RunOnceMethodStateHelper

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol


class StructuredConfigUtils(RunOnceMethodStateHelper):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self,
        structured_config: EosCliConfigGen,
        inputs: EosDesigns,
        shared_utils: SharedUtilsProtocol,
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        self.inputs = inputs
        self.shared_utils = shared_utils
        """The shared structured config instance to write config into."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""

    def set_sequence_numbers_inband_mgmt(self: StructuredConfigUtils) -> None:
        """Set rules in route map RM-CONN-2-BGP for inband mgmt."""
        route_map = self.structured_config.route_maps.obtain("RM-CONN-2-BGP")
        if self.shared_utils.inband_management_parent_vlans and self.shared_utils.inband_mgmt_vrf is None:
            if self.shared_utils.inband_mgmt_ipv4_parent:
                route_map.sequence_numbers.append_new(
                    sequence=20, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-L2LEAF-INBAND-MGMT"])
                )

                pl_sequence_numbers = EosCliConfigGen.PrefixListsItem.SequenceNumbers()
                for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
                    pl_sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv4']}")

                self.structured_config.prefix_lists.append_new(name="PL-L2LEAF-INBAND-MGMT", sequence_numbers=pl_sequence_numbers)

            if self.shared_utils.inband_mgmt_ipv6_parent:
                route_map.sequence_numbers.append_new(
                    sequence=60,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list IPv6-PL-L2LEAF-INBAND-MGMT"]),
                )
                pl_sequence_numbers = EosCliConfigGen.Ipv6PrefixListsItem.SequenceNumbers()
                for index, subnet in enumerate(self.shared_utils.inband_management_parent_vlans.values(), start=1):
                    pl_sequence_numbers.append_new(sequence=(index) * 10, action=f"permit {subnet['ipv6']}")

                self.structured_config.ipv6_prefix_lists.append_new(name="IPv6-PL-L2LEAF-INBAND-MGMT", sequence_numbers=pl_sequence_numbers)


__all__ = ["StructuredConfigUtils"]
