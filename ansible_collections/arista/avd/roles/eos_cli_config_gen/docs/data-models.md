---
# This title is used for search results
title: EOS Config data models (eos_cli_config_gen)
template: custom-banner.html
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# EOS Config data models (eos_cli_config_gen)

The EOS Config provides device-centric data models for expressing the Arista EOS device configurations syntax. These data models are also referred to as "structured config" within the AVD Design data models and can be leveraged with [custom structured configuration](../../eos_designs/docs/how-to/custom-structured-configuration.md) to extend or override the behaviour of Arista AVD.

For Ansible users this document describes the supported input variables for the role `arista.avd.eos_cli_config_gen`.

Since several data models have changed between AVD versions 5.x and 6.x, it is recommended to study the [Porting Guide for AVD 6.x.x](../../../../../../docs/porting-guides/6.x.x.md) for existing deployments.

The data models are documented below in tables and YAML.

All values are optional.

!!! note
    All input variables are validated by a schema. If additional custom keys are desired, a key starting with an underscore `_`, will be ignored.

!!! warning
    Available features and variables may vary by platforms, refer to documentation on arista.com for specifics.

## Authentication

### AAA accounting

--8<--
schemas/eos_config/docs/tables/aaa-accounting.md
--8<--

### AAA authentication

--8<--
schemas/eos_config/docs/tables/aaa-authentication.md
--8<--

### AAA authorization

--8<--
schemas/eos_config/docs/tables/aaa-authorization.md
--8<--

### AAA root

--8<--
schemas/eos_config/docs/tables/aaa-root.md
--8<--

### AAA server groups

--8<--
schemas/eos_config/docs/tables/aaa-server-groups.md
--8<--

### Enable password

--8<--
schemas/eos_config/docs/tables/enable-password.md
--8<--

### IP radius source-interfaces

--8<--
schemas/eos_config/docs/tables/ip-radius-source-interfaces.md
--8<--

### IP tacacs source-interfaces

--8<--
schemas/eos_config/docs/tables/ip-tacacs-source-interfaces.md
--8<--

### IP FTP client source-interfaces

--8<--
schemas/eos_config/docs/tables/ip-ftp-client.md
--8<--

### IP Telnet client source-interfaces

--8<--
schemas/eos_config/docs/tables/ip-telnet-client.md
--8<--

### IP TFTP client source-interfaces

--8<--
schemas/eos_config/docs/tables/ip-tftp-client.md
--8<--

### Local users

--8<--
schemas/eos_config/docs/tables/local-users.md
--8<--

### Radius proxy

--8<--
schemas/eos_config/docs/tables/radius-proxy.md
--8<--

### Radius server

--8<--
schemas/eos_config/docs/tables/radius-server.md
--8<--

### Roles

--8<--
schemas/eos_config/docs/tables/roles.md
--8<--

### Tacacs servers

--8<--
schemas/eos_config/docs/tables/tacacs-servers.md
--8<--

## ACLs

### IP Extended access-lists

AVD currently supports two different data models for extended ACLs:

- The legacy `access_lists` data model, for compatibility with existing deployments
- The improved `ip_access_lists` data model, for access to more EOS features

Both data models can coexists without conflicts, as different keys are used: `access_lists` vs `ip_access_lists`.
Access list names must be unique.

The legacy data model supports simplified ACL definition with `sequence` to `action` mapping:

--8<--
schemas/eos_config/docs/tables/access-lists.md
--8<--

The improved data model has a more sophisticated design documented below:

--8<--
schemas/eos_config/docs/tables/ip-access-lists.md
--8<--

The improved data model allows to limit the number of ACL entries that AVD is allowed to generate by defining `ip_access_lists_max_entries`.
Only normal entries under `ip_access_lists` will be counted, remarks will be ignored.
If the number is above the limit, the playbook will fail. This provides a simplified control over hardware utilization.
The numbers must be based on the hardware tests and AVD does not provide any guidance. Note that other EOS features may use the same hardware resources and affect the supported scale.

