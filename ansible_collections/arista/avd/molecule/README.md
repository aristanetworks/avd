# AVD Unit test

This section provides a list of AVD scenario executed during Continuous Integration to validate AVD integration.

- [AVD Unit test](#avd-unit-test)
  - [Ansible molecule](#ansible-molecule)
  - [Scenario](#scenario)
  - [How to use scenario](#how-to-use-scenario)
    - [Which file to update](#which-file-to-update)
      - [If you are updating `eos_cli_config_gen`](#if-you-are-updating-eos_cli_config_gen)
      - [If you are updating `eos_l3ls_evpn`](#if-you-are-updating-eos_l3ls_evpn)

## Ansible molecule

Molecule provides support for testing with multiple instances, operating systems and distributions, virtualization providers, test frameworks and testing scenarios. Molecule encourages an approach that results in consistently developed roles that are well-written, easily understood and maintained.

## Scenario

Current molecule implementation provides following scenario:

- `eos_l3ls_evpn` with standard eBGP as underlay and overlay: [evpn_underlay_ebgp_overlay_ebgp](./evpn_underlay_ebgp_overlay_ebgp/molecule.yml)
- `eos_l3ls_evpn` with standard OSPF as underlay and eBGP overlay: [evpn_underlay_ospf_overlay_ebgp](./evpn_underlay_ospf_overlay_ebgp/molecule.yml)
- `eos_cli_config_gen` scenario to run unit test

## How to use scenario

Molecule scenario are used to validate role execution and coverage of data-model. When you update a role or data-model, scenario must be updated to reflect your changes and validate it is not breaking other supported scenario.

```bash
# Go to test folder
$ cd ansible_collections/arista/avd

# Edit molecule scenario
$ vim <molecule-file>

# Run testing
$ molecule test --scenario-name < scenario-name >

# Cleanup your environment
$ molecule cleanup --scenario-name < scenario-name >
```

### Which file to update

#### If you are updating `eos_cli_config_gen`

Testing for `eos_cli_config_gen` is part of [scenario `eos_cli_config_gen`](./eos_cli_config_gen/molecule.yml). It is based on a in flat inventory with 1 host covering a specific section of templates like:

- Ethernet Interfaces defined in [host_vars/ethernet_interfaces](./eos_cli_config_gen/inventory/host_vars/ethernet_interfaces.yml)
- Loopback Interfaces defined in [host_vars/ethernet_interfaces](./eos_cli_config_gen/inventory/host_vars/loopbacks.yml)
- Vlans defined in [host_vars/ethernet_interfaces](./eos_cli_config_gen/inventory/host_vars/vlans.yml)

[ ... to be continued ... ]

Edit files based on your own change to implement your own testing.

#### If you are updating `eos_l3ls_evpn`

[ TO BE DONE ]
