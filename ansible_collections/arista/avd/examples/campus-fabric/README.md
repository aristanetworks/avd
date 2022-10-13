# Example for Campus Fabric

## Introduction

This example describes and includes all the AVD files used to build an Campus Fabric by building upon the previous [L2LS Fabric](../../examples/campus-fabric/README.md) example. The spine nodes provide L3 routing of SVIs and the L2 leaf nodes support 802.1x Network Access Control (NAC) with port ranges.

## Installation & Requirements

1. Install AVD - Installation guide found [here](../../docs/installation/collection-installation.md).
2. Install Ansible module requirements - Instructions found [here](../../docs/installation/requirements.md).
3. Run the following playbook which will copy Getting Started examples to your current working directory.

``` bash
# current working directory: ~/ansible-avd-examples
ansible-playbook arista.avd.install_examples
```

The output will show something similar to the following. If not, please ensure that AVD and all requirements are correctly installed.

``` shell
 ~/ansible-avd-examples# ansible-playbook arista.avd.install_examples

PLAY [Install Examples]***************************************************************************************************************************************************************************************************************************************************************

TASK [Copy all examples to ~/ansible-avd-examples]*****************************************************************************************************************************************************
changed: [localhost]

PLAY RECAP
****************************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

After the playbook has run successfully, the following directory structure will be created.

``` shell
ansible-avd-examples/     (directory where playbook was run)
  ├── campus-fabric/
    ├── documentation/
    ├── group_vars/
    ├── images/
    ├── intended/
    ├── switch-basic-configurations/
    ├── ansible.cfg
    ├── build.yml
    ├── deploy.yml
    ├── inventory.yml
    └── README.md (this document)
```

???+ info

    If the content of any file in the example is ***modified*** and the playbook is run again, the file ***will not*** be overwritten. However, if any file in the example is ***deleted*** and the playbook is run again, the file will be re-created.

## Design Overview

### Physical Campus Fabric Topology

In a Campus network it is common to refer to the location of the switches as **MDF** (Main Distribution Frame) and **IDFs** (Independent Distribution Frame). Throughtout this example we refer to the spine nodes as the MDF and the leaf nodes as the IDFs. This example shows various switch types and common ways of cabling the IDF to the MDF.

- MDF
  - 2 Spine nodes
- IDFs
  - IDF1 supporting 192 users with a 2 leafs (2RU - 96 ports each)
  - IDF2 supporting 240 users with a Modular 5 slot chassis (48 ports per module)
  - IDF3 supporting 480 users with 5 leafs (2RU - 96 ports each)

The drawing below shows the physical topology used in this example. The interface assignment shown here are referenced across the entire example, so keep that in mind if this example must be adapted to a different topology.

![Figure: 1](images/campus_topo.svg)

## Basic EOS Switch Configuration

Basic connectivity between the Ansible controller host and the switches must be established before Ansible can be used to deploy configurations. The following should be configured on all switches:

- Switch Hostname
- IP enabled interface
- Username and Password defined
- Management eAPI enabled

???+ info

    When using vEOS/cEOS virtual switches, `Management0` is used. When using actual hardware switches, `Management1` is used. The included basic switch configurations may need to be adjusted for your environment.

Below is the basic configuration file for SPINE1:

``` shell
--8<--
examples/campus-fabric/switch-basic-configurations/SPINE1.cfg
--8<--
```

## Ansible Inventory

Now that we understand the physical L2LS topology, we need to create the Ansible inventory that represents this topology. The following is a textual and graphical representation of the Ansible inventory group variables and naming scheme used in this example:

``` text
- DC1
  - DC1_FABRIC
    - DC1_SPINES
    - DC1_LEAFS
  - DC1_NETWORK_SERVICES
    - DC1_SPINES
    - DC1_LEAFS
  - DC1_NETWORK_PORTS
    - DC1_SPINES
    - DC1_LEAFS
