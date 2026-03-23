# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils.run_once import RunOnceMethodStateHelper

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
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


__all__ = ["StructuredConfigUtils"]
