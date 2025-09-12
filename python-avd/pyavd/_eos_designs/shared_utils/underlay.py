# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default
from pyavd._utils.password_utils.password import isis_encrypt

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class UnderlayMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_bgp(self: SharedUtilsProtocol) -> bool:
        return self.bgp and self.underlay_routing_protocol == "ebgp" and self.underlay_router and self.uplink_type in ["p2p", "p2p-vrfs"]

    @cached_property
    def underlay_mpls(self: SharedUtilsProtocol) -> bool:
        return (
            self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.mpls_lsr
            and self.underlay_router
            and self.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ldp(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["ospf", "ospf-ldp"] and self.underlay_router and self.uplink_type in ["p2p", "p2p-vrfs"]

    @cached_property
    def underlay_isis(self: SharedUtilsProtocol) -> bool:
        return (
            self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"]
            and self.underlay_router
            and self.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ipv6(self: SharedUtilsProtocol) -> bool:
        return self.inputs.underlay_ipv6 and self.underlay_router

    @cached_property
    def underlay_multicast_pim_sm_enabled(self: SharedUtilsProtocol) -> bool:
        # TODO: AVD 6.0, remove legacy underlay_multicast
        return (
            default(self.node_config.underlay_multicast.pim_sm.enabled, self.inputs.underlay_multicast_pim_sm, self.inputs.underlay_multicast)
            and self.underlay_router
        )

    @cached_property
    def underlay_multicast_static_enabled(self: SharedUtilsProtocol) -> bool:
        return (default(self.node_config.underlay_multicast.static.enabled, self.inputs.underlay_multicast_static)) and self.underlay_router

    @cached_property
    def any_multicast_enabled(self: SharedUtilsProtocol) -> bool:
        return self.underlay_multicast_pim_sm_enabled or self.underlay_multicast_static_enabled

    @cached_property
    def underlay_multicast_rp_interfaces(self: SharedUtilsProtocol) -> list[EosCliConfigGen.LoopbackInterfacesItem] | None:
        if not self.underlay_multicast_pim_sm_enabled or not self.inputs.underlay_multicast_rps:
            return None

        underlay_multicast_rp_interfaces = []
        for rp_entry in self.inputs.underlay_multicast_rps:
            if self.hostname not in rp_entry.nodes:
                continue

            underlay_multicast_rp_interfaces.append(
                EosCliConfigGen.LoopbackInterfacesItem(
                    name=f"Loopback{rp_entry.nodes[self.hostname].loopback_number}",
                    description=rp_entry.nodes[self.hostname].description,
                    ip_address=f"{rp_entry.rp}/32",
                )
            )

        if underlay_multicast_rp_interfaces:
            return underlay_multicast_rp_interfaces

        return None

    @cached_property
    def underlay_ipv6_numbered(self: SharedUtilsProtocol) -> bool:
        if self.inputs.underlay_ipv6_numbered:
            if self.is_wan_router:
                msg = "Invalid combination of inputs. WAN is not yet supported with IPv6 underlay"
                raise AristaAvdInvalidInputsError(msg)
            if self.underlay_multicast_rp_interfaces or self.underlay_multicast_static_enabled:
                msg = "Invalid combination of inputs. Underlay multicast is not yet supported with IPv6 underlay"
                raise AristaAvdInvalidInputsError(msg)
            if self.inputs.underlay_rfc5549:
                msg = "Invalid combination of inputs. RFC5549 is not supported with numbered IPv6 underlay"
                raise AristaAvdInvalidInputsError(msg)
            if self.inputs.vtep_vvtep_ip:
                msg = "Invalid combination of inputs. vtep_vvtep_ip is not supported with numbered IPv6 underlay"
                raise AristaAvdInvalidInputsError(msg)
            if self.node_config.inband_ztp:
                msg = "Invalid combination of inputs. inband_ztp is not supported with numbered IPv6 underlay"
                raise AristaAvdInvalidInputsError(msg)
            if self.inputs.underlay_routing_protocol not in (None, "ebgp"):
                msg = (
                    f"Invalid combination of inputs. {self.inputs.underlay_routing_protocol} is not supported with numbered IPv6 underlay. "
                    "underlay_routing_protocol must be set to 'ebgp'"
                )
                raise AristaAvdInvalidInputsError(msg)
        return self.inputs.underlay_ipv6_numbered

    @cached_property
    def underlay_isis_authentication_key(self: SharedUtilsProtocol) -> str | None:
        """
        Retrieves the ISIS authentication key configuration.

        Returns:
            str or None: The 'underlay_isis_authentication_key' if defined,
                or the encrypted (type-7) 'underlay_isis_authentication_cleartext_key'.
                Returns None if neither key is defined.
        """
        if self.inputs.underlay_isis_authentication_key is not None:
            return self.inputs.underlay_isis_authentication_key

        if self.inputs.underlay_isis_authentication_cleartext_key is None:
            return None

        return isis_encrypt(
            password=self.inputs.underlay_isis_authentication_cleartext_key,
            mode=self.inputs.underlay_isis_authentication_mode or "none",
            key=cast("str", self.isis_instance_name),
        )
