---
# This title is used for search results
title: AVD example for a single data center using multiple pods for l3ls
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD example for a single data center with multipod using L3LS

## Introduction

This example shows how to create a multipod environment (also known as a 5-stage Clos) in a DC environment. This can be used in multiple DCs of course, but this example is only for two pods in a single DC. 

Also included is an external router for an external routed connection for VRF_A. 

This example will not teach all the aspects of a l3ls EVPN/VXLAN build, see the single-dc-l3ls directory for that. This is a supplement to this, concentrating on the differences between a typical DC l3ls and one with multiple pods/5-stage Clos.  

Ansible playbooks are included to show the following:

- Building the intended configuration and documentation
- Deploying the configuration via CloudVision to the switches, including a full change-based workflow with rollback capability etc.
- Validating the configuration 


## Overall design overview

### Physical topology

The drawing below shows the physical topology used in this example. The interface assignment shown here are referenced across the entire example, so keep that in mind if this example must be adapted to a different topology. 

![Figure: Arista Leaf Spine physical topology](images/l3ls-multipod.png)


### Fabric Design

The fabric is a basic l3ls EVPN/VXLAN design with a multi-pod (5-stage Clos) architecture. Of course four leafs and four spines wouldn't be put into multi-pod, this is just a demonstration of how it is configured. 

## Ansible inventory, group vars, and naming scheme

The following drawing shows a graphic overview of the Ansible inventory, group variables, and naming scheme used in this example:

![Figure: Arista Leaf Spine physical topology](images/inventory.png)

There is the addition of a SUPERSPINES group as well as a POD1 and POD2 groups with PODX_LEAFS and PODX_SPINES under each. The EVPN_SERVICES and ENDPOINT_CONNECT allow separation of YAML files, and putting the PODX_LEAFS under them will build the appropriate configs for those devices (VXLAN/VLAN/anycast gateways do not get instantiated on spines, of course).



### Content of the inventory.yml file

```yaml title="inventory.yml"
---
all:
  children:
    CVP_cluster:
      vars:
        ansible_user: arista
        ansible_password: arista123
        ansible_connection: httpapi
        ansible_httpapi_use_ssl: True
        ansible_httpapi_validate_certs: False
        ansible_network_os: eos
        ansible_httpapi_port: 443
      hosts: 
        cvp1: 
          ansible_host: 192.168.0.5
        cvp2: 
          ansible_host: 192.168.0.6
        cvp3: 
          ansible_host: 192.168.0.7

    FABRIC:
      vars:
        ansible_user: arista
        ansible_ssh_pass: arista123 # If using SSH keys with CLI, this can be removed
# Use this section if you want to perform testing via the eAPI
        ansible_connection: httpapi
        ansible_httpapi_use_ssl: True
        ansible_httpapi_validate_certs: False
        ansible_network_os: eos
        ansible_httpapi_port: 443
# Use this section if you want to perform testing via the CLI through SSH
        # ansible_connection: network_cli
        # ansible_network_os: eos
        # ansible_become: yes
        # ansible_become_method: enable
      children:
        SUPERSPINES:
          vars:
            type: super-spine
          hosts:  
            borderleaf1:
              ansible_host: 192.168.0.15
            borderleaf2:
              ansible_host: 192.168.0.16
        POD1:
          children:
            POD1_SPINES:
              vars:
                type: spine
              hosts:
                spine1:
                  ansible_host: 192.168.0.11
                spine2:
                  ansible_host: 192.168.0.12
            POD1_LEAFS:
              vars: 
                type: l3leaf
              hosts:
                leaf1:
                  ansible_host: 192.168.0.21
                leaf2:
                  ansible_host: 192.168.0.22
        POD2:
          children:
            POD2_SPINES:
              vars:
                type: spine
              hosts:
                spine3:
                  ansible_host: 192.168.0.13
                spine4:
                  ansible_host: 192.168.0.14
            POD2_LEAFS:
              vars:
                type: l3leaf
              hosts:
                leaf3:
                  ansible_host: 192.168.0.23
                leaf4:
                  ansible_host: 192.168.0.24
    EVPN_SERVICES:
      children:
        POD1_LEAFS:
        POD2_LEAFS:
    ENDPOINT_CONNECT:
      children:
        POD1_LEAFS:
        POD2_LEAFS:
```

