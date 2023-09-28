<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state - Preview Intergration with ANTA

!!! warning
    eos_validate_state intergration with ANTA is in preview. Everything is subject to change.
    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)

## Overview

**eos_validate_state** is a role leveraged to validate Arista EOS devices' operational states.

**eos_validate_state** role:

- Consumes structured EOS configuration file, the same input as the role [eos_cli_config_gen](../eos_cli_config_gen). This input is considered the source of truth (the desired state).
- Connects to EOS devices to collect operational states (actual state). This requires access to the configured devices.
- Compares the actual states against the desired state.
- Generates CSV and Markdown reports of the results.

## Known limitations

- Loose mode to ignore playbook errors is no longer supported in ANTA mode.

## Expected changes

- You should expect faster execution, and if not please report on the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)
- Hardware tests are now collapsed.
- Some description of tests have been updated to be more precise.
- Sorting of the test results is now done per device as opposed to per category.

## How to run eos_validate_state in ANTA mode

- Install anta v0.9.0: `pip install anta==v0.9.0`

- Run eos_validate_state playbook with `anta` tag i.e `--tags anta`.

  Example: `ansible-playbook playbooks/fabric-validate.yaml --tags anta`

  Not providing the `anta` tag will run the current `eos_validate_state` leveraging Ansible asserts.

- Legacy Ansible tags are also supported if you want to run/skip tests:

  Example: `ansible-playbook playbooks/fabric-validate.yaml --tags anta,routing_table`

- You can now run the eos_validate_state role in check_mode. This will produce a report of tests that will be performed.

  Example: `ansible-playbook playbooks/fabric-validate.yaml --check`

## Test Categories

- AvdTestHardware
  - VerifyEnvironmentPower: Validate environment power supplies status.
  - VerifyEnvironmentCooling: Validate environment fan status.
  - VerifyTemperature: Validate environment temperature.
  - VerifyTransceiversManufacturers: Validate transceivers manufacturer.

- AvdTestNTP
  - VerifyNTP: Validate NTP status.

- AvdTestInterfacesState
  - VerifyInterfacesStatus: Validate interfaces admin and operational status.
    - Ethernet interfaces
    - Port-channel interfaces
    - Vlan interfaces
    - Loopback interfaces
    - Vxlan1 interface

- AvdTestP2PIPReachability
  - VerifyReachability: Validate IP reachability for point-to-point l3 ethernet interfaces.

- AvdTestInbandReachability
  - VerifyReachability: Validate loopback reachability between devices.

- AvdTestLoopback0Reachability
  - VerifyReachability: Validate loopback reachability between devices.

- AvdTestLLDPTopology
  - VerifyLLDPNeighbors: Validate LLDP topology.

- AvdTestMLAG
  - VerifyMlagStatus: Validate MLAG status.

- AvdTestRoutingTable
  - VerifyRoutingTableEntry: Validate remote Loopback0 address and source interface for Vxlan1 interface are in the routing table.

- AvdTestBGP
  - VerifyBGPSpecificPeers: Validate IP BGP and BGP EVPN sessions state.
  - VerifyRoutingProtocolModel: Validate ArBGP is configured and operating.

- AvdTestReloadCause
  - VerifyReloadCause: Validate last reload cause. (Optional)

## Input variables

```yaml
# Format for path to r/w reports. Sync with default values configured in arista.avd.build_output_folders
root_dir: '{{ inventory_dir }}'
eos_validate_state_name: 'reports'
eos_validate_state_dir: '{{ root_dir }}/{{ eos_validate_state_name }}'

# Reports name
eos_validate_state_md_report_path: '{{ eos_validate_state_dir }}/{{ fabric_name }}-state.md'
eos_validate_state_csv_report_path: '{{ eos_validate_state_dir }}/{{ fabric_name }}-state.csv'

# Markdown flavor to support non-text rendering
# Only support default and github
validate_state_markdown_flavor: "default"

# The variable `skipped_tests` can be used for running/skipping tests

skipped_tests:
    AvdTestHardware:

# You can also decide to skip specific subtests (ANTA test) for more granularity

skipped_tests:
    AvdTestHardware:
        - VerifyTransceiversTemperature

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
```
