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
root_dir: '{{ inventory_dir }}'

# Main output directory
output_dir_name: 'intended'
# Output for structured YAML files:
structured_dir_name: 'structured_configs'
# Output for CloudVision structured YAML files:
structured_cvp_dir_name: 'cvp'
# EOS configuration directory name
eos_config_dir_name: 'configs'
# Main documentation folder
documentation_dir_name: 'documentation'
# Fabric documentation
fabric_dir_name: 'fabric'
# Device documentation
devices_dir_name: 'devices'
# EOS config deploy eapi running config backup directory
post_running_config_backup_dir_name: 'config_backup'
pre_running_config_backup_dir_name: 'config_backup'
# EOS snapshots
snapshots_backup_dir_name: 'snapshots'
# ANTA catalogs and reports
anta_dir_name: 'anta'
user_catalogs_dir_name: 'user_catalogs'
avd_catalogs_dir_name: 'avd_catalogs'
anta_reports_dir_name: 'reports'
```

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

The role deletes and recreates `output_dir`. It also deletes subdirectories of `anta_dir`, except for the directory named
`user_catalogs_dir_name`. It creates the other directories if missing and preserves their existing contents.
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