```

DC1 represents the highest level within the hierarchy. Ansible variables defined at this level will be applied to all nodes in the fabric. Ansible groups have parent and child relationships. For example, both DC1_SPINES and DC1_LEAFS are children of DC1_FABRIC. Groups of Groups are possible and allow variables to be shared at any level within the hierarchy. For example, DC1_NETWORK_SERVICES is a group with two other groups defined as children: DC1_SPINES and DC1_LEAFS. The same applies to the group named DC1_NETWORK_PORTS. You will see these groups listed at the bottom of the inventory file.

This naming convention makes it possible to extend anything quickly and can be changed based on your preferences. The names of all groups and hosts must be unique.

![Figure: 2](images/ansible_groups.svg)

### inventory.yml

The below inventory file represents two Spines and four Leafs. The nodes are defined under the groups DC1_SPINES and DC1_LEAFS, respectively. We apply group variables (group_vars) to these groups to define their functionality and configurations.

The hostnames specified in the inventory must exist either in DNS or in the hosts file on your Ansible host to allow successful name lookup and be able to reach the switches directly. A successful ping from the Ansible host to each inventory host verifies name resolution (e.g., ping SPINE1).

Alternatively, if DNS is not available, define the variable ansible_host to be an IP address for each device.

``` yaml
--8<--
examples/campus-fabric/inventory.yml
--8<--
```

## Build Fabric Topology

AVD Fabric Input Variables

To apply AVD input variables to the nodes in the fabric, we make use of Ansible group_vars. How and where you define the variables is your choice. The group_vars table below is one example of AVD fabric variables.

| group_vars/              | Description                                   |
| ------------------------ | --------------------------------------------- |
| DC1.yml                  | Global settings for all devices               |
| DC1_FABRIC.yml           | Fabric, Topology, and Device settings         |
| DC1_SPINES.yml           | Device type for Spines                        |
| DC1_LEAFS.yml            | Device type for Leafs                         |
| DC1_NETWORK_SERVICES.yml | VLANs/SVIs                                    |
| DC1_NETWORK_PORTS.yml    | Port Profiles and Network Port Ranges         |

The tabs below show the Ansible **group_vars** used in this example.

=== "DC1"
    At the top level (DC1), the following variables are defined in **group_vars/DC1.yml**. These Ansible variables apply to all nodes in the fabric and is a common place to set AAA, users, NTP, and management interface settings. Update local_users and passwords for your environment.

    You can create a sha512_password by creating a username and password on a switch and copy/paste it within double quotes here.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1.yml
    --8<--
    ```

=== "DC1_FABRIC"
    At the Fabric level (DC1_FABRIC), the following variables are defined in **group_vars/DC1_FABRIC.yml**. The fabric name, design type (l2ls), spine and leaf defaults, ansible authentication, and interface links are defined at this level. Other variables you must supply include: spanning-tree mode and priority along with an mlag IP pool.  Typically, and IDF has a unique set of VLANs. You may use the `filter.tags` variable to constrain which vlans are built on an IDF node.

    Variables applied under the node key type (spine/leaf) defaults section are inherited to nodes under each type. These variables may be overwritten under the node itself.

    The spine interface used by a particular leaf is defined from the leaf's perspective with a variable called `uplink_switch_interfaces`. For example, LEAF2A has a unique variable `uplink_switch_interfaces: [Ethernet49/1, Ethernet49/1]` defined. This means that LEAF2A is connected to SPINE1's Ethernet49/1 and SPINE2's Ethernet49/1, respectively.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1_FABRIC.yml
    --8<--
    ```

=== "DC1_SPINES"
    In an L2LS design, there are two types of spine nodes: `spine` and `l3spine`. In AVD. the node type defines the functionality and the EOS CLI configuration to be generated. For an L2LS design, we will use node type: spine. Later, we will add routing to the Spines by changing the node type to l3spine.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1_SPINES.yml
    --8<--
    ```

=== "DC1_LEAFS"
    In an L2LS design, we have one type of leaf node: `leaf`.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1_LEAFS.yml
    --8<--
    ```

=== "DC1_NETWORK_SERVICES"
    You add VLANs and SVIs to the Fabric by updating the **group_vars/DC1_NETWORK_SERVICES.yml**. Each VLAN will be given a name and a list of tags. The tags filter the VLAN to specific Leaf Pairs. These variables are applied to spine and leaf nodes since they are a part of this group.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1_NETWORK_SERVICES.yml
    --8<--
    ```

