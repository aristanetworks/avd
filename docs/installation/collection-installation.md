<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Ansible Collection Installation

## Installation workflow

- Install supported [Python](https://www.python.org/downloads/) version **3.11-3.14**.
  - The Python version determines the supported `ansible-core` version. Consult the [ansible-core support matrix](https://docs.ansible.com/ansible/latest/reference_appendices/release_and_maintenance.html#ansible-core-support-matrix) for more information.
- Install the [pyavd](https://pypi.org/project/pyavd/) Python package with `ansible` dependencies.
  - Note: This will install the supported ansible-core version and all required [Python dependencies](#python-dependencies).
- Install [arista.avd](https://galaxy.ansible.com/ui/repo/published/arista/avd/) Ansible collection.

!!! warning "Python 3.10 end of life"

    Python 3.10 has reached [end of life](https://devguide.python.org/versions/) and no longer receives security updates.
    AVD support for Python 3.10 is deprecated and will be removed in a future release. Please upgrade to a supported Python version.

## Python dependencies

The installed version of PyAVD **must** match the version of the `arista.avd` collection.
Installation instructions are included under the [Install Arista AVD](#install-arista-avd) section.

!!! important "Keep Python dependencies up to date"

    When installing or upgrading PyAVD, update its Python dependencies to the
    latest compatible releases to pick up available security fixes using:

    - pip: `--upgrade --upgrade-strategy eager`
    - uv: `--upgrade`

```text
--8<--
docs/avd-requirements.txt:4:
--8<--
```

## Install Arista AVD

These instructions are for regular users to install via Ansible Galaxy.
The instructions also include installation of all Python requirements for a given version.
To set up a development environment, please follow the [development tooling](../contribution/development-tooling.md) instructions.
**arista.avd** can also be consumed using the ["Universal" container](../containers/overview.md#how-to-use-dev-containers).
The **arista.avd** collection is available on the [Ansible Galaxy](https://galaxy.ansible.com/arista/avd)
server and can be automatically installed on your system.

!!! warning
    If you have an `ansible.cfg` file in the directory where you run `ansible-galaxy`, it may affect the directory under which the collection and dependencies will be installed.

!!! warning
    Depending on your operating system settings, `pip` might be replaced by `pip3`.

These commands install all Python requirements including `ansible-core` and then installs the `arista.avd` Ansible collection including
all required Ansible collections:

=== "pip"

    ### Install or upgrade to the latest version

    ```shell
    pip install --upgrade --upgrade-strategy eager "pyavd[ansible]"
    ansible-galaxy collection install arista.avd --upgrade
    ```

    ### Install a specific version

    ```shell
    pip install --upgrade --upgrade-strategy eager "pyavd[ansible]==6.1.0"
    ansible-galaxy collection install arista.avd:==6.1.0 --upgrade
    ```

    ### Install latest `devel` version from AVD GitHub

    !!! note
        When installing from devel, collection dependencies like `arista.eos` will be installed from Ansible Galaxy unless installed first using similar GitHub source.

    ```shell
    pip install --upgrade --upgrade-strategy eager "pyavd[ansible] @ git+https://github.com/aristanetworks/avd.git@devel#subdirectory=python-avd"
    ansible-galaxy collection install git+https://github.com/aristanetworks/avd.git#/ansible_collections/arista/avd/,devel --upgrade
    ```

=== "uv"

    !!! note
        Before using the `uv pip` command, create or activate the intended virtual environment.
        For example, run `uv venv` and then `source .venv/bin/activate` on macOS or Linux.

    ### Install or upgrade to the latest version

    ```shell
    uv pip install --upgrade "pyavd[ansible]"
    ansible-galaxy collection install arista.avd --upgrade
    ```

    ### Install a specific version

    ```shell
    uv pip install --upgrade "pyavd[ansible]==6.1.0"
    ansible-galaxy collection install arista.avd:==6.1.0 --upgrade
    ```

    ### Install latest `devel` version from AVD GitHub

    !!! note
        When installing from devel, collection dependencies like `arista.eos` will be installed from Ansible Galaxy unless installed first using similar GitHub source.

    ```shell
    uv pip install --upgrade "pyavd[ansible] @ git+https://github.com/aristanetworks/avd.git@devel#subdirectory=python-avd"
    ansible-galaxy collection install git+https://github.com/aristanetworks/avd.git#/ansible_collections/arista/avd/,devel --upgrade
    ```

## Ansible configuration file

- By default, Ansible will issue a warning when a duplicate dict key is encountered in YAML. We recommend to change to error instead and stop playbook execution when a duplicate key is detected.

```ini title="ansible.cfg"
[defaults]
duplicate_dict_key=error
```

## Arista EOS requirements

- EOS **4.21.8M** or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista CloudVision requirements

If you leverage [CloudVision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, the cv_deploy role is **only** supported on **CloudVision as a Service (CVaaS)** or "on-prem" **CloudVision 2024.1.0** or later.

## Ansible Documentation

- [Ansible Collection User Guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
