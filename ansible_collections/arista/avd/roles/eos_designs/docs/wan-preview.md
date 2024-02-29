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

The intention is to support both a single [AutoVPN design](https://www.arista.com/en/cg-veos-router/veos-router-auto-vpn) and [CV Pathfinder](https://www.arista.com/en/solutions/enterprise-wan/pathfinder).

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

#### LAN Designs

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

##### EBGP LAN

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

###### HA

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

##### OSPF LAN HA

- Configure `underlay_routing_protocol` to OSPF for both the WAN router and the uplink router.

!!! warning

    In the current implementation, OSPF on LAN is not supported as there is no redistribution of route from OSPF to BGP and vice-versa implemented.

###### HA

The HA tunnel will come up properly today but route redistribution will be missing so it is not usable.

- the HA interface(s) is(are) the uplink interface(s) which are automatically included in  OSPF.

## Known limitations

- Zones are not configurable for CV Pathfinder. All sites are being configured in a default zone `DEFAULT-ZONE` with ID `1`.
- Because of the previous point, in `eos_designs`, the `transit` node type is always configured as `transit region`.
- For `cv-pathfinder` mode, the following flow-tracking configuration is applied
    without any customization possible:

    ```eos
    flow tracking hardware
       tracker WAN-FLOW-TRACKER
        record export on inactive timeout 70000
        record export on interval 5000
        exporter DPI-EXPORTER
         collector 127.0.0.1
         local interface Loopback0
         template interval 5000
    ```

- All Pathfinders must be able to create a full mesh
- No IPv6 support
- For WAN interfaces, NAT IP on the Pathfinder side can be supported using the `wan_route_servers.path_groups.interfaces` key.
- Path-group ID is currently required under `wan_path_groups` until an algorithm is implemented to auto generate IDs.
- It is not yet supported to disable HA on a specific LAN interface on the device, nor is it supported to add HA configuration on a non-uplink interface.
- The name of the AVT policies and AVT profiles are configurable in the input variables. The Load Balance policies are named `LB-<profile_name>` and are not configurable.
- For LAN, the current supported funcitonality is to use `uplink_type: p2p-vrfs` on the WAN routers and to have the relevant VRFs present on the uplink switches via `network_services`. Other LAN scenarios will come with time.
- HA for AutoVPN is not supported

## Future work

- Auto generation of Path-group IDs and other IDs.
- New LAN scenarios (L2, ..)
- HA for AutoVPN
- Proper OSPF-BGP redistribution in VRF default.
- Support for OSPF subinterfaces.

## `eos_cli_config_gen` support

- `eos_cli_config_gen` schema should support all of the required keys to
    configure a WAN network, whether AutoVPN or Pathfinder. If you find any
    missing functionality, please open an issue on Github.

## Input variables

!!! warning
    All the keys in this section marked as PREVIEW or children of a key marked as
    PREVIEW are subject to change and are not supported.

### New node types in L3LS eos_designs

- `wan_router`: Edge routers for AutoVPN or Edge and Transit routers for CV Pathfinder depending on the `wan_mode` value.
- `wan_rr`: AutoVPN RR or Pathfinder depending on the `wan_mode` value.

The following table indicates the settings:

| Node Type Key | Underlay Router | Uplink Type | Default EVPN Role | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints | Defaut WAN Role | Default CV Pathfinder Role |
| ------------- | --------------- | ----------- | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- | --------------- | -------------------------- |
| wan_rr        | ✅               | p2p         | server            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | server          | pathfinder                 |
| wan_router    | ✅               | p2p         | client            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | client          | edge                       |

All these node types are defined with `default_underlay_routing_protocol: none` and `default_overlay_routing_protocol: ibgp`.

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
| `Region`        | `cv_pathfinder_region` for `wan_router`                    |
| `Zone`          | `DEFAULT-ZONE` for `wan_router`                            |
| `Site`          | `cv_pathfinder_site` for `wan_router`                      |
| `PathfinderSet` | name of `node_group` or default `PATHFINDERS` for `wan_rr` |
| `Role`          | `pathfinder`, `edge`, `transit region` or `transit zone`   |

#### Interface Tags

| Hint Tag Name | Source of information                       |
| ------------- | ------------------------------------------- |
| `Type`        | `lan` or `wan`                              |
| `Carrier`     | `wan_carrier` if this is a WAN interface    |
| `Circuit`     | `wan_circuit_id` if this is a WAN interface |

## Getting started with WAN

### Global settings

TODO - cover here WAN hierarchy, wan mode, route-servers, path-groups and carriers and how they are linked together.

### WAN interfaces

TODO

### Defining policies

TODO
