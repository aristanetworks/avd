# Input variables for eos_cli_config_gen

This document describes the supported input variables for the role `arista.avd.eos_cli_config_gen`.

Since several data models have changed between AVD versions 3.x and 4.x, it is recommended to study the [Porting Guide for AVD 4.x.x](../../../docs/porting-guides/4.x.x.md) for existing deployments.

The input variables are documented below in tables and YAML.

All values are optional.

!!! note
    All input variables are validated by a schema. If additional custom keys are desired, a key starting with an underscore `_`, will be ignored.

!!! warning
    Available features and variables may vary by platforms, refer to documentation on arista.com for specifics.

## Authentication

### AAA accounting

--avdschema--
eos_cli_config_gen:aaa-accounting
--avdschema--

### AAA authentication

--avdschema--
eos_cli_config_gen:aaa-authentication
--avdschema--

### AAA authorization

--avdschema--
eos_cli_config_gen:aaa-authorization
--avdschema--

### AAA root

--avdschema--
eos_cli_config_gen:aaa-root
--avdschema--

### AAA server groups

--avdschema--
eos_cli_config_gen:aaa-server-groups
--avdschema--

### Enable password

--avdschema--
eos_cli_config_gen:enable-password
--avdschema--

### IP radius source-interfaces

--avdschema--
eos_cli_config_gen:ip-radius-source-interfaces
--avdschema--

### IP tacacs source-interfaces

--avdschema--
eos_cli_config_gen:ip-tacacs-source-interfaces
--avdschema--

### Local users

--avdschema--
eos_cli_config_gen:local-users
--avdschema--

### Radius server

--avdschema--
eos_cli_config_gen:radius-server
--avdschema--

### Radius servers

--avdschema--
eos_cli_config_gen:radius-servers
--avdschema--

### Roles

--avdschema--
eos_cli_config_gen:roles
--avdschema--

### Tacacs servers

--avdschema--
eos_cli_config_gen:tacacs-servers
--avdschema--

## ACLs

### IP Extended access-lists

AVD currently supports two different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:

--avdschema--
eos_cli_config_gen:access-lists
--avdschema--

The improved data model has a more sophisticated design documented below:

--avdschema--
eos_cli_config_gen:ip-access-lists
--avdschema--

The improved data model allows to limit the number of ACL entries that AVD is allowed to generate by defining `ip_access_lists_max_entries`.
Only normal entries under `ip_access_lists` will be counted, remarks will be ignored.
If the number is above the limit, the playbook will fail. This provides a simplified control over hardware utilization.
The numbers must be based on the hardware tests and AVD does not provide any guidance. Note that other EOS features may use the same hardware resources and affect the supported scale.

--avdschema--
eos_cli_config_gen:ip-access-lists-max-entries
--avdschema--

### IPv6 access-lists

--avdschema--
eos_cli_config_gen:ipv6-access-lists
--avdschema--

### IPv6 standard access-lists

--avdschema--
eos_cli_config_gen:ipv6-standard-access-lists
--avdschema--

### MAC access-lists

--avdschema--
eos_cli_config_gen:mac-access-lists
--avdschema--

### Standard access-lists

--avdschema--
eos_cli_config_gen:standard-access-lists
--avdschema--

## Endpoint Security

### Address-locking

--avdschema--
eos_cli_config_gen:address-locking
--avdschema--

### Dot1x

--avdschema--
eos_cli_config_gen:dot1x
--avdschema--

### MAC security

--avdschema--
eos_cli_config_gen:mac-security
--avdschema--

## Filters and policies

### AS path

--avdschema--
eos_cli_config_gen:as-path
--avdschema--

### Class-maps

--avdschema--
eos_cli_config_gen:class-maps
--avdschema--

### Dynamic prefix lists

--avdschema--
eos_cli_config_gen:dynamic-prefix-lists
--avdschema--

### IP community lists

AVD currently supports two different data models for community lists:

- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.
- The improved `ip_community_lists` data model.

Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.
Community list names must be unique.

The legacy data model supports simplified community list definition that only allows a single action to be defined as string:

