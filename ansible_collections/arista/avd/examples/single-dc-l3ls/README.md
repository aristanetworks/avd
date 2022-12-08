# AVD example for a single data center using L3LS

## Introduction

This example is meant to be used as the logical second step in introducing AVD to new users, directly following the [Introduction to Ansible and AVD](../../docs/getting-started/intro-to-ansible-and-avd.md) section. The idea is that new users with access to virtual switches (using Arista vEOS-lab or cEOS) can learn how to generate configuration and documentation for a complete fabric environment. Users with access to physical switches will have to adapt a few settings. This is all documented inline in the comments included in the YAML files. If a lab with virtual or physical switches is not accessible, this example can also be used to only generate the output from AVD if required.

The example includes and describes all the AVD files and their content used to build an L3LS EVPN/VXLAN Symmetric IRB network covering a single DC, using the following:

- Two (virtual) spine switches.
- Two sets of (virtual) leaf switches, serving endpoints such as servers.
- Two (virtual) layer2-only switches often used for management connectivity to the servers.

Integration with CloudVision is not included in this example to keep everything as simple as possible. In this case, the Ansible host will communicate directly with the switches using eAPI.

## Installation

Requirements to use this example:

- Follow the installation guide for AVD found [here](../../docs/installation/collection-installation.md).
- Run the following playbook to copy the examples to your current working directory, for example `ansible-avd-examples`:

`ansible-playbook arista.avd.install_examples`

This will show the following:

```shell
 ~/ansible-avd-examples# ansible-playbook arista.avd.install_examples

PLAY [Install Examples]***************************************************************************************************************************************************************************************************************************************************************

TASK [Copy all examples to ~/ansible-avd-examples]*****************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP
****************************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

After the playbook has run successfully, the directory structure will look as shown below, the contents of which will be covered in later sections:

```shell
ansible-avd-examples/ (or wherever the playbook was run)
  |── single-dc-l3ls
    ├── ansible.cfg
    ├── documentation
    ├── group_vars
    ├── images
    ├── intended
    ├── inventory.yml
    ├── playbook.yml
    ├── README.md
    └── switch-basic-configurations
