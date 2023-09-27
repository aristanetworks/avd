<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Setup Ansible AVD Environment

Two methods can be used to get Ansible up and running quickly with all the requirements to leverage **ansible-avd**:
A Python Virtual Environment or [Docker container](https://hub.docker.com/repository/docker/avdteam/base).

In both scenarios, this document will leverage the git approach to create a local environment with collections installed in their respective folders and additional folders for all your content. All examples will be based on the following folder structure:

```shell
├── git_projects
│   ├── ansible-avd
│   ├── ansible-cvp
│   ├── ansible-avd-cloudvision-demo
│   ├── Makefile
```

## Ansible runner requirements

As described in [requirement page](../installation/collection-installation.md), your runner should run Python 3.8 or Docker engine with [`docker-compose`](https://docs.docker.com/compose/install/).

Besides that, the local runner will read your gitconfig file to let you manipulate files in a container as if you were on your host. If you haven't configured Git on your host, it's required to create at least a [basic git](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) configuration file:

```shell
# Create your username exposed in git commit
$ git config --global user.name "John Doe"

# Create email exposed in your commit
$ git config --global user.email johndoe@example.com
```

## Create a local folder structure

To build a local folder structure, you manually run all the following commands to git clone [ansible-avd](https://github.com/aristanetworks/ansible-avd), [ansible-cvp collection](https://github.com/aristanetworks/ansible-cvp) and a [repository with demo content](https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo)

In addition to these three git clones, you can also deploy a [Makefile](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) built to provide some shortcuts we will discuss in a second stage.

```shell
$ mkdir git_projects

$ cd git_projects

$ git clone https://github.com/aristanetworks/ansible-avd.git
$ git clone https://github.com/aristanetworks/ansible-cvp.git
$ git clone https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo.git

# Copy Makefile at the root position
$ cp ansible-avd/development/Makefile ./
$ make start
```

Or you can use a one-liner script available in ansible-avd repository to create this structure for you. This script accomplishes the following actions:

- Create a local folder for development
- Instantiate a local git repository (no remote)
- Clone AVD and CVP collections
- Deploy Makefile

Because we're cloning the Ansible collection using Git, it's recommended to read the documentation about [how to setup Ansible to use collection based on git clone](setup-git.md#update-your-ansiblecfg).

## Environment with the latest stable

This one-liner will install the AVD and CVP collections using the latest version released on GitHub. These branches might have some differences from the devel branch.

```shell
sh -c "$(curl -fsSL https://get.avd.sh)"
```

## Development environment with AVD

This one-liner will install AVD using the `devel` branch.

```shell
sh -c "$(curl -fsSL https://get.avd.sh/dev/)"
```

!!! warning
    As the devel branch always includes the latest features and updates, the data models might change without notice, and demo content could be broken. It should be used for development only.

## Use Docker as an AVD shell

This approach will leverage a Docker container to provide all the AVD requirements and playbooks. The collection will be shared from your localhost to the container.

This approach will make the run process easier as all libraries are pre-configured in the container, and you can continue to use your preferred text editor to edit and build your content.

Considering you have deployed [Makefile](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) described in the previous section, all the outputs will provide native Docker command and the Make command.

### AVD environment commands

When using the installation script to create your own AVD environment, a [`Makefile`](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) is deployed under `./ansible-arista` to automate some common commands:

```shell
make <your command>
```

#### Commands for docker-compose

- `start`: Start the Docker compose stack to develop with AVD and CVP collection (alias: `start`)
  - Deploy an [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) instance to expose AVD documentation with live reload for development purposes.
  - Deploy an [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) instance to expose CVP documentation with live reload for development purposes.
  - Deploy an [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) with a pseudo-terminal connected to a shell for Ansible execution
- `stop`: Stop the Docker compose stack and remove containers (alias: `stop`)
- `shell`: Run a shell attached to the Ansible container (alias: `shell`)
- `reload`: Stop and Start the docker-compose stack
- `ansible-upgrade`: To upgrade Ansible in your runner in conjunction with `ANSIBLE_VERSION`

```shell
$ make ansible-upgrade ANSIBLE_VERSION=2.10.7
docker-compose -f ansible-avd/development/docker-compose.yml exec -u avd ansible pip install --user --upgrade ansible==2.10.7
Collecting ansible==2.10.7
  Downloading ansible-2.10.7.tar.gz (14.2 MB)
     |████████████████████████████████| 14.2 MB 475 kB/s
...
$ make shell
docker-compose -f ansible-avd/development/docker-compose.yml exec -u avd ansible zsh

Agent pid 109
➜  /projects ansible --version
ansible 2.10.7
```

### Commands for Docker only

- `run`: Run a [Docker container](https://hub.docker.com/repository/docker/avdteam/base) with local folder mounted under `/projects`. This command supports some options to test development versions like:
  - `ANSIBLE_VERSION`: Specific version of Ansible to install during container startup.
  - `PIP_REQ`: Specific pip requirements file to install during container startup.
- `vscode`: start a VScode container available in your browser to edit your local files.

```shell
$ make run ANSIBLE_VERSION=2.10
docker run --rm -it \
                -e AVD_REQUIREMENTS= \
                -e AVD_ANSIBLE=2.10 \
                -e AVD_GIT_USER="xxxxx" \
                -e AVD_GIT_EMAIL="xxxxx" \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -v /Users/tgrimonet/Projects/arista-ansible/:/projects \
                -v /etc/hosts:/etc/hosts avdteam/base:3.6
Install ansible with version 2.10
Collecting ansible==2.10
  Downloading ansible-2.10.0.tar.gz (14.1 MB)
...
```

#### Command for image management

- `update`: Get the latest version of [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) and [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) servers
- `clean`: Remove the AVD image from the local repository

### Run AVD shell

We will start a [new container](https://hub.docker.com/repository/docker/avdteam/base) running Ansible with all the Python requirements and mount a local folder under `/projects`. If the image is missing, Docker will pull it automatically.

```shell
$ docker run --rm -it -v ${pwd}/:/projects avdteam/base:3.6
Unable to find image 'avdteam/base:3.6' locally
3.6: Pulling from avdteam/base
bf5952930446: Already exists
385bb58d08e6: Already exists
f59c6df69726: Already exists
cc14d0cfa632: Already exists
f4eba3bd5be8: Already exists
55c6a5feb373: Already exists
83464a988ea4: Pull complete
9b675b85887d: Pull complete
9cce9aa068f4: Pull complete
a49dbba0fea8: Pull complete
793f98fe2265: Pull complete
Digest: sha256:ead3ef030caa6caeafd6ddbfd31ce935da26b66914096c9543d9a44cca993dfd
Status: Downloaded newer image for avdteam/base:3.6
Agent pid 45
➜  /projects
```

You can use the Make command to run the same set of actions:

```shell
$ make run
Unable to find image 'avdteam/base:3.6' locally
3.6: Pulling from avdteam/base
bf5952930446: Already exists
385bb58d08e6: Already exists
f59c6df69726: Already exists
cc14d0cfa632: Already exists
f4eba3bd5be8: Already exists
55c6a5feb373: Already exists
83464a988ea4: Pull complete
9b675b85887d: Pull complete
9cce9aa068f4: Pull complete
a49dbba0fea8: Pull complete
793f98fe2265: Pull complete
Digest: sha256:ead3ef030caa6caeafd6ddbfd31ce935da26b66914096c9543d9a44cca993dfd
Status: Downloaded newer image for avdteam/base:3.6
Agent pid 45
➜  /projects
```

Then you can move to your content folder as the structure remains the same:

```shell
➜  /projects ls -l
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-avd
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-cvp
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-avd-cloudvision-demo
drwxr-xr-x 24 root root  768 Sep  4 15:47 Makefile
```

You can validate if everything is set up correctly:

```shell
➜  /projects python --version
Python 3.6.12

➜  /projects ansible --version
ansible 2.10.7
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /root/.local/lib/python3.6/site-packages/ansible
  executable location = /root/.local/bin/ansible
  python version = 3.6.12 (default, Aug 18 2020, 04:28:43) [GCC 8.3.0]
```

To exit the container, use `exit`

```shell
➜  /projects exit
$
```

### Get the latest image of the AVD container

The AVD container is updated frequently to reflect some changes in either Python requirements or the Ansible version. Because your Docker engine won't get the latest version automatically, it's essential to manually update this container:

```shell
$ docker pull avdteam/base:3.6
latest: Pulling from avdteam/base
8a29a15cefae: Already exists
95df01e08bce: Downloading [==============================================>    ]  33.55MB/36.35MB
512a8a4d71f7: Downloading [=========================================>         ]   45.1MB/53.85MB
209c1657264b: Download complete
bd6eece0221e: Downloading [===================>                               ]  52.04MB/132.1MB
036c486feecb: Waiting
```

Your environment is now ready, and you can start to build your project leveraging ansible-avd and ansible-cvp collections.

## Using Python 3 Virtual Environment feature

This section describes how to configure Python to run the ansible-AVD.

As a requirement, we consider python3 as the default Python interpreter and pip3 as the package manager for python3. Some differences can be spotted depending on your operating system and how they package Python.

**Disclaimer**: Not a preferred method. If you are an inexperienced user, please use the Docker approach.

In a shell, install the `virtualenv` package:

```shell
# install virtualenv via pip3
sudo pip3 install virtualenv
```

Create a dedicated virtual environment where AVD will install all required Python packages:

```shell
$ pwd
/home/user/git_projects

# Configure Python virtual environment
$ virtualenv -p python3 .venv
$ source .venv/bin/activate

# Install Python requirements
$ pip3 install -r ansible-avd/ansible_collections/arista/avd/requirements.txt
...
```
