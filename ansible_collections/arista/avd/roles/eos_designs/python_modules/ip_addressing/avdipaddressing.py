# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import ipaddress
from collections import ChainMap

from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get_ip_from_pool

from .utils import UtilsMixin


class AvdIpAddressing(AvdFacts, UtilsMixin):
    """
    Class used to render IP addresses either from custom Jinja2 templates or using default Python Logic

    Since some templates might contain certain legacy variables (switch_*),
    those are mapped from the switch.* model

    This class is imported adhoc based on the variable `templates.ip_addressing.python_module` so it can
    be overridden by a custom python class.
    """

    def _ip(self, pool: str, prefixlen: int, subnet_offset: int, ip_offset: int) -> str:
        """
        Shortcut to get_ip_from_pool in case any custom subclasses are using this
        """
        return get_ip_from_pool(pool, prefixlen, subnet_offset, ip_offset)

    def _template(self, template_path, **kwargs):
        template_vars = ChainMap(kwargs, self._hostvars)
        return self.shared_utils.template_var(template_path, template_vars)

    def _mlag_ip(self, pool: str, ip_offset: int) -> str:
        """
        Different addressing algorithms:
            - first_id: offset from pool is `(mlag_primary_id - 1) * 2`
            - odd_id: offset from pool is `(odd_id - 1) * 2`. Requires MLAG pair to have a node with odd and a node with an even ID
            - same_subnet: offset from pool is always 0. All MLAG pairs will be the same /31. Requires pool to be a /31
        """
        if self._fabric_ipaddress_mlag_algorithm == "odd_id":
            offset = self._mlag_odd_id_based_offset
            return get_ip_from_pool(pool, 31, offset, ip_offset)

        if self._fabric_ipaddress_mlag_algorithm == "same_subnet":
            pool_network = ipaddress.ip_network(pool, strict=False)
            if pool_network.prefixlen != 31:
                raise AristaAvdError("MLAG same_subnet addressing requires the pool to be a /31")
            return get_ip_from_pool(pool, 31, 0, ip_offset)

        # Use default first_id
        offset = self._mlag_primary_id - 1
        return get_ip_from_pool(pool, 31, offset, ip_offset)

    def mlag_ibgp_peering_ip_primary(self, mlag_ibgp_peering_ipv4_pool: str) -> str:
        """
        Return IP for L3 Peerings in VRFs for MLAG Primary
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_ibgp_peering_ip_primary"):
            return self._template(
                template_path,
                vrf={"mlag_ibgp_peering_ipv4_pool": mlag_ibgp_peering_ipv4_pool},
            )

        return self._mlag_ip(mlag_ibgp_peering_ipv4_pool, 0)

    def mlag_ibgp_peering_ip_secondary(self, mlag_ibgp_peering_ipv4_pool: str) -> str:
        """
        Return IP for L3 Peerings in VRFs for MLAG Secondary
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_ibgp_peering_ip_secondary"):
            return self._template(
                template_path,
                vrf={"mlag_ibgp_peering_ipv4_pool": mlag_ibgp_peering_ipv4_pool},
            )

        return self._mlag_ip(mlag_ibgp_peering_ipv4_pool, 1)

    def mlag_ip_primary(self) -> str:
        """
        Return IP for MLAG Primary

        Default pool is "mlag_peer_ipv4_pool"
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_ip_primary"):
            return self._template(
                template_path,
                mlag_primary_id=self._mlag_primary_id,
                mlag_secondary_id=self._mlag_secondary_id,
                switch_data={"combined": {"mlag_peer_ipv4_pool": self._mlag_peer_ipv4_pool}},
            )

        return self._mlag_ip(self._mlag_peer_ipv4_pool, 0)

    def mlag_ip_secondary(self) -> str:
        """
        Return IP for MLAG Secondary

        Default pool is "mlag_peer_ipv4_pool"
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_ip_secondary"):
            return self._template(
                template_path,
                mlag_primary_id=self._mlag_primary_id,
                mlag_secondary_id=self._mlag_secondary_id,
                switch_data={"combined": {"mlag_peer_ipv4_pool": self._mlag_peer_ipv4_pool}},
            )

        return self._mlag_ip(self._mlag_peer_ipv4_pool, 1)

    def mlag_l3_ip_primary(self) -> str:
        """
        Return IP for L3 Peerings for MLAG Primary

        Default pool is "mlag_peer_l3_ipv4_pool"
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_l3_ip_primary"):
            return self._template(
                template_path,
                mlag_primary_id=self._mlag_primary_id,
                mlag_secondary_id=self._mlag_secondary_id,
                switch_data={"combined": {"mlag_peer_l3_ipv4_pool": self._mlag_peer_l3_ipv4_pool}},
            )

        return self._mlag_ip(self._mlag_peer_l3_ipv4_pool, 0)

    def mlag_l3_ip_secondary(self) -> str:
        """
        Return IP for L3 Peerings for MLAG Secondary

        Default pool is "mlag_peer_l3_ipv4_pool"
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("mlag_l3_ip_secondary"):
            return self._template(
                template_path,
                mlag_primary_id=self._mlag_primary_id,
                mlag_secondary_id=self._mlag_secondary_id,
                switch_data={"combined": {"mlag_peer_l3_ipv4_pool": self._mlag_peer_l3_ipv4_pool}},
            )

        return self._mlag_ip(self._mlag_peer_l3_ipv4_pool, 1)

    def p2p_uplinks_ip(self, uplink_switch_index: int) -> str:
        """
        Return Child IP for P2P Uplinks

        Default pool is "uplink_ipv4_pool"
        Default offset from pool is `((id - 1) * 2 * max_uplink_switches * max_parallel_uplinks) + (uplink_switch_index * 2) + 1`
        """
        uplink_switch_index = int(uplink_switch_index)
        if template_path := self.shared_utils.ip_addressing_templates.get("p2p_uplinks_ip"):
            return self._template(
                template_path,
                uplink_switch_index=uplink_switch_index,
            )

        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index
        return get_ip_from_pool(self._uplink_ipv4_pool, 31, offset, 1)

    def p2p_uplinks_peer_ip(self, uplink_switch_index: int) -> str:
        """
        Return Parent IP for P2P Uplinks

        Default pool is "uplink_ipv4_pool"
        Default offset from pool is `((id - 1) * 2 * max_uplink_switches * max_parallel_uplinks) + (uplink_switch_index * 2)`
        """
        uplink_switch_index = int(uplink_switch_index)
        if template_path := self.shared_utils.ip_addressing_templates.get("p2p_uplinks_peer_ip"):
            return self._template(
                template_path,
                uplink_switch_index=uplink_switch_index,
            )

        offset = ((self._id - 1) * self._max_uplink_switches * self._max_parallel_uplinks) + uplink_switch_index
        return get_ip_from_pool(self._uplink_ipv4_pool, 31, offset, 0)

    def router_id(self) -> str:
        """
        Return IP address for Router ID

        Default pool is "loopback_ipv4_pool"
        Default offset from pool is `id + loopback_ipv4_offset`
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("router_id"):
            return self._template(
                template_path,
                switch_id=self._id,
                loopback_ipv4_pool=self._loopback_ipv4_pool,
                loopback_ipv4_offset=self._loopback_ipv4_offset,
            )

        offset = self._id + self._loopback_ipv4_offset
        return get_ip_from_pool(self._loopback_ipv4_pool, 32, offset, 0)

    def ipv6_router_id(self) -> str:
        """
        Return IPv6 address for Router ID

        Default pool is "loopback_ipv6_pool"
        Default offset from pool is `id + loopback_ipv6_offset`
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("ipv6_router_id"):
            return self._template(
                template_path,
                switch_id=self._id,
                loopback_ipv6_pool=self._loopback_ipv6_pool,
                loopback_ipv6_offset=self._loopback_ipv6_offset,
            )

        offset = self._id + self._loopback_ipv6_offset
        return get_ip_from_pool(self._loopback_ipv6_pool, 128, offset, 0)

    def vtep_ip_mlag(self) -> str:
        """
        Return IP address for VTEP for MLAG Leaf

        Default pool is "vtep_loopback_ipv4_pool"
        Default offset from pool is `mlag_primary_id + loopback_ipv4_offset`
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("vtep_ip_mlag"):
            return self._template(
                template_path,
                switch_id=self._id,
                switch_vtep_loopback_ipv4_pool=self._vtep_loopback_ipv4_pool,
                loopback_ipv4_offset=self._loopback_ipv4_offset,
                mlag_primary_id=self._mlag_primary_id,
                mlag_secondary_id=self._mlag_secondary_id,
            )

        offset = self._mlag_primary_id + self._loopback_ipv4_offset
        return get_ip_from_pool(self._vtep_loopback_ipv4_pool, 32, offset, 0)

    def vtep_ip(self) -> str:
        """
        Return IP address for VTEP for MLAG Leaf

        Default pool is "vtep_loopback_ipv4_pool"
        Default offset from pool is `id + loopback_ipv4_offset`
        """
        if template_path := self.shared_utils.ip_addressing_templates.get("vtep_ip"):
            return self._template(
                template_path,
                switch_id=self._id,
                switch_vtep_loopback_ipv4_pool=self._vtep_loopback_ipv4_pool,
                loopback_ipv4_offset=self._loopback_ipv4_offset,
            )

        offset = self._id + self._loopback_ipv4_offset
        return get_ip_from_pool(self._vtep_loopback_ipv4_pool, 32, offset, 0)

    def vrf_loopback_ip(self, pool: str) -> str:
        """
        Return IP address for a Loopback interface based on the given pool.
        Default offset from pool is `id + loopback_ipv4_offset`

        Used for "vtep_diagnostic.loopback".
        """
        offset = self.shared_utils.id + self.shared_utils.loopback_ipv4_offset
        return get_ip_from_pool(pool, 32, offset, 0)

    def evpn_underlay_l3_multicast_group(
        self,
        underlay_l3_multicast_group_ipv4_pool: str,
        vrf_vni: int,
        vrf_id: int,
        evpn_underlay_l3_multicast_group_ipv4_pool_offset: int,
    ) -> str:
        """
        Return IP address to be used for EVPN underlay L3 multicast group

        TODO: Change algorithm to use VRF ID instead of VRF VNI as offset.
        """
        offset = vrf_vni - 1 + evpn_underlay_l3_multicast_group_ipv4_pool_offset
        return get_ip_from_pool(underlay_l3_multicast_group_ipv4_pool, 32, offset, 0)

    def evpn_underlay_l2_multicast_group(
        self,
        underlay_l2_multicast_group_ipv4_pool: str,
        vlan_id: int,
        underlay_l2_multicast_group_ipv4_pool_offset: int,
    ) -> str:
        """
        Return IP address to be used for EVPN underlay L2 multicast group
        """
        offset = vlan_id - 1 + underlay_l2_multicast_group_ipv4_pool_offset
        return get_ip_from_pool(underlay_l2_multicast_group_ipv4_pool, 32, offset, 0)
