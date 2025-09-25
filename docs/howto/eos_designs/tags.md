<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Tags

## Introduction to Tags

**Tags** are a powerful and flexible way to apply configurations and policies to specific groups of devices, interfaces, or other network elements. Think of them as labels that you can attach to various components in your network definition. 🏷️

By assigning tags, you can create logical groupings that are independent of the physical network topology or naming conventions. This makes it much easier to manage configurations at scale.

## Key Concepts of AVD Tags

### 1. Applying Configuration

The primary use of tags is to **select which devices or interfaces a particular configuration should apply to**. For example, you can define a set of NTP servers and then use a tag to apply that configuration only to your "core" routers.

Instead of creating separate configurations for each device, you define a feature once and use tags to control its deployment.

### 2. Defining and Assigning Tags

Tags are typically defined in your AVD group variable files. You can assign them to:

- **Nodes (Devices):** You can tag a device based on its role (e.g., `spine`, `leaf`), location (e.g., `datacenter-1`, `closet-5`), or any other criteria.

- **Links/Interfaces:** You can tag interfaces to define where specific services, like an SVI (Switched Virtual Interface) or a VRF (Virtual Routing and Forwarding), should be deployed.

**Example:**

In your group variables, you might define your leaf switches like this:

```yaml
leaf:
  nodes:
    - name: leaf1
      tags: [ "prod", "rack-1" ]
    - name: leaf2
      tags: [ "prod", "rack-2" ]
    - name: leaf3
      tags: [ "dev", "rack-3" ]
    - name: leaf4
      tags: [ "dev", "rack-4" ]
```

Here, `leaf1` has the tags `prod` and `rack-1`.

### 3. Targeting with Tags

When defining a service, you specify which tags it should target. AVD uses this information to determine where to generate the configuration.

#### Example

Let's say you want to deploy VLAN 100 only on devices tagged as `prod`. You would define the VLAN and use the `tags` key to specify your target.

```yaml
tenants:
  - name: my_tenant
    svis:
      - id: 100
        name: VLAN100
        tags: [ "prod" ] # This SVI will only be configured on devices with the 'prod' tag
        ip_address_virtual: "10.10.100.1/24"
```

Based on the examples above, only `leaf1` and `leaf2` would have VLAN 100 configured, because they both have the `prod` tag.

### 4. "All" vs. "Any" Logic

AVD provides flexibility in how it matches tags:

- **`any` (Default):** If you provide a list of tags like `[ "tagA", "tagB" ]`, the configuration will be applied to any device that has *at least one* of those tags. This is an "OR" condition.

- **`all`:** You can specify that a device must have *all* of the listed tags for the configuration to be applied. This is an "AND" condition. You can control this using the `mode` setting where applicable.

This logic is crucial for creating precise and targeted configurations in complex environments.

In summary, **tags are the glue** that connects your intended configuration policies to the specific network components where they should be implemented. They are fundamental to AVD's declarative and automated approach to network management.
