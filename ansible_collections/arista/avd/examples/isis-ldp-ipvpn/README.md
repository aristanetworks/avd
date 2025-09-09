---
# This title is used for search results
title: MPLS-VPN based WAN Network
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# MPLS-VPN based WAN Network

## Introduction

This example is the logical second step in introducing AVD to new users, following the [Introduction to Ansible and AVD](../../../../../docs/user-manual/intro-to-ansible-and-avd.md) section. New users with access to virtual routers (using Arista vEOS-lab or cEOS) can learn how to generate configuration and documentation for a complete fabric environment. Users with access to physical routers will have to adapt a few settings. This is all documented inline in the comments included in the YAML files. If a lab with virtual or physical routers is not accessible, this example can also be used to only generate the output from AVD if desired.

The example includes and describes all the AVD files and their content used to build a MPLS-VPN WAN network covering two sites using the following:

- Four (virtual) p routers.
- Three (virtual) pe routers serving aggregation devices and CPEs.
- Two (virtual) route reflectors act as route servers for the WAN.

This example does not include Integration with CloudVision to keep everything as simple as possible. In this case, the Ansible host will communicate directly with the routers using eAPI.

## AVD Playground

--8<--
ansible_collections/arista/avd/examples/common/start-avd-playground.md
--8<--

## Installation

--8<--
ansible_collections/arista/avd/examples/common/example-installation.md
--8<--

```shell
ansible-avd-examples/ (or wherever the playbook was run)
  |── isis-ldp-ipvpn
    ├── ansible.cfg
    ├── build.yml
    ├── deploy.yml
    ├── documentation
    ├── group_vars
    ├── images
    ├── intended
    ├── inventory.yml
    ├── README.md
    └── switch-basic-configurations
```

## Overall design overview

### Physical topology

The drawing below shows the physical topology used in this example. The interface assignment shown here is referenced across the entire example, so keep that in mind if this example must be adapted to a different topology. Finally, the Ansible host is connected to the dedicated out-of-band management port (Management1 when using vEOS-lab):

![Figure: Arista MPLS-VPN physical topology](images/avd-isis-ldp-ipvpn.svg)

### IP ranges used

| Out-of-band management IP allocation for WAN1 | 172.16.1.0/24 |
| --------------------------------------------- | ------------- |
| Default gateway | 172.16.1.1 |
| p1 | 172.16.1.11 |
| p2 | 172.16.1.12 |
| p3 | 172.16.1.13 |
| p4 | 172.16.1.14 |
| pe1 | 172.16.1.101 |
| pe2 | 172.16.1.102 |
| pe3 | 172.16.1.103 |
| rr1 | 172.16.1.151 |
| rr2 | 172.16.1.152 |
| **Point-to-point links between network nodes** | **(Underlay)** |
| WAN1 | 10.255.3.0/24 |
| **Loopback0 interfaces for router ID (p)** | 10.255.0.0/27 |
| **Loopback0 interfaces for overlay peering (pe)** | 10.255.1.0/27 |
| **Loopback0 interfaces for overlay peering (rr)** | 10.255.2.0/27 |
| **L3 Interfaces** | **10.0-1.1.0/24** |
| For example pe1 `Ethernet3.10` has the IP address: | 10.0.1.1 |
| For example pe3 `Ethernet4` has the IP address: | 10.1.1.9 |

### ISIS-LDP design

=== "Underlay"

    ![Figure: Arista Underlay ISIS-LDP Design](images/isis-ldp-underlay.svg)

### BGP design

=== "Overlay"

    ![Figure: Arista Overlay BGP Design](images/bgp-overlay.svg)

### Basic EOS config

Basic connectivity between the Ansible host and the routers must be established before Ansible can be used to push configurations. You must configure the following on all routers:

- A hostname configured purely for ease of understanding.
- An IP enabled interface - in this example, the dedicated out-of-band management interface is used.
- A username and password with the proper access privileges.

Below is the basic configuration file for `p1`:

```eos title="p1-basic-configuration.txt"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/switch-basic-configurations/p1-basic-configuration.txt
--8<--
```

!!! note
    The folder `isis-ldp-ipvpn/switch-basic-configurations/` contains a file per device for the initial configurations.

