# Ansible Role: eos_cli_config_gen

**Table of Contents:**

- [Ansible Role: eos_cli_config_gen](#ansible-role-eoscliconfiggen)
  - [Overview](#overview)
  - [Role Inputs and Outputs](#role-inputs-and-outputs)
  - [Requirements](#requirements)
  - [Input Variables](#input-variables)
    - [Terminal Settings](#terminal-settings)
    - [Aliases](#aliases)
    - [Hardware Counters](#hardware-counters)
    - [Daemon TerminAttr](#daemon-terminattr)
    - [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
    - [Event Monitor](#event-monitor)
    - [Event Handler](#event-handler)
    - [Load Interval](#load-interval)
    - [Queue Monitor Length](#queue-monitor-length)
    - [Logging](#logging)
    - [Domain Lookup](#domain-lookup)
    - [Name Servers](#name-servers)
    - [DNS Domain](#dns-domain)
    - [NTP Servers](#ntp-servers)
    - [Sflow](#sflow)
    - [redundancy](#redundancy)
    - [SNMP Settings](#snmp-settings)
    - [Spanning Tree](#spanning-tree)
    - [Tacacs+ Servers](#tacacs-servers)
    - [AAA Server Groups](#aaa-server-groups)
    - [AAA Authentication](#aaa-authentication)
    - [AAA Authorization](#aaa-authorization)
    - [Local users](#local-users)
    - [clock timezone](#clock-timezone)
    - [VLANs](#vlans)
    - [VRF Instances](#vrf-instances)
    - [bfd multihop interval](#bfd-multihop-interval)
    - [Port-Channel Interfaces](#port-channel-interfaces)
    - [Ethernet Interfaces](#ethernet-interfaces)
    - [Loopback Interfaces](#loopback-interfaces)
    - [Management Interfaces](#management-interfaces)
    - [VLAN Interfaces](#vlan-interfaces)
    - [VxLAN interface](#vxlan-interface)
    - [Hardware TCAM Profiles](#hardware-tcam-profiles)
    - [MAC address-table](#mac-address-table)
    - [Router Virtual MAC Address](#router-virtual-mac-address)
    - [Virtual Source NAT](#virtual-source-nat)
    - [Static Routes](#static-routes)
    - [IPv6 Static Routes](#ipv6-static-routes)
    - [Prefix Lists](#prefix-lists)
    - [MLAG Configuration](#mlag-configuration)
    - [Route Maps](#route-maps)
    - [Peer Filters](#peer-filters)
    - [Router BGP Configuration](#router-bgp-configuration)
    - [Router OSPF Configuration](#router-ospf-configuration)
    - [Queue Monitor Streaming](#queue-monitor-streaming)
    - [IP TACACS+ Source Interfaces](#ip-tacacs-source-interfaces)
    - [VM Tracer Sessions](#vmtracer-sessions)
    - [Banners](#banners)
    - [HTTP Management API](#http-management-api)
    - [Management Console](#management-console)
    - [Management SSH](#management-ssh)
  - [License](#license)

## Overview

**eos_cli_config_gen**, is a role that generates eos cli syntax and device documentation.

The **eos_cli_config_gen** role:

- Designed to generate the intended configuration offline, without relying on switch current state information.
- Facilitates the evaluation of the configuration prior to deployment with tools like [Batfish](https://www.batfish.org/)

## Role Inputs and Outputs

Figure 1 below provides a visualization of the roles inputs, and outputs and tasks in order executed by the role.

![Figure 1: Ansible Role eos_cli_config_gen](media/figure-1-role-eos_cli_config_gen.gif)

**Inputs:**

- Structured EOS configuration file in yaml format.

**Outputs:**

- EOS configuration in CLI format.
- Device Documentation in Markdown format.

**Tasks:**

1. Include device structured configuration that was previously generated.
2. Generate EOS configuration in CLI format.
3. Generate Device Documentation in Markdown format.

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## Input Variables

- The input variables are documented inline within yaml formated output with: "< >"
- Variables are organized in order of how they appear in the CLI syntax.
- Available features  and variables may vary by platforms, refer to documentation on arista.com for specifics.
- All values are optional. Boolean variables default to "false" unless explicitly stated.

### Terminal Settings

```yaml
terminal:
  length: < integer between 0 and 32767 >
  width: < integer between 0 and 32767 >
```

### Aliases

```yaml
aliases: |
< list of alias commands in EOS CLI >
```

### Hardware Counters

```yaml
hardware_counters:
  features:
    - <feature_1>: < direction | in | out >
    - <feature_1>: < direction | in | out >
```

### Daemon TerminAttr

```yaml
daemon_terminattr:
  ingestgrpcurl:
    ips:
      - < IPv4_address >
      - < IPv4_address >
      - < IPv4_address >
    port: < port_id >
  ingestauth_key: < ingest_key >
  ingestvrf: < vrf_name >
  smashexcludes: "< list as string >"
  ingestexclude: "< list as string >"

```

### Internal VLAN Allocation Policy

```yaml
vlan_internal_allocation_policy:
  allocation: < ascending | descending >
  range:
    beginning: < vlan_id >
    ending: < vlan_id >
```

### Event Monitor

```yaml
event_monitor:
  enabled: < true | false >
```

### Event Handler

```yaml
### Event Handler ###
event_handlers:
  evpn-blacklist-recovery:
    action_type: < Type of action. [bash, increment, log]>
    action: < Command to execute >
    delay: < Event-handler delay in seconds >
    trigger: < Configure event trigger condition. Only supports on-logging >
    regex: < Regular expression to use for searching log messages. Required for on-logging trigger >
    asynchronous: < Set the action to be non-blocking. if unset, default is False >
```

### Load Interval

```yaml
load_interval:
  default: < seconds >

```

### Queue Monitor Length

```yaml
queue_monitor_length:
  log: < seconds >
  notifying: < true | false >
```

### Logging

```yaml
logging:
  console: < severity_level >
  monitor: < severity_level >
  buffered:
    size: < integer between 10 and 2147483647 representing number of messages >
    level: < severity_level >
  trap: < severity_level >
  source_interface:
  vrfs:
    mgt:
      source_interface:
      hosts:
        - < syslog_server_1>
        - < syslog_server_2>
```

### Domain Lookup

```yaml
ip_domain_lookup:
  source_interfaces:
    <source_interface_1>:
      vrf: <vrf_name>
```

### Name Servers

```yaml
name_server:
  source:
    vrf: < vrf_name >
  nodes:
    - < name_server_1 >
    - < name_server_2 >
```

### DNS Domain

```yaml
dns_domain: <domain_name>
```

### NTP Servers

```yaml
ntp_server:
  local_interface:
    vrf: < vrf_name >
    interface: < source_interface >
  nodes:
    - < ntp_server_1 >
    - < ntp_server_2 >
```

### Sflow

```yaml
sflow:
  destinations:
    < sflow_destination_ip_1 >:
    < sflow_destination_ip_2 >:
  source_interface: < interface >
  sample: < integer >
  run: < true | false >
```

### redundancy

```yaml
redundancy:
  protocol: < redundancy_protocol >
```

### Snmp Settings

```yaml
snmp_server:
  contact: < contact_name >
  location: < location >
  local_interfaces:
    - name: < interface_name_1 >
      vrf: < vrf_name >
    - name: < interface_name_2 >  
  views:
    - name: < view_name >
      MIB_family_name: < MIB_family_name >
      included: < true | false >
    - name: < view_name >
      MIB_family_name: < MIB_family_name >
      included: < true | false >
  groups:
    - name: < group_name >
      version: < v1 | v2c | v3 >
      authentication: < auth | noauth | priv >
      read: < read_view >
      write: < write_view >
      notify: < notify_view >
    - name: < group_name >
      version: < v1 | v2c | v3 >
      authentication: < auth | noauth | priv >
      read: < read_view >
  users:
    - name: < user_name >
      group: < group_name >
      version: < v1 | v2c | v3 >
      auth: < md5 | sha | sha224 | sha256 | sha 384 | sha512 >
      auth_passphrase: < encrypted_auth_passphrase >
      priv: < aes | eas192 | aes256 | des >
      priv_passphrase: < encrypted_priv_passphrase >
    - name: < user_name >
      group: < group_name >
      version: < v1 | v2c | v3 >
  hosts:
    - host: < host IP address or name >
      vrf: < vrf_name >
      users:
        - username: < username >
          authentication_level: < auth | noauth | priv >
          version: < 1 | 2c | 3 >
    - host: < host IP address or name >
      vrf: < vrf_name >
      users:
        - username: < username >
          authentication_level: < auth | noauth | priv >
          version: < 1 | 2c | 3 >
  traps:
    enable: < true | false >
  vrfs:
    - name: < vrf_name >
      enable: < true | false >
    - name: < vrf_name >
      enable: < true | false >
```

### Spanning Tree

```yaml
spanning_tree:
  edge_port:
    bpduguard_default: < true | false >
  mode: < spanning_tree_mode >
  priority: < priority_level >
  no_spanning_tree_vlan: < vlan_id >, < vlan_id >-< vlan_id >
```

### Tacacs+ Servers

```yaml
tacacs_servers:
  hosts:
    - host: < host_1_ip_address >
      vrf: < vrf_name >
      key: < encypted_key >
    - host: < host_1_ip_address >
      key: < encypted_key >
```

### AAA Server Groups

```yaml
aaa_server_groups:
  - name: <name_of_the_server_group>
    type: < tacacs+ | radius | ladp >
    servers:
      - <server_1_ip_address>
      - <server_2_ip_address>
  - name: <name_of_the_server_group>
    type: < tacacs+ | radius | ladp >
    servers:
      - <server_1_ip_address>
```

### AAA Authentication

```yaml
aaa_authentication:
  login:
    default: < group | local | none >
    serial_console: < group | local | none >
```

### AAA Authorization

```yaml
aaa_authorization:
  exec_default: < group | local | none >
  config_commands: < true | false >
```

### Local users

```yaml
local_users:
  < user_1 >:
    privilege: < 1-15 >
    role: < role >
    sha512_password: "< sha_512_password >"
  < user_2 >:
    privilege: < 1-15 >
    role: < role >
    sha512_password: "< sha_512_password >"
```

### clock timezone

```yaml
clock:
  timezone: < timezone >
```

### VLANs

```yaml
vlans:
  < vlan_id >:
    name: < vlan_name >
    trunk_groups:
      - < trunk_group_name_1 >
      - < trunk_group_name_2 >
  < vlan_id >:
    name: < vlan_name >
```

### VRF Instances

```yaml
vrfs:
  < vrf_name >:
    description: < description>
    ip_routing: < true | false >
    ipv6_routing: < true | false >
  < vrf_name >:
    description: < description>
    ip_routing: < true | false >
    ipv6_routing: < true | false >
```

### bfd multihop interval

```yaml
bfd_multihop:
  interval: < Rate in milliseconds >
  min_rx: < Rate in milliseconds >
  multiplier: < 3-50 >
```

### Port-Channel Interfaces

```yaml
port_channel_interfaces:
  < Port-Channel_interface_1 >:
    description: < description >
    vlans: "< list of vlans as sting >"
    mode: < access | dot1q-tunnel | trunk >
    mlag: < mlag_id >
    trunk_groups:
      - < trunk_group_name_1 >
      - < trunk_group_name_2 >
  < Port-Channel_interface_1 >:
    description: < description >
    vlans: "< list of vlans as sting >"
    mode: < access | dot1q-tunnel | trunk >
```

### Ethernet Interfaces

```yaml
# Routed Interfaces
ethernet_interfaces:
  <Ethernet_interface_1 >:
    description: < description >
    speed: < interface_speed >
    mtu: < mtu >
    type: routed
    vrf: < vrf_name >
    ip_address: < IPv4_address/Mask >
    ospf_network_point_to_point: < true | false >
    ospf_area: < ospf_area >

# Switched Interfaces
  <Ethernet_interface_2 >:
    description: < description >
    speed: < interface_speed >
    vlans: "< list of vlans as sting >"
    mode: < access | dot1q-tunnel | trunk >
    flowcontrol:
      received: < received | send | on >
    channel_group:
      id: < Port-Channel_id >
      mode: < on | active | passive >
```

### Loopback Interfaces

```yaml
loopback_interfaces:
  < Loopback_interface_1 >:
    description: < description >
    ip_address: < IPv4_address/Mask >
    ospf_area: < ospf_area >
  < Loopback_interface_2 >:
    description: < description >
    ip_address: < IPv4_address/Mask >
```

### Management Interfaces

```yaml
management_interfaces:
  < Management_interface_1:
    description: < description >
    vrf: < vrf_name >
    ip_address: < IPv4_address/Mask >
    ipv6_address: < IPv6_address/Mask >
    ipv6_enable: < true | false >
    gateway: <IPv4 address of gateway>
    ipv6_gateway: <IPv6 address of gateway>
```

### VLAN Interfaces

```yaml
vlan_interfaces:
  < Vlan_id_1 >:
    description: < description >
    vrf: < vrf_name >
    ip_address: < IPv4_address/Mask >
    ip_address_secondary: < IPv4_address/Mask >
    ip_router_virtual_address: < IPv4_address >
    ip_router_virtual_address_secondary: < IPv4_address >
    ip_address_virtual: < IPv4_address/Mask >
    virtual: < true | false >
    mtu: < mtu >
    ip_helpers:
      < ip_helper_address_1 >:
        source_interface: < interface_name >
        vrf: < vrf_name >
      < ip_helper_address_2 >:
        source_interface: < interface_name >
    ospf_network_point_to_point: < true | false >
    ospf_area: < ospf_area >
    pim:
      ipv4:
        sparse_mode: < true | false >
  < Vlan_id_2 >:
    description: < description >
    ip_address: < IPv4_address/Mask >
```

### VxLAN interface

```yaml
vxlan_tunnel_interface:
  Vxlan1:
    description: < description >
    source_interface: < interface >
    virtual_router:
      encapsulation_mac_address: < mlag-system-id | ethernet_address (H.H.H) >
    vxlan_udp_port: < udp_port >
    vxlan_vni_mappings:
      vlans:
        < vlan_id_1 >:
          vni: < vni_id_1 >
        < vlan_id_2 >:
          vni: < vni_id_2 >
      vrfs:
        < vrf_name >:
          vni: < vni_id_3 >
        < vrf_name >:
          vni: < vni_id_4 >
```

### Hardware TCAM Profiles

```yaml
tcam_profile:
  - < tcam_profile >
```

### MAC address-table

```yaml
mac_address_table:
  aging_time: < agin_time_in_seconds >
```

### Router Virtual MAC Address

```yaml
ip_virtual_router_mac_address: < mac_address (hh:hh:hh:hh:hh:hh) >
```

### Virtual Source NAT

```yaml
virtual_source_nat_vrfs:
  < vrf_name_1 >:
    ip_address: < IPv4_address >
  < vrf_name_2 >:
    ip_address: < IPv4_address >
```

### Static Routes

```yaml
static_routes:
  - vrf: < vrf_name, if vrf_name = default the route will be placed in the GRT >
    destination_address_prefix: < IPv4_network/Mask >
    gateway: < IPv4_address >
    distance: < integer between 1 and 255 >
    tag: < integer between 0 and 4294967295 >
    name: < description >
  - destination_address_prefix: < IPv4_network/Mask >
    gateway: < IPv4_address >
```

### IPv6 Static Routes

```yaml
ipv6_static_routes:
  - vrf: < vrf_name, if vrf_name = default the route will be placed in the GRT >
    destination_address_prefix: < IPv6_network/Mask >
    gateway: < IPv6_address >
    distance: < integer between 1 and 255 >
    tag: < integer between 0 and 4294967295 >
    name: < description >
  - destination_address_prefix: < IPv6_network/Mask >
    gateway: < IPv6_address >
```

### Prefix Lists

```yaml
prefix_lists:
  < prefix_list_name_1 >:
    sequence_numbers:
      < sequence_id_1 >:
        action: "< action as string >"
      < sequence_id_2 >:
        action: "< action as string >"
  < prefix_list_name_2 >:
    sequence_numbers:
      < sequence_id_1 >:
        action: "< action as string >"
```

### MLAG Configuration

```yaml
mlag_configuration:
  domain_id: < domain_id_name >
  local_interface: < interface >
  peer_address: < IPv4_address >
  peer_address_heartbeat:
    peer_ip: < IPv4_address >
    vrf: < vrf_name >
  dual_primary_detection_delay: < seconds >
  peer_link: < Port-Channel_id >
  reload_delay_mlag: < seconds >
  reload_delay_non_mlag: < seconds >
```

### Route Maps

```yaml
route_maps:
  < route_map_name_1 >:
    sequence_numbers:
      < sequence_id_1 >:
        type: < permit | deny >
        description: < description >
        match: "< match as string >"
        set: "< set as string >"
      < sequence_id_1 >:
        type: < permit | deny >
        match: "< match as string >"
  < route_map_name_2 >:
    sequence_numbers:
      < sequence_id_1 >:
        type: < permit | deny >
        description: < description >
        set: "< set as string >"
```

### Peer Filters

```yaml
peer_filters:
  < peer_filter_name_1:
    sequence_numbers:
      < sequence_id_1 >:
        match: "< match as string >"
      < sequence_id_2 >:
        match: "< match as string >"
  < peer_filter_name_2:
    sequence_numbers:
      < sequence_id_1 >:
        match: "< match as string >"
```

### Router BGP Configuration

```yaml
router_bgp:
  as: < bgp_as >
  router_id: < IPv4_address >
  bgp_defaults:
    - "< bgp command as string >"
    - "< bgp command as string >"
  peer_groups:
    < peer_group_name_1>:
      type: < ipv4 | evpn >
      peer_filter: < peer_filter >
      next_hop_unchanged: < true | false >
      update_source: < interface >
      fall_over_bfd: < true | false >
      ebgp_multihop: < integer >
      next_hop_self: < true | false >
      password: "< encrypted_password >"
      send_community: < true | false >
      maximum_routes: < integer >
    < peer_group_name_2 >:
      type: < ipv4 | evpn >
      bgp_listen_range_prefix: < IP prefix range >
      peer_filter: < peer_filter >
      password: "< encrypted_password >"
      maximum_routes: < integer >
  neighbors:
    < IPv4_address_1 >:
      peer_group: < peer_group_name >
      remote_as: < bgp_as >
    < IPv4_address_2 >:
      peer_group: < peer_group_name >
      remote_as: < bgp_as >
  redistribute_routes:
    connected:
      route_map: < route_map_name >
  vlan_aware_bundles:
    < vlan_aware_bundle_name_1 >:
      rd: "< route distinguisher >"
      route_targets:
        < both | import | export >:
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
      vlan: < vlan_range >
    < vlan_aware_bundle_name_2 >:
      rd: "< route distinguisher >"
      route_targets:
        < both | import | export >:
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
      vlan: < vlan_range >
  vlans:
    < vlan_id_1>:
      rd: "< route distinguisher >"
      route_targets:
        < both | import | export >:
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
    <vlan_id_2 >:
      rd: "< route distinguisher >"
      route_targets:
        < both | import | export >:
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
  vrfs:
    < vrf_name_1 >:
      rd: "< route distinguisher >"
      route_targets:
        import:
          address_family: < evpn >
          asn: "< asn >"
        export:
          address_family: < evpn >
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
    < vrf_name_2 >:
      rd: "<route distinguisher >"
      route_targets:
        import:
          address_family: < evpn >
          asn: "< asn >"
        export:
          address_family: < evpn >
          asn: "< asn >"
      redistribute_routes:
        - < connected >
        - < learned >
```

### Router OSPF Configuration

```yaml
router_ospf:
  process_ids:
    < process_id >:
      passive_interface_default: < true | false >
      router_id: < IPv4_address >
      no_passive_interfaces:
        - < interface_1 >
        - < interface_2 >
      max_lsa: < integer >
```

### Queue Monitor Streaming

```yaml
queue_monitor_streaming:
  enable: < true | false >
```

### IP TACACS+ Source Interfaces

```yaml
ip_tacacs_source_interfaces:
    - name: <interface_name_1 >
      vrf: < vrf_name_1 >
    - name: <interface_name_2 >
```

### VM Tracer Sessions

```yaml
vmtracer_sessions:
  < vmtracer_session_name_1 >:
    username: < username >
    password: < encrypted_password >
    autovlan_disable: < true | false >
    source_interface: < interface_name >
  < vmtracer_session_name_2 >:  
    username: < username >
    password: < encrypted_password >
```

### Banners

```yaml
banners:
  login: |
    < text ending by EOF >
  motd: |
    < text ending by EOF >
```

### HTTP Management API

```yaml
management_api_http:
  enable_http: < true | false >
  enable_https: < true | false >
  enable_vrfs:
    < vrf_name_1 >:
      access_group: < Standard IPv4 ACL name >
    < vrf_name_2 >:
```

### Management Console

```yaml
management_console:
  idle_timeout: < integer between 0 and 86400 representing minutes >
```

### Management SSH

```yaml
management_ssh:
  access_groups:
    < standard_acl_name_1 >:
    < standard_acl_name_2 >:
      vrf: < vrf name >
  idle_timeout: < integer between 0 and 86400 representing minutes >
  enable: < true | false >
  vrfs:
    < vrf_name_1 >:
      enable: < true | false >
    < vrf_name_2 >:
      enable: < true | false >
```

## License

Project is published under [Apache 2.0 License](../../LICENSE)
