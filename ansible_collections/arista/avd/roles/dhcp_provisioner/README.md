# Ansible Role: dhcp_provisioner

**Table of Contents:**

- [Ansible Role: dhcp_provisioner](#ansible-role-dhcp_provisioner)
  - [Overview](#overview)
  - [Role requirements](#role-requirements)
  - [Role Inputs and Outputs](#role-inputs-and-outputs)
    - [Inputs](#inputs)
      - [Inventory configuration](#inventory-configuration)
      - [Module variables](#module-variables)
      - [Variables dedicated to DHCP device](#variables-dedicated-to-dhcp-device)
      - [Outputs](#outputs)
    - [Tasks](#tasks)
  - [Requirements](#requirements)
  - [License](#license)

## Overview

**dhcp_provisioner** is a role to build and deploy a DHCP configuration file to support Zero Touch Provisioning with Arista EOS devices.

!!! tip - The role supports 2 modes: `offline` and `online`:

 - `Offline` mode let you generate a configuration you can apply on your DHCP server after carefully reviewing it.
 - `Online` mode lets you generate and push configuration to RHEL or Ubuntu based linux system. This mode shall be limited for testing and lab purposes only.

## Role requirements

This role requires to install `arista.cvp` collection to support CloudVision interactions.

```shell
$ ansible-galaxy collection install arista.cvp
```

## Role Inputs and Outputs

### Inputs

#### Inventory configuration

An entry must be part of the inventory to describe DHCP server.

```yaml
all:
  children:
    TOOLS:
      hosts:
        dhcp_server01:
```

#### Module variables

#### Variables dedicated to DHCP device

- __`fabric_group`__: Ansible group where devices are defined per type.
- __`ztp_network_summary`__: Subnet where DHCP will listen for request
- __`ztp_pool_start`__: First IP available in the pool
- __`ztp_pool_end`__: Last IP available in the pool
- __`ztp_lease_time`__: Maximum lease time before device loose IP. Renewal is max/2 (default is 300sec)
- __`ztp_mac_source`__: Define which mac-address field is used for identification: interface ma-address (`interface`) or system-mac-address (`system`). Default: `system`
- __`ztp_mode`__: Define how role works either `offline` or `online`. (Default `offline`)

_Example_:

```yaml
---
- name: Build Switch configuration
  hosts: TOOLS
  connection: local
  gather_facts: false
  tasks:
    - name: Create dhcp configuration file
      import_role:
          name: arista.avd.dhcp_provisioner
      vars:
        ztp_network_summary: 10.73.1.0/24
        ztp_pool_start: 10.73.1.200
        ztp_pool_end: 10.73.1.210
        ztp_lease_time: 300
        fabric_group: 'DC1_FABRIC'
        ztp_mac_source: system
```

This module also reads information from Fabric definition. For any node defined under __spine__, __l3leaf__ and __l2leaf__, role generate an DHCP entry if mac-address is found. Entry is based on the following fields:

- __`mgmt_ip`__: Management IP set as per `eos_l3ls_evpn`
- __`mac_address`__: Mac address used for DHCP. it can be either interface mac-address or system-mac-address

```yaml
# Spine Switches
spine:
  platform: vEOS-LAB
  bgp_as: 65001
  # defines the range of acceptable remote ASNs from leaf switches
  leaf_as_range: 65101-65132
  nodes:
    AVD2-SPINE1:
      id: 1
      mgmt_ip: 10.73.254.1/24
      mac_address: '0c:1d:c0:1d:62:01'
    AVD2-SPINE2:
      id: 2
      mgmt_ip: 10.73.254.2/24
      mac_address: '0c:1d:c0:1d:62:02'
```

#### Outputs

- DHCP configuration file under `intended/configs/dhcpd.conf`

### Tasks

1. Generate structured configuration for DHCP configuration as documented in [`arista.cvp.dhcp_configuration`](https://cvp.avd.sh/en/latest/roles/dhcp_configuration/).
2. Load generated variables.
3. Create DHCP configuration file.
4. If mode is online, apply configuration to DHCP server.

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
