# Copyright (c) 2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import EosDesignsFactsGenerator, EosDesignsFactsGeneratorProtocol


class UtilsMixin(EosDesignsFactsProtocol, Protocol):
    """
    Mixin Class with helper functions for the EosDesignsFacts class.

    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def get_peer_facts_generator(self: EosDesignsFactsGeneratorProtocol, peer_name: str) -> EosDesignsFactsGenerator:
        """Returns EosDesignsFactsGenerator for the peer. Raise if not found."""
        if peer_name not in self.peer_generators:
            msg = (
                f"Facts not found for node '{peer_name}'. Something in the input vars is pointing to this node. "
                f"Check that '{peer_name}' is in the inventory and is part of the group set by 'fabric_name'. Node is required."
            )
            raise AristaAvdInvalidInputsError(msg)
        return self.peer_generators[peer_name]

    @cached_property
    def _mlag_peer_facts_generator(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsGenerator:
        """EosDesignsFactsGenerator for the MLAG peer. Raises if not found."""
        return self.get_peer_facts_generator(self.shared_utils.mlag_peer)
