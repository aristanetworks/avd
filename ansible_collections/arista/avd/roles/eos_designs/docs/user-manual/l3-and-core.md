---
# This title is used for search results
title: AVD Design data models for l3 and core
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# L3 edge and core

Configure additional L3 point-to-point links at the edge or between sites, and define core-facing interfaces where the design uses a dedicated core layer.

## L3 edge and DCI settings

The `l3_edge` data model can be used to configure extra L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.

The data model supports using IP pools, Subnet per link, specifying the IP addresses manually or using ipv6 with rfc5549. One of these options must be set.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

--8<--
schemas/avd_design/docs/tables/l3-edge.md
--8<--

## Core interfaces settings

The `core_interfaces` data model can be used to configure L3 P2P links anywhere in the fabric. It can be between two switches that are already part of the fabric inventory, or it can be towards another device, where only one end of the link is on a switch in the fabric.

The data model supports using IP pools, Subnet per link or specifying the IP addresses manually.
For BGP peerings the AS number must be specified. If the AS number is different than the AS number configured for the node, the local-as will be replaced on this BGP peering (`neighbor <ip> local-as <as> no-prepend replace-as`).

Make sure to configure the variables in a group_vars file covering all devices mentioned in the data model.

--8<--
schemas/avd_design/docs/tables/core-interfaces.md
--8<--