--avdschema--
eos_cli_config_gen:community-lists
--avdschema--

The improved data model has a better design documented below:

--avdschema--
eos_cli_config_gen:ip-community-lists
--avdschema--

### IP extcommunity-lists

--avdschema--
eos_cli_config_gen:ip-extcommunity-lists
--avdschema--

### IP extcommunity-lists-regexp

--avdschema--
eos_cli_config_gen:ip-extcommunity-lists-regexp
--avdschema--

### IPv6 prefix-lists

--avdschema--
eos_cli_config_gen:ipv6-prefix-lists
--avdschema--

### Match list input

--avdschema--
eos_cli_config_gen:match-list-input
--avdschema--

### Peer-filters

--avdschema--
eos_cli_config_gen:peer-filters
--avdschema--

### Policy-maps

--avdschema--
eos_cli_config_gen:policy-maps
--avdschema--

### Prefix-lists

--avdschema--
eos_cli_config_gen:prefix-lists
--avdschema--

### Route-maps

--avdschema--
eos_cli_config_gen:route-maps
--avdschema--

### Trackers

--avdschema--
eos_cli_config_gen:trackers
--avdschema--

### Traffic policies

--avdschema--
eos_cli_config_gen:traffic-policies
--avdschema--

## Interfaces

### Errdisable

--avdschema--
eos_cli_config_gen:errdisable
--avdschema--

### Ethernet interfaces

--avdschema--
eos_cli_config_gen:ethernet-interfaces
--avdschema--

### Interface defaults

--avdschema--
eos_cli_config_gen:interface-defaults
--avdschema--

### Interface profiles

--avdschema--
eos_cli_config_gen:interface-profiles
--avdschema--

### LACP

--avdschema--
eos_cli_config_gen:lacp
--avdschema--

### Link tracking groups

--avdschema--
eos_cli_config_gen:link-tracking-groups
--avdschema--

### LLDP

--avdschema--
eos_cli_config_gen:lldp
--avdschema--

### Loopback interfaces

--avdschema--
eos_cli_config_gen:loopback-interfaces
--avdschema--

### Management interfaces

--avdschema--
eos_cli_config_gen:management-interfaces
--avdschema--

### Patch panel

--avdschema--
eos_cli_config_gen:patch-panel
--avdschema--

### Port-channel interfaces

--avdschema--
eos_cli_config_gen:port-channel-interfaces
--avdschema--

### Switchport default

--avdschema--
eos_cli_config_gen:switchport-default
--avdschema--

### Tunnel interfaces

--avdschema--
eos_cli_config_gen:tunnel-interfaces
--avdschema--

### VLAN interfaces

--avdschema--
eos_cli_config_gen:vlan-interfaces
--avdschema--

### VXLAN interface

--avdschema--
eos_cli_config_gen:vxlan-interface
--avdschema--

## Maintenance Mode

### BGP groups

--avdschema--
eos_cli_config_gen:bgp-groups
--avdschema--

### Interface groups

--avdschema--
eos_cli_config_gen:interface-groups
--avdschema--

### Maintenance

--avdschema--
eos_cli_config_gen:maintenance
--avdschema--

## Management

### Aliases

--avdschema--
eos_cli_config_gen:aliases
--avdschema--

### Banners

--avdschema--
eos_cli_config_gen:banners
--avdschema--

### Boot

--avdschema--
eos_cli_config_gen:boot
--avdschema--

### Clock

--avdschema--
eos_cli_config_gen:clock
--avdschema--

### DNS domain

--avdschema--
eos_cli_config_gen:dns-domain
--avdschema--

### Domain-list

--avdschema--
eos_cli_config_gen:domain-list
--avdschema--

### IP domain lookup

--avdschema--
eos_cli_config_gen:ip-domain-lookup
--avdschema--

### IP HTTP client source-interfaces

--avdschema--
eos_cli_config_gen:ip-http-client-source-interfaces
--avdschema--

### IP name servers

--avdschema--
eos_cli_config_gen:ip-name-servers
--avdschema--

