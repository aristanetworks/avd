# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, merge

if TYPE_CHECKING:
    from . import SharedUtils


class SwitchDataMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def switch_data(self: SharedUtils) -> dict:
        """
        internal _switch_data containing inherited vars from fabric_topology data model.

        Vars are inherited like:
        <node_type_key>.defaults ->
            <node_type_key>.node_groups.[<node_group>] ->
                <node_type_key>.node_groups.[<node_group>].nodes.[<node>] ->
                    <node_type_key>.nodes.[<node>]

        Returns:
        -------
        dict
            node_group : dict
                Configuration set at the node_group level - including the "nodes" list.
                Empty dict if the node is not defined under a node_group.
            group : str
                Optional - Name of the matching node_group. Not set if the node is not defined under a node_group.
            combined : dict
                Combined configuration after inheritance from all levels
        """
        switch_data = {"node_group": {}}
        node_config = {}
        hostname = self.hostname

        node_type_key = self.node_type_key_data["key"]
        node_type_config = get(self.hostvars, f"{node_type_key}", required=True)
        nodes = node_type_config.get("nodes", [])

        for node in nodes:
            if hostname == node["name"]:
                node_config = node
                break
        if not node_config:
            node_groups = node_type_config.get("node_groups", [])
            for node_group in node_groups:
                nodes = node_group.get("nodes", [])
                node_group["nodes"] = nodes
                for node in nodes:
                    if hostname == node["name"]:
                        node_config = node
                        switch_data["node_group"] = node_group
                        switch_data["group"] = node_group["group"]
                        break
                if node_config:
                    break

        # Load defaults
        defaults_config = get(node_type_config, "defaults", default={})

        # Merge node data -> node_group data -> defaults into combined
        switch_data["combined"] = merge(defaults_config, switch_data["node_group"], node_config, list_merge="replace", destructive_merge=False)

        return switch_data

    @property
    def switch_data_combined(self: SharedUtils) -> dict:
        """switch_data_combined containing self._switch_data['combined'] for easier reference."""
        return self.switch_data["combined"]

    @cached_property
    def switch_data_node_group_nodes(self: SharedUtils) -> list:
        """switch_data_node_group_nodes pointing to self.switch_data['node_group']['nodes'] for easier reference."""
        return get(self.switch_data, "node_group.nodes", default=[])
