# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdMissingVariableError
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from typing import Literal

    from . import SharedUtilsProtocol


class MlagMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag(self: SharedUtilsProtocol) -> bool:
        return bool(self.switch_facts.mlag_peer)

    @cached_property
    def group(self: SharedUtilsProtocol) -> str | None:
        """Group set to "node_group" name or None."""
        if self.node_group_config is not None:
            return self.node_group_config.group
        if self.device_config is not None:
            return self.device_config.mlag_group
        return None

    @cached_property
    def mlag_interfaces(self: SharedUtilsProtocol) -> list[str]:
        return range_expand(self.node_config.mlag_interfaces or self.cv_topology_config.mlag_interfaces or self.default_interfaces.mlag_interfaces)

    @cached_property
    def mlag_peer_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_ipv4_pool:
            msg = "mlag_peer_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv4_pool

    @cached_property
    def mlag_peer_ipv6_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_ipv6_pool:
            msg = "mlag_peer_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_ipv6_pool

    @cached_property
    def mlag_peer_l3_ipv4_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_l3_ipv4_pool:
            msg = "mlag_peer_l3_ipv4_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_l3_ipv4_pool

    @cached_property
    def mlag_peer_l3_ipv6_pool(self: SharedUtilsProtocol) -> str:
        if not self.node_config.mlag_peer_l3_ipv6_pool:
            msg = "mlag_peer_l3_ipv6_pool"
            raise AristaAvdMissingVariableError(msg)
        return self.node_config.mlag_peer_l3_ipv6_pool

    @cached_property
    def mlag_role(self: SharedUtilsProtocol) -> Literal["primary", "secondary"] | None:
        if not self.mlag or (is_primary := self.switch_facts.mlag_primary) is None:
            return None

        return "primary" if is_primary else "secondary"

    @cached_property
    def mlag_peer(self: SharedUtilsProtocol) -> str:
        if self.switch_facts.mlag_peer:
            return self.switch_facts.mlag_peer

        msg = "Unable to find MLAG peer within same node group. 'shared_utils.mlag_peer' should not be called unless MLAG is configured."
        raise NotImplementedError(msg)

    @cached_property
    def mlag_l3(self: SharedUtilsProtocol) -> bool:
        return self.mlag and self.switch_facts.mlag.local.mlag_l3_enabled

    @cached_property
    def mlag_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.switch_facts.mlag.local.mlag_l3_ip is not None:
            return self.switch_facts.mlag.local.mlag_l3_ip

        return self.switch_facts.mlag.local.mlag_ip

    @cached_property
    def mlag_peer_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.switch_facts.mlag.peer.mlag_l3_ip is not None:
            return self.switch_facts.mlag.peer.mlag_l3_ip

        return self.switch_facts.mlag.peer.mlag_ip

    @cached_property
    def use_separate_peer_group_for_mlag_vrfs(self: SharedUtilsProtocol) -> bool:
        return bool(
            self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer
            and self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer.name != self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name
        )

    @cached_property
    def mlag_vrfs_peer_group_name(self: SharedUtilsProtocol) -> str:
        if self.use_separate_peer_group_for_mlag_vrfs:
            return self.inputs.bgp_peer_groups.mlag_ipv4_vrfs_peer.name
        return self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name

    @cached_property
    def underlay_multicast_pim_mlag_enabled(self: SharedUtilsProtocol) -> bool:
        """
        Return whether PIM should be enabled on MLAG L3 interface.

        Requires PIM SM to be enabled on the router.
        """
        if self.underlay_multicast_pim_sm_enabled:
            return self.node_config.underlay_multicast.pim_sm.mlag
        return False

    @cached_property
    def underlay_multicast_static_mlag_enabled(self: SharedUtilsProtocol) -> bool:
        """
        Return whether static multicast should be enabled on MLAG L3 interface.

        Requires static multicast to be enabled on the router.
        """
        if self.underlay_multicast_static_enabled:
            return self.node_config.underlay_multicast.static.mlag
        return False