## Ansible inventory, group vars, and naming scheme

The following drawing shows a graphic overview of the Ansible inventory, group variables, and naming scheme used in this example:

![Figure: Ansible inventory and vars](images/ansible-groups.svg)

!!! note
    The CPE's and aggregation nodes are **not** configured by AVD, but the ports used to connect to them are.

Group names use uppercase and underscore syntax:

- FABRIC
- WAN1
- WAN1_P_ROUTERS
- WAN1_PE_ROUTERS
- WAN1_RR_ROUTERS

All hostnames use lowercase, for example:

- p4
- pe1
- rr2

The drawing also shows the relationships between groups and their children:

- For example, `p1`, `p2`, `p3`, and `p4` are all children of the group called `WAN1_P_ROUTERS`.

Additionally, groups themselves can be children of another group, for example:

- `WAN1_P_ROUTERS` is a child of the group `WAN1`.
- `WAN1_PE_ROUTERS` is a child of both `WAN1` and `NETWORK_SERVICES`.

This naming convention makes it possible to extend anything easily, but as always, this can be changed based on your preferences. Just ensure that the names of all groups and hosts are unique.

### Content of the inventory.yml file

This section describes the entire `ansible-avd-examples/isis-ldp-ipvpn/inventory.yml` file used to represent the above topology.

The hostnames specified in the inventory must exist either in DNS or in the hosts file on your Ansible host to allow successful name lookup and be able to reach the routers directly. A successful ping from the Ansible host to each inventory host verifies name resolution(e.g., `ping p1`).

Alternatively, if there is no DNS available, or if devices need to be reached using a fully qualified domain name (FQDN), define `ansible_host` to be an IP address or FQDN for each device - see below for an example:

```yaml title="inventory.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/inventory.yml
--8<--
```

The above is included in this example, *purely* to make it as simple as possible. However, in the future, please do not carry over this practice to a production environment, where an inventory file for an identical topology should look as follows when using DNS:

```yaml title="inventory_no_ip.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/inventory_no_ip.yml
--8<--
```

1. `NETWORK_SERVICES`

    - Creates a group named `NETWORK_SERVICES`. Ansible variable resolution resolves this group name to the identically named group_vars file (`ansible-avd-examples/isis-ldp-ipvpn/group_vars/NETWORK_SERVICES.yml`).

    - The file's contents are specifications of tenant VRFs and their associated routed interfaces, BGP peers, and OSPF interfaces, then applied to the group's children. In this case, the group `WAN1_PE_ROUTERS`.

## Defining device types

Since this example covers building a MPLS WAN network, AVD must know about the device types, for example, p, pe, rr routers, etc. The devices are already grouped in the inventory, so the device types are specified in the group variable files with the following names and content:

=== "WAN1_P_ROUTERS.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1_P_ROUTERS.yml
    --8<--
    ```

=== "WAN1_PE_ROUTERS.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1_PE_ROUTERS.yml
    --8<--
    ```

