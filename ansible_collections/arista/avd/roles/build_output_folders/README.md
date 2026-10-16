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

!!! warning "Deprecated in AVD 6.5.0"

    The `arista.avd.build_output_folders` role is deprecated and will be removed in AVD 7.0.0.
    AVD roles create their required output directories. See [Migration](#migration) before removing the role from your playbooks.
    The role retains its existing behavior throughout AVD 6.x.

Role to clean up and create local folder structure to save roles' outputs

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

## Dependencies

None

## Migration

Remove the `arista.avd.build_output_folders` invocation from your playbooks:

```diff
 tasks:
-  - name: Build local folders for output
-    ansible.builtin.import_role:
-      name: arista.avd.build_output_folders
   - name: Generate structured configuration
     ansible.builtin.import_role:
       name: arista.avd.eos_designs
```

The `eos_designs`, `eos_cli_config_gen`, `anta_runner`, `eos_config_deploy_eapi`, and `eos_snapshot` roles create their required output directories.
If you set `avd_create_directories: false`, enable directory creation or create the required directories in your own playbook.
Custom tasks that require additional directories, including `structured_cvp_dir`, must create those directories explicitly.

### Variables and custom paths

Review any variables previously supplied by this role's defaults. Set variables needed by custom tasks explicitly in your inventory or playbook.
Keep shared path overrides such as `root_dir`, `output_dir`, `structured_dir`, and `documentation_dir` in inventory or playbook variables so that
all consuming roles use the same paths. Move overrides passed only to the removed role invocation to the appropriate shared scope.

### Cleanup of existing outputs

Removing the role also removes its cleanup steps. Existing files, including outputs for devices removed from inventory, may remain on disk.
If your workflow requires a clean build, add explicit cleanup before generating outputs. Limit cleanup to the generated output paths used by your workflow.
For example, with the default output path:

```yaml
- name: Remove previous intended outputs
  ansible.builtin.file:
    path: "{{ inventory_dir }}/intended"
    state: absent
  delegate_to: localhost
  run_once: true
```

Use your configured `output_dir` instead if you override the default path. Keep directory creation enabled in consuming roles after cleanup.

For ANTA, explicitly remove generated catalogs and reports when a clean run is required. Use your configured `avd_catalogs_dir` and
`anta_reports_dir` paths, and preserve `user_catalogs_dir` and any user-provided catalog files. The old role also deleted other subdirectories
of `anta_dir` apart from the directory named `user_catalogs_dir_name`; decide which of those require cleanup in your workflow.
If user catalogs are stored inside `output_dir`, preserve them before cleaning that directory.

## License

Project is published under [Apache 2.0 License](https://github.com/aristanetworks/avd/blob/devel/LICENSE)