```

!!! info
    If the content of any file is ***modified*** and the playbook is rerun, the file ***will not*** be overwritten. However, if any file in the example is ***deleted*** and the playbook is rerun, Ansible will re-create the file.

## Overall design overview

### Physical topology

The drawing below shows the physical topology used in this example. The interface assignment shown here are referenced across the entire example, so keep that in mind if this example must be adapted to a different topology. Finally, the Ansible host is connected to the dedicated out-of-band management port (Ethernet0 when using vEOS-lab):

![Figure: Arista Leaf Spine physical topology](images/avd-single-dc-l3ls-example.svg)

### IP ranges used

| Out-of-band management IP allocation for DC1        | 172.16.1.0/24               |
|-----------------------------------------------------|-----------------------------|
| Default gateway                                     | 172.16.1.1                  |
| dc1-spine1                                          | 172.16.1.11                 |
| dc1-spine2                                          | 172.16.1.12                 |
| dc1-leaf1a                                          | 172.16.1.101                |
| dc1-leaf1b                                          | 172.16.1.102                |
| dc1-leaf2a                                          | 172.16.1.103                |
| dc1-leaf2b                                          | 172.16.1.104                |
| dc1-leaf1c                                          | 172.16.1.151                |
| dc1-leaf2c                                          | 172.16.1.152                |
| **Point-to-point links between leaf and spine**     | **(Underlay)**              |
| DC1                                                 | 10.255.255.0/26             |
| **Loopback0 interfaces used for EVPN peering**      | 10.255.0.0/27               |
| **Loopback1 interfaces used for VTEP**              | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.0/27               |
| **VTEP Loopbacks used for diagnostics**             | **(Leaf switches)**         |
| VRF10                                               | 10.255.10.0/27              |
| VRF11                                               | 10.255.11.0/27              |
| **SVIs (interface vlan...)**                        | **10.10.`<VLAN-ID>`.0/24**  |
| For example `interface VLAN11` has the IP address:  | 10.10.11.1                  |
| **MLAG Peer-link (interface vlan 4094)**            | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.64/27              |
| **MLAG iBGP Peering (interface vlan 4093)**         | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.96/27              |

### BGP design

=== "Underlay"

    ![Figure: Arista Underlay BGP Design](images/bgp-underlay.svg)

=== "Overlay"

    ![Figure: Arista Underlay BGP Design](images/bgp-overlay.svg)

### Basic EOS config

Basic connectivity between the Ansible host and the switches must be established before Ansible can be used to push configurations. You must configure the following on all switches:

- A hostname configured purely for ease of understanding.
- An IP enabled interface - in this example the dedicated out-of-band management interface is used.
- A username and password with the proper access privileges.

Below is the basic configuration file for `dc1-leaf1a`:

```eos title="dc1-leaf1a-basic-configuration.txt"
--8<--
examples/single-dc-l3ls/switch-basic-configurations/dc1-leaf1a-basic-configuration.txt
--8<--
```

!!! note
    The folder `single-dc-l3ls/switch-basic-configurations/` contains a file per device for the initial configurations.

## Ansible inventory, group vars and naming scheme

The following drawing shows a graphic overview of the Ansible inventory, group variables, and naming scheme used in this example:

![Figure: Ansible inventory and vars](images/ansible-groups.svg)

!!! note
    The two servers `dc1-leaf1-server1` and `dc1-leaf2-server1` at the bottom are **not** configured by AVD, but the switch ports used to connect to the servers are.

Group names use uppercase and underscore syntax:

- FABRIC
- DC1
- DC1_SPINES
- DC1_L3_LEAVES
- DC1_L2_LEAVES

All hostnames use lowercase and dashes, for example:

- dc1-spine1
- dc1-leaf1a
- dc1-leaf2c

The drawing also shows the relationships between groups and their children:

- For example, `dc1-spine1` and `dc1-spine2` are both children of the group called `DC1_SPINES`.

Additionally, groups themselves can be children of another group, for example:

- `DC1_L3_LEAVES` is a group consisting of the groups `DC1_LEAF1` and `DC1_LEAF2`
- `DC1_L3_LEAVES` is also a child of the group `DC1`.

This naming convention makes it possible to extend anything easily, but as always, this can be changed based on your preferences. Just ensure that the names of all groups and hosts are unique.

### Content of the inventory.yml file

This section describes the entire `ansible-avd-examples/single-dc-l3ls/inventory.yml` file used to represent the above topology.

It is important that the hostnames specified in the inventory exist either in DNS or in the hosts file on your Ansible host to allow successful name lookup and be able to reach the switches directly. A successful ping from the Ansible host to each inventory host verifies name resolution(e.g., `ping dc1-spine1`).

Alternatively, if there is no DNS available, or if devices need to be reached using a fully qualified domain name (FQDN), define `ansible_host` to be an IP address or FQDN for each device - see below for an example:

```yaml title="inventory.yml"
---
all:
  children:
    FABRIC:
      children:
        DC1:
          children:
            DC1_SPINES:
              hosts:
                dc1-spine1:
                  ansible_host: 172.16.1.11
                dc1-spine2:
                  ansible_host: 172.16.1.12
            DC1_L3_LEAVES:
              hosts:
                dc1-leaf1a:
                  ansible_host: 172.16.1.101
                dc1-leaf1b:
                  ansible_host: 172.16.1.102
                dc1-leaf2a:
                  ansible_host: 172.16.1.103
                dc1-leaf2b:
                  ansible_host: 172.16.1.104
            DC1_L2_LEAVES:
              hosts:
                dc1-leaf1c:
                  ansible_host: 172.16.1.151
                dc1-leaf2c:
                  ansible_host: 172.16.1.152

        NETWORK_SERVICES:
          children:
            DC1_L3_LEAVES:
            DC1_L2_LEAVES:
        CONNECTED_ENDPOINTS:
          children:
            DC1_L3_LEAVES:
            DC1_L2_LEAVES:
