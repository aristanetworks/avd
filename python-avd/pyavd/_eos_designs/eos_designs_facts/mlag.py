# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.eos_designs_facts.schema import EosDesignsFactsProtocol
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import remove_cached_property_type
from pyavd.j2filters import natural_sort

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
        """
        Set this device as mlag_peer in the facts of the mlag_peer.

        Also verifies that exactly two devices are part of the same mlag_group.
        """
        if not self.shared_utils.mlag:
            return None

        if self.shared_utils.node_group_is_primary_and_peer_hostname:
            return self.shared_utils.node_group_is_primary_and_peer_hostname[1]

        if self.shared_utils.device_config and (mlag_group := self.shared_utils.device_config.mlag_group):
            mlag_group_members = self._mlag_groups[mlag_group]
            if (length := len(mlag_group_members)) != 2:
                msg = (
                    f"When trying to establish the MLAG pair, we found {length} members {natural_sort(mlag_group_members)} "
                    f"of the 'mlag_group: \"{mlag_group}\"'. There should be exactly two members of the group to form an MLAG pair."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            return next(iter(mlag_group_members.difference([self.shared_utils.hostname])))

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
        """
        if not (mlag_switch_ids := self.shared_utils.mlag_switch_ids):
            return EosDesignsFactsProtocol.MlagSwitchIds()

        return EosDesignsFactsProtocol.MlagSwitchIds(primary=mlag_switch_ids["primary"], secondary=mlag_switch_ids["secondary"])

    @remove_cached_property_type
    @cached_property
    def mlag_underlay_multicast(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.MlagUnderlayMulticast:
        """
        Exposed in avd_switch_facts.

        Returns the switch MLAG enabled protocol for Underlay Multicast
        """
        return EosDesignsFactsProtocol.MlagUnderlayMulticast(
            pim_sm=self.shared_utils.underlay_multicast_pim_mlag_enabled,
            static=self.shared_utils.underlay_multicast_static_mlag_enabled,
        )