## FABRIC Files

With the topology, five YAML files are used: 

* FABRIC.yml
* POD1.yml
* POD2.yml
* EVPN_SERVICES.yml
* ENDPOINT_CONNECT.yml



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

# Spine Switches
spine:
  defaults:
    platform: cEOS
    bgp_as: 65001
    loopback_ipv4_pool: 192.168.101.0/24
    mlag: false
    uplink_switches: [superspine1, superspine2] # Where the leaf uplinks go
    uplink_ipv4_pool: 192.168.103.0/24 # For the p2p interfaces to chopped up into /31s
    uplink_interfaces: [Ethernet7, Ethernet8] # Spine uplinks
  nodes:
    spine1:
      id: 11
      mgmt_ip: 192.168.0.11/24
      uplink_switch_interfaces: [Ethernet3, Ethernet3]
      evpn_route_servers: [superspine1, superspine2]
    spine2:
      id: 12
      mgmt_ip: 192.168.0.12/24
      uplink_switch_interfaces: [Ethernet4, Ethernet4]
      evpn_route_servers: [superspine1, superspine2]



# Leaf switches. Most leafs will be l3leaf, not l2leaf.
l3leaf:
  defaults:
    bgp_as: 65100-65199 # Gives a range which will be auto-assigned
    platform: cEOS
    loopback_ipv4_pool: 192.168.101.0/24 # This is loopback0 (underlay)
    vtep_loopback_ipv4_pool: 192.168.102.0/24 # This is loopback1 (VTEP)
    uplink_interfaces: [Ethernet3, Ethernet4] # Leaf uplinks
    uplink_switches: [spine1, spine2] # Where the leaf uplinks go
    uplink_ipv4_pool: 192.168.103.0/24 # For the p2p interfaces to chopped up into /31s
    mlag_interfaces: [Ethernet1, Ethernet2] # MLAG peer link
    mlag_peer_ipv4_pool: 10.255.252.0/24 # MLAG peer IPs
    mlag_peer_l3_ipv4_pool: 10.255.251.0/24 # iBGP peering between MLAG peers
    virtual_router_mac_address: 00:1c:73:00:00:99 # The vMAC for the anycast gateways
    bgp_defaults:
      - 'no bgp default ipv4-unicast'
      - 'distance bgp 20 200 200'
      - 'graceful-restart restart-time 300'
      - 'graceful-restart'
    spanning_tree_mode: mstp # Spanning Tree is still enabled even in EVPN setups
    spanning_tree_priority: 16384 
    mlag: true # By default, use MLAG

  node_groups:
    mlag1:
      nodes:
        leaf1:
          id: 1
          mgmt_ip: 192.168.0.21/24
          uplink_switch_interfaces: [Ethernet3, Ethernet3]
        leaf2:
          id: 2
          mgmt_ip: 192.168.0.22/24
          uplink_switch_interfaces: [Ethernet4, Ethernet4]
```


## Connecting an External Router

In addition to multi-pod, this AVD set also has an example of connecting to an external network. This is defined in the EVPN_SERVICES.yml file. The `l3_interfaces` parameter creates an L3 interface in the VRF on a specific leaf, and the `bgp_peer` section. 

```YAML
---
tenants:
  - name: ACME
    mac_vrf_vni_base: 10000
    vrfs:
      - name: VRF_A
        vrf_vni: 10
        svis:
          - id: 10
            # SVI Description
            name: DMZ
            enabled: true
            ip_address_virtual: 10.1.10.1/24
          - id: 20
            name: Internal
            enabled: true
            ip_address_virtual: 10.1.20.1/24
        l3_interfaces:
          - interfaces: [Ethernet9]
            ip_addresses: [10.1.5.0/31]
            nodes: [leaf4]
            enabled: True 
        bgp_peers:
          - ip_address: 10.1.5.1
            remote_as: 65534
            nodes: [leaf4]