=== "DC1_NETWORK_PORTS"
    Our fabric would not be complete without connecting some devices to it. We define port profiles and network port ranges in **group_vars/DC1_NETWORKS_PORTS.yml**. A single port_profile may be used across a number of switches and port ranges.  In our example we create a port_profile called `PP-DOT1X` to define generic 802.1x (NAC) settings we wish to apply to a range of ports. The network_ports data model is where we define which switches and ports to apply the port profile.  This data model allows a single regex statement to define a list of switches. In addition, the variable `switch_ports` expands into a range of ports. Details of the range_expand filter can be viewed [here](https://avd.sh/en/stable/plugins/index.html#range_expand-filter). These variables are applied to spine and leaf nodes since they are a part of this inventory group.

    ``` yaml
    --8<--
    examples/campus-fabric/group_vars/DC1_NETWORK_PORTS.yml
    --8<--
    ```

## Network Services

The Network Services data model is stored in the **DC1_NETWORK_SERVICES** group_var tab above. Each IDF will have 3 unique VLANs to support Data, Voice and Guest networks. The spine nodes will provide routing for these VLANs via locally assigned SVIs.

### VLAN/IP Subnet Assignment

| IDF  | Data                 | Voice                 | Guest                 |
| ---- | -------------------- | --------------------- | --------------------- |
| IDF1 | 110 - (10.1.10.0/23) | 120 - (10.1.20.0/23)  | 130 - (10.1.30.0/23)  |
| IDF2 | 210 - (10.2.10.0/23) | 220 - (10.2.20.0/23)  | 230 - (10.2.30.0/23)  |
| IDF3 | 310 - (10.3.10.0/23) | 320 - (10.3.20.0/23)  | 330 - (10.3.30.0/23)  |

## Port Profiles and Network Ports

AVD provides a way to standardize and reuse port profiles through a compact data model that can be utilized across the network. The Network Ports data model is stored in the **DC1_NETWORK_PORTS** group_vars tab above. Each port is configured to support NAC and dynamically assigns the proper vlan based on 802.1x authentication. Multiple device types (IP Phone, Workstations, Printers, Access Points, etc...) can share the same port configuration below.

![Figure: 3](images/dot1x_ports.svg)

The above sample port configuration is easily produced with `port_profiles` and `network_ports` data models. Each port has similar configuration items defined in port_profiles, while network_ports defines which switches and port ranges to be applied. The network_ports data model allows the use of regex to match switches and an expand_range filter to cover a range of ports. For details, see documentation for [port_profiles](https://avd.sh/en/stable/roles/eos_designs/doc/connected-endpoints.html#port-profiles) and [network_ports](https://avd.sh/en/stable/roles/eos_designs/doc/connected-endpoints.html#network-ports_1).

## Deploy Fabric

## The Playbooks

Now that we have defined all of our Ansible variables (AVD inputs), it is time to generate some configs. To make things simple, we provide two playbooks. One playbook will allow you to build and view EOS CLI intended configurations per device. The second playbook has an additional task to deploy the configurations to your switches. The playbooks are provided in the tabs below. The playbook is straightforward as it imports two AVD roles: eos_designs and eos_cli_config_gen, which do all the heavy lifting. The combination of these two roles produces recommended configurations that follow Arista Design Guides.

=== "build.yml"

    ``` yaml
    --8<--
    examples/campus-fabric/build.yml
    --8<--
    ```

=== "deploy.yml"

    ``` yaml
    --8<--
    examples/campus-fabric/deploy.yml
    --8<--
    ```

### Playbook Run

To build the configurations files, run the playbook called `build.yml`.

``` bash
### Build configurations
ansible-playbook build.yml
```

After the playbook run finishes, EOS CLI intended configuration files were written to `intended/configs`.

To build and deploy the configurations to your switches, run the playbook called `deploy.yml`. This assumes that your Ansible host has access and authentication rights to the switches. Those auth variables were defined in DC1_FABRIC.yml.

``` bash
### Build configurations & Push Configs to switches
ansible-playbook deploy.yml
```

### EOS Intended Configurations

Your configuration files should be similar to these.

=== "SPINE1"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/SPINE1.cfg
    --8<--
    ```

=== "SPINE2"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/SPINE2.cfg
    --8<--
    ```

=== "LEAF1A"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF1A.cfg
    --8<--
    ```

=== "LEAF1B"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF1B.cfg
    --8<--
    ```

=== "LEAF2A"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF2A.cfg
    --8<--
    ```

=== "LEAF3A"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF3A.cfg
    --8<--
    ```

=== "LEAF3B"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF3B.cfg
    --8<--
    ```

=== "LEAF3C"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF3C.cfg
    --8<--
    ```

=== "LEAF3D"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF3D.cfg
    --8<--
    ```

=== "LEAF3E"

    ``` shell
    --8<--
    examples/campus-fabric/intended/configs/LEAF3E.cfg
    --8<--
    ```

## Next steps

Modify this example and expand the features to match your Campus topology.
