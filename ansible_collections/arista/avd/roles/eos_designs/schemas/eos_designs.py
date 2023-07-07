from pydantic import BaseModel


class Eos_designsUplink_ptp(BaseModel):
    enable: bool = False


class Eos_designsUnderlay_multicast_rpsitemNodesitem(BaseModel):
    name: str | None = None
    loopback_number: int = None
    description: str = "PIM RP"


class Eos_designsUnderlay_multicast_rpsitem(BaseModel):
    rp: str = None
    nodes: list[Eos_designsUnderlay_multicast_rpsitemNodesitem] | None = None
    groups: list[str] | None = None
    access_list_name: str | None = None


class Eos_designsUnderlay_multicast_anycast_rp(BaseModel):
    mode: str = "pim"


class Eos_designsTrunk_groupsUplink(BaseModel):
    name: str = "UPLINK"


class Eos_designsTrunk_groupsMlag_l3(BaseModel):
    name: str = "LEAF_PEER_L3"


class Eos_designsTrunk_groupsMlag(BaseModel):
    name: str = "MLAG"


class Eos_designsTrunk_groups(BaseModel):
    mlag: Eos_designsTrunk_groupsMlag | None = None
    mlag_l3: Eos_designsTrunk_groupsMlag_l3 | None = None
    uplink: Eos_designsTrunk_groupsUplink | None = None


class Eos_designsSvi_profilesitemBgp(BaseModel):
    structured_config: dict | None = None
    raw_eos_cli: str | None = None


class Eos_designsSvi_profilesitemOspfMessage_digest_keysitem(BaseModel):
    id: int | None = None
    hash_algorithm: str = "sha512"
    key: str | None = None


class Eos_designsSvi_profilesitemOspf(BaseModel):
    enabled: bool | None = None
    point_to_point: bool = True
    area: str = "0"
    cost: int | None = None
    authentication: str | None = None
    simple_auth_key: str | None = None
    message_digest_keys: list[Eos_designsSvi_profilesitemOspfMessage_digest_keysitem] | None = None


class Eos_designsSvi_profilesitemIgmp_snooping_querier(BaseModel):
    enabled: bool | None = None
    source_address: str | None = None
    version: int | None = None


class Eos_designsSvi_profilesitemEvpn_l3_multicast(BaseModel):
    enabled: bool | None = None


class Eos_designsSvi_profilesitemEvpn_l2_multicast(BaseModel):
    enabled: bool | None = None


class Eos_designsSvi_profilesitemIp_helpersitem(BaseModel):
    ip_helper: str | None = None
    source_interface: str | None = None
    source_vrf: str | None = None


class Eos_designsSvi_profilesitemNodesitemBgp(BaseModel):
    structured_config: dict | None = None
    raw_eos_cli: str | None = None


class Eos_designsSvi_profilesitemNodesitemOspfMessage_digest_keysitem(BaseModel):
    id: int | None = None
    hash_algorithm: str = "sha512"
    key: str | None = None


class Eos_designsSvi_profilesitemNodesitemOspf(BaseModel):
    enabled: bool | None = None
    point_to_point: bool = True
    area: str = "0"
    cost: int | None = None
    authentication: str | None = None
    simple_auth_key: str | None = None
    message_digest_keys: list[Eos_designsSvi_profilesitemNodesitemOspfMessage_digest_keysitem] | None = None


class Eos_designsSvi_profilesitemNodesitemIgmp_snooping_querier(BaseModel):
    enabled: bool | None = None
    source_address: str | None = None
    version: int | None = None


class Eos_designsSvi_profilesitemNodesitemEvpn_l3_multicast(BaseModel):
    enabled: bool | None = None


class Eos_designsSvi_profilesitemNodesitemEvpn_l2_multicast(BaseModel):
    enabled: bool | None = None


class Eos_designsSvi_profilesitemNodesitemIp_helpersitem(BaseModel):
    ip_helper: str | None = None
    source_interface: str | None = None
    source_vrf: str | None = None


class Eos_designsSvi_profilesitemNodesitem(BaseModel):
    node: str | None = None
    name: str | None = None
    enabled: bool | None = None
    description: str | None = None
    ip_address: str | None = None
    ipv6_address: str | None = None
    ipv6_enable: bool | None = None
    ip_address_virtual: str | None = None
    ipv6_address_virtual: str | None = None
    ipv6_address_virtuals: list[str] | None = None
    ip_address_virtual_secondaries: list[str] | None = None
    ip_virtual_router_addresses: list[str] | None = None
    ipv6_virtual_router_addresses: list[str] | None = None
    ip_helpers: list[Eos_designsSvi_profilesitemNodesitemIp_helpersitem] | None = None
    vni_override: int | None = None
    rt_override: str | None = None
    rd_override: str | None = None
    tags: list[str] = ["all"]
    trunk_groups: list[str] | None = None
    evpn_l2_multicast: Eos_designsSvi_profilesitemNodesitemEvpn_l2_multicast | None = None
    evpn_l3_multicast: Eos_designsSvi_profilesitemNodesitemEvpn_l3_multicast | None = None
    igmp_snooping_enabled: bool | None = None
    igmp_snooping_querier: Eos_designsSvi_profilesitemNodesitemIgmp_snooping_querier | None = None
    vxlan: bool = True
    mtu: int | None = None
    ospf: Eos_designsSvi_profilesitemNodesitemOspf | None = None
    bgp: Eos_designsSvi_profilesitemNodesitemBgp | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsSvi_profilesitem(BaseModel):
    profile: str | None = None
    parent_profile: str | None = None
    nodes: list[Eos_designsSvi_profilesitemNodesitem] | None = None
    name: str | None = None
    enabled: bool | None = None
    description: str | None = None
    ip_address: str | None = None
    ipv6_address: str | None = None
    ipv6_enable: bool | None = None
    ip_address_virtual: str | None = None
    ipv6_address_virtual: str | None = None
    ipv6_address_virtuals: list[str] | None = None
    ip_address_virtual_secondaries: list[str] | None = None
    ip_virtual_router_addresses: list[str] | None = None
    ipv6_virtual_router_addresses: list[str] | None = None
    ip_helpers: list[Eos_designsSvi_profilesitemIp_helpersitem] | None = None
    vni_override: int | None = None
    rt_override: str | None = None
    rd_override: str | None = None
    tags: list[str] = ["all"]
    trunk_groups: list[str] | None = None
    evpn_l2_multicast: Eos_designsSvi_profilesitemEvpn_l2_multicast | None = None
    evpn_l3_multicast: Eos_designsSvi_profilesitemEvpn_l3_multicast | None = None
    igmp_snooping_enabled: bool | None = None
    igmp_snooping_querier: Eos_designsSvi_profilesitemIgmp_snooping_querier | None = None
    vxlan: bool = True
    mtu: int | None = None
    ospf: Eos_designsSvi_profilesitemOspf | None = None
    bgp: Eos_designsSvi_profilesitemBgp | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsSnmp_settingsUsersitem(BaseModel):
    name: str | None = None
    group: str | None = None
    version: str | None = None
    auth: str | None = None
    auth_passphrase: str | None = None
    priv: str | None = None
    priv_passphrase: str | None = None