```

Connecting to an 

```yaml title="DC1.yml"
---
mgmt_gateway: 192.168.0.1 # (1)!

spine:
  defaults:
    platform: vEOS-lab # (2)!
    loopback_ipv4_pool: 10.255.0.0/27 # (3)!
    bgp_as: 65100 # (4)!

  nodes: # (5)!
    - name: dc1-spine1
      id: 1 # (6)!
      mgmt_ip: 192.168.0.11/24 # (7)!

    - name: dc1-spine2
      id: 2
      mgmt_ip: 192.168.0.12/24
```

1. The default gateway for the management interface of all devices in DC1 is defined.
2. `platform` references default settings defined in AVD specific to certain switch platforms.
3. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0.
4. `bgp_as` defines the BGP AS number.
5. `nodes` defines the actual spine switches, using the hostnames defined in the inventory.
6. `id` is used to calculate the various IP addresses, for example, the IPv4 address for the Loopback0 interface. In this case, dc1-spine1 will get the IPv4 address 10.255.0.1/27 assigned to the Loopback0 interface.
7. `mgmt_ip` defines the IPv4 address of the management interface. As stated earlier, Ansible will perform name lookups using the hostnames specified in the inventory unless using the `ansible_host` option. However, there is no automatic mechanism to grab the result of the name lookup and use that to generate the management interface configuration.

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
    virtual_router_mac_address: 00:1c:73:00:00:99 # (11)!
    spanning_tree_priority: 4096 # (12)!
    spanning_tree_mode: mstp # (13)!

  node_groups: # (14)!
    - group: DC1_L3_LEAF1
      bgp_as: 65101 # (15)!
      nodes:
        - name: dc1-leaf1a
          id: 1
          mgmt_ip: 192.168.0.101/24
          uplink_switch_interfaces: # (16)!
            - Ethernet1
            - Ethernet1
        - name: dc1-leaf1b
          id: 2
          mgmt_ip: 192.168.0.102/24
          uplink_switch_interfaces:
            - Ethernet2
            - Ethernet2

    DC1_L3_LEAF2:
      bgp_as: 65102
      nodes:
        - name: dc1-leaf2a
          id: 3
          mgmt_ip: 192.168.0.103/24
          uplink_switch_interfaces:
            - Ethernet3
            - Ethernet3
        - name: dc1-leaf2b
          id: 4
          mgmt_ip: 192.168.0.104/24
          uplink_switch_interfaces:
            - Ethernet4
            - Ethernet4
```

1. `platform` references default settings defined in AVD specific to certain switch platforms.
2. `loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for Loopback0. Please note that this IP pool is identical to the one used for the spine switches in this example. To avoid setting the same IP addresses for several devices, we define the option `loopback_ipv4_offset`.
3. `loopback_ipv4_offset` offsets all assigned loopback IP addresses counting from the beginning of the IP scope. This is required to avoid overlapping IPs when the same IP pool is used for two different node_types (like spine and l3leaf in this example). The offset is "2" because each spine switch uses one loopback address.
4. `vtep_loopback_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the VTEP (Loopback1).
5. `uplink_interfaces` used by the `l3leaf` nodes to connect to the spine switches.
6. `uplink_switches` defines the uplink switches, which are dc1-spine1 and dc1-spine2. Note that the `uplink_interfaces` and `uplink_switches` are paired vertically.
7. `uplink_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the uplink interfaces that were just defined.
8. `mlag_interfaces` defines the MLAG interfaces used on each leaf switch.
9. `mlag_peer_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the MLAG peer link interface VLAN4094.
10. `mlag_peer_l3_ipv4_pool` defines the IP scope from which AVD assigns IPv4 addresses for the iBGP peering established between the two leaf switches via the SVI/IRB interface VLAN4093.
11. `virtual_router_mac_address` defines the MAC address used for the anycast gateway on the various subnets. This is the MAC address connected endpoints will learn when ARPing for their default gateway.
12. `spanning_tree_priority` sets the spanning tree priority. Since spanning tree in an L3LS network is effectively only running locally on the switch, the same priority across all L3 leaf switches can be re-used.
13. `spanning_tree_mode` defines the spanning tree mode. In this case, we are using MSTP, which is the default. However, other modes are supported should they be required, for example, for connectivity to legacy or third-party vendor environments.
14. `node_groups` defines settings common to more than one node. For example, when exactly two nodes are part of a node group for leaf switches, AVD will, by default, automatically generate MLAG configuration.
15. `bgp_as` is defined once since an MLAG pair shares a single BGP AS number.
16. `uplink_switch_interfaces` defines the interfaces used on the uplink switches (Ethernet1 on dc1-spine1 and dc1-spine2 in this example).

