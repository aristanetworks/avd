---
# This title is used for search results
title: AVD example for a single data center using multiple pods for l3ls
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD example for a single data center with Multi-Pod using L3LS

## Introduction

This example shows how to create a multi-pod environment (also known as a 5-stage Clos) in a single DC environment. This can be used in multiple DCs of course, but this example is only for two pods in a single DC.

Also included is an example of connecting an external router to a VRF/tenant.

This example will not teach all the aspects of a l3ls EVPN/VXLAN build, see the single-dc-l3ls directory for that. This is a supplement to single-dc-l3ls, concentrating on the aspects that are unique when doing multiple pods/5-stage Clos.

Ansible playbooks are included to show the following:

- Building the intended configuration and documentation
- Deploying the configuration via CloudVision to the switches, including a full change-based workflow with rollback capability etc.
- Validating the configuration

## Overall design overview

### Physical topology

The drawing below shows the physical topology used in this example. The interface assignment shown here are referenced across the entire example, so keep that in mind if this example must be adapted to a different topology.

![Figure: Arista Leaf Spine physical topology](images/l3ls-multipod.png)

### Fabric Design

The fabric is a basic l3ls EVPN/VXLAN design with a multi-pod (5-stage Clos) architecture.

## Ansible inventory, group vars, and naming scheme

The following drawing shows a graphic overview of the Ansible inventory, group variables, and naming scheme used in this example:

![Figure: Arista Leaf Spine physical topology](images/inventory.png)

There is the addition of a SUPERSPINES group as well as a POD1 and POD2 groups with PODX_LEAFS and PODX_SPINES under each. The EVPN_SERVICES and ENDPOINT_CONNECT allow separation of YAML files, and putting the PODX_LEAFS under them will build the appropriate configs for those devices (VXLAN/VLAN/anycast gateways do not get instantiated on spines, of course).

### Content of the inventory.yml file

```yaml title="inventory.yml"
--8<--
examples/single-dc-multipod-l3ls/inventory.yml
--8<-
```

## FABRIC Files

With the topology, five YAML files are used in group_vars:

- FABRIC.yml
- POD1.yml
- POD2.yml
- EVPN_SERVICES.yml
- ENDPOINT_CONNECT.yml

The FABRIC.yml file contains parameters that would apply to the entire fabric, such as `evpn_vlan_aware_bundles: true`. FABRIC.yml also contains the definitions for the superspines.

```yaml title="FABRIC.yml"
---

fabric_name: FABRIC

# Various fabric settings

# Enable vlan aware bundles
evpn_vlan_aware_bundles: true

# Super-Spine Switches
super_spine:
  defaults:
    platform: cEOS
    bgp_as: 65000
    loopback_ipv4_pool: 192.168.101.0/24
    mlag: false
    evpn_role: server

  nodes:
    superspine1:
      id: 201
      mgmt_ip: 192.168.0.25/24
    superspine2:
      id: 202
      mgmt_ip: 192.168.0.26/24
```

The pod leafs and spines are not in the FABRIC.yml file in this example (although the contents of POD1.yml and POD2.yml could be consolidated into FABRIC.yml). The super_spine section is new, but it works much like the traditional spine section did in a single pod l3ls. It will need an ASN (seprate from the pod spines), loopback pool (which can the same pool as the pods, as long as the IDs are unique). The `evpn_role` server makes the super-spines a router server, as the routes from the pods will need to be propagated to each other.

The rest of the FABRIC.yml would contain any parameters for your fabric, such as NTP servers, user accounts, and p2p MTUs.

The POD1 and POD2 YAML files contain the descriptions of the leafs and spines. Note that each pod's spines have their own unique ASN (eBGP). Also the spines now have uplink interfaces and uplinks switches specificed (to the superspines) with the `uplink_switches` and `uplink_interfaces` directives. The uplink pool can overlap between the pods in a DC. If doing multi-DC, the pools should be on different subnets.

The leaf configurations, EVPN_SERVICES and ENDPOINT_CONNECT sections aren't affected by the multi-pod format.

```yaml title="POD1.yml"
--8<--
examples/single-dc-multipod-l3ls/group_vars/POD1.yml
--8<-
```

## Connecting an External Router

In addition to multi-pod, this example also has a tenant/VRF connecting to an external network via a router (R1). This is defined in the EVPN_SERVICES.yml file. The `l3_interfaces` parameter creates an L3 interface in the VRF on a specific leaf, and the `bgp_peer` section.

```yaml
--8<--
examples/single-dc-multipod-l3ls/group_vars/EVPN_SERVICES.yml
--8<--
```
