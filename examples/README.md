![](https://img.shields.io/badge/Arista-EOS%20Automation-blue) ![GitHub](https://img.shields.io/github/license/aristanetworks/ansible-avd)  ![GitHub last commit](https://img.shields.io/github/last-commit/aristanetworks/ansible-avd) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/aristanetworks/ansible-avd)

![Development Status](https://img.shields.io/badge/development-In_Progress-red)  __WARNING:
Early Field Trial - Ansible Collection for Arista Validated Designs Work in Progress

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Ansible Arista Validated Design](#ansible-arista-validated-design)
  - [Quick Start](#quick-start)
  - [Resources](#resources)
- [License](#license)
- [Ask question or report issue](#ask-question-or-report-issue)
- [Contribute](#contribute)

<!-- /code_chunk_output -->

# Ansible Arista Validated Design

Repository provides modules and roles to build an EVPN/VXLAN fabric using Ansible to build and deploy configuration to devices.

Devices configuration are based on [Arista EVPN Design Guide](https://www.arista.com/en/solutions/design-guides) and cover a generic Unified Cloud Network environment.

![arista-bgp-evpn-fabric](documentation/arista-bgp-evpn-vxlan.png)

## Quick Start

```shell
# Configure Python virtual environment
$ virtualenv -p $(which python) .venv
$ source .venv/bin/activate

# Install Python requirements
$ pip install -r requirements.txt

# Edit Inventory file
$ vim inventory.yml

# Edit fabric variables
# Change values to point to your own information
$ vim group_vars/DC1_FABRIC.yml

# Run ansible playbooks
$ cd examples/evpn-design-guide/
$ ansible-playbook dc1-fabric-config.yml --tags "documentation" --diff
```

## Docker

The docker container approach for development can be used to ensure that
everybody is using the same development environment while still being flexible
enough to use the repo you are making changes in. You can inspect the
Dockerfile to see what packages have been installed.

The ansible version is passed in with the docker build command using
***ANSIBLE*** variable.  If the ***ANSIBLE*** variable is not used the
Dockerfile will by default set the ansible version to 2.8.5.

```
$ docker build -t ansible_avd . --build-arg UID=$(id -u) --build-arg GID=$(id -g) --build-arg ANSIBLE=<ansible version>
```

Start up the docker container from the root of the repo directory with the
following command. Note that specifying the -u option allows you to run the
container as your user-id and not as root. This eliminates problem with
creating files owned by root in your repo.

```
$ docker run -t -d --name ansible_avd -v $(pwd)/:/ansible_avd -v /etc/hosts:/etc/hosts ansible_avd
```

Use docker exec to login into the container with a bash shell.

```
$ docker exec -it ansible_avd bash
```

In addition to using docker commands to start up and access the container, make can be used to do
this in a single step.  A user can pass the ansible version number to make and alter the default
ansible-version number.  This allows a user to setup multiple containers running differing
versions of ansible.

```
$ make                            # Use default version of Ansible
$ make ANSIBLE_VERSION=2.8.3      # Explicitly set Ansible version to 2.8.3
$
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
38dc36a91ccc        ansible_avd:2.8.3   "/bin/sh"           7 seconds ago       Up 5 seconds                            ansible_avd_2.8.3
9d82d0ca9105        ansible_avd:2.8.5   "/bin/sh"           22 seconds ago      Up 21 seconds                           ansible_avd_2.8.5
```

Another make target (clean) has been created to stop and remove the container once the user
is finished with it.

```
$ make clean                           # Clean default container version of Ansible
$ make ANSIBLE_VERSION=2.8.3 clean     # Explicitly clean Ansible 2.8.3 container
$
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

## Resources

- EOS Ansible modules are documented part of [Ansible core modules](https://docs.ansible.com/ansible/latest/modules/list_of_network_modules.html#eos)

- [An eBGP EVPN over eBGP network design](https://eos.arista.com/evpn-configuration-ebgp-design-for-evpn-overlay-network/)

# License

Project is published under [Apache License](LICENSE).

# Ask question or report issue

Please open an issue on Github this is the fastest way to get an answer.

# Contribute

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we’ll be able to merge it.