Finally, more of the same, but this time for the L2 leaf switches:

```yaml title="DC1.yml"
l2leaf:
  defaults:
    platform: vEOS-lab
    spanning_tree_mode: mstp

  node_groups:
    - group: DC1_L2_LEAF1
      uplink_switches: ['dc1-leaf1a', 'dc1-leaf1b']
      nodes:
        - name: dc1-leaf1c
          id: 1
          mgmt_ip: 192.168.0.151/24
          uplink_switch_interfaces:
            - Ethernet8
            - Ethernet8

    - group: DC1_L2_LEAF2
      uplink_switches: ['dc1-leaf2a', 'dc1-leaf2b']
      nodes:
        - name: dc1-leaf2c
          id: 2
          mgmt_ip: 192.168.0.152/24
          uplink_switch_interfaces:
            - Ethernet8
            - Ethernet8
```

An L2 leaf switch is more simple than an L3 switch. Hence there are fewer settings to define.

## Specifying network services (VRFs and VLANs) in the EVPN/VXLAN fabric

The `ansible-avd-examples/single-dc-l3ls/group_vars/NETWORK_SERVICES.yml` file defines All VRF and VLANs. This means that regardless of where a given VRF or VLAN must exist, its existence is defined in this file, but it does not indicate ***where*** in the fabric it exists. That was done at the bottom of the inventory file previously described in the [Inventory](#content-of-the-inventoryyml-file) section.

```yaml title="NETWORK_SERVICES.yml"
tenants: # (1)!
  - name: TENANT1
    mac_vrf_vni_base: 10000 # (2)!
    vrfs: # (3)!
      - name: VRF10
        vrf_vni: 10 # (4)!
        vtep_diagnostic: # (5)!
          loopback: 10 # (6)!
          loopback_ip_range: 10.255.10.0/27 # (7)!
        svis: # (8)!
          - id: 11
            name: VRF10_VLAN11 # (9)!
            enabled: true
            ip_address_virtual: 10.10.11.1/24 # (10)!
          - id: 12
            name: VRF10_VLAN12
            enabled: true
            ip_address_virtual: 10.10.12.1/24
      - name: VRF11
        vrf_vni: 11
        vtep_diagnostic:
          loopback: 11
          loopback_ip_range: 10.255.11.0/27
        svis:
          - id: 21
            name: VRF11_VLAN21
            enabled: true
            ip_address_virtual: 10.10.21.1/24
          - name: 22
            name: VRF11_VLAN22
            enabled: true
            ip_address_virtual: 10.10.22.1/24

    l2vlans: # (11)!
      - id: 3401
        name: L2_VLAN3401
      - id: 3402
        name: L2_VLAN3402
```

1. Definition of tenants. Additional level of abstraction in addition to VRFs. In this example just one tenant named `TENANT1` is specified.
2. The base number (`10000`) used to generate the L2VNI numbers automatically, `L2VNI = base number + VLAN-id`. For example, L2VNI for VLAN11 = 10000 + 11 = 10011.
3. VRF definitions inside the tenant.
4. VRF VNI definition.
5. Enable VTEP Network diagnostics. This will create a loopback with virtual source-nat enable to perform diagnostics from the switch:

   ```eos
   interface Loopback10
     description VRF10_VTEP_DIAGNOSTICS
     no shutdown
     vrf VRF10
     ip address 10.255.10.3/32
   !
   ip address virtual source-nat vrf VRF10 address 10.255.10.3
   ```

6. Loopback interface number.
7. Loopback IP range, a unique IP is derived from this range and assigned to each l3 leaf based on its unique id.
8. SVI Definitions for all SVIs within this tenant.
9. SVI Description.
10. IP anycast gateway to be used in the SVI in every leaf across the fabric.
11. These are pure L2 VLANs. They do not have an SVI defined in the l3leafs and they will be bridged inside the VXLAN fabric.

AVD offers granular control of where Tenants and VLANs are configured using `tags` and `filter`. Those areas are not covered in this basic example.

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
    - endpoint_ports: [ PCI1, PCI2 ] # (2)!
      switch_ports: [ Ethernet5, Ethernet5 ] # (3)!
      switches: [ dc1-leaf1a, dc1-leaf1b ] # (4)!
      vlans: 11-12,21-22 # (5)!
      native_vlan: 4092 # (6)!
      mode: trunk # (7)!
      spanning_tree_portfast: edge # (8)!
      port_channel: # (9)!
        description: PortChannel dc1-leaf1-server1
        mode: active

    - endpoint_ports: [ iLO ]
      switch_ports: [ Ethernet5 ]
      switches: [ dc1-leaf1c ]
      vlans: 11
      mode: access
      spanning_tree_portfast: edge
```

1. The relevant `adapters` are defined. For example, the `type` set to `server` and `ilo` is purely for documentation and readability. It has no operational significance.
2. `endpoint_ports` are defined for use in the interface descriptions on the switch. This does not configure anything on the server.
3. `switch_ports` defines the interfaces used in the switches. In this example the server is dual-connected to Ethernet5 and Ethernet5. These two ports exist on switch dc1-leaf1a and dc1-leaf1b defined in the following line.
4. `switches` defines the switches used, in this case dc1-leaf1a and dc1-leaf1b. Note that the `endpoint_ports`, `switch_ports` and `switches` definitions are paired vertically.
5. `vlans` defines which VLANs are allowed on the switch_ports, in this case it is two ranges, VLAN11-12 and VLAN21-22 for the dual-attached server ports and VLAN11 for the iLO port.
6. `native_vlan` specifies the native VLAN when the switch port mode is set to trunk.
7. `mode` is set to trunk for the dual-attached server ports and access for the iLO port.
8. `spanning_tree_portfast` defines whether the switch port should be a spanning tree edge or network port.
9. `port_channel` defines the description and mode for the port-channel.

## The playbooks

In this example, three playbooks are included, of which two must be used:

1. The first playbook `build.yml` is mandatory and is used to build the structured configuration, documentation and finally the actual EOS CLI configuration.
2. The second playbook is a choice between:
   1. `deploy.yml` to deploy the configurations generated by `build.yml` directly to the Arista switches using eAPI.
   2. `deploy-cvp.yml` to deploy the configurations generated by `build.yml` to the Arista switches using CloudVision.

The `build.yml` playbook looks like the following:

```yaml title="build.yml"
--8<--
examples/single-dc-l3ls/build.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the role `arista.avd.eos_designs`, which generates structured configuration for each device. This structured configuration can be found in the `ansible-avd-examples/single-dc-l3ls/intended/structured_configs` folder.
3. This task uses the role `arista.avd.eos_cli_config_gen`, which generates the Arista EOS CLI configurations found in the `ansible-avd-examples/single-dc-l3ls/intended/configs` folder, along with the device-specific and fabric wide documentation found in the `ansible-avd-examples/single-dc-l3ls/documentation/` folder. In addition, it relies on the structured configuration generated by `arista.avd.eos_designs`.

The `deploy.yml` playbook looks like the following:

```yaml title="deploy.yml"
--8<--
examples/single-dc-l3ls/deploy.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the `arista.avd.eos_config_deploy_eapi` role to deploy the configurations directly to EOS nodes that were generated by the `arista.avd.eos_cli_config_gen` role.

The `deploy-cvp.yml` playbook looks like the following:

```yaml title="deploy-cvp.yml"
--8<--
examples/single-dc-l3ls/deploy-cvp.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the CloudVision server named `CLOUDVISION`.
2. This task uses the `arista.avd.eos_config_deploy_cvp` role to deploy and manage the Fabric with CloudVision.
3. Sets `v3` as the version of the collection to use (default in AVD 4.x).
4. `fabric_name` is used to specify the container root in CVP (must match a group name).

In addition, the `arista.avd.eos_config_deploy_cvp` collection performs the following actions:

- Reads the AVD inventory and builds the container topology in CloudVision
- Looks for configuration previously generated by arista.avd.eos_cli_config_gen and builds configlets list, one per device
- Looks for additional configlets to attach to either devices or containers
- Build configlets on CVP
- Create containers topology
- Move devices to the container
- Bind configlet to device
- Deploy Fabric configuration by running all pending tasks (optional, if execute_tasks == true)

### Testing AVD output without a lab

Using the `build.yml` playbook without any actual devices is possible. The playbook will generate all the output (variables, configurations, documentation) but will not attempt to communicate with devices.

Please look through the folders and files described above to learn more about the output generated by AVD.

### Playbook Run

To build the configuration files, run the playbook called `build.yml`.

``` bash
### Build Configurations and Documentation
ansible-playbook playbooks/build.yml
```

After the playbook run finishes, EOS CLI intended configuration files were written to `intended/configs`.

To build and deploy the configurations to your switches directly, using eAPI, run the playbook called `deploy.yml`. This assumes that your Ansible host has access and authentication rights to the switches. Those auth variables are defined in FABRIC.yml.

``` bash
### Deploy Configurations to Devices using eAPI
ansible-playbook playbooks/deploy.yml
```

To build and deploy the configurations to your switches using CloudVision Portal, run the playbook called `deploy-cvp.yml`. This assumes that your CloudVision Portal server has access and authentication rights to the switches. Those auth variables are defined in FABRIC.yml.

``` bash
### Deploy Configurations to Devices Using CloudVision Portal
ansible-playbook playbooks/deploy-cvp.yml
```

### EOS Intended Configurations

Your configuration files should be similar to these.

=== "dc1-spine1"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-spine1.cfg
    --8<--
    ```

=== "dc1-spine2"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-spine2.cfg
    --8<--
    ```

=== "dc1-leaf1a"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf1a.cfg
    --8<--
    ```

=== "dc1-leaf1b"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf1b.cfg
    --8<--
    ```

=== "dc1-leaf1c"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf1c.cfg
    --8<--
    ```

=== "dc1-leaf2a"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf2a.cfg
    --8<--
    ```

=== "dc1-leaf2b"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf2b.cfg
    --8<--
    ```

=== "dc1-leaf2c"

    ``` shell
    --8<--
    examples/single-dc-l3ls/intended/configs/dc1-leaf2c.cfg
    --8<--
    ```

The execution of the playbook should produce the following output:

```shell
user@ubuntu:~/ansible-avd-examples/single-dc-l3ls$ ansible-playbook build.yml

PLAY [Run AVD] *****************************************************************************************************************************************************************************

TASK [arista.avd.eos_designs : Collection arista.avd version 4.0.0 loaded from /home/user/.ansible/collections/ansible_collections] ******************************************************
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
3. Log in to a leaf device, for example, dc1-leaf1a and run the command `show bgp evpn summary` to view EVPN routes.

The following error message is shown:

```eos
dc1-leaf1a#show bgp evpn summ
% Not supported
dc1-leaf1a#
```

This is caused by AVD pushing the configuration line `service routing protocols model multi-agent`, which enables the multi-agent routing process supporting EVPN. This change *requires* a reboot of the device.
