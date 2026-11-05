# Copyright (c) 2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils.password_utils.password import bgp_decrypt, bgp_encrypt

if TYPE_CHECKING:
    from . import SharedUtilsProtocol

MSG_PREFIX = "Invalid combination of inputs."


class UnderlayIbgpMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.

    'underlay_ibgp' can be used while generating facts.
    'validate_underlay_ibgp' reads the facts of this device and its downlink switches, so it must only be used while generating structured config.
    The route reflector groups and cluster IDs are validated per device while generating facts, in 'eos_designs_facts.underlay_ibgp'.
    """

    @cached_property
    def underlay_ibgp(self: SharedUtilsProtocol) -> bool:
        """Is this an underlay router running 'underlay_routing_protocol: ibgp'."""
        return self.underlay_router and self.underlay_routing_protocol == "ibgp"

    def validate_underlay_ibgp(self: SharedUtilsProtocol) -> None:
        """
        Raise if the inputs of this node are not supported with 'underlay_routing_protocol: ibgp'.

        Does nothing if this node is not an iBGP underlay router.
        Must only be called while generating structured config.
        """
        if not self.underlay_ibgp:
            return

        if self.inputs.underlay_rfc5549 is not True:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'underlay_rfc5549: true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.underlay_ipv6 or self.inputs.underlay_ipv6_numbered:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support 'underlay_ipv6' or 'underlay_ipv6_numbered'; set them to false."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.overlay_routing_protocol != "none":
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'overlay_routing_protocol: none', but got '{self.overlay_routing_protocol}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.uplink_type != "p2p":
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' requires 'uplink_type: p2p', but got '{self.uplink_type}'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.mpls_lsr:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported on node types with 'mpls_lsr: true'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.mlag:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported with MLAG; set 'mlag: false'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.is_wan_router:
            msg = f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' is not supported on WAN routers; remove 'wan_role'."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.l3_bgp_neighbors:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support BGP peers on 'l3_interfaces' or 'l3_port_channels'; "
                "remove their 'bgp' settings."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        for tenant in self.filtered_tenants:
            if tenant.vrfs or tenant.l2vlans:
                msg = (
                    f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support network services, but tenant '{tenant.name}' has VRFs or L2 VLANs "
                    "on this node; remove them or exclude the tenant with 'filter.tenants'."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if (
            self.configure_inband_mgmt
            or self.configure_inband_mgmt_ipv6
            or self.node_config.inband_ztp
            # Inband management of downlink switches.
            or self.inband_management_parent_vlans
        ):
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support inband management or 'inband_ztp'; "
                "remove the inband management settings from this node and its downlink switches."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.any_multicast_enabled:
            msg = (
                f"{MSG_PREFIX} 'underlay_routing_protocol: ibgp' does not support underlay multicast; "
                "disable 'underlay_multicast_pim_sm', 'underlay_multicast_static' and the node 'underlay_multicast' settings."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.node_config.uplink_bfd:
            msg = (
                f"{MSG_PREFIX} 'uplink_bfd: true' is not supported with 'underlay_routing_protocol: ibgp'; "
                "use 'bgp_peer_groups.ipv4_underlay_peers.bfd' instead."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.inputs.underlay_filter_peer_as:
            msg = f"{MSG_PREFIX} 'underlay_filter_peer_as: true' is not supported with 'underlay_routing_protocol: ibgp'; set it to false."
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if self.node_config.bgp_cluster_id is not None and not self.switch_facts.downlink_switches:
            msg = (
                f"{MSG_PREFIX} 'bgp_cluster_id' is set on a node without downlink switches, "
                "which is not a route reflector with 'underlay_routing_protocol: ibgp'; remove 'bgp_cluster_id'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

        if (ipv4_underlay_peers_name := self.inputs.bgp_peer_groups.ipv4_underlay_peers.name) == self.inputs.bgp_peer_groups.rr_clients_underlay_peers.name:
            msg = (
                f"{MSG_PREFIX} 'bgp_peer_groups.ipv4_underlay_peers.name' and 'bgp_peer_groups.rr_clients_underlay_peers.name' must be different "
                f"with 'underlay_routing_protocol: ibgp', but both are '{ipv4_underlay_peers_name}'."
            )
            raise AristaAvdInvalidInputsError(msg, host=self.hostname)

    @cached_property
    def underlay_ibgp_rr_clients_password(self: SharedUtilsProtocol) -> str | None:
        """
        Type 7 password of 'rr_clients_underlay_peers', derived from the password of 'ipv4_underlay_peers'.

        EOS encrypts BGP type 7 passwords with the peer group name, so the same password renders a different type 7 string on each peer group.
        """
        ipv4_underlay_peers = self.inputs.bgp_peer_groups.ipv4_underlay_peers
        if ipv4_underlay_peers.password is not None:
            try:
                cleartext_password = bgp_decrypt(ipv4_underlay_peers.password, key=ipv4_underlay_peers.name)
            except ValueError as e:
                msg = (
                    f"{MSG_PREFIX} 'bgp_peer_groups.ipv4_underlay_peers.password' must be a type 7 password encrypted with the peer group name "
                    f"'{ipv4_underlay_peers.name}', since 'underlay_routing_protocol: ibgp' encrypts it again for 'bgp_peer_groups.rr_clients_underlay_peers', "
                    "but it could not be decrypted. Use 'cleartext_password' or encrypt the password for this peer group name."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.hostname) from e
        elif (cleartext_password := ipv4_underlay_peers.cleartext_password) is None:
            return None

        return bgp_encrypt(cleartext_password, key=self.inputs.bgp_peer_groups.rr_clients_underlay_peers.name)
