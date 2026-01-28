<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
-->

# AVD Usage Patterns - A Progressive Guide

This guide demonstrates the different ways to use Arista AVD roles, starting from basic usage and progressively introducing more advanced patterns. Each section builds upon the previous one, showing how AVD's flexibility allows you to customize configurations to meet your specific needs.

## Using eos_cli_config_gen Directly

The `eos_cli_config_gen` role is the foundation of AVD. It converts structured configuration data (in YAML format) into EOS CLI commands.

!!! warning "Not Recommended for Most Users"
    Using `eos_cli_config_gen` directly is **not the typical way** to use AVD. Most users should start with the `eos_designs` role (see next section), which provides a higher-level abstraction and automatically generates the structured configuration for you.

### High-Level Flow

```mermaid
graph LR
    A[EOS Config Input Model] --> B{eos_cli_config_gen}
    B --> C[EOS CLI Configuration]

    style A fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff
```

### Explanation

When using `eos_cli_config_gen` directly, you provide structured configuration using the EOS CLI Config Gen data model. The role processes this input and generates the corresponding EOS CLI configuration file.

This approach might be useful in specific cases:

- You want full control over the exact configuration
- You're working with a small number of devices
- You're migrating from manual configuration to automation
- You're using AVD for non-fabric use cases

### Example: Configuring DNS Name Servers

#### Input (YAML)

```yaml
# host_vars/leaf1.yml
ip_name_servers:
  - ip_address: 10.10.128.10
    vrf: MGMT
  - ip_address: 10.10.128.11
    vrf: MGMT
```

#### Example Flow Diagram

```mermaid
graph LR
    A["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"] --> B{eos_cli_config_gen}
    B --> C["ip name-server vrf MGMT 10.10.128.10<br/>ip name-server vrf MGMT 10.10.128.11"]

    style A fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
```

#### Generated EOS CLI Output

```eos
ip name-server vrf MGMT 10.10.128.10
ip name-server vrf MGMT 10.10.128.11
```

---

## Using eos_designs with eos_cli_config_gen

The `eos_designs` role provides a higher level of abstraction. Instead of defining low-level structured configuration, you describe your network design intent, and `eos_designs` generates the structured configuration, which is then processed by `eos_cli_config_gen`.

### High-Level Flow

```mermaid
graph LR
    A[AVD Design Input Model] --> B{eos_designs}
    B --> C[Structured Configuration<br/>EOS Config Input Model]
    C --> D{eos_cli_config_gen}
    D --> E[EOS CLI Configuration]

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff
```

### Explanation

The `eos_designs` role implements Arista's best practices and design patterns. You provide high-level design parameters (like fabric topology, VLANs, VRFs), and the role:

1. Generates the complete structured configuration following the EOS Config Input Model
2. Passes this to `eos_cli_config_gen` for CLI generation

This two-stage process separates design intent from configuration rendering, making it easier to manage large-scale deployments.

### Example: Configuring DNS Settings for a Fabric

#### Input (YAML)

```yaml
# group_vars/FABRIC.yml
dns_settings:
  servers:
    - ip_address: 10.10.128.10
    - ip_address: 10.10.128.11
```

#### Example Flow Diagram

```mermaid
graph LR
    A["dns_settings:<br/>&nbsp;&nbsp;servers:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.11"] --> B{eos_designs}
    B --> C["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"]
    C --> D{eos_cli_config_gen}
    D --> E["ip name-server vrf MGMT 10.10.128.10<br/>ip name-server vrf MGMT 10.10.128.11"]

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:2px,color:#fff,font-family:monospace,text-align:left
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,font-family:monospace,text-align:left
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff,font-family:monospace,text-align:left
```

#### Generated Structured Configuration (Intermediate)

```yaml
# Automatically generated by eos_designs
ip_name_servers:
  - ip_address: 10.10.128.10
    vrf: MGMT
  - ip_address: 10.10.128.11
    vrf: MGMT
```

#### Generated EOS CLI Output

```eos
ip name-server vrf MGMT 10.10.128.10
ip name-server vrf MGMT 10.10.128.11
```

---

## Using structured_config for Device-Specific Overrides

Sometimes you need to override or extend the configuration generated by `eos_designs` for specific devices. The `structured_config` key allows you to inject custom structured configuration that will be merged with the auto-generated configuration.

### High-Level Flow

```mermaid
graph LR
    A --> B1
    A --> B4
    B4 --> C[Final Structured Configuration<br/>EOS Config Input Model]
    C --> D{eos_cli_config_gen}
    D --> E[EOS CLI Configuration]

    subgraph A[AVD Design Inputs]
        direction TB
        A1[Design Model]
        A2[structured_config in the model]
    end

    subgraph B[eos_designs]
        direction LR
        B1{Input Processing<br/>Design Modules} --> B2[Intermediate<br/>Structured Config]
        B2 --> B4{Merge<br/>Overrides}
    end

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:3px,color:#fff
    style A1 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff
    style A2 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:3px,color:#fff
    style B1 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style B2 fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style B4 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff
```

