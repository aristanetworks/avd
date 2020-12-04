# AVD Unit test

This section provides a list of AVD scenario executed during Continuous Integration to validate AVD integration.

- [AVD Unit test](#avd-unit-test)
  - [Ansible molecule](#ansible-molecule)
  - [Scenario](#scenario)
  - [How to use scenario](#how-to-use-scenario)
    - [Which file to update](#which-file-to-update)
      - [If you are updating `eos_cli_config_gen`](#if-you-are-updating-eos_cli_config_gen)
      - [If you are updating `eos_l3ls_evpn`](#if-you-are-updating-eos_l3ls_evpn)
        - [Update related to underlay or overlay protocol](#update-related-to-underlay-or-overlay-protocol)
        - [General l3ls_evpn update](#general-l3ls_evpn-update)

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
$ vim molecule/<scenario-name>/<molecule-file>

# Run testing
$ molecule test --scenario-name <scenario-name>

# Cleanup your environment
$ molecule cleanup --scenario-name <scenario-name>
```

### Which file to update

#### If you are updating `eos_cli_config_gen`

Testing for `eos_cli_config_gen` is part of [scenario `eos_cli_config_gen`](./eos_cli_config_gen/molecule.yml). It is based on a in flat inventory with 1 host covering a specific section of templates like:

- Ethernet Interfaces defined in [host_vars/ethernet_interfaces](./eos_cli_config_gen/inventory/host_vars/ethernet_interfaces.yml)
- Loopback Interfaces defined in [host_vars/loopback-interfaces](./eos_cli_config_gen/inventory/host_vars/loopbacks.yml)
- Vlans defined in [host_vars/vlans](./eos_cli_config_gen/inventory/host_vars/vlans.yml)

When you update a template in `eos_cli_config_gen`, you should report a test case in molecule scenario [`ansible_collections/arista/avd/molecule/eos_cli_config_gen`](./eos_cli_config_gen/).

1. Create or update a file related to updated section under `inventory/host_vars`
2. If section is new, update inventory file to add a new host. Host SHALL be the name of your section and also file in your `host_vars`
3. Run molecule scenario to generate artifacts:

```bash
# Move to AVD collection
$ cd ansible_collections/arista/avd/

# Run molecule
$ molecule test --scenario-name eos_cli_config_gen
```

4. Commit artifacts. They will be used by CI to validate their is no change in the future.

```bash
$ git commit -m 'Upload artefact for issue #...' molecule/eos_cli_config_gen
```

> If you have `pre-commit` enabled, use `--no-verify` trigger to avoid any content change in your commit

#### If you are updating `eos_l3ls_evpn`

##### Update related to underlay or overlay protocol

In such case, copy an existing scenario to create a new one:

```bash
# Move to AVD collection
$ cd ansible_collections/arista/avd/

# Run Molecule scenario
$ molecule test --scenario-name eos_cli_config_gen
```

##### General l3ls_evpn update

If your update is not related to underlay or overlay protocol, edit scenario `evpn_underlay_ebgp_overlay_ebgp` and edit group_vars accordingly. Then run molecule to validate it is working as expected

1. Create your scenario

```bash
# Move to AVD collection
$ cd ansible_collections/arista/avd/

# Copy existing molecule scenario
$ cp -r molecule/evpn_underlay_isis_overlay_ebgp molecule/evpn_underlay_<underlay-protocol>_overlay_<overlay-protocol>
```

2. Edit files from your scenario's inventory

```bash
$ cd molecule/evpn_underlay_<underlay-protocol>_overlay_<overlay-protocol>/inventory

# Edit group_vars
$ vim group_vars/DC1_FABRIC.yml
```

3. Run your molecule scenario for validation

```bash
# Move to AVD collection
$ cd ../../../

# Run Molecule scenario
$ molecule test --scenario-name evpn_underlay_<underlay-protocol>_overlay_<overlay-protocol>
```

4. Edit CI file to include your scenario

```yaml
#.github/workflows/molecule-l3ls-evpn.yml
jobs:
  molecule:
    name: Run CI test for eos_l3ls_evpn
    runs-on: ubuntu-latest
    strategy:
      fail-fast: true
      matrix:
        avd_scenario:
          - 'evpn_underlay_ebgp_overlay_ebgp'
          - 'evpn_underlay_ospf_overlay_ebgp'
          - 'evpn_underlay_isis_overlay_ebgp'
          - 'evpn_underlay_<underlay-protocol>_overlay_<overlay-protocol>'
          - 'upgrade_v1.0_to_v1.1'
```

Once you are ready, commit your change and push to Github.
