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

    def _set_ipv4_acl(self: StructuredConfigUtils, ipv4_acl: EosDesigns.Ipv4AclsItem) -> None:
        """
        Set structured config for ip_access_lists.

        Called for each interface in l3_interfaces and l3_port_channels when applying ipv4_acls
        """
        self.structured_config.ip_access_lists.append(ipv4_acl._cast_as(EosCliConfigGen.IpAccessListsItem))

    def _set_ipv6_acl(self: StructuredConfigUtils, ipv6_acl: EosDesigns.Ipv6AclsItem) -> None:
        """
        Set structured config for ip_access_lists.

        Called for each interface in l3_interfaces and l3_port_channels when applying ipv6_acls
        """
        self.structured_config.ipv6_access_lists.append(ipv6_acl._cast_as(EosCliConfigGen.Ipv6AccessListsItem))


__all__ = ["StructuredConfigUtils"]