### Explanation

The `eos_designs` role processes your design inputs in multiple stages:

1. **Input Processing & Design Modules**: Generate structured configuration based on your fabric design (topology, VLANs, VRFs, etc.)
2. **Intermediate Structured Config**: The auto-generated configuration following the EOS Config Input Model
3. **Merge Overrides**: Apply any device-specific `structured_config` (and/or `custom_structured_configuration_*` variables) on top of the generated configuration
4. **Final Output**: The complete structured configuration ready for `eos_cli_config_gen`

This allows you to:

- Override specific values generated by `eos_designs`
- Add configuration elements not covered by the design model
- Customize individual devices while maintaining fabric-wide consistency

The merge is recursive, so you can update specific sub-keys without replacing entire configuration sections.

**Note**: You can use both `structured_config` and `custom_structured_configuration_*` variables together - they will both be merged onto the generated configuration.

### Example: Fabric DNS with Device-Specific Override

In this example, we configure DNS servers for the entire fabric, but one leaf switch needs additional name servers with higher priority.

#### Input (YAML)

```yaml
# group_vars/FABRIC.yml
dns_settings:
  servers:
    - ip_address: 10.10.128.10
    - ip_address: 10.10.128.11

l3leaf:
  nodes:
    - name: leaf1
      id: 1
      mgmt_ip: 192.168.1.11/24
      structured_config:
        ip_name_servers:
          - ip_address: 10.20.20.10
            vrf: MGMT
          - ip_address: 10.10.128.10
            vrf: MGMT
            priority: 2
```

#### Example Flow Diagram

```mermaid
graph LR
    A1 --> B1
    A2 --> B4
    B4 --> C["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;priority: 2<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.20.20.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"]
    C --> D{eos_cli_config_gen}
    D --> E["ip name-server vrf MGMT 10.10.128.10 priority 2<br/>ip name-server vrf MGMT 10.10.128.11<br/>ip name-server vrf MGMT 10.20.20.10"]

    subgraph A[AVD Design Inputs]
        direction TB
        A1["dns_settings:<br/>&nbsp;&nbsp;servers:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.11"]
        A2["l3leaf:<br/>&nbsp;&nbsp;nodes:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- name: leaf1<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id: 1<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip: 192.168.1.11/24<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config:<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_name_servers:<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address: 10.20.20.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority: 2"]
    end

    subgraph B[eos_designs]
        direction LR
        B1{Process<br/>dns_settings} --> B2["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"]
        B2 --> B4{Merge<br/>Overrides}
    end

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:3px,color:#fff
    style A1 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff,text-align:left,font-family:monospace
    style A2 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff,text-align:left,font-family:monospace
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:3px,color:#fff
    style B1 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style B2 fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
    style B4 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
```

#### Generated EOS CLI Output (leaf1 only)

```eos
ip name-server vrf MGMT 10.10.128.10 priority 2
ip name-server vrf MGMT 10.10.128.11
ip name-server vrf MGMT 10.20.20.10
```

---

## Using custom_structured_configuration Prefix

The `custom_structured_configuration` prefix provides an alternative way to supply custom structured configuration. Instead of nesting configuration under `structured_config` keys, you can define variables at any group or host level using the prefix.

### High-Level Flow

```mermaid
graph LR
    A --> B1
    A --> B4
    B4 --> C[Final Structured Configuration<br/>EOS Config Input Model]
    C --> D{eos_cli_config_gen}
    D --> E[EOS CLI Configuration]

    subgraph A[AVD Design Inputs]
        direction TB
        A1[Design Model]
        A2[custom_structured_configuration_*s]
    end

    subgraph B[eos_designs]
        direction LR
        B1{Input Processing<br/>Design Modules} --> B2[Intermediate<br/>Structured Config]
        B2 --> B4{Merge<br/>Overrides}
    end

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:3px,color:#fff
    style A1 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff
    style A2 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:3px,color:#fff
    style B1 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style B2 fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style B4 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff
```

### Explanation

The `custom_structured_configuration` prefix approach works similarly to `structured_config`, but offers more flexibility in where you define the variables:

- Variables are prefixed with `custom_structured_configuration_` (by default)
- They can be defined at any level: group_vars, host_vars, or even in inventory
- The prefix is stripped, and the remaining variable name must match an `eos_cli_config_gen` key
- Multiple custom variables are merged together, then merged on top of `eos_designs` generated configuration

This approach is useful when:

- You want to organize custom configuration separately from design inputs
- You need to apply custom configuration at different inventory levels
- You prefer a flatter variable structure

