<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Ansible Collection Installation

## Installation workflow

- Install supported [Python](https://www.python.org/downloads/) version **3.10-3.14**.
  - The Python version determines the supported `ansible-core` version. Consult the [ansible-core support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix) for more information.
- Install the [pyavd](https://pypi.org/project/pyavd/) Python package with `ansible` dependencies.
  - Note: This will install the supported ansible-core version and all required [Python dependencies](#python-dependencies).
- Install [arista.avd](https://galaxy.ansible.com/ui/repo/published/arista/avd/) Ansible collection.

## Python dependencies

``` shell
--8<--
ansible_collections/arista/avd/requirements.txt:4:
--8<--
```

## Install Collection from Ansible Galaxy

These instructions are for regular users to install via Ansible Galaxy.
The instructions also include installation of all Python requirements for a given version.
To set up a development environment, please follow the [development tooling](../contribution/development-tooling.md) instructions.
**arista.avd** can also be consumed using the ["Universal" container](../containers/overview.md#how-to-use-dev-containers).
The **arista.avd** collection is available on the [Ansible Galaxy](https://galaxy.ansible.com/arista/avd)
server and can be automatically installed on your system.

### Latest version

These commands install all Python requirements including `ansible-core` and then installs the `arista.avd` Ansible collection including
all required Ansible collections.

```shell
pip install "pyavd[ansible]"
ansible-galaxy collection install arista.avd
```

!!! warning
    If you have an `ansible.cfg` file in the directory where you run `ansible-galaxy`, it may affect the directory under which the collection and dependencies will be installed.

!!! warning
    Depending on your operating system settings, `pip` might be replaced by `pip3`.

### Install a specific version

```shell
pip install "pyavd[ansible]==4.8.0"
ansible-galaxy collection install arista.avd:==4.8.0
```

### Install latest `devel` version from AVD GitHub

```shell
pip install "pyavd[ansible] @ git+https://github.com/aristanetworks/avd.git@devel#subdirectory=python-avd"
ansible-galaxy collection install git+https://github.com/aristanetworks/avd.git#/ansible_collections/arista/avd/,devel
```

!!! note
    Installing from `devel` will require minimum Python 3.10, since the PyAVD package will be built during installation, and some
    of the build tooling requires minimum 3.10.

!!! note
    Collection dependencies like `ansible-cvp` will be installed from Ansible Galaxy unless installed first using similar GitHub source.

### Install in a specific directory

If you want to install collection in a specific directory part of your project, you can call `ansible-galaxy` with the `-p` option
and update your `ansible.cfg`:

```shell
# Install collection under ${PWD}/collections/
$ ansible-galaxy collection install arista.avd -p collections/

# Update ansible.cfg file
$ vim ansible.cfg
collections_paths = ${PWD}/collections:~/.ansible/collections:/usr/share/ansible/collections
```

### Upgrade installed AVD collection

You can use `-U` to upgrade to a new version for any installed collection:

```shell
$ ansible-galaxy collection install -U arista.avd
Process install dependency map
Starting collection install process
Installing 'arista.avd:4.9.0' to '/home/arista/.ansible/collections/ansible_collections/arista/avd'
```

After an upgrade, some python requirements may have changed. Make sure to also update the Python requirements for the same version (the version given below matches the installed collection above):

```shell
pip install "pyavd[ansible]==4.9.0"
```

### Python requirements installation

Python requirements can be installed with `pip install "pyavd[ansible]"`.
The installed version of PyAVD **must** match the version of the `arista.avd` collection.

See the [collection installation](#install-collection-from-ansible-galaxy) section for details of each installation method.

## Ansible configuration file

- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini
duplicate_dict_key=error
```

## Arista EOS requirements

- EOS **4.21.8M** or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision requirements

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [CloudVision Ansible collection](https://aristanetworks.github.io/ansible-cvp/)

!!! note
    When using ansible-cvp modules, the user who is executing the ansible-playbook must have access to both CVP and the EOS CLI.

## Ansible Documentation

- [Ansible Collection User Guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
