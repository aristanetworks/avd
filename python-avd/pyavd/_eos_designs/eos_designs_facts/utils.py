# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils import get

if TYPE_CHECKING:
    from . import EosDesignsFacts, EosDesignsFactsProtocol


class UtilsMixin(Protocol):
    """
    Mixin Class with helper functions for the EosDesignsFacts class.

    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def get_peer_facts_cls(self: EosDesignsFactsProtocol, peer_name: str) -> EosDesignsFacts:
        """Returns an instance of EosDesignsFacts for the peer. Raise if not found."""
        msg = (
            f"Facts not found for node '{peer_name}'. Something in the input vars is pointing to this node. "
            f"Check that '{peer_name}' is in the inventory and is part of the group set by 'fabric_name'. Node is required."
        )
        return get(self._hostvars, f"avd_switch_facts..{peer_name}..switch", separator="..", required=True, custom_error_msg=msg)

    @cached_property
    def _mlag_peer_facts(self: EosDesignsFactsProtocol) -> EosDesignsFacts:
        """EosDesignsFacts for the MLAG peer. Raises if not found."""
        return self.get_peer_facts_cls(self.shared_utils.mlag_peer)
