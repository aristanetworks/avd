# Copyright (c) 2023-2026 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import findall
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
    def mlag(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.Mlag:
        """
        Return facts for the MLAG peer or None if MLAG is not enabled.

        Verifies that exactly two devices are part of the same mlag_group.

        Verify that settings are compatible between the devices.
        """
        if (peer_hostname := self.mlag_peer) is None:
            return EosDesignsFactsProtocol.Mlag(enabled=False)

        if (mlag_local_info := self._mlag_local_info) is None:
            return EosDesignsFactsProtocol.Mlag(enabled=False)

        peer_facts_generator = self._mlag_peer_facts_generator

        if (peer_id := peer_facts_generator.id) is None:
            msg = f"Could not determine ID for MLAG peer '{peer_hostname}'"
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if (peer_mlag_info := peer_facts_generator._mlag_local_info) is None:
            msg = f"MLAG is not properly configured for MLAG peer '{peer_hostname}'"
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if mlag_local_info.primary == peer_mlag_info.primary or peer_facts_generator.mlag_peer != self.shared_utils.hostname:
            msg = f"MLAG is not properly configured for MLAG peer '{peer_hostname}'"
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        peer_mlag_interfaces = peer_facts_generator._mlag_interfaces
        if len(self.shared_utils.mlag_interfaces) != len(peer_mlag_interfaces):
            msg = f"Inconsistent number of 'mlag_interfaces' defined for MLAG peer '{peer_hostname}'"
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        if mlag_local_info.mlag_l3_enabled != peer_mlag_info.mlag_l3_enabled or (
            mlag_local_info.mlag_l3_enabled and (mlag_local_info.mlag_l3_vlan != peer_mlag_info.mlag_l3_vlan)
        ):
            msg = f"MLAG L3 peering is not properly configured for MLAG peer '{peer_hostname}'"
            raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

        # Override local capabilities with common capabilities
        mlag_local_info.underlay_multicast = EosDesignsFactsProtocol.Mlag.Local.UnderlayMulticast(
            pim_sm=mlag_local_info.underlay_multicast.pim_sm and peer_mlag_info.underlay_multicast.pim_sm,
            static=mlag_local_info.underlay_multicast.static and peer_mlag_info.underlay_multicast.static,
        )

        peer = EosDesignsFactsProtocol.Mlag.Peer(
            hostname=peer_hostname,
            id=peer_id,
            mlag_ip=peer_mlag_info.mlag_ip,
            port_channel_id=peer_mlag_info.port_channel_id,
            mlag_interfaces=peer_mlag_interfaces,
            mgmt_ip=peer_facts_generator.mgmt_ip,
            mlag_l3_ip=peer_mlag_info.mlag_l3_ip,
            bgp_as=peer_facts_generator.bgp_as,
            inband_ztp=peer_facts_generator.inband_ztp,
            inband_ztp_lacp_fallback_delay=peer_facts_generator.inband_ztp_lacp_fallback_delay,
            inband_ztp_vlan=peer_facts_generator.inband_ztp_vlan,
        )
        return EosDesignsFactsProtocol.Mlag(
            enabled=True,
            local=mlag_local_info,
            peer=peer,
        )

    @cached_property
    def _mlag_allowed(self: EosDesignsFactsGeneratorProtocol) -> bool:
        return self.shared_utils.node_type_key_data.mlag_support and self.shared_utils.node_config.mlag

    @cached_property
    def _mlag_is_primary_and_peer_hostname(self: EosDesignsFactsGeneratorProtocol) -> tuple[bool, str] | None:
        if primary_and_peer_hostname := self.shared_utils.node_group_is_primary_and_peer_hostname:
            return primary_and_peer_hostname

        if self.shared_utils.device_config and (mlag_group := self.shared_utils.device_config.mlag_group):
            mlag_group_members = self._mlag_groups[mlag_group]
            if (length := len(mlag_group_members)) != 2:
                msg = (
                    f"When trying to establish the MLAG pair, we found {length} members {natural_sort(mlag_group_members)} "
                    f"of the 'mlag_group: \"{mlag_group}\"'. There should be exactly two members of the group to form an MLAG pair."
                )
                raise AristaAvdInvalidInputsError(msg, host=self.shared_utils.hostname)

            is_primary = natural_sort(mlag_group_members)[0] == self.shared_utils.hostname
            peer_hostname = next(iter(mlag_group_members.difference([self.shared_utils.hostname])))
            return is_primary, peer_hostname

        return None

    @remove_cached_property_type
    @cached_property
    def mlag_peer(self: EosDesignsFactsGeneratorProtocol) -> str | None:
        """
        MLAG peer is only set when MLAG is allowed and configured with a proper peer.

        So presence of the mlag_peer fact is the same as MLAG should be configured.

        'mlag_peer' cannot be folded in to 'mlag', since it is used as a dependency in shared_utils that are indirectly used to build this.
        """
        if not self._mlag_allowed:
            return None

        if (is_primary_and_peer_hostname := self._mlag_is_primary_and_peer_hostname) is None:
            return None

        return is_primary_and_peer_hostname[1]

    @remove_cached_property_type
    @cached_property
    def mlag_primary(self: EosDesignsFactsGeneratorProtocol) -> bool | None:
        """
        MLAG priority is only set when MLAG is allowed and configured with a proper peer.

        'mlag_priority' cannot be folded in to 'mlag', since it is used as a dependency in shared_utils that are indirectly used to build this.
        """
        if not self._mlag_allowed:
            return None

        if (is_primary_and_peer_hostname := self._mlag_is_primary_and_peer_hostname) is None:
            return None

        return is_primary_and_peer_hostname[0]

    @remove_cached_property_type
    @cached_property
    def mlag_peer_id(self: EosDesignsFactsGeneratorProtocol) -> int | None:
        """
        MLAG priority is only set when MLAG is allowed and configured with a proper peer.

        'mlag_peer_id' cannot be folded in to 'mlag', since it is used as a dependency in shared_utils that are indirectly used to build this.
        """
        if not self.mlag_peer:
            return None

        return self._mlag_peer_facts_generator.id

    @cached_property
    def _mlag_local_info(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.Mlag.Local | None:
        """
        Generate the local MLAG information.

        This is also called from the MLAG peer's facts generator.
        """
        if (primary_and_peer_hostname := self._mlag_is_primary_and_peer_hostname) is None:
            return None

        is_primary = primary_and_peer_hostname[0]

        mlag_ip = self.shared_utils.ip_addressing.mlag_ip_primary() if is_primary else self.shared_utils.ip_addressing.mlag_ip_secondary()

        if self.shared_utils.underlay_router:
            mlag_l3_enabled = True
            mlag_l3_vlan = self._get_mlag_l3_vlan()
            needs_l3_ip = mlag_l3_vlan and not (self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549)
            # Only set a specific L3 IP, when there is a dedicated L3 vlan and not unnumbered.
            mlag_l3_ip = self._get_mlag_l3_ip(is_primary) if needs_l3_ip else None
        else:
            mlag_l3_enabled = False
            mlag_l3_ip = None
            mlag_l3_vlan = None

        return EosDesignsFactsProtocol.Mlag.Local(
            primary=is_primary,
            mlag_ip=mlag_ip,
            port_channel_id=self._get_mlag_port_channel_id(),
            mlag_l3_enabled=mlag_l3_enabled,
            mlag_l3_vlan=mlag_l3_vlan,
            mlag_l3_ip=mlag_l3_ip,
            underlay_multicast=EosDesignsFactsProtocol.Mlag.Local.UnderlayMulticast(
                pim_sm=self.shared_utils.underlay_multicast_pim_mlag_enabled,
                static=self.shared_utils.underlay_multicast_static_mlag_enabled,
            ),
        )

    def _get_mlag_l3_vlan(self: EosDesignsFactsGeneratorProtocol) -> int | None:
        mlag_peer_vlan = self.shared_utils.node_config.mlag_peer_vlan
        mlag_peer_l3_vlan = self.shared_utils.node_config.mlag_peer_l3_vlan
        if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
            return mlag_peer_l3_vlan

        return None

    def _get_mlag_l3_ip(self: EosDesignsFactsGeneratorProtocol, is_primary: bool) -> str:
        if self.shared_utils.underlay_ipv6_numbered:
            return self.shared_utils.ip_addressing.mlag_l3_ipv6_primary() if is_primary else self.shared_utils.ip_addressing.mlag_l3_ipv6_secondary()

        return self.shared_utils.ip_addressing.mlag_l3_ip_primary() if is_primary else self.shared_utils.ip_addressing.mlag_l3_ip_secondary()

    def _get_mlag_port_channel_id(self: EosDesignsFactsGeneratorProtocol) -> int:
        first_mlag_interface = self._mlag_interfaces[0]
        if (manual_id := self.shared_utils.node_config.mlag_port_channel_id) is not None:
            return manual_id

        return int("".join(findall(r"\d", first_mlag_interface)))

    @cached_property
    def _mlag_interfaces(self: EosDesignsFactsGeneratorProtocol) -> EosDesignsFactsProtocol.Mlag.Peer.MlagInterfaces:
        """
        Local MLAG interfaces.

        This is also called from the MLAG peer's facts generator.
        """
        if not (mlag_interfaces := self.shared_utils.mlag_interfaces):
            msg = "'mlag_interfaces' not set"
            raise AristaAvdInvalidInputsError(msg)

        return EosDesignsFactsProtocol.Mlag.Peer.MlagInterfaces(mlag_interfaces)