```

The above is what is included in this example, *purely* to make it as simple as possible to get started. However, in the future, please do not carry over this practice to a production environment, where an inventory file for an identical topology should look as follows when using DNS:

```yaml title="inventory.yml"
---
all:
  children:
    FABRIC:
      children:
        DC1:
          children:
            DC1_SPINES:
              hosts:
                dc1-spine1:
                dc1-spine2:
            DC1_L3_LEAVES:
              hosts:
                dc1-leaf1a:
                dc1-leaf1b:
                dc1-leaf2a:
                dc1-leaf2b:
            DC1_L2_LEAVES:
              hosts:
                dc1-leaf1c:
                dc1-leaf2c:

        NETWORK_SERVICES: # (1)!
          children:
            DC1_L3_LEAVES:
            DC1_L2_LEAVES:
        CONNECTED_ENDPOINTS: # (2)!
          children:
            DC1_L3_LEAVES:
            DC1_L2_LEAVES:
```

1. `NETWORK_SERVICES`

    - Creates a group named `NETWORK_SERVICES`. Ansible variable resolution resolves this group name to the identically named group_vars file (`ansible-avd-examples/single-dc-l3ls/group_vars/NETWORK_SERVICES.yml`).

    - The file's contents, which in this case are specifications of VRFs and VLANs, are then applied to the group's children. In this case, the two groups `DC1_L3_LEAVES` and `DC1_L2_LEAVES`.

2. `CONNECTED_ENDPOINTS`

    - Creates a group named `CONNECTED_ENDPOINTS`. Ansible variable resolution resolves this group name to the identically named group_vars file (`ansible-avd-examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS.yml`).

    - The file's contents, which in this case are specifications of connected endpoints (typically servers), are then applied to the children of the group, in this case, the two groups `DC1_L3_LEAVES` and `DC1_L2_LEAVES`.

## Defining device types

Since this example covers building an L3LS network, AVD must know about the device types, for example, spines, L3 leaves, L2 leaves, etc. The devices are already grouped in the inventory, so the device types are specified in the group variable files with the following names and content:

=== "DC1_SPINES.yml"

    ```yaml
    --8<--
    examples/single-dc-l3ls/group_vars/DC1_SPINES.yml
    --8<--
    ```

=== "DC1_L3_LEAVES.yml"

    ```yaml
    --8<--
    examples/single-dc-l3ls/group_vars/DC1_L3_LEAVES.yml
    --8<--
    ```

=== "DC1_L2_LEAVES.yml"

    ```yaml
    --8<--
    examples/single-dc-l3ls/group_vars/DC1_L2_LEAVES.yml
    --8<--
    ```

For example, all switches that are children of the DC1_SPINES group defined in the inventory will be of type `spine`.

## Setting fabric-wide configuration parameters

The `ansible-avd-examples/single-dc-l3ls/group_vars/FABRIC.yml` file defines generic settings that apply to all children of the `FABRIC` group as specified in the inventory described earlier.

The first section defines how the Ansible host connects to the devices:

```yaml title="FABRIC.yml"
ansible_connection: ansible.netcommon.httpapi # (1)!
ansible_network_os: arista.eos.eos # (2)!
ansible_user: ansible # (3)!
ansible_password: ansible
ansible_become: true
ansible_become_method: enable # (4)!
ansible_httpapi_use_ssl: true # (5)!
ansible_httpapi_validate_certs: false # (6)!
```

1. The Ansible host must use eAPI
2. Network OS which in this case is Arista EOS
3. The username/password combo
4. How to escalate privileges to get write access
5. Use SSL
6. Do not validate SSL certificates

The following section specifies variables that generate configuration to be applied to all devices in the fabric:

```yaml title="FABRIC.yml"
fabric_name: FABRIC # (1)!

underlay_routing_protocol: EBGP
overlay_routing_protocol: EBGP

local_users: # (2)!
  ansible:
    privilege: 15
    role: network-admin
    sha512_password: $6$7u4j1rkb3VELgcZE$EJt2Qff8kd/TapRoci0XaIZsL4tFzgq1YZBLD9c6f/knXzvcYY0NcMKndZeCv0T268knGKhOEwZAxqKjlMm920
  admin:
    privilege: 15
    role: network-admin
    no_password: true

bgp_peer_groups: # (3)!
  evpn_overlay_peers:
    password: Q4fqtbqcZ7oQuKfuWtNGRQ==
  ipv4_underlay_peers:
    password: 7x4B4rnJhZB438m9+BrBfQ==
  mlag_ipv4_underlay_peer:
    password: 4b21pAdCvWeAqpcKDFMdWw==

