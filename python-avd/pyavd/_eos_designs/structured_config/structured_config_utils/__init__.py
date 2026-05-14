# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
Structured Config Utils Module.

This module provides utility classes for structured config generation.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.parent_interfaces import ParentInterfacesTracker
from pyavd._utils.run_once import RunOnceMethodStateHelper

from .mlag import MlagMixin
from .sflow import SflowMixin
from .underlay import UnderlayMixin
from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd._eos_designs.schema import EosDesigns
    from pyavd._eos_designs.shared_utils import SharedUtilsProtocol
    from pyavd._eos_designs.structured_config.structured_config_generator import StructCfgs


class StructuredConfigUtilsProtocol(UtilsMixin, MlagMixin, UnderlayMixin, SflowMixin, Protocol):
    structured_config: EosCliConfigGen
    custom_structured_configs: StructCfgs
    shared_utils: SharedUtilsProtocol
    inputs: EosDesigns


class StructuredConfigUtils(RunOnceMethodStateHelper, StructuredConfigUtilsProtocol):
    """
    Utility class for structured config generation.

    This class holds shared utilities and trackers used across all structured config modules.
    """

    def __init__(
        self, structured_config: EosCliConfigGen, inputs: EosDesigns, shared_utils: SharedUtilsProtocol, custom_structured_configs: StructCfgs
    ) -> None:
        """Initialize the StructuredConfigUtils with a ParentInterfacesTracker instance and structured config instance."""
        super().__init__()
        self.structured_config = structured_config
        """The shared structured config instance to write config into."""
        self.inputs = inputs
        self.shared_utils = shared_utils
        self.custom_structured_configs = custom_structured_configs
        self.parent_interfaces_tracker = ParentInterfacesTracker()
        """Tracker for parent interfaces that need to be created for subinterfaces."""