=== "WAN1_RR_ROUTERS.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1_RR_ROUTERS.yml
    --8<--
    ```

For example, all routers that are children of the WAN1_P_ROUTERS group defined in the inventory will be of type `p`.

## Setting fabric-wide configuration parameters

The `ansible-avd-examples/isis-ldp-ipvpn/group_vars/FABRIC.yml` file defines generic settings that apply to all children of the `FABRIC` group as specified in the inventory described earlier.

```yaml title="FABRIC.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/FABRIC.yml
--8<--
```

1. The Ansible host must use eAPI.
2. Network OS which in this case is Arista EOS.
3. The username/password combo.
4. How to escalate privileges for write access.
5. Use SSL.
6. Do not validate SSL certificates.
7. The name of the fabric for internal AVD use. This name *must* match the name of an Ansible Group (and therefore a corresponding group_vars file) covering all network devices.
8. Generate CSVs with fabric link info.
9. Define underlay and overlay routing protocols to be used.
10. Local users/passwords and their privilege levels. In this case, the `admin` user is set with no password and the `arista` user is set with the password `arista`.
11. BGP peer groups and their passwords (all passwords are "arista").
12. Internal storage encryption-key.

## Setting device-specific configuration parameters

The `ansible-avd-examples/isis-ldp-ipvpn/group_vars/WAN1.yml` file defines settings that apply to all children of the `WAN1` group as specified in the inventory described earlier. However, this time the settings defined are no longer fabric-wide but are limited to WAN1. This example is of limited benefit with only a single data center. Still, it allows us to scale the configuration to a scenario with multiple data centers in the future.

```yaml title="WAN1.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1.yml:1:27
--8<--
```

1. The default gateway for the management interface of all devices in WAN1 is defined.
2. iBGP ASN for the Fabric.
3. BGP distance for specific route types.
4. `platform` references default settings defined in AVD specific to certain switch platforms.
5. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0.
6. ISIS NET system id prefix.
7. `nodes` defines the actual p routers, using the hostnames defined in the inventory.
8. The name of the node to be defined (must be consistent with definition in inventory).
9. `id` is used to calculate the various IP addresses, for example, the IPv4 address for the Loopback0 interface. In this case, p1 will get the IPv4 address 10.255.0.1/27 assigned to the Loopback0 interface.
10. `mgmt_ip` defines the IPv4 address of the management interface. As stated earlier, Ansible will perform name lookups using the hostnames specified in the inventory unless using the `ansible_host` option. However, there is no automatic mechanism to grab the result of the name lookup and use that to generate the management interface configuration.

The following section covers the pe routers. Significantly more settings need to be set compared to the p routers:

```yaml title="WAN1.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1.yml:35:59
--8<--
```

1. `platform` references default settings defined in AVD specific to certain switch platforms.
2. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0. Please note that this IP pool differs from the one used for the p routers in this example. If you want to reuse the same IP pool for multiple node types to avoid setting the same IP addresses for several devices, we can define the option `loopback_ipv4_offset`.
3. `virtual_router_mac_address` defines the MAC address used for the anycast gateway on the various subnets. This is the MAC address connected endpoints will learn when ARPing for their default gateway. It is irrelevant for the vpn-ipv4/6 services used in this example but is still mandatory to set.
4. `mpls_route_reflectors` defines which route reflectors the pe nodes peer with for overlay route distribution.
5. `isis_system_id_prefix` is mandatory to set when using ISIS for the underlay routing protocol. It is used to calculate the ISIS NET ID.
6. `spanning_tree_mode` defines the spanning tree mode. In this case, we are not using spanning tree since we have only routed interfaces on our pe routers.
7. `node_groups` defines settings common to more than one node. In the l3ls-evpn design this has more utility than here, which is used to define MLAG pairs. In the MPLS design, it is mainly used to logically group devices for organizational purposes.

Finally, more of the same, but this time for the rr routers:

```yaml title="WAN1.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1.yml:62:78
--8<--
```

1. `mpls_route_reflectors` is used here to make the rr nodes peer with each other.

## Defining underlay connectivity between network nodes

A free-standing list of `core_interfaces` dictionaries and their associated profiles and IP pools defines the underlay connectivity between nodes.

```yaml title="WAN1.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/WAN1.yml:83:103
--8<--
```

1. First, an IP-pool for the underlay p2p links is defined.
2. The IP pool `name` is used to assign a name to the IP pool, this is later called in the profile to associate the pool to the profile.
3. The profile `name` is used to assign a name to the link profile, which is later called under the p2p link definitions to inherit settings from the profile.
4. Each list item in `p2p_links` is a dictionary that defines one routed point-to-point underlay link and its associated parameters.
5. `nodes` is used to identify which nodes are connecting.
6. `id` is used to extract a single /31 subnet for the link from the IP pool mentioned by the profile. Each link that shares an IP pool must have a unique ID to prevent overlapping IP addressing.
7. `profile` is used here to inherit common settings for the link from the profile.

## Specifying network services (VRFs and routed interfaces) and endpoint connectivity in the VPN-IPv4 fabric

```yaml title="NETWORK_SERVICES.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/NETWORK_SERVICES.yml
--8<--
```

All tenant VRFs and routed interfaces for endpoint connectivity in the network are defined here.

Two tenants called `CUSTOMER1` and `CUSTOMER2` are specified. Each of these tenants has a single VRF defined, and under those VRFs, we define the routed interfaces, tenant (PE-CE) routing protocols and address families in use:

```yaml title="NETWORK_SERVICES.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/group_vars/NETWORK_SERVICES.yml:7:29
--8<--
```

This defines `C1_VRF1`, with a VRF ID of `10`, enables OSPF routing for PE-CE connections inside the VRF on selected pe routers and defines routed interfaces that are used to connect to the CE devices/aggregation nodes. Each interface has an IP address assigned, a description, and has OSPF routing enabled.

The lists of interfaces, nodes, and ip_addresses used in the above definition of the l3 interface are read by the Ansible logic as follows: interface `Ethernet3.10` belongs to the node `pe1` and has the IP address of `10.0.1.1/29`. In other words, the list indices are used to form the basic parameters for one interface.

## The playbook

In this example, the deploy playbook looks like the following:

```yaml title="deploy.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/deploy.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the role `arista.avd.eos_designs`, which generates structured configuration for each device. This structured configuration can be found in the `ansible-avd-examples/isis-ldp-ipvpn/intended/structured_configs` folder.
3. This task uses the role `arista.avd.eos_cli_config_gen`, which generates the actual Arista EOS CLI configurations found in the `ansible-avd-examples/isis-ldp-ipvpn/intended/configs` folder, along with the device-specific and fabric wide documentation found in the `ansible-avd-examples/isis-ldp-ipvpn/documentation/` folder. In addition, it relies on the structured configuration generated by `arista.avd.eos_designs`.
4. This task uses the role `arista.avd.eos_config_deploy_eapi` that pushes the generated configuration to the devices in scope.

