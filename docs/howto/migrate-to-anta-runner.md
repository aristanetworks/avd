<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Migrating from eos_validate_state to anta_runner

This guide helps you migrate from the deprecated `arista.avd.eos_validate_state` role to the new `arista.avd.anta_runner` role.

!!! note
    The `eos_validate_state` role was deprecated in AVD 5.7 and removed in AVD 6.0.0. The `anta_runner` role provides the same functionality with additional features and improvements.

For full documentation on the `anta_runner` role, see the [anta_runner documentation](../../ansible_collections/arista/avd/roles/anta_runner/README.md).

## Quick Start

The simplest migration requires only updating the role name in your playbook:

```diff
  ---
  - name: Validate Network State
    hosts: FABRIC
    connection: local
    gather_facts: false
    tasks:
      - name: Validate states on EOS devices
        import_role:
-         name: arista.avd.eos_validate_state
+         name: arista.avd.anta_runner
```

This basic migration uses sensible defaults and will work for most use cases. However, there are some behavioral differences between the two roles. Review the sections below to understand these differences and how to achieve the same behavior as `eos_validate_state`.

## Connection Variables

The `anta_runner` role supports both standard Ansible connection variables and ANTA-specific variables. The ANTA-specific variables take precedence when both are defined:

| Standard Ansible Variable | ANTA Variable (takes precedence) |
| :--- | :--- |
| `ansible_user` | `anta_user` |
| `ansible_password` | `anta_password` |
| `ansible_become` | `anta_enable` |
| `ansible_become_password` | `anta_enable_password` |
| `ansible_httpapi_use_ssl` | `anta_use_ssl` |
| `ansible_httpapi_port` | `anta_port` |

