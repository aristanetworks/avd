<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_validate_state - Preview Intergration with ANTA

!!! warning
    eos_validate_state intergration with ANTA is in preview. Everything is subject to change.
    If you have any questions, please leverage the GitHub [discussions board](https://github.com/aristanetworks/ansible-avd/discussions)

## Known limitations

- Loose mode is no longer supported in ANTA mode.

## How to run eos_validate_state in ANTA mode

- Install anta v0.9.0: `pip install anta>v0.9.0`

- Run eos_validate_state playbook with `anta` tag i.e `--tags anta`.
  Example: `ansible-playbook playbooks/fabric-validate.yaml --tags anta`
  Not providing the `anta` tag will run the regular `eos_validate_state`

- Legacy Ansible tags are also supported if you want to run/skip tests:
`ansible-playbook playbooks/fabric-validate.yaml --tags anta,routing_table`

## Test Categories

- AvdTestP2PIPReachability
  - VerifyReachability
- AvdTestInbandReachability
  - VerifyReachability
- AvdTestLoopback0Reachability
  - VerifyReachability
- AvdTestLLDPTopology
  - VerifyLLDPNeighbors
- AvdTestHardware
  - VerifyEnvironmentPower
  - VerifyEnvironmentCooling
  - VerifyTemperature
  - VerifyTransceiversManufacturers
- AvdTestInterfacesState
  - VerifyInterfacesStatus
- AvdTestMLAG
  - VerifyMlagStatus
- AvdTestRoutingTable
  - VerifyRoutingTableEntry
- AvdTestBGP
  - VerifyBGPSpecificPeers
  - VerifyRoutingProtocolModel
- AvdTestNTP
  - VerifyNTP
- AvdTestReloadCause
  - VerifyReloadCause

## Input variables

The variable `skipped_tests` can now be used for running/skipping tests:

```yaml
skipped_tests:
    AvdTestHardware:
```

You can also decide to skip specific subtests (ANTA test) for more granularity:

```yaml
skipped_tests:
    AvdTestHardware:
        - VerifyTransceiversTemperature
```
