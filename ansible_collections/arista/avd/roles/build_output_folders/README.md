---
# This title is used for search results
title: Ansible Collection Role build_output_folders
---
<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# build_output_folders

Role to cleanup and create local folder structure to save roles' outputs

## Requirements

None

## Role Variables

The role supports the following collection-wide variables:

```yaml
# Root directory where to build output structure
# All folder below will be created in this directory folder.
avd_root_dir: "{{ inventory_dir }}"

# Main output directory
avd_output_dir_name: "intended"
# Output for structured YAML files:
avd_structured_dir_name: "structured_configs"
# EOS configuration directory name
avd_eos_config_dir_name: "configs"
# Main documentation folder
avd_documentation_dir_name: "documentation"
# Fabric documentation
avd_fabric_dir_name: "fabric"
# Device documentation
avd_devices_dir_name: "devices"
# EOS config deploy eapi running config backup directory
avd_post_running_config_backup_dir_name: "config_backup"
avd_pre_running_config_backup_dir_name: "config_backup"
```

Existing unprefixed inputs remain supported silently. If both names are set, the
`avd_*` value wins. Use the `avd_*` paths when consuming the output from another role.

Role will create following structure:

```shell
├── config_backup
├── documentation
│   ├── fabric
│   └── devices
├── intended
│   ├── configs
│   └── structured_configs
├── reports

```

If folders already exists, role will delete them and recreate structure.

## Dependencies

None

## Example Playbook

Below is an example to use in your playbook to build output folders using default values.

```yaml
- name: Build Switch configuration
  hosts: DC1_FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: 'Build local folders for output'
      ansible.builtin.import_role:
        name: arista.avd.build_output_folders
```

## License

Project is published under [Apache 2.0 License](https://github.com/aristanetworks/avd/blob/devel/LICENSE)
