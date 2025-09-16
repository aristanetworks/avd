
<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# How-To Guide: AVD Network Services

## Introduction to AVD Network Services

In Arista Validated Designs (AVD), **"Network Services"** is an abstracted data model that allows you to define and deploy Layer 2 (VLANs) and Layer 3 (VRF) services across your entire fabric from a central location.

The model is designed to be tenant-based, meaning you group network services under a **"tenant"** which can represent an organization, department, or any logical container. This structure allows for the reuse of VLAN and SVI IDs across different tenants while ensuring that configurations are deployed only to the relevant devices in the fabric.

## Core Concept: Tenants

Everything starts with a tenant. A tenant is the top-level key under which you define all associated VRFs and VLANs.

- **Grouping:** Tenants group VRFs and L2 VLANs.

- **VNI Range:** For EVPN VXLAN fabrics, each tenant is assigned a `mac_vrf_vni_base`. This number is used to automatically calculate the VXLAN Network Identifier (VNI) for each VLAN/SVI within that tenant (e.g., `vni = mac_vrf_vni_base + vlan_id`).

- **Filtering:** AVD uses a filtering model to control which devices a tenant's configuration is applied to. This is typically done using tags.

### Basic Tenant Structure

```yaml
tenants:
  - name: MY_TENANT
    mac_vrf_vni_base: 10000
    vrfs:
      # ... VRF definitions go here
    l2vlans:
      # ... L2 VLAN definitions go here

```

## How-To: Configure L3 Services (VRFs and SVIs)

L3 services are defined under the `vrfs` list within a tenant. A VRF contains Switched Virtual Interfaces (SVIs) which act as the default gateways for your VLANs.

### Step 1: Define the VRF

Inside a tenant, create an entry in the `vrfs` list. Each VRF needs a unique name.

### Step 2: Define the SVIs (Gateways)

Inside the VRF, create a list of `svis`. Each SVI requires:

- `id`: The VLAN ID for the SVI.
- `name`: A descriptive name for the VLAN.
- `ip_address_virtual`: The virtual IP address that will be shared across all leafs where this SVI is deployed. This is typically a VARP/Anycast Gateway address.

### Example: VRF with two SVIs

```yaml
tenants:
  - name: CORP_TENANT
    mac_vrf_vni_base: 20000
    vrfs:
      - name: CORP_VRF_1
        svis:
          # SVI for the Web Servers VLAN
          - id: 110
            name: WEB_VLAN
            tags: ["web"]
            ip_address_virtual: 10.1.10.1/24

          # SVI for the App Servers VLAN
          - id: 120
            name: APP_VLAN
            tags: ["app"]
            ip_address_virtual: 10.1.20.1/24

```

In this example:

- The SVI for VLAN 110 will have a VNI of `20110`.
- The SVI for VLAN 120 will have a VNI of `20120`.
- The `tags` are used to control which devices or interfaces receive this configuration.

## How-To: Configure L2 Services (L2VLANs)

Sometimes you need to stretch a VLAN across the fabric without an L3 gateway. These are defined under the `l2vlans` list within a tenant.

### Step 1: Define the L2VLAN

Inside a tenant, create an entry in the `l2vlans` list. Each L2VLAN requires:

- `id`: The VLAN ID.

- `name`: A descriptive name.

### Example: L2VLAN for a storage network

```yaml
tenants:
  - name: STORAGE_TENANT
    mac_vrf_vni_base: 30000
    l2vlans:
      - id: 250
        name: ISCSI_STORAGE
        tags: ["storage"]

```

In this example, VLAN 250 will be created and stretched across any devices matching the `storage` tag, but it will not have an SVI or IP address managed by AVD's network services model.

## Complete Tenant Example

Here is a complete example combining the concepts above into a single tenant definition. This would typically be placed in a file like `group_vars/TENANTS.yml`.

```yaml
tenants:
  - name: CORP_SERVICES # (1)!
    mac_vrf_vni_base: 10000 # (2)!

    vrfs: # (3)!
      - name: VRF_PROD
        svis: # (4)!
          - id: 101
            name: PROD_SERVERS
            tags: [prod]
            ip_address_virtual: 172.16.1.1/24
            structured_config: # (5)!
              ip_helper_address:
                - 10.0.0.10
                - 10.0.0.11

          - id: 102
            name: PROD_DATABASE
            tags: [prod, db]
            ip_address_virtual: 172.16.2.1/24

    l2vlans: # (6)!
      - id: 500
        name: BACKUP_NETWORK
        tags: [backup]
```

1. Tenant for Corporate Services
2. VNI for each SVI will be 10000 + <vlan_id>
3. VRFs for this Tenant
4. SVIs (L3 Gateways) for this VRF
5. Optional: Add custom structured config like DHCP helper addresses
6. This will be an L2-only VLAN with VNI 10500
