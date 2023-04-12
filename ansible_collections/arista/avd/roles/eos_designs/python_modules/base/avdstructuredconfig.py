from __future__ import annotations

from functools import cached_property
from hashlib import sha1

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.snmp_hash import hash_passphrase
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdStructuredConfig(AvdFacts):
    @cached_property
    def _mgmt_interface_vrf(self) -> str | None:
        """
        Returns the value for mgmt_interface_vrf variable used in static_routes, name_Server,
        vrfs and management_interfaces data-models
        """
        return get(self._hostvars, "mgmt_interface_vrf")

    @cached_property
    def _mgmt_gateway(self) -> str | None:
        """
        Returns the value for mgmt_gateway variable used in static_routes and management_interfaces data-models
        """
        return get(self._hostvars, "mgmt_gateway")

    @cached_property
    def _ipv6_mgmt_gateway(self) -> str | None:
        """
        Returns the value for ipv6_mgmt_gateway variable used in ipv6_static_routes and management_interfaces data-models
        """
        return get(self._hostvars, "ipv6_mgmt_gateway")

    @cached_property
    def _platform_settings(self) -> list:
        """
        Returns the value for switch.platform_settings fact used in queue_monitor_length, tcam_profile, platform
        and eos_cli data-models
        """
        return get(self._hostvars, "switch.platform_settings")

    @cached_property
    def _mgmt_ip(self) -> str | None:
        """
        Returns the value for switch.mgmt_ip fact used in snmp_server and management_interfaces data-models
        """
        return get(self._hostvars, "switch.mgmt_ip")

    @cached_property
    def _ipv6_mgmt_ip(self) -> str | None:
        """
        Returns the value for switch.ipv6_mgmt_ip fact used in management_interfaces data-models
        """
        return get(self._hostvars, "switch.ipv6_mgmt_ip")

    @cached_property
    def _hostname(self) -> str | None:
        """
        hostname variable set based on switch.hostname fact
        """
        return get(self._hostvars, "switch.hostname", required=True)

    @cached_property
    def _system_mac_address(self) -> str | None:
        """
        system_mac_address variable set based on switch.system_mac_address fact
        """
        return get(self._hostvars, "switch.system_mac_address")

    @cached_property
    def _underlay_router(self) -> bool:
        return get(self._hostvars, "switch.underlay_router") is True

    @cached_property
    def _always_configure_ip_routing(self) -> bool:
        return get(self._hostvars, "switch.always_configure_ip_routing")

    @cached_property
    def serial_number(self) -> str | None:
        """
        serial_number variable set based on switch.serial_number fact
        """
        return get(self._hostvars, "switch.serial_number")

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        router_bgp set based on switch.bgp_as, switch.bgp_defaults, switch.router_id facts
        and aggregating the values of bgp_maximum_paths and bgp_ecmp variables
        """
        if (bgp_as := get(self._hostvars, "switch.bgp_as")) is None:
            return None

        bgp_defaults = get(self._hostvars, "switch.bgp_defaults")
        if (bgp_maximum_paths := get(self._hostvars, "bgp_maximum_paths")) is not None:
            max_paths_str = f"maximum-paths {bgp_maximum_paths}"
            if (bgp_ecmp := get(self._hostvars, "bgp_ecmp")) is not None:
                max_paths_str += f" ecmp {bgp_ecmp}"
            bgp_defaults.append(max_paths_str)

        return {
            "as": bgp_as,
            "router_id": get(self._hostvars, "switch.router_id"),
            "bgp_defaults": bgp_defaults,
        }

    @cached_property
    def static_routes(self) -> list | None:
        """
        static_routes set based on mgmt_gateway, mgmt_destination_networks and mgmt_interface_vrf
        """
        if self._mgmt_gateway is None:
            return None

        static_routes = []
        if (mgmt_destination_networks := get(self._hostvars, "mgmt_destination_networks")) is not None:
            for mgmt_destination_network in mgmt_destination_networks:
                static_routes.append(
                    {
                        "vrf": self._mgmt_interface_vrf,
                        "destination_address_prefix": mgmt_destination_network,
                        "gateway": self._mgmt_gateway,
                    }
                )
        else:
            static_routes.append(
                {
                    "vrf": self._mgmt_interface_vrf,
                    "destination_address_prefix": "0.0.0.0/0",
                    "gateway": self._mgmt_gateway,
                }
            )

        return static_routes

    @cached_property
    def ipv6_static_routes(self) -> list | None:
        """
        ipv6_static_routes set based on ipv6_mgmt_gateway, ipv6_mgmt_destination_networks and mgmt_interface_vrf
        """
        if self._ipv6_mgmt_gateway is None or self._ipv6_mgmt_ip is None:
            return None

        ipv6_static_routes = []
        if (ipv6_mgmt_destination_networks := get(self._hostvars, "ipv6_mgmt_destination_networks")) is not None:
            for mgmt_destination_network in ipv6_mgmt_destination_networks:
                ipv6_static_routes.append(
                    {
                        "vrf": self._mgmt_interface_vrf,
                        "destination_address_prefix": mgmt_destination_network,
                        "gateway": self._ipv6_mgmt_gateway,
                    }
                )
        else:
            ipv6_static_routes.append(
                {
                    "vrf": self._mgmt_interface_vrf,
                    "destination_address_prefix": "::/0",
                    "gateway": self._ipv6_mgmt_gateway,
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
        if not self._underlay_router and not self._always_configure_ip_routing:
            return None

        if self.ip_routing_ipv6_interfaces is True:
            return None
        return True

    @cached_property
    def ipv6_unicast_routing(self) -> bool | None:
        """
        ipv6_unicast_routing set based on underlay_rfc5549 and switch.underlay_ipv6
        """
        if not self._underlay_router and not self._always_configure_ip_routing:
            return None

        if get(self._hostvars, "underlay_rfc5549") is True or get(self._hostvars, "switch.underlay_ipv6") is True:
            return True
        return None

    @cached_property
    def ip_routing_ipv6_interfaces(self) -> bool | None:
        """
        ip_routing_ipv6_interfaces set based on underlay_rfc5549 variable
        """
        if not self._underlay_router and not self._always_configure_ip_routing:
            return None

        if get(self._hostvars, "underlay_rfc5549") is True:
            return True
        return None

    @cached_property
    def router_multicast(self) -> dict | None:
        """
        router_multicast set based on switch.underlay_multicast, switch.underlay_router
        and switch.evpn_multicast facts
        """
        if get(self._hostvars, "switch.underlay_multicast") is not True:
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
        switch_platform = get(self._hostvars, "switch.platform")
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
                cv_address = f"{cvp_instance_ip}:{get(self._hostvars, 'terminattr_ingestgrpcurl_port')}"
                daemon_terminattr["cvaddrs"].append(cv_address)
                if (cvp_ingestauth_key := get(self._hostvars, "cvp_ingestauth_key")) is not None:
                    daemon_terminattr["cvauth"] = {
                        "method": "key",
                        "key": cvp_ingestauth_key,
                    }
                else:
                    daemon_terminattr["cvauth"] = {
                        "method": "token-secure",
                        "token_file": get(self._hostvars, "cvp_token_file", "/tmp/cv-onboarding-token"),
                    }

        daemon_terminattr["cvvrf"] = self._mgmt_interface_vrf
        daemon_terminattr["smashexcludes"] = get(self._hostvars, "terminattr_smashexcludes")
        daemon_terminattr["ingestexclude"] = get(self._hostvars, "terminattr_ingestexclude")
        daemon_terminattr["disable_aaa"] = get(self._hostvars, "terminattr_disable_aaa", False)

        return daemon_terminattr

    @cached_property
    def vlan_internal_order(self) -> dict:
        """
        vlan_internal_order set based on internal_vlan_order data-model
        """
        return {
            "allocation": get(self._hostvars, "internal_vlan_order.allocation"),
            "range": {
                "beginning": get(self._hostvars, "internal_vlan_order.range.beginning"),
                "ending": get(self._hostvars, "internal_vlan_order.range.ending"),
            },
        }

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
        switch.feature_support.queue_monitor_length_notify fact
        """
        if (queue_monitor_length := get(self._hostvars, "queue_monitor_length")) is None:
            return None

        queue_monitor_length_dict = {"enabled": True}
        queue_monitor_length_notifying = get(queue_monitor_length, "notifying")
        notify_supported = get(self._platform_settings, "feature_support.queue_monitor_length_notify")
        if queue_monitor_length_notifying is not None and notify_supported is not False:
            queue_monitor_length_dict["notifying"] = queue_monitor_length_notifying

        if get(queue_monitor_length, "log") is not None:
            queue_monitor_length_dict["log"] = queue_monitor_length.get("log")

        return queue_monitor_length_dict

    @cached_property
    def name_server(self) -> dict | None:
        """
        name_server set based on name_servers data-model and mgmt_interface_vrf
        """
        if (name_servers := get(self._hostvars, "name_servers")) is not None:
            return {"source": {"vrf": self._mgmt_interface_vrf}, "nodes": name_servers}

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
        unique local_engine_id value based on switch.hostname and switch.mgmt_ip facts.

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
                local_engine_id = sha1(f"{self._hostname}{self._mgmt_ip}".encode("utf-8")).hexdigest()
            elif compute_source == "system_mac":
                if self._system_mac_address is None:
                    raise AristaAvdMissingVariableError("default_engine_id_from_system_mac: true requires system_mac_address to be set!")
                # the default engine id on switches is derived as per the following formula
                local_engine_id = f"f5717f{str(self._system_mac_address).replace(':', '').lower()}00"
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
                get(self._hostvars, "dc_name"),
                get(self._hostvars, "pod_name"),
                get(self._hostvars, "switch.rack"),
                self._hostname,
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
        spanning_tree set based on switch.spanning_tree_root_super, switch.spanning_tree_mode
        and switch.spanning_tree_priority facts
        """
        spanning_tree_root_super = get(self._hostvars, "switch.spanning_tree_root_super")
        spanning_tree_mode = get(self._hostvars, "switch.spanning_tree_mode")
        if spanning_tree_root_super is not True and spanning_tree_mode is None:
            return None

        spanning_tree = {}
        if spanning_tree_root_super is True:
            spanning_tree["root_super"] = True

        if spanning_tree_mode is not None:
            spanning_tree["mode"] = spanning_tree_mode
            priority = get(self._hostvars, "switch.spanning_tree_priority", "32768")
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
        local_users set based on various information from local_users data-model
        """
        if (local_users := get(self._hostvars, "local_users")) is None:
            return None

        local_users = convert_dicts(local_users, "name")
        local_users_list = []
        for local_user in natural_sort(local_users, "name"):
            name = local_user.get("name")
            if local_user.get("disabled") is True:
                local_users_list.append({"name": name, "disabled": True})
                continue

            local_users_dict = {"name": name, "privilege": get(local_user, "privilege")}
            if (role := local_user.get("role")) is not None:
                local_users_dict["role"] = role

            if (sha512_password := local_user.get("sha512_password")) is not None:
                local_users_dict["sha512_password"] = sha512_password
            elif (no_password := local_user.get("no_password")) is not None:
                local_users_dict["no_password"] = no_password

            if (ssh_key := local_user.get("ssh_key")) is not None:
                local_users_dict["ssh_key"] = ssh_key

            local_users_list.append(local_users_dict)

        return local_users_list

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
        vrf_settings = {
            "name": self._mgmt_interface_vrf,
            "ip_routing": get(self._hostvars, "mgmt_vrf_routing"),
        }
        if self._ipv6_mgmt_ip is not None:
            vrf_settings["ipv6_routing"] = get(self._hostvars, "mgmt_vrf_routing")
        return [vrf_settings]

    @cached_property
    def management_interfaces(self) -> list | None:
        """
        management_interfaces set based on switch.mgmt_interface, switch.mgmt_ip, switch.ipv6_mgmt_ip facts,
        mgmt_gateway, ipv6_mgmt_gateway and mgmt_interface_vrf variables
        """
        mgmt_interface = get(self._hostvars, "switch.mgmt_interface")
        if mgmt_interface is not None and self._mgmt_interface_vrf is not None and (self._mgmt_ip is not None or self._ipv6_mgmt_ip is not None):
            interface_settings = {
                "name": mgmt_interface,
                "description": get(self._hostvars, "mgmt_interface_description", default="oob_management"),
                "shutdown": False,
                "vrf": self._mgmt_interface_vrf,
                "ip_address": self._mgmt_ip,
                "gateway": self._mgmt_gateway,
                "type": "oob",
            }
            """
            inserting ipv6 variables if self._ipv6_mgmt_ip is set
            """
            if self._ipv6_mgmt_ip is not None:
                interface_settings.update(
                    {
                        "ipv6_enable": True,
                        "ipv6_address": self._ipv6_mgmt_ip,
                        "ipv6_gateway": self._ipv6_mgmt_gateway,
                    }
                )

            return [interface_settings]

        return None

    @cached_property
    def tcam_profile(self) -> dict | None:
        """
        tcam_profile set based on switch.platform_settings.tcam_profile fact
        """
        if (tcam_profile := get(self._platform_settings, "tcam_profile")) is not None:
            return {"system": tcam_profile}
        return None

    @cached_property
    def platform(self) -> dict | None:
        """
        platform set based on switch.platform_settings.lag_hardware_only,
        switch.platform_settings.trident_forwarding_table_partition and switch.evpn_multicast facts
        """
        platform = {}
        if (lag_hardware_only := get(self._platform_settings, "lag_hardware_only")) is not None:
            platform["sand"] = {"lag": {"hardware_only": lag_hardware_only}}

        trident_forwarding_table_partition = get(self._platform_settings, "trident_forwarding_table_partition")
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
        if (management_eapi := get(self._hostvars, "management_eapi")) is None:
            return None

        management_api_http = {"enable_vrfs": [{"name": self._mgmt_interface_vrf}]}
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
        link_tracking_groups set based on switch.link_tracking_groups fact
        """
        if (link_tracking_groups := get(self._hostvars, "switch.link_tracking_groups")) is not None:
            return link_tracking_groups
        return None

    @cached_property
    def lacp(self) -> dict | None:
        """
        lacp set based on switch.lacp_port_id fact
        """

        begin = get(self._hostvars, "switch.lacp_port_id.begin")
        end = get(self._hostvars, "switch.lacp_port_id.end")
        if begin is not None and end is not None:
            return {
                "port_id": {
                    "range": {
                        "begin": begin,
                        "end": end,
                    }
                }
            }

        return None

    @cached_property
    def ptp(self) -> dict | None:
        """
        ptp set to contents of switch.ptp.device_config if switch.ptp.enabled is True
        """
        if get(self._hostvars, "switch.ptp.enabled") is True:
            return get(self._hostvars, "switch.ptp.device_config")
        return None

    @cached_property
    def eos_cli(self) -> str | None:
        """
        Aggregate the values of switch.raw_eos_cli and switch.platform_settings.platform_raw_eos_cli facts
        """
        raw_eos_cli = get(self._hostvars, "switch.raw_eos_cli")
        platform_raw_eos_cli = get(self._platform_settings, "raw_eos_cli")
        if raw_eos_cli is not None or platform_raw_eos_cli is not None:
            return "\n".join(filter(None, [raw_eos_cli, platform_raw_eos_cli]))
        return None

    @cached_property
    def struct_cfg(self):
        """
        struct_cfg set based on switch.struct_cfg facts
        """
        if (struct_cfg := get(self._hostvars, "switch.struct_cfg")) is not None:
            return struct_cfg
        return None