--8<--
schemas/eos_config/docs/tables/ip-access-lists-max-entries.md
--8<--

### IPv6 access-lists

--8<--
schemas/eos_config/docs/tables/ipv6-access-lists.md
--8<--

### IPv6 standard access-lists

--8<--
schemas/eos_config/docs/tables/ipv6-standard-access-lists.md
--8<--

### MAC access-lists

--8<--
schemas/eos_config/docs/tables/mac-access-lists.md
--8<--

### Standard access-lists

--8<--
schemas/eos_config/docs/tables/standard-access-lists.md
--8<--

## Endpoint Security

### Address-locking

--8<--
schemas/eos_config/docs/tables/address-locking.md
--8<--

### Dot1x

--8<--
schemas/eos_config/docs/tables/dot1x.md
--8<--

### MAC security

--8<--
schemas/eos_config/docs/tables/mac-security.md
--8<--

## Filters and policies

### AS path

--8<--
schemas/eos_config/docs/tables/as-path.md
--8<--

### Class-maps

--8<--
schemas/eos_config/docs/tables/class-maps.md
--8<--

### Dynamic prefix lists

--8<--
schemas/eos_config/docs/tables/dynamic-prefix-lists.md
--8<--

### IP community lists

--8<--
schemas/eos_config/docs/tables/ip-community-lists.md
--8<--

### IP extcommunity-lists

--8<--
schemas/eos_config/docs/tables/ip-extcommunity-lists.md
--8<--

### IP extcommunity-lists-regexp

--8<--
schemas/eos_config/docs/tables/ip-extcommunity-lists-regexp.md
--8<--

### IP large community lists

--8<--
schemas/eos_config/docs/tables/ip-large-community-lists.md
--8<--

### IPv6 prefix-lists

--8<--
schemas/eos_config/docs/tables/ipv6-prefix-lists.md
--8<--

### Match list input

--8<--
schemas/eos_config/docs/tables/match-list-input.md
--8<--

### Peer-filters

--8<--
schemas/eos_config/docs/tables/peer-filters.md
--8<--

### Policy-maps

--8<--
schemas/eos_config/docs/tables/policy-maps.md
--8<--

### Port-channel

--8<--
schemas/eos_config/docs/tables/port-channel.md
--8<--

### Prefix-lists

--8<--
schemas/eos_config/docs/tables/prefix-lists.md
--8<--

### Route-maps

--8<--
schemas/eos_config/docs/tables/route-maps.md
--8<--

### Trackers

--8<--
schemas/eos_config/docs/tables/trackers.md
--8<--

### Traffic policies

--8<--
schemas/eos_config/docs/tables/traffic-policies.md
--8<--

## Interfaces

### DPS interfaces

--8<--
schemas/eos_config/docs/tables/dps-interfaces.md
--8<--

### Errdisable

--8<--
schemas/eos_config/docs/tables/errdisable.md
--8<--

### Ethernet interfaces

--8<--
schemas/eos_config/docs/tables/ethernet-interfaces.md
--8<--

### Interface defaults

--8<--
schemas/eos_config/docs/tables/interface-defaults.md
--8<--

### Interface profiles

--8<--
schemas/eos_config/docs/tables/interface-profiles.md
--8<--

### LACP

--8<--
schemas/eos_config/docs/tables/lacp.md
--8<--

### Link tracking groups

--8<--
schemas/eos_config/docs/tables/link-tracking-groups.md
--8<--

### LLDP

--8<--
schemas/eos_config/docs/tables/lldp.md
--8<--

### Loopback interfaces

--8<--
schemas/eos_config/docs/tables/loopback-interfaces.md
--8<--

### Management interfaces

--8<--
schemas/eos_config/docs/tables/management-interfaces.md
--8<--

### Patch panel

--8<--
schemas/eos_config/docs/tables/patch-panel.md
--8<--

