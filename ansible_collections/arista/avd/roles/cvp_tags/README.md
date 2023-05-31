# cvp_tags

## Overview

**cvp_tags** is a role that generates Tags to be added to Devices and Interfaces in CloudVision Portal.

The **cvp_tags** role:

- Generates `topology_hint` tags to assist CloudVision in generating a better
 Topology layout.
- Generates any custom CloudVision tags defined in the group vars.
- Genereate tags for interfaces to asssit with filtering/searching with
CloudVision dashboards.
- Defines the generated tags on CloudVision via the API.

## Role requirements

This role requires to install `arista.cvp` collection to support CloudVision interactions.

```shell
ansible-galaxy collection install arista.cvp
```

> **NOTE**: When using ansible-cvp modules, the user executing the Ansible playbook must have access to both CVP and the EOS CLI.

## Managing Device Tags

By default, the `cvp_tags` role generates the following CloudVision tags that are applied to each device.

- **topology_hint_type**
  - This tag indicates to CloudVision whether a device is acting as a leaf,spine,core or edge switch.
  - This is defined for each `node_type` by default. The default values can be overriden by redefining the whole `node_type_keys`.
  - When adding new `node_type_keys` it is important to define what `topology_hint_type` is the default for this node type. Example:

    ```yaml
        node_type_keys:
        - border_leaf:
            type: border_leaf
            cvp_tags:
              topology_hint_type: edge
            connected_endpoints: True
            default_evpn_role: "client"
            mlag_support: True
            network_services:
              l2: True
              l3: True
            vtep: True
    ```

  - Overriding type on a particular device can be done using the `topology_hint_type` key in the `cvp_tags` dictionary. Example:

    ```yaml
                dc1-leaf2c:
                  ansible_host: 172.16.1.152
                  cvp_tags:
                    topology_hint_type: edge
    ```

- **topology_hint_datacenter**
  - This tag indicates to CloudVision the datacenter in which the device is located. This value is extracted from `dc_name`, refer to the `eos_designs` documentation for more information on this key.
- **topology_hint_fabric**
  - This tag indicates to CloudVision which fabric this device pertains to. This value is extracted from `fabric_name`, refer to the `eos_designs` documentation for more information on this key.
- **topology_hint_pod**
  - This tag indicates to CloudVision which pod this device is part of. This value is extracted from `pod_name`, refer to the `eos_designs` documentation for more information on this key.
- **topology_hint_rack**
  - This tag indicates to CloudVision in which physical rack the device is located. It is generated if the `rack` key is defined for a device node group. If `rack` is undefined, this tag is not added.

Additionally, custom tags can be defined for devices by using the `cvp_tags` key.

```yaml
            DC1_L3_LEAVES:
              hosts:
                dc1-leaf1a:
                  cvp_tags:
                    custom_tags:
                      - name: custom_tag
                        value: custom_value
                      - name: another_custom_tag
                        value: another_custom_value
```

## Managing Interface Tags

By default, no Interface Tags are added. However, it is possible to add a number of tags and specify the name to be used for these tags, by defining the `cvp_interface_tags` list.
Each entry should define:

- **type** : The type of information to be set in the tag value. Refer to the table below for all the options.
- **name** : The

Refer to the example below:

```yaml
cvp_interface_tags: []
  - type: peer # The type of information in the tag
    name: interface_peer # The name to be used for the tag in CVP
  - type: description
    name: interface_desc
```

The support `type` are listed below

| Type | Description |
| ---- | ----------- |
| description  | adds the full interface desciption tag value |
| peer  | adds the peer name as a value |
| peer_interface  | interface name of the peer interface |
| peer_type | the node type of the peer |
| peer_is_deployed | true or false depending on whether peer is deployed |
| peer_bgp_as | |
| type | The type of this interface |
| ip_address | IP address of this interface |
| peer_ip_address | IP Address for the peer interface |
| channel_group_id | For devices in PortChannel Groups, the ID of this interface |
| peer_channel_group_id | The ID used locally on the Peer Device for PortChannel |
| channel_description | Description on the port channel |
| vlans | vlans allowed on this interface |
| native_vlan | native vlan on this interface |
| trunk_groups | Name of trunk groups | |
| bfd | |
| ptp | |
| mac_security | |
| short_esi | |
| underlay_multicast | |
| ipv6_enable | |

