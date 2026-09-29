---
# This title is used for search results
title: AVD Design data models for network services
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Network services

Define tenants, VRFs, VLANs, SVIs, and related overlay services once at fabric scope, then control where each service is deployed using tags and node-type filters.

## Network Services

The network services variables provide an abstracted model to define network services across the fabric.
The network services are grouped by tenants. The definition of a tenant may vary between organizations. E.g. tenants can be organizations or departments.

The filtering models defined under [Node type network services configuration](#node-type-network-services-configuration) allows
for granular deployment of network services to the fabric leveraging the tenant name and tags applied to the service definition.

- This allows for the reuse of SVI/VLAN IDs across the fabric.
- An error will be returned at runtime in case of duplicate or conflicting SVI/VLAN IDs or VNIs targeted towards the same device.

### Network services settings

The supported network services for each tenant cover:

- VRFs
  - SVIs
  - L3 Interfaces
  - Loopbacks
  - BGP routing
  - OSPF routing
- L2 VLANs
- Point-to-point services (Pseudowires, only for MPLS designs)
- Multicast

Typically services within each tenant share common VNI ranges and MAC VRF assignment pattern.

The keys used to define network services are configurable using [`network_services_keys`](#network-services-keys-settings).
The default available keys is `tenants`.

--8<--
schemas/avd_design/docs/tables/network-services.md
--8<--

#### Network services VRFs configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-settings.md
--8<--

#### Network services VRF SVIs configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-svis-settings.md
--8<--

#### Network services VRF L3 Interfaces configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-l3-interfaces-settings.md
--8<--

#### Network services VRF L3 Port-Channels configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-l3-port-channel-settings.md
--8<--

#### Network services VRF Loopbacks configuration

Loopbacks are usually configured with `vtep_diagnostic` which supports IP pools etc.

`loopbacks` is used to provision extra loopback interfaces with manually assigned
IP addresses on individual nodes.

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-loopbacks-settings.md
--8<--

#### Network services VRF BGP configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-bgp-settings.md
--8<--

#### Network services VRF OSPF configuration

--8<--
schemas/avd_design/docs/tables/network-services-vrfs-ospf-settings.md
--8<--

#### Network services L2 VLANs configuration

--8<--
schemas/avd_design/docs/tables/network-services-l2vlans-settings.md
--8<--

#### Network services point-to-point services configuration

--8<--
schemas/avd_design/docs/tables/network-services-point-to-point-services-settings.md
--8<--

#### Network services multicast configuration

--8<--
schemas/avd_design/docs/tables/network-services-multicast-settings.md
--8<--

### SVI profiles settings

SVI profiles can be leveraged to share common settings between SVIs.

- Keys are the same as those used under SVI settings, except for the `tags` key.
- Keys defined under SVIs take precedence.
- Structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:

  1. svi.nodes[inventory_hostname].structured_config
  2. svi_profile.nodes[inventory_hostname].structured_config
  3. svi_parent_profile.nodes[inventory_hostname].structured_config
  4. svi.structured_config
  5. svi_profile.structured_config
  6. svi_parent_profile.structured_config

--8<--
schemas/avd_design/docs/tables/svi-profiles.md
--8<--

### EVPN VLAN aware bundles settings

EVPN VLAN aware bundles referenced by name in `<network_services_key>[].evpn_vlan_bundle` or `<network_services_key>[].vrfs[].svis[].evpn_vlan_bundle` or `<network_services_key>[].l2vlans[].evpn_vlan_bundle`.

An EVPN VLAN aware bundle will only be configured if at least one VLAN is associated with it.

--8<--
schemas/avd_design/docs/tables/evpn-vlan-bundles.md
--8<--

### Network services keys settings

Network Services can be grouped by using separate keys.

The keys can be customized to provide a better better organization or grouping of your data.
`network_services_keys` should be defined in the top level group_vars for the fabric.

!!! note
    The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.

--8<--
schemas/avd_design/docs/tables/network-services-keys.md
--8<--
