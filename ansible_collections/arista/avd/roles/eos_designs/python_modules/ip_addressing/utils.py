# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors.errors import AristaAvdError, AristaAvdMissingVariableError

if TYPE_CHECKING:
    from .avdipaddressing import AvdIpAddressing


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to an AvdIpAddressing class
    """

    @cached_property
    def _mlag_primary_id(self: "AvdIpAddressing") -> int:
        if self.shared_utils.mlag_switch_ids is None or self.shared_utils.mlag_switch_ids.get("primary") is None:
            raise AristaAvdMissingVariableError("'mlag_switch_ids' is required to calculate MLAG IP addresses")
        return self.shared_utils.mlag_switch_ids["primary"]

    @cached_property
    def _mlag_secondary_id(self: "AvdIpAddressing") -> int:
        if self.shared_utils.mlag_switch_ids is None or self.shared_utils.mlag_switch_ids.get("secondary") is None:
            raise AristaAvdMissingVariableError("'mlag_switch_ids' is required to calculate MLAG IP addresses")
        return self.shared_utils.mlag_switch_ids["secondary"]

    @cached_property
    def _fabric_ipaddress_mlag_algorithm(self: "AvdIpAddressing") -> str:
        return self.shared_utils.fabric_ip_addressing_mlag_algorithm

    @cached_property
    def _mlag_peer_ipv4_pool(self: "AvdIpAddressing") -> str:
        return self.shared_utils.mlag_peer_ipv4_pool

    @cached_property
    def _mlag_peer_l3_ipv4_pool(self: "AvdIpAddressing") -> str:
        return self.shared_utils.mlag_peer_l3_ipv4_pool

    @cached_property
    def _uplink_ipv4_pool(self: "AvdIpAddressing") -> str:
        if self.shared_utils.uplink_ipv4_pool is None:
            raise AristaAvdMissingVariableError("'uplink_ipv4_pool' is required to calculate uplink IP addresses")
        return self.shared_utils.uplink_ipv4_pool

    @cached_property
    def _id(self: "AvdIpAddressing") -> int:
        if self.shared_utils.id is None:
            raise AristaAvdMissingVariableError("'id' is required to calculate IP addresses")
        return self.shared_utils.id

    @cached_property
    def _max_uplink_switches(self: "AvdIpAddressing") -> int:
        return self.shared_utils.max_uplink_switches

    @cached_property
    def _max_parallel_uplinks(self: "AvdIpAddressing") -> int:
        return self.shared_utils.max_parallel_uplinks

    @cached_property
    def _loopback_ipv4_pool(self: "AvdIpAddressing") -> str:
        return self.shared_utils.loopback_ipv4_pool

    @cached_property
    def _loopback_ipv4_offset(self: "AvdIpAddressing") -> int:
        return self.shared_utils.loopback_ipv4_offset

    @cached_property
    def _loopback_ipv6_pool(self: "AvdIpAddressing") -> str:
        return self.shared_utils.loopback_ipv6_pool

    @cached_property
    def _loopback_ipv6_offset(self: "AvdIpAddressing") -> int:
        return self.shared_utils.loopback_ipv6_offset

    @cached_property
    def _vtep_loopback_ipv4_pool(self: "AvdIpAddressing") -> str:
        return self.shared_utils.vtep_loopback_ipv4_pool

    @cached_property
    def _mlag_odd_id_based_offset(self: "AvdIpAddressing") -> int:
        """
        Return the subnet offset for an MLAG pair based on odd id

        Requires a pair of odd and even IDs
        """

        # Verify a mix of odd and even IDs
        if (self._mlag_primary_id % 2) == (self._mlag_secondary_id % 2):
            raise AristaAvdError("MLAG compact addressing mode requires all MLAG pairs to have a single odd and even ID")

        odd_id = self._mlag_primary_id
        if odd_id % 2 == 0:
            odd_id = self._mlag_secondary_id

        return int((odd_id - 1) / 2)