### Port-channel interfaces

--8<--
schemas/eos_config/docs/tables/port-channel-interfaces.md
--8<--

### Switchport

#### Switchport default

--8<--
schemas/eos_config/docs/tables/switchport-default.md
--8<--

#### Switchport port security

--8<--
schemas/eos_config/docs/tables/switchport-port-security.md
--8<--

#### Switchport Ethernet LLC Validation

--8<--
schemas/eos_config/docs/tables/switchport-ethernet-llc-validation.md
--8<--

#### Switchport VLAN Tag Validation

--8<--
schemas/eos_config/docs/tables/switchport-vlan-tag-validation.md
--8<--

### Sync-e

--8<--
schemas/eos_config/docs/tables/sync-e.md
--8<--

### Transceiver QSFP default mode 4x10

--8<--
schemas/eos_config/docs/tables/transceiver-qsfp-default-mode-4x10.md
--8<--

### Transceiver DOM threshold

--8<--
schemas/eos_config/docs/tables/transceiver.md
--8<--

### Tunnel interfaces

--8<--
schemas/eos_config/docs/tables/tunnel-interfaces.md
--8<--

### VLAN interfaces

--8<--
schemas/eos_config/docs/tables/vlan-interfaces.md
--8<--

### VXLAN interface

--8<--
schemas/eos_config/docs/tables/vxlan-interface.md
--8<--

## Maintenance Mode

### BGP groups

--8<--
schemas/eos_config/docs/tables/bgp-groups.md
--8<--

### Interface groups

--8<--
schemas/eos_config/docs/tables/interface-groups.md
--8<--

### Maintenance

--8<--
schemas/eos_config/docs/tables/maintenance.md
--8<--

## Management

### Aliases

--8<--
schemas/eos_config/docs/tables/aliases.md
--8<--

### Banners

--8<--
schemas/eos_config/docs/tables/banners.md
--8<--

### Boot

--8<--
schemas/eos_config/docs/tables/boot.md
--8<--

### Clock

--8<--
schemas/eos_config/docs/tables/clock.md
--8<--

### DNS domain

--8<--
schemas/eos_config/docs/tables/dns-domain.md
--8<--

### Domain-list

--8<--
schemas/eos_config/docs/tables/domain-list.md
--8<--

### Environment

--8<--
schemas/eos_config/docs/tables/environment-fan-speed.md
--8<--

### Hostname

--8<--
schemas/eos_config/docs/tables/hostname.md
--8<--

### IP domain lookup

--8<--
schemas/eos_config/docs/tables/ip-domain-lookup.md
--8<--

### IP Host

--8<--
schemas/eos_config/docs/tables/ip-hosts.md
--8<--

### IP HTTP client

--8<--
schemas/eos_config/docs/tables/ip-http-client.md
--8<--

### IP name server

--8<--
schemas/eos_config/docs/tables/ip-name-server.md
--8<--

### IP name server groups

--8<--
schemas/eos_config/docs/tables/ip-name-server-groups.md
--8<--

### IP SSH client

--8<--
schemas/eos_config/docs/tables/ip-ssh-client.md
--8<--

### Management accounts

--8<--
schemas/eos_config/docs/tables/management-accounts.md
--8<--

### Management API HTTP

--8<--
schemas/eos_config/docs/tables/management-api-http.md
--8<--

### Management API models

--8<--
schemas/eos_config/docs/tables/management-api-models.md
--8<--

### Management console

--8<--
schemas/eos_config/docs/tables/management-console.md
--8<--

### Management defaults

--8<--
schemas/eos_config/docs/tables/management-defaults.md
--8<--

### Management LDAP

--8<--
schemas/eos_config/docs/tables/management-ldap.md
--8<--

### Management security

--8<--
schemas/eos_config/docs/tables/management-security.md
--8<--

### Management SSH

--8<--
schemas/eos_config/docs/tables/management-ssh.md
--8<--

### Management tech-support

