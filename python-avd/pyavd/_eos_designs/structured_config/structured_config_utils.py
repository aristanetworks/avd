# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker


class StructuredConfigUtils:
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(self) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance."""
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""


__all__ = ["StructuredConfigUtils"]
