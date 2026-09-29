---
# This title is used for search results
title: AVD Design data models for digital twin
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

## PREVIEW - Digital Twin settings

!!! note
    To easily switch between production mode and digital twin mode, it is recommended to create a dedicated playbook where `avd_digital_twin_mode: true` is set in the playbook vars.

    By default, Digital Twin artifacts (such as the topology file, adjusted structured and EOS configuration, device and fabric documentation)
    will replace original fabric artifacts.

    To keep Digital Twin artifacts separate, adjust the `output_dir_name` and `documentation_dir_name` variables for both `eos_designs`
    and `eos_cli_config_gen` to point to a dedicated output location.

AVD Digital Twin functionality natively generates all artifacts required to deploy a virtual replica of a production AVD fabric.
The generated artifacts are automatically optimized for the specific Digital Twin environment. For example, an EOS configuration generated for an ACT environment will automatically remove or adjust any unsupported features.

AVD currently supports the following Digital Twin environments:

- ACT (Arista Cloud Test)
- Containerlab

To generate Digital Twin artifacts, run the `eos_designs` and `eos_cli_config_gen` roles with the `avd_digital_twin_mode` flag set to `true` in your Ansible playbook:

```yaml
---

# Production playbook to generate production fabric artifacts
- name: Build Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

# Digital Twin playbook to generate Digital Twin mode artifacts
- name: Build Configurations and Documentation
  hosts: FABRIC
  gather_facts: false
  vars:
    # Adjust the output dirs to keep Digital Twin artifacts in a separate directory
    output_dir_name: "digital_twin/intended"
    documentation_dir_name: "digital_twin/documentation"
    # Set this flag to True to enable Digital Twin mode
    avd_digital_twin_mode: true
  tasks:

    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen

```

Produced artifacts (ACT Digital Twin):

```text
.
├── digital_twin
│   ├── documentation
│   │   ├── devices
│   │   │   ├── <DEVICE_NAME>.md
│   │   │   └── ...
│   │   └── fabric
│   │       ├── <FABRIC_NAME>-documentation.md
│   │       ├── <FABRIC_NAME>-p2p-links.csv
│   │       ├── <FABRIC_NAME>-topology.csv
│   │       └── <FABRIC_NAME>-topology.yml
│   └── intended
│       ├── configs
│       │   ├── <DEVICE_NAME>.cfg
│       │   └── ...
│       └── structured_configs
│           ├── <DEVICE_NAME>.yml
│           └── ...
```

If not specified otherwise, AVD uses the following default values when generating ACT Digital Twin artifacts:

| Attribute | Description | Default value | Source of information |
| --------- | ----------- | ------------- | --------------------- |
| act_os_version | OS version of the replica device | `cloudeos`: `4.33.2F`<br>`cvp`: `2024.3.2`<br>`generic`: `ubuntu-2204-lts`<br>`third-party`: `byod`<br>`tools-server`: `ubuntu-2204-lts`<br>`veos`: `4.33.1.1F` | `node_config.digital_twin.act_os_version` or `digital_twin.fabric.act_os_version` |
| act_username | username of the default account deployed on the replica device | `admin` | `digital_twin.fabric.act_username` |
| act_password | password of the default account deployed on the replica device | `admin` | `digital_twin.fabric.act_password` |

--8<--
schemas/avd_design/docs/tables/digital-twin-configuration.md
--8<--

### Node type Digital Twin configuration

--8<--
schemas/avd_design/docs/tables/node-type-digital-twin-configuration.md
--8<--

### Containerlab Digital Twin

Produced artifacts (Containerlab Digital Twin):

```text
.
├── digital_twin
│   ├── <FABRIC_NAME>-topology.clab.yml
│   ├── interface_mapping.json
│   ├── documentation
│   │   ├── devices
│   │   │   ├── <DEVICE_NAME>.md
│   │   │   └── ...
│   │   └── fabric
│   │       ├── <FABRIC_NAME>-documentation.md
│   │       ├── <FABRIC_NAME>-p2p-links.csv
│   │       └── <FABRIC_NAME>-topology.csv
│   └── intended
│       ├── configs
│       │   ├── <DEVICE_NAME>.cfg
│       │   └── ...
│       └── structured_configs
│           ├── <DEVICE_NAME>.yml
│           └── ...
```

Containerlab Digital Twin is available as a `PREVIEW` feature. It is not ready for production use and is intended for user testing only.

To enable it, set `digital_twin.environment: containerlab` and run the same Digital Twin playbook shown above with the environment set to `containerlab`:

```yaml
---
- name: Build Containerlab Digital Twin artifacts
  hosts: FABRIC
  gather_facts: false
  vars:
    output_dir_name: "digital_twin/intended"
    documentation_dir_name: "digital_twin/documentation"
    avd_digital_twin_mode: true
    digital_twin:
      environment: containerlab
      fabric: {}
  tasks:
    - name: Generate AVD Structured Configurations and Fabric Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_designs

    - name: Generate Device Configurations and Documentation
      ansible.builtin.import_role:
        name: arista.avd.eos_cli_config_gen
```

For Containerlab, `digital_twin.fabric` is still required for schema validation, even if it is left empty as `fabric: {}`. This is a temporary limitation and it will be removed once the shared Digital Twin schema is updated.

Limitations of the current Containerlab implementation:

