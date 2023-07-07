from pydantic import BaseModel


class AvdfactsSwitchIpvpn_gateway(BaseModel):
    evpn_domain_id: str = "0:1"
    ipvpn_domain_id: str = "0:2"
    max_routes: int = 0
    local_as: str | None = None
    remote_peers: list[dict] = []


class AvdfactsSwitchOverlay(BaseModel):
    peering_address: str | None = None
    ler: bool = None
    vtep: bool = None
    evpn: bool = None
    evpn_vxlan: bool = None
    evpn_mpls: bool = None
    vpn_ipv4: bool = None
    vpn_ipv6: bool = None
    ipvpn_gateway: bool = None
    dpath: bool = None


class AvdfactsSwitchUnderlay(BaseModel):
    bgp: bool = None
    ldp: bool = None
    mpls: bool = None
    sr: bool = None
    ospf: bool = None
    isis: bool = None


class AvdfactsSwitchMlag_switch_ids(BaseModel):
    primary: int | None = None
    secondary: int | None = None


class AvdfactsSwitchTrunk_groupsUplink(BaseModel):
    name: str = "UPLINK"


class AvdfactsSwitchTrunk_groupsMlag_l3(BaseModel):
    name: str = "LEAF_PEER_L3"


class AvdfactsSwitchTrunk_groupsMlag(BaseModel):
    name: str = "MLAG"


class AvdfactsSwitchTrunk_groups(BaseModel):
    mlag: AvdfactsSwitchTrunk_groupsMlag | None = None
    mlag_l3: AvdfactsSwitchTrunk_groupsMlag_l3 | None = None
    uplink: AvdfactsSwitchTrunk_groupsUplink | None = None


class AvdfactsSwitchLacp_port_id(BaseModel):
    begin: int | None = None
    end: int | None = None


class AvdfactsSwitchUplink_ptp(BaseModel):
    enable: bool | None = None