--8<--
schemas/eos_config/docs/tables/management-tech-support.md
--8<--

### NTP

--8<--
schemas/eos_config/docs/tables/ntp.md
--8<--

### Prompt

--8<--
schemas/eos_config/docs/tables/prompt.md
--8<--

### Terminal

--8<--
schemas/eos_config/docs/tables/terminal.md
--8<--

### Virtual source NAT VRFs

--8<--
schemas/eos_config/docs/tables/virtual-source-nat-vrfs.md
--8<--

## Miscellaneous

### Config comment

--8<--
schemas/eos_config/docs/tables/config-comment.md
--8<--

### Config end

--8<--
schemas/eos_config/docs/tables/config-end.md
--8<--

### CVX

--8<--
schemas/eos_config/docs/tables/cvx.md
--8<--

### EOS cli

--8<--
schemas/eos_config/docs/tables/eos-cli.md
--8<--

### Management CVX

--8<--
schemas/eos_config/docs/tables/management-cvx.md
--8<--

### MCS client

--8<--
schemas/eos_config/docs/tables/mcs-client.md
--8<--

## Monitoring

### Connectivity Fault Management

--8<--
schemas/eos_config/docs/tables/cfm.md
--8<--

### Daemons

--8<--
schemas/eos_config/docs/tables/daemons.md
--8<--

### Daemon terminattr

--8<--
schemas/eos_config/docs/tables/daemon-terminattr.md
--8<--

### Event handlers

--8<--
schemas/eos_config/docs/tables/event-handlers.md
--8<--

### Event monitor

--8<--
schemas/eos_config/docs/tables/event-monitor.md
--8<--

### Flow tracking

--8<--
schemas/eos_config/docs/tables/flow-tracking.md
--8<--

### Load interval

--8<--
schemas/eos_config/docs/tables/load-interval.md
--8<--

### Logging

--8<--
schemas/eos_config/docs/tables/logging.md
--8<--

### Management API gNMI

--8<--
schemas/eos_config/docs/tables/management-api-gnmi.md
--8<--

### Monitor connectivity

--8<--
schemas/eos_config/docs/tables/monitor-connectivity.md
--8<--

### Monitor layer 1

--8<--
schemas/eos_config/docs/tables/monitor-layer1.md
--8<--

### Monitor link flap policy

--8<--
schemas/eos_config/docs/tables/monitor-link-flap-policy.md
--8<--

### Monitor loop protection

--8<--
schemas/eos_config/docs/tables/monitor-loop-protection.md
--8<--

### Monitor server Radius

--8<--
schemas/eos_config/docs/tables/monitor-server-radius.md
--8<--

### Monitor sessions

--8<--
schemas/eos_config/docs/tables/monitor-sessions.md
--8<--

### Monitor telemetry

--8<--
schemas/eos_config/docs/tables/monitor-telemetry.md
--8<--

### Monitor TWAMP

--8<--
schemas/eos_config/docs/tables/monitor-twamp.md
--8<--

### Queue monitor-length

--8<--
schemas/eos_config/docs/tables/queue-monitor-length.md
--8<--

### Queue monitor-streaming

--8<--
schemas/eos_config/docs/tables/queue-monitor-streaming.md
--8<--

### Schedule

--8<--
schemas/eos_config/docs/tables/schedule.md
--8<--

### SFLOW

--8<--
schemas/eos_config/docs/tables/sflow.md
--8<--

### SNMP server

--8<--
schemas/eos_config/docs/tables/snmp-server.md
--8<--

### Tap aggregation

--8<--
schemas/eos_config/docs/tables/tap-aggregation.md
--8<--

### VM tracer-sessions

--8<--
schemas/eos_config/docs/tables/vmtracer-sessions.md
--8<--

## Multicast

### IP IGMP snooping

--8<--
schemas/eos_config/docs/tables/ip-igmp-snooping.md
--8<--

### Router IGMP

