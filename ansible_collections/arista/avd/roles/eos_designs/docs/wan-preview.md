---
# This title is used for search results
title: Ansible Collection Role eos_designs - WAN preview
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# WAN preview

!!! warning

    The integration of WAN designs to `eos_designs` role is in preview mode.

    Everything is subject to change, is not supported and may not be complete.

    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/avd/discussions)

## Overview

The intention is to support both a single AutoVPN design and [CV Pathfinder](https://www.arista.com/en/solutions/enterprise-wan/pathfinder).

### Design points

- The intent is to be able to support having the different WAN participating devices in different inventories.
- Only iBGP is supported as an overlay_routing_protocol.
- On the AutoVPN Route Reflectors and Pathfinders, a listen range statement is used for BGP to allow for point number 1.
- The default VRF is being configured by default on all WAN devices with a `vni_id` of 1. To override this, it is necessary to configure the `default` VRF in a tenant in `network_services`.
- When configuring HA on a site, the path-group ID `65535` is reserved for the path-group called `LAN_HA`.
- The policies definition works as follow:

  - The policies are defined under `wan_virtual_topologies.policies`. For AutoVPN mode, the policies are configured under `router path-selection`, for CV Pathfinder, they are configured under `router adaptive-virtual-topology`.
  - A policy is composed of a list of `application_virtual_topologies` and one `default_virtual_topology`.
  - The `application_virtual_topologies` entries and the `default_virtual_topology` key are used to create the policy match statement, the AVT profile (when `wan_mode` is CV Pathfinder) and the load balancing policy.
  - The `default_virtual_topology` is used as the default match in the policy.  To prevent configuring it, the `drop_unmatched` boolean must be set to `true` otherwise, at least one `path-group` must be configured or AVD will raise an error.
  - Policies are assigned to VRFs using the list `wan_virtual_topologies.vrfs`. A policy can be reused in multiple VRFs.
  - If no policy is assigned for the `default` VRF policy, AVD auto generates one with one `default_virtual_topology` entry configured to use all available local path-groups.
  - For the policy defined for VRF `default` (or the auto-generared one), an extra match statement is injected in the policy to match the traffic towards the Pathfinders or AutoVPN RRs, the name of the application-profile is hardcoded as `APP-PROFILE-CONTROL-PLANE`. A special policy is created by appending `-WITH-CP` at the end of the targetted policy name.
  - For HA, the considered interfaces are only the `uplink_interfaces` in VRF default. It is possible to disable HA under node settings.
  - For a given application profile match in a WAN policy, if the path-groups in the input data have an empty intersection with the path-groups on the device (no common path-group), the match statement / AVT profile is **NOT** configured on the device. This implies that the traffic could be matched in one of the following application profiles or the default virtual topology. Note that the default virtual topology can be configured to drop traffic.

## Known limitations

- Zones are not configurable for CV Pathfinder. All sites are being configured in a default zone `<region_name>-ZONE` with ID `1`.
- Because of the previous point, in `eos_designs`, the `transit` node type is always configured as `transit region`.
- All Pathfinders must be able to create a full mesh
- No IPv6 support
- For WAN interfaces, NAT IP on the Pathfinder side can be supported using the `wan_route_servers.path_groups.interfaces` key.
- Path-group ID is currently required under `wan_path_groups` until an algorithm is implemented to auto generate IDs.
- It is not yet supported to disable HA on a specific LAN interface on the device, nor is it supported to add HA configuration on a non-uplink interface.
- The name of the AVT policies and AVT profiles are configurable in the input variables. The Load Balance policies are named `LB-<profile_name>` and are not configurable.
- For LAN, the current supported funcitonality is to use `uplink_type: p2p-vrfs` on the WAN routers and to have the relevant VRFs present on the uplink switches via `network_services`. Other LAN scenarios will come with time.
- HA for AutoVPN is not supported
- All the WAN routers must have a common path-group with at least one WAN route server to be able to inject the default control-plane match statement in the VRF default WAN policy.

## Future work

- New LAN scenarios (L2 port-channel, HA for L2 `lan` using VRRP..)
- WAN Internet exit
- Indirect connectivity to pathfinder
- `import path-group` functionality
- BGP peerings on WAN L3 interfaces
- Connectivity Monitor configuration
- More configuration options for static generated config (flow tracker names, timers,...)
- Extra STUN server for a given path-group not connected to pathfinder
- Auto generation of Path-group IDs and other IDs.
- Proper OSPF-BGP redistribution in VRF default.
- Support for OSPF subinterfaces.
- validate_state support for AutoVPN and CV-Pathfinder
- Path selection outlier detection feature
- HA for AutoVPN

## `eos_cli_config_gen` support

- `eos_cli_config_gen` schema should support all of the required keys to
    configure a WAN network, whether AutoVPN or Pathfinder. If you find any
    missing functionality, please open an issue on Github.

## Getting started with WAN

When deploying CV Pathfinder, the assumption is that the deployment is using CVaaS.

!!! Warning Disclaimer
    This section does not intend to be a network design nor a best practice document.
    It is about how to deploy a WAN network using AVD.

### Global settings

!!! Warning

    These global settings must be the same for every WAN device participating
    in the WAN network. When using multiple inventories, the recommendation is
    to use Global Variables, for instance leveraging the `arista.avd.global_vars`
    Ansible plugin.

#### TL;DR

The following top level keys must be defined globally and have the same value for every single WAN router.

- `wan_mode`: Two possible modes, `autovpn` and `cv-pathfinder` (default)
- `wan_virtual_topologies`: to define the Policies and the VRF to policy mappings
- `wan_path_groups`: to define the list of path-groups in the network
- `wan_carriers`: to define the list of carriers in the network, each carrier is assigned to a path-group
- `wan_ipsec_profiles`: to define the shared key for the Control Plane and Data Plane IPSec profiles.
- `cv_pathfinder_regions`: to define the Region/Zone/Site hierarchy, not required for AutoVPN.
- `tenants`: the default tenant key from `network_services` or any other key for tenant that would hold some WAN VRF informaiton
- `wan_stun_dtls_disable`: disable dTLS for STUN for instance for lab. (**NOT** recommended in production)
- `application_classification`: to define the specific traffic classification required for the WAN if any.

The following keys must be set for each WAN router but can have different values

- `wan_route_servers`: To indicate to which WAN route servers the WAN router should connect to.

The following keys must be set for the WAN route servers for the connectivity to work:

- `bgp_peer_groups.wan_overlay_peers.listen_range_prefixes`: To set the ranges of IP address from which to expect BGP peerings for the WAN.

#### WAN mode

AVD supports two design types for WAN:

- AutoVPN
- CV Pathfinder

By default the mode is set to `cv-pathfinder` and can be changed using:

```yaml
---
wan_mode: autovpn | cv-pathfinder
```

#### WAN node_types

There are two built-in node types for WAN:

- `wan_router`: WAN routers can be AutoVPN edges, CV Pathfinder edges or transits.
- `wan_rr`: WAN route servers, used for the AutoVPN RRs and CV Pathfinder Pathfinder nodes.

#### WAN route servers

The AVD model for WAN has been built with the intention that it should be possible to have the different WAN routers in different inventories.

The top level `wan_route_servers` allow to indicate to which AutoVPN RRs or to which Pathinders node the routers should connect to. The key can be different per region for instance.

```yaml
 WAN routers with this configuration will establish static peerings towards pf1 and pf2 and the common path-groups.
wan_route_servers:
  - hostname: pf1
  - hostname: pf2
```

!!! Note
    It is recommended to always have at least 2 WAN route servers for redundancy.

When the WAN route servers are part of the same inventory, each WAN routers in the inventory is able to pick up the required information to generate the configuration from the inventory device.
However, if the WAN route servers are in a different inventory, it is then necessary to add some information under the `wan_route_servers` key entry. AVD will raise an error if any required information to generate the configuration is missing. Note that the configuration under `wan_route_servers` takes precedence over what AVD could derive from the device if it is in the same inventory.

#### CV Pathfinder hierarchy

When deploying CV Pathfinder, it is required to define a hierarchy using the top
level key `cv_pathfinder_regions` in order to then be able to allocat a region
and a site to each WAN routers in the node settings.

The hierarchy looks like:

```yaml
cv_pathfinder_regions:
  - name: Region_1
    id: 1
    description: AVD Region 1
    sites:
      - name: Site11
        id: 11
        location: Somewhere
      - name: Site12
        id: 12
        location: Somewhere else
  - name: Region_2
    id: 2
    description: AVD Region 2
    sites:
      - name: Site11
        id: 11
      - name: Site21
        id: 21
```

!!! Note
    Site IDs and names must be unique per region.

And then for each `wan_router` (not needed for Pathfinders node):

```yaml
wan_router:
  nodes:
    - name: EDGE1
      cv_pathfinder_region: Region_1
      cv_pathfinder_site: Site11
```

#### WAN carriers and path-groups

Path-groups are used to define overlays over the various providers a WAN network can use.
In AVD, the list of desired path-groups must be defined the same across all WAN participating routers using the following top level key.

```yaml
wan_path_groups:
  - name: MPLS
    # TODO update ipsec documentation
    ipsec: false
    id: 100
  - name: INET
    id: 101
  - name: LTE
    id: 102
  - name: Equinix
    id: 103
  - name: Satellite
    id: 104
```

!!! Note
    The IDs are required and it is possible to turn on and off ipsec at the path-group level for dynamic or static peers.

To allow for a better visualization in CVaaS, AVD implements on level of indirection to be able to specify the Carrier for the last mile provider. Each carrier is associated to a path-group and multiple carriers can be assigned to the same path-group (e.g. all the Internet providers can be differentiated at the carrier level but bundled together at the path-group level).
The list of carriers must also be the same across all WAN routers:

```yaml
wan_carriers:
  - name: IPS-1
    path_group: INET
  - name: ISP-2
    path_group: INET
  - name: MPLS-SP1
    path_group: MPLS
  - name: MPLS-SP2
    path_group: MPLS
  - name: LTE-5G-SP
    path_group: LTE
  - name: Satellite-SP
    path_group: Satellite
```

### Flow tracking

For scalabilty reasons, flow-tracking is enabled only on Dps1 interface by default.
It can be added on WAN and LAN interfaces using `custom_structured_configuration`.

### WAN interfaces

A WAN interface in AVD is defined under the node settings under the `l3_interfaces` list. To be considered as a WAN interface by AVD, the l3_interface must have the `wan_carrier` key defined (which will allow to detect the path-group thanks to the carrier to path-group mapping). The `wan_circuit_id` is optional and used on CVaaS to provide more information in the visualization as well as in the AVD generated interface description. Finally the key `connected_to_pathfinder` allows to disable the static peering configuration on a given path-group.

```yaml
wan_router:
  defaults:
    loopback_ipv4_pool: 192.168.42.0/24
    vtep_loopback_ipv4_pool: 192.168.142.0/24
    uplink_ipv4_pool: 172.17.0.0/16
    bgp_as: 65000
    cv_pathfinder_region: Region_1
    cv_pathfinder_site: Site11
    nodes:
      - name: cv-pathfinder-edge
        id: 1
        uplink_switch_interfaces: [Ethernet1]
        l3_interfaces:
          # This is a WAN interface because `wan_carrier` is defined
          - name: Ethernet1
            peer: peer3
            peer_interface: Ethernet42
            wan_carrier: ISP-1
            wan_circuit_id: 666
            dhcp_accept_default_route: true
            ip_address: dhcp
          - name: Ethernet2
            wan_carrier: MPLS-1
            wan_circuit_id: 10555
            ip_address: 172.15.5.5/31
            peer_ip: 172.16.5.4
            static_routes:
              - prefix: 172.16.0.0/16
            connected_to_pathfinder: False
          # This is NOT a WAN interface
          - name: Ethernet3
            ip_address: 172.20.20.20/31
```

### Defining policies

TODO

### LAN Designs

!!! note

    An important design point to keep in mind is that the current CV Pathfinder and AutoVPN
    solutions require the Dps1 interface to be in VRF default.
    This implies that all the WAN interfaces also live in VRF default.
    And the LAN interfaces also have subnets in the default VRF.
    All of this means VRF default routing must be handled with care.

!!! warning

    AVD does not yet configure any route-map to filter potential routes received
    from the WAN for a WAN interface purpose (e.g. internet) to be advertised
    towards the LAN. The plan is to add an inbound route-map set the
    no-advertise community on the received routes.

    Similarly there is no current prevention to prevent advertising the LAN routes towards the WAN,
    The plan is to apply an outbound route-map preventing any routes to be advertised.

#### EBGP LAN

- the Site of Origin (SoO) extended community is configured as <router_id>:<site_id>
    note: site id is unique per zone (only a default zone supported today).
- the routes redistributed into BGP via the route-map `RM-CONN-2-BGP` are tagged with the SoO.
- the Underlay peer group (towards the LAN) is configured with two route-maps reused from existing designed but configured differently
  - one outbound route-map `RM-BGP-UNDERLAY-PEERS-OUT`:
    - advertised the local routes tagged with the SoO extended community.
    - advertised the routes received from iBGP (WAN) towards the LAN
  - one outbound route-map `RM-BGP-UNDERLAY-PEERS-IN`:
    - deny routes received from LAN that already contain the WAN AS in the path.
    - accept routes coming from the LAN and set the SoO extended community on them.
- For VRF default, there is a requirement to explicitly redistribute the routes for EVPN. The `RM-EVPN-EXPORT-VRF-DEFAULT` is configured to export the routes tagged with the SoO.

##### HA

for eBGP LAN routing protocol the following is done to enable HA:

- the uplink interfaces are used as HA interfaces.
- the subnets of the HA interfaces are redistributed to BGP via the `RM-CONN-2-BGP` route-map
BGP underlay peer group is configured with `allowas-in 1` to be able to learn the HA peer uplink interface subnet over the LAN as well as learning WAN routes from other sites (as backup in case all WAN links are lost).
- the Underlay peer group is configured with two route-maps
  - one inbound route-map `RM-UNDERLAY-PEERS-IN`
    - Match HA peer's uplink subnets (not marked) to be able to form HA tunnel (not exported to EVPN).
    - Match HA peer's originated prefixes, set longer AS path and mark with SoO to export to EVPN. These will be used as backup from other sites to destinations on HA Peer Router in case all WAN connections on Peer are down.
    - Match all WAN routes using AS path and set no-advertise community. This will be used as backup routes to the WAN in case this router looses all WAN connections.
    - Match anything else (LAN prefixes) and mark with the SoO `<bgp_as>:<wan_site_id>` to export to EVPN.
  - one outbound route-map `RM-UNDERLAY-PEERS-OUT`
    - allowing local routes marked with SoO (routes/interfaces defined via tenants + router-id)
    - allowing subnets of uplink interfaces.
    - allow all routes learned from iBGP (WAN)
    - Implicitly denying other routes which could be learned from BGP towards a WAN provider or redistributed without marking with SoO.

#### OSPF LAN

- Configure `underlay_routing_protocol` to OSPF for both the WAN router and the uplink router.

!!! warning

    In the current implementation, OSPF on LAN is not supported as there is no redistribution of route from OSPF to BGP and vice-versa implemented.

##### HA

The HA tunnel will come up properly today but route redistribution will be missing so it is not usable.

- the HA interface(s) is(are) the uplink interface(s) which are automatically included in  OSPF.

#### L2 LAN

- Configure `underlay_routing_protocol` to OSPF for both the WAN router and the uplink router.

!!! warning

    In the current implementation, OSPF on LAN is not supported as there is no redistribution of route from OSPF to BGP and vice-versa implemented.

##### HA

!!! warning

    Not Implemented - will be using VRRP

## Input variables

!!! warning
    All the keys in this section marked as PREVIEW or children of a key marked as
    PREVIEW are subject to change and are not supported.

### New node types in L3LS eos_designs

- `wan_router`: Edge routers for AutoVPN or Edge and Transit routers for CV Pathfinder depending on the `wan_mode` value.
- `wan_rr`: AutoVPN RR or Pathfinder depending on the `wan_mode` value.

The following table indicates the settings:

| Node Type Key | Underlay Router | Uplink Type | Default EVPN Role | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints | Defaut WAN Role | Default CV Pathfinder Role | Default Underlay Routing Protocol | Default Overlay Routing Protocol |
| ------------- | --------------- | ----------- | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- | --------------- | -------------------------- | --------------------------------- | -------------------------------- |
| wan_rr        | ✅               | p2p         | server            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | server          | pathfinder                 | none                           | iBGP                             |
| wan_router    | ✅               | p2p         | client            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | client          | edge                       | none                           | iBGP                             |

### WAN Settings

#### Top level keys

--8<--
roles/eos_designs/docs/tables/wan-settings.md
--8<--

##### WAN path-groups

--8<--
roles/eos_designs/docs/tables/wan-path-groups.md
--8<--

##### WAN carriers

--8<--
roles/eos_designs/docs/tables/wan-carriers.md
--8<--

##### WAN hierarchy

!!! note

    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
roles/eos_designs/docs/tables/wan-cv-pathfinder-regions.md
--8<--

#### WAN interfaces

--8<--
roles/eos_designs/docs/tables/wan-interfaces-settings.md
--8<--

#### WAN Virtual topologies

--8<--
roles/eos_designs/docs/tables/wan-virtual-topologies.md
--8<--

#### Application Classification

--8<--
roles/eos_designs/docs/tables/application-classification.md
--8<--

#### Flow Tracking Settings

--8<--
roles/eos_designs/docs/tables/flow-tracking-settings.md
--8<--

#### New BGP peer-group

--8<--
roles/eos_designs/docs/tables/wan-bgp-peer-groups.md
--8<--

#### New node keys

--8<--
roles/eos_designs/docs/tables/node-type-wan-configuration.md
--8<--

#### New node type keys

--8<--
roles/eos_designs/docs/tables/node-type-key-wan-configuration.md
--8<--

### CloudVision Tags

`arista.avd.eos_designs` will generate CloudVision Tags that assist CloudVision with visualizing the WAN.

The tags will only be generated when `wan_mode` is set to `cv-pathfinder`.

#### Device Tags

| Tag Name        | Source of information                                      |
| --------------- | ---------------------------------------------------------- |
| `Region`        | `cv_pathfinder_region`                                     |
| `Zone`          | `<region_name>-ZONE` for `wan_router`                      |
| `Site`          | `cv_pathfinder_site` for `wan_router`                      |
| `PathfinderSet` | name of `node_group` or default `PATHFINDERS` for `wan_rr` |
| `Role`          | `pathfinder`, `edge`, `transit region` or `transit zone`   |

#### Interface Tags

| Hint Tag Name | Source of information                       |
| ------------- | ------------------------------------------- |
| `Type`        | `lan` or `wan`                              |
| `Carrier`     | `wan_carrier` if this is a WAN interface    |
| `Circuit`     | `wan_circuit_id` if this is a WAN interface |
