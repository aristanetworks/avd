from __future__ import annotations

from functools import cached_property
from hashlib import sha1

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.snmp_hash import hash_passphrase
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfigBase(AvdFacts):
    @cached_property
    def serial_number(self) -> str | None:
        """
        serial_number variable set based on serial_number fact
        """
        return self.shared_utils.serial_number

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        router_bgp set based on switch.bgp_as, switch.bgp_defaults, router_id facts
        and aggregating the values of bgp_maximum_paths and bgp_ecmp variables
        """
        if self.shared_utils.bgp_as is None:
            return None

        platform_bgp_update_wait_for_convergence = (
            get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_for_convergence", default=True) is True
        )
        platform_bgp_update_wait_install = get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_install", default=True) is True

        router_bgp = {
            "as": self.shared_utils.bgp_as,
            "router_id": self.shared_utils.router_id,
            "distance": get(self._hostvars, "bgp_distance"),
            "bgp_defaults": get(self.shared_utils.switch_data_combined, "bgp_defaults"),
            "bgp": {
                "default": {
                    "ipv4_unicast": get(self._hostvars, "bgp_default_ipv4_unicast", default=False),
                },
            },
            "maximum_paths": {
                "paths": get(self._hostvars, "bgp_maximum_paths", default=4),
                "ecmp": get(self._hostvars, "bgp_ecmp", default=4),
            },
        }
        if get(self._hostvars, "bgp_update_wait_for_convergence", default=False) is True and platform_bgp_update_wait_for_convergence:
            router_bgp.setdefault("updates", {})["wait_for_convergence"] = True

        if get(self._hostvars, "bgp_update_wait_install", default=True) is True and platform_bgp_update_wait_install:
            router_bgp.setdefault("updates", {})["wait_install"] = True

        if get(self._hostvars, "bgp_graceful_restart.enabled", default=True) is True:
            router_bgp.update(
                {
                    "graceful_restart": {
                        "enabled": True,
                        "restart_time": get(self._hostvars, "bgp_graceful_restart.restart_time", default=300),
                    },
                },
            )

        return strip_null_from_data(router_bgp)

    @cached_property
    def static_routes(self) -> list | None:
        """
        static_routes set based on mgmt_gateway, mgmt_destination_networks and mgmt_interface_vrf
        """
        if self.shared_utils.mgmt_gateway is None:
            return None

        static_routes = []
        if (mgmt_destination_networks := get(self._hostvars, "mgmt_destination_networks")) is not None:
            for mgmt_destination_network in mgmt_destination_networks:
                static_routes.append(
                    {
                        "vrf": self.shared_utils.mgmt_interface_vrf,
                        "destination_address_prefix": mgmt_destination_network,
                        "gateway": self.shared_utils.mgmt_gateway,
                    }
                )
        else:
            static_routes.append(
                {
                    "vrf": self.shared_utils.mgmt_interface_vrf,
                    "destination_address_prefix": "0.0.0.0/0",
                    "gateway": self.shared_utils.mgmt_gateway,
                }
            )

        return static_routes

    @cached_property
    def ipv6_static_routes(self) -> list | None:
        """
        ipv6_static_routes set based on ipv6_mgmt_gateway, ipv6_mgmt_destination_networks and mgmt_interface_vrf
        """
        if self.shared_utils.ipv6_mgmt_gateway is None or self.shared_utils.ipv6_mgmt_ip is None:
            return None

        ipv6_static_routes = []
        if (ipv6_mgmt_destination_networks := get(self._hostvars, "ipv6_mgmt_destination_networks")) is not None:
            for mgmt_destination_network in ipv6_mgmt_destination_networks:
                ipv6_static_routes.append(
                    {
                        "vrf": self.shared_utils.mgmt_interface_vrf,
                        "destination_address_prefix": mgmt_destination_network,
                        "gateway": self.shared_utils.ipv6_mgmt_gateway,
                    }
                )
        else:
            ipv6_static_routes.append(
                {
                    "vrf": self.shared_utils.mgmt_interface_vrf,
                    "destination_address_prefix": "::/0",
                    "gateway": self.shared_utils.ipv6_mgmt_gateway,
                }
            )

        return ipv6_static_routes

    @cached_property
    def service_routing_protocols_model(self) -> str:
        """
        service_routing_protocols_model set to 'multi-agent'
        """
        return "multi-agent"

    @cached_property
    def ip_routing(self) -> bool:
        """
        For l3 devices, configure ip routing unless ip_routing_ipv6_interfaces is True.
        For other devices only configure if "always_configure_ip_routing" is True.
        """
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.ip_routing_ipv6_interfaces is True:
            return None
        return True

    @cached_property
    def ipv6_unicast_routing(self) -> bool | None:
        """
        ipv6_unicast_routing set based on underlay_rfc5549 and underlay_ipv6
        """
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.shared_utils.underlay_rfc5549 or self.shared_utils.underlay_ipv6:
            return True
        return None

    @cached_property
    def ip_routing_ipv6_interfaces(self) -> bool | None:
        """
        ip_routing_ipv6_interfaces set based on underlay_rfc5549 variable
        """
        if not self.shared_utils.underlay_router and not self.shared_utils.always_configure_ip_routing:
            return None

        if self.shared_utils.underlay_rfc5549:
            return True
        return None

    @cached_property
    def router_multicast(self) -> dict | None:
        """
        router_multicast set based on underlay_multicast, underlay_router
        and switch.evpn_multicast facts
        """
        if not self.shared_utils.underlay_multicast:
            return None

        router_multicast = {"ipv4": {"routing": True}}
        if get(self._hostvars, "switch.evpn_multicast") is True:
            router_multicast["ipv4"]["software_forwarding"] = "sfe"

        return router_multicast

    @cached_property
    def hardware_counters(self) -> dict | None:
        """
        hardware_counters set based on hardware_counters.features variable
        """
        return get(self._hostvars, "hardware_counters")

    @cached_property
    def hardware(self) -> dict | None:
        """
        hardware set based on platform_speed_groups variable and switch.platform fact.
        Converting nested dict to list of dict to support avd_v4.0
        """
        platform_speed_groups = get(self._hostvars, "platform_speed_groups")
        switch_platform = self.shared_utils.platform
        if platform_speed_groups is None or switch_platform is None:
            return None

        tmp_speed_groups = {}
        # converting nested dict to list of dict to support avd_v4.0
        platform_speed_groups = convert_dicts(platform_speed_groups, "platform", "speeds")
        for platform_item in platform_speed_groups:
            if platform_item["platform"] == switch_platform:
                # converting nested dict to list of dict to support avd_v4.0
                speeds = convert_dicts(platform_item.get("speeds"), "speed", "speed_groups")
                for speed in natural_sort(speeds, "speed"):
                    for speed_group in speed["speed_groups"]:
                        tmp_speed_groups[speed_group] = speed["speed"]

        if tmp_speed_groups:
            hardware = {"speed_groups": []}
            for speed_group in natural_sort(tmp_speed_groups):
                hardware["speed_groups"].append({"speed_group": speed_group, "serdes": tmp_speed_groups[speed_group]})
            return hardware

    @cached_property
    def daemon_terminattr(self) -> dict | None:
        """
        daemon_terminattr set based on cvp_instance_ip and cvp_instance_ips variables

        Updating cvaddrs and cvauth considering conditions for cvaas and cvp_on_prem IPs

            if 'arista.io' in cvp_instance_ip:
                 <updating as cvaas_ip>
            else:
                 <updating as cvp_on_prem ip>
        """
        cvp_instance_ip = get(self._hostvars, "cvp_instance_ip")
        cvp_instance_ip_list = get(self._hostvars, "cvp_instance_ips", [])
        if cvp_instance_ip is not None:
            cvp_instance_ip_list.append(cvp_instance_ip)
        if not cvp_instance_ip_list:
            return None

        daemon_terminattr = {"cvaddrs": []}
        for cvp_instance_ip in cvp_instance_ip_list:
            if "arista.io" in cvp_instance_ip:
                # updating for cvaas_ips
                daemon_terminattr["cvaddrs"].append(f"{cvp_instance_ip}:443")
                daemon_terminattr["cvauth"] = {
                    "method": "token-secure",
                    "token_file": get(self._hostvars, "cvp_token_file", "/tmp/cv-onboarding-token"),
                }
            else:
                # updating for cvp_on_prem_ips
                cv_address = f"{cvp_instance_ip}:{get(self._hostvars, 'terminattr_ingestgrpcurl_port', default=9910)}"
                daemon_terminattr["cvaddrs"].append(cv_address)
                if (cvp_ingestauth_key := get(self._hostvars, "cvp_ingestauth_key")) is not None:
                    daemon_terminattr["cvauth"] = {
                        "method": "key",
                        "key": cvp_ingestauth_key,
                    }
                else:
                    daemon_terminattr["cvauth"] = {
                        "method": "token",
                        "token_file": get(self._hostvars, "cvp_token_file", "/tmp/token"),
                    }

        daemon_terminattr["cvvrf"] = self.shared_utils.mgmt_interface_vrf
        daemon_terminattr["smashexcludes"] = get(self._hostvars, "terminattr_smashexcludes", default="ale,flexCounter,hardware,kni,pulse,strata")
        daemon_terminattr["ingestexclude"] = get(self._hostvars, "terminattr_ingestexclude", default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent")
        daemon_terminattr["disable_aaa"] = get(self._hostvars, "terminattr_disable_aaa", False)

        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self) -> dict:
        """
        vlan_internal_order set based on internal_vlan_order data-model
        """
        DEFAULT_INTERNAL_VLAN_ORDER = {
            "allocation": "ascending",
            "range": {
                "beginning": 1006,
                "ending": 1199,
            },
        }
        return get(self._hostvars, "internal_vlan_order", default=DEFAULT_INTERNAL_VLAN_ORDER)

    @cached_property
    def event_monitor(self) -> dict | None:
        """
        event_monitor set based on event_monitor data-model
        """
        if get(self._hostvars, "event_monitor") is True:
            return {"enabled": "true"}
        return None

    @cached_property
    def event_handlers(self) -> list | None:
        """
        event_handlers set based on event_handlers data-model
        """
        return get(self._hostvars, "event_handlers")

    @cached_property
    def load_interval(self) -> dict | None:
        """
        load_interval set based on load_interval_default variable
        """
        if (load_interval_default := get(self._hostvars, "load_interval_default")) is not None:
            return {"default": load_interval_default}
        return None

    @cached_property
    def queue_monitor_length(self) -> dict | None:
        """
        queue_monitor_length set based on queue_monitor_length data-model and
        platform_settings.feature_support.queue_monitor_length_notify fact
        """
        if (queue_monitor_length := get(self._hostvars, "queue_monitor_length")) is None:
            return None

        # Remove notifying key if not supported by the platform settings.
        if not self.shared_utils.platform_settings_feature_support_queue_monitor_length_notify:
            queue_monitor_length.pop("notifying", None)

        return queue_monitor_length

    @cached_property
    def ip_name_servers(self) -> list | None:
        """
        ip_name_servers set based on name_servers data-model and mgmt_interface_vrf
        """
        ip_name_servers = [
            {
                "ip_address": name_server,
                "vrf": self.shared_utils.mgmt_interface_vrf,
            }
            for name_server in get(self._hostvars, "name_servers", default=[])
        ]
        if ip_name_servers:
            return ip_name_servers

        return None

    @cached_property
    def redundancy(self) -> dict | None:
        """
        redundancy set based on redundancy data-model
        """
        if get(self._hostvars, "redundancy") is not None:
            return {"protocol": get(self._hostvars, "redundancy.protocol")}
        return None

    @cached_property
    def snmp_server(self) -> dict | None:
        """
        snmp_server set based on snmp_settings data-model, using various snmp_settings information.

        if snmp_settings.compute_local_engineid is True we will use sha1 to create a
        unique local_engine_id value based on hostname and mgmt_ip facts.

        If user.version is set to 'v3', compute_local_engineid and compute_v3_user_localized_key are set to 'True'
        we will use hash_passphrase filter to create an instance of hashlib._hashlib.HASH corresponding to the auth_type
        value based on various snmp_settings.users information.
        """
        if (snmp_settings := get(self._hostvars, "snmp_settings")) is None:
            return None

        snmp_server = {}

        local_engine_id = None

        if snmp_settings.get("compute_local_engineid") is True:
            compute_source = get(snmp_settings, "compute_local_engineid_source", default="hostname_and_ip")
            if compute_source == "hostname_and_ip":
                local_engine_id = sha1(f"{self.shared_utils.hostname}{self.shared_utils.mgmt_ip}".encode("utf-8")).hexdigest()
            elif compute_source == "system_mac":
                if self.shared_utils.system_mac_address is None:
                    raise AristaAvdMissingVariableError("default_engine_id_from_system_mac: true requires system_mac_address to be set!")
                # the default engine id on switches is derived as per the following formula
                local_engine_id = f"f5717f{str(self.shared_utils.system_mac_address).replace(':', '').lower()}00"
            else:
                # Unknown mode
                raise AristaAvdError(
                    f"'{compute_source}' is not a valid value to compute the engine ID, accepted values are 'hostname_and_ip' and 'system_mac'"
                )

            snmp_server["engine_ids"] = {"local": local_engine_id}

        if (contact := snmp_settings.get("contact")) is not None:
            snmp_server["contact"] = contact

        if snmp_settings.get("location") is not None:
            location_elements = [
                get(self._hostvars, "fabric_name"),
                self.shared_utils.dc_name,
                self.shared_utils.pod_name,
                get(self.shared_utils.switch_data_combined, "rack"),
                self.shared_utils.hostname,
            ]
            location_elements = [location for location in location_elements if location is not None]
            snmp_location = " ".join(location_elements)
            snmp_server["location"] = snmp_location

        users = snmp_settings.get("users")
        if users is not None:
            snmp_server["users"] = []
            for user in users:
                version = get(user, "version")
                user_dict = {"name": get(user, "name"), "group": get(user, "group"), "version": version}
                compute_v3_user_localized_key = snmp_settings.get("compute_v3_user_localized_key")
                if version == "v3":
                    if local_engine_id is not None and compute_v3_user_localized_key is True:
                        user_dict["localized"] = local_engine_id

                    auth = user.get("auth")
                    auth_passphrase = user.get("auth_passphrase")
                    if auth is not None and auth_passphrase is not None:
                        user_dict["auth"] = auth
                        if local_engine_id is not None and compute_v3_user_localized_key is True:
                            hash_filter = {"passphrase": auth_passphrase, "auth": auth, "engine_id": local_engine_id}
                            user_dict["auth_passphrase"] = hash_passphrase(hash_filter)
                        else:
                            user_dict["auth_passphrase"] = auth_passphrase

                        priv = user.get("priv")
                        priv_passphrase = user.get("priv_passphrase")
                        if priv is not None and priv_passphrase is not None:
                            user_dict["priv"] = priv
                            if local_engine_id is not None and compute_v3_user_localized_key is True:
                                hash_filter.update({"passphrase": priv_passphrase, "priv": priv})
                                user_dict["priv_passphrase"] = hash_passphrase(hash_filter)
                            else:
                                user_dict["priv_passphrase"] = priv_passphrase
                snmp_server["users"].append(user_dict)

        return snmp_server

    @cached_property
    def spanning_tree(self) -> dict | None:
        """
        spanning_tree set based on spanning_tree_root_super, spanning_tree_mode
        and spanning_tree_priority
        """
        if not self.shared_utils.network_services_l2:
            return {"mode": "none"}

        spanning_tree_root_super = get(self.shared_utils.switch_data_combined, "spanning_tree_root_super")
        spanning_tree_mode = get(self.shared_utils.switch_data_combined, "spanning_tree_mode")
        if spanning_tree_root_super is not True and spanning_tree_mode is None:
            return None

        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree["root_super"] = True

        if spanning_tree_mode is not None:
            spanning_tree["mode"] = spanning_tree_mode
            priority = get(self.shared_utils.switch_data_combined, "spanning_tree_priority", default="32768")
            if spanning_tree_mode == "mstp":
                spanning_tree["mst_instances"] = [{"id": "0", "priority": priority}]
            elif spanning_tree_mode == "rapid-pvst":
                spanning_tree["rapid_pvst_instances"] = [{"id": "1-4094", "priority": priority}]
            elif spanning_tree_mode == "rstp":
                spanning_tree["rstp_priority"] = priority

        return spanning_tree

    @cached_property
    def service_unsupported_transceiver(self) -> dict | None:
        """
        service_unsupported_transceiver based on unsupported_transceiver data-model
        """
        if (unsupported_transceiver := get(self._hostvars, "unsupported_transceiver")) is not None:
            return {"license_name": unsupported_transceiver.get("license_name"), "license_key": unsupported_transceiver.get("license_key")}

        return None

    @cached_property
    def local_users(self) -> list | None:
        """
        local_users set based on local_users data model
        """
        if (local_users := get(self._hostvars, "local_users")) is None:
            return None

        return natural_sort(convert_dicts(local_users, "name"), "name")

    @cached_property
    def clock(self) -> dict | None:
        """
        clock set based on timezone variable
        """
        if (timezone := get(self._hostvars, "timezone")) is not None:
            return {"timezone": timezone}
        return None

    @cached_property
    def vrfs(self) -> list:
        """
        vrfs set based on mgmt_interface_vrf variable
        """
        mgmt_vrf_routing = get(self._hostvars, "mgmt_vrf_routing", default=False)
        vrf_settings = {
            "name": self.shared_utils.mgmt_interface_vrf,
            "ip_routing": mgmt_vrf_routing,
        }
        if self.shared_utils.ipv6_mgmt_ip is not None:
            vrf_settings["ipv6_routing"] = mgmt_vrf_routing
        return [vrf_settings]

    @cached_property
    def management_interfaces(self) -> list | None:
        """
        management_interfaces set based on mgmt_interface, mgmt_ip, ipv6_mgmt_ip facts,
        mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables
        """
        mgmt_interface = self.shared_utils.mgmt_interface
        if (
            mgmt_interface is not None
            and self.shared_utils.mgmt_interface_vrf is not None
            and (self.shared_utils.mgmt_ip is not None or self.shared_utils.ipv6_mgmt_ip is not None)
        ):
            interface_settings = {
                "name": mgmt_interface,
                "description": get(self._hostvars, "mgmt_interface_description", default="oob_management"),
                "shutdown": False,
                "vrf": self.shared_utils.mgmt_interface_vrf,
                "ip_address": self.shared_utils.mgmt_ip,
                "gateway": self.shared_utils.mgmt_gateway,
                "type": "oob",
            }
            """
            inserting ipv6 variables if ipv6_mgmt_ip is set
            """
            if self.shared_utils.ipv6_mgmt_ip is not None:
                interface_settings.update(
                    {
                        "ipv6_enable": True,
                        "ipv6_address": self.shared_utils.ipv6_mgmt_ip,
                        "ipv6_gateway": self.shared_utils.ipv6_mgmt_gateway,
                    }
                )

            return [interface_settings]

        return None

    @cached_property
    def tcam_profile(self) -> dict | None:
        """
        tcam_profile set based on platform_settings.tcam_profile fact
        """
        if (tcam_profile := get(self.shared_utils.platform_settings, "tcam_profile")) is not None:
            return {"system": tcam_profile}
        return None

    @cached_property
    def platform(self) -> dict | None:
        """
        platform set based on platform_settings.lag_hardware_only,
        platform_settings.trident_forwarding_table_partition and switch.evpn_multicast facts
        """
        platform = {}
        if (lag_hardware_only := get(self.shared_utils.platform_settings, "lag_hardware_only")) is not None:
            platform["sand"] = {"lag": {"hardware_only": lag_hardware_only}}

        trident_forwarding_table_partition = get(self.shared_utils.platform_settings, "trident_forwarding_table_partition")
        if trident_forwarding_table_partition is not None and get(self._hostvars, "switch.evpn_multicast") is True:
            platform["trident"] = {"forwarding_table_partition": trident_forwarding_table_partition}

        if platform:
            return platform
        return None

    @cached_property
    def mac_address_table(self) -> dict | None:
        """
        mac_address_table set based on mac_address_table data-model
        """
        if (aging_time := get(self._hostvars, "mac_address_table.aging_time")) is not None:
            return {"aging_time": aging_time}
        return None

    @cached_property
    def queue_monitor_streaming(self) -> dict | None:
        """
        queue_monitor_streaming set based on queue_monitor_streaming data-model
        """
        enable = get(self._hostvars, "queue_monitor_streaming.enable")
        vrf = get(self._hostvars, "queue_monitor_streaming.vrf")
        if enable is not True or vrf is None:
            return None

        queue_monitor = {}
        if enable is True:
            queue_monitor["enable"] = enable

        if vrf is not None:
            queue_monitor["vrf"] = vrf

        return queue_monitor

    @cached_property
    def management_api_http(self) -> dict | None:
        """
        management_api_http set based on management_eapi data-model
        """
        if (management_eapi := get(self._hostvars, "management_eapi", default={"enable_https": True})) is None:
            return None

        management_api_http = {"enable_vrfs": [{"name": self.shared_utils.mgmt_interface_vrf}]}
        management_api = management_eapi.fromkeys(["enable_http", "enable_https", "default_services"])
        for key in dict(management_api).keys():
            if (value := management_eapi.get(key)) is not None:
                management_api[key] = value
            else:
                del management_api[key]

        management_api_http.update(management_api)
        return management_api_http

    @cached_property
    def link_tracking_groups(self) -> list | None:
        """
        link_tracking_groups
        """
        return self.shared_utils.link_tracking_groups

    @cached_property
    def lacp(self) -> dict | None:
        """
        lacp set based on lacp_port_id_range
        """
        lacp_port_id_range = get(self.shared_utils.switch_data_combined, "lacp_port_id_range", default={})
        if lacp_port_id_range.get("enabled") is not True:
            return None

        if (switch_id := self.shared_utils.id) is None:
            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.shared_utils.hostname}' to set LACP port ID ranges")

        node_group_length = max(len(self.shared_utils.switch_data_node_group_nodes), 1)
        port_range = int(get(lacp_port_id_range, "size", default=128))
        port_offset = int(get(lacp_port_id_range, "offset", default=0))

        begin = 1 + (((switch_id - 1) % node_group_length) * port_range) + port_offset
        end = (((switch_id - 1) % node_group_length + 1) * port_range) + port_offset

        return {
            "port_id": {
                "range": {
                    "begin": begin,
                    "end": end,
                }
            }
        }

    @cached_property
    def ptp(self) -> dict | None:
        """
        Generates PTP config on node level as well as for interfaces, using various defaults.
        - The following are set in default node_type_keys for design "l3ls-evpn":
                spine:
                  default_ptp_priority1: 20
                l3leaf:
                  default_ptp_priority1: 30
        PTP priority2 is set in the code below, calculated based on the node id:
            default_priority2 = self.id % 256
        """
        if not self.shared_utils.ptp_enabled:
            return None

        default_ptp_domain = get(self._hostvars, "ptp.domain", default=127)
        default_ptp_priority1 = get(self.shared_utils.node_type_key_data, "default_ptp_priority1", default=127)
        default_clock_identity = None

        priority1 = get(self.shared_utils.switch_data_combined, "ptp.priority1", default=default_ptp_priority1)
        priority2 = get(self.shared_utils.switch_data_combined, "ptp.priority2")
        if priority2 is None:
            if self.shared_utils.id is None:
                raise AristaAvdMissingVariableError(f"'id' must be set on '{self.shared_utils.hostname}' to set ptp priority2")

            priority2 = self.shared_utils.id % 256

        if get(self.shared_utils.switch_data_combined, "ptp.auto_clock_identity", default=True) is True:
            clock_identity_prefix = get(self.shared_utils.switch_data_combined, "ptp.clock_identity_prefix", default="00:1C:73")
            default_clock_identity = f"{clock_identity_prefix}:{priority1:02x}:00:{priority2:02x}"

        ptp = {
            "mode": get(self.shared_utils.switch_data_combined, "ptp.mode", default="boundary"),
            "forward_unicast": get(self.shared_utils.switch_data_combined, "ptp.forward_unicast"),
            "clock_identity": get(self.shared_utils.switch_data_combined, "ptp.clock_identity", default=default_clock_identity),
            "source": {"ip": get(self.shared_utils.switch_data_combined, "ptp.source_ip")},
            "priority1": priority1,
            "priority2": priority2,
            "ttl": get(self.shared_utils.switch_data_combined, "ptp.ttl"),
            "domain": get(self.shared_utils.switch_data_combined, "ptp.domain", default=default_ptp_domain),
            "message_type": {
                "general": {
                    "dscp": get(self.shared_utils.switch_data_combined, "ptp.dscp.general_messages"),
                },
                "event": {
                    "dscp": get(self.shared_utils.switch_data_combined, "ptp.dscp.event_messages"),
                },
            },
            "monitor": {
                "enabled": get(self.shared_utils.switch_data_combined, "ptp.monitor.enabled", default=True),
                "threshold": {
                    "offset_from_master": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.offset_from_master", default=250),
                    "mean_path_delay": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.mean_path_delay", default=1500),
                    "drop": {
                        "offset_from_master": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.drop.offset_from_master"),
                        "mean_path_delay": get(self.shared_utils.switch_data_combined, "ptp.monitor.threshold.drop.mean_path_delay"),
                    },
                },
                "missing_message": {
                    "intervals": {
                        "announce": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.announce"),
                        "follow_up": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.follow_up"),
                        "sync": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.intervals.sync"),
                    },
                    "sequence_ids": {
                        "enabled": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.enabled", default=True),
                        "announce": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.announce", default=3),
                        "delay_resp": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.delay_resp", default=3),
                        "follow_up": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.follow_up", default=3),
                        "sync": get(self.shared_utils.switch_data_combined, "ptp.monitor.missing_message.sequence_ids.sync", default=3),
                    },
                },
            },
        }
        ptp = strip_null_from_data(ptp, (None, {}))
        return ptp

    @cached_property
    def eos_cli(self) -> str | None:
        """
        Aggregate the values of raw_eos_cli and platform_settings.platform_raw_eos_cli facts
        """
        raw_eos_cli = get(self.shared_utils.switch_data_combined, "raw_eos_cli")
        platform_raw_eos_cli = get(self.shared_utils.platform_settings, "raw_eos_cli")
        if raw_eos_cli is not None or platform_raw_eos_cli is not None:
            return "\n".join(filter(None, [raw_eos_cli, platform_raw_eos_cli]))
        return None