--8<--
schemas/eos_config/docs/tables/router-igmp.md
--8<--

### Router MSDP

--8<--
schemas/eos_config/docs/tables/router-msdp.md
--8<--

### Router multicast

--8<--
schemas/eos_config/docs/tables/router-multicast.md
--8<--

### Router PIM sparse-mode

--8<--
schemas/eos_config/docs/tables/router-pim-sparse-mode.md
--8<--

## Quality of Service

### Priority flow control

--8<--
schemas/eos_config/docs/tables/priority-flow-control.md
--8<--

### QoS

--8<--
schemas/eos_config/docs/tables/qos.md
--8<--

### QoS profiles

--8<--
schemas/eos_config/docs/tables/qos-profiles.md
--8<--

### Application traffic recognition

--8<--
schemas/eos_config/docs/tables/application-traffic-recognition.md
--8<--

## Routing

### ARP

--8<--
schemas/eos_config/docs/tables/arp.md
--8<--

### DHCP relay

--8<--
schemas/eos_config/docs/tables/dhcp-relay.md
--8<--

### IP DHCP relay

--8<--
schemas/eos_config/docs/tables/ip-dhcp-relay.md
--8<--

### IP DHCP Snooping

--8<--
schemas/eos_config/docs/tables/ip-dhcp-snooping.md
--8<--

### DHCP Servers

--8<--
schemas/eos_config/docs/tables/dhcp-servers.md
--8<--

### IP ICMP redirect

--8<--
schemas/eos_config/docs/tables/ip-icmp-redirect.md
--8<--

### IP NAT

--8<--
schemas/eos_config/docs/tables/ip-nat.md
--8<--

### IP routing IPv6 interfaces

--8<--
schemas/eos_config/docs/tables/ip-routing-ipv6-interfaces.md
--8<--

### IP routing

--8<--
schemas/eos_config/docs/tables/ip-routing.md
--8<--

### IP virtual router MAC address

--8<--
schemas/eos_config/docs/tables/ip-virtual-router-mac-address.md
--8<--

--8<--
schemas/eos_config/docs/tables/ip-virtual-router-mac-address-advertisement-interval.md
--8<--

--8<--
schemas/eos_config/docs/tables/ip-virtual-router-mac-address-mlag-peer.md
--8<--

### IPv6 DHCP relay

--8<--
schemas/eos_config/docs/tables/ipv6-dhcp-relay.md
--8<--

### IPv6 ICMP redirects

--8<--
schemas/eos_config/docs/tables/ipv6-icmp-redirect.md
--8<--

### IPv6 static routes

--8<--
schemas/eos_config/docs/tables/ipv6-static-routes.md
--8<--

### IPv6 unicast routing

--8<--
schemas/eos_config/docs/tables/ipv6-unicast-routing.md
--8<--

### IPv6 Neighbors

--8<--
schemas/eos_config/docs/tables/ipv6-neighbor.md
--8<--

### MPLS

--8<--
schemas/eos_config/docs/tables/mpls.md
--8<--

### Router adaptive virtual topology

--8<--
schemas/eos_config/docs/tables/router-adaptive-virtual-topology.md
--8<--

### Router BFD

--8<--
schemas/eos_config/docs/tables/router-bfd.md
--8<--

### Router BGP

--8<--
schemas/eos_config/docs/tables/router-bgp.md
--8<--

### Router general

--8<--
schemas/eos_config/docs/tables/router-general.md
--8<--

### Router internet-exit

--8<--
schemas/eos_config/docs/tables/router-internet-exit.md
--8<--

### Router ISIS

--8<--
schemas/eos_config/docs/tables/router-isis.md
--8<--

### Router L2 VPN

--8<--
schemas/eos_config/docs/tables/router-l2-vpn.md
--8<--

### Router OSPF

--8<--
schemas/eos_config/docs/tables/router-ospf.md
--8<--

### Router OSPFv3

--8<--
schemas/eos_config/docs/tables/router-ospfv3.md
--8<--

