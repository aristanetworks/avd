<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Semantic Versioning

The AVD project follows Semantic Versioning ([SemVer](https://semver.org/)).
This document describes what attributes and APIs are stable and follow SemVer and which ones may change between minor releases.

## Ansible Roles

### eos_designs

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months before being removed.

Outputs:

- eos_designs `structured_configuration` may change between minor releases.
  - Structure config can change to use new keys when keys are deprecated in the eos_cli_config_gen role.
  - The resulting EOS configuration generated from eos_cli_config_gen will be maintained, unless in rare cases when addressing a bug.
  - Breaking changes will be communicated in the release notes.
- Fabric documentation artifacts may change between minor releases.
  - Breaking changes to YAML/JSON/CSV outputs will be communicated in the release notes.

### eos_cli_config_gen

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- EOS configuration generated from eos_cli_config_gen follows SemVer.
  - Breaking changes may occur in rare cases when addressing a bug.
  - Reordering of the CLI output may occur but with no impact on the resulting configuration on EOS.
- Device documentation artifacts may change during minor releases.

### cvp_configlet_upload

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

### eos_config_deploy_cvp

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- Structured configuration output may change during minor releases, to accommodate changes in the ansible-cvp collection.
- The resulting CloudVision configuration will be maintained, unless in rare cases when addressing a bug.
  - Breaking changes will be communicated in the release notes.

### eos_config_deploy_eapi

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- All role outputs follow SemVer.

### eos_validate_state

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- The generated reports and other artifacts may change between minor releases.
  - Breaking changes to YAML/JSON/CSV outputs will be communicated in the release notes.

### dhcp_provisioner

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- Structured configuration output may change during minor releases, to accommodate changes in the ansible-cvp collection.
- The resulting DHCP configuration will be maintained, unless in rare cases when addressing a bug.
  - Breaking changes will be communicated in the release notes.

### build_output_folders

Inputs:

- All role input variables follow SemVer.
  - Any breaking changes will at a minimum be communicated with a deprecation notice for 6 months.
  - Keys will then be documented as removed in the next major release.

Outputs:

- All role ouptus follow SemVer.

## Ansible Plugins

- All Ansible modules, action plugins, filter plugins, test plugins or vars plugins are not covered by SemVer.
  - Functionality may change in minor releases, to accommodate the project's needs.
  - Breaking changes will be communicated in the release notes.