class AvdfactsSwitch(BaseModel):
    type: str = None
    hostname: str = None
    node_type_key: str = None
    connected_endpoints: bool = False
    default_downlink_interfaces: list[str] = []
    default_evpn_role: str = "none"
    default_interfaces: dict = {}
    default_underlay_routing_protocol: str = "ebgp"
    default_overlay_routing_protocol: str = "ebgp"
    default_overlay_address_families: list[str] = ["evpn"]
    default_mpls_overlay_role: str = "none"
    mpls_lsr: bool = False
    mlag_support: bool = False
    network_services_l1: bool = False
    network_services_l2: bool = False
    network_services_l3: bool = False
    underlay_router: bool = True
    uplink_type: str = "p2p"
    vtep: bool = False
    ip_addressing: dict = {}
    interface_descriptions: dict = {}
    group: str | None = None
    id: int = None
    mgmt_ip: str | None = None
    platform: str | None = None
    max_parallel_uplinks: int = 1
    uplink_switches: list[str] | None = None
    uplink_interfaces: list[str] = []
    uplink_switch_interfaces: list[str] | None = None
    uplink_interface_speed: str | None = None
    uplink_bfd: bool | None = None
    uplink_ptp: AvdfactsSwitchUplink_ptp | None = None
    default_ptp_priority1: int = 127
    ptp: dict | None = None
    uplink_macsec: bool | None = None
    uplink_structured_config: dict | None = None
    short_esi: str | None = None
    rack: str | None = None
    raw_eos_cli: str | None = None
    struct_cfg: dict | None = None
    max_uplink_switches: int = None
    is_deployed: bool = True
    platform_settings: dict = {}
    mgmt_interface: str | None = None
    system_mac_address: str | None = None
    underlay_routing_protocol: str = None
    overlay_routing_protocol: str = None
    overlay_address_families: list[str] = []
    link_tracking_groups: list[dict] | None = None
    lacp_port_id: AvdfactsSwitchLacp_port_id | None = None
    filter_tenants: list[str] = ["all"]
    always_include_vrfs_in_tenants: list[str] | None = None
    filter_tags: list[str] = ["all"]
    filter_only_vlans_in_use: bool = False
    virtual_router_mac_address: str | None = None
    trunk_groups: AvdfactsSwitchTrunk_groups | None = None
    enable_trunk_groups: bool | None = None
    only_local_vlan_trunk_groups: bool | None = None
    endpoint_trunk_groups: list = []
    vlans: str = ""
    spanning_tree_mode: str | None = None
    spanning_tree_priority: int | None = None
    spanning_tree_root_super: bool | None = None
    underlay_multicast: bool | None = None
    overlay_rd_type_admin_subfield: str = None
    evpn_multicast: bool | None = None
    multi_vtep: bool | None = None
    igmp_snooping_enabled: bool | None = None
    loopback_ipv4_pool: str | None = None
    loopback_ipv4_offset: int | None = None
    uplink_ipv4_pool: str | None = None
    router_id: str | None = None
    evpn_gateway_vxlan_l2: bool | None = None
    evpn_gateway_vxlan_l3: bool | None = None
    evpn_gateway_vxlan_l3_inter_domain: bool | None = None
    evpn_gateway_remote_peers: list[dict] | None = None
    bgp_defaults: list[str] | None = None
    bgp_cluster_id: str | None = None
    bgp_peer_groups: dict | None = None
    evpn_role: str | None = None
    mpls_overlay_role: str | None = None
    bgp_as: str | None = None
    evpn_route_servers: list[str] = []
    mpls_route_reflectors: list[str] | None = None
    isis_net: str | None = None
    is_type: str | None = None
    isis_instance_name: str | None = None
    node_sid: str | None = None
    underlay_ipv6: bool | None = None
    loopback_ipv6_pool: str | None = None
    loopback_ipv6_offset: int | None = None
    ipv6_router_id: str | None = None
    mlag: bool = None
    mlag_ibgp_origin_incomplete: bool | None = None
    mlag_peer_vlan: int | None = None
    mlag_peer_link_allowed_vlans: str | None = None
    mlag_dual_primary_detection: bool | None = None
    mlag_interfaces: list[str] | None = None
    mlag_interfaces_speed: str | None = None
    mlag_peer_ipv4_pool: str | None = None
    mlag_peer_l3_ipv4_pool: str | None = None
    mlag_port_channel_structured_config: dict | None = None
    mlag_peer_vlan_structured_config: dict | None = None
    mlag_peer_l3_vlan_structured_config: dict | None = None
    mlag_role: str | None = None
    mlag_peer: str | None = None
    mlag_l3: bool | None = None
    mlag_peer_l3_vlan: int | None = None
    mlag_port_channel_id: int | None = None
    vtep_loopback_ipv4_pool: str | None = None
    vtep_loopback: str | None = None
    inband_management_subnet: str | None = None
    inband_management_role: str | None = None
    inband_management_parents: list[str] | None = None
    inband_management_vlan: int | None = None
    inband_management_ip: str | None = None
    inband_management_gateway: str | None = None
    inband_management_interface: str | None = None
    uplinks: list[dict] = []
    uplink_peers: list[str] = []
    mlag_switch_ids: AvdfactsSwitchMlag_switch_ids | None = None
    vtep_ip: str | None = None
    mlag_ip: str | None = None
    mlag_peer_ip: str | None = None
    mlag_l3_ip: str | None = None
    mlag_peer_l3_ip: str | None = None
    mlag_peer_mgmt_ip: str | None = None
    overlay_routing_protocol_address_family: str = "ipv4"
    bgp: bool = None
    evpn_encapsulation: str = "vxlan"
    underlay: AvdfactsSwitchUnderlay = None
    overlay: AvdfactsSwitchOverlay = None
    ipvpn_gateway: AvdfactsSwitchIpvpn_gateway | None = None


class Avdfacts(BaseModel):
    switch: AvdfactsSwitch = None
