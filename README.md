# Refactor assignments:
- [ ] aaa-accounting.j2 (CB)
- [ ] aaa-authentication.j2 (CB)
- [ ] aaa-authorization.j2 (XR)
- [ ] aaa-root.j2 (XR)
- [ ] aaa-server-groups.j2 (XR)
- [ ] access-lists.j2 (XR)
- [ ] aliases.j2 (XR)
- [ ] arp.j2 (XR)
- [ ] banners.j2 (XR)
- [ ] clock-timezone.j2 (XR)
- [ ] community-lists.j2 (XR)
- [ ] custom-templates.j2 (XR)
- [ ] daemon-terminattr.j2 (XR)
- [ ] dns-domain.j2 (XR)
- [ ] domain-list.j2 (XR)
- [ ] domain-lookup.j2 (XR)
- [ ] enable-password.j2 (XR)
- [ ] errdisable.j2 (XR)
- [ ] ethernet-interfaces.j2
- [ ] event-handler.j2
- [ ] event-monitor.j2
- [ ] hardware-counters.j2
- [ ] hardware.j2
- [ ] interface-defaults.j2
- [ ] ip-dhcp-relay.j2
- [ ] ip-extended-communities.j2
- [ ] ip-igmp-snooping.j2
- [ ] ip-routing.j2
- [ ] ip-tacacs-source-interfaces.j2
- [ ] ipv6-access-lists.j2
- [ ] ipv6-prefix-lists.j2
- [ ] ipv6-routing.j2
- [ ] ipv6-standard-access-lists.j2
- [ ] ipv6-static-routes.j2
- [ ] lldp.j2
- [ ] load-interval.j2
- [ ] local-users.j2
- [ ] logging.j2
- [ ] loopback-interfaces.j2
- [ ] mac-address-table.j2
- [ ] mac-security.j2
- [ ] management-api-gnmi.j2
- [ ] management-api-http.j2
- [ ] management-console.j2
- [ ] management-interfaces.j2
- [ ] management-security.j2
- [ ] management-ssh.j2
- [ ] mlag-configuration.j2
- [ ] name-servers.j2
- [ ] ntp-servers.j2
- [ ] peer-filters.j2
- [ ] platform.j2
- [ ] port-channel-interfaces.j2
- [ ] prefix-lists.j2
- [ ] ptp.j2
- [ ] qos-profiles.j2
- [ ] qos.j2
- [ ] queue-monitor-length.j2
- [ ] queue-monitor-streaming.j2
- [ ] radius-servers.j2
- [ ] redundancy.j2
- [ ] route-maps.j2
- [ ] router-bfd.j2
- [ ] router-bgp.j2 (CB)
- [ ] router-isis.j2
- [ ] router-l2-vpn.j2
- [ ] router-multicast.j2
- [ ] router-ospf.j2
- [ ] router-pim-sparse-mode.j2
- [ ] service-routing-protocols-model.j2
- [ ] sflow.j2
- [ ] snmp-settings.j2
- [ ] spanning-tree.j2 (OG)
- [ ] standard-access-lists.j2 (OG)
- [ ] static-routes.j2 (OG)
- [ ] tacacs-servers.j2 (OG)
- [ ] tcam-profile.j2 (OG)
- [ ] terminal-settings.j2 (OG)
- [ ] unsupported-transeiver.j2 (OG)
- [ ] virtual-router-mac-address.j2 (OG)
- [ ] virtual-source-nat.j2 (OG)
- [ ] vlan-interfaces.j2 (TG)
- [ ] vlan-internal-order.j2 (OG)
- [ ] vlans.j2 (OG)
- [ ] vmtracer-sessions.j2 (TG)
- [ ] vrf-instances.j2 (TG)
- [ ] vxlan-interface.j2 (TG)



# Ansible Collection For Arista Validated Designs - arista.avd

