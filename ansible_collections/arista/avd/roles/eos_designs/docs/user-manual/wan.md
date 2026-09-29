---
# This title is used for search results
title: AVD Design data models for wan
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# WAN

Variables for WAN deployments, including AutoVPN and CV Pathfinder designs, hierarchy, transports, and related services.

## WAN Settings

### WAN generic settings

--8<--
schemas/avd_design/docs/tables/wan-settings.md
--8<--

### WAN hierarchy

!!! note

    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
schemas/avd_design/docs/tables/wan-cv-pathfinder-regions.md
--8<--

### WAN path-groups and carriers

--8<--
schemas/avd_design/docs/tables/wan-path-groups-and-carriers.md
--8<--

### WAN route-servers

--8<--
schemas/avd_design/docs/tables/wan-route-servers.md
--8<--

### WAN Virtual topologies

WAN virtual topologies leverage Deep Packet Inspection Engine to match traffic.

--8<--
schemas/avd_design/docs/tables/wan-virtual-topologies.md
--8<--

#### Application Classification

--8<--
schemas/avd_design/docs/tables/application-classification.md
--8<--

#### Internet Exit policies

!!! note

    This section is only relevant for CV Pathfinder and not for AutoVPN

--8<--
schemas/avd_design/docs/tables/cv-pathfinder-internet-exit-policies.md
--8<--

##### Zscaler Internet Exit

!!! note

    This data model is intended to be autofilled using a lookup plugin.
    See the top level key description for more information.

--8<--
schemas/avd_design/docs/tables/zscaler-endpoints.md
--8<--

### WAN Zscaler Integration

--8<--
schemas/avd_design/docs/tables/wan-cv-pathfinder-zscaler-integration.md
--8<--
