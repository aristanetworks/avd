<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Brainstorm

## Table of contents - Input variables for eos_design

Node Type - Variables
Node Type customization
Type settings
Default node types settings
Node type settings
  Node type structure
  Node type common configurations
  Node type inband management
  Node type uplink management
  Node type L2 and MLAG configuration
  Node type Loopback and VTEP configuration
  Node type L3 interfaces
  Node type L3 port-channels
  Node type BGP configuration
  Node type Mutlicast configuration
  Node type network services configuration
  Node type EVPN gateway configuration
  Node type EVPN multi-domain gateway configuration
  Node type ISIS Configuration
  Node type MPLS configuration
  Node type WAN configuration
  Node type PTP configuration

### Variables

Table highlighting the different capabilities of the different node type key
List of default node types

- [node type key] (spine, l3leaf,l2leaf, wan_rr,...) with their
- associated functionality (Underlay Router, Uplink Type, EVPN Role, MPLS,... )

## Customization

Provider ??
AVD provides the capability to customize your node types, supporting a variety of designs.
Create or modify node_type keys

## Type setting

Question: This is where we reference/consume node_type_key?
The type: variable needs to be defined for each device in the fabric.
This is leveraged to load the appropriate settings to generate the configuration.

## Default node type setting

Assign a node type based on hostname ?

## Node type settings
