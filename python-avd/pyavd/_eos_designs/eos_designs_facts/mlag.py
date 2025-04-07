# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._utils import remove_cached_property_type

if TYPE_CHECKING:
    from . import EosDesignsFactsGeneratorProtocol


class MlagMixin(EosDesignsFactsProtocol, Protocol):
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @remove_cached_property_type
    @cached_property
    def mlag_peer(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_peer
        return None

    @remove_cached_property_type
    @cached_property
    def mlag_port_channel_id(self: EosDesignsFactsGeneratorProtocol) -> int | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_port_channel_id
        return None

    @remove_cached_property_type
    @cached_property
    def mlag_interfaces(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.MlagInterfaces:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return EosDesignsFactsProtocol.MlagInterfaces(self.shared_utils.mlag_interfaces)
        return EosDesignsFactsProtocol.MlagInterfaces()

    @remove_cached_property_type
    @cached_property
    def mlag_ip(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.mlag:
            return self.shared_utils.mlag_ip
        return None

    @remove_cached_property_type
    @cached_property
    def mlag_l3_ip(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """
        Exposed in avd_switch_facts.

        Only if L3 and not running rfc5549 for both underlay and overlay
        """
        if (
            self.shared_utils.mlag_l3
            and self.shared_utils.mlag_peer_l3_vlan is not None
            and not (self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549)
        ):
            return self.shared_utils.mlag_l3_ip
        return None

    @remove_cached_property_type
    @cached_property
    def mlag_switch_ids(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.MlagSwitchIds:
        """
        Exposed in avd_switch_facts.

        Returns the switch ids of both primary and secondary switches for a given node group or an empty class.
        {"primary": int, "secondary": int}
        """
        if not (mlag_switch_ids := self.shared_utils.mlag_switch_ids):
            return EosDesignsFactsProtocol.MlagSwitchIds()

        return EosDesignsFactsProtocol.MlagSwitchIds(primary=mlag_switch_ids["primary"], secondary=mlag_switch_ids["secondary"])