p2p_uplinks_mtu: 1500 # (4)!
```

1. The name of the fabric for internal AVD use. This name *must* match the name of an Ansible Group (and therefore a corresponding group_vars file) covering all network devices.
2. Local users/passwords and their privilege levels. In this case, the `ansible` user is set with the password `ansible` and an `admin` user is set with no password.
3. BGP peer groups and their passwords (all passwords are "arista").
4. Point-to-point interface MTU, in this case, is set to 1500 since the example uses vEOS, but when using hardware, this should be set to 9214 instead.

## Setting device specific configuration parameters

The `ansible-avd-examples/single-dc-l3ls/group_vars/DC1.yml` file defines settings that apply to all children of the `DC1` group as specified in the inventory described earlier. However, this time the settings defined are no longer fabric-wide but are limited to DC1. In this example, this is of limited benefit with only a single data center. Still, it allows us to scale the configuration to a scenario with multiple data centers in the future.

```yaml title="DC1.yml"
---
mgmt_gateway: 172.16.1.1 # (1)!

spine:
  defaults:
    platform: vEOS-lab # (2)!
    loopback_ipv4_pool: 10.255.0.0/27 # (3)!
    bgp_as: 65100 # (4)!
    bgp_defaults: # (5)!
      - no bgp default ipv4-unicast
      - distance bgp 20 200 200
      - graceful-restart restart-time 300
      - graceful-restart

  nodes: # (6)!
    dc1-spine1:
      id: 1 # (7)!
      mgmt_ip: 172.16.1.11/24 # (8)!

    dc1-spine2:
      id: 2
      mgmt_ip: 172.16.1.12/24
```

1. The default gateway for the management interface of all devices in DC1 is defined.
2. `platform` references default settings defined in AVD specific to certain switch platforms.
3. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0.
4. `bgp_as` defines the BGP AS number.
5. `bgp_defaults` defines generic BGP settings.
6. `nodes` defines the actual spine switches, using the hostnames defined in the inventory.
7. `id` is used to calculate the various IP addresses, for example, the IPv4 address for the Loopback0 interface. In this case, dc1-spine1 will get the IPv4 address 10.255.0.1/27 assigned to the Loopback0 interface.
8. `mgmt_ip` defines the IPv4 address of the management interface. As stated earlier, Ansible will perform name lookups using the hostnames specified in the inventory unless using the `ansible_host` option. However, there is no automatic mechanism to grab the result of the name lookup and use that to generate the management interface configuration.

The following section covers the L3 leaf switches. Significantly more settings need to be set compared to the spine switches:

```yaml title="DC1.yml"
l3leaf:
  defaults:
    platform: vEOS-lab # (1)!
    loopback_ipv4_pool: 10.255.0.0/27 # (2)!
    loopback_ipv4_offset: 2 # (3)!
    vtep_loopback_ipv4_pool: 10.255.1.0/27 # (4)!
    uplink_interfaces: ['Ethernet1', 'Ethernet2'] # (5)!
    uplink_switches: ['dc1-spine1', 'dc1-spine2'] # (6)!
    uplink_ipv4_pool: 10.255.255.0/26 # (7)!
    mlag_interfaces: ['Ethernet3', 'Ethernet4'] # (8)!
    mlag_peer_ipv4_pool: 10.255.1.64/27 # (9)!
    mlag_peer_l3_ipv4_pool: 10.255.1.96/27 # (10)!
    bgp_defaults:
      - no bgp default ipv4-unicast
      - distance bgp 20 200 200
      - graceful-restart restart-time 300
      - graceful-restart
    virtual_router_mac_address: 00:1c:73:00:00:99 # (11)!
    spanning_tree_priority: 4096 # (12)!
    spanning_tree_mode: mstp # (13)!

  node_groups: # (14)!
    DC1_L3_LEAF1:
      bgp_as: 65101 # (15)!
      nodes:
        dc1-leaf1a:
          id: 1
          mgmt_ip: 172.16.1.101/24
          uplink_switch_interfaces: # (16)!
            - Ethernet1
            - Ethernet1
        dc1-leaf1b:
          id: 2
          mgmt_ip: 172.16.1.102/24
          uplink_switch_interfaces:
            - Ethernet2
            - Ethernet2

    DC1_L3_LEAF2:
      bgp_as: 65102
      nodes:
        dc1-leaf2a:
          id: 3
          mgmt_ip: 172.16.1.103/24
          uplink_switch_interfaces:
            - Ethernet3
            - Ethernet3
        dc1-leaf2b:
          id: 4
          mgmt_ip: 172.16.1.104/24
          uplink_switch_interfaces:
            - Ethernet4
            - Ethernet4