### IP SSH client source-interfaces

--avdschema--
eos_cli_config_gen:ip-ssh-client-source-interfaces
--avdschema--

### Management API HTTP

--avdschema--
eos_cli_config_gen:management-api-http
--avdschema--

### Management API models

--avdschema--
eos_cli_config_gen:management-api-models
--avdschema--

### Management console

--avdschema--
eos_cli_config_gen:management-console
--avdschema--

### Management defaults

--avdschema--
eos_cli_config_gen:management-defaults
--avdschema--

### Management security

--avdschema--
eos_cli_config_gen:management-security
--avdschema--

### Management SSH

--avdschema--
eos_cli_config_gen:management-ssh
--avdschema--

### Management tech-support

--avdschema--
eos_cli_config_gen:management-tech-support
--avdschema--

### Name server

--avdschema--
eos_cli_config_gen:name-server
--avdschema--

### NTP

--avdschema--
eos_cli_config_gen:ntp
--avdschema--

### Prompt

--avdschema--
eos_cli_config_gen:prompt
--avdschema--

### Terminal

--avdschema--
eos_cli_config_gen:terminal
--avdschema--

### Virtual source NAT VRFs

--avdschema--
eos_cli_config_gen:virtual-source-nat-vrfs
--avdschema--

## Miscellaneous

### CVX

--avdschema--
eos_cli_config_gen:cvx
--avdschema--

### EOS cli

--avdschema--
eos_cli_config_gen:eos-cli
--avdschema--

### Management CVX

--avdschema--
eos_cli_config_gen:management-cvx
--avdschema--

### MCS client

--avdschema--
eos_cli_config_gen:mcs-client
--avdschema--

## Monitoring

### Daemons

--avdschema--
eos_cli_config_gen:daemons
--avdschema--

### Daemon terminattr

--avdschema--
eos_cli_config_gen:daemon-terminattr
--avdschema--

### Event handlers

--avdschema--
eos_cli_config_gen:event-handlers
--avdschema--

### Event monitor

--avdschema--
eos_cli_config_gen:event-monitor
--avdschema--

### Flow tracking

--avdschema--
eos_cli_config_gen:flow-trackings
--avdschema--

### Load interval

--avdschema--
eos_cli_config_gen:load-interval
--avdschema--

### Logging

--avdschema--
eos_cli_config_gen:logging
--avdschema--

### Management API gNMI

--avdschema--
eos_cli_config_gen:management-api-gnmi
--avdschema--

### Monitor connectivity

--avdschema--
eos_cli_config_gen:monitor-connectivity
--avdschema--

### Monitor sessions

--avdschema--
eos_cli_config_gen:monitor-sessions
--avdschema--

### SFLOW

--avdschema--
eos_cli_config_gen:sflow
--avdschema--

### SNMP server

--avdschema--
eos_cli_config_gen:snmp-server
--avdschema--

### Tap aggregation

--avdschema--
eos_cli_config_gen:tap-aggregation
--avdschema--

### VM tracer-sessions

--avdschema--
eos_cli_config_gen:vmtracer-sessions
--avdschema--

## Multicast

### IP IGMP snooping

--avdschema--
eos_cli_config_gen:ip-igmp-snooping
--avdschema--

### Router IGMP

--avdschema--
eos_cli_config_gen:router-igmp
--avdschema--

### Router MSDP

--avdschema--
eos_cli_config_gen:router-msdp
--avdschema--

### Router multicast

--avdschema--
eos_cli_config_gen:router-multicast
--avdschema--

### Router PIM sparse-mode

--avdschema--
eos_cli_config_gen:router-pim-sparse-mode
--avdschema--

## Quality of Service

### QoS

--avdschema--
eos_cli_config_gen:qos
--avdschema--

### QoS profiles

--avdschema--
eos_cli_config_gen:qos-profiles
--avdschema--

### Queue monitor-length

--avdschema--
eos_cli_config_gen:queue-monitor-length
--avdschema--

### Queue monitor-streaming

--avdschema--
eos_cli_config_gen:queue-monitor-streaming
--avdschema--

