# CloudVision Tags

If  `avd_generate_cloudvision_tags` is set to `True`, `arista.avd.eos_designs` can generate CloudVision Tags that can be applied to interfaces and/or devices. These tags can be used during Topology generateion, or used in searches/filters to select devices based on tags values.

!!! note
    - **By default this new feature is turned off. Set `avd_generate_cloudvision_tags: True` in the Fabric to enable this feature.**
    - **These tags would need to be applied to CloudVision using the [`arista.avd.cloudvision`](../../../cloudvision/README.md) role.**

## Available Input Variables

--8<--
roles/eos_designs/docs/tables/cloudvision-tags.md
--8<--

## CloudVision Topology Tags

`arista.avd.eos_designs` will attempt to generate CloudVision tags that assist CloudVision with rendering the Topology correctly.
It will attempt to generate what are called 'hints' for the following fields. These are picked up from the fabric variables if they are defined.

| Hint Tag Name | Description | Source of information |
| ---------- | ----------- |--------------------- |
| `topology_hint_type` | Indicates whether the node is a leaf, spine, core device etc. | As defined in `node_type` keys. |
| `topology_hint_fabric` | The overall fabric that the devices pertains to. Useful for multi-fabric deployments. | `fabric_name` |
| `topology_hint_datacenter` | The datacenter to which the devices belongs. Helpful for multi-dc deployments. | `dc_name` |
| `topology_hint_pod` | The pod to which the devices belongs. | `pod_name` |
| `topology_hint_rack` | The physical rack in which the device is located. | `rack` defined on `node` or `node_group` |

The `topology_hint_type` for a particular node can be overriden by defining the `cloudvision_tags_topology_type` as per the below table.

??? example "Example: Overriding default topology type"

    ```yaml
      # This should be defined in host_vars or group_vars for the devices
      # we want to affect
      cloudvision_tags_topology_type: edge
    ```

## CloudVision Custom Tags

It is possible to assing custom Tags and values to devices. Depending where the key `cloudvision_tags_device_custom` is defined, the tag can be generated for a whole group or only a single device.

!!! warning
    **Tag names cannot have the name of any existing system tags on CloudVision. System tags cannot be emanded with this approach.**

??? example "Example: Adding custom tags to devices"

    ```yaml
      # This should be defined in host_vars or group_vars for the devices
      # we want to affect
      cloudvision_tags_device_custom:
        - name: custom_tag
          value: custom_value_leaf1a
    ```

## CloudVision Generated Tags

It is possible to generate tags based on values that would be defined in `structured_config`. Any value that is not:

- a list
- a dictionary
- a value in a list

can be defined as the value for a tag. This allows for tags to be generated with values that are calculated for that device. Refer to the example below.

!!! tip
    **Generate the `structured_config` first to get a better idea of what keys are available.**

!!! warning
    - **Tag names cannot have the name of any existing system tags on CloudVision. System tags cannot be emanded with this approach.**
    - **If the key specified in `field` is not found, the tag is not generated. This avoids having a lot of empty tags.**

??? example "Example: Generating device and interface tags"

    ```yaml
      # Each interface will have a tag called 'peer_device_name' with the hostname of
      # of the peer, and a tag 'peer_device_interface' with the value of the
      # interface name on the peer device.
      # If the keys `peer` or `peer_interface` are not found in the structured_config
      # the respective tags will not be created.
      cloudvision_tags_interface_generate:
        - field: peer
          name: peer_device_name
        - field: peer_interface
          name: peer_device_interface

      cloudvision_tags_device_generate:
        # Each EOS device will have tag called 'ip_routing' which will
        # have a value of 'True' if ip_routing is enabled on the device.
        - field: ip_routing
          name: layer3_routing
        # Each EOS device will have tag called 'bgp_router_id' which will
        # have the router_id used for BGP, if it is configured for the device.
        # Note the use of dot notation for the field.
        - field: router_bgp.router_id
          name: bgp_router_id
    ```

## Applying the Tags on CloudVision

For the tags to be available and applied to devices in CloudVision, the role [`arista.avd.cloudvision`](./../../../cloudvision/README.md) need to be called against the fabric.

The **cloudvision** role:

- Is designed to have the device inventory as targets.
- Follows the `hosts` definition as would `eos_designs` and `eos_cli_config_gen`
- Works well with intentory groups, and cli `--limit` arguments
- Uses the `delegate_to` functionality to point to the CloudVision instance.

### Role requirements

This role requires `arista.cvp` collection to support CloudVision interactions.

```shell
ansible-galaxy collection install arista.cvp
```

!!! note
    When using ansible-cvp modules, the user executing the Ansible playbook must have access to both CVP and the EOS CLI.

### Inputs

**Sturctured Config:**

The role expects that the `structured_config` for the devices to be target has already been generated using `eos_designs` role.

**Inventory configuration:**

A host should be defined in the inventory to describe the CloudVision server. `arista.cvp` modules use the httpapi approach. The example below provides a framework to use in your inventory.

!!! warning
    As opposed to `eos_config_deploy_cvp`, the target/host that the role expectes to be run against in the playbook is the EOS device. The `delegate_to` functionality should be used to delegate to the cloudvision node listed in the inventory.**

```yaml
# Example of cloudvision being defined in the inventory
all:
  children:
    cloudvision:
      hosts:
        cv_server01:
          ansible_host: 10.83.28.164
          ansible_user: ansible
          ansible_password: ansible
          ansible_connection: httpapi
          ansible_httpapi_use_ssl: True
          ansible_httpapi_validate_certs: False
          ansible_network_os: eos
          ansible_httpapi_port: 443
```

Below is an example of how to use the role:

```yaml
- name: Apply CloudVision Tags
  hosts: DC1_FABRIC
  gather_facts: false
  tasks:
    - name: Apply Generated CloudVision Tags
      ansible.builtin.import_role:
          name: arista.avd.cloudvision
      delegate_to: cv_server01
```

!!! info
    For a complete list of authentication options available with CloudVision Ansible collection, you can read the dedicated page on [arista.cvp collection](https://cvp.avd.sh/en/latest/docs/how-to/cvp-authentication/).

#### Ignore devices not provisioned in CloudVision

When you want to apply CloudVision tags to a complete topology and devices aren't already in CloudVision, you can configure inventory to ignore these devices by setting the host variable `is_deployed`.

- `is_deployed: true` or `is_deployed is not defined`: The tags for this device are applied on CloudVision
- `is_deployed: false`: Device is skipped.

Here is an overview with the key configured in the YAML inventory:

```yaml
  DC1_BL_LEAFS:
    hosts:
      DC1-BL1A:
        # is_deployed is assumed to be True
        # Device configuration is generated by AVD
        # Device configurationa and tags are applied on Cloudvision
      DC1-BL2A:
        # Device configuration is generated by AVD
        # Device is not configured on Cloudvision and no CloudVision tags are applied.
        is_deployed: false
```