```

1. `platform` references default settings defined in AVD specific to certain switch platforms.
2. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0. Please note that this IP pool is identical to the one used for the spine switches in this example. To avoid setting the same IP addresses for several devices, we define the option `loopback_ipv4_offset`.
3. `loopback_ipv4_offset` offsets all assigned loopback IP addresses counting from the beginning of the IP scope. This is required when the same IP pool is used for two different node_types (like spine and l3leaf in this example) to avoid overlapping IPs. The offset is "2" in this case because each spine switch uses one loopback address.
4. `vtep_loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the VTEP (Loopback1).
5. `uplink_interfaces` defines the interfaces used locally on the leaf switches.
6. `uplink_switches` defines the uplink switches, which are dc1-spine1 and dc1-spine2. Note that the `uplink_interfaces` and `uplink_switches` are paired vertically.
7. `uplink_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the uplink interfaces that were just defined.
8. `mlag_interfaces` defines the MLAG interfaces used on each leaf switch, in this case, Ethernet3 and Ethernet4. These two interfaces will form PortChannel3 used for the MLAG peer link. Note that PortChannel3 is selected since the first interface is Ethernet3.
9. `mlag_peer_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the MLAG peer link interface VLAN4094.
10. `mlag_peer_l3_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the iBGP peering established between the two leaf switches via the SVI/IRB interface VLAN4093.
11. `virtual_router_mac_address` defines the MAC address used for the anycast gateway on the various subnets. This is the MAC address connected endpoints will learn when ARPing for their default gateway.
12. `spanning_tree_priority` sets the spanning tree priority. Since spanning tree in an L3LS network is effectively only running locally on the switch, the same priority across all L3 leaf switches can be re-used.
13. `spanning_tree_mode` defines the spanning tree mode. In this case, we are using MSTP, which is the default. However, other modes are supported should they be required, for example, for connectivity to legacy or third-party vendor environments.
14. `node_groups` defines settings common to more than one node. For example, for leaf switches, when exactly two nodes are part of a node group, AVD will, by default, automatically generate MLAG configuration.
15. `bgp_as` is defined once since an MLAG pair shares a single BGP AS number.
16. `uplink_switch_interfaces` defines the interfaces used on the uplink switches (Ethernet1 on dc1-spine1 and dc1-spine2 in this example). Defining which spine interfaces the leaf is connected to under the leaf switch settings makes adding and removing leaf switches much easier. There is no need to add/remove any settings under the spine switch section; AVD takes care of that for you. This child device/parent device hierarchy also applies to L2 and L3 leaves.

Finally, more of the same, but this time for the L2 leaf switches:

```yaml title="DC1.yml"
l2leaf:
  defaults:
    platform: vEOS-lab
    uplink_interfaces: ['Ethernet1', 'Ethernet2']
    spanning_tree_mode: mstp

  node_groups:
    DC1_L2_LEAF1:
      uplink_switches: ['dc1-leaf1a', 'dc1-leaf1b']
      nodes:
        dc1-leaf1c:
          id: 1
          mgmt_ip: 172.16.1.151/24
          uplink_switch_interfaces:
            - Ethernet8
            - Ethernet8

    DC1_L2_LEAF2:
      uplink_switches: ['dc1-leaf2a', 'dc1-leaf2b']
      nodes:
        dc1-leaf2c:
          id: 2
          mgmt_ip: 172.16.1.152/24
          uplink_switch_interfaces:
            - Ethernet8
            - Ethernet8
