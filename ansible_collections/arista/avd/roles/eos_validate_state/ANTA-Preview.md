---
# This title is used for search results
title: Ansible Collection Role eos_valudate_state - Preview Integration with ANTA
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state - Preview Integration with ANTA

!!! warning
    eos_validate_state intergration with ANTA is in preview. Everything is subject to change.
    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)

## Overview

**eos_validate_state** is a role leveraged to validate Arista EOS devices' operational states.

**eos_validate_state** role:

- Consumes structured EOS configuration file, the same input as the role [eos_cli_config_gen](../eos_cli_config_gen/README.md). This input is considered the source of truth (the desired state).
- Connects to EOS devices to collect operational states (actual state). This requires access to the configured devices.
- Compares the actual states against the desired state.
- Generates CSV and Markdown reports of the results.

## Known limitations

- Loose mode to ignore playbook errors is no longer supported in ANTA mode.
- ANTA mode exclusively supports the newer "list-of-dicts" data models in the structured configuration file input. For further details, consult the AVD 4.x.x [porting guides](https://avd.sh/en/stable/docs/porting-guides/4.x.x.html#data-model-changes-from-dict-of-dicts-to-list-of-dicts).

## Expected changes

- You should expect faster execution, and if not please report on the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)
- Hardware tests are now collapsed.
- Some description of tests have been updated to be more precise.
- Sorting of the test results is now done per device as opposed to per category.
- All tests will be skipped for a device flagged as undeployed using the host level variable [`is_deployed: false`](https://avd.sh/en/stable/roles/eos_designs/docs/input-variables.html#flagging-a-device-as-not-deployed). Additionally, all tests take into account the `is_deployed` variable value and skip tests accordingly.
- BGP tests will only run if `service_routing_protocols_model` is set to `multi-agent` in the structured configuration file.

!!! note
    Starting from version 4.30.1F, `service_routing_protocols_model` is preset to `multi-agent` by default on EOS devices.

## How to run eos_validate_state in ANTA mode

- Install the "anta" Python package (this is *not* part of the `requirements.txt`):

  ```shell
  pip3 install '
  --8<-- "roles/eos_validate_state/preview_requirements.txt:4:4"
  '
  ```

- Run eos_validate_state playbook by setting the variable `use_anta=true`.

  This can be set for instance in your group_vars or under the task in your playbook.

  If you `use_anta=false` which is the default, the current version of `eos_validate_state` leveraging Ansible asserts will be run.

- Ansible tags are supported for backwards compatibility until AVD version 5.0.0.
  To run/skip tests use `--tags` or `--skip-tags`.

  ```shell
  ansible-playbook playbooks/fabric-validate.yaml --tags routing_table
  ```

- You can now run the eos_validate_state role in check_mode. This will produce a report of tests that will be performed without running the tests on your network.

  ```shell
  ansible-playbook playbooks/fabric-validate.yaml --check
  ```

- You have the option to save the test catalog generate by the role for each device in the `intended/test_catalogs` folder by setting the variable `save_catalog` to `true`.

## Test Categories

- AvdTestHardware (Ansible tags: `hardware`, `platform_information`)
  - VerifyEnvironmentPower: Validate environment power supplies status.
  - VerifyEnvironmentCooling: Validate environment fan status.
  - VerifyTemperature: Validate environment temperature.
  - VerifyTransceiversManufacturers: Validate transceivers manufacturer.

- AvdTestNTP (Ansible tags: `ntp`)
  - VerifyNTP: Validate NTP status.

- AvdTestInterfacesState (Ansible tags: `interfaces_state`)
  - VerifyInterfacesStatus: Validate interfaces admin and operational status.
    - Ethernet interfaces
    - Port-channel interfaces
    - Vlan interfaces
    - Loopback interfaces
    - Vxlan1 interface

- AvdTestP2PIPReachability (Ansible tags: `ip_reachability`)
  - VerifyReachability: Validate IP reachability for point-to-point l3 ethernet interfaces.

- AvdTestInbandReachability (Ansible tags: `loopback_reachability`, `loopback0_reachability`, `optional`)
  - VerifyReachability: Validate loopback reachability between devices.

- AvdTestLoopback0Reachability (Ansible tags: `loopback_reachability`, `loopback0_reachability`)
  - VerifyReachability: Validate loopback reachability between devices.

- AvdTestLLDPTopology (Ansible tags: `lldp_topology`)
  - VerifyLLDPNeighbors: Validate LLDP topology.

- AvdTestMLAG (Ansible tags: `mlag`)
  - VerifyMlagStatus: Validate MLAG status.

- AvdTestRoutingTable (Ansible tags: `routing_table`)
  - VerifyRoutingTableEntry: Validate remote Loopback0 address and source interface for Vxlan1 interface are in the routing table.

- AvdTestBGP (Ansible tags: `bgp_check`)
  - VerifyBGPSpecificPeers: Validate IP BGP and BGP EVPN sessions state.
  - VerifyRoutingProtocolModel: Validate ArBGP is configured and operating.

- AvdTestReloadCause (Ansible tags: `reload_cause`, `optional`, `never`)
  - VerifyReloadCause: Validate last reload cause. (Optional)

## Input variables

```yaml
# Format for path to r/w reports. Sync with default values configured in arista.avd.build_output_folders
root_dir: '{{ inventory_dir }}'

# AVD configurations output
# Main output directory
output_dir_name: 'intended'
output_dir: '{{ root_dir }}/{{ output_dir_name }}'

# Output for test catalog YAML files if save_catalog is set to true
test_catalogs_dir_name: 'test_catalogs'
test_catalogs_dir: '{{ output_dir }}/{{ test_catalogs_dir_name }}'

# Output directory for eos_validate_state reports
eos_validate_state_name: 'reports'
eos_validate_state_dir: '{{ root_dir }}/{{ eos_validate_state_name }}'

# Reports name
eos_validate_state_md_report_path: '{{ eos_validate_state_dir }}/{{ fabric_name }}-state.md'
eos_validate_state_csv_report_path: '{{ eos_validate_state_dir }}/{{ fabric_name }}-state.csv'

# Markdown flavor to support non-text rendering
# Only support default and github
validate_state_markdown_flavor: "default"

# The variable `skipped_tests` can be used for running/skipping tests categories
skipped_tests:
  - category: AvdTestHardware

# You can also decide to skip specific subtests (ANTA test name) for more granularity
skipped_tests:
  - category: AvdTestBGP
    tests:
      - VerifyRoutingProtocolModel
  - category: AvdTestHardware
    tests:
      - VerifyEnvironmentCooling

# Fabric Name, required to match Ansible Group name covering all devices in the Fabric | Required and **must** be an inventory group name.
fabric_name: "all"

# Allow different manufacturers
accepted_xcvr_manufacturers: "{{ validation_role.xcvr_own_manufacturers | arista.avd.default(['Arastra, Inc.', 'Arista Networks']) }}"

# Allow different states for power supplies
accepted_pwr_supply_states: "{{ validation_role.pwr_supply_states | arista.avd.default(['ok']) }}"

# Allow different states for fans
accepted_fan_states: "{{ validation_role.fan_states | arista.avd.default(['ok']) }}"

# Generate CSV results file
validation_report_csv: "{{ validation_role.validation_report_csv | arista.avd.default(true) }}"

# Generate MD results file
validation_report_md: "{{ validation_role.validation_report_md | arista.avd.default(true) }}"

# Print only FAILED tests
only_failed_tests: "{{ validation_role.only_failed_tests | arista.avd.default(false) }}"

# Variable to enable ANTA eos_validate_state
# Defaults to false as ANTA is currently preview
use_anta: false
# Whether or not to save each device test catalog to 'test_catalogs_dir'
# Used only when 'use_anta' is set to true
save_catalog: false
# Which tests to skip when using ANTA.
# If set, Ansible tags are ignored
skipped_tests: []
# Logging level for the ANTA libraries
# Default is warning
logging_level: "WARNING"
```

## Example Playbook

```yaml
---
- name: validate states on EOS devices using ANTA
  hosts: DC1
  gather_facts: false
  tasks:
    - name: validate states on EOS devices
      ansible.builtin.import_role:
        name: arista.avd.eos_validate_state
      vars:
        # To enable ANTA
        use_anta: true
        # To save catalogs
        save_catalog: true
```
