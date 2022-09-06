from ansible_collections.arista.avd.plugins.module_utils.eos_designs import AvdFacts
from functools import cached_property
from ansible_collections.arista.avd.plugins.module_utils.utils import get
from ansible_collections.arista.avd.plugins.filter.snmp_hash import hash_passphrase
from hashlib import sha1


class AVDStructConfig(AvdFacts):

    @cached_property
    def _mgmt_interface_vrf(self):
        return get(self._hostvars, 'mgmt_interface_vrf')

    @cached_property
    def _mgmt_gateway(self):
        return get(self._hostvars, 'mgmt_gateway')

    @cached_property
    def _switch(self):
        return get(self._hostvars, 'switch', required=True)

    @cached_property
    def _internal_vlan_order(self):
        return get(self._hostvars, 'internal_vlan_order')

    @cached_property
    def _platform_settings(self):
        return get(self._switch, 'platform_settings')

    @cached_property
    def _mgmt_ip(self):
        return get(self._switch, 'mgmt_ip')

    @cached_property
    def _hostname(self):
        """
        switch.hostname fact set based on inventory_hostname variable
        """
        return get(self._hostvars, "inventory_hostname", required=True)

    @cached_property
    def router_bgp(self):
        bgp_as = get(self._switch, "bgp_as")
        if bgp_as is None:
            return None

        bgp_defaults = get(self._switch, 'bgp_defaults')
        bgp_maximum_paths = get(self._hostvars, 'bgp_maximum_paths')
        bgp_ecmp = get(self._hostvars, 'bgp_ecmp')
        if bgp_maximum_paths is not None:
            max_paths_str = f"maximum-paths {bgp_maximum_paths}"
            if get(self._hostvars, 'bgp_ecmp') is not None:
                max_paths_str += f" ecmp {bgp_ecmp}"

            bgp_defaults.append(max_paths_str)

        return {
            'as': bgp_as,
            'router_id': get(self._switch, 'router_id'),
            'bgp_defaults': bgp_defaults,
        }

    @cached_property
    def static_routes(self):
        if self._mgmt_gateway is None:
            return None
        static_routes = []
        mgmt_destination_networks = get(self._hostvars, 'mgmt_destination_network')
        if mgmt_destination_networks is not None:
            for mgmt_destination_network in self._mgmt_destination_networks:
                static_routes.append({'vrf': self._mgmt_interface_vrf,
                                      'destination_address_prefix': mgmt_destination_network,
                                      'gateway': self._mgmt_gateway})
        else:
            static_routes.append({'vrf': self._mgmt_interface_vrf,
                                  'destination_address_prefix': '0.0.0.0/0',
                                  'gateway': self._mgmt_gateway})
        return static_routes

    @cached_property
    def service_routing_protocols_model(self):
        return 'multi-agent'

    @cached_property
    def ip_routing(self):
        return True

    @cached_property
    def ipv6_unicast_routing(self):
        if get(self._hostvars, 'underlay_rfc5549') is True or get(self._switch, 'underlay_ipv6') is True:
            return True
        return None

    @cached_property
    def ip_routing_ipv6_interfaces(self):
        if get(self._hostvars, 'underlay_rfc5549') is True:
            return True
        return None

    @cached_property
    def router_multicast(self):
        if (
                get(self._switch, 'underlay_multicast') is True and
                get(self._switch, 'underlay_router') is True
        ):
            router_multicast = {'ipv4': {'routing': True}}
            if get(self._switch, 'evpn_multicast') is True:
                router_multicast['ipv4'].update({'software_forwarding': 'sfe'})
            return router_multicast
        return None

    @cached_property
    def hardware_counters(self):
        hardware_counter = get(self._hostvars, 'hardware_counters')
        if hardware_counter is not None:
            features = []
            if get(hardware_counter, 'features') is None:
                return None
            features = [{feature: direction} for feature, direction in get(hardware_counter, 'features').items()]
            return {"features": features}

    @cached_property
    def hardware(self):
        platform_speed_groups = get(self._hostvars, 'platform_speed_groups')
        if platform_speed_groups is not None:
            tmp_speed_groups = {}
            switch_platform = get(self._switch, 'platform')
            if switch_platform is not None:
                for platform_item in platform_speed_groups:
                    if "platform" in platform_item and "speeds" in platform_item:
                        platform = platform_item
                    else:
                        platform = {"platform": platform_item, "speeds": platform_speed_groups[platform_item]}
                    if platform['platform'] == switch_platform:
                        speeds = self._convert_dicts(get(platform, 'speeds'), 'speed', 'speed_groups')
                        for speed in self._natural_sort(speeds, 'speed'):
                            for speed_group in speed['speed_groups']:
                                tmp_speed_groups.update({speed_group: speed['speed']})
            if tmp_speed_groups:
                hardware = {'speed_groups': {}}
                for speed_group in self._natural_sort(tmp_speed_groups):
                    hardware['speed_groups'].update({speed_group: {'serdes': tmp_speed_groups[speed_group]}})
                return hardware
        return None

    @cached_property
    def daemon_terminattr(self):
        cvp_instance_ip = get(self._hostvars, 'cvp_instance_ip')
        cvp_instance_ips = get(self._hostvars, 'cvp_instance_ips')
        if cvp_instance_ip is None and cvp_instance_ips is None:
            return None
        cvp_on_prem = {'ips': []}
        cvaas = {'ips': []}
        if cvp_instance_ip is not None:
            if "arista.io" in cvp_instance_ip:
                cvaas['ips'].append(cvp_instance_ip)
            else:
                cvp_on_prem['ips'].append(cvp_instance_ip)
        elif cvp_instance_ips is not None:
            for cvp_ip in cvp_instance_ips:
                if "arista.io" in cvp_ip:
                    cvaas['ips'].append(cvp_ip)
                else:
                    cvp_on_prem['ips'].append(cvp_ip)

        daemon_terminattr = {'cvaddrs': []}
        if cvp_on_prem['ips']:
            for cvp_instance_ip in cvp_on_prem['ips']:
                daemon_terminattr['cvaddrs'].append(f"{cvp_instance_ip}:"
                                                    f"{get(self._hostvars, 'terminattr_ingestgrpcurl_port')}")
            daemon_terminattr['cvauth'] = {
                'method': 'key',
                'key': get(self._hostvars, 'cvp_ingestauth_key')
            }

        elif cvaas['ips']:
            for cvp_instance_ip in cvaas['ips']:
                daemon_terminattr['cvaddrs'].append(f"{cvp_instance_ip}:443")
            daemon_terminattr.update({'cvauth': {'method': 'token-secure',
                                                 'token_file': get(self._hostvars, 'cvp_token_file',
                                                                   '/tmp/cv-onboarding-token')}})

        daemon_terminattr.update({'cvvrf': self._mgmt_interface_vrf})
        daemon_terminattr.update({'smashexcludes': get(self._hostvars, 'terminattr_smashexcludes')})
        daemon_terminattr.update({'ingestexclude': get(self._hostvars, 'terminattr_ingestexclude')})
        daemon_terminattr.update({'disable_aaa': get(self._hostvars, 'terminattr_disable_aaa', False)})
        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self):
        range = get(self._internal_vlan_order, 'range')
        return {
            'allocation': get(self._internal_vlan_order, 'allocation'),
            'range': {
                'beginning': get(range, 'beginning'),
                'ending': get(range, 'ending')
            }
        }

    @cached_property
    def event_monitor(self):
        if get(self._hostvars, 'event_monitor') is True:
            return {'enabled': 'true'}
        return None

    @cached_property
    def event_handlers(self):
        event_handlers = get(self._hostvars, 'event_handlers')
        if event_handlers is not None and hasattr(event_handlers, '__iter__'):
            event_handlers = self._convert_dicts(event_handlers, 'name')
            for handler in event_handlers:
                handler_name = get(handler, 'name')
                event_handler = {handler_name: {}}
                action = get(handler, 'action')
                action_type = get(handler, 'action_type')
                delay = get(handler, 'delay')
                trigger = get(handler, 'trigger')
                regex = get(handler, 'regex')
                if action is not None and action_type is not None:
                    event_handler[handler_name].update({'action_type': action_type})
                    event_handler[handler_name].update({'action': action})
                if delay is not None:
                    event_handler[handler_name].update({'delay': delay})
                if get(handler, 'asynchronous') is True:
                    event_handler[handler_name].update({'asynchronous': 'handler.asynchronous'})
                if trigger is not None:
                    event_handler[handler_name].update({'trigger': trigger})
                if regex is not None:
                    event_handler[handler_name].update({'regex': regex})
            return event_handler
        return None

    @cached_property
    def load_interval(self):
        if (load_interval_default := get(self._hostvars, 'load_interval_default')) is not None:
            return {'default': load_interval_default}
        return None

    @cached_property
    def queue_monitor_length(self):
        queue_monitor_length = get(self._hostvars, 'queue_monitor_length')
        if queue_monitor_length is not None:
            queue_monitor_length_dict = {'enabled': True}
            queue_monitor_length_notifying = get(queue_monitor_length, 'notifying')
            feature_support = get(self._platform_settings, 'feature_support')
            queue_monitor_length_notify = ""
            if feature_support is not None:
                queue_monitor_length_notify = get(feature_support, 'queue_monitor_length_notify')
            if (
                    queue_monitor_length_notifying is not None and
                    queue_monitor_length_notify is not False
            ):
                queue_monitor_length_dict.update({'notifying': queue_monitor_length_notifying})
            if get(queue_monitor_length, 'log') is not None:
                queue_monitor_length_dict.update({'log': get(queue_monitor_length, 'log')})
            return queue_monitor_length_dict
        return None

    @cached_property
    def name_server(self):
        name_servers = get(self._hostvars, 'name_servers')
        if name_servers is not None:
            return {
                'source':
                    {
                        'vrf': self._mgmt_interface_vrf
                    },
                'nodes': name_servers
            }
        return None

    @cached_property
    def redundancy(self):
        redundancy = get(self._hostvars, 'redundancy')
        if redundancy is not None:
            protocol = get(redundancy, 'protocol')
            if protocol is not None:
                return {'protocol': protocol}
        return None

    @cached_property
    def snmp_server(self):
        snmp_settings = get(self._hostvars, 'snmp_settings')
        if snmp_settings is not None:
            snmp_server = {}
            compute_local_engineid = get(snmp_settings, 'compute_local_engineid')
            if compute_local_engineid is True:
                local_engine_id = sha1(f"{self._hostname}{self._mgmt_ip}".encode('utf-8')).hexdigest()
                snmp_server.update({'engineid': {'local': local_engine_id}})
            contact = get(snmp_settings, 'contact')
            if contact is not None:
                snmp_server.update({'contact': contact})
            if get(snmp_settings, 'location') is not None:
                snmp_location = get(self._hostvars, 'fabric_name')
                dc_name = get(self._hostvars, 'dc_name')
                if dc_name is not None:
                    snmp_location = f"{snmp_location} {dc_name}"
                pod_name = get(self._hostvars, 'pod_name')
                if pod_name is not None:
                    snmp_location = f"{snmp_location} {pod_name}"
                rack = get(self._switch, 'rack')
                if rack is not None:
                    snmp_location = f"{snmp_location} {rack}"
                snmp_location = f"{snmp_location} {self._hostname}"
                snmp_server.update({'location': snmp_location})
            users = get(snmp_settings, 'users')
            if users is not None:
                snmp_server.update({'users': []})
                for user in users:
                    version = get(user, 'version')
                    user_dict = {
                        'name': get(user, 'name'),
                        'group': get(user, 'group'),
                        'version': version
                    }
                    compute_v3_user_localized_key = get(snmp_settings, 'compute_v3_user_localized_key')
                    if (
                            version == 'v3' and
                            compute_local_engineid is True and
                            compute_v3_user_localized_key is True
                    ):
                        user_dict.update({'localized': local_engine_id})

                    auth = get(user, 'auth')
                    auth_passphrase = get(user, 'auth_passphrase')
                    if (
                            version == 'v3' and
                            auth is not None and
                            auth_passphrase is not None
                    ):
                        user_dict.update({'auth': auth})
                        hash_filter = {}
                        if (
                                compute_local_engineid is True and
                                compute_v3_user_localized_key is True
                        ):
                            hash_filter.update({"passphrase": auth_passphrase, "auth": auth,
                                                "engine_id": local_engine_id})
                            user_dict.update({'auth_passphrase': hash_passphrase(hash_filter)})
                        else:
                            user_dict.update({'auth_passphrase': auth_passphrase})

                        priv = get(user, 'priv')
                        priv_passphrase = get(user, 'priv_passphrase')
                        if (
                            priv is not None and
                            priv_passphrase is not None
                        ):
                            user_dict.update({'priv': priv})
                            if (
                                    compute_local_engineid is True and
                                    compute_v3_user_localized_key is True
                            ):
                                hash_filter.update({"passphrase": priv_passphrase, "priv": priv})
                                user_dict.update({'priv_passphrase': hash_passphrase(hash_filter)})
                            else:
                                user_dict.update({'priv_passphrase': priv_passphrase})
                    snmp_server['users'].append(user_dict)
            return snmp_server
        return None

    @cached_property
    def spanning_tree(self):
        spanning_tree_root_super = get(self._switch, 'spanning_tree_root_super')
        spanning_tree_mode = get(self._switch, 'spanning_tree_mode')
        if spanning_tree_root_super is False or spanning_tree_mode is None:
            return None
        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree.update({'root_super': True})
        if spanning_tree_mode is not None:
            spanning_tree.update({'mode': spanning_tree_mode})
            if spanning_tree_mode == "mstp":
                spanning_tree.update({'mst_instances': {"0": {'priority': get(self._switch,
                                                                              'spanning_tree_priority', '32768')}}})
            elif spanning_tree_mode == "rapid-pvst":
                spanning_tree.update({'rapid_pvst_instances':
                                     {"1-4094": {'priority': get(self._switch, 'spanning_tree_priority',
                                                                 '32768')}}})
            elif spanning_tree_mode == "rstp":
                spanning_tree.update({'rstp_priority': get(self._switch, 'spanning_tree_priority', '32768')})
        return spanning_tree

    @cached_property
    def service_unsupported_transceiver(self):
        unsupported_transceiver = get(self._hostvars, 'unsupported_transceiver')
        if unsupported_transceiver is not None:
            return {'license_name': get(unsupported_transceiver, 'license_name'),
                    'license_key': get(unsupported_transceiver, 'license_key')}
        return None

    @cached_property
    def local_users(self):
        local_users = get(self._hostvars, 'local_users')
        if local_users is None:
            return None
        local_users = self._convert_dicts(local_users, 'name')
        local_users_dict = {}
        for local_user in self._natural_sort(local_users, 'name'):
            name = get(local_user, 'name')
            local_users_dict.update({name: {'privilege': get(local_user, 'privilege')}})
            role = get(local_user, 'role')
            sha512_password = get(local_user, 'sha512_password')
            no_password = get(local_user, 'no_password')
            ssh_key = get(local_user, 'ssh_key')
            if role is not None:
                local_users_dict[name].update({'role': role})
            if sha512_password is not None:
                local_users_dict[name].update({'sha512_password': sha512_password})
            elif no_password is not None:
                local_users_dict[name].update({'no_password': no_password})
            if ssh_key is not None:
                local_users_dict[name].update({'ssh_key': ssh_key})
        return local_users_dict

    @cached_property
    def clock(self):
        timezone = get(self._hostvars, 'timezone')
        if timezone is not None:
            return {'timezone': timezone}
        return None

    @cached_property
    def vrfs(self):
        return {self._mgmt_interface_vrf: {'ip_routing': get(self._hostvars, 'mgmt_vrf_routing')}}

    @cached_property
    def management_interfaces(self):
        mgmt_interface = get(self._switch, 'mgmt_interface')
        if (
                mgmt_interface is not None and
                self._mgmt_ip is not None and
                self._mgmt_interface_vrf is not None and
                self._mgmt_gateway is not None
        ):
            return {
                mgmt_interface: {
                    'description': 'oob_management',
                    'shutdown': False, 'vrf': self._mgmt_interface_vrf,
                    'ip_address': self._mgmt_ip, 'gateway': self._mgmt_gateway,
                    'type': 'oob'
                }
            }
        return None

    @cached_property
    def tcam_profile(self):
        tcam_profile = get(self._platform_settings, 'tcam_profile')
        if tcam_profile is not None:
            return {'system': tcam_profile}
        return None

    @cached_property
    def platform(self):
        lag_hardware_only = get(self._platform_settings, 'lag_hardware_only')
        platform = {}
        if lag_hardware_only is not None:
            platform.update({'sand': {'lag': {'hardware_only': lag_hardware_only}}})
        if (
                get(self._platform_settings, 'trident_forwarding_table_partition') is not None and
                get(self._switch, 'evpn_multicast') is True
        ):
            platform.update({'trident': {'forwarding_table_partition':
                            get(self._platform_settings, 'trident_forwarding_table_partition')}})
        if platform:
            return platform
        return None

    @cached_property
    def mac_address_table(self):
        mac_address_table = get(self._hostvars, 'mac_address_table')
        if mac_address_table is None or (aging_time := get(mac_address_table, 'aging_time')) is None:
            return None
        return {'aging_time': aging_time}

    @cached_property
    def queue_monitor_streaming(self):
        queue_monitor_streaming = get(self._hostvars, 'queue_monitor_streaming')
        if queue_monitor_streaming is None:
            return None
        enable = get(queue_monitor_streaming, 'enable')
        vrf = get(queue_monitor_streaming, 'vrf')
        if enable is True or vrf is not None:
            queue_monitor = {}
            if enable is True:
                queue_monitor.update({'enable': enable})
            if vrf is not None:
                queue_monitor.update({'vrf': vrf})
            return queue_monitor

    @cached_property
    def management_api_http(self):
        management_eapi = get(self._hostvars, 'management_eapi')
        if management_eapi is not None:
            management_api_http = {'enable_vrfs': {self._mgmt_interface_vrf: {}}}
            if get(management_eapi, 'enable_http') is not None:
                management_api_http.update({'enable_http': get(management_eapi, 'enable_http')})
            if get(management_eapi, 'enable_https') is not None:
                management_api_http.update({'enable_https': get(management_eapi, 'enable_https')})
            if get(management_eapi, 'default_services') is not None:
                management_api_http.update({'default_services': get(management_eapi, 'default_services')})
            return management_api_http
        return None

    @cached_property
    def link_tracking_groups(self):
        link_tracking_groups = get(self._switch, 'link_tracking_groups')
        if link_tracking_groups is not None:
            return link_tracking_groups
        return None

    @cached_property
    def lacp(self):
        lacp_port_id = get(self._switch, 'lacp_port_id')
        if lacp_port_id is None:
            return None

        begin = get(lacp_port_id, 'begin')
        end = get(lacp_port_id, 'end')
        if begin is not None and end is not None:
            return {
                'port_id':
                    {'range':
                        {'begin': begin,
                         'end': end,
                         }
                     }
            }

    @cached_property
    def eos_cli(self):
        raw_eos_cli = get(self._switch, 'raw_eos_cli')
        platform_raw_eos_cli = get(self._platform_settings, 'raw_eos_cli')
        if (
                raw_eos_cli is not None or
                platform_raw_eos_cli is not None
        ):
            eos_cli = ""
            if raw_eos_cli is not None:
                eos_cli = raw_eos_cli
            if platform_raw_eos_cli is not None:
                if eos_cli:
                    eos_cli = "\n".join([eos_cli, platform_raw_eos_cli])
                else:
                    eos_cli = platform_raw_eos_cli
            return eos_cli
        return None

    @cached_property
    def struct_cfg(self):
        struct_cfg = get(self._switch, 'struct_cfg')
        if struct_cfg is not None:
            return struct_cfg
        return None