class Eos_designsSnmp_settings(BaseModel):
    contact: str | None = None
    location: bool = False
    compute_local_engineid: bool = False
    compute_local_engineid_source: str = "hostname_and_ip"
    compute_v3_user_localized_key: bool = False
    users: list[Eos_designsSnmp_settingsUsersitem] | None = None


class Eos_designsRedundancy(BaseModel):
    protocol: str | None = None


class Eos_designsQueue_monitor_lengthCpuThresholds(BaseModel):
    high: int = None
    low: int | None = None


class Eos_designsQueue_monitor_lengthCpu(BaseModel):
    thresholds: Eos_designsQueue_monitor_lengthCpuThresholds | None = None


class Eos_designsQueue_monitor_lengthDefault_thresholds(BaseModel):
    high: int = None
    low: int | None = None


class Eos_designsQueue_monitor_length(BaseModel):
    enabled: bool = None
    notifying: bool | None = None
    default_thresholds: Eos_designsQueue_monitor_lengthDefault_thresholds | None = None
    log: int | None = None
    cpu: Eos_designsQueue_monitor_lengthCpu | None = None


class Eos_designsPtp_profilesitemSync_message(BaseModel):
    interval: int | None = None


class Eos_designsPtp_profilesitemAnnounce(BaseModel):
    interval: int | None = None
    timeout: int | None = None


class Eos_designsPtp_profilesitem(BaseModel):
    profile: str | None = None
    announce: Eos_designsPtp_profilesitemAnnounce | None = None
    delay_req: int | None = None
    sync_message: Eos_designsPtp_profilesitemSync_message | None = None
    transport: str | None = None


class Eos_designsPtp(BaseModel):
    enabled: bool | None = None
    profile: str = "aes67-r16-2016"
    domain: int | None = None
    auto_clock_identity: bool = True


class Eos_designsPort_profilesitemPort_channelSubinterfacesitemEncapsulation_vlan(BaseModel):
    client_dot1q: int | None = None


class Eos_designsPort_profilesitemPort_channelSubinterfacesitem(BaseModel):
    number: int | None = None
    short_esi: str | None = None
    vlan_id: int | None = None
    encapsulation_vlan: Eos_designsPort_profilesitemPort_channelSubinterfacesitemEncapsulation_vlan | None = None


class Eos_designsPort_profilesitemPort_channelLacp_timer(BaseModel):
    mode: str | None = None
    multiplier: int | None = None


class Eos_designsPort_profilesitemPort_channelLacp_fallback(BaseModel):
    mode: str | None = None
    timeout: int | None = None


class Eos_designsPort_profilesitemPort_channel(BaseModel):
    mode: str | None = None
    channel_id: int | None = None
    description: str | None = None
    enabled: bool = True
    esi: str | None = None
    short_esi: str | None = None
    lacp_fallback: Eos_designsPort_profilesitemPort_channelLacp_fallback | None = None
    lacp_timer: Eos_designsPort_profilesitemPort_channelLacp_timer | None = None
    subinterfaces: list[Eos_designsPort_profilesitemPort_channelSubinterfacesitem] | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsPort_profilesitemEthernet_segment(BaseModel):
    short_esi: str = None
    redundancy: str | None = None
    designated_forwarder_algorithm: str | None = None
    designated_forwarder_preferences: list[str] | None = None
    dont_preempt: bool | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitemSession_settingsTruncate(BaseModel):
    enabled: bool | None = None
    size: int | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitemSession_settingsAccess_group(BaseModel):
    type: str | None = None
    name: str | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitemSession_settings(BaseModel):
    encapsulation_gre_metadata_tx: bool | None = None
    header_remove_size: int | None = None
    access_group: Eos_designsPort_profilesitemMonitor_sessionsitemSession_settingsAccess_group | None = None
    rate_limit_per_ingress_chip: str | None = None
    rate_limit_per_egress_chip: str | None = None
    sample: int | None = None
    truncate: Eos_designsPort_profilesitemMonitor_sessionsitemSession_settingsTruncate | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitemSource_settingsAccess_group(BaseModel):
    type: str | None = None
    name: str | None = None
    priority: int | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitemSource_settings(BaseModel):
    direction: str | None = None
    access_group: Eos_designsPort_profilesitemMonitor_sessionsitemSource_settingsAccess_group | None = None


class Eos_designsPort_profilesitemMonitor_sessionsitem(BaseModel):
    name: str = None
    role: str | None = None
    source_settings: Eos_designsPort_profilesitemMonitor_sessionsitemSource_settings | None = None
    session_settings: Eos_designsPort_profilesitemMonitor_sessionsitemSession_settings | None = None


