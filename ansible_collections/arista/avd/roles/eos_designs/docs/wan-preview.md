---
# This title is used for search results
title: Ansible Collection Role eos_design - WAN preview
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# WAN preview

!!! warning
    The integration of WAN designs to `eos_designs` role is in preview mode.

    Everything is subject to change, is not supported and may not be complete.

    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)

## Overview

The intention is to support both a single [AutoVPN design](https://www.arista.com/en/cg-veos-router/veos-router-auto-vpn) and [CV Pathfinder](https://www.arista.com/en/solutions/enterprise-wan/pathfinder).

### Design points

1. The intent is to be able to support having the different WAN participating devices in different inventories.
2. Only iBGP is supported as an overlay_routing_protocol.
3. On the AutoVPN Route Reflectors and Pathfinders, a listen range statement is used for BGP to allow for point number 1.
4. The default VRF is being configured by default on all WAN devices with a `vni_id` of 1. To override this, it is necessary to configure the `default` VRF in a tenant in `network_services`.
5. When configuring HA on a site, the path-group ID `65535` is reserved for the path-group called `LAN_HA`.

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

## Future work

- As of now, only the fundations of the `eos_designs` functionality for WAN is
    being introduced without any support for LAN and WAN interfaces.
    This implies that path-groups are not configured.
- The configuration of AVT policies is not supported yet and will be introduced
    later.
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

| Node Type Key      | Underlay Router | Uplink Type | Default EVPN Role  | L2 Network Services | L3 Network Services | VTEP | MLAG Support | Connected Endpoints | Defaut WAN Role | Default CV Pathfinder Role |
| ------------------ | --------------- | ------------ | ----------------- | ------------------- | ------------------- | ---- | ------------ | ------------------- | --------------- | -------------------------- |
| wan_rr             | ✅              | p2p          | server            | ✘                   | ✅                  | ✘    | ✘            | ✘                   | server          | pathfinder                 |
| wan_edge           | ✅              | p2p          | client            | ✘                   | ✅                  | ✘    | ✘            | ✘                   | client          | edge                       |
| wan_transit        | ✅              | p2p          | client            | ✘                   | ✅                  | ✘    | ✘            | ✘                   | client          | transit region             |

All these node types are defined with `default_underlay_routing_protocol: none` and `default_overlay_routing_protocol: ibgp`.

### WAN Settings

#### Top level keys

--8<--
roles/eos_designs/docs/tables/wan-settings.md
--8<--

#### WAN hierarchy

!!! note
    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
roles/eos_designs/docs/tables/wan-cv-pathfinder-regions.md
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