```

As should be clear, an L2 leaf switch is much simpler than an L3 switch. Hence there are fewer settings to define.

## Specifying network services (VRFs and VLANs) in the EVPN/VXLAN fabric

```yaml title="NETWORK_SERVICES.yml"
--8<--
examples/single-dc-l3ls/group_vars/NETWORK_SERVICES.yml
--8<--
```

All VRF and VLANs are defined here. This means that regardless of where a given VRF or VLAN must exist, its existence is defined in this file, but it does not indicate ***where*** in the fabric it exists. That was done at the bottom of the inventory file previously described in the [Inventory](#content-of-the-inventoryyml-file) section.

AVD offers granular control of where Tenants and VLANs are configured using `tags` and `filter`. Those areas are not covered in this basic example.

A single tenant called `TENANT1` is specified. The first setting is the base number (`10000`) used to generate the L2VNI numbers automatically, `L2VNI = base number + VLAN-id`. For example, L2VNI for VLAN11 = 10000 + 11 = 10011.

Next, two VRFs are defined, each with two VLANs. For example:

```yaml title="NETWORK_SERVICES.yml"
      VRF10:
        vrf_vni: 10
        vtep_diagnostic:
          loopback: 10
          loopback_ip_range: 10.255.10.0/27
        svis:
          "11":
            name: VRF10_VLAN11
            enabled: true
            ip_address_virtual: 10.10.11.1/24
          "12":
            name: VRF10_VLAN12
            enabled: true
            ip_address_virtual: 10.10.12.1/24
```

This defines `VRF10`, with an L3VNI of `10` and two VLANs (`VLAN11` and `VLAN12`). Each VLAN has a name and a virtual IP address, which will be used as the default gateway for that particular VLAN on all leaf switches where the VLAN is created.

The following configuration is also defined under `VRF10`:

```yaml title="NETWORK_SERVICES.yml"
        vtep_diagnostic:
          loopback: 10
          loopback_ip_range: 10.255.10.0/27
```

This enables more user-friendly diagnostics for troubleshooting purposes by defining a specific loopback per VRF. This will create the following Arista EOS config. For example, on dc1-leaf1a:

```eos
interface Loopback10
   description VRF10_VTEP_DIAGNOSTICS
   no shutdown
   vrf VRF10
   ip address 10.255.10.3/32
!
ip address virtual source-nat vrf VRF10 address 10.255.10.3
```

At the bottom of the `NETWORK_SERVICES.yml` file, two layer2-only VLANs (`VLAN3401` and `VLAN3402`) are defined. These VLANs are only bridged across the fabric but never routed anywhere:

```yaml title="NETWORK_SERVICES.yml"
    l2vlans:
      "3401":
        name: L2_VLAN3401
      "3402":
        name: L2_VLAN3402
```

## Specifying endpoint connectivity in the EVPN/VXLAN fabric

After the previous section, all VRFs and VLANs across the fabric are now defined. The `ansible-avd-examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS.yml` file specifies the connectivity for all endpoints in the fabric (typically servers):

```yaml title="CONNECTED_ENDPOINTS.yml"
--8<--
examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS.yml
--8<--
```

This defines the settings for the relevant switch ports to which the endpoints connect, in this case the two servers `dc1-leaf1-server1` and `dc1-leaf2-server1`.

As an example, here is the configuration for `dc1-leaf1-server1`:

```yaml title="CONNECTED_ENDPOINTS.yml"
  dc1-leaf1-server1:
    adapters: # (1)!
    - type: server
      server_ports: [ PCI1, PCI2 ] # (2)!
      switch_ports: [ Ethernet5, Ethernet5 ] # (3)!
      switches: [ dc1-leaf1a, dc1-leaf1b ] # (4)!
      vlans: 11-12,21-22 # (5)!
      native_vlan: 4092 # (6)!
      mode: trunk # (7)!
      spanning_tree_portfast: edge # (8)!
      port_channel: # (9)!
        description: PortChannel dc1-leaf1-server1
        mode: active

    - type: ilo
      server_ports: [ iLO ]
      switch_ports: [ Ethernet5 ]
      switches: [ dc1-leaf1c ]
      vlans: 11
      mode: access
      spanning_tree_portfast: edge
