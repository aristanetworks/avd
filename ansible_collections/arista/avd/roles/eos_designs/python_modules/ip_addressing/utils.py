from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from ansible_collections.arista.avd.plugins.plugin_utils.eos_designs_shared_utils import SharedUtils


class UtilsMixin:
    """
    Mixin Class with internal functions.
    Class should only be used as Mixin to an AvdIpAddressing class
    """

    _hostvars: dict
    shared_utils: SharedUtils

    @cached_property
    def _mlag_primary_id(self) -> int:
        return int(get(self._hostvars, "switch.mlag_switch_ids.primary", required=True))

    @cached_property
    def _mlag_secondary_id(self) -> int:
        return int(get(self._hostvars, "switch.mlag_switch_ids.secondary", required=True))

    @cached_property
    def _mlag_peer_ipv4_pool(self) -> str:
        return self.shared_utils.mlag_peer_ipv4_pool

    @cached_property
    def _mlag_peer_l3_ipv4_pool(self) -> str:
        return self.shared_utils.mlag_peer_l3_ipv4_pool

    @cached_property
    def _uplink_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.uplink_ipv4_pool", required=True)

    @cached_property
    def _id(self) -> int:
        return int(get(self._hostvars, "switch.id", required=True))

    @cached_property
    def _max_uplink_switches(self) -> int:
        return int(get(self._hostvars, "switch.max_uplink_switches", required=True))

    @cached_property
    def _max_parallel_uplinks(self) -> int:
        return int(get(self._hostvars, "switch.max_parallel_uplinks", required=True))

    @cached_property
    def _loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.loopback_ipv4_pool", required=True)

    @cached_property
    def _loopback_ipv4_offset(self) -> int:
        return self.shared_utils.loopback_ipv4_offset

    @cached_property
    def _loopback_ipv6_pool(self) -> str:
        return self.shared_utils.loopback_ipv6_pool

    @cached_property
    def _loopback_ipv6_offset(self) -> int:
        return self.shared_utils.loopback_ipv6_offset

    @cached_property
    def _vtep_loopback_ipv4_pool(self) -> str:
        return get(self._hostvars, "switch.vtep_loopback_ipv4_pool", required=True)