## Role Inputs and Outputs

1. Read inventory
2. Build tags per device
   1. Build interface tags for each device
3. Apply tags per device on CloudVision Portal

### Inputs

**Inventory configuration:**

An entry must be part of the inventory to describe the CloudVision server. `arista.cvp` modules use the httpapi approach. The example below provides a framework to use in your inventory.

> **NOTE**: When using this role, the `hosts` that the playbook should target are the EOS devices defined in the inventory. The CloudVision server should be passed to the role as a varaible. Refer to the [example below](#getting-started).

```yaml
all:
  children:
    cloudvision:
      hosts:
        cv_server01:
          ansible_httpapi_host: 10.83.28.164
          ansible_host: 10.83.28.164
          ansible_user: ansible
          ansible_password: ansible
          ansible_connection: httpapi
          ansible_httpapi_use_ssl: True
          ansible_httpapi_validate_certs: False
          ansible_network_os: eos
          ansible_httpapi_port: 443
          # Configuration to get Virtual Env information
          ansible_python_interpreter: $(which python3)
```

For a complete list of authentication options available with CloudVision Ansible collection, you can read the dedicated page on [arista.cvp collection](https://cvp.avd.sh/en/latest/docs/how-to/cvp-authentication/).

### Role variables

- **`skip_cvp`**: *Optional* When set to `true`, the role will run through the generation of CloudVision Tags but does not apply any changes to CloudVision. *Useful when troubleshooting/testing together with the `debug` ansible tag.*
- **`cvp_node`**: *Required* The hostname as specified in the inventory for the CloudVision server.
- **`cvp_tags_dir`**: *Optional* Define a custom directory where to store the generated tags when running with the `debug` ansible tag. By default it is `intended/cvp_tags/`.
- **`cvp_interface_tags`**: *Optional* List the interfaces tags that are desired. Refer to the [Managing interface tags](#managing-interface-tags) for more information. By default this is an empty list.

> **NOTE**: By default, the generated tags are not saved to files. To save tags in yaml files, use the `--tags debug` when calling the playbook. This will save the tags to the directory defined `cvp_tags_dir`.

#### Getting Started

```yaml
- name: Generate and push CVP Tags
  hosts: FABRIC
  gather_facts: false
  tasks:
    - name: Generate CVP Tags
      ansible.builtin.import_role:
          name: arista.avd.cvp_tags
      vars:
        skip_cvp: false  # Set this to true to just generate YAML files with tags
        cvp_node: <name of cvp node in the inventory>
```

#### Ignore devices not provisioned in CloudVision

When you want to provision a complete topology and devices aren't already in CloudVision, you can configure inventory to ignore these devices by using a host variable: `is_deployed`.

- `is_deployed: true` or `is_deployed is not defined`: Tags are generated and API calls are made to CloudVision to create the tags. If device is undefined, an error is raised.
- `is_deployed: false`: Tags are generated in memory on the localhost, but not created on CloudVision. *The tags can be saved to file if the `debug` ansible tags is passed to the playbook.*

Here is an overview with the key configured in the YAML inventory:

```yaml
  DC1_BL1:
    hosts:
      DC1-BL1A:
  DC1_BL2:
    hosts:
      DC1-BL2A:
        # Tags are generated in memory by role.
        # Tags are not applied to CloudVision.
        is_deployed: false
```

#### Run module with different tags

This module also supports tags to run a subset of ansible tasks:

- **`debug`**: Save the generated tags to separate YAML files in the `cvp_tags_dir`. By default `cvp_tags_dir` will be `intended/cvp_tags/`.

```shell
ansible-playbook playbook.to.deploy.cvp.tags.yml --tags "debug"
```

### Outputs

- None.

### Tasks

1. Copy generated configuration to CloudVision static configlets.
2. Create container topology and attach devices to the correct container.
3. Bind configlet for each device.
4. Apply generated tasks to deploy the configuration to devices.

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
