# eos_designs to containerlab

**eos_designs_to_containerlab** is a role to build a [containerlab](https://containerlab.srlinux.dev/) topology from [Arista AVD](https://www.avd.sh) project

!!! info
    This role only supports l3ls-evpn topology from [arista.avd.eos_designs](https://avd.sh/en/latest/roles/eos_designs/doc/l3ls-evpn.html)

## Requirements

Requirements are located here: [avd-requirements](../../README.md#Requirements)

## Default Variables

The following default variables are defined, and can be modified as desired:

- `containerlabs_configuration`: Location and name of the containerlabs configuration generated. (default: `{{ inventory_dir }}/containerlabs.yml`)
- `ceos_version`: Version of cEOS to use for the topology (default: 4.25.2F)
- `mgmt_network_v4`: Subnet for management IPs use for OOB

```yaml
# cEOS Image to use
ceos_version: ceos:latest

# Default management network IP
mgmt_network_v4: 192.168.1.0/24

# Default containerlabs configuration file generated
containerlab_configuration: '{{ inventory_dir }}/containerlabs.yml'
```

## Requirements

- Requirements are located here: [avd-requirements](../../README.md#Requirements)
- **containerlab** in version `>=0.15.3`

```bash
$ containerlab version
                           _                   _       _
                 _        (_)                 | |     | |
 ____ ___  ____ | |_  ____ _ ____   ____  ____| | ____| | _
/ ___) _ \|  _ \|  _)/ _  | |  _ \ / _  )/ ___) |/ _  | || \
( (__| |_|| | | | |_( ( | | | | | ( (/ /| |   | ( ( | | |_) )
\____)___/|_| |_|\___)_||_|_|_| |_|\____)_|   |_|\_||_|____/

    version: 0.15.3
     commit: 533d911
       date: 2021-07-19T14:35:16Z
     source: https://github.com/srl-labs/containerlab
 rel. notes: https://containerlab.srlinux.dev/rn/0.15/#0153
```

## Example Playbook

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
- name: Build containerlab topology
  hosts: DC1_FABRIC
  connection: local
  gather_facts: false
  tasks:
    - name: 'Build a containerlab topolgy'
      import_role:
        name: arista.avd.eos_designs_to_containerlab
      vars:
        mgmt_network_v4: 10.73.0.0/16
        ceos_version: arista/ceos:4.25.2F
```

## License

Project is published under [Apache 2.0 License](../../LICENSE)
