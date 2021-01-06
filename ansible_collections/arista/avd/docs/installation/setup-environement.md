# Setup Ansible AVD environment

Two methods can be used get Ansible up and running quickly with all the requirements to leverage __ansible-avd__:
A Python Virtual Environment or [Docker container](https://hub.docker.com/repository/docker/avdteam/base).

In both scenario, this document will leverage git approach to create a local environment with collections installed in their respective folders and additional folders for all your content. It means, all examples will be based on the following folder structure:

```shell
├── git_projects
│   ├── ansible-avd
│   ├── ansible-cvp
│   ├── ansible-avd-cloudvision-demo
│   ├── Makefile
```

## Ansible runner requirements

As described in [requirement page](../../docs/installation/requirements.md), your runner should run Python 3.6.8 or Docker engine with [`docker-compose`](https://docs.docker.com/compose/install/).

## Create local folder structure

To build local folder structure you manually run all the following commands to git clone [ansible-avd](https://github.com/aristanetworks/ansible-avd), [ansible-cvp collection](https://github.com/aristanetworks/ansible-cvp) and a [repository with demo content](https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo)

In addition to this 3 `git clone`, you can also deployed a [Makefile](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) built to provide some shortcut we will discuss in a second stage.

```shell
$ mkdir git_projects

$ cd git_projects

$ git clone https://github.com/aristanetworks/ansible-avd.git
$ git clone https://github.com/aristanetworks/ansible-cvp.git
$ git clone https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo.git4

# Copy Makefile at the root position
$ cp ansible-avd/development/Makefile ./
$ make start
```

Or you can use a one-liner script available in ansible-avd repository to create this structure for you. This script does following actions:

- Create local folder for development
- Instantiate a local git repository (no remote)
- Clone AVD and CVP collections
- Deploy Makefile

```shell
$ sh -c "$(curl -fsSL https://get.avd.sh)"
```

Because we are cloning ansible collection using git, it is recommended to read documentation about [how to setup ansible to use collection based on git clone](../setup-git/#update-your-ansiblecfg).

## Use docker as AVD shell

In this approach Docker container will be leveraged to provides all the AVD requirements and playbooks and collection will be shared from your localhost to the container.

This approach make the run process easier as all libraries are pre-configured in container and you can continue to use your preferred text editor to edit and build your content.

Considering you have deployed [Makefile](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) described in previous section, all the outputs will provide native docker command and the Make command.

### AVD environment commands

When using installation script to create your own AVD environment, a [`Makefile`](https://github.com/aristanetworks/ansible-avd/blob/devel/development/Makefile) is deployed under `./ansible-arista` to automate some common commands:

```shell
$ make <your command>
```

#### Commands for docker-compose

- `dev-start`: Start docker compose stack to develop with AVD and CVP collection (alias: `start`)
    - Deploy an [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) instance to expose AVD documentation with live reload for development purposes.
    - Deploy an [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) instance to expose CVP documentation with live reload for development purposes.
    - Deploy an [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) with a pseudo terminal connected to shell for ansible execution
- `dev-stop`: Stop docker compose stack and remove containers (alias: `stop`)
- `dev-run`: Run a shell attached to ansible container (alias: `shell`)
- `dev-reload`: Stop and Start docker-compose stack

### Commands for docker only

- `run`: Run a [docker container](https://hub.docker.com/repository/docker/avdteam/base) with local folder mounted under `/projects`. This command supports some option to test development version like:
    - `ANSIBLE_VERSION`: Specific version of ansible to install during container startup.
    - `PIP_REQ`: Specific pip requirements file to install during container startup.

#### Command for image management

- `update`: Get latest version of [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) and [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) servers
- `clean`: Remove avd image from local repository

### Run AVD shell

We are going to start a [new container](https://hub.docker.com/repository/docker/avdteam/base) running ansible with all the python requirements and mount local folder under `/projects`. if image is missing, docker will pull out image for you automatically.

```shell
$ docker run --rm -it -v $(PWD)/:/projects avdteam/base:3.6
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

You can use a Make command to run exact same set of actions:

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

Then you can move to your content folder as structure remains the same:

```shell
➜  /projects ls -l
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-avd
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-cvp
drwxr-xr-x 24 root root  768 Sep  4 15:47 ansible-avd-cloudvision-demo
drwxr-xr-x 24 root root  768 Sep  4 15:47 Makefile
```

You can validate everything is setup correctly:

```shell
➜  /projects python --version
Python 3.6.12

➜  /projects ansible --version
ansible 2.9.6
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /root/.local/lib/python3.6/site-packages/ansible
  executable location = /root/.local/bin/ansible
  python version = 3.6.12 (default, Aug 18 2020, 04:28:43) [GCC 8.3.0]
```

To exit container, just use `exit`

```shell
➜  /projects exit
$
```

### Get latest image of AVD container

Time to time, AVD container is updated to reflect some changes in either python requirements or ansible version. Because your docker engine won't automatically get latest version, it might be important to update manually this container:

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

Your environment is now ready and you can start to build your own project leveraging ansible-avd and ansible-cvp collections.

## Using Python 3 Virtual Environment feature

This section describes how to configure python to run ansible and AVD.

As a requirement, we consider python3 as default python interpreter and pip3 as package manager for python3. Some differences can be spotted depending on your own operating system and how they package python.

__Disclaimer__: Not preferred method. if you are not an experienced user, please use docker approach.

In a shell, install `virtualenv` package:

```shell
# install virtualenv via pip3
$ sudo pip3 install virtualenv
```

Create a dedicated virtual-environment where AVD will installed all required Python pakages:

```shell
$ pwd
/home/user/git_projects

# Configure Python virtual environment
$ virtualenv -p python3 .venv
$ source .venv/bin/activate

# Install Python requirements
$ pip3 install -r ansible-avd/development/requirements.txt
...
```