![Arista AVD](https://img.shields.io/badge/Arista-AVD%20Automation-blue) ![collection version](https://img.shields.io/github/v/release/aristanetworks/ansible-avd) ![License](https://img.shields.io/github/license/aristanetworks/ansible-avd)

**Table of Contents:**

- [Ansible Collection For Arista Validated Designs - arista.avd](#ansible-collection-for-arista-validated-designs---aristaavd)
  - [About](#about)
  - [Project Documentation](#project-documentation)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation from ansible-galaxy](#installation-from-ansible-galaxy)
  - [Example Playbooks](#example-playbooks)
  - [Examples](#examples)
  - [Additional Resources](#additional-resources)
  - [Ask a question](#ask-a-question)
  - [Contributing](#contributing)
  - [Branching Model](#branching-model)
  - [License](#license)

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system natively through eapi or [CloudVision Portal (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision). This collection includes a set of ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs!

<center><img src="ansible_collections/arista/avd/media/avd-logo.png" alt="Arista AVD Overview" width="800"/></center>

## Project Documentation

The documentation how to leverage ansible-avd collection is located here: **[arista.avd](./ansible_collections/arista/avd/README.md)**

## Installation

### Requirements

**Arista EOS:**

- EOS 4.21.8M or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

**Python:**

- Python 3.6.8 or later

**Supported Ansible Versions:**

- ansible 2.9.2 or later

**Additional Python Libraries required:**

- Jinja2  `2.10.3`
- netaddr `0.7.19`
- requests `2.22.0`
- treelib `1.5.5`
- pytest `5.3.4`
- pytest-html `2.0.1`
- cvprac `1.0.4`

**Ansible + Additional Python Libraries Installation:**

```shell
pip3 install -r development/requirements.txt
```

requirements.txt content:

```text
ansible==2.9.2
Jinja2==2.10.3
netaddr==0.7.19
requests==2.22.0
treelib==1.5.5
pytest==5.3.4
pytest-html==2.0.1
cvprac==1.0.4
```

**Ansible Configuration INI file:**

- enable jinja2 extensions: loop controls and do
  - [Jinja2 Extensions Documentation](https://svn.python.org/projects/external/Jinja-2.1.1/docs/_build/html/extensions.html)
- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

> **_NOTE:_** When using ansible-cvp modules, the user that is executing the ansible-playbook has to have access to both CVP and the EOS CLI.

### Installation from ansible-galaxy

Ansible galaxy hosts all stable version of this collection. Installation from ansible-galaxy is the most convenient approach for consuming `arista.avd` content

```shell
ansible-galaxy collection install arista.avd
```

## Example Playbooks

**An example playbook to deploy VXLAN/EVPN Fabric via CloudVision:**

![Figure 1: Example Playbook CloudVision Deployment](media/example-playbook-evpn-deploy-cvp.gif)

```yml
- hosts: DC1_FABRIC
  tasks:
    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn
    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

- hosts: CVP
  tasks:
    - name: deploy configuration via CVP
      import_role:
         name: arista.avd.eos_config_deploy_cvp
```

Execute eos_state_validation playbook once change control has been approved and deployed to devices in CVP.
Note: To run this playbook, ansible_host **must** be configured in your inventory for every EOS device. eAPI access **must** be configured and allowed in your networks.

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

**An example playbook to deploy VXLAN/EVPN Fabric via eAPI:**

![Figure 2: Example Playbook CloudVision Deployment](media/example-playbook-evpn-deploy-eapi.gif)

```yml
- hosts: DC1_FABRIC

  tasks:

    - name: generate intended variables
      import_role:
         name: arista.avd.eos_l3ls_evpn

    - name: generate device intended config and documentation
      import_role:
         name: arista.avd.eos_cli_config_gen

    - name: deploy configuration via eAPI
      import_role:
         name: arista.avd.eos_config_deploy_eapi

    - name: audit fabric state using EOS eAPI connection
      import_role:
         name: arista.avd.eos_validate_state
```

## Examples

**Full examples with variables and outputs, are located here:**

[Arista NetDevOps Examples](https://github.com/aristanetworks/netdevops-examples)

## Additional Resources

- Ansible [EOS modules](https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#eos) on ansible documentation.
- Ansible [CloudVision modules](https://github.com/aristanetworks/ansible-cvp)
- [CloudVision Portal](https://www.arista.com/en/products/eos/eos-cloudvision)
- [Arista Design and Deployment Guides](https://www.arista.com/en/solutions/design-guides)

## Ask a question

Support for this `arista.avd` collection is provided by the community directly in this repository. Easiest way to get support is to open [an issue](https://github.com/aristanetworks/ansible-avd/issues).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we'll be able to merge it.

You can also open an [issue](https://github.com/aristanetworks/ansible-avd/issues) to report any problem or to submit enhancement.

## Branching Model

- The __`devel`__ branch corresponds to the release actively under development.
- The __`releases/x.x.x`__ branches correspond to stable releases.
- Fork repository and create a branch based on __`devel`__ to set up a dev environment if you want to open a PR.
- See the ansible-avd release for information about active branches.

## License

Project is published under [Apache 2.0 License](LICENSE)
