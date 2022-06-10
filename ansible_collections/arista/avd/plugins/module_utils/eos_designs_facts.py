from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
import ipaddress
from functools import cached_property
from hashlib import sha256
from ansible_collections.arista.avd.plugins.module_utils.utils import AristaAvdError, get, default, template_var, AristaAvdMissingVariableError


class EosDesignsFacts:
    def __init__(
        self,
        hostvars=None,
        combine=None,
        list_compress=None,
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
        raise AristaAvdMissingVariableError(f"node_type_keys.<>.type=={type}")

    @cached_property
    def connected_endpoints(self):
        """
        switch.connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints
        """
        return get(self._node_type_key_data, "connected_endpoints", default=False)

    @cached_property
    def default_evpn_role(self):
        """
        switch.default_evpn_role set based on
        node_type_keys.<node_type_key>.default_evpn_role
        """
        return get(self._node_type_key_data, "default_evpn_role", default="none")

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
    def _switch_data(self):
        """
        internal _switch_data containing inherited vars from fabric_topology data model

        Vars are inherited like:
        <node_type_key>.defaults ->
            <node_type_key>.node_groups.<group> ->
                <node_type_key>.node_groups.<group>.nodes.<node> ->
                <node_type_key>.nodes.<node>

        Returns
        -------
        dict
            node_group : dict
                Configuration set at the node_group level - including the "nodes" dict.
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

        if hostname in node_type_config.get('nodes', {}):
            node_config = node_type_config['nodes'][hostname]
        else:
            for node_group in node_type_config.get('node_groups', {}):
                if hostname in node_type_config['node_groups'][node_group].get('nodes', {}):
                    node_config = node_type_config['node_groups'][node_group]['nodes'][hostname]
                    switch_data['node_group'] = node_type_config['node_groups'][node_group]
                    switch_data['group'] = node_group
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
        return get(self._switch_data_combined, "uplink_interfaces")

    @cached_property
    def uplink_switch_interfaces(self):
        return get(self._switch_data_combined, "uplink_switch_interfaces")

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
        if underlay_routing_protocol not in ['ebgp', 'isis', 'isis-ldp', 'isis-sr', 'isis-sr-ldp', 'ospf', 'ospf-ldp']:
            underlay_routing_protocol = self.default_underlay_routing_protocol
        return underlay_routing_protocol

    @cached_property
    def overlay_routing_protocol(self):
        overlay_routing_protocol = str(get(self._hostvars, "overlay_routing_protocol", default=self.default_overlay_routing_protocol)).lower()
        if overlay_routing_protocol not in ['ebgp', 'ibgp']:
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
    def virtual_router_mac_address(self):
        if self._any_network_services:
            return get(self._switch_data_combined, "virtual_router_mac_address")
        return None

    @cached_property
    def _vlans(self):
        if self._any_network_services:
            vlans = []
            match_tags = self.filter_tags
            if self.group is not None:
                match_tags.append(self.group)

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
                                vlans.append(int(svi['id']))

                    l2vlans = tenant.get('l2vlans', [])
                    # Support legacy data model by converting nested dict to list of dict
                    l2vlans = self._convert_dicts(l2vlans, 'id')

                    for l2vlan in self._natural_sort(l2vlans, 'id'):
                        l2vlan_tags = l2vlan.get('tags', ['all'])
                        if "all" in match_tags or set(l2vlan_tags).intersection(match_tags):
                            vlans.append(int(l2vlan['id']))
            return vlans
        return []

    @cached_property
    def vlans(self):
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
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
                },
                "evpn_overlay_core": {
                    "name": get(self._hostvars, "bgp_peer_groups.evpn_overlay_core.name", default="EVPN-OVERLAY-CORE"),
                    "password": get(self._hostvars, "bgp_peer_groups.evpn_overlay_core.password")
                },
                "mpls_overlay_peers": {
                    "name": get(self._hostvars, "bgp_peer_groups.mpls_overlay_peers.name", default="MPLS-OVERLAY-PEERS"),
                    "password": get(self._hostvars, "bgp_peer_groups.mpls_overlay_peers.password")
                },
                "rr_overlay_peers": {
                    "name": get(self._hostvars, "bgp_peer_groups.rr_overlay_peers.name", default="RR-OVERLAY-PEERS"),
                    "password": get(self._hostvars, "bgp_peer_groups.rr_overlay_peers.password")
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
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
            return get(self._switch_data_combined, "mlag_interfaces")
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
            index = list(self._switch_data_node_group_nodes.keys()).index(self.hostname)
            if index == 0:
                return "primary"
            elif index == 1:
                return "secondary"
        return None

    @cached_property
    def mlag_peer(self):
        if self.mlag is True:
            if self.mlag_role == "primary":
                return list(self._switch_data_node_group_nodes.keys())[1]
            if self.mlag_role == "secondary":
                return list(self._switch_data_node_group_nodes.keys())[0]
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
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
        if self.uplinks is not None:
            return [uplink['peer'] for uplink in self.uplinks]

    @cached_property
    def _mlag_peer_id(self):
        if self.mlag is True:
            return get(self._hostvars,
                       f"avd_switch_facts..{self.mlag_peer}..switch..id",
                       required=True,
                       org_key=f"avd_switch_facts.({self.mlag_peer}).switch.id",
                       separator="..")

    @cached_property
    def vtep_ip(self):
        '''
        Run template lookup to render ipv4 address for vtep_ip

        Since some templates might contain certain legacy variables (switch_*),
        those are mapped from the switch.* model
        '''
        if self.vtep is True:
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
            template_vars = {"ansible_search_path": self._ansible_search_path}
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