class Eos_designsPort_profilesitemStorm_controlUnknown_unicast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsPort_profilesitemStorm_controlMulticast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsPort_profilesitemStorm_controlBroadcast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsPort_profilesitemStorm_controlAll(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsPort_profilesitemStorm_control(BaseModel):
    all: Eos_designsPort_profilesitemStorm_controlAll | None = None
    broadcast: Eos_designsPort_profilesitemStorm_controlBroadcast | None = None
    multicast: Eos_designsPort_profilesitemStorm_controlMulticast | None = None
    unknown_unicast: Eos_designsPort_profilesitemStorm_controlUnknown_unicast | None = None


class Eos_designsPort_profilesitemPoeLimit(BaseModel):
    class: int | None = None
    watts: str | None = None
    fixed: bool | None = None


class Eos_designsPort_profilesitemPoeShutdown(BaseModel):
    action: str | None = None


class Eos_designsPort_profilesitemPoeLink_down(BaseModel):
    action: str | None = None
    power_off_delay: int | None = None


class Eos_designsPort_profilesitemPoeReboot(BaseModel):
    action: str | None = None


class Eos_designsPort_profilesitemPoe(BaseModel):
    disabled: bool = False
    priority: str | None = None
    reboot: Eos_designsPort_profilesitemPoeReboot | None = None
    link_down: Eos_designsPort_profilesitemPoeLink_down | None = None
    shutdown: Eos_designsPort_profilesitemPoeShutdown | None = None
    limit: Eos_designsPort_profilesitemPoeLimit | None = None
    negotiation_lldp: bool | None = None
    legacy_detect: bool | None = None


class Eos_designsPort_profilesitemDot1xTimeout(BaseModel):
    idle_host: int | None = None
    quiet_period: int | None = None
    reauth_period: str | None = None
    reauth_timeout_ignore: bool | None = None
    tx_period: int | None = None


class Eos_designsPort_profilesitemDot1xMac_based_authentication(BaseModel):
    enabled: bool | None = None
    always: bool | None = None
    host_mode_common: bool | None = None


class Eos_designsPort_profilesitemDot1xHost_mode(BaseModel):
    mode: str | None = None
    multi_host_authenticated: bool | None = None


class Eos_designsPort_profilesitemDot1xAuthentication_failure(BaseModel):
    action: str | None = None
    allow_vlan: int | None = None


class Eos_designsPort_profilesitemDot1xPae(BaseModel):
    mode: str | None = None


class Eos_designsPort_profilesitemDot1x(BaseModel):
    port_control: str | None = None
    port_control_force_authorized_phone: bool | None = None
    reauthentication: bool | None = None
    pae: Eos_designsPort_profilesitemDot1xPae | None = None
    authentication_failure: Eos_designsPort_profilesitemDot1xAuthentication_failure | None = None
    host_mode: Eos_designsPort_profilesitemDot1xHost_mode | None = None
    mac_based_authentication: Eos_designsPort_profilesitemDot1xMac_based_authentication | None = None
    timeout: Eos_designsPort_profilesitemDot1xTimeout | None = None
    reauthorization_request_limit: int | None = None


class Eos_designsPort_profilesitemLink_tracking(BaseModel):
    enabled: bool | None = None
    name: str | None = None


class Eos_designsPort_profilesitemPtp(BaseModel):
    enabled: bool = False
    endpoint_role: str = "follower"
    profile: str = "aes67-r16-2016"


class Eos_designsPort_profilesitemFlowcontrol(BaseModel):
    received: str | None = None


class Eos_designsPort_profilesitem(BaseModel):
    profile: str | None = None
    parent_profile: str | None = None
    speed: str | None = None
    description: str | None = None
    enabled: bool = True
    mode: str | None = None
    mtu: int | None = None
    l2_mtu: int | None = None
    native_vlan: int | None = None
    native_vlan_tag: bool = False
    trunk_groups: list[str] | None = None
    vlans: str | None = None
    spanning_tree_portfast: str | None = None
    spanning_tree_bpdufilter: str | None = None
    spanning_tree_bpduguard: str | None = None
    flowcontrol: Eos_designsPort_profilesitemFlowcontrol | None = None
    qos_profile: str | None = None
    ptp: Eos_designsPort_profilesitemPtp | None = None
    link_tracking: Eos_designsPort_profilesitemLink_tracking | None = None
    dot1x: Eos_designsPort_profilesitemDot1x | None = None
    poe: Eos_designsPort_profilesitemPoe | None = None
    storm_control: Eos_designsPort_profilesitemStorm_control | None = None
    monitor_sessions: list[Eos_designsPort_profilesitemMonitor_sessionsitem] | None = None
    ethernet_segment: Eos_designsPort_profilesitemEthernet_segment | None = None
    port_channel: Eos_designsPort_profilesitemPort_channel | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsPlatform_speed_groupsitemSpeedsitem(BaseModel):
    speed: str | None = None
    speed_groups: list[int] | None = None


class Eos_designsPlatform_speed_groupsitem(BaseModel):
    platform: str | None = None
    speeds: list[Eos_designsPlatform_speed_groupsitemSpeedsitem] | None = None


class Eos_designsPlatform_settingsitemFeature_support(BaseModel):
    queue_monitor_length_notify: bool = True
    interface_storm_control: bool = True
    poe: bool = False
    bgp_update_wait_install: bool = True
    bgp_update_wait_for_convergence: bool = True


class Eos_designsPlatform_settingsitemReload_delay(BaseModel):
    mlag: int | None = None
    non_mlag: int | None = None


class Eos_designsPlatform_settingsitem(BaseModel):
    platforms: list[str] | None = None
    trident_forwarding_table_partition: str | None = None
    reload_delay: Eos_designsPlatform_settingsitemReload_delay | None = None
    tcam_profile: str | None = None
    lag_hardware_only: bool | None = None
    feature_support: Eos_designsPlatform_settingsitemFeature_support | None = None
    management_interface: str = "Management1"
    raw_eos_cli: str | None = None


class Eos_designsOverlay_rt_type(BaseModel):
    admin_subfield: str = "vrf_id"
    vrf_admin_subfield: str = "vrf_id"
    vlan_assigned_number_subfield: str = "mac_vrf_id"


class Eos_designsOverlay_rd_type(BaseModel):
    admin_subfield: str = "overlay_loopback_ip"
    admin_subfield_offset: str | None = None
    vrf_admin_subfield: str | None = None
    vrf_admin_subfield_offset: str | None = None
    vlan_assigned_number_subfield: str = "mac_vrf_id"


class Eos_designsNode_type_keysitemInterface_descriptions(BaseModel):
    python_module: str | None = None
    python_class_name: str | None = None
    underlay_ethernet_interfaces: str | None = None
    underlay_port_channel_interfaces: str | None = None
    mlag_ethernet_interfaces: str | None = None
    mlag_port_channel_interfaces: str | None = None
    connected_endpoints_ethernet_interfaces: str | None = None
    connected_endpoints_port_channel_interfaces: str | None = None
    overlay_loopback_interface: str | None = None
    vtep_loopback_interface: str | None = None


class Eos_designsNode_type_keysitemIp_addressing(BaseModel):
    python_module: str | None = None
    python_class_name: str | None = None
    router_id: str | None = None
    router_id_ipv6: str | None = None
    mlag_ip_primary: str | None = None
    mlag_ip_secondary: str | None = None
    mlag_l3_ip_primary: str | None = None
    mlag_l3_ip_secondary: str | None = None
    mlag_ibgp_peering_ip_primary: str | None = None
    mlag_ibgp_peering_ip_secondary: str | None = None
    p2p_uplinks_ip: str | None = None
    p2p_uplinks_peer_ip: str | None = None
    vtep_ip_mlag: str | None = None
    vtep_ip: str | None = None


class Eos_designsNode_type_keysitemNetwork_services(BaseModel):
    l1: bool = False
    l2: bool = False
    l3: bool = False


class Eos_designsNode_type_keysitem(BaseModel):
    key: str | None = None
    type: str | None = None
    connected_endpoints: bool = False
    default_evpn_role: str = "none"
    default_ptp_priority1: int = 127
    default_underlay_routing_protocol: str = "ebgp"
    default_overlay_routing_protocol: str = "ebgp"
    default_mpls_overlay_role: str | None = None
    default_overlay_address_families: list[str] | None = None
    default_evpn_encapsulation: str | None = None
    mlag_support: bool = False
    network_services: Eos_designsNode_type_keysitemNetwork_services | None = None
    underlay_router: bool = True
    uplink_type: str = "p2p"
    vtep: bool = False
    mpls_lsr: bool = False
    ip_addressing: Eos_designsNode_type_keysitemIp_addressing | None = None
    interface_descriptions: Eos_designsNode_type_keysitemInterface_descriptions | None = None


class Eos_designsNetwork_services_keysitem(BaseModel):
    name: str | None = None


class Eos_designsNetwork_portsitemPort_channelSubinterfacesitemEncapsulation_vlan(BaseModel):
    client_dot1q: int | None = None


class Eos_designsNetwork_portsitemPort_channelSubinterfacesitem(BaseModel):
    number: int | None = None
    short_esi: str | None = None
    vlan_id: int | None = None
    encapsulation_vlan: Eos_designsNetwork_portsitemPort_channelSubinterfacesitemEncapsulation_vlan | None = None


class Eos_designsNetwork_portsitemPort_channelLacp_timer(BaseModel):
    mode: str | None = None
    multiplier: int | None = None


class Eos_designsNetwork_portsitemPort_channelLacp_fallback(BaseModel):
    mode: str | None = None
    timeout: int | None = None


class Eos_designsNetwork_portsitemPort_channel(BaseModel):
    mode: str | None = None
    channel_id: int | None = None
    description: str | None = None
    enabled: bool = True
    esi: str | None = None
    short_esi: str | None = None
    lacp_fallback: Eos_designsNetwork_portsitemPort_channelLacp_fallback | None = None
    lacp_timer: Eos_designsNetwork_portsitemPort_channelLacp_timer | None = None
    subinterfaces: list[Eos_designsNetwork_portsitemPort_channelSubinterfacesitem] | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsNetwork_portsitemEthernet_segment(BaseModel):
    short_esi: str = None
    redundancy: str | None = None
    designated_forwarder_algorithm: str | None = None
    designated_forwarder_preferences: list[str] | None = None
    dont_preempt: bool | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settingsTruncate(BaseModel):
    enabled: bool | None = None
    size: int | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settingsAccess_group(BaseModel):
    type: str | None = None
    name: str | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settings(BaseModel):
    encapsulation_gre_metadata_tx: bool | None = None
    header_remove_size: int | None = None
    access_group: Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settingsAccess_group | None = None
    rate_limit_per_ingress_chip: str | None = None
    rate_limit_per_egress_chip: str | None = None
    sample: int | None = None
    truncate: Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settingsTruncate | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitemSource_settingsAccess_group(BaseModel):
    type: str | None = None
    name: str | None = None
    priority: int | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitemSource_settings(BaseModel):
    direction: str | None = None
    access_group: Eos_designsNetwork_portsitemMonitor_sessionsitemSource_settingsAccess_group | None = None


class Eos_designsNetwork_portsitemMonitor_sessionsitem(BaseModel):
    name: str = None
    role: str | None = None
    source_settings: Eos_designsNetwork_portsitemMonitor_sessionsitemSource_settings | None = None
    session_settings: Eos_designsNetwork_portsitemMonitor_sessionsitemSession_settings | None = None


class Eos_designsNetwork_portsitemStorm_controlUnknown_unicast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsNetwork_portsitemStorm_controlMulticast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsNetwork_portsitemStorm_controlBroadcast(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsNetwork_portsitemStorm_controlAll(BaseModel):
    level: str | None = None
    unit: str = "percent"


class Eos_designsNetwork_portsitemStorm_control(BaseModel):
    all: Eos_designsNetwork_portsitemStorm_controlAll | None = None
    broadcast: Eos_designsNetwork_portsitemStorm_controlBroadcast | None = None
    multicast: Eos_designsNetwork_portsitemStorm_controlMulticast | None = None
    unknown_unicast: Eos_designsNetwork_portsitemStorm_controlUnknown_unicast | None = None


class Eos_designsNetwork_portsitemPoeLimit(BaseModel):
    class: int | None = None
    watts: str | None = None
    fixed: bool | None = None


class Eos_designsNetwork_portsitemPoeShutdown(BaseModel):
    action: str | None = None


class Eos_designsNetwork_portsitemPoeLink_down(BaseModel):
    action: str | None = None
    power_off_delay: int | None = None


class Eos_designsNetwork_portsitemPoeReboot(BaseModel):
    action: str | None = None


class Eos_designsNetwork_portsitemPoe(BaseModel):
    disabled: bool = False
    priority: str | None = None
    reboot: Eos_designsNetwork_portsitemPoeReboot | None = None
    link_down: Eos_designsNetwork_portsitemPoeLink_down | None = None
    shutdown: Eos_designsNetwork_portsitemPoeShutdown | None = None
    limit: Eos_designsNetwork_portsitemPoeLimit | None = None
    negotiation_lldp: bool | None = None
    legacy_detect: bool | None = None


class Eos_designsNetwork_portsitemDot1xTimeout(BaseModel):
    idle_host: int | None = None
    quiet_period: int | None = None
    reauth_period: str | None = None
    reauth_timeout_ignore: bool | None = None
    tx_period: int | None = None


class Eos_designsNetwork_portsitemDot1xMac_based_authentication(BaseModel):
    enabled: bool | None = None
    always: bool | None = None
    host_mode_common: bool | None = None


class Eos_designsNetwork_portsitemDot1xHost_mode(BaseModel):
    mode: str | None = None
    multi_host_authenticated: bool | None = None


class Eos_designsNetwork_portsitemDot1xAuthentication_failure(BaseModel):
    action: str | None = None
    allow_vlan: int | None = None


class Eos_designsNetwork_portsitemDot1xPae(BaseModel):
    mode: str | None = None


class Eos_designsNetwork_portsitemDot1x(BaseModel):
    port_control: str | None = None
    port_control_force_authorized_phone: bool | None = None
    reauthentication: bool | None = None
    pae: Eos_designsNetwork_portsitemDot1xPae | None = None
    authentication_failure: Eos_designsNetwork_portsitemDot1xAuthentication_failure | None = None
    host_mode: Eos_designsNetwork_portsitemDot1xHost_mode | None = None
    mac_based_authentication: Eos_designsNetwork_portsitemDot1xMac_based_authentication | None = None
    timeout: Eos_designsNetwork_portsitemDot1xTimeout | None = None
    reauthorization_request_limit: int | None = None


class Eos_designsNetwork_portsitemLink_tracking(BaseModel):
    enabled: bool | None = None
    name: str | None = None


class Eos_designsNetwork_portsitemPtp(BaseModel):
    enabled: bool = False
    endpoint_role: str = "follower"
    profile: str = "aes67-r16-2016"


class Eos_designsNetwork_portsitemFlowcontrol(BaseModel):
    received: str | None = None


class Eos_designsNetwork_portsitem(BaseModel):
    switches: list[str] | None = None
    switch_ports: list[str] | None = None
    description: str | None = None
    speed: str | None = None
    profile: str | None = None
    enabled: bool = True
    mode: str | None = None
    mtu: int | None = None
    l2_mtu: int | None = None
    native_vlan: int | None = None
    native_vlan_tag: bool = False
    trunk_groups: list[str] | None = None
    vlans: str | None = None
    spanning_tree_portfast: str | None = None
    spanning_tree_bpdufilter: str | None = None
    spanning_tree_bpduguard: str | None = None
    flowcontrol: Eos_designsNetwork_portsitemFlowcontrol | None = None
    qos_profile: str | None = None
    ptp: Eos_designsNetwork_portsitemPtp | None = None
    link_tracking: Eos_designsNetwork_portsitemLink_tracking | None = None
    dot1x: Eos_designsNetwork_portsitemDot1x | None = None
    poe: Eos_designsNetwork_portsitemPoe | None = None
    storm_control: Eos_designsNetwork_portsitemStorm_control | None = None
    monitor_sessions: list[Eos_designsNetwork_portsitemMonitor_sessionsitem] | None = None
    ethernet_segment: Eos_designsNetwork_portsitemEthernet_segment | None = None
    port_channel: Eos_designsNetwork_portsitemPort_channel | None = None
    raw_eos_cli: str | None = None
    structured_config: dict | None = None


class Eos_designsMlag_ibgp_peering_vrfs(BaseModel):
    base_vlan: int = 3000


class Eos_designsManagement_eapi(BaseModel):
    enable_http: bool = False
    enable_https: bool = True
    default_services: bool | None = None


class Eos_designsMac_address_table(BaseModel):
    aging_time: int | None = None


class Eos_designsLocal_usersitem(BaseModel):
    name: str = None
    disabled: bool | None = None
    privilege: int | None = None
    role: str | None = None
    sha512_password: str | None = None
    no_password: bool | None = None
    ssh_key: str | None = None
    shell: str | None = None


class Eos_designsL3_edgeP2p_linksitemPort_channelNodes_child_interfacesitem(BaseModel):
    node: str = None
    interfaces: list[str] | None = None


class Eos_designsL3_edgeP2p_linksitemPort_channel(BaseModel):
    mode: str = "active"
    nodes_child_interfaces: list[Eos_designsL3_edgeP2p_linksitemPort_channelNodes_child_interfacesitem] | None = None


class Eos_designsL3_edgeP2p_linksitemPtp(BaseModel):
    enabled: bool = False


class Eos_designsL3_edgeP2p_linksitem(BaseModel):
    nodes: list[str] = None
    profile: str | None = None
    id: int | None = None
    speed: str | None = None
    ip_pool: str | None = None
    subnet: str | None = None
    ip: list[str] | None = None
    ipv6_enable: bool = False
    interfaces: list[str] | None = None
    as: list[str] | None = None
    descriptions: list[str] | None = None
    include_in_underlay_protocol: bool = True
    isis_hello_padding: bool = False
    isis_metric: int | None = None
    isis_circuit_type: str | None = None
    isis_authentication_mode: str | None = None
    isis_authentication_key: str | None = None
    mpls_ip: bool | None = None
    mpls_ldp: bool | None = None
    mtu: int | None = None
    bfd: bool = False
    ptp: Eos_designsL3_edgeP2p_linksitemPtp | None = None
    qos_profile: str | None = None
    macsec_profile: str | None = None
    port_channel: Eos_designsL3_edgeP2p_linksitemPort_channel | None = None
    raw_eos_cli: str | None = None


class Eos_designsL3_edgeP2p_links_profilesitemPort_channelNodes_child_interfacesitem(BaseModel):
    node: str = None
    interfaces: list[str] | None = None


class Eos_designsL3_edgeP2p_links_profilesitemPort_channel(BaseModel):
    mode: str = "active"
    nodes_child_interfaces: list[Eos_designsL3_edgeP2p_links_profilesitemPort_channelNodes_child_interfacesitem] | None = None


class Eos_designsL3_edgeP2p_links_profilesitemPtp(BaseModel):
    enabled: bool = False


class Eos_designsL3_edgeP2p_links_profilesitem(BaseModel):
    name: str = None
    id: int | None = None
    speed: str | None = None
    ip_pool: str | None = None
    subnet: str | None = None
    ip: list[str] | None = None
    ipv6_enable: bool = False
    nodes: list[str] | None = None
    interfaces: list[str] | None = None
    as: list[str] | None = None
    descriptions: list[str] | None = None
    include_in_underlay_protocol: bool = True
    isis_hello_padding: bool = False
    isis_metric: int | None = None
    isis_circuit_type: str | None = None
    isis_authentication_mode: str | None = None
    isis_authentication_key: str | None = None
    mpls_ip: bool | None = None
    mpls_ldp: bool | None = None
    mtu: int | None = None
    bfd: bool = False
    ptp: Eos_designsL3_edgeP2p_links_profilesitemPtp | None = None
    qos_profile: str | None = None
    macsec_profile: str | None = None
    port_channel: Eos_designsL3_edgeP2p_links_profilesitemPort_channel | None = None
    raw_eos_cli: str | None = None


class Eos_designsL3_edgeP2p_links_ip_poolsitem(BaseModel):
    name: str = None
    ipv4_pool: str | None = None
    prefix_size: int = 31


class Eos_designsL3_edge(BaseModel):
    p2p_links_ip_pools: list[Eos_designsL3_edgeP2p_links_ip_poolsitem] | None = None
    p2p_links_profiles: list[Eos_designsL3_edgeP2p_links_profilesitem] | None = None
    p2p_links: list[Eos_designsL3_edgeP2p_linksitem] | None = None


class Eos_designsIsis_ti_lfa(BaseModel):
    enabled: bool = False
    protection: str | None = None
    local_convergence_delay: int = 10000


class Eos_designsInternal_vlan_orderRange(BaseModel):
    beginning: int = None
    ending: int = None


class Eos_designsInternal_vlan_order(BaseModel):
    allocation: str = None
    range: Eos_designsInternal_vlan_orderRange | None = None


class Eos_designsHardware_countersFeaturesitem(BaseModel):
    name: str | None = None
    direction: str | None = None
    address_type: str | None = None
    layer3: bool | None = None
    vrf: str | None = None
    prefix: str | None = None
    units_packets: bool | None = None


class Eos_designsHardware_counters(BaseModel):
    features: list[Eos_designsHardware_countersFeaturesitem] | None = None


class Eos_designsFabric_ip_addressingMlag(BaseModel):
    algorithm: str = "first_id"


class Eos_designsFabric_ip_addressing(BaseModel):
    mlag: Eos_designsFabric_ip_addressingMlag | None = None


class Eos_designsEvpn_hostflap_detection(BaseModel):
    enabled: bool = True
    threshold: int = 5
    window: int = 180
    expiry_timeout: int | None = None


class Eos_designsEvent_handlersitem(BaseModel):
    name: str | None = None
    action_type: str | None = None
    action: str | None = None
    delay: int | None = None
    trigger: str | None = None
    regex: str | None = None
    asynchronous: bool = False


class Eos_designsEos_designs_documentation(BaseModel):
    connected_endpoints: bool = False


class Eos_designsEos_designs_custom_templatesitemOptions(BaseModel):
    list_merge: str = "append_rp"
    strip_empty_keys: bool = True


class Eos_designsEos_designs_custom_templatesitem(BaseModel):
    template: str = None
    options: Eos_designsEos_designs_custom_templatesitemOptions | None = None


class Eos_designsDesign(BaseModel):
    type: str = "l3ls-evpn"


class Eos_designsDefault_node_typesitem(BaseModel):
    node_type: str = None
    match_hostnames: list[str] = None


class Eos_designsDefault_interfacesitem(BaseModel):
    types: list[str] = None
    platforms: list[str] = None
    uplink_interfaces: list[str] | None = None
    mlag_interfaces: list[str] | None = None
    downlink_interfaces: list[str] | None = None


class Eos_designsCore_interfacesP2p_linksitemPort_channelNodes_child_interfacesitem(BaseModel):
    node: str = None
    interfaces: list[str] | None = None


class Eos_designsCore_interfacesP2p_linksitemPort_channel(BaseModel):
    mode: str = "active"
    nodes_child_interfaces: list[Eos_designsCore_interfacesP2p_linksitemPort_channelNodes_child_interfacesitem] | None = None


class Eos_designsCore_interfacesP2p_linksitemPtp(BaseModel):
    enabled: bool = False


class Eos_designsCore_interfacesP2p_linksitem(BaseModel):
    nodes: list[str] = None
    profile: str | None = None
    id: int | None = None
    speed: str | None = None
    ip_pool: str | None = None
    subnet: str | None = None
    ip: list[str] | None = None
    ipv6_enable: bool = False
    interfaces: list[str] | None = None
    as: list[str] | None = None
    descriptions: list[str] | None = None
    include_in_underlay_protocol: bool = True
    isis_hello_padding: bool = False
    isis_metric: int | None = None
    isis_circuit_type: str | None = None
    isis_authentication_mode: str | None = None
    isis_authentication_key: str | None = None
    mpls_ip: bool | None = None
    mpls_ldp: bool | None = None
    mtu: int | None = None
    bfd: bool = False
    ptp: Eos_designsCore_interfacesP2p_linksitemPtp | None = None
    qos_profile: str | None = None
    macsec_profile: str | None = None
    port_channel: Eos_designsCore_interfacesP2p_linksitemPort_channel | None = None
    raw_eos_cli: str | None = None


class Eos_designsCore_interfacesP2p_links_profilesitemPort_channelNodes_child_interfacesitem(BaseModel):
    node: str = None
    interfaces: list[str] | None = None


class Eos_designsCore_interfacesP2p_links_profilesitemPort_channel(BaseModel):
    mode: str = "active"
    nodes_child_interfaces: list[Eos_designsCore_interfacesP2p_links_profilesitemPort_channelNodes_child_interfacesitem] | None = None


class Eos_designsCore_interfacesP2p_links_profilesitemPtp(BaseModel):
    enabled: bool = False


class Eos_designsCore_interfacesP2p_links_profilesitem(BaseModel):
    name: str = None
    id: int | None = None
    speed: str | None = None
    ip_pool: str | None = None
    subnet: str | None = None
    ip: list[str] | None = None
    ipv6_enable: bool = False
    nodes: list[str] | None = None
    interfaces: list[str] | None = None
    as: list[str] | None = None
    descriptions: list[str] | None = None
    include_in_underlay_protocol: bool = True
    isis_hello_padding: bool = False
    isis_metric: int | None = None
    isis_circuit_type: str | None = None
    isis_authentication_mode: str | None = None
    isis_authentication_key: str | None = None
    mpls_ip: bool | None = None
    mpls_ldp: bool | None = None
    mtu: int | None = None
    bfd: bool = False
    ptp: Eos_designsCore_interfacesP2p_links_profilesitemPtp | None = None
    qos_profile: str | None = None
    macsec_profile: str | None = None
    port_channel: Eos_designsCore_interfacesP2p_links_profilesitemPort_channel | None = None
    raw_eos_cli: str | None = None


class Eos_designsCore_interfacesP2p_links_ip_poolsitem(BaseModel):
    name: str = None
    ipv4_pool: str | None = None
    prefix_size: int = 31


class Eos_designsCore_interfaces(BaseModel):
    p2p_links_ip_pools: list[Eos_designsCore_interfacesP2p_links_ip_poolsitem] | None = None
    p2p_links_profiles: list[Eos_designsCore_interfacesP2p_links_profilesitem] | None = None
    p2p_links: list[Eos_designsCore_interfacesP2p_linksitem] | None = None


class Eos_designsConnected_endpoints_keysitem(BaseModel):
    key: str | None = None
    type: str | None = None
    description: str | None = None


class Eos_designsBgp_peer_groupsIpvpn_gateway_peers(BaseModel):
    name: str = "IPVPN-GATEWAY-PEERS"
    password: str | None = None
    bfd: bool = True
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsRr_overlay_peers(BaseModel):
    name: str = "RR-OVERLAY-PEERS"
    password: str | None = None
    bfd: bool = True
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsMpls_overlay_peers(BaseModel):
    name: str = "MPLS-OVERLAY-PEERS"
    password: str | None = None
    bfd: bool = True
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsEvpn_overlay_core(BaseModel):
    name: str = "EVPN-OVERLAY-CORE"
    password: str | None = None
    bfd: bool = True
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsEvpn_overlay_peers(BaseModel):
    name: str = "EVPN-OVERLAY-PEERS"
    password: str | None = None
    bfd: bool = True
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsMlag_ipv4_underlay_peer(BaseModel):
    name: str = "MLAG-IPv4-UNDERLAY-PEER"
    password: str | None = None
    bfd: bool = False
    structured_config: dict | None = None


class Eos_designsBgp_peer_groupsIpv4_underlay_peers(BaseModel):
    name: str = "IPv4-UNDERLAY-PEERS"
    password: str | None = None
    bfd: bool = False
    structured_config: dict | None = None


class Eos_designsBgp_peer_groups(BaseModel):
    ipv4_underlay_peers: Eos_designsBgp_peer_groupsIpv4_underlay_peers | None = None
    mlag_ipv4_underlay_peer: Eos_designsBgp_peer_groupsMlag_ipv4_underlay_peer | None = None
    evpn_overlay_peers: Eos_designsBgp_peer_groupsEvpn_overlay_peers | None = None
    evpn_overlay_core: Eos_designsBgp_peer_groupsEvpn_overlay_core | None = None
    mpls_overlay_peers: Eos_designsBgp_peer_groupsMpls_overlay_peers | None = None
    rr_overlay_peers: Eos_designsBgp_peer_groupsRr_overlay_peers | None = None
    ipvpn_gateway_peers: Eos_designsBgp_peer_groupsIpvpn_gateway_peers | None = None
    IPv4_UNDERLAY_PEERS: dict | None = None
    MLAG_IPv4_UNDERLAY_PEER: dict | None = None
    EVPN_OVERLAY_PEERS: dict | None = None


class Eos_designsBgp_graceful_restart(BaseModel):
    enabled: bool = False
    restart_time: int = 300


class Eos_designsBgp_distance(BaseModel):
    external_routes: int = None
    internal_routes: int = None
    local_routes: int = None


class Eos_designsBfd_multihop(BaseModel):
    interval: int = None
    min_rx: int = None
    multiplier: int = None


class Eos_designs(BaseModel):
    avd_data_conversion_mode: str = "debug"
    avd_data_validation_mode: str = "warning"
    bfd_multihop: Eos_designsBfd_multihop = {'interval': 300, 'min_rx': 300, 'multiplier': 3}
    bgp_as: str | None = None
    bgp_default_ipv4_unicast: bool = False
    bgp_distance: Eos_designsBgp_distance | None = None
    bgp_ecmp: int = 4
    bgp_graceful_restart: Eos_designsBgp_graceful_restart | None = None
    bgp_maximum_paths: int = 4
    bgp_mesh_pes: bool = False
    bgp_peer_groups: Eos_designsBgp_peer_groups | None = None
    bgp_update_wait_install: bool | None = None
    bgp_update_wait_for_convergence: bool | None = None
    connected_endpoints_keys: list[Eos_designsConnected_endpoints_keysitem] = [{"key": "servers", "type": "server", "description": "Server"}, {"key": "firewalls", "type": "firewall", "description": "Firewall"}, {"key": "routers", "type": "router", "description": "Router"}, {"key": "load_balancers", "type": "load_balancer", "description": "Load Balancer"}, {"key": "storage_arrays", "type": "storage_array", "description": "Storage Array"}, {"key": "cpes", "type": "cpe", "description": "CPE"}, {"key": "workstations", "type": "workstation", "description": "Workstation"}, {"key": "access_points", "type": "access_point", "description": "Access Point"}, {"key": "phones", "type": "phone", "description": "Phone"}, {"key": "printers", "type": "printer", "description": "Printer"}, {"key": "cameras", "type": "camera", "description": "Camera"}, {"key": "generic_devices", "type": "generic_device", "description": "Generic Device"}]
    core_interfaces: Eos_designsCore_interfaces | None = None
    custom_structured_configuration_list_merge: str = "append_rp"
    custom_structured_configuration_prefix: list[str] = ["custom_structured_configuration_"]
    cvp_ingestauth_key: str | None = None
    cvp_instance_ip: str | None = None
    cvp_instance_ips: list[str] | None = None
    cvp_token_file: str | None = None
    dc_name: str | None = None
    default_igmp_snooping_enabled: bool = True
    default_interfaces: list[Eos_designsDefault_interfacesitem] | None = None
    default_node_types: list[Eos_designsDefault_node_typesitem] | None = None
    design: Eos_designsDesign | None = None
    enable_trunk_groups: bool = False
    eos_designs_custom_templates: list[Eos_designsEos_designs_custom_templatesitem] | None = None
    eos_designs_documentation: Eos_designsEos_designs_documentation | None = None
    event_handlers: list[Eos_designsEvent_handlersitem] | None = None
    evpn_ebgp_gateway_inter_domain: bool | None = None
    evpn_ebgp_gateway_multihop: int = 15
    evpn_ebgp_multihop: int = 3
    evpn_hostflap_detection: Eos_designsEvpn_hostflap_detection | None = None
    evpn_import_pruning: bool = False
    evpn_multicast: bool = False
    evpn_overlay_bgp_rtc: bool = False
    evpn_prevent_readvertise_to_server: bool = False
    evpn_rd_type: dict | None = None
    evpn_rt_type: dict | None = None
    evpn_short_esi_prefix: str = "0000:0000:"
    evpn_vlan_aware_bundles: bool = False
    fabric_evpn_encapsulation: str = "vxlan"
    fabric_ip_addressing: Eos_designsFabric_ip_addressing | None = None
    fabric_name: str = None
    hardware_counters: Eos_designsHardware_counters | None = None
    internal_vlan_order: Eos_designsInternal_vlan_order = {'allocation': 'ascending', 'range': {'beginning': 1006, 'ending': 1199}}
    ipv6_mgmt_destination_networks: list[str] | None = None
    ipv6_mgmt_gateway: str | None = None
    is_deployed: bool = True
    isis_advertise_passive_only: bool = False
    isis_area_id: str = "49.0001"
    isis_default_circuit_type: str = "level-2"
    isis_default_is_type: str = "level-2"
    isis_default_metric: int = 50
    isis_maximum_paths: int | None = None
    isis_ti_lfa: Eos_designsIsis_ti_lfa | None = None
    l3_edge: Eos_designsL3_edge | None = None
    local_users: list[Eos_designsLocal_usersitem] | None = None
    mac_address_table: Eos_designsMac_address_table | None = None
    management_eapi: Eos_designsManagement_eapi | None = None
    mgmt_destination_networks: list[str] | None = None
    mgmt_gateway: str | None = None
    mgmt_interface: str = "Management1"
    mgmt_interface_description: str = "oob_management"
    mgmt_interface_vrf: str = "MGMT"
    mgmt_vrf_routing: bool = False
    mlag_ibgp_peering_vrfs: Eos_designsMlag_ibgp_peering_vrfs | None = None
    name_servers: list[str] | None = None
    network_ports: list[Eos_designsNetwork_portsitem] | None = None
    network_services_keys: list[Eos_designsNetwork_services_keysitem] = [{"name": "tenants"}]
    node_type_keys: list[Eos_designsNode_type_keysitem] | None = None
    only_local_vlan_trunk_groups: bool = False
    overlay_cvx_servers: list[str] | None = None
    overlay_her_flood_list_per_vni: bool = False
    overlay_her_flood_list_scope: str = "fabric"
    overlay_loopback_description: str | None = None
    overlay_mlag_rfc5549: bool = False
    overlay_rd_type: Eos_designsOverlay_rd_type | None = None
    overlay_routing_protocol: str = "ebgp"
    overlay_routing_protocol_address_family: str = "ipv4"
    overlay_rt_type: Eos_designsOverlay_rt_type | None = None
    p2p_uplinks_mtu: int = 9214
    p2p_uplinks_qos_profile: str | None = None
    platform_settings: list[Eos_designsPlatform_settingsitem] = [{"platforms": ["default"], "feature_support": {"queue_monitor_length_notify": False}, "reload_delay": {"mlag": 300, "non_mlag": 330}}, {"platforms": ["7050X3", "720XP", "722XP"], "feature_support": {"queue_monitor_length_notify": False}, "reload_delay": {"mlag": 300, "non_mlag": 330}, "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072"}, {"platforms": ["7280R", "7280R2", "7020R"], "lag_hardware_only": True, "reload_delay": {"mlag": 900, "non_mlag": 1020}, "tcam_profile": "vxlan-routing"}, {"platforms": ["7280R3"], "reload_delay": {"mlag": 900, "non_mlag": 1020}}, {"platforms": ["7500R", "7500R2"], "lag_hardware_only": True, "management_interface": "Management0", "reload_delay": {"mlag": 900, "non_mlag": 1020}, "tcam_profile": "vxlan-routing"}, {"platforms": ["7500R3", "7800R3"], "management_interface": "Management0", "reload_delay": {"mlag": 900, "non_mlag": 1020}}, {"platforms": ["7368X4"], "management_interface": "Management0", "reload_delay": {"mlag": 300, "non_mlag": 330}}, {"platforms": ["7300X3"], "management_interface": "Management0", "reload_delay": {"mlag": 1200, "non_mlag": 1320}, "trident_forwarding_table_partition": "flexible exact-match 16384 l2-shared 98304 l3-shared 131072"}, {"platforms": ["VEOS", "VEOS-LAB", "vEOS", "vEOS-lab"], "feature_support": {"bgp_update_wait_for_convergence": False, "bgp_update_wait_install": False, "interface_storm_control": False, "queue_monitor_length_notify": False}, "reload_delay": {"mlag": 300, "non_mlag": 330}}, {"platforms": ["CEOS", "cEOS", "ceos", "cEOSLab"], "feature_support": {"bgp_update_wait_for_convergence": False, "bgp_update_wait_install": False, "interface_storm_control": False, "queue_monitor_length_notify": False}, "management_interface": "Management0", "reload_delay": {"mlag": 300, "non_mlag": 330}}]
    platform_speed_groups: list[Eos_designsPlatform_speed_groupsitem] | None = None
    pod_name: str | None = None
    port_profiles: list[Eos_designsPort_profilesitem] | None = None
    ptp: Eos_designsPtp | None = None
    ptp_profiles: list[Eos_designsPtp_profilesitem] = [{"announce": {"interval": 0, "timeout": 3}, "delay_req": -3, "profile": "aes67-r16-2016", "sync_message": {"interval": -3}, "transport": "ipv4"}, {"announce": {"interval": -2, "timeout": 3}, "delay_req": -4, "profile": "smpte2059-2", "sync_message": {"interval": -4}, "transport": "ipv4"}, {"announce": {"interval": 2, "timeout": 3}, "delay_req": 0, "profile": "aes67", "sync_message": {"interval": 0}, "transport": "ipv4"}]
    queue_monitor_length: Eos_designsQueue_monitor_length | None = None
    redundancy: Eos_designsRedundancy | None = None
    serial_number: str | None = None
    shutdown_interfaces_towards_undeployed_peers: bool = False
    snmp_settings: Eos_designsSnmp_settings | None = None
    svi_profiles: list[Eos_designsSvi_profilesitem] | None = None
    system_mac_address: str | None = None
    terminattr_disable_aaa: bool = False
    terminattr_ingestexclude: str = "/Sysdb/cell/1/agent,/Sysdb/cell/2/agent"
    terminattr_ingestgrpcurl_port: int = 9910
    terminattr_smashexcludes: str = "ale,flexCounter,hardware,kni,pulse,strata"
    timezone: str | None = None
    trunk_groups: Eos_designsTrunk_groups | None = None
    type: str | None = None
    underlay_filter_peer_as: bool = False
    underlay_filter_redistribute_connected: bool = True
    underlay_ipv6: bool = False
    underlay_isis_instance_name: str | None = None
    underlay_multicast: bool = False
    underlay_multicast_anycast_rp: Eos_designsUnderlay_multicast_anycast_rp | None = None
    underlay_multicast_rps: list[Eos_designsUnderlay_multicast_rpsitem] | None = None
    underlay_ospf_area: str = "0.0.0.0"
    underlay_ospf_bfd_enable: bool = False
    underlay_ospf_max_lsa: int = 12000
    underlay_ospf_process_id: int = 100
    underlay_rfc5549: bool = False
    underlay_routing_protocol: str | None = None
    uplink_ptp: Eos_designsUplink_ptp | None = None
    vtep_vvtep_ip: str | None = None
    vxlan_vlan_aware_bundles: bool = False