```

1. The relevant `adapters` are defined. The `type` set to `server` and `ilo` is purely for documentation and readability purposes. It has no operational significance.
2. `server_ports` are defined for use in the interface descriptions on the switch. This does not configure anything on the server.
3. `switch_ports` defines the interfaces used in the switches. In this example the server is dual-connected to Ethernet5 and Ethernet5. These two ports exist on switch dc1-leaf1a and dc1-leaf1b defined in the following line.
4. `switches` defines the switches used, in this case dc1-leaf1a and dc1-leaf1b. Note that the `server_ports`, `switch_ports` and `switches` definitions are paired vertically.
5. `vlans` defines which VLANs are allowed on the switch_ports, in this case it is two ranges, VLAN11-12 and VLAN21-22 for the dual-attached server ports and VLAN11 for the iLO port.
6. `native_vlan` specifies the native VLAN when the switch port mode is set to trunk.
7. `mode` is set to trunk for the dual-attached server ports and access for the iLO port.
8. `spanning_tree_portfast` defines whether the switch port should be a spanning tree edge port or a network port.
9. `port-channel` defines the description and mode for the port-channel.

## The playbook

In this example, the playbook looks like the following:

```yaml title="playbook.yml"
--8<--
examples/single-dc-l3ls/playbook.yml
--8<--
```

1. At the highest level, the name and scope of the playbook is set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the role `arista.avd.eos_designs`, which generates structured configuration for each device. This structured configuration can be found in the `ansible-avd-examples/single-dc-l3ls/intended/structured_configs` folder.
3. This task uses the role `arista.avd.eos_cli_config_gen`, which generates the actual Arista EOS CLI configurations found in the `ansible-avd-examples/single-dc-l3ls/intended/configs` folder, along with the device-specific and fabric wide documentation found in the `ansible-avd-examples/single-dc-l3ls/documentation/` folder. It relies on the structured configuration generated by `arista.avd.eos_designs`.
4. This task uses the role `arista.avd.eos_config_deploy_eapi` that pushes the generated configuration to the devices in scope.

### Testing AVD output without a lab

Example of using this playbook without devices (local tasks):

```yaml title="playbook.yml"
- name: Run AVD
  hosts: FABRIC
  gather_facts: false
  tasks:
    - name: generate intended variables
      import_role:
        name: arista.avd.eos_designs
    - name: generate device intended config and documentation
      import_role:
        name: arista.avd.eos_cli_config_gen
    # - name: deploy configuration to device
    #   import_role:
    #      name: arista.avd.eos_config_deploy_eapi
```

By simply commenting out (or deleting) the last task definition, the playbook will generate all of the output (variables, configurations, documentation), but will not attempt to communicate with any devices.

Please look through the folders and files described above to learn more about the output generated by AVD.

### Executing the playbook

The execution of the playbook should produce the following output:

```shell
user@ubuntu:~/Documents/git_projects/ansible-avd-examples/single-dc-l3ls$ ansible-playbook playbook.yml

PLAY [Run AVD] *****************************************************************************************************************************************************************************

TASK [arista.avd.eos_designs : Collection arista.avd version 3.5.0 loaded from /home/user/.ansible/collections/ansible_collections] ******************************************************
ok: [dc1-leaf1a]

TASK [arista.avd.eos_designs : Create required output directories if not present] **********************************************************************************************************
ok: [dc1-leaf1a -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/single-dc-l3ls/intended/structured_configs)
ok: [dc1-leaf1a -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/single-dc-l3ls/documentation/fabric)
(...)
```

If similar output is not shown, make sure:

1. The documented [requirements](../../docs/installation/collection-installation.md) are met.
2. The latest `arista.avd` collection is installed.

## Troubleshooting

### EVPN not working

If after doing the following steps:

1. Manually copy/paste the switch-basic-configuration to the devices.
2. Run the playbook and push the generated configuration to the fabric.
3. Login to a leaf device, for example, dc1-leaf1a and run the command `show bgp evpn summary` to view EVPN routes.

The following error message is shown:

```eos
dc1-leaf1a#show bgp evpn summ
% Not supported
dc1-leaf1a#
```

This is caused by AVD pushing the configuration line `service routing protocols model multi-agent`, which enables the multi-agent routing process supporting EVPN. This change *requires* a reboot of the device.
