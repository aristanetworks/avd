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

Create and clean up the local directory structure used to store AVD role outputs.

## Requirements

None

## Role Variables

The role supports the following variables:

```yaml
# Root directory where to build output structure
# All folders below will be created in this directory.
avd_root_dir: '{{ inventory_dir }}'

# Main output directory
avd_output_dir_name: "intended"
# Output for structured YAML files:
avd_structured_dir_name: 'structured_configs'
# Output for CloudVision structured YAML files:
avd_structured_cvp_dir_name: 'cvp'
# EOS configuration directory name
avd_eos_config_dir_name: "configs"
# Main documentation folder
avd_documentation_dir_name: "documentation"
# Fabric documentation
avd_fabric_dir_name: "fabric"
# Device documentation
avd_devices_dir_name: "devices"
# EOS config deploy eapi running config backup directory
avd_post_running_config_backup_dir_name: 'config_backup'
avd_pre_running_config_backup_dir_name: 'config_backup'
# EOS snapshots
avd_snapshots_backup_dir_name: 'snapshots'
# ANTA catalogs and reports
avd_anta_dir_name: 'anta'
avd_user_catalogs_dir_name: 'user_catalogs'
avd_catalogs_dir_name: 'avd_catalogs'
avd_anta_reports_dir_name: 'reports'
```

Existing unprefixed inputs remain supported silently. If both names are set, the
`avd_*` value wins. Use the `avd_*` paths when consuming the output from another role.

With the default paths, the role creates the following structure:

```shell
├── anta
│   ├── avd_catalogs
│   ├── reports
│   └── user_catalogs
├── config_backup
├── documentation
│   ├── fabric
│   └── devices
├── intended
│   ├── configs
│   └── structured_configs
│       └── cvp
└── snapshots
```

The role deletes and recreates `avd_output_dir`. It also deletes subdirectories of `avd_anta_dir`, except for the directory named
`avd_user_catalogs_dir_name`. It creates the other directories if missing and preserves their existing contents.
With the default paths, documentation, configuration backups, snapshots, and ANTA user catalogs are preserved.
When overriding paths, keep files you want to preserve outside the directories that the role cleans.

The role delegates filesystem operations to `localhost` and uses `run_once` to execute each task once per inventory batch.
Use the same output paths for all hosts in a batch.

## Dependencies

None

## Example Playbook

```yaml
- name: Build Switch configuration
  hosts: DC1_FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: Build local folders for output
      ansible.builtin.import_role:
        name: arista.avd.build_output_folders
```

## License

Project is published under [Apache 2.0 License](https://github.com/aristanetworks/avd/blob/devel/LICENSE)