## Routing

### ARP

--avdschema--
eos_cli_config_gen:arp
--avdschema--

### DHCP relay

--avdschema--
eos_cli_config_gen:dhcp-relay
--avdschema--

### IP DHCP relay

--avdschema--
eos_cli_config_gen:ip-dhcp-relay
--avdschema--

### IP ICMP redirect

--avdschema--
eos_cli_config_gen:ip-icmp-redirect
--avdschema--

### IP NAT

--avdschema--
eos_cli_config_gen:ip-nat
--avdschema--

### IP routing IPv6 interfaces

--avdschema--
eos_cli_config_gen:ip-routing-ipv6-interfaces
--avdschema--

### IP routing

--avdschema--
eos_cli_config_gen:ip-routing
--avdschema--

### IP virtual router MAC address

--avdschema--
eos_cli_config_gen:ip-virtual-router-mac-address
--avdschema--

### IPv6 ICMP redirects

--avdschema--
eos_cli_config_gen:ipv6-icmp-redirect
--avdschema--

### IPv6 static routes

--avdschema--
eos_cli_config_gen:ipv6-static-routes
--avdschema--

### IPv6 unicast routing

--avdschema--
eos_cli_config_gen:ipv6-unicast-routing
--avdschema--

### MPLS

--avdschema--
eos_cli_config_gen:mpls
--avdschema--

### Router BFD

--avdschema--
eos_cli_config_gen:router-bfd
--avdschema--

### Router BGP

--avdschema--
eos_cli_config_gen:router-bgp
--avdschema--

### Router general

--avdschema--
eos_cli_config_gen:router-general
--avdschema--

### Router ISIS

--avdschema--
eos_cli_config_gen:router-isis
--avdschema--

### Router L2 VPN

--avdschema--
eos_cli_config_gen:router-l2-vpn
--avdschema--

### Router OSPF

--avdschema--
eos_cli_config_gen:router-ospf
--avdschema--

### Router traffic engineering

--avdschema--
eos_cli_config_gen:router-traffic-engineering
--avdschema--

### Service routing configuration bgp

--avdschema--
eos_cli_config_gen:service-routing-configuration-bgp
--avdschema--

### Service routing protocols model

--avdschema--
eos_cli_config_gen:service-routing-protocols-model
--avdschema--

### Static routes

--avdschema--
eos_cli_config_gen:static-routes
--avdschema--

### VRFs

--avdschema--
eos_cli_config_gen:vrfs
--avdschema--

## Switching

### MLAG configuration

--avdschema--
eos_cli_config_gen:mlag-configuration
--avdschema--

### Spanning-tree

--avdschema--
eos_cli_config_gen:spanning-tree
--avdschema--

### VLAN internal order

--avdschema--
eos_cli_config_gen:vlan-internal-order
--avdschema--

### VLANs

--avdschema--
eos_cli_config_gen:vlans
--avdschema--

## System settings

### Hardware counters

--avdschema--
eos_cli_config_gen:hardware-counters
--avdschema--

### Hardware

--avdschema--
eos_cli_config_gen:hardware
--avdschema--

### IP hardware

--avdschema--
eos_cli_config_gen:ip-hardware
--avdschema--

### IPv6 hardware

--avdschema--
eos_cli_config_gen:ipv6-hardware
--avdschema--

### L2 protocol

--avdschema--
eos_cli_config_gen:l2-protocol
--avdschema--

### MAC address-table

--avdschema--
eos_cli_config_gen:mac-address-table
--avdschema--

### Platform

--avdschema--
eos_cli_config_gen:platform
--avdschema--

### PoE

--avdschema--
eos_cli_config_gen:poe
--avdschema--

### PTP

--avdschema--
eos_cli_config_gen:ptp
--avdschema--

### Redundancy

--avdschema--
eos_cli_config_gen:redundancy
--avdschema--

### System

--avdschema--
eos_cli_config_gen:system
--avdschema--

### TCAM profile

--avdschema--
eos_cli_config_gen:tcam-profile
--avdschema--
