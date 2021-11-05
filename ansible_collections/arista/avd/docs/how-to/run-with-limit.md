# How to run AVD eos_designs role with --limit flag

First some background on the issue with `--limit`.

The `eos_designs` role consists of many different templates which are run in stages across all devices.
All stages run on all devices, but each stage must be completed for all devices, before continuing to the next stage.
The first stage is "Switch Facts" which sets facts on every switch, only concerning that single switch.
The second stage is "Topology Facts" which sets facts per switch based on the "Switch Facts" from this _and_ upstream/peer switches.
The third stage is "Structured Config" which parses "Topology Facts" for _all_ switches in the `fabric`, to look for peers connecting to this switch and generates the full config in a structured data model.

This method is what allows the high flexibility of AVD, while maintaining a simpler topology data model e.g. you only define connectivity from child perspective.
It is also what allows variables to be scoped to only the single devices as necessary e.g. `POD1` only needs to know about the topology of `POD1`, even though it may have a direct connection to `POD2`.

If the playbook is executed with `--limit`, the facts are only computed for this switch, hence it will not be able to create "Topology Facts" nor "Structured Config" for anything outside of this switch.
This means that ex. uplinks to spines will not be possible because we cannot look up the ASN of the spine.

To work around this, it is possible to combine `--limit` with "Fact Caching". "Fact Caching" allows ansible to store all computed facts between plays.
The stored facts will be loaded on the next play, even if that play is limited to one or a few switches.

"Fact Caching" can be enabled in multiple ways and with various plugins. See [Ansible Documentation](https://docs.ansible.com/ansible/latest/plugins/cache.html) for details.

## Example

The simplest cache is to store a YAML file for each device. The cache plugin and path is configured in `ansible.cfg`:
```ini
[defaults]
<...>
fact_caching = jsonfile
fact_caching_connection = < path to directory >
```

After adding the above config, run the playbook once _without_ `--limit`. This will store facts for all devices in the set path. Each switch will have it's own file.

Now it is possible to run the playbook again _with_ `--limit` flag set, and the config will be completely the same because facts are loaded for all devices.

## Limitations and recommendations


1. Avoid using `--limit` if possible because of the pitfalls below.
1. When using the `eos_config_deploy_cvp` role the `--limit` must also contain the CVP server hostname.
1. Before pushing any configuration to any devices, make sure to verify that important configuration is not affected in case the "Fact Cache" was not updated.
1. Fabric documentation and CSV files cannot be generated while using `--limit`. The tasks are skipped automatically.
1. When adding new devices, the playbook _must_ be run at least once without `--limit`. This is to set ensure that uplinks and downlinks are configured correctly on other switches.
1. A warning will be shown during the play, if we detect that facts have not been cached once. _This warning will only be shown on the first run for this device._
   ```cli
   !!! Warning - The role 'arista.avd.eos_designs' only supports '--limit' flag in combination with fact caching
   !!! Warning - UD-a02-LF-2-B not found in cache
   !!! Warning - When adding new devices, the playbook must be run once without '--limit'
   ```
1. If any "Fabric Topology", "Network Services" or other general variables are changed, it may affect multiple devices, so it is recommended to run a full play without `--limit`.
1. To catch any missed changes and to keep Fabric Documentation up to date, it is recommended to run a full play without `--limit` in a schedule, and verify any changes.
