from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
import ipaddress
from functools import cached_property
from hashlib import sha256
from ansible_collections.arista.avd.plugins.module_utils.utils import AristaAvdError, get, get_item, default, template_var, AristaAvdMissingVariableError


class EosDesignsFacts:
    def __init__(
        self,
        hostvars=None,
        combine=None,
        list_compress=None,
        range_expand=None,
        convert_dicts=None,
        natural_sort=None,
        template_lookup_module=None
    ):
        if hostvars:
            self._hostvars = hostvars
        if combine:
            self._combine = combine
        if list_compress:
            self._list_compress = list_compress
        if range_expand:
            self._range_expand = range_expand
        if convert_dicts:
            self._convert_dicts = convert_dicts
        if natural_sort:
            self._natural_sort = natural_sort
        if template_lookup_module:
            self._template_lookup_module = template_lookup_module

    @classmethod
    def keys(cls):
        '''
        Return the list of "keys"

        Actually the returned list are the names of attributes not starting with "_" and using cached_property class.
        The "_" check is added to allow support for "internal" cached_properties storing temporary values.
        '''

        return [key for key in dir(cls) if not key.startswith('_') and isinstance(getattr(cls, key), cached_property)]

    @classmethod
    def internal_keys(cls):
        '''
        Return the list of "keys" starting with _

        Actually the returned list are the names of attributes starting with "_" and using cached_property class.
        The "_" check is added to only include "internal" cached_properties storing temporary values.
        '''

        return [key for key in dir(cls) if key.startswith('_') and isinstance(getattr(cls, key), cached_property)]

    def get(self, key, default_value=None):
        '''
        Emulate the builtin dict .get method
        '''
        if key in self.keys():
            return getattr(self, key)
        return default_value

    def reset(self):
        '''
        Reset the cached attribute values
        '''

        self.__dict__ = {}

    def render(self):
        '''
        Return a dictionary of all @cached_property values.

        If the value is cached, it will automatically get returned from cache
        If the value is not cached, it will be resolved by the attribute function first.
        Empty values are removed from the returned data.
        '''
        return {key: getattr(self, key) for key in self.keys() if getattr(self, key) is not None}

    '''
    ------------------------------------------------
    Example function to set a fact based on hostvars
    ------------------------------------------------
    @cached_property
    def foo(self):
        """
        "switch.foo" fact set based on "bar" data model
        """
        return get(self._hostvars, "bar.foo", default="zoo")

    -----------------------------------------------------------------------------------------------------
    Example function to set a fact based on a required key under ex "l3leaf.node_groups.<>.nodes.<>.<key>

    Notice the variable _switch_data_combined starts with _ meaning it is an internal variable which will
    not be returned as part of the facts. We can load such variables with commonly used data, leveraged
    by multiple facts functions.
    -----------------------------------------------------------------------------------------------------
    @cached_property
    def foo(self):
        """
        "switch.foo" fact set based on "<node_type_key>.*" data model

        Example l3leaf.defaults.foo -> switch.foo
        """
        return get(self._switch_data_combined, "foo", required=True)
    '''

    @cached_property
    def type(self):
        """
        switch.type fact set based on type variable
        """
        return get(self._hostvars, "type", required=True)

    @cached_property
    def hostname(self):
        """
        switch.hostname fact set based on inventory_hostname variable
        """
        return get(self._hostvars, "inventory_hostname", required=True)

    @cached_property
    def node_type_key(self):
        """
        switch.node_type_key fact set by finding a matching "type" in "node_type_keys" variable
        """
        return self._node_type_key_data['key']

    @cached_property
    def _node_type_key_data(self):
        """
        internal _node_type_key_data containing settings for this node_type.
        """
        node_type_keys = get(self._hostvars, "node_type_keys", required=True)
        node_type_keys = self._convert_dicts(node_type_keys, 'key')
        for node_type in node_type_keys:
            if node_type['type'] == self.type:
                return node_type

        # Not found
        raise AristaAvdMissingVariableError(f"node_type_keys.<>.type=={self.type}")

    @cached_property
    def connected_endpoints(self):
        """
        switch.connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints
        """
        return get(self._node_type_key_data, "connected_endpoints", default=False)

    @cached_property
    def default_downlink_interfaces(self):
        """
        internal switch.default_downlink_interfaces set based on default_interfaces
        """
        return self._range_expand(get(self.default_interfaces, "downlink_interfaces", default=[]))

    @cached_property
    def default_evpn_role(self):
        """
        switch.default_evpn_role set based on
        node_type_keys.<node_type_key>.default_evpn_role
        """
        return get(self._node_type_key_data, "default_evpn_role", default="none")

    @cached_property
    def default_interfaces(self):
        default_interfaces = get(self._hostvars, "default_interfaces", default=[])

        device_platform = default(self.platform, "default")

        # First look for a matching default interface set that matches our platform and type
        for default_interface in default_interfaces:
            for platform in default_interface.get('platforms', []):
                if (
                    re.search(f"^{platform}$", device_platform) and
                    self.type in default_interface.get('types', [])
                ):
                    return default_interface

        # If not found, then look for a default default_interface that matches our type
        for default_interface in default_interfaces:
            for platform in default_interface.get('platforms', []):
                if (
                    re.search(f"^{platform}$", "default") and
                    self.type in default_interface.get('types', [])
                ):
                    return default_interface

        return {}

    @cached_property
    def default_underlay_routing_protocol(self):
        """
        switch.default_underlay_routing_protocol set based on
        node_type_keys.<node_type_key>.default_underlay_routing_protocol
        """
        return get(self._node_type_key_data, "default_underlay_routing_protocol", default="ebgp")

    @cached_property
    def default_overlay_routing_protocol(self):
        """
        switch.default_overlay_routing_protocol set based on
        node_type_keys.<node_type_key>.default_overlay_routing_protocol
        """
        return get(self._node_type_key_data, "default_overlay_routing_protocol", default="ebgp")

    @cached_property
    def default_overlay_address_families(self):
        """
        switch.default_overlay_address_families set based on
        node_type_keys.<node_type_key>.default_overlay_address_families
        """
        return get(self._node_type_key_data, "default_overlay_address_families", default=["evpn"])

    @cached_property
    def default_mpls_overlay_role(self):
        """
        switch.default_mpls_overlay_role set based on
        node_type_keys.<node_type_key>.default_mpls_overlay_role
        """
        return get(self._node_type_key_data, "default_mpls_overlay_role", default="none")

    @cached_property
    def mpls_lsr(self):
        """
        switch.mpls_lsr set based on
        node_type_keys.<node_type_key>.mpls_lsr
        """
        return get(self._node_type_key_data, "mpls_lsr", default=False)

    @cached_property
    def mlag_support(self):
        """
        switch.mlag_support set based on
        node_type_keys.<node_type_key>.mlag_support
        """
        return get(self._node_type_key_data, "mlag_support", default=False)

    @cached_property
    def network_services_l1(self):
        """
        switch.network_services_l1 set based on
        node_type_keys.<node_type_key>.network_services.l1
        """
        return get(self._node_type_key_data, "network_services.l1", default=False)

    @cached_property
    def network_services_l2(self):
        """
        switch.network_services_l2 set based on
        node_type_keys.<node_type_key>.network_services.l2
        """
        return get(self._node_type_key_data, "network_services.l2", default=False)

    @cached_property
    def network_services_l3(self):
        """
        switch.network_services_l3 set based on
        node_type_keys.<node_type_key>.network_services.l3 and
        <node_type_key>.<defaults | node_groups.<> | nodes.<> >.evpn_services_l2_only
        """
        if self.vtep is True:
            # switch.network_services_l3 override based on evpn_services_l2_only
            if get(self._switch_data_combined, "evpn_services_l2_only") is True:
                return False
        return get(self._node_type_key_data, "network_services.l3", default=False)

    @cached_property
    def underlay_router(self):
        """
        switch.underlay_router set based on
        node_type_keys.<node_type_key>.underlay_router
        """
        return get(self._node_type_key_data, "underlay_router", default=True)

    @cached_property
    def uplink_type(self):
        """
        switch.uplink_type set based on
        node_type_keys.<node_type_key>.uplink_type
        """
        return get(self._node_type_key_data, "uplink_type", default="p2p")

    @cached_property
    def vtep(self):
        """
        switch.vtep set based on
        node_type_keys.<node_type_key>.vtep
        """
        return get(self._node_type_key_data, "vtep", default=False)

    @cached_property
    def mpls_ler(self):
        """
        switch.mpls_ler set based on
        node_type_keys.<node_type_key>.mpls_ler
        """
        return get(self._node_type_key_data, "mpls_ler", default=False)

    @cached_property
    def ip_addressing(self):
        """
        switch.ip_addressing.* set based on
        templates.ip_addressing.* combined with (overridden by)
        node_type_keys.<node_type_key>.ip_addressing.*
        """
        hostvar_templates = get(self._hostvars, "templates.ip_addressing", default={})
        node_type_templates = get(self._node_type_key_data, "ip_addressing", default={})
        if hostvar_templates or node_type_templates:
            return self._combine(hostvar_templates, node_type_templates, recursive=True, list_merge='replace')
        else:
            return {}

    @cached_property
    def interface_descriptions(self):
        """
        switch.interface_descriptions.* set based on
        templates.interface_descriptions.* combined with (overridden by)
        node_type_keys.<node_type_key>.interface_descriptions.*
        """
        hostvar_templates = get(self._hostvars, "templates.interface_descriptions", default={})
        node_type_templates = get(self._node_type_key_data, "interface_descriptions", default={})
        if hostvar_templates or node_type_templates:
            return self._combine(hostvar_templates, node_type_templates, recursive=True, list_merge='replace')
        else:
            return {}

    @cached_property
    def _template_vars(self):
        template_vars = {"ansible_search_path": self._ansible_search_path}
        custom_templates_extra_vars = get(self._node_type_key_data, "custom_templates_extra_vars", default=[])
        for extra_var in custom_templates_extra_vars:
            template_vars[extra_var] = get(self._hostvars, extra_var)
        return template_vars

    @cached_property
    def _switch_data(self):
        """
        internal _switch_data containing inherited vars from fabric_topology data model

        Vars are inherited like:
        <node_type_key>.defaults ->
            <node_type_key>.node_groups.[<node_group>] ->
                <node_type_key>.node_groups.[<node_group>].nodes.[<node>] ->
                    <node_type_key>.nodes.[<node>]

        Returns
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
        switch_data = {'node_group': {}}
        node_config = {}
        hostname = self.hostname
        node_type_config = get(self._hostvars, f"{self.node_type_key}", required=True)
        nodes = self._convert_dicts(node_type_config.get('nodes', []), 'name')

        for node in nodes:
            if hostname == node['name']:
                node_config = node
                break
        if not node_config:
            node_groups = self._convert_dicts(node_type_config.get('node_groups', []), 'group')
            for node_group in node_groups:
                nodes = self._convert_dicts(node_group.get('nodes', []), 'name')
                node_group['nodes'] = nodes
                for node in nodes:
                    if hostname == node['name']:
                        node_config = node
                        switch_data['node_group'] = node_group
                        switch_data['group'] = node_group['group']
                        break
                if node_config:
                    break

        # Load defaults
        defaults_config = node_type_config.get('defaults', {})
        # Merge node_group data on top of defaults into combined
        switch_data['combined'] = self._combine(defaults_config, switch_data['node_group'], recursive=True, list_merge='replace')
        # Merge node data on top of combined
        switch_data['combined'] = self._combine(switch_data['combined'], node_config, recursive=True, list_merge='replace')

        return switch_data

    @cached_property
    def _switch_data_combined(self):
        """
        internal _switch_data_combined pointing to
        self._switch_data['combined'] for easier reference.
        """
        return get(self._switch_data, "combined", required=True)

    @cached_property
    def _switch_data_node_group_nodes(self):
        """
        internal _switch_data_node_group_nodes pointing to
        self._switch_data['node_group']['nodes'] for easier reference.
        """
        return get(self._switch_data, "node_group.nodes", default=[])

    @cached_property
    def group(self):
        """
        switch.group set to "node_group" name or None
        """
        return get(self._switch_data, "group")

    @cached_property
    def id(self):
        return get(self._switch_data_combined, "id", required=True)

    @cached_property
    def mgmt_ip(self):
        return get(self._switch_data_combined, "mgmt_ip")

    @cached_property
    def platform(self):
        return get(self._switch_data_combined, "platform")

    @cached_property
    def max_parallel_uplinks(self):
        return get(self._switch_data_combined, "max_parallel_uplinks", default=1)

    @cached_property
    def uplink_switches(self):
        return get(self._switch_data_combined, "uplink_switches")

    @cached_property
    def uplink_interfaces(self):
        return self._range_expand(default(
            get(self._switch_data_combined, "uplink_interfaces"),
            get(self.default_interfaces, "uplink_interfaces"),
            [])
        )

    @cached_property
    def uplink_switch_interfaces(self):
        uplink_switch_interfaces = get(self._switch_data_combined, "uplink_switch_interfaces")
        if uplink_switch_interfaces is not None:
            return uplink_switch_interfaces

        if self.uplink_switches is None:
            return []

        uplink_switch_interfaces = []
        uplink_switch_counter = {}
        for uplink_switch in self.uplink_switches:
            uplink_switch_facts: EosDesignsFacts = get(self._hostvars,
                                                       f"avd_switch_facts..{uplink_switch}..switch",
                                                       required=True,
                                                       org_key=f"avd_switch_facts.({uplink_switch}).switch",
                                                       separator="..")

            # Count the number of instances the current switch was processed
            uplink_switch_counter[uplink_switch] = uplink_switch_counter.get(uplink_switch, 0) + 1
            index_of_parallel_uplinks = uplink_switch_counter[uplink_switch] - 1

            # Add uplink_switch_interface based on this switch's ID (-1 for 0-based) * max_parallel_uplinks + index_of_parallel_uplinks.
            # For max_parallel_uplinks: 2 this would assign downlink interfaces like this:
            # spine1 downlink-interface mapping: [ leaf-id1, leaf-id1, leaf-id2, leaf-id2, leaf-id3, leaf-id3, ... ]
            downlink_index = (self.id - 1) * self.max_parallel_uplinks + index_of_parallel_uplinks
            if len(uplink_switch_facts.default_downlink_interfaces) > downlink_index:
                uplink_switch_interfaces.append(uplink_switch_facts.default_downlink_interfaces[downlink_index])
            else:
                raise AristaAvdError(
                    f"'uplink_switch_interfaces' is not set on '{self.hostname}' and 'uplink_switch' '{uplink_switch}' "
                    f"does not have 'downlink_interfaces[{downlink_index}]' set under 'default_interfaces'"
                )

        return uplink_switch_interfaces

    @cached_property
    def uplink_interface_speed(self):
        return get(self._switch_data_combined, "uplink_interface_speed")

    @cached_property
    def uplink_bfd(self):
        return get(self._switch_data_combined, "uplink_bfd")

    @cached_property
    def uplink_ptp(self):
        return get(self._switch_data_combined, "uplink_ptp")

    @cached_property
    def uplink_macsec(self):
        return get(self._switch_data_combined, "uplink_macsec")

    @cached_property
    def uplink_structured_config(self):
        return get(self._switch_data_combined, "uplink_structured_config")

    @cached_property
    def short_esi(self):
        '''
        If short_esi is set to "auto" we will use sha256 to create a
        unique short_esi value based on various uplink information.
        '''
        short_esi = get(self._switch_data_combined, "short_esi")
        if short_esi == "auto":
            esi_seed_1 = ''.join(default(self.uplink_switches, [])[:2])
            esi_seed_2 = ''.join(default(self.uplink_switch_interfaces, [])[:2])
            esi_seed_3 = ''.join(default(self.uplink_interfaces, [])[:2])
            esi_seed_4 = default(self.group, '')
            esi_hash = sha256(f"{esi_seed_1}{esi_seed_2}{esi_seed_3}{esi_seed_4}".encode('utf-8')).hexdigest()
            short_esi = re.sub(r'([0-9a-f]{4})', r'\1:', esi_hash)[:14]
        return short_esi

    @cached_property
    def rack(self):
        return get(self._switch_data_combined, "rack")

    @cached_property
    def raw_eos_cli(self):
        return get(self._switch_data_combined, "raw_eos_cli")

    @cached_property
    def struct_cfg(self):
        return get(self._switch_data_combined, "structured_config")

    @cached_property
    def max_uplink_switches(self):
        """
        max_uplink_switches will default to the length of uplink_switches
        """
        return default(
            get(self._switch_data_combined, "max_uplink_switches"),
            len(get(self._switch_data_combined, "uplink_switches", default=[]))
        )

    @cached_property
    def is_deployed(self):
        return get(self._hostvars, "is_deployed", default=True)

    @cached_property
    def platform_settings(self):
        platform_settings = get(self._hostvars, "platform_settings", default=[])

        # First look for a matching platform setting specifying our platform
        for platform_setting in platform_settings:
            if self.platform in platform_setting.get('platforms', []):
                return platform_setting

        # If not found, then look for a default platform setting
        for platform_setting in platform_settings:
            if 'default' in platform_setting.get('platforms', []):
                return platform_setting

        return {}

    @cached_property
    def mgmt_interface(self):
        """
        mgmt_interface is inherited from
        Global var mgmt_interface ->
          Platform Settings management_interface ->
            Fabric Topology data model mgmt_interface
        """
        return default(
            get(self._switch_data_combined, "mgmt_interface"),
            self.platform_settings.get("management_interface"),
            get(self._hostvars, "mgmt_interface")
        )

    @cached_property
    def underlay_routing_protocol(self):
        underlay_routing_protocol = str(get(self._hostvars, "underlay_routing_protocol", default=self.default_underlay_routing_protocol)).lower()
        if underlay_routing_protocol not in ['ebgp', 'isis', 'isis-ldp', 'isis-sr', 'isis-sr-ldp', 'ospf', 'ospf-ldp', 'none']:
            underlay_routing_protocol = self.default_underlay_routing_protocol
        return underlay_routing_protocol

    @cached_property
    def overlay_routing_protocol(self):
        overlay_routing_protocol = str(get(self._hostvars, "overlay_routing_protocol", default=self.default_overlay_routing_protocol)).lower()
        if overlay_routing_protocol not in ['ebgp', 'ibgp', 'none']:
            overlay_routing_protocol = self.default_overlay_routing_protocol
        return overlay_routing_protocol

    @cached_property
    def overlay_address_families(self):
        return get(self._switch_data_combined, "overlay_address_families", default=self.default_overlay_address_families)

    @cached_property
    def link_tracking_groups(self):
        if get(self._switch_data_combined, "link_tracking.enabled") is True:
            link_tracking_groups = []
            default_recovery_delay = get(self.platform_settings, 'reload_delay.mlag', 300)
            lt_groups = get(self._switch_data_combined, "link_tracking.groups", default=[])

            if len(lt_groups) > 0:
                for lt_group in lt_groups:
                    lt_group['recovery_delay'] = lt_group.get('recovery_delay', default_recovery_delay)
                    link_tracking_groups.append(lt_group)
            else:
                link_tracking_groups.append({"name": "LT_GROUP1", "recovery_delay": default_recovery_delay})

            return link_tracking_groups

        return None

    @cached_property
    def lacp_port_id(self):
        if get(self._switch_data_combined, "lacp_port_id_range.enabled") is True:
            node_group_length = max(len(self._switch_data_node_group_nodes), 1)
            lacp_port_id = {}
            switch_id = self.id
            port_range = int(get(self._switch_data_combined, 'lacp_port_id_range.size', default=128))
            port_offset = int(get(self._switch_data_combined, 'lacp_port_id_range.offset', default=0))
            lacp_port_id['begin'] = 1 + (((switch_id - 1) % node_group_length) * port_range) + port_offset
            lacp_port_id['end'] = (((switch_id - 1) % node_group_length + 1) * port_range) + port_offset
            return lacp_port_id

        return None

    @cached_property
    def _any_network_services(self):
        '''
        Returns True if either L1, L2 or L3 network_services are enabled
        '''
        return (
            self.network_services_l1 is True
            or self.network_services_l2 is True
            or self.network_services_l3 is True
        )

    @cached_property
    def filter_tenants(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "filter.tenants", default=["all"])
        return None

    @cached_property
    def always_include_vrfs_in_tenants(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "filter.always_include_vrfs_in_tenants")
        return None

    @cached_property
    def filter_tags(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "filter.tags", default=["all"])
        return None

    @cached_property
    def filter_only_vlans_in_use(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "filter.only_vlans_in_use", default=False)
        return None

    @cached_property
    def virtual_router_mac_address(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "virtual_router_mac_address")
        return None

    @cached_property
    def enable_trunk_groups(self):
        if self._any_network_services:
            return get(self._hostvars, "enable_trunk_groups", default=False)
        return None

    @cached_property
    def only_local_vlan_trunk_groups(self):
        if self.enable_trunk_groups:
            return get(self._hostvars, "only_local_vlan_trunk_groups", default=False)
        return None

    @cached_property
    def _endpoint_vlans_and_trunk_groups(self):
        '''
        Return list of vlans and list of trunk groups used by connected_endpoints
        '''
        if not (self._any_network_services and self.connected_endpoints):
            return [], []

        vlans = []
        trunk_groups = []

        port_profiles = get(self._hostvars, "port_profiles", default=[])
        # Support legacy data model by converting nested dict to list of dict
        port_profiles = self._convert_dicts(port_profiles, "profile")

        connected_endpoints_keys = get(self._hostvars, "connected_endpoints_keys", default=[])
        # Support legacy data model by converting nested dict to list of dict
        connected_endpoints_keys = self._convert_dicts(connected_endpoints_keys, "key")
        for connected_endpoints_key in connected_endpoints_keys:
            connected_endpoints_key_key = connected_endpoints_key.get("key")
            if connected_endpoints_key_key is None or get(self._hostvars, connected_endpoints_key_key) is None:
                # Invalid connected_endpoints_key.key. Skipping.
                continue

            connected_endpoints = get(self._hostvars, connected_endpoints_key_key)
            # Support legacy data model by converting nested dict to list of dict
            connected_endpoints = self._convert_dicts(connected_endpoints, 'name')
            for connected_endpoint in connected_endpoints:
                for adapter in connected_endpoint.get("adapters", []):
                    profile_name = adapter.get("profile")
                    adapter_profile = get_item(port_profiles, "profile", profile_name, default={})
                    parent_profile_name = adapter_profile.get("parent_profile")
                    parent_profile = get_item(port_profiles, "profile", parent_profile_name, default={})

                    adapter_settings = self._combine(parent_profile, adapter_profile, adapter, recursive=True, list_merge='replace')

                    if self.hostname not in adapter_settings.get("switches", []):
                        # This switch is not connected to this endpoint. Skipping.
                        continue

                    if "vlans" in adapter_settings and adapter_settings["vlans"] not in ["all", "", None]:
                        vlans.extend(map(int, self._range_expand(str(adapter_settings["vlans"]))))
                        if adapter_settings.get("trunk_groups"):
                            trunk_groups.extend(adapter_settings["trunk_groups"])
                    elif "trunk" in adapter_settings.get("mode"):
                        if adapter_settings.get("trunk_groups"):
                            trunk_groups.extend(adapter_settings["trunk_groups"])
                        else:
                            # No vlans or trunk_groups defined, but this is a trunk, so default is all vlans allowed
                            # No need to check further, since the list is now containing all vlans.
                            # The trunk group list may not be complete, but it will not matter, since we will
                            # configure all vlans anyway.
                            return list(range(1, 4094)), trunk_groups
                    else:
                        # No vlans or mode defined so this is an access port with only vlan 1 allowed
                        vlans.append(1)

                    if "native_vlan" in adapter_settings:
                        vlans.append(int(adapter_settings["native_vlan"]))

                    if get(adapter_settings, "port_channel.subinterfaces"):
                        for subinterface in get(adapter_settings, "port_channel.subinterfaces"):
                            if "vlan_id" in subinterface:
                                vlans.append(int(subinterface["vlan_id"]))
                            elif "number" in subinterface:
                                vlans.append(int(subinterface["number"]))
        # At this point "vlans" contain the full list of vlans used by locally connected endpoints
        # Next we traverse any downstream L2 switches so ensure we can provide connectivity to any
        # vlans used by them.
        for fabric_switch in get(self._hostvars, "avd_switch_facts", default=[]):
            fabric_switch_facts: EosDesignsFacts = get(self._hostvars,
                                                       f"avd_switch_facts..{fabric_switch}..switch",
                                                       required=True,
                                                       separator="..",
                                                       org_key=f"avd_switch_facts.{fabric_switch}.switch")
            if (
                fabric_switch_facts.uplink_type == "port-channel"
                and self.hostname in fabric_switch_facts.uplink_peers
            ):
                vlans.extend(fabric_switch_facts._vlans)

        return list(set(vlans)), list(set(trunk_groups))

    @cached_property
    def endpoint_trunk_groups(self):
        '''
        Return list of trunk_groups in use by endpoints connected to this switch
        '''
        if self.only_local_vlan_trunk_groups:
            vlans_in_use, trunk_groups_in_use = self._endpoint_vlans_and_trunk_groups
            return list(set(trunk_groups_in_use))
        return []

    @cached_property
    def _vlans(self):
        '''
        Return list of vlans after filtering network services.
        The filter is based on filter.tenants, filter.tags and filter.only_vlans_in_use

        Ex. [1, 2, 3 ,4 ,201, 3021]
        '''
        if self._any_network_services:
            vlans = []
            match_tags = self.filter_tags
            if self.group is not None:
                match_tags.append(self.group)

            if self.filter_only_vlans_in_use:
                # Only include the vlans that are used by connected endpoints
                vlans_in_use, trunk_groups_in_use = self._endpoint_vlans_and_trunk_groups
                if self.mlag:
                    # Make sure to also configure vlans used on the MLAG peer.
                    # This could happen if a connected endpoint is only connected to one leaf.
                    mlag_peer_facts: EosDesignsFacts = get(self._hostvars, f"avd_switch_facts..{self.mlag_peer}..switch", separator="..")
                    if mlag_peer_facts:
                        mlag_vlans_in_use, mlag_trunk_groups_in_use = mlag_peer_facts._endpoint_vlans_and_trunk_groups
                        vlans_in_use.extend(mlag_vlans_in_use)
                        trunk_groups_in_use.extend(mlag_trunk_groups_in_use)
                vlans_in_use = set(vlans_in_use)
                trunk_groups_in_use = set(trunk_groups_in_use)

            network_services_keys = get(self._hostvars, "network_services_keys", default=[])
            for network_services_key in self._natural_sort(network_services_keys, "name"):
                network_services_key_name = network_services_key.get("name")
                if network_services_key_name is None or get(self._hostvars, network_services_key_name) is None:
                    # Invalid network_services_key.name. Skipping.
                    continue

                tenants = get(self._hostvars, network_services_key_name)
                # Support legacy data model by converting nested dict to list of dict
                tenants = self._convert_dicts(tenants, 'name')
                for tenant in self._natural_sort(tenants, 'name'):
                    if not set(self.filter_tenants).intersection([tenant['name'], 'all']):
                        # Not matching tenant filters. Skipping this tenant.
                        continue

                    vrfs = tenant.get('vrfs', [])
                    # Support legacy data model by converting nested dict to list of dict
                    vrfs = self._convert_dicts(vrfs, 'name')
                    for vrf in self._natural_sort(vrfs, 'name'):
                        svis = vrf.get('svis', [])
                        # Support legacy data model by converting nested dict to list of dict
                        svis = self._convert_dicts(svis, 'id')
                        for svi in self._natural_sort(svis, 'id'):
                            svi_tags = svi.get('tags', ['all'])
                            if "all" in match_tags or set(svi_tags).intersection(match_tags):
                                if self.filter_only_vlans_in_use:
                                    # Check if vlan is in use
                                    if int(svi['id']) in vlans_in_use:
                                        vlans.append(int(svi['id']))
                                        continue
                                    # Check if vlan has a trunk group defined which is in use
                                    if self.enable_trunk_groups and svi.get("trunk_groups") and trunk_groups_in_use.intersection(svi["trunk_groups"]):
                                        vlans.append(int(svi['id']))
                                        continue
                                    # Skip since the vlan is not in use
                                    continue
                                vlans.append(int(svi['id']))

                    l2vlans = tenant.get('l2vlans', [])
                    # Support legacy data model by converting nested dict to list of dict
                    l2vlans = self._convert_dicts(l2vlans, 'id')

                    for l2vlan in self._natural_sort(l2vlans, 'id'):
                        l2vlan_tags = l2vlan.get('tags', ['all'])
                        if "all" in match_tags or set(l2vlan_tags).intersection(match_tags):
                            if self.filter_only_vlans_in_use:
                                # Check if vlan is in use
                                if int(l2vlan['id']) in vlans_in_use:
                                    vlans.append(int(l2vlan['id']))
                                    continue
                                # Check if vlan has a trunk group defined which is in use
                                if self.enable_trunk_groups and l2vlan.get("trunk_groups") and trunk_groups_in_use.intersection(l2vlan["trunk_groups"]):
                                    vlans.append(int(l2vlan['id']))
                                    continue
                                # Skip since the vlan is not in use
                                continue
                            vlans.append(int(l2vlan['id']))
            return vlans
        return []

    @cached_property
    def vlans(self):
        '''
        Return the compressed list of vlans to be defined on this switch

        Ex. "1-100, 201-202"
        '''
        return self._list_compress(self._vlans)

    @cached_property
    def spanning_tree_mode(self):
        if self.network_services_l2 is True:
            return get(self._switch_data_combined, "spanning_tree_mode")
        return "none"

    @cached_property
    def spanning_tree_priority(self):
        if self.network_services_l2 is True:
            return get(self._switch_data_combined, "spanning_tree_priority")
        return None

    @cached_property
    def spanning_tree_root_super(self):
        if self.network_services_l2 is True:
            return get(self._switch_data_combined, "spanning_tree_root_super")
        return None

    @cached_property
    def underlay_multicast(self):
        return get(self._hostvars, "underlay_multicast")

    @cached_property
    def overlay_rd_type_admin_subfield(self):
        tmp_overlay_rd_type_admin_subfield = default(
            get(self._hostvars, "evpn_rd_type.admin_subfield"),
            get(self._hostvars, "overlay_rd_type.admin_subfield")
        )
        tmp_overlay_rd_type_admin_subfield_offset = default(
            get(self._hostvars, "evpn_rd_type.admin_subfield_offset"),
            get(self._hostvars, "overlay_rd_type.admin_subfield_offset"),
            0
        )
        if tmp_overlay_rd_type_admin_subfield is None:
            return self.router_id
        if tmp_overlay_rd_type_admin_subfield == "vtep_loopback":
            return self.vtep_ip
        if tmp_overlay_rd_type_admin_subfield == "bgp_as":
            return self.bgp_as
        if tmp_overlay_rd_type_admin_subfield == "switch_id":
            return self.id + tmp_overlay_rd_type_admin_subfield_offset
        if isinstance(tmp_overlay_rd_type_admin_subfield, int) and tmp_overlay_rd_type_admin_subfield > 0 and tmp_overlay_rd_type_admin_subfield <= 4294967295:
            return tmp_overlay_rd_type_admin_subfield + tmp_overlay_rd_type_admin_subfield_offset
        if isinstance(tmp_overlay_rd_type_admin_subfield, str):
            try:
                ipaddress.ip_address(tmp_overlay_rd_type_admin_subfield)
                return tmp_overlay_rd_type_admin_subfield
            except ValueError:
                pass
        return self.router_id

    @cached_property
    def evpn_multicast(self):
        if "evpn" not in self.overlay_address_families:
            return None
        if get(self._hostvars, "evpn_multicast") is True and self.vtep is True:
            if not (
                self.underlay_multicast is True
                and self.igmp_snooping_enabled is not False
            ):
                raise AristaAvdError(
                    "'evpn_multicast: True' is only supported in "
                    "combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                )
            elif self.mlag is True:
                peer_overlay_rd_type_admin_subfield = get(self._hostvars,
                                                          f"avd_switch_facts..{self.mlag_peer}..switch..overlay_rd_type_admin_subfield",
                                                          org_key=f"avd_switch_facts.({self.mlag_peer}).switch.overlay_rd_type_admin_subfield",
                                                          separator="..")
                if self.overlay_rd_type_admin_subfield == peer_overlay_rd_type_admin_subfield:
                    raise AristaAvdError(
                        "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' "
                        "since it will create a multi-vtep configuration."
                    )
            return get(self._hostvars, "evpn_multicast", default=False)
        return None

    @cached_property
    def multi_vtep(self):
        if self.mlag is True and self.evpn_multicast is True:
            return True
        return None

    @cached_property
    def igmp_snooping_enabled(self):
        if self.network_services_l2 is True:
            default_igmp_snooping_enabled = get(self._hostvars, "default_igmp_snooping_enabled")
            return get(self._switch_data_combined, "igmp_snooping_enabled", default=default_igmp_snooping_enabled)
        return None

    @cached_property
    def loopback_ipv4_pool(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def loopback_ipv4_offset(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "loopback_ipv4_offset", default=0)
        return None

    @cached_property
    def uplink_ipv4_pool(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "uplink_ipv4_pool")
        return None

    @cached_property
    def _ansible_search_path(self):
        return get(self._hostvars, "ansible_search_path", required=True)

    @cached_property
    def router_id(self):
        '''
        Run template lookup to render ipv4 address for router_id

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.underlay_router is True:
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            template_vars['loopback_ipv4_pool'] = self.loopback_ipv4_pool
            template_vars['loopback_ipv4_offset'] = self.loopback_ipv4_offset
            template_path = get(self.ip_addressing, "router_id", required=True)
            return template_var(template_path, template_vars, self._template_lookup_module)
        return None

    @cached_property
    def evpn_gateway_vxlan_l2(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "evpn_gateway.evpn_l2.enabled", default=False)
        return None

    @cached_property
    def evpn_gateway_vxlan_l3(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "evpn_gateway.evpn_l3.enabled", default=False)
        return None

    @cached_property
    def evpn_gateway_vxlan_l3_inter_domain(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "evpn_gateway.evpn_l3.inter_domain", default=True)
        return None

    @cached_property
    def evpn_gateway_remote_peers(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "evpn_gateway.remote_peers")
        return None

    @cached_property
    def bgp_defaults(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "bgp_defaults", default=[])
        return None

    @cached_property
    def bgp_cluster_id(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "bgp_cluster_id")
        return None

    @cached_property
    def bgp_peer_groups(self):
        '''
        Get bgp_peer_groups configurations or fallback to defaults

        Supporting legacy uppercase keys as well.
        '''
        if self.underlay_router is True:
            return {
                "ipv4_underlay_peers": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.name"),
                        get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name"),
                        "IPv4-UNDERLAY-PEERS"
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.password"),
                        get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password")
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.structured_config")
                    ),
                },
                "mlag_ipv4_underlay_peer": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.name"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name"),
                        "MLAG-IPv4-UNDERLAY-PEER"
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.password"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password")
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.structured_config")
                    ),
                },
                "evpn_overlay_peers": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.name"),
                        get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.name"),
                        "EVPN-OVERLAY-PEERS"
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.password"),
                        get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.password")
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.structured_config")
                    ),
                },
                "evpn_overlay_core": {
                    "name": get(self._hostvars, "bgp_peer_groups.evpn_overlay_core.name", default="EVPN-OVERLAY-CORE"),
                    "password": get(self._hostvars, "bgp_peer_groups.evpn_overlay_core.password"),
                    "structured_config": get(self._hostvars, "bgp_peer_groups.evpn_overlay_core.structured_config"),
                },
                "mpls_overlay_peers": {
                    "name": get(self._hostvars, "bgp_peer_groups.mpls_overlay_peers.name", default="MPLS-OVERLAY-PEERS"),
                    "password": get(self._hostvars, "bgp_peer_groups.mpls_overlay_peers.password"),
                    "structured_config": get(self._hostvars, "bgp_peer_groups.mpls_overlay_peers.structured_config"),
                },
                "rr_overlay_peers": {
                    "name": get(self._hostvars, "bgp_peer_groups.rr_overlay_peers.name", default="RR-OVERLAY-PEERS"),
                    "password": get(self._hostvars, "bgp_peer_groups.rr_overlay_peers.password"),
                    "structured_config": get(self._hostvars, "bgp_peer_groups.rr_overlay_peers.structured_config"),
                },
            }
        return None

    @cached_property
    def evpn_role(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "evpn_role", default=self.default_evpn_role)
        return None

    @cached_property
    def mpls_overlay_role(self):
        if self.underlay_router is True:
            return get(self._switch_data_combined, "mpls_overlay_role", default=self.default_mpls_overlay_role)
        return None

    @cached_property
    def bgp_as(self):
        '''
        Get global bgp_as or fabric_topology bgp_as.

        This will fail if none of these are found.
        '''
        if self.underlay_router is True:
            if self.underlay_routing_protocol == 'ebgp' or self.evpn_role != 'none' or self.mpls_overlay_role != 'none':
                if get(self._hostvars, "bgp_as") is not None:
                    return str(get(self._hostvars, "bgp_as"))
                else:
                    return str(get(self._switch_data_combined, "bgp_as", required=True))
            # Hack to make mpls PR non-breaking, adds empty bgp to igp topology spines
            # TODO: Remove this as part of AVD4.0
            elif (
                self.underlay_routing_protocol in ['isis', 'ospf']
                and self.evpn_role == 'none'
                and get(self._hostvars, "bgp_as") is not None
            ):
                return str(get(self._hostvars, "bgp_as"))
        return None

    @cached_property
    def evpn_route_servers(self):
        '''
        For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
        For all other evpn roles there is no default.
        '''
        if self.underlay_router is True:
            if self.evpn_role == "client":
                return get(self._switch_data_combined, "evpn_route_servers", default=self.uplink_switches)
            else:
                return get(self._switch_data_combined, "evpn_route_servers")
        return []

    @cached_property
    def mpls_route_reflectors(self):
        if self.underlay_router is True:
            if self.mpls_overlay_role in ["client", "server"]:
                return get(self._switch_data_combined, "mpls_route_reflectors")
        return None

    @cached_property
    def isis_net(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ['isis', 'isis-ldp', 'isis-sr', 'isis-sr-ldp']:
                isis_system_id_prefix = get(self._switch_data_combined, "isis_system_id_prefix")
                if isis_system_id_prefix is not None:
                    isis_area_id = get(self._hostvars, "isis_area_id", required=True)
                    switch_id = self.id
                    return f"{isis_area_id}.{isis_system_id_prefix}.{switch_id:04d}.00"
        return None

    @cached_property
    def is_type(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ['isis', 'isis-ldp', 'isis-sr', 'isis-sr-ldp']:
                default_is_type = get(self._hostvars, "isis_default_is_type", default="level-2")
                is_type = str(get(self._switch_data_combined, "is_type", default=default_is_type)).lower()
                if is_type not in ["level-1", "level-2", "level-1-2"]:
                    is_type = "level-2"
                return is_type
        return None

    @cached_property
    def isis_instance_name(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ['isis', 'isis-ldp', 'isis-sr', 'isis-sr-ldp']:
                if self.mpls_lsr is True:
                    default_isis_instance_name = "CORE"
                else:
                    default_isis_instance_name = "EVPN_UNDERLAY"
                return get(self._hostvars, "underlay_isis_instance_name", default=default_isis_instance_name)
        return None

    @cached_property
    def node_sid(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ['isis-sr', 'isis-sr-ldp']:
                node_sid_base = int(get(self._switch_data_combined, "node_sid_base", 0))
                return self.id + node_sid_base
        return None

    @cached_property
    def underlay_ipv6(self):
        if self.underlay_router is True:
            return get(self._hostvars, "underlay_ipv6")
        return None

    @cached_property
    def loopback_ipv6_pool(self):
        if self.underlay_ipv6 is True:
            return get(self._switch_data_combined, "loopback_ipv6_pool", required=True)
        return None

    @cached_property
    def loopback_ipv6_offset(self):
        if self.underlay_ipv6 is True:
            return get(self._switch_data_combined, "loopback_ipv6_offset", default=0)
        return None

    @cached_property
    def ipv6_router_id(self):
        '''
        Run template lookup to render ipv6 address for router_id

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.underlay_ipv6 is True:
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            template_vars['loopback_ipv6_pool'] = self.loopback_ipv6_pool
            template_vars['loopback_ipv6_offset'] = self.loopback_ipv6_offset
            template_path = get(self.ip_addressing, "ipv6_router_id", required=True)
            return template_var(template_path, template_vars, self._template_lookup_module)
        return None

    @cached_property
    def mlag(self):
        return (
            self.mlag_support is True
            and get(self._switch_data_combined, "mlag", default=True) is True
            and len(self._switch_data_node_group_nodes) == 2
        )

    @cached_property
    def mlag_ibgp_origin_incomplete(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_ibgp_origin_incomplete", default=True)
        return None

    @cached_property
    def mlag_peer_vlan(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_vlan", default=4094)
        return None

    @cached_property
    def mlag_peer_link_allowed_vlans(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_link_allowed_vlans", default="2-4094")
        return None

    @cached_property
    def mlag_dual_primary_detection(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_dual_primary_detection", default=False)
        return None

    @cached_property
    def mlag_interfaces(self):
        if self.mlag is True:
            return self._range_expand(default(
                get(self._switch_data_combined, "mlag_interfaces"),
                get(self.default_interfaces, "mlag_interfaces"),
                [])
            )
        return None

    @cached_property
    def mlag_interfaces_speed(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_interfaces_speed")
        return None

    @cached_property
    def mlag_peer_ipv4_pool(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_ipv4_pool")
        return None

    @cached_property
    def mlag_peer_l3_ipv4_pool(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_l3_ipv4_pool")
        return None

    @cached_property
    def mlag_port_channel_structured_config(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_port_channel_structured_config")
        return None

    @cached_property
    def mlag_peer_vlan_structured_config(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_vlan_structured_config")
        return None

    @cached_property
    def mlag_peer_l3_vlan_structured_config(self):
        if self.mlag is True:
            return get(self._switch_data_combined, "mlag_peer_l3_vlan_structured_config")
        return None

    @cached_property
    def mlag_role(self):
        if self.mlag is True:
            if self._switch_data_node_group_nodes[0]["name"] == self.hostname:
                return "primary"
            elif self._switch_data_node_group_nodes[1]["name"] == self.hostname:
                return "secondary"
        return None

    @cached_property
    def mlag_peer(self):
        if self.mlag is True:
            if self.mlag_role == "primary":
                return self._switch_data_node_group_nodes[1]["name"]
            if self.mlag_role == "secondary":
                return self._switch_data_node_group_nodes[0]["name"]
        return None

    @cached_property
    def mlag_l3(self):
        if self.mlag is True and self.underlay_router is True:
            return True
        return None

    @cached_property
    def mlag_peer_l3_vlan(self):
        if self.mlag_l3 is True:
            mlag_peer_vlan = self.mlag_peer_vlan
            mlag_peer_l3_vlan = get(self._switch_data_combined, "mlag_peer_l3_vlan", default=4093)
            if mlag_peer_l3_vlan not in [None, False, mlag_peer_vlan]:
                return mlag_peer_l3_vlan
        return None

    @cached_property
    def mlag_port_channel_id(self):
        if self.mlag is True:
            default_mlag_port_channel_id = ''.join(re.findall(r'\d', self.mlag_interfaces[0]))
            return get(self._switch_data_combined, "mlag_port_channel_id", default_mlag_port_channel_id)
        return None

    @cached_property
    def vtep_loopback_ipv4_pool(self):
        if self.vtep is True:
            return get(self._switch_data_combined, "vtep_loopback_ipv4_pool", required=True)
        return None

    @cached_property
    def vtep_loopback(self):
        if self.vtep is True:
            return get(self._switch_data_combined, "vtep_loopback", default="Loopback1")

    @cached_property
    def inband_management_subnet(self):
        return get(self._switch_data_combined, "inband_management_subnet")

    @cached_property
    def inband_management_role(self):
        if self.inband_management_subnet is not None and self.uplink_type == 'port-channel':
            return "child"
        return None

    @cached_property
    def inband_management_parents(self):
        if self.inband_management_role == "child":
            return self.uplink_switches
        return None

    @cached_property
    def inband_management_vlan(self):
        if self.inband_management_role == "child":
            return get(self._switch_data_combined, "inband_management_vlan", default=4092)
        return None

    @cached_property
    def inband_management_ip(self):
        if self.inband_management_role == "child":
            subnet = ipaddress.ip_network(self.inband_management_subnet, strict=False)
            hosts = list(subnet.hosts())
            inband_management_ip = str(hosts[2 + self.id])
            inband_management_prefix = str(subnet.prefixlen)
            return f"{inband_management_ip}/{inband_management_prefix}"
        return None

    @cached_property
    def inband_management_gateway(self):
        if self.inband_management_role == "child":
            subnet = ipaddress.ip_network(self.inband_management_subnet, strict=False)
            hosts = list(subnet.hosts())
            return str(hosts[0])
        return None

    @cached_property
    def inband_management_interface(self):
        if self.inband_management_role == "child":
            return f"Vlan{self.inband_management_vlan}"
        return None

    @cached_property
    def uplinks(self):
        '''
        List of uplinks with all parameters

        These facts are leveraged by templates for this device when rendering uplinks
        and by templates for peer devices when rendering downlinks
        '''
        uplinks = []

        if self.uplink_type == 'p2p':
            uplink_interfaces = default(self.uplink_interfaces, [])
            uplink_switches = default(self.uplink_switches, [])
            uplink_switch_interfaces = default(self.uplink_switch_interfaces, [])
            fabric_name = get(self._hostvars, "fabric_name", required=True)
            inventory_group = get(self._hostvars, f"groups.{fabric_name}", required=True)
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            for uplink_index, uplink_interface in enumerate(uplink_interfaces):
                if len(uplink_switches) <= uplink_index or len(uplink_switch_interfaces) <= uplink_index:
                    # Invalid length of input variables. Skipping
                    continue

                uplink_switch = uplink_switches[uplink_index]
                if uplink_switch is None or uplink_switch not in inventory_group:
                    # Invalid uplink_switch. Skipping.
                    continue

                uplink_switch_facts: EosDesignsFacts = get(self._hostvars,
                                                           f"avd_switch_facts..{uplink_switch}..switch",
                                                           required=True,
                                                           org_key=f"avd_switch_facts.({uplink_switch}).switch",
                                                           separator="..")
                uplink = {}
                uplink['interface'] = uplink_interface
                uplink['peer'] = uplink_switch
                uplink['peer_interface'] = uplink_switch_interfaces[uplink_index]
                uplink['peer_type'] = uplink_switch_facts.type
                uplink['peer_is_deployed'] = uplink_switch_facts.is_deployed
                uplink['peer_bgp_as'] = uplink_switch_facts.bgp_as
                uplink['type'] = 'underlay_p2p'
                if self.uplink_interface_speed is not None:
                    uplink['speed'] = self.uplink_interface_speed
                if self.uplink_bfd is True:
                    uplink['bfd'] = True
                if self.uplink_ptp is not None:
                    uplink['ptp'] = self.uplink_ptp
                if self.uplink_macsec is not None:
                    uplink['mac_security'] = self.uplink_macsec
                if self.underlay_multicast is True and uplink_switch_facts.underlay_multicast is True:
                    uplink['underlay_multicast'] = True
                if get(self._hostvars, "underlay_rfc5549") is True:
                    uplink['ipv6_enable'] = True
                else:
                    template_vars['uplink_switch_index'] = uplink_index
                    template_path = get(self.ip_addressing, "p2p_uplinks_ip", required=True)
                    uplink['ip_address'] = template_var(template_path, template_vars, self._template_lookup_module)
                    template_path = get(self.ip_addressing, "p2p_uplinks_peer_ip", required=True)
                    uplink['peer_ip_address'] = template_var(template_path, template_vars, self._template_lookup_module)

                if self.link_tracking_groups is not None:
                    uplink['link_tracking_groups'] = []
                    for lt_group in self.link_tracking_groups:
                        uplink['link_tracking_groups'].append({"name": lt_group["name"], "direction": "upstream"})

                if self.uplink_structured_config is not None:
                    uplink['structured_config'] = self.uplink_structured_config

                uplinks.append(uplink)
            return uplinks

        elif self.uplink_type == 'port-channel':
            uplink_interfaces = default(self.uplink_interfaces, [])
            uplink_switches = default(self.uplink_switches, [])
            uplink_switch_interfaces = default(self.uplink_switch_interfaces, [])
            fabric_name = get(self._hostvars, "fabric_name", required=True)
            inventory_group = get(self._hostvars, f"groups.{fabric_name}", required=True)

            for uplink_index, uplink_interface in enumerate(uplink_interfaces):
                if len(uplink_switches) <= uplink_index or len(uplink_switch_interfaces) <= uplink_index:
                    # Invalid length of input variables. Skipping
                    continue

                uplink_switch = uplink_switches[uplink_index]
                if uplink_switch is None or uplink_switch not in inventory_group:
                    # Invalid uplink_switch. Skipping.
                    continue

                uplink_switch_facts: EosDesignsFacts = get(self._hostvars,
                                                           f"avd_switch_facts..{uplink_switch}..switch",
                                                           required=True,
                                                           org_key=f"avd_switch_facts.({uplink_switch}).switch",
                                                           separator="..")
                uplink = {}
                uplink['interface'] = uplink_interface
                uplink['peer'] = uplink_switch
                uplink['peer_interface'] = uplink_switch_interfaces[uplink_index]
                uplink['peer_type'] = uplink_switch_facts.type
                uplink['peer_is_deployed'] = uplink_switch_facts.is_deployed
                uplink['type'] = 'underlay_l2'

                if self.uplink_interface_speed is not None:
                    uplink['speed'] = self.uplink_interface_speed

                if uplink_switch_facts.mlag is True or self.short_esi is not None:
                    # Override our description on port-channel to be peer's group name if they are mlag pair or A/A #}
                    uplink['channel_description'] = uplink_switch_facts.group

                if self.mlag is True:
                    # Override the peer's description on port-channel to be our group name if we are mlag pair #}
                    uplink['peer_channel_description'] = self.group

                if self.mlag_role == 'secondary':
                    mlag_peer_switch_facts: EosDesignsFacts = get(self._hostvars, f"avd_switch_facts.{self.mlag_peer}.switch", required=True)

                    uplink['channel_group_id'] = ''.join(re.findall(r'\d', mlag_peer_switch_facts.uplink_interfaces[0]))
                    uplink['peer_channel_group_id'] = ''.join(re.findall(r'\d', mlag_peer_switch_facts.uplink_switch_interfaces[0]))
                else:
                    uplink['channel_group_id'] = ''.join(re.findall(r'\d', uplink_interfaces[0]))
                    uplink['peer_channel_group_id'] = ''.join(re.findall(r'\d', uplink_switch_interfaces[0]))

                # Remove vlans if upstream switch does not have them #}
                if self.enable_trunk_groups:
                    uplink['trunk_groups'] = ["UPLINK"]
                    if self.mlag is True:
                        uplink['peer_trunk_groups'] = [self.group]
                    else:
                        uplink['peer_trunk_groups'] = [self.hostname]

                switch_vlans = self._vlans
                uplink_switch_vlans = uplink_switch_facts._vlans
                uplink_vlans = list(set(switch_vlans).intersection(uplink_switch_vlans))

                if self.inband_management_vlan is not None:
                    uplink_vlans.append(int(self.inband_management_vlan))

                if uplink_vlans:
                    uplink['vlans'] = self._list_compress(uplink_vlans)
                else:
                    uplink['vlans'] = 'none'

                if self.short_esi is not None:
                    uplink['peer_short_esi'] = self.short_esi

                if self.link_tracking_groups is not None:
                    uplink['link_tracking_groups'] = []
                    for lt_group in self.link_tracking_groups:
                        uplink['link_tracking_groups'].append({"name": lt_group["name"], "direction": "upstream"})

                if self.uplink_structured_config is not None:
                    uplink['structured_config'] = self.uplink_structured_config

                uplinks.append(uplink)
        return uplinks

    @cached_property
    def uplink_peers(self):
        '''
        List of all uplink peers

        These are used to generate the "avd_topology_peers" fact covering downlinks for all devices.
        '''
        fabric_name = get(self._hostvars, "fabric_name", required=True)
        inventory_group = get(self._hostvars, f"groups.{fabric_name}", required=True)
        uplink_switches = default(self.uplink_switches, [])
        return [uplink_switch for uplink_switch in uplink_switches if uplink_switch in inventory_group]

    @cached_property
    def _mlag_peer_id(self):
        if self.mlag is True:
            return get(self._hostvars,
                       f"avd_switch_facts..{self.mlag_peer}..switch..id",
                       required=True,
                       org_key=f"avd_switch_facts.({self.mlag_peer}).switch.id",
                       separator="..")

    @cached_property
    def mlag_switch_ids(self):
        '''
        Returns the switch id's of both primary and secondary switches for a given node group
        '''
        if self.mlag_role == 'primary':
            return {"primary": self.id, "secondary": self._mlag_peer_id}
        elif self.mlag_role == 'secondary':
            return {"primary": self._mlag_peer_id, "secondary": self.id}

    @cached_property
    def vtep_ip(self):
        '''
        Run template lookup to render ipv4 address for vtep_ip

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.vtep is True:
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            template_vars['switch_vtep_loopback_ipv4_pool'] = self.vtep_loopback_ipv4_pool
            template_vars['loopback_ipv4_offset'] = self.loopback_ipv4_offset

            if self.mlag is True:
                if self.mlag_role == 'primary':
                    template_vars['mlag_primary_id'] = self.id
                    template_vars['mlag_secondary_id'] = self._mlag_peer_id
                elif self.mlag_role == 'secondary':
                    template_vars['mlag_secondary_id'] = self.id
                    template_vars['mlag_primary_id'] = self._mlag_peer_id

                template_path = get(self.ip_addressing, "vtep_ip_mlag", required=True)
                return template_var(template_path, template_vars, self._template_lookup_module)
            else:
                template_path = get(self.ip_addressing, "vtep_ip", required=True)
                return template_var(template_path, template_vars, self._template_lookup_module)

        return None

    @cached_property
    def mlag_ip(self):
        '''
        Run template lookup to render ipv4 address for mlag_ip

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.mlag is True:
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            template_vars['switch_data'] = {
                "combined": {
                    "mlag_peer_ipv4_pool": self.mlag_peer_ipv4_pool
                }
            }
            if self.mlag_role == 'primary':
                template_vars['mlag_primary_id'] = self.id
                template_vars['mlag_secondary_id'] = self._mlag_peer_id
                template_path = get(self.ip_addressing, "mlag_ip_primary", required=True)
            elif self.mlag_role == 'secondary':
                template_vars['mlag_secondary_id'] = self.id
                template_vars['mlag_primary_id'] = self._mlag_peer_id
                template_path = get(self.ip_addressing, "mlag_ip_secondary", required=True)

            return template_var(template_path, template_vars, self._template_lookup_module)
        return None

    @cached_property
    def mlag_peer_ip(self):
        if self.mlag is True:
            return get(self._hostvars,
                       f"avd_switch_facts..{self.mlag_peer}..switch..mlag_ip",
                       required=True,
                       org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_ip",
                       separator="..")
        return None

    @cached_property
    def mlag_l3_ip(self):
        '''
        Run template lookup to render ipv4 address for mlag_l3_ip

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.mlag_l3 is True and self.mlag_peer_l3_vlan is not None:
            template_vars = self._template_vars
            # Copying __dict__ will expose all switch facts cached up until this function is run.
            # TODO: We should probably find and document a list of supported context variables instead.
            template_vars['switch'] = {key: self.__dict__.get(key) for key in self.keys()}
            template_vars['switch_id'] = self.id
            template_vars['switch_data'] = {
                "combined": {
                    "mlag_peer_l3_ipv4_pool": self.mlag_peer_l3_ipv4_pool
                }
            }
            if self.mlag_role == 'primary':
                template_vars['mlag_primary_id'] = self.id
                template_vars['mlag_secondary_id'] = self._mlag_peer_id
                template_path = get(self.ip_addressing, "mlag_l3_ip_primary", required=True)
            elif self.mlag_role == 'secondary':
                template_vars['mlag_secondary_id'] = self.id
                template_vars['mlag_primary_id'] = self._mlag_peer_id
                template_path = get(self.ip_addressing, "mlag_l3_ip_secondary", required=True)

            return template_var(template_path, template_vars, self._template_lookup_module)
        return None

    @cached_property
    def mlag_peer_l3_ip(self):
        if self.mlag_l3 is True and self.mlag_peer_l3_vlan is not None:
            return get(self._hostvars,
                       f"avd_switch_facts..{self.mlag_peer}..switch..mlag_l3_ip",
                       required=True,
                       org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_l3_ip",
                       separator="..")
        return None

    @cached_property
    def mlag_peer_mgmt_ip(self):
        if self.mlag is True:
            peer_mgmt_ip = get(self._hostvars,
                               f"avd_switch_facts..{self.mlag_peer}..switch..mgmt_ip",
                               org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mgmt_ip",
                               separator="..")
            if peer_mgmt_ip is not None:
                return str(ipaddress.ip_interface(peer_mgmt_ip).ip)
        return None

    @cached_property
    def overlay_routing_protocol_address_family(self):
        overlay_routing_protocol_address_family = get(self._hostvars, "overlay_routing_protocol_address_family", default="ipv4")
        if overlay_routing_protocol_address_family == "ipv6":
            if not (
                get(self._hostvars, "underlay_ipv6") is True
                and get(self._hostvars, "underlay_rfc5549") is True
            ):
                raise AristaAvdError(
                    "'overlay_routing_protocol_address_family: ipv6' is only supported in"
                    "combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
                )
        return overlay_routing_protocol_address_family

    @cached_property
    def overlay_routing_protocol_peering_address(self):
        if self.overlay_routing_protocol_address_family == "ipv6":
            return self.ipv6_router_id
        return self.router_id
