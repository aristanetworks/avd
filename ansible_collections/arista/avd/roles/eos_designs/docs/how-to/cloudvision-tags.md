## CloudVision Tags

If  `avd_generate_cloudvision_tags` is set to `True`, `arista.avd.eos_designs` can generate CloudVision Tags that can be applied to interfaces and/or devices. These tags can be used during Topology generateion, or used in searches/filters to select devices based on tags values.

!!! note
    - **By default this new feature is turned off. Set `avd_generate_cloudvision_tags: True` in the Fabric to enable this feature.**
    - **These tags would need to be applied to CloudVision using the [`arista.avd.cloudvision`](../../../roles/cloudvision/README.md) role.**

### CloudVision Topology Tags

`arista.avd.eos_designs` will attempt to generate CloudVision tags that assist CloudVision with rendering the Topology correctly.
It will attempt to generate what are called 'hints' for the following fields. These are picked up from the fabric variables if they are defined.

| Hint Label | Description | Source of information |
| ---------- | ----------- |--------------------- |
| `topology_hint_type` | Indicates whether the node is a leaf, spine, core device etc. | As defined in `node_type` keys. |
| `topology_hint_fabric` | The overall fabric that the devices pertains to. Useful for multi-fabric deployments. | `fabric_name` |
| `topology_hint_datacenter` | The datacenter to which the devices belongs. Helpful for multi-dc deployments. | `dc_name` |
| `topology_hint_pod` | The pod to which the devices belongs. | `pod_name` |
| `topology_hint_rack` | The physical rack in which the device is located. | `rack` defined on `node` or `node_group` |

The `topology_hint_type` for a particular node can be overriden by defining the `cloudvision_tags_topology_type` as per the below table.

--8<--
roles/eos_designs/docs/tables/cloudvision-tags.md
--8<--

??? example "Example: Overriding default topology type"

    ```yaml
      # This should be defined in host_vars or group_vars for the devices
      # we want to affect
      cloudvision_tags_topology_type: edge
    ```

### CloudVision Custom Tags

It is possible to assing custom Tags and values to devices. Depending where the key `cloudvision_tags_device_custom` is defined, the tag can be generated for a whole group or only a single device.

!!! warning
    **Tag labels cannot have the name of any existing system tags on CloudVision. System tags cannot be emanded with this approach.**

--8<--
roles/eos_designs/docs/tables/cloudvision-tags.md
--8<--

??? example "Example: Adding custom tags to devices"

    ```yaml
      DC1_POD1_L3_LEAVES:
        hosts:
          dc1-pod1-leaf1a:
            cloudvision_tags_device_custom:
              - name: custom_tag
                value: custom_value_leaf1a
            ansible_host: 172.16.1.101
    ```

### CloudVision Generated Tags

It is possible to generate tags based on values that would be defined in `structured_config`. Any value that is not:

- a list
- a dictionary
- a value in a list

can be defined as the value for a tag. This allows for tags to be generated with values that are calculated for that device. Refer to the example below.

!!! tip
    **Generate the `structured_config` once to get a better idea of what keys are available.**

!!! warning
    - **Note 1: Tag labels cannot have the name of any existing system tags on CloudVision. System tags cannot be emanded with this approach.**
    - **Note 2: If the key specified in `field` is not found, the tag is not generated. This avoids having a lot of empty tags.**

#### Generating Tags for Devices

--8<--
roles/eos_designs/docs/tables/cloudvision-tags.md
--8<--

#### Generating Tags for Intefaces

--8<--
roles/eos_designs/docs/tables/cloudvision-tags-.md
--8<--

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

      # Each EOS device will have tag called 'ip_routing' which will
      # have a value of 'True' if ip_routing is enabled on the device.
      cloudvision_tags_device_generate:
        - field: ip_routing
          name: layer3_routing
    ```