### Testing AVD output without a lab

Example of using the build playbook without devices (local tasks):

```yaml title="build.yml"
--8<--
ansible_collections/arista/avd/examples/isis-ldp-ipvpn/build.yml
--8<--
```

The build playbook will generate all of the output (variables, configurations, documentation) but will not attempt to communicate with any devices.

Please look through the folders and files described above to learn more about the output generated by AVD.

### Executing the playbook

The execution of the playbook should produce the following output:

```shell
user@ubuntu:~/isis-ldp-ipvpn$ ansible-playbook deploy.yml

PLAY [Run AVD] *****************************************************************************************************************************************************************************

TASK [arista.avd.eos_designs : Collection arista.avd version 3.5.0 loaded from /home/user/.ansible/collections/ansible_collections] ******************************************************
ok: [p1]

TASK [arista.avd.eos_designs : Create required output directories if not present] **********************************************************************************************************
ok: [p1 -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/isis-ldp-ipvpn/intended/structured_configs)
ok: [p1 -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/isis-ldp-ipvpn/documentation/fabric)
(...)
```

If similar output is not shown, make sure:

1. The documented [requirements](../../../../../docs/installation/collection-installation.md) are met.
2. The latest `arista.avd` collection is installed.

## Troubleshooting

### VPN-IPv4 Overlay not working

If after doing the following steps:

1. Manually copy/paste the switch-basic-configuration to the devices.
2. Run the playbook and push the generated configuration to the fabric.
3. Login to a pe or rr device, for example, pe1 and run the command `show bgp vpn-ipv4 summary` to view VPN routes.

The following error message is shown:

```eos
pe1#show bgp vpn-ipv4 summary
% Not supported
pe1#
```

This is caused by AVD pushing the configuration line `service routing protocols model multi-agent`, which enables the multi-agent routing process supporting VPN-IPv4 and EVPN. This change *requires* a reboot of the device.

### VPN-IPv4 Overlay in Arista Cloud Test (ACT)

Suppose you are running this lab in the Arista Cloud Test service, and the overlay services are not working (no connectivity from CPE to CPE) after performing the above mentioned steps. In that case, you may need to change the default forwarding engine of the vEOS nodes.

Add the following line to the starting configurations for each node:

```eos
platform tfa personality arfa
```

Currently, this command **must** be manually entered into the device configurations **before** trying to push the command with AVD. After you have entered it manually on each node, add the following YAML to group_vars/WAN1.yml and run the deployment playbook:

```yaml
eos_cli: |
  platform tfa personality arfa
```

Retest the services. They should now work, provided the CPEs and aggregation node are correctly configured.
