# AVD Unit test

This section provides a list of AVD scenarios executed during Continuous Integration to validate AVD integration.

- [AVD Unit test](#avd-unit-test)
  - [Ansible molecule](#ansible-molecule)
  - [Scenario](#scenario)
  - [E2E-only projects](#e2e-only-projects)
  - [How to use scenario](#how-to-use-scenario)
    - [Which file to update](#which-file-to-update)
      - [If you are updating `eos_cli_config_gen`](#if-you-are-updating-eos_cli_config_gen)
      - [If you are updating `eos_designs`](#if-you-are-updating-eos_designs)
        - [Update related to underlay or overlay protocol](#update-related-to-underlay-or-overlay-protocol)
        - [General eos\_designs update](#general-eos_designs-update)

## Ansible molecule

Molecule provides support for testing with multiple instances, operating systems and distributions, virtualization providers, test frameworks and testing scenarios. Molecule encourages an approach that results in consistently developed roles that are well-written, easily understood and maintained.

## Scenario

CI runs the following Molecule scenarios for Ansible integration:

- ansible_only
- anta_runner
- digital_twin_containerlab
- digital_twin_containerlab_negative_tests
- eos_cli_config_gen
- eos_cli_config_gen_deprecated_vars
- example-cv-pathfinder
- howto

## E2E-only projects

The following projects retain their location under this directory during the transition to PyAVD E2E testing. Run them with the [PyAVD E2E tool](../../../../../docs/contribution/e2e-test/using-the-tool.md#run-selected-projects):

- [digital_twin](./digital_twin/): Regular and ACT Digital Twin generation.
- [eos_designs_deprecated_vars](./eos_designs_deprecated_vars/): Deprecated design inputs and generated artifacts.
- [eos_designs-l2ls](./eos_designs-l2ls/): L2 leaf-spine designs.
- [eos_designs-mpls-isis-sr-ldp](./eos_designs-mpls-isis-sr-ldp/): MPLS designs using IS-IS, segment routing, and LDP.
- [eos_designs-twodc-5stage-clos](./eos_designs-twodc-5stage-clos/): Two-datacenter five-stage Clos designs and Digital Twin outputs.
- [evpn_underlay_ebgp_overlay_ebgp](./evpn_underlay_ebgp_overlay_ebgp/): EVPN with eBGP underlay and overlay.
- [evpn_underlay_isis_overlay_ibgp](./evpn_underlay_isis_overlay_ibgp/): EVPN with IS-IS underlay and iBGP overlay.
- [evpn_underlay_ospf_overlay_ebgp](./evpn_underlay_ospf_overlay_ebgp/): EVPN with OSPF underlay and eBGP overlay.
- [evpn_underlay_rfc5549_overlay_ebgp](./evpn_underlay_rfc5549_overlay_ebgp/): EVPN with RFC 5549 underlay and eBGP overlay.
- [eos_cli_config_gen_negative_unit_tests](./eos_cli_config_gen_negative_unit_tests/): EOS structured configuration validation and CLI rendering failures.
- [eos_designs_negative_unit_tests](./eos_designs_negative_unit_tests/): AVD design validation and generation failures.
- [eos_designs_unit_tests](./eos_designs_unit_tests/): AVD design facts, structured configuration, and EOS configuration artifacts.

The example projects below run through their existing E2E configurations under `examples/`; their former `example-*` Molecule wrappers have been removed:

- [campus-fabric](../../examples/campus-fabric/)
- [dual-dc-l3ls](../../examples/dual-dc-l3ls/)
- [isis-ldp-ipvpn](../../examples/isis-ldp-ipvpn/)
- [l2ls-fabric](../../examples/l2ls-fabric/)
- [single-dc-l3ls](../../examples/single-dc-l3ls/)
- [single-dc-l3ls-ipv6](../../examples/single-dc-l3ls-ipv6/)
- [single-dc-multipod-l3ls](../../examples/single-dc-multipod-l3ls/)

Run `make e2e` from the repository root to regenerate all E2E projects. The local `refresh-facts` target uses `MOLECULE_SCENARIOS.txt` and only runs the remaining listed Molecule scenarios.

When migrating another project to E2E-only execution, remove its Molecule wrappers and registry entry, and document its E2E location here.

## How to use scenario

Molecule scenarios validate Ansible role execution and integration behavior. E2E projects validate the data model and generated artifacts. Update the relevant tests when changing either layer.

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

Testing for `eos_cli_config_gen` is part of [scenario `eos_cli_config_gen`](./eos_cli_config_gen/molecule.yml). It is based on a flat inventory with 1 host covering a specific section of templates like:

- Ethernet Interfaces defined in [host_vars/ethernet_interfaces](./eos_cli_config_gen/inventory/host_vars/ethernet-interfaces.yml)
- Loopback Interfaces defined in [host_vars/loopback-interfaces](./eos_cli_config_gen/inventory/host_vars/loopbacks-interfaces.yml)
- Vlans defined in [host_vars/vlans](./eos_cli_config_gen/inventory/host_vars/vlans.yml)

When you update a template in `eos_cli_config_gen`, you should report a test case in molecule scenario [`ansible_collections/arista/avd/extensions/molecule/eos_cli_config_gen`](./eos_cli_config_gen/).

1. Create or update a file related to updated section under `inventory/host_vars`

2. If the section is new, update the inventory file ([hosts.yml](eos_cli_config_gen/inventory/hosts.yml)) to add a new host. The host SHALL be the name of your section and also the `<filename>.yml` in your `host_vars`

3. Run molecule scenario to generate artifacts:

    ```bash
    # Move to AVD collection
    $ cd ansible_collections/arista/avd/

    # Run molecule
    $ molecule test --scenario-name eos_cli_config_gen
    ```

4. Commit artifacts. They will be used by CI to validate there is no change in the future.

```bash
git commit -m 'Upload artefact for issue #...' molecule/eos_cli_config_gen
```

> If you have `prek` enabled, use `--no-verify` trigger to avoid any content change in your commit

#### If you are updating `eos_designs`

##### Update related to underlay or overlay protocol

Update the closest existing E2E project, such as `evpn_underlay_ebgp_overlay_ebgp`, `evpn_underlay_isis_overlay_ibgp`, or `eos_designs-mpls-isis-sr-ldp`. These directories contain inventories and intended artifacts, but no longer contain Molecule scenarios.

##### General eos_designs update

Update the appropriate E2E project's inventory and regenerate its artifacts from the repository root, for example:

```shell
uv run --no-project tools/e2e-test-avd.py \
  ansible_collections/arista/avd/extensions/molecule/evpn_underlay_ebgp_overlay_ebgp
```

Inspect the generated diagnostics and complete Git diff, including added and deleted artifacts. Captured build failures do not necessarily produce a nonzero exit status. See the [E2E instructions](../../../../../docs/contribution/e2e-test/using-the-tool.md) for selecting projects, adding cases, and reviewing results.

For changes to Ansible-specific behavior, use the remaining Molecule scenarios or focused [Ansible integration tests](../../../../../docs/contribution/development-tooling.md#ansible-test).
