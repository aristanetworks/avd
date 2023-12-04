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

The intention is to support both a single AutoVPN design
[https://www.arista.com/en/cg-veos-router/veos-router-auto-vpn](https://www.arista.com/en/cg-veos-router/veos-router-auto-vpn)
and Pathfinder
[https://www.arista.com/en/solutions/enterprise-wan/pathfinder](https://www.arista.com/en/solutions/enterprise-wan/pathfinder).

## Known limitations

- As of now, only the fundations of the `eos_designs` functionality for WAN is
    being introduced without any support for LAN and WAN interfaces.

## `eos_cli_config_gen` support

- `eos_cli_config_gen` schema should support all of the required keys to
    configure a WAN network, whether AutoVPN or Pathfinder. If you find any
    missing functionality, please open an issue on Github.

## Input variables

!!! warning
    All the keys in this section marked as PREVIEW or children of a key marked as
    PREVIEW are subject to change and are not supported.

### New node types in L3LS eos_designs

- `edge`: Edge routers for AutoVPN or Pathfinder.
- `transit`: Transit routers in Pathfinder context, not supported for AutoVPN.
- `wan_controller`: AutoVPN RR or Pathfinder

### WAN Settings

#### Top level keys

--8<--
roles/eos_designs/docs/tables/wan-settings.md
--8<--

#### New node keys

--8<--
roles/eos_designs/docs/tables/node-type-wan-configuration.md
--8<--

#### New node type keys

--8<--
roles/eos_designs/docs/tables/node-type-key-wan-configuration.md
--8<--
