# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class NodeTypeMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def type(self: SharedUtils) -> str:
        """
        type fact set based on type variable
        """
        if (node_type := get(self.hostvars, "type")) is not None:
            return node_type
        elif self.default_node_type:
            return self.default_node_type

        raise AristaAvdMissingVariableError(f"'type' for host {self.hostname}")

    @cached_property
    def default_node_type(self: SharedUtils) -> str:
        """
        default_node_type set based on hostname, returning
        first node type matching a regex in default_node_types
        """
        default_node_types = get(self.hostvars, "default_node_types", default=[])

        for default_node_type in default_node_types:
            for hostname_regex in default_node_type["match_hostnames"]:
                if search(f"^{hostname_regex}$", self.hostname):
                    return default_node_type["node_type"]

        return None

    @cached_property
    def connected_endpoints(self: SharedUtils) -> bool:
        """
        connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints
        """
        return get(self.node_type_key_data, "connected_endpoints", default=False)

    @cached_property
    def underlay_router(self: SharedUtils) -> bool:
        """
        underlay_router set based on
        node_type_keys.<node_type_key>.underlay_router
        """
        return get(self.node_type_key_data, "underlay_router", default=True)

    @cached_property
    def uplink_type(self: SharedUtils) -> str:
        """
        uplink_type set based on
        node_type_keys.<node_type_key>.uplink_type
        """
        return get(self.node_type_key_data, "uplink_type", default="p2p")

    @cached_property
    def network_services_l1(self: SharedUtils) -> bool:
        """
        network_services_l1 set based on
        node_type_keys.<node_type_key>.network_services.l1
        """
        return get(self.node_type_key_data, "network_services.l1", default=False)

    @cached_property
    def network_services_l2(self: SharedUtils) -> bool:
        """
        network_services_l2 set based on
        node_type_keys.<node_type_key>.network_services.l2
        """
        return get(self.node_type_key_data, "network_services.l2", default=False)

    @cached_property
    def network_services_l3(self: SharedUtils) -> bool:
        """
        network_services_l3 set based on
        node_type_keys.<node_type_key>.network_services.l3 and
        <node_type_key>.<defaults | node_groups.<> | nodes.<> >.evpn_services_l2_only
        """
        if self.vtep is True:
            # network_services_l3 override based on evpn_services_l2_only
            if get(self.switch_data_combined, "evpn_services_l2_only") is True:
                return False
        return get(self.node_type_key_data, "network_services.l3", default=False)

    @cached_property
    def any_network_services(self: SharedUtils) -> bool:
        """
        Returns True if either L1, L2 or L3 network_services are enabled
        """
        return self.network_services_l1 is True or self.network_services_l2 is True or self.network_services_l3 is True

    @cached_property
    def mpls_lsr(self: SharedUtils) -> bool:
        """
        mpls_lsr set based on
        node_type_keys.<node_type_key>.mpls_lsr
        """
        return get(self.node_type_key_data, "mpls_lsr", default=False)

    @cached_property
    def vtep(self: SharedUtils) -> bool:
        """
        vtep set based on
        <node_type_key>.nodes.[].vtep and
        node_type_keys.<node_type_key>.vtep
        """
        default_vtep = get(self.node_type_key_data, "vtep")
        return get(self.switch_data_combined, "vtep", default=default_vtep) is True
