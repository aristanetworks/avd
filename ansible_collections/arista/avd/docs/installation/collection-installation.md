<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Collection installation

## Installation workflow

- Install [Python](https://www.python.org/downloads/) **3.9** or later
- Install [ansible-core](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) from **2.14.0** to **2.16.x**
- Install [arista.avd](#install-collection-from-ansible-galaxy) collection
- Install additional Python [requirements](#python-requirements-installation)
- Modify `ansible.cfg` file to support additional [jinja2 extensions](#ansible-configuration-file)

## Install Collection from Ansible Galaxy

These instructions are for regular users to install via Ansible Galaxy. To setup a development environment use [these](../contribution/setup-environment.md) instructions. **arista.avd** can also be consumed using the ["AVD All-in-one" container](https://github.com/arista-netdevops-community/avd-all-in-one-container). The **arista.avd** collection is available on [Ansible Galaxy](https://galaxy.ansible.com/arista/avd) server and can be automatically installed on your system.

### Latest version

```shell
ansible-galaxy collection install arista.avd
```

!!! warning
    If you have an `ansible.cfg` file in the directory where you run `ansible-galaxy`, it may affect the directory under which the collection and dependencies will be installed.

### Install a specific version

```shell
ansible-galaxy collection install arista.avd:==4.4.0
```

You can specify multiple range identifiers which are split by `,`. For example, you can use the following range identifiers:

- `*`: Any version, this is the default used when no range specified is set.
- `!=`: Version isn't equal to the one specified.
- `==`: Version must be the one specified.
- `>=`: Version is greater than or equal to the one specified.
- `>`: Version is greater than the one specified.
- `<=`: Version is less than or equal to the one specified.
- `<`: Version is less than the one specified.

!!! note
    If you are installing with a range command, you must surround the command in quotes. For example, `ansible-galaxy collection install 'arista.avd:>=4.0.0,<5.0.0'`

### Install latest `devel` version from AVD GitHub

```shell
ansible-galaxy collection install git+https://github.com/aristanetworks/ansible-avd.git#/ansible_collections/arista/avd/,devel
```

!!! note
    Collection dependencies like `ansible-cvp` will be installed from ansible-galaxy unless installed first using similar GitHub source.

### Install in a specific directory

If you want to install collection in a specific directory part of your project, you can call `ansible-galaxy` and update your `ansible.cfg`

```shell
# Install collection under ${PWD/collections/}
$ ansible-galaxy collection install arista.avd -p collections/

# Update ansible.cfg file
$ vim ansible.cfg
collections_paths = ${PWD}/collections:~/.ansible/collections:/usr/share/ansible/collections
```

### Upgrade installed AVD collection

!!! note
    You can use `-U` to upgrade to a new version for any installed collection:

```shell
$ ansible-galaxy collection install -U arista.avd
Process install dependency map
Starting collection install process
Installing 'arista.avd:4.4.0' to '/root/.ansible/collections/ansible_collections/arista/avd'
```

!!! warning
After an upgrade, some python requirements may have changed. Follow the
instructions in the Python [requirements](#python-requirements-installation)
section to update your python packages.

!!! note
    You can find some additional information about how to use Ansible's collections on the following Ansible pages:

    - [Ansible collection user guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
    - [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)

## Additional Python Libraries required

```pip
--8<--
requirements.txt
--8<--
```

### Python requirements installation

In a shell, run the following commands after installing the collection from ansible-galaxy:

```shell
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.avd --format yaml | head -1 | cut -d: -f1)
pip3 install -r ${ARISTA_AVD_DIR}/arista/avd/requirements.txt
```

If the collection is cloned from GitHub, we can reference the requirements file directly:

```shell
pip3 install -r ansible-avd/ansible_collections/arista/avd/requirements.txt
```

!!! warning
    Depending of your operating system settings, `pip3` might be replaced by `pip`.

## Ansible configuration file

- Enable Jinja2 extensions: `loopcontrols` and `do`
  - [Jinja2 Extensions Documentation](https://jinja.palletsprojects.com/extensions/)
- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

## Arista EOS requirements

- EOS **4.21.8M** or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision requirements

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [CloudVision Ansible collection](https://cvp.avd.sh/)

!!! note
    When using ansible-cvp modules, the user who is executing the ansible-playbook must have access to both CVP and the EOS CLI.