**Important**: Both `structured_config` and `custom_structured_configuration_*` can be used together in the same deployment. They are both merged onto the intermediate structured configuration during the same merge step.

### Example: Same Override Using Prefix Approach

This example achieves the same result as Section 3, but uses the `custom_structured_configuration_` prefix instead of nested `structured_config`.

#### Input (YAML)

```yaml
# group_vars/FABRIC.yml
dns_settings:
  servers:
    - ip_address: 10.10.128.10
    - ip_address: 10.10.128.11

# host_vars/leaf1.yml
# Using custom_structured_configuration prefix
custom_structured_configuration_ip_name_servers:
  - ip_address: 10.20.20.10
    vrf: MGMT
  - ip_address: 10.10.128.10
    vrf: MGMT
    priority: 2
```

#### Example Flow Diagram

```mermaid
graph LR
    A1 --> B1
    A2 --> B4
    B4 --> C["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;priority: 2<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.20.20.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"]
    C --> D{eos_cli_config_gen}
    D --> E["ip name-server vrf MGMT 10.10.128.10 priority 2<br/>ip name-server vrf MGMT 10.10.128.11<br/>ip name-server vrf MGMT 10.20.20.10"]

    subgraph A[AVD Design Inputs]
        direction TB
        A1["dns_settings:<br/>&nbsp;&nbsp;servers:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;- 10.10.128.11"]
        A2["leaf1:<br/>&nbsp;&nbsp;custom_structured_configuration_ip_name_servers:<br/>&nbsp;&nbsp;&nbsp;&nbsp;- ip_address: 10.20.20.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority: 2"]
    end

    subgraph B[eos_designs]
        direction LR
        B1{Process<br/>dns_settings} --> B2["ip_name_servers:<br/>&nbsp;&nbsp;- ip_address: 10.10.128.10<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT<br/>&nbsp;&nbsp;- ip_address: 10.10.128.11<br/>&nbsp;&nbsp;&nbsp;&nbsp;vrf: MGMT"]
        B2 --> B4{Merge<br/>Overrides}
    end

    style A fill:#1e3a5f,stroke:#4a90e2,stroke-width:3px,color:#fff
    style A1 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff,text-align:left,font-family:monospace
    style A2 fill:#2d5a8f,stroke:#4a90e2,stroke-width:1px,color:#fff,text-align:left,font-family:monospace
    style B fill:#5f4c2e,stroke:#d4a574,stroke-width:3px,color:#fff
    style B1 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style B2 fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
    style B4 fill:#7a6340,stroke:#d4a574,stroke-width:2px,color:#fff
    style C fill:#3d2f5f,stroke:#9575cd,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
    style D fill:#5f4c2e,stroke:#d4a574,stroke-width:2px,color:#fff
    style E fill:#2d4a2e,stroke:#7cb342,stroke-width:2px,color:#fff,text-align:left,font-family:monospace
```

#### Generated EOS CLI Output (leaf1 only)

```eos
ip name-server vrf MGMT 10.10.128.10 priority 2
ip name-server vrf MGMT 10.10.128.11
ip name-server vrf MGMT 10.20.20.10
```

**Result**: Identical to the previous approach, but using the `custom_structured_configuration_*` prefix instead of nested `structured_config`.

---

## Summary and Comparison

| Approach | Use Case | Complexity | Flexibility |
|----------|----------|------------|-------------|
| **eos_cli_config_gen only** | Small deployments, full control, migration from manual config, non-fabric use cases | Low | High (full control) |
| **eos_designs + eos_cli_config_gen** | Standard fabric deployments, best practices (recommended starting point) | Medium | Medium (design-driven) |
| **structured_config** | Device-specific overrides within design model | Medium-High | High (targeted overrides) |
| **custom_structured_configuration** | Flexible overrides across inventory levels | Medium-High | Very High (maximum flexibility) |

### Key Takeaways

1. **Start with eos_designs**: Most users should begin with `eos_designs` for fabric deployments, not `eos_cli_config_gen` directly
2. **Override When Needed**: Use `structured_config` or `custom_structured_configuration_` for exceptions
3. **Combine Approaches**: The last two approaches can be used together - both `structured_config` and `custom_structured_configuration_*` variables are merged during the same step
4. **Understand Precedence**: Custom configuration is merged *after* design generation, allowing overrides
5. **Choose Your Style**: Pick the override method that fits your workflow - nested `structured_config` or prefixed variables

### Next Steps

- Review the [Custom Structured Configuration How-To](../../ansible_collections/arista/avd/roles/eos_designs/docs/how-to/custom-structured-configuration.md) for advanced patterns
- Explore the [eos_designs data model](../../ansible_collections/arista/avd/roles/eos_designs/README.md) for available design options
- Check the [eos_cli_config_gen data model](../../ansible_collections/arista/avd/roles/eos_cli_config_gen/README.md) for all configuration options