If you were using standard Ansible connection variables with `eos_validate_state`, they will continue to work with `anta_runner`. For more details, see [Connection Options](../../ansible_collections/arista/avd/roles/anta_runner/README.md#connection-options).

## Directory Structure Changes

The output directory structure has changed:

<div class="grid" markdown>

=== "eos_validate_state"

    ```text
    inventory/
    ├── intended/
    │   ├── structured_configs/
    │   └── test_catalogs/          # Optional: saved catalogs (save_catalog: true)
    ├── custom_anta_catalogs/       # Custom catalogs
    └── reports/
        ├── test_results/           # JSON results per device
        ├── FABRIC-state.csv
        └── FABRIC-state.md
    ```

=== "anta_runner"

    ```text
    inventory/
    ├── intended/
    │   └── structured_configs/
    └── anta/
        ├── avd_catalogs/           # AVD-generated catalogs per device (always saved)
        ├── user_catalogs/          # User-defined catalogs (previously called custom catalogs)
        └── reports/
            ├── anta_report.json
            ├── anta_report.csv
            └── anta_report.md
    ```

</div>

To customize directory and report paths in `anta_runner`:

```yaml
avd_catalogs_dir: "{{ inventory_dir }}/anta/avd_catalogs"
user_catalogs_dir: "{{ inventory_dir }}/anta/user_catalogs"
anta_reports_dir: "{{ inventory_dir }}/anta/reports"
anta_report_md_path: "{{ anta_reports_dir }}/anta_report.md"
anta_report_csv_path: "{{ anta_reports_dir }}/anta_report.csv"
anta_report_json_path: "{{ anta_reports_dir }}/anta_report.json"
```

## User-Defined Catalogs

In `eos_validate_state`, custom ANTA catalogs were automatically loaded from the `custom_anta_catalogs_dir` directory. In `anta_runner`, the nomenclature has changed to *user-defined catalogs* and must be explicitly enabled:

```yaml
user_catalogs_enabled: true
```

Additionally, the device targeting mechanism has changed:

- In `eos_validate_state`, catalogs were targeted to specific devices or groups based on the **filename** (`<hostname>.yml`, `<group>.yml`, or `all.yml`).
- In `anta_runner`, all catalogs are merged together and targeting is done using **tags** in the catalog files and `anta_tags` in the Ansible inventory.

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml title="custom_anta_catalogs/DC1_LEAFS.yml"
    # Applied to all devices in DC1_LEAFS group based on filename
    anta.tests.vxlan:
      - VerifyVxlan1Interface:
    ```

=== "anta_runner"

    ```yaml title="user_catalogs/vxlan_tests.yml"
    # Tag the test to target specific devices
    anta.tests.vxlan:
      - VerifyVxlan1Interface:
          filters:
            tags: [ leaf ]
    ```

    ```yaml title="inventory.yml"
    # Assign anta_tags to devices
    all:
      children:
        DC1_LEAFS:
          hosts:
            DC1-LEAF1A:
              anta_tags: [ leaf ]
            DC1-LEAF1B:
              anta_tags: [ leaf ]
    ```

</div>

For more details on tag-based filtering, see [Tag-Based Filtering](../../ansible_collections/arista/avd/roles/anta_runner/README.md#tag-based-filtering).

## Test Filtering

The `skip_tests` variable has been replaced with `avd_catalogs_filters`. The key difference is that `anta_runner` no longer uses AVD test categories (e.g., `AvdTestHardware`, `AvdTestNTP`). Instead, you specify ANTA test class names directly (e.g., `VerifyNTP`, `VerifyEnvironmentPower`).

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    skip_tests:
      - category: AvdTestHardware
      - category: AvdTestNTP
    ```

=== "anta_runner"

    ```yaml
    avd_catalogs_filters:
      - skip_tests:
          - VerifyEnvironmentPower
          - VerifyEnvironmentCooling
          - VerifyTemperature
          - VerifyTransceiversManufacturers
          - VerifyNTP
    ```

</div>

!!! note
    The `anta_runner` role generates additional tests compared to `eos_validate_state`. If you want to match the exact test coverage of `eos_validate_state`, you can use `avd_catalogs_filters` to skip specific tests.

For a complete list of available ANTA test names, see the [AVD-generated Catalog Test Index](../../ansible_collections/arista/avd/roles/anta_runner/README.md#avd-generated-catalog-test-index). For additional filtering options, see [Test-Based Filtering](../../ansible_collections/arista/avd/roles/anta_runner/README.md#test-based-filtering).

## Logging Verbosity

In `eos_validate_state`, logging verbosity was controlled by the `logging_level` variable.

In `anta_runner`, logging verbosity is controlled by **Ansible standard verbosity flags** (`-v`, `-vv`, `-vvv`, `-vvvv`):

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    logging_level: "DEBUG"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
    ```

=== "anta_runner"

    ```shell
    # Use Ansible verbosity flags instead
    ansible-playbook playbooks/fabric-validate.yaml -vvv
    ```

</div>

For more details, see [Logging and Troubleshooting](../../ansible_collections/arista/avd/roles/anta_runner/README.md#logging-and-troubleshooting).

## Test Catalog Storage

In `eos_validate_state`, saving test catalogs was optional and controlled by `save_catalog`. When enabled, the saved catalog included both AVD-generated tests and custom catalog tests merged together.

In `anta_runner`, AVD-generated catalogs are **always** saved to the `avd_catalogs_dir` directory. Only the AVD-generated catalogs are saved, not the merged catalog that includes user-defined catalogs.

!!! note
    This is acceptable because user-defined catalogs now use tag-based targeting instead of filename-based targeting, so the merged catalog is no longer needed for debugging or inspection.

To disable AVD-generated catalogs entirely (for example, when running only user-defined catalogs), use `avd_catalogs_enabled`:

```yaml
# Disable AVD-generated catalogs
avd_catalogs_enabled: false
# Enable user-defined catalogs only
user_catalogs_enabled: true
```

## Dry Run Mode

The `anta_runner` role does **not** support Ansible check mode (`--check`). To generate tests without executing them, use the `anta_runner_dry_run` variable instead:

<div class="grid" markdown>

=== "eos_validate_state"

    ```shell
    ansible-playbook playbooks/fabric-validate.yaml --check
    ```

=== "anta_runner"

    ```yaml
    anta_runner_dry_run: true
    ```

</div>

## Report Generation

### Showing Only Failed Tests

In `eos_validate_state`, the `only_failed_tests` variable controlled whether reports showed only failed tests.

In `anta_runner`, use `anta_report_exclude_statuses` to exclude specific test statuses from reports:

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    only_failed_tests: true
    ```

=== "anta_runner"

    ```yaml
    anta_report_exclude_statuses: [ success, skipped ]
    ```

</div>

### Disabling Report Generation

In `eos_validate_state`, CSV and Markdown report generations were controlled by boolean variables.

In `anta_runner`, set the report path to `null` to disable generation of a specific report format:

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    validation_report_csv: false
    validation_report_md: true
    ```

=== "anta_runner"

    ```yaml
    # Set to null to disable
    anta_report_csv_path: null
    # Markdown report will still be generated
    anta_report_md_path: "{{ anta_reports_dir }}/anta_report.md"
    ```

</div>

## Markdown Report Formatting

The `anta_runner` role has different default report formatting compared to `eos_validate_state`:

1. **Condensed results**: By default, tests are condensed in the report to avoid large report files on high-scale fabrics. To show individual test entries (granular results) like `eos_validate_state`, use `anta_report_expand_results`.

2. **Custom field hidden**: By default, the `custom_field` column is hidden. To show it like `eos_validate_state`, use `anta_report_custom_field`.

```yaml
# Expand results to show individual test inputs
anta_report_expand_results: true
# Include the custom_field column in Markdown reports
anta_report_custom_field: true
```

## Fan and Power Supply States

The ANTA tests for fan and power supply validation have been improved. The `accepted_fan_states` and `accepted_pwr_supply_states` variables are no longer required.

If you are expecting that not all fans and power supplies are inserted in specific devices, you can use **validation profiles** to define the expected number of fans and power supplies.

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    # No longer required
    accepted_fan_states: [ ok ]
    accepted_pwr_supply_states: [ ok ]
    ```

=== "anta_runner"

    ```yaml
    # eos_designs configuration
    validation_profiles:
      - name: chassis_profile
        hardware:
          min_power_supplies: 2  # Set to 0 to skip validation
          min_fans: 4            # Set to 0 to skip validation

    # Apply to node types
    spine:
      defaults:
        validation_profile: chassis_profile
    ```

</div>

For more details, see [Validation Profiles](../../ansible_collections/arista/avd/roles/anta_runner/README.md#validation-profiles).

## Transceiver Manufacturers

In `eos_validate_state`, accepted transceiver manufacturers were configured using the `accepted_xcvr_manufacturers` variable.

In `anta_runner`, this setting has moved to `eos_designs` and is configured through `validation_profiles`:

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    accepted_xcvr_manufacturers:
      - Arista Networks
      - Arastra, Inc.
      - Third Party Vendor
    ```

=== "anta_runner"

    ```yaml
    # eos_designs configuration
    validation_profiles:
      - name: datacenter
        hardware:
          transceiver_manufacturers:
            - Arista Networks
            - Arastra, Inc.
            - Third Party Vendor

    # Apply to node types
    spine:
      defaults:
        validation_profile: datacenter
    l3leaf:
      defaults:
        validation_profile: datacenter
    ```

</div>

For more details, see [Validation Profiles](../../ansible_collections/arista/avd/roles/anta_runner/README.md#validation-profiles).

## Fabric-Wide Validation

In `eos_validate_state`, fabric-wide validation tests (Loopback0 reachability, VTEP reachability, inband management reachability, DPS reachability, routing table entries for fabric underlay) were generated by default.

In `anta_runner`, these tests are **disabled by default** and require enabling `avd_catalogs_extra_fabric_validation`.

!!! info
    This change was made because these tests can generate many additional inputs to tests and significantly increase execution time in large-scale deployments.

To enable fabric-wide tests:

```yaml
avd_catalogs_extra_fabric_validation: true
```

For more details, see [Extra Fabric Validation](../../ansible_collections/arista/avd/roles/anta_runner/README.md#extra-fabric-validation).

## Hardware Validation on Virtual Platforms

In `eos_validate_state`, hardware tests were generated for all platforms, but ANTA would skip them on virtual platforms and show them as "skipped" in the report.

In `anta_runner`, hardware tests are **not generated** for known virtual platforms by default. This means these tests will be absent from the report rather than appearing as "skipped".

This behavior is controlled by `feature_support.hardware_validation` in `eos_designs` platform settings. The following platforms have this set to `false` by default:

- **vEOS**: VEOS, VEOS-LAB, vEOS, vEOS-lab
- **cEOS**: CEOS, cEOS, ceos, cEOSLab
- **CloudEOS**: CloudEOS

To get the same behavior as `eos_validate_state` (hardware tests generated and skipped by ANTA), you can use `custom_platform_settings`:

```yaml
custom_platform_settings:
  - platforms:
      - VEOS
      - VEOS-LAB
      - vEOS
      - vEOS-lab
      - CEOS
      - cEOS
      - ceos
      - cEOSLab
      - CloudEOS
    feature_support:
      hardware_validation: true
```

## Complete Migration Example

The following example shows a complete migration from `eos_validate_state` to `anta_runner` with equivalent behavior:

<div class="grid" markdown>

=== "eos_validate_state"

    ```yaml
    - name: Validate Network State
      hosts: FABRIC
      connection: local
      gather_facts: false
      tasks:
        - name: Validate states on EOS devices
          import_role:
            name: arista.avd.eos_validate_state
          vars:
            save_catalog: true
            only_failed_tests: true
    ```

=== "anta_runner"

    ```yaml
    - name: Validate Network State
      hosts: FABRIC
      connection: local
      gather_facts: false
      tasks:
        - name: Run ANTA on EOS devices
          import_role:
            name: arista.avd.anta_runner
          vars:
            # Enable reachability tests (default in eos_validate_state)
            avd_catalogs_extra_fabric_validation: true
            # Equivalent to only_failed_tests: true
            anta_report_exclude_statuses: [ success, skipped ]
            # Equivalent Markdown report formatting
            anta_report_expand_results: true
            anta_report_custom_field: true
    ```

</div>

For information about new features available in `anta_runner`, see the [anta_runner documentation](../../ansible_collections/arista/avd/roles/anta_runner/README.md).

## Additional Resources

- [ANTA Framework Documentation](https://anta.arista.com)