### Router RIP

--8<--
schemas/eos_config/docs/tables/router-rip.md
--8<--

### IP OSPF router-id output-format hostnames

--8<--
schemas/eos_config/docs/tables/ip-ospf-router-id-output-format-hostnames.md
--8<--

### IPV6 Router OSPF

--8<--
schemas/eos_config/docs/tables/ipv6-router-ospf.md
--8<--

### Router path selection

--8<--
schemas/eos_config/docs/tables/router-path-selection.md
--8<--

### Router service-insertion

--8<--
schemas/eos_config/docs/tables/router-service-insertion.md
--8<--

### Router traffic engineering

--8<--
schemas/eos_config/docs/tables/router-traffic-engineering.md
--8<--

### Service routing configuration bgp

--8<--
schemas/eos_config/docs/tables/service-routing-configuration-bgp.md
--8<--

### Service routing protocols model

--8<--
schemas/eos_config/docs/tables/service-routing-protocols-model.md
--8<--

### Static routes

--8<--
schemas/eos_config/docs/tables/static-routes.md
--8<--

### STUN

--8<--
schemas/eos_config/docs/tables/stun.md
--8<--

### VRFs

--8<--
schemas/eos_config/docs/tables/vrfs.md
--8<--

## Security

### IP Security

--8<--
schemas/eos_config/docs/tables/ip-security.md
--8<--

### Router segment-security

--8<--
schemas/eos_config/docs/tables/router-segment-security.md
--8<--

## Switching

### MLAG configuration

--8<--
schemas/eos_config/docs/tables/mlag-configuration.md
--8<--

### Spanning-tree

--8<--
schemas/eos_config/docs/tables/spanning-tree.md
--8<--

### VLAN internal order

--8<--
schemas/eos_config/docs/tables/vlan-internal-order.md
--8<--

### VLANs

--8<--
schemas/eos_config/docs/tables/vlans.md
--8<--

## System settings

### Agents

--8<--
schemas/eos_config/docs/tables/agents.md
--8<--

### Hardware counters

--8<--
schemas/eos_config/docs/tables/hardware-counters.md
--8<--

### Hardware

--8<--
schemas/eos_config/docs/tables/hardware.md
--8<--

### IP software forwarding

--8<--
schemas/eos_config/docs/tables/ip-software-forwarding.md
--8<--

### IP hardware

--8<--
schemas/eos_config/docs/tables/ip-hardware.md
--8<--

### IPv6 hardware

--8<--
schemas/eos_config/docs/tables/ipv6-hardware.md
--8<--

### L2 protocol

--8<--
schemas/eos_config/docs/tables/l2-protocol.md
--8<--

### MAC address-table

--8<--
schemas/eos_config/docs/tables/mac-address-table.md
--8<--

### Platform

--8<--
schemas/eos_config/docs/tables/platform.md
--8<--

### PoE

--8<--
schemas/eos_config/docs/tables/poe.md
--8<--

### PTP

--8<--
schemas/eos_config/docs/tables/ptp.md
--8<--

### Redundancy

--8<--
schemas/eos_config/docs/tables/redundancy.md
--8<--

### Load Balance

--8<--
schemas/eos_config/docs/tables/load-balance.md
--8<--

### System

--8<--
schemas/eos_config/docs/tables/system.md
--8<--

### TCAM profile

--8<--
schemas/eos_config/docs/tables/tcam-profile.md
--8<--

### Kernel

--8<--
schemas/eos_config/docs/tables/kernel.md
--8<--

## Metadata

These fields are not generating any configuration. They are meant to be used by tools that parse structured configuration.

--8<--
schemas/eos_config/docs/tables/metadata.md
--8<--

## Future EOS CLI Behaviors

Opt-in to future EOS CLI behaviors which will become default behaviors in a future AVD major version.

--8<--
schemas/eos_config/docs/tables/eos-config-future.md
--8<--