- It is a `PREVIEW` feature and behavior may still change.
- Only out-of-band management is supported.
- Only `Management1` is supported as the management interface. This is the recommended default, and the management interface is not currently configurable.
- Only a single IPv4 management subnet is supported across the lab.
- Deploying multiple Containerlab Digital Twin topologies on the same host is not supported. The management network name is fixed to `custom_mgmt` and is not configurable. Sharing this network across topologies can cause management IP address collisions when subnets match, or deployment failures when subnets differ. Use a clean lab environment with only one topology deployed at a time.
- Management IP addresses in the lab and production must currently match.
- Each node must have a static `mgmt_ip`. Unset management IPs and `mgmt_ip: dhcp` are not supported.
- `digital_twin.mgmt_ip` is not currently used by the Containerlab topology generator. Instead, topology generation uses each node's `mgmt_ip` value from the AVD fabric facts.
- The generated topology includes fabric nodes and point-to-point fabric links. Connected endpoints and non-point-to-point links are not modeled.
- The generated topology sets `prefix: ""` intentionally to preserve the original AVD hostnames.
- The generated topology currently defaults to `arista_ceos` with `image: arista/ceos:latest`. Please set up your lab environment accordingly, or update the generated topology file if needed.

!!! warning
    Make sure your lab environment is isolated from production. The management addresses are reused, so take the necessary precautions to avoid pushing configurations to the wrong environment.

The generated topology file is written to the parent of `output_dir` as `{{ output_dir | dirname }}/{{ fabric_name }}-topology.clab.yml`, independently of `documentation_dir`.
The `interface_mapping.json` file is written beside the topology and mounted by each node using a path relative to the topology file.
EOS startup configurations are generated by `eos_cli_config_gen` in `eos_config_dir` (default: `{{ output_dir }}/configs`) as `<hostname>.cfg`.
Each node's `startup-config` path is relative to the topology file's directory and is currently fixed to `intended/configs/<hostname>.cfg`.

Example generated topology:

```yaml
---
name: FABRIC
prefix: ''
mgmt:
  network: custom_mgmt
  ipv4-subnet: 172.16.1.0/24
topology:
  defaults:
    kind: arista_ceos
  kinds:
    arista_ceos:
      enforce-startup-config: true
      image: arista/ceos:latest
      binds:
      - interface_mapping.json:/mnt/flash/EosIntfMapping.json:ro
  nodes:
    dc1-leaf1a:
      mgmt-ipv4: 172.16.1.101
      startup-config: intended/configs/dc1-leaf1a.cfg
    dc1-leaf1b:
      mgmt-ipv4: 172.16.1.102
      startup-config: intended/configs/dc1-leaf1b.cfg
    dc1-leaf1c:
      mgmt-ipv4: 172.16.1.151
      startup-config: intended/configs/dc1-leaf1c.cfg
    dc1-leaf2a:
      mgmt-ipv4: 172.16.1.103
      startup-config: intended/configs/dc1-leaf2a.cfg
    dc1-leaf2b:
      mgmt-ipv4: 172.16.1.104
      startup-config: intended/configs/dc1-leaf2b.cfg
    dc1-leaf2c:
      mgmt-ipv4: 172.16.1.152
      startup-config: intended/configs/dc1-leaf2c.cfg
    dc1-spine1:
      mgmt-ipv4: 172.16.1.11
      startup-config: intended/configs/dc1-spine1.cfg
    dc1-spine2:
      mgmt-ipv4: 172.16.1.12
      startup-config: intended/configs/dc1-spine2.cfg
  links:
  - endpoints:
    - dc1-leaf1a:eth1
    - dc1-spine1:eth1
  - endpoints:
    - dc1-leaf1a:eth2
    - dc1-spine2:eth1
  - endpoints:
    - dc1-leaf1a:eth3
    - dc1-leaf1b:eth3
  - endpoints:
    - dc1-leaf1a:eth4
    - dc1-leaf1b:eth4
  - endpoints:
    - dc1-leaf1a:eth8
    - dc1-leaf1c:eth1
  - endpoints:
    - dc1-leaf1b:eth1
    - dc1-spine1:eth2
  - endpoints:
    - dc1-leaf1b:eth2
    - dc1-spine2:eth2
  - endpoints:
    - dc1-leaf1b:eth8
    - dc1-leaf1c:eth2
  - endpoints:
    - dc1-leaf2a:eth1
    - dc1-spine1:eth3
  - endpoints:
    - dc1-leaf2a:eth2
    - dc1-spine2:eth3
  - endpoints:
    - dc1-leaf2a:eth3
    - dc1-leaf2b:eth3
  - endpoints:
    - dc1-leaf2a:eth4
    - dc1-leaf2b:eth4
  - endpoints:
    - dc1-leaf2a:eth8
    - dc1-leaf2c:eth1
  - endpoints:
    - dc1-leaf2b:eth1
    - dc1-spine1:eth4
  - endpoints:
    - dc1-leaf2b:eth2
    - dc1-spine2:eth4
  - endpoints:
    - dc1-leaf2b:eth8
    - dc1-leaf2c:eth2
```

From the root directory containing `digital_twin/`, launch the generated topology with:

```bash
containerlab deploy -t "digital_twin/<FABRIC_NAME>-topology.clab.yml"
```
