from __future__ import annotations

import ipaddress
import re
from functools import cached_property
from hashlib import sha256

from ansible.plugins.filter.core import combine

from ansible_collections.arista.avd.plugins.filter.convert_dicts import convert_dicts
from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.filter.natural_sort import natural_sort
from ansible_collections.arista.avd.plugins.filter.range_expand import range_expand
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError, AristaAvdMissingVariableError
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_null_from_data
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get, get_item
from ansible_collections.arista.avd.roles.eos_designs.python_modules.ip_addressing import load_ip_addressing


class EosDesignsFacts(AvdFacts):

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

    def __init__(self, hostvars, templar):
        # Add reference to this instance of EosDesignsFacts object inside hostvars.
        # This is used to allow templates to access the facts object directly with "switch.*"
        hostvars["switch"] = self

        super().__init__(hostvars, templar)
        self.avd_ip_addressing = load_ip_addressing(self._hostvars, self._templar)

    @cached_property
    def type(self):
        """
        switch.type fact set based on type variable
        """
        if (node_type := get(self._hostvars, "type")) is not None:
            return node_type
        elif self._default_node_type:
            return self._default_node_type

        raise AristaAvdMissingVariableError(f"'type' for host {self.hostname}")

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
        return self._node_type_key_data["key"]

    @cached_property
    def _node_type_key_data(self):
        """
        internal _node_type_key_data containing settings for this node_type.
        """
        node_type_keys = get(self._hostvars, "node_type_keys", required=True)
        node_type_keys = convert_dicts(node_type_keys, "key")
        for node_type in node_type_keys:
            if node_type["type"] == self.type:
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
        return range_expand(get(self.default_interfaces, "downlink_interfaces", default=[]))

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
            for platform in default_interface.get("platforms", []):
                if re.search(f"^{platform}$", device_platform) and self.type in default_interface.get("types", []):
                    return default_interface

        # If not found, then look for a default default_interface that matches our type
        for default_interface in default_interfaces:
            for platform in default_interface.get("platforms", []):
                if re.search(f"^{platform}$", "default") and self.type in default_interface.get("types", []):
                    return default_interface

        return {}

    @cached_property
    def _default_node_type(self):
        """
        switch._default_node_type set based on hostname, returning
        first node type matching a regex in default_node_types
        """
        default_node_types = get(self._hostvars, "default_node_types", default=[])

        for default_node_type in default_node_types:
            for hostname_regex in default_node_type["match_hostnames"]:
                if re.search(f"^{hostname_regex}$", self.hostname):
                    return default_node_type["node_type"]

        return None

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
        switch_data = {"node_group": {}}
        node_config = {}
        hostname = self.hostname
        node_type_config = get(self._hostvars, f"{self.node_type_key}", required=True)
        nodes = convert_dicts(node_type_config.get("nodes", []), "name")

        for node in nodes:
            if hostname == node["name"]:
                node_config = node
                break
        if not node_config:
            node_groups = convert_dicts(node_type_config.get("node_groups", []), "group")
            for node_group in node_groups:
                nodes = convert_dicts(node_group.get("nodes", []), "name")
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
        defaults_config = node_type_config.get("defaults", {})
        # Merge node_group data on top of defaults into combined
        switch_data["combined"] = combine(defaults_config, switch_data["node_group"], recursive=True, list_merge="replace")
        # Merge node data on top of combined
        switch_data["combined"] = combine(switch_data["combined"], node_config, recursive=True, list_merge="replace")

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
    def group(self) -> str:
        """
        switch.group set to "node_group" name or None
        """
        return get(self._switch_data, "group")

    @cached_property
    def id(self) -> int | None:
        """
        id is optional.
        """
        return get(self._switch_data_combined, "id")

    @cached_property
    def mgmt_ip(self):
        return get(self._switch_data_combined, "mgmt_ip")

    @cached_property
    def ipv6_mgmt_ip(self):
        return get(self._switch_data_combined, "ipv6_mgmt_ip")

    @cached_property
    def platform(self):
        return get(self._switch_data_combined, "platform")

    @cached_property
    def always_configure_ip_routing(self):
        return get(self._switch_data_combined, "always_configure_ip_routing")

    @cached_property
    def max_parallel_uplinks(self):
        return get(self._switch_data_combined, "max_parallel_uplinks", default=1)

    @cached_property
    def uplink_switches(self):
        return get(self._switch_data_combined, "uplink_switches")

    @cached_property
    def uplink_interfaces(self):
        return range_expand(default(get(self._switch_data_combined, "uplink_interfaces"), get(self.default_interfaces, "uplink_interfaces"), []))

    @cached_property
    def uplink_switch_interfaces(self):
        uplink_switch_interfaces = get(self._switch_data_combined, "uplink_switch_interfaces")
        if uplink_switch_interfaces is not None:
            return uplink_switch_interfaces

        if self.uplink_switches is None:
            return []

        if self.id is None:
            raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}'")

        uplink_switch_interfaces = []
        uplink_switch_counter = {}
        for uplink_switch in self.uplink_switches:
            uplink_switch_facts: EosDesignsFacts = get(
                self._hostvars,
                f"avd_switch_facts..{uplink_switch}..switch",
                required=True,
                org_key=f"avd_switch_facts.({uplink_switch}).switch",
                separator="..",
            )

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
    def default_ptp_priority1(self):
        """
        switch.default_ptp_priority1 set based on
        node_type_keys.<node_type_key>.default_ptp_priority1
        """
        return get(self._node_type_key_data, "default_ptp_priority1", default=127)

    @cached_property
    def ptp(self):
        """
        Generates PTP config on node level as well as for interfaces, using various defaults.
        - The following are set in roles/eos_designs/defaults/main/default-node-type-keys.yml
            default_node_type_keys:
              "l3ls-evpn":
                spine:
                  default_ptp_priority1: 20
                l3leaf:
                  default_ptp_priority1: 30
        PTP priority2 is set in the code below, calculated based on the node id:
            default_priority2 = self.id % 256
        """
        # Set defaults
        default_ptp_enabled = get(self._hostvars, "ptp.enabled")
        default_ptp_domain = get(self._hostvars, "ptp.domain", default=127)
        default_ptp_profile = get(self._hostvars, "ptp.profile", default="aes67-r16-2016")
        default_clock_identity = None
        ptp = {}
        ptp["enabled"] = get(self._switch_data_combined, "ptp.enabled", default=default_ptp_enabled)
        if ptp["enabled"] is True:
            auto_clock_identity = get(self._switch_data_combined, "ptp.auto_clock_identity", default=True)
            priority1 = get(self._switch_data_combined, "ptp.priority1", default=self.default_ptp_priority1)
            priority2 = get(self._switch_data_combined, "ptp.priority2")
            if priority2 is None:
                if self.id is None:
                    raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' to set ptp priority2")
                priority2 = self.id % 256
            if auto_clock_identity is True:
                clock_identity_prefix = get(self._switch_data_combined, "ptp.clock_identity_prefix", default="00:1C:73")
                default_clock_identity = f"{clock_identity_prefix}:{priority1:02x}:00:{priority2:02x}"

            ptp["device_config"] = {
                "mode": get(self._switch_data_combined, "ptp.mode", default="boundary"),
                "forward_unicast": get(self._switch_data_combined, "ptp.forward_unicast"),
                "clock_identity": get(self._switch_data_combined, "ptp.clock_identity", default=default_clock_identity),
                "source": {"ip": get(self._switch_data_combined, "ptp.source_ip")},
                "priority1": priority1,
                "priority2": priority2,
                "ttl": get(self._switch_data_combined, "ptp.ttl"),
                "domain": get(self._switch_data_combined, "ptp.domain", default=default_ptp_domain),
                "message_type": {
                    "general": {
                        "dscp": get(self._switch_data_combined, "ptp.dscp.general_messages"),
                    },
                    "event": {
                        "dscp": get(self._switch_data_combined, "ptp.dscp.event_messages"),
                    },
                },
                "monitor": {
                    "enabled": get(self._switch_data_combined, "ptp.monitor.enabled", default=True),
                    "threshold": {
                        "offset_from_master": get(self._switch_data_combined, "ptp.monitor.threshold.offset_from_master", default=250),
                        "mean_path_delay": get(self._switch_data_combined, "ptp.monitor.threshold.mean_path_delay", default=1500),
                        "drop": {
                            "offset_from_master": get(self._switch_data_combined, "ptp.monitor.threshold.drop.offset_from_master"),
                            "mean_path_delay": get(self._switch_data_combined, "ptp.monitor.threshold.drop.mean_path_delay"),
                        },
                    },
                    "missing_message": {
                        "intervals": {
                            "announce": get(self._switch_data_combined, "ptp.monitor.missing_message.intervals.announce"),
                            "follow_up": get(self._switch_data_combined, "ptp.monitor.missing_message.intervals.follow_up"),
                            "sync": get(self._switch_data_combined, "ptp.monitor.missing_message.intervals.sync"),
                        },
                        "sequence_ids": {
                            "enabled": get(self._switch_data_combined, "ptp.monitor.missing_message.sequence_ids.enabled", default=True),
                            "announce": get(self._switch_data_combined, "ptp.monitor.missing_message.sequence_ids.announce", default=3),
                            "delay_resp": get(self._switch_data_combined, "ptp.monitor.missing_message.sequence_ids.delay_resp", default=3),
                            "follow_up": get(self._switch_data_combined, "ptp.monitor.missing_message.sequence_ids.follow_up", default=3),
                            "sync": get(self._switch_data_combined, "ptp.monitor.missing_message.sequence_ids.sync", default=3),
                        },
                    },
                },
            }

            ptp["profile"] = get(self._switch_data_combined, "ptp.profile", default_ptp_profile)
            ptp = strip_null_from_data(ptp, (None, {}))

            return ptp
        return None

    @cached_property
    def uplink_macsec(self):
        return get(self._switch_data_combined, "uplink_macsec")

    @cached_property
    def uplink_structured_config(self):
        return get(self._switch_data_combined, "uplink_structured_config")

    @cached_property
    def short_esi(self):
        """
        If short_esi is set to "auto" we will use sha256 to create a
        unique short_esi value based on various uplink information.
        """
        short_esi = get(self._switch_data_combined, "short_esi")
        if short_esi == "auto":
            esi_seed_1 = "".join(default(self.uplink_switches, [])[:2])
            esi_seed_2 = "".join(default(self.uplink_switch_interfaces, [])[:2])
            esi_seed_3 = "".join(default(self.uplink_interfaces, [])[:2])
            esi_seed_4 = default(self.group, "")
            esi_hash = sha256(f"{esi_seed_1}{esi_seed_2}{esi_seed_3}{esi_seed_4}".encode("UTF-8")).hexdigest()
            short_esi = re.sub(r"([0-9a-f]{4})", r"\1:", esi_hash)[:14]
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
        return default(get(self._switch_data_combined, "max_uplink_switches"), len(get(self._switch_data_combined, "uplink_switches", default=[])))

    @cached_property
    def is_deployed(self):
        return get(self._hostvars, "is_deployed", default=True)

    @cached_property
    def platform_settings(self):
        platform_settings = get(self._hostvars, "platform_settings", default=[])

        # First look for a matching platform setting specifying our platform
        for platform_setting in platform_settings:
            if self.platform in platform_setting.get("platforms", []):
                return platform_setting

        # If not found, then look for a default platform setting
        for platform_setting in platform_settings:
            if "default" in platform_setting.get("platforms", []):
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
            get(self._switch_data_combined, "mgmt_interface"), self.platform_settings.get("management_interface"), get(self._hostvars, "mgmt_interface")
        )

    @cached_property
    def system_mac_address(self):
        """
        system_mac_address is inherited from
        Fabric Topology data model system_mac_address ->
            Host variable var system_mac_address ->
        """
        return default(get(self._switch_data_combined, "system_mac_address"), get(self._hostvars, "system_mac_address"))

    @cached_property
    def serial_number(self):
        """
        serial_number is inherited from
        Fabric Topology data model serial_number ->
            Host variable var serial_number
        """
        return default(get(self._switch_data_combined, "serial_number"), get(self._hostvars, "serial_number"))

    @cached_property
    def underlay_routing_protocol(self):
        underlay_routing_protocol = str(get(self._hostvars, "underlay_routing_protocol", default=self.default_underlay_routing_protocol)).lower()
        if underlay_routing_protocol not in ["ebgp", "isis", "isis-ldp", "isis-sr", "isis-sr-ldp", "ospf", "ospf-ldp", "none"]:
            underlay_routing_protocol = self.default_underlay_routing_protocol
        return underlay_routing_protocol

    @cached_property
    def overlay_routing_protocol(self):
        overlay_routing_protocol = str(get(self._hostvars, "overlay_routing_protocol", default=self.default_overlay_routing_protocol)).lower()
        if overlay_routing_protocol not in ["ebgp", "ibgp", "her", "cvx", "none"]:
            overlay_routing_protocol = self.default_overlay_routing_protocol
        return overlay_routing_protocol

    @cached_property
    def overlay_address_families(self):
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            return get(self._switch_data_combined, "overlay_address_families", default=self.default_overlay_address_families)
        return []

    @cached_property
    def link_tracking_groups(self):
        if get(self._switch_data_combined, "link_tracking.enabled") is True:
            link_tracking_groups = []
            default_recovery_delay = get(self.platform_settings, "reload_delay.mlag", 300)
            lt_groups = get(self._switch_data_combined, "link_tracking.groups", default=[])

            if len(lt_groups) > 0:
                for lt_group in lt_groups:
                    lt_group["recovery_delay"] = lt_group.get("recovery_delay", default_recovery_delay)
                    link_tracking_groups.append(lt_group)
            else:
                link_tracking_groups.append({"name": "LT_GROUP1", "recovery_delay": default_recovery_delay})

            return link_tracking_groups

        return None

    @cached_property
    def lacp_port_id(self):
        if get(self._switch_data_combined, "lacp_port_id_range.enabled") is True:
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' to set LACP swicth ids")
            node_group_length = max(len(self._switch_data_node_group_nodes), 1)
            lacp_port_id = {}
            switch_id = self.id
            port_range = int(get(self._switch_data_combined, "lacp_port_id_range.size", default=128))
            port_offset = int(get(self._switch_data_combined, "lacp_port_id_range.offset", default=0))
            lacp_port_id["begin"] = 1 + (((switch_id - 1) % node_group_length) * port_range) + port_offset
            lacp_port_id["end"] = (((switch_id - 1) % node_group_length + 1) * port_range) + port_offset
            return lacp_port_id

        return None

    @cached_property
    def _any_network_services(self):
        """
        Returns True if either L1, L2 or L3 network_services are enabled
        """
        return self.network_services_l1 is True or self.network_services_l2 is True or self.network_services_l3 is True

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
    def trunk_groups(self):
        if not self._any_network_services:
            return None

        return {
            "mlag": {"name": get(self._hostvars, "trunk_groups.mlag.name", default="MLAG")},
            "mlag_l3": {"name": get(self._hostvars, "trunk_groups.mlag_l3.name", default="LEAF_PEER_L3")},
            "uplink": {"name": get(self._hostvars, "trunk_groups.uplink.name", default="UPLINK")},
        }

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
    def _port_profiles(self):
        port_profiles = get(self._hostvars, "port_profiles", default=[])
        # Support legacy data model by converting nested dict to list of dict
        return convert_dicts(port_profiles, "profile")

    def _get_adapter_settings(self, adapter_or_network_port: dict) -> dict:
        """
        Applies port-profiles to the given adapter_or_network_port and returns the combined result.
        adapter_or_network_port can either be an adapter of a connected endpoint or one item under network_ports.
        """
        profile_name = adapter_or_network_port.get("profile")
        adapter_profile = get_item(self._port_profiles, "profile", profile_name, default={})
        parent_profile_name = adapter_profile.get("parent_profile")
        parent_profile = get_item(self._port_profiles, "profile", parent_profile_name, default={})
        return combine(parent_profile, adapter_profile, adapter_or_network_port, recursive=True, list_merge="replace")

    def _parse_adapter_settings(self, adapter_settings: dict) -> tuple[set, set]:
        """
        Parse the given adapter_settings and return relevant vlans and trunk_groups
        """
        vlans = set()
        trunk_groups = set(adapter_settings.get("trunk_groups", []))
        if "vlans" in adapter_settings and adapter_settings["vlans"] not in ["all", "", None]:
            vlans.update(map(int, range_expand(str(adapter_settings["vlans"]))))
        elif "trunk" in adapter_settings.get("mode", "") and not trunk_groups:
            # No vlans or trunk_groups defined, but this is a trunk, so default is all vlans allowed
            # No need to check further, since the list is now containing all vlans.
            return set(range(1, 4094)), trunk_groups
        else:
            # No vlans or mode defined so this is an access port with only vlan 1 allowed
            vlans.add(1)

        if "native_vlan" in adapter_settings:
            vlans.add(int(adapter_settings["native_vlan"]))

        for subinterface in get(adapter_settings, "port_channel.subinterfaces", default=[]):
            if "vlan_id" in subinterface:
                vlans.add(int(subinterface["vlan_id"]))
            elif "number" in subinterface:
                vlans.add(int(subinterface["number"]))

        return vlans, trunk_groups

    @cached_property
    def _local_endpoint_vlans_and_trunk_groups(self) -> tuple[set, set]:
        """
        Return list of vlans and list of trunk groups used by connected_endpoints on this switch
        """
        if not (self._any_network_services and self.connected_endpoints):
            return set(), set()

        vlans = set()
        trunk_groups = set()

        connected_endpoints_keys = get(self._hostvars, "connected_endpoints_keys", default=[])
        # Support legacy data model by converting nested dict to list of dict
        connected_endpoints_keys = convert_dicts(connected_endpoints_keys, "key")
        for connected_endpoints_key in connected_endpoints_keys:
            connected_endpoints_key_key = connected_endpoints_key.get("key")
            if connected_endpoints_key_key is None or get(self._hostvars, connected_endpoints_key_key) is None:
                # Invalid connected_endpoints_key.key. Skipping.
                continue

            connected_endpoints = get(self._hostvars, connected_endpoints_key_key)
            # Support legacy data model by converting nested dict to list of dict
            connected_endpoints = convert_dicts(connected_endpoints, "name")
            for connected_endpoint in connected_endpoints:
                for adapter in connected_endpoint.get("adapters", []):
                    adapter_settings = self._get_adapter_settings(adapter)
                    if self.hostname not in adapter_settings.get("switches", []):
                        # This switch is not connected to this endpoint. Skipping.
                        continue

                    adapter_vlans, adapter_trunk_groups = self._parse_adapter_settings(adapter_settings)
                    vlans.update(adapter_vlans)
                    trunk_groups.update(adapter_trunk_groups)
                    if len(vlans) >= 4094:
                        # No need to check further, since the set is now containing all vlans.
                        # The trunk group list may not be complete, but it will not matter, since we will
                        # configure all vlans anyway.
                        return vlans, trunk_groups

        network_ports = get(self._hostvars, "network_ports", default=[])
        for network_port_item in network_ports:
            for switch_regex in network_port_item.get("switches", []):
                # The match test is built on Python re.match which tests from the beginning of the string #}
                # Since the user would not expect "DC1-LEAF1" to also match "DC-LEAF11" we will force ^ and $ around the regex
                switch_regex = rf"^{switch_regex}$"
                if not re.match(switch_regex, self.hostname):
                    # Skip entry if no match
                    continue

                adapter_settings = self._get_adapter_settings(network_port_item)
                adapter_vlans, adapter_trunk_groups = self._parse_adapter_settings(adapter_settings)
                vlans.update(adapter_vlans)
                trunk_groups.update(adapter_trunk_groups)
                if len(vlans) >= 4094:
                    # No need to check further, since the list is now containing all vlans.
                    # The trunk group list may not be complete, but it will not matter, since we will
                    # configure all vlans anyway.
                    return vlans, trunk_groups

        return vlans, trunk_groups

    @cached_property
    def _downstream_switch_endpoint_vlans_and_trunk_groups(self) -> tuple[set, set]:
        """
        Return set of vlans and set of trunk groups used by downstream switches.
        Traverse any downstream L2 switches so ensure we can provide connectivity to any vlans / trunk groups used by them.
        """
        if not self._any_network_services:
            return set(), set()

        vlans = set()
        trunk_groups = set()
        for fabric_switch in get(self._hostvars, "avd_switch_facts", default=[]):
            fabric_switch_facts: EosDesignsFacts = get(
                self._hostvars, f"avd_switch_facts..{fabric_switch}..switch", required=True, separator="..", org_key=f"avd_switch_facts.{fabric_switch}.switch"
            )
            if fabric_switch_facts.uplink_type == "port-channel" and self.hostname in fabric_switch_facts.uplink_peers:
                fabric_switch_endpoint_vlans, fabric_switch_endpoint_trunk_groups = fabric_switch_facts._endpoint_vlans_and_trunk_groups
                vlans.update(fabric_switch_endpoint_vlans)
                trunk_groups.update(fabric_switch_endpoint_trunk_groups)

        return vlans, trunk_groups

    @cached_property
    def _mlag_peer_endpoint_vlans_and_trunk_groups(self) -> tuple[set, set]:
        """
        Return set of vlans and set of trunk groups used by connected_endpoints on the MLAG peer.
        This could differ from local vlans and trunk groups if a connected endpoint is only connected to one leaf.
        """
        if not self.mlag:
            return set(), set()

        mlag_peer_facts: EosDesignsFacts = get(self._hostvars, f"avd_switch_facts..{self.mlag_peer}..switch", separator="..")
        if not mlag_peer_facts:
            return set(), set()

        return mlag_peer_facts._endpoint_vlans_and_trunk_groups

    @cached_property
    def _endpoint_vlans_and_trunk_groups(self) -> tuple[set, set]:
        """
        Return set of vlans and set of trunk groups used by connected_endpoints on this switch,
        downstream switches but NOT mlag peer (since we would have circular references then).
        """
        local_endpoint_vlans, local_endpoint_trunk_groups = self._local_endpoint_vlans_and_trunk_groups
        downstream_switch_endpoint_vlans, downstream_switch_endpoint_trunk_groups = self._downstream_switch_endpoint_vlans_and_trunk_groups
        return local_endpoint_vlans.union(downstream_switch_endpoint_vlans), local_endpoint_trunk_groups.union(downstream_switch_endpoint_trunk_groups)

    @cached_property
    def _endpoint_vlans(self) -> set[int]:
        """
        Return set of vlans in use by endpoints connected to this switch, downstream switches or MLAG peer.
        Ex: {1, 20, 21, 22, 23} or set()
        """
        if not self.filter_only_vlans_in_use:
            return set()

        endpoint_vlans, endpoint_trunk_groups = self._endpoint_vlans_and_trunk_groups
        if not self.mlag:
            return endpoint_vlans

        mlag_endpoint_vlans, mlag_endpoint_trunk_groups = self._mlag_peer_endpoint_vlans_and_trunk_groups
        return endpoint_vlans.union(mlag_endpoint_vlans)

    @cached_property
    def endpoint_vlans(self) -> str | None:
        """
        Return compressed list of vlans in use by endpoints connected to this switch or MLAG peer.
        Ex: "1,20-30" or ""
        """
        if self.filter_only_vlans_in_use:
            return list_compress(list(self._endpoint_vlans))

        return None

    @cached_property
    def _endpoint_trunk_groups(self) -> set[str]:
        """
        Return set of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer.
        """
        if not self.filter_only_vlans_in_use:
            return set()

        endpoint_vlans, endpoint_trunk_groups = self._endpoint_vlans_and_trunk_groups
        if not self.mlag:
            return endpoint_trunk_groups

        mlag_endpoint_vlans, mlag_endpoint_trunk_groups = self._mlag_peer_endpoint_vlans_and_trunk_groups
        return endpoint_trunk_groups.union(mlag_endpoint_trunk_groups)

    @cached_property
    def local_endpoint_trunk_groups(self) -> list[str]:
        """
        Return list of trunk_groups in use by endpoints connected to this switch only.
        Used for only applying the trunk groups in config that are relevant on this device
        This is a subset of endpoint_trunk_groups which is used for filtering.
        """
        if self.only_local_vlan_trunk_groups:
            local_endpoint_vlans, local_endpoint_trunk_groups = self._local_endpoint_vlans_and_trunk_groups
            return list(local_endpoint_trunk_groups)

        return []

    @cached_property
    def endpoint_trunk_groups(self) -> list[str]:
        """
        Return list of trunk_groups in use by endpoints connected to this switch, downstream switches or MLAG peer.
        Used for filtering which vlans we configure on the device. This is a superset of local_endpoint_trunk_groups.
        """
        return list(self._endpoint_trunk_groups)

    @cached_property
    def _vlans(self):
        """
        Return list of vlans after filtering network services.
        The filter is based on filter.tenants, filter.tags and filter.only_vlans_in_use

        Ex. [1, 2, 3 ,4 ,201, 3021]
        """
        if self._any_network_services:
            vlans = []
            match_tags = self.filter_tags
            if self.group is not None:
                match_tags.append(self.group)

            if self.filter_only_vlans_in_use:
                # Only include the vlans that are used by connected endpoints
                endpoint_trunk_groups = self._endpoint_trunk_groups
                endpoint_vlans = self._endpoint_vlans

            network_services_keys = get(self._hostvars, "network_services_keys", default=[])
            for network_services_key in natural_sort(network_services_keys, "name"):
                network_services_key_name = network_services_key.get("name")
                if network_services_key_name is None or get(self._hostvars, network_services_key_name) is None:
                    # Invalid network_services_key.name. Skipping.
                    continue

                tenants = get(self._hostvars, network_services_key_name)
                # Support legacy data model by converting nested dict to list of dict
                tenants = convert_dicts(tenants, "name")
                for tenant in natural_sort(tenants, "name"):
                    if not set(self.filter_tenants).intersection([tenant["name"], "all"]):
                        # Not matching tenant filters. Skipping this tenant.
                        continue

                    vrfs = tenant.get("vrfs", [])
                    # Support legacy data model by converting nested dict to list of dict
                    vrfs = convert_dicts(vrfs, "name")
                    for vrf in natural_sort(vrfs, "name"):
                        svis = vrf.get("svis", [])
                        # Support legacy data model by converting nested dict to list of dict
                        svis = convert_dicts(svis, "id")
                        for svi in natural_sort(svis, "id"):
                            svi_tags = svi.get("tags", ["all"])
                            if "all" in match_tags or set(svi_tags).intersection(match_tags):
                                if self.filter_only_vlans_in_use:
                                    # Check if vlan is in use
                                    if int(svi["id"]) in endpoint_vlans:
                                        vlans.append(int(svi["id"]))
                                        continue
                                    # Check if vlan has a trunk group defined which is in use
                                    if self.enable_trunk_groups and svi.get("trunk_groups") and endpoint_trunk_groups.intersection(svi["trunk_groups"]):
                                        vlans.append(int(svi["id"]))
                                        continue
                                    # Skip since the vlan is not in use
                                    continue
                                vlans.append(int(svi["id"]))

                    l2vlans = tenant.get("l2vlans", [])
                    # Support legacy data model by converting nested dict to list of dict
                    l2vlans = convert_dicts(l2vlans, "id")

                    for l2vlan in natural_sort(l2vlans, "id"):
                        l2vlan_tags = l2vlan.get("tags", ["all"])
                        if "all" in match_tags or set(l2vlan_tags).intersection(match_tags):
                            if self.filter_only_vlans_in_use:
                                # Check if vlan is in use
                                if int(l2vlan["id"]) in endpoint_vlans:
                                    vlans.append(int(l2vlan["id"]))
                                    continue
                                # Check if vlan has a trunk group defined which is in use
                                if self.enable_trunk_groups and l2vlan.get("trunk_groups") and endpoint_trunk_groups.intersection(l2vlan["trunk_groups"]):
                                    vlans.append(int(l2vlan["id"]))
                                    continue
                                # Skip since the vlan is not in use
                                continue
                            vlans.append(int(l2vlan["id"]))
            return vlans
        return []

    @cached_property
    def vlans(self):
        """
        Return the compressed list of vlans to be defined on this switch

        Ex. "1-100, 201-202"

        This excludes the optional "uplink_native_vlan" if that vlan is not used for anything else.
        This is to ensure that native vlan is not necessarily permitted on the uplink trunk.
        """
        return list_compress(self._vlans)

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
        if self.underlay_router is True:
            return get(self._hostvars, "underlay_multicast")
        return None

    @cached_property
    def overlay_rd_type_admin_subfield(self):
        tmp_overlay_rd_type_admin_subfield = get(self._hostvars, "overlay_rd_type.admin_subfield")
        tmp_overlay_rd_type_admin_subfield_offset = int(default(get(self._hostvars, "overlay_rd_type.admin_subfield_offset"), 0))
        if tmp_overlay_rd_type_admin_subfield is None:
            return self.router_id

        if tmp_overlay_rd_type_admin_subfield == "vtep_loopback":
            return self.vtep_ip

        if tmp_overlay_rd_type_admin_subfield == "bgp_as":
            return self.bgp_as

        if tmp_overlay_rd_type_admin_subfield == "switch_id":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and 'overlay_rd_type_admin_subfield' is set to 'switch_id'")
            return self.id + tmp_overlay_rd_type_admin_subfield_offset

        if re.fullmatch(r"[0-9]+", str(tmp_overlay_rd_type_admin_subfield)):
            return str(int(tmp_overlay_rd_type_admin_subfield) + tmp_overlay_rd_type_admin_subfield_offset)

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
            if not (self.underlay_multicast is True and self.igmp_snooping_enabled is not False):
                raise AristaAvdError(
                    "'evpn_multicast: True' is only supported in combination with 'underlay_multicast: True' and 'igmp_snooping_enabled : True'"
                )
            elif self.mlag is True:
                peer_overlay_rd_type_admin_subfield = get(
                    self._hostvars,
                    f"avd_switch_facts..{self.mlag_peer}..switch..overlay_rd_type_admin_subfield",
                    org_key=f"avd_switch_facts.({self.mlag_peer}).switch.overlay_rd_type_admin_subfield",
                    separator="..",
                )
                if self.overlay_rd_type_admin_subfield == peer_overlay_rd_type_admin_subfield:
                    raise AristaAvdError(
                        "For MLAG devices Route Distinguisher must be unique when 'evpn_multicast: True' since it will create a multi-vtep configuration."
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
    def router_id(self):
        """
        Render ipv4 address for router_id using dynamically loaded python module.
        """
        if self.underlay_router is True:
            return self.avd_ip_addressing.router_id()
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
        """
        Get bgp_peer_groups configurations or fallback to defaults

        Supporting legacy uppercase keys as well.
        """
        if self.underlay_router is True:
            return {
                "ipv4_underlay_peers": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.name"),
                        get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.name"),
                        "IPv4-UNDERLAY-PEERS",
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.password"), get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.password")
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.ipv4_underlay_peers.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.IPv4_UNDERLAY_PEERS.structured_config"),
                    ),
                },
                "mlag_ipv4_underlay_peer": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.name"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.name"),
                        "MLAG-IPv4-UNDERLAY-PEER",
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.password"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.password"),
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.MLAG_IPv4_UNDERLAY_PEER.structured_config"),
                    ),
                },
                "evpn_overlay_peers": {
                    "name": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.name"),
                        get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.name"),
                        "EVPN-OVERLAY-PEERS",
                    ),
                    "password": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.password"), get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.password")
                    ),
                    "structured_config": default(
                        get(self._hostvars, "bgp_peer_groups.evpn_overlay_peers.structured_config"),
                        get(self._hostvars, "bgp_peer_groups.EVPN_OVERLAY_PEERS.structured_config"),
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
                "ipvpn_gateway_peers": {
                    "name": get(self._hostvars, "bgp_peer_groups.ipvpn_gateway_peers.name", default="IPVPN-GATEWAY-PEERS"),
                    "password": get(self._hostvars, "bgp_peer_groups.ipvpn_gateway_peers.password"),
                    "structured_config": get(self._hostvars, "bgp_peer_groups.ipvpn_gateway_peers.structured_config"),
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
        """
        Get global bgp_as or fabric_topology bgp_as.

        At least one of global bgp_as or fabric_topology bgp_as must be defined.

        AS ranges in fabric_topology bgp_as will be expanded to a list and:
         - For standalone or A/A MH devices, the node id will be used to index into the list to find the ASN.
         - For MLAG devices, the node id of the first node in the node group will be used to index into the ASN list.
         - If a bare ASN is used, that ASN will be used for all relevant devices (depending on whether defined
           at the defaults, node_group or node level).
         - Lower level definitions override higher level definitions as is standard with AVD.
        """
        if self.underlay_router is True:
            if self.underlay_routing_protocol == "ebgp" or self.evpn_role != "none" or self.mpls_overlay_role != "none":
                if get(self._hostvars, "bgp_as") is not None:
                    return str(get(self._hostvars, "bgp_as"))
                else:
                    bgp_as_range_expanded = range_expand(str(get(self._switch_data_combined, "bgp_as", required=True)))
                    try:
                        if len(bgp_as_range_expanded) == 1:
                            return bgp_as_range_expanded[0]
                        elif self.mlag:
                            return bgp_as_range_expanded[self.mlag_switch_ids["primary"] - 1]
                        else:
                            if self.id is None:
                                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required when expanding 'bgp_as'")
                            return bgp_as_range_expanded[self.id - 1]
                    except IndexError as exc:
                        raise AristaAvdError(
                            f"Unable to allocate BGP AS: bgp_as range is too small ({len(bgp_as_range_expanded)}) for the id of the device"
                        ) from exc

            # Hack to make mpls PR non-breaking, adds empty bgp to igp topology spines
            # TODO: Remove this as part of AVD4.0
            elif self.underlay_routing_protocol in ["isis", "ospf"] and self.evpn_role == "none" and get(self._hostvars, "bgp_as") is not None:
                return str(get(self._hostvars, "bgp_as"))
        return None

    @cached_property
    def evpn_route_servers(self):
        """
        For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
        For all other evpn roles there is no default.
        """
        if self.underlay_router is True:
            if self.evpn_role == "client":
                return get(self._switch_data_combined, "evpn_route_servers", default=self.uplink_switches)
            else:
                return get(self._switch_data_combined, "evpn_route_servers")
        return []

    @cached_property
    def mpls_route_reflectors(self):
        if self.underlay_router is True:
            if self.mpls_overlay_role in ["client", "server"] or (self.evpn_role in ["client", "server"] and self.overlay["evpn_mpls"]):
                return get(self._switch_data_combined, "mpls_route_reflectors")
        return None

    @cached_property
    def isis_net(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
                isis_system_id_prefix = get(self._switch_data_combined, "isis_system_id_prefix")
                if isis_system_id_prefix is not None:
                    isis_area_id = get(self._hostvars, "isis_area_id", required=True)
                    if self.id is None:
                        raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to set ISIS NET address using prefix")
                    return f"{isis_area_id}.{isis_system_id_prefix}.{self.id:04d}.00"
        return None

    @cached_property
    def is_type(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
                default_is_type = get(self._hostvars, "isis_default_is_type", default="level-2")
                is_type = str(get(self._switch_data_combined, "is_type", default=default_is_type)).lower()
                if is_type not in ["level-1", "level-2", "level-1-2"]:
                    is_type = "level-2"
                return is_type
        return None

    @cached_property
    def isis_instance_name(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
                if self.mpls_lsr is True:
                    default_isis_instance_name = "CORE"
                else:
                    default_isis_instance_name = "EVPN_UNDERLAY"
                return get(self._hostvars, "underlay_isis_instance_name", default=default_isis_instance_name)
        return None

    @cached_property
    def node_sid(self):
        if self.underlay_router is True:
            if self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"]:
                if self.id is None:
                    raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to set node SID")
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
        """
        Render ipv6 address for router_id using dynamically loaded python module.
        """
        if self.underlay_ipv6 is True:
            return self.avd_ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def mlag(self):
        return self.mlag_support is True and get(self._switch_data_combined, "mlag", default=True) is True and len(self._switch_data_node_group_nodes) == 2

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
            return range_expand(default(get(self._switch_data_combined, "mlag_interfaces"), get(self.default_interfaces, "mlag_interfaces"), []))
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
            default_mlag_port_channel_id = "".join(re.findall(r"\d", self.mlag_interfaces[0]))
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
        if self.inband_management_subnet is not None and self.uplink_type == "port-channel":
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
            return int(get(self._switch_data_combined, "inband_management_vlan", default=4092))
        return None

    @cached_property
    def inband_management_ip(self):
        if self.inband_management_role == "child":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to set inband_management_ip")
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
        """
        List of uplinks with all parameters

        These facts are leveraged by templates for this device when rendering uplinks
        and by templates for peer devices when rendering downlinks
        """
        uplinks = []

        if self.uplink_type == "p2p":
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

                uplink_switch_facts: EosDesignsFacts = get(
                    self._hostvars,
                    f"avd_switch_facts..{uplink_switch}..switch",
                    required=True,
                    org_key=f"avd_switch_facts.({uplink_switch}).switch",
                    separator="..",
                )
                uplink = {}
                uplink["interface"] = uplink_interface
                uplink["peer"] = uplink_switch
                uplink["peer_interface"] = uplink_switch_interfaces[uplink_index]
                uplink["peer_type"] = uplink_switch_facts.type
                uplink["peer_is_deployed"] = uplink_switch_facts.is_deployed
                uplink["peer_bgp_as"] = uplink_switch_facts.bgp_as
                uplink["type"] = "underlay_p2p"
                if self.uplink_interface_speed is not None:
                    uplink["speed"] = self.uplink_interface_speed
                if self.uplink_bfd is True:
                    uplink["bfd"] = True
                if self.uplink_ptp is not None:
                    uplink["ptp"] = self.uplink_ptp
                elif self.ptp is not None:
                    if self.ptp["enabled"] is True:
                        uplink["ptp"] = {"enable": True}
                if self.uplink_macsec is not None:
                    uplink["mac_security"] = self.uplink_macsec
                if self.underlay_multicast is True and uplink_switch_facts.underlay_multicast is True:
                    uplink["underlay_multicast"] = True
                if get(self._hostvars, "underlay_rfc5549") is True:
                    uplink["ipv6_enable"] = True
                else:
                    uplink["ip_address"] = self.avd_ip_addressing.p2p_uplinks_ip(uplink_index)
                    uplink["peer_ip_address"] = self.avd_ip_addressing.p2p_uplinks_peer_ip(uplink_index)

                if self.link_tracking_groups is not None:
                    uplink["link_tracking_groups"] = []
                    for lt_group in self.link_tracking_groups:
                        uplink["link_tracking_groups"].append({"name": lt_group["name"], "direction": "upstream"})

                if self.uplink_structured_config is not None:
                    uplink["structured_config"] = self.uplink_structured_config

                uplinks.append(uplink)
            return uplinks

        elif self.uplink_type == "port-channel":
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

                uplink_switch_facts: EosDesignsFacts = get(
                    self._hostvars,
                    f"avd_switch_facts..{uplink_switch}..switch",
                    required=True,
                    org_key=f"avd_switch_facts.({uplink_switch}).switch",
                    separator="..",
                )
                uplink = {}
                uplink["interface"] = uplink_interface
                uplink["peer"] = uplink_switch
                uplink["peer_interface"] = uplink_switch_interfaces[uplink_index]
                uplink["peer_type"] = uplink_switch_facts.type
                uplink["peer_is_deployed"] = uplink_switch_facts.is_deployed
                uplink["type"] = "underlay_l2"

                if self.uplink_interface_speed is not None:
                    uplink["speed"] = self.uplink_interface_speed

                if uplink_switch_facts.mlag is True or self.short_esi is not None:
                    # Override our description on port-channel to be peer's group name if they are mlag pair or A/A #}
                    uplink["channel_description"] = uplink_switch_facts.group

                if self.mlag is True:
                    # Override the peer's description on port-channel to be our group name if we are mlag pair #}
                    uplink["peer_channel_description"] = self.group

                if self.mlag_role == "secondary":
                    mlag_peer_switch_facts: EosDesignsFacts = get(
                        self._hostvars,
                        f"avd_switch_facts..{self.mlag_peer}..switch",
                        required=True,
                        separator="..",
                        org_key=f"avd_switch_facts.{self.mlag_peer}.switch",
                    )

                    uplink["channel_group_id"] = "".join(re.findall(r"\d", mlag_peer_switch_facts.uplink_interfaces[0]))
                    uplink["peer_channel_group_id"] = "".join(re.findall(r"\d", mlag_peer_switch_facts.uplink_switch_interfaces[0]))
                else:
                    uplink["channel_group_id"] = "".join(re.findall(r"\d", uplink_interfaces[0]))
                    uplink["peer_channel_group_id"] = "".join(re.findall(r"\d", uplink_switch_interfaces[0]))

                # Remove vlans if upstream switch does not have them #}
                if self.enable_trunk_groups:
                    uplink["trunk_groups"] = ["UPLINK"]
                    if self.mlag is True:
                        uplink["peer_trunk_groups"] = [self.group]
                    else:
                        uplink["peer_trunk_groups"] = [self.hostname]

                switch_vlans = self._vlans
                uplink_switch_vlans = uplink_switch_facts._vlans
                uplink_vlans = list(set(switch_vlans).intersection(uplink_switch_vlans))

                if self.inband_management_vlan is not None:
                    uplink_vlans.append(int(self.inband_management_vlan))

                if uplink_vlans:
                    uplink["vlans"] = list_compress(uplink_vlans)
                else:
                    uplink["vlans"] = "none"

                if uplink_native_vlan := get(self._switch_data_combined, "uplink_native_vlan"):
                    uplink["native_vlan"] = uplink_native_vlan

                if self.short_esi is not None:
                    uplink["peer_short_esi"] = self.short_esi

                if self.link_tracking_groups is not None:
                    uplink["link_tracking_groups"] = []
                    for lt_group in self.link_tracking_groups:
                        uplink["link_tracking_groups"].append({"name": lt_group["name"], "direction": "upstream"})

                if self.uplink_structured_config is not None:
                    uplink["structured_config"] = self.uplink_structured_config

                uplinks.append(uplink)
        return uplinks

    @cached_property
    def uplink_peers(self):
        """
        List of all uplink peers

        These are used to generate the "avd_topology_peers" fact covering downlinks for all devices.
        """
        fabric_name = get(self._hostvars, "fabric_name", required=True)
        inventory_group = get(self._hostvars, f"groups.{fabric_name}", required=True)
        uplink_switches = default(self.uplink_switches, [])
        return [uplink_switch for uplink_switch in uplink_switches if uplink_switch in inventory_group]

    @cached_property
    def _mlag_peer_id(self):
        if self.mlag is True:
            return get(
                self._hostvars,
                f"avd_switch_facts..{self.mlag_peer}..switch..id",
                required=True,
                org_key=f"avd_switch_facts.({self.mlag_peer}).switch.id",
                separator="..",
            )

    @cached_property
    def mlag_switch_ids(self):
        """
        Returns the switch id's of both primary and secondary switches for a given node group
        """
        if self.mlag_role == "primary":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids")
            return {"primary": self.id, "secondary": self._mlag_peer_id}
        elif self.mlag_role == "secondary":
            if self.id is None:
                raise AristaAvdMissingVariableError(f"'id' is not set on '{self.hostname}' and is required to compute MLAG ids")
            return {"primary": self._mlag_peer_id, "secondary": self.id}

    @cached_property
    def vtep_ip(self):
        """
        Render ipv4 address for vtep_ip using dynamically loaded python module.
        """
        if self.vtep is True:
            if self.mlag is True:
                return self.avd_ip_addressing.vtep_ip_mlag()

            else:
                return self.avd_ip_addressing.vtep_ip()

        return None

    @cached_property
    def mlag_ip(self):
        """
        Render ipv4 address for mlag_ip using dynamically loaded python module.
        """
        if self.mlag is True:
            if self.mlag_role == "primary":
                return self.avd_ip_addressing.mlag_ip_primary()
            elif self.mlag_role == "secondary":
                return self.avd_ip_addressing.mlag_ip_secondary()
        return None

    @cached_property
    def mlag_peer_ip(self):
        if self.mlag is True:
            return get(
                self._hostvars,
                f"avd_switch_facts..{self.mlag_peer}..switch..mlag_ip",
                required=True,
                org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_ip",
                separator="..",
            )
        return None

    @cached_property
    def mlag_l3_ip(self):
        """
        Render ipv4 address for mlag_l3_ip using dynamically loaded python module.
        """
        if self.mlag_l3 is True and self.mlag_peer_l3_vlan is not None:
            if self.mlag_role == "primary":
                return self.avd_ip_addressing.mlag_l3_ip_primary()
            elif self.mlag_role == "secondary":
                return self.avd_ip_addressing.mlag_l3_ip_secondary()
        return None

    @cached_property
    def mlag_peer_l3_ip(self):
        if self.mlag_l3 is True and self.mlag_peer_l3_vlan is not None:
            return get(
                self._hostvars,
                f"avd_switch_facts..{self.mlag_peer}..switch..mlag_l3_ip",
                required=True,
                org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mlag_l3_ip",
                separator="..",
            )
        return None

    @cached_property
    def mlag_peer_mgmt_ip(self):
        if self.mlag is True:
            peer_mgmt_ip = get(
                self._hostvars,
                f"avd_switch_facts..{self.mlag_peer}..switch..mgmt_ip",
                org_key=f"avd_switch_facts.({self.mlag_peer}).switch.mgmt_ip",
                separator="..",
            )
            if peer_mgmt_ip is not None:
                return str(ipaddress.ip_interface(peer_mgmt_ip).ip)
        return None

    @cached_property
    def overlay_routing_protocol_address_family(self):
        overlay_routing_protocol_address_family = get(self._hostvars, "overlay_routing_protocol_address_family", default="ipv4")
        if overlay_routing_protocol_address_family == "ipv6":
            if not (get(self._hostvars, "underlay_ipv6") is True and get(self._hostvars, "underlay_rfc5549") is True):
                raise AristaAvdError(
                    "'overlay_routing_protocol_address_family: ipv6' is only supported in combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
                )
        return overlay_routing_protocol_address_family

    @cached_property
    def bgp(self):
        """
        Boolean telling if BGP Routing should be configured.
        """
        return (
            self.underlay_router
            and self.uplink_type == "p2p"
            and (
                self.underlay_routing_protocol == "ebgp"
                or (
                    self.overlay_routing_protocol in ["ebgp", "ibgp"]
                    and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
                )
            )
        )

    @cached_property
    def evpn_encapsulation(self):
        """
        Toggle to set EVPN encapsulation based on fabric_evpn_encapsulation and node default_evpn_encapsulation.
        """
        return get(self._hostvars, "fabric_evpn_encapsulation", default=get(self._node_type_key_data, "default_evpn_encapsulation", default="vxlan"))

    @cached_property
    def underlay(self):
        """
        Returns a dictionary of underlay parameters to configure on the node.
        """
        if self.uplink_type != "p2p" or not self.underlay_router:
            return {"bgp": False, "ldp": False, "sr": False, "mpls": False, "ospf": False, "isis": False}
        bgp = self.bgp and self.underlay_routing_protocol == "ebgp"
        mpls = self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.mpls_lsr
        ldp = self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and mpls
        sr = self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and mpls
        ospf = self.underlay_routing_protocol in ["ospf", "ospf-ldp"]
        isis = self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"]

        return {
            "bgp": bgp,
            "ldp": ldp,
            "mpls": mpls,
            "sr": sr,
            "ospf": ospf,
            "isis": isis,
        }

    @cached_property
    def _overlay_evpn(self) -> bool:
        # Set overlay.evpn to enable EVPN on the node
        return (
            self.bgp
            and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
            and self.overlay_routing_protocol in ["ebgp", "ibgp"]
            and "evpn" in self.overlay_address_families
        )

    @cached_property
    def _overlay_ipvpn_gateway(self) -> bool:
        # Set ipvpn_gateway to trigger ipvpn interworking configuration.
        return self._overlay_evpn and get(self._switch_data_combined, "ipvpn_gateway.enabled", default=False)

    @cached_property
    def _overlay_ler(self) -> bool:
        return (
            self.underlay["mpls"]
            and (self.mpls_overlay_role in ["client", "server"] or self.evpn_role in ["client", "server"])
            and (self.network_services_l1 or self.network_services_l2 or self.network_services_l3)
        )

    @cached_property
    def _overlay_vtep(self) -> bool:
        # Set overlay.vtep to enable VXLAN edge PE features
        return (
            self.overlay_routing_protocol in ["ebgp", "ibgp", "her", "cvx"]
            and (self.network_services_l2 or self.network_services_l3)
            and self.underlay_router
            and self.uplink_type == "p2p"
            and self.vtep
        )

    @cached_property
    def _overlay_vpn_ipv4(self) -> bool:
        # Set overlay.vpn_ipv4 and vpn_ipv6 to enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv4" in self.overlay_address_families) or (
            "vpn-ipv4" in get(self._switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self._overlay_ipvpn_gateway
        )

    @cached_property
    def _overlay_vpn_ipv6(self) -> bool:
        # Set overlay.vpn_ipv4 and vpn_ipv6 to enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv6" in self.overlay_address_families) or (
            "vpn-ipv6" in get(self._switch_data_combined, "ipvpn_gateway.address_families", default=["vpn-ipv4"]) and self._overlay_ipvpn_gateway
        )

    @cached_property
    def overlay(self) -> dict:
        """
        Returns a dictionary of overlay parameters to configure on the node.
        """
        # Set overlay.peering_address to use
        if self.overlay_routing_protocol_address_family == "ipv6":
            peering_address = self.ipv6_router_id
        else:
            peering_address = self.router_id

        cvx = self.overlay_routing_protocol == "cvx"
        her = self.overlay_routing_protocol == "her"
        # Set overlay.evpn_vxlan and overlay.evpn_mpls to differentiate between VXLAN and MPLS use cases.
        evpn_vxlan = self._overlay_evpn and self.evpn_encapsulation == "vxlan"
        evpn_mpls = self._overlay_evpn and self.evpn_encapsulation == "mpls"
        # Set dpath based on ipvpn_gateway parameters
        dpath = self._overlay_ipvpn_gateway and get(self._switch_data_combined, "ipvpn_gateway.enable_d_path", default=True)

        return {
            "peering_address": peering_address,
            "ler": self._overlay_ler,
            "vtep": self._overlay_vtep,
            "cvx": cvx,
            "her": her,
            "evpn": self._overlay_evpn,
            "evpn_vxlan": evpn_vxlan,
            "evpn_mpls": evpn_mpls,
            "vpn_ipv4": self._overlay_vpn_ipv4,
            "vpn_ipv6": self._overlay_vpn_ipv6,
            "ipvpn_gateway": self._overlay_ipvpn_gateway,
            "dpath": dpath,
        }

    @cached_property
    def ipvpn_gateway(self) -> dict | None:
        """
        Returns a dictionary of ipvpn interworking gateway parameters to configure on the node.
        """
        if get(self.overlay, "ipvpn_gateway"):
            return {
                "evpn_domain_id": get(self._switch_data_combined, "ipvpn_gateway.evpn_domain_id", default="0:1"),
                "ipvpn_domain_id": get(self._switch_data_combined, "ipvpn_gateway.ipvpn_domain_id", default="0:2"),
                "max_routes": get(self._switch_data_combined, "ipvpn_gateway.maximum_routes", default=0),
                "local_as": get(self._switch_data_combined, "ipvpn_gateway.local_as"),
                "remote_peers": get(self._switch_data_combined, "ipvpn_gateway.remote_peers", default=[]),
            }

        return None
