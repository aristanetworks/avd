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
  - For the policy defined for VRF `default` (or the auto-generared one), an extra match statement is injected in the policy to match the traffic towards the Pathfinders or AutoVPN RRs, the name of the application-profile is hardcoded as `CONTROL-PLANE-APPLICATION-PROFILE`. A special policy is created by appending `-WITH-CP` at the end of the targetted policy name.

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

- No IPv6 support
- For WAN interfaces, NAT IP on the Pathfinder side can be supported using the `wan_route_servers.path_groups.interfaces` key.
- Path-group ID is currently required under `wan_path_groups` until an algorithm is implemented to auto generate IDs.

## Future work

- As of now, only the fundations of the `eos_designs` functionality for WAN is being introduced without any support for LAN interfaces.
- Auto generation of Path-group IDs and other IDs.
- HA for sites will be covered in a future PR

## `eos_cli_config_gen` support

- `eos_cli_config_gen` schema should support all of the required keys to
    configure a WAN network, whether AutoVPN or Pathfinder. If you find any
    missing functionality, please open an issue on Github.

## Input variables

!!! warning
    All the keys in this section marked as PREVIEW or children of a key marked as
    PREVIEW are subject to change and are not supported.

### New node types in L3LS eos_designs

- `wan_edge`: Edge routers for AutoVPN or Pathfinder depending on the `wan_mode` value.
- `wan_transit`: Transit routers in Pathfinder context, not supported for AutoVPN.
- `wan_rr`: AutoVPN RR or Pathfinder depending on the `wan_mode` value.

The following table indicates the settings:

| Node Type Key | Underlay Router | Uplink Type | Default EVPN Role | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints | Defaut WAN Role | Default CV Pathfinder Role |
| ------------- | --------------- | ----------- | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- | --------------- | -------------------------- |
| wan_rr        | ✅               | p2p         | server            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | server          | pathfinder                 |
| wan_edge      | ✅               | p2p         | client            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | client          | edge                       |
| wan_transit   | ✅               | p2p         | client            | ✘                   | ✅                   | ✅    | ✘            | ✘                   | client          | transit region             |

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

#### Application traffic recognition

--8<--
roles/eos_designs/docs/tables/application-traffic-recognition.md
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

#### Device Tags

| Tag Name        | Source of information                                                                 |
| --------------- | ------------------------------------------------------------------------------------- |
| `Region`        | `cv_pathfinder_region` if `cv_pathfinder_role` is set but not `pathfinder`            |
| `Zone`          | `DEFAULT-ZONE` if `cv_pathfinder_role` is set but not `pathfinder`                    |
| `Site`          | `cv_pathfinder_site` if `cv_pathfinder_role` is set but not `pathfinder`              |
| `PathfinderSet` | name of `node_group` or default `PATHFINDERS` if `cv_pathfinder_role` is `pathfinder` |
| `Role`          | `cv_pathfinder_role` if set                                                           |

#### Interface Tags

| Hint Tag Name | Source of information                                                       |
| ------------- | --------------------------------------------------------------------------- |
| `Type`        | `lan` or `wan` if `cv_pathfinder_role` is set                               |
| `Carrier`     | `wan_carrier` if `cv_pathfinder_role` is set and this is a WAN interface    |
| `Circuit`     | `wan_circiot_id` if `cv_pathfinder_role` is set and this is a LAN interface |

## Getting started with WAN

### Global settings

TODO - cover here WAN hierarchy, wan mode, route-servers, path-groups and carriers and how they are linked together.

### WAN interfaces

TODO

### Defining policies

TODO
