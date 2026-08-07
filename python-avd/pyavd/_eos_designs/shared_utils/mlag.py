# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import findall
from typing import TYPE_CHECKING, Protocol, cast

from pyavd._errors import AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd._utils import Undefined, UndefinedType, default, get_ip_from_ip_prefix
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from typing import Literal

    from pyavd._eos_designs.eos_designs_facts.schema.protocol import EosDesignsFactsProtocol

    from . import SharedUtilsProtocol


class MlagMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def mlag(self: SharedUtilsProtocol) -> bool:
        if not self.node_type_key_data.mlag_support:
            return False

        if self.node_group_config is not None and len(self.node_group_config.nodes) > 2 and self.inputs.avd_design_future.allow_mlag_in_shared_node_groups:
            return self.node_group_mlag_is_primary_and_peer_hostname is not None

        if not self.node_config.mlag:
            return False

        # Node groups used for mlag peer.
        if self.node_group_mlag_is_primary_and_peer_hostname:
            return True

        # devices[].mlag_group used for mlag peer.
        return bool(self.device_config and self.device_config.mlag_group)

    @cached_property
    def node_group_mlag_is_primary_and_peer_hostname(self: SharedUtilsProtocol) -> tuple[bool, str] | None:
        """
        Node group position and peer used for MLAG.

        Returns None if the device should not use a node_group peer for MLAG.
        Returns True, <peer> if this device is the first MLAG node in node_group.
        Returns False, <peer> if this device is the second MLAG node in node_group.
        """
        if self.node_group_config is None:
            return None

        if len(self.node_group_config.nodes) == 2:
            return self.node_group_is_primary_and_peer_hostname

        if not self.inputs.avd_design_future.allow_mlag_in_shared_node_groups:
            return None

        mlag_nodes = [hostname for hostname, _ in self.node_group_config.nodes.items() if self._node_group_member_has_mlag_enabled(hostname)]

        if self.hostname not in mlag_nodes:
            return None

        if (length := len(mlag_nodes)) != 2:
            msg = (
                f"Node group '{self.node_group_config.group}' has {length} nodes with 'mlag: true' ({natural_sort(mlag_nodes)}). "
                "Exactly two MLAG-enabled nodes are supported in a shared node group when 'avd_design_future.allow_mlag_in_shared_node_groups' is true."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        index = mlag_nodes.index(self.hostname)
        peer_index = not index
        return index == 0, mlag_nodes[peer_index]

    def _node_group_member_has_mlag_enabled(self: SharedUtilsProtocol, hostname: str) -> bool:
        """Return whether the given node_group member has effective 'mlag: true' after inheritance."""
        # This condition is already checked before calling this method, it is kept here only to make pyright happy.
        if self.node_group_config is None or self.node_type_config is None:
            return False

        node_config = self.node_type_config.nodes.get(hostname, default=Undefined)
        node_mlag = None if isinstance(node_config, UndefinedType) else node_config._get("mlag")

        default_member_mlag = True
        member_mlag = default(
            node_mlag,
            self.node_group_config.nodes[hostname]._get("mlag"),
            self.node_group_config._get("mlag"),
            self.node_type_config.defaults._get("mlag"),
            default_member_mlag,
        )

        return member_mlag is True

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
        if not self.mlag:
            return None
        if self.node_group_mlag_is_primary_and_peer_hostname is not None:
            return "primary" if self.node_group_mlag_is_primary_and_peer_hostname[0] else "secondary"

        if self.switch_facts.mlag_peer:
            return "primary" if natural_sort([self.hostname, self.switch_facts.mlag_peer])[0] == self.hostname else "secondary"

        return None

    @cached_property
    def mlag_peer(self: SharedUtilsProtocol) -> str:
        if self.switch_facts.mlag_peer:
            return self.switch_facts.mlag_peer

        msg = "Unable to find MLAG peer within same node group. 'shared_utils.mlag_peer' should not be called unless MLAG is configured."
        raise NotImplementedError(msg)

    @cached_property
    def mlag_l3(self: SharedUtilsProtocol) -> bool:
        return self.mlag is True and self.underlay_router is True

    @cached_property
    def mlag_peer_l3_vlan(self: SharedUtilsProtocol) -> int | None:
        if self.mlag_l3:
            mlag_peer_vlan = self.node_config.mlag_peer_vlan
            mlag_peer_l3_vlan = self.node_config.mlag_peer_l3_vlan
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_peer_ip(self: SharedUtilsProtocol) -> str:
        return cast("str", self.mlag_peer_facts.mlag_ip)

    @cached_property
    def mlag_peer_l3_ip(self: SharedUtilsProtocol) -> str | None:
        if self.mlag_peer_l3_vlan is not None:
            return self.mlag_peer_facts.mlag_l3_ip
        return None

    @cached_property
    def mlag_peer_id(self: SharedUtilsProtocol) -> int:
        return cast("int", self.mlag_peer_facts.id)

    @cached_property
    def mlag_peer_facts(self: SharedUtilsProtocol) -> EosDesignsFactsProtocol:
        return self.get_peer_facts(self.mlag_peer)

    @cached_property
    def mlag_peer_mgmt_ip(self: SharedUtilsProtocol) -> str | None:
        if (mlag_peer_mgmt_ip := self.mlag_peer_facts.mgmt_ip) is None:
            return None

        if mlag_peer_mgmt_ip == "dhcp":
            msg = (
                f"'mgmt_ip: dhcp' is not supported for MLAG peer '{self.mlag_peer}'."
                f" MLAG dual-primary detection heartbeat requires a static management IP address."
            )
            raise AristaAvdInvalidInputsError(msg)

        return get_ip_from_ip_prefix(mlag_peer_mgmt_ip)

    @cached_property
    def mlag_ip(self: SharedUtilsProtocol) -> str | None:
        """Render ipv4 address for mlag_ip using dynamically loaded python module."""
        if self.mlag_role == "primary":
            return self.ip_addressing.mlag_ip_primary()
        if self.mlag_role == "secondary":
            return self.ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_l3_ip(self: SharedUtilsProtocol) -> str | None:
        """Render ipv4 or ipv6 address for mlag_l3_ip using dynamically loaded python module."""
        if self.mlag_peer_l3_vlan is None:
            return None
        if self.mlag_role == "primary":
            if self.underlay_ipv6_numbered:
                return self.ip_addressing.mlag_l3_ipv6_primary()
            return self.ip_addressing.mlag_l3_ip_primary()
        if self.mlag_role == "secondary":
            if self.underlay_ipv6_numbered:
                return self.ip_addressing.mlag_l3_ipv6_secondary()
            return self.ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_switch_ids(self: SharedUtilsProtocol) -> dict[str, int] | None:
        """
        Returns the switch id's of both primary and secondary switches for a given node group.

        {"primary": int, "secondary": int}.
        """
        if self.mlag_role == "primary":
            if self.id is None:
                msg = "'id' is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.id, "secondary": self.mlag_peer_id}
        if self.mlag_role == "secondary":
            if self.id is None:
                msg = "'id' is required to compute MLAG ids"
                raise AristaAvdInvalidInputsError(msg)
            return {"primary": self.mlag_peer_id, "secondary": self.id}
        return None

    @cached_property
    def mlag_port_channel_id(self: SharedUtilsProtocol) -> int:
        if not self.mlag_interfaces:
            msg = "'mlag_interfaces' not set"
            raise AristaAvdInvalidInputsError(msg)
        default_mlag_port_channel_id = int("".join(findall(r"\d", self.mlag_interfaces[0])))
        return default(self.node_config.mlag_port_channel_id, default_mlag_port_channel_id)

    @cached_property
    def mlag_peer_port_channel_id(self: SharedUtilsProtocol) -> int:
        return self.mlag_peer_facts.mlag_port_channel_id or self.mlag_port_channel_id

    @cached_property
    def mlag_peer_interfaces(self: SharedUtilsProtocol) -> list[str]:
        return list(self.mlag_peer_facts.mlag_interfaces) or self.mlag_interfaces

    @cached_property
    def mlag_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.mlag_l3_ip is not None:
            return self.mlag_l3_ip

        return cast("str", self.mlag_ip)

    @cached_property
    def mlag_peer_ibgp_ip(self: SharedUtilsProtocol) -> str:
        if self.mlag_peer_l3_ip is not None:
            return self.mlag_peer_l3_ip

        return self.mlag_peer_ip

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
