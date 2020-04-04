# Development Tool

Two methods can be used get Ansible up and running quickly with all the requirements to leverage ansible-avd.
A Python Virtual Environment or Docker container.

The best way to use the development files, is to copy them to the root directory where you have your repositories cloned.
For example, see the file/folder structure below.

```shell
├── git_projects
│   ├── ansible-avd
│   ├── ansible-cvp
│   ├── ansible-eos
│   ├── eve-ng-lab
│   ├── netdevops-examples
│   │
│   ├── Dockerfile
│   ├── Makefile
│   ├── requirements-dev.txt
│   ├── requirements.txt

```

## Python Virtual Environment

### Install Python3 Virtual Environment

```shell
# install virtualenv via pip3
$ sudo pip3 install virtualenv

```

```shell
# Configure Python virtual environment
$ virtualenv -p python3 .venv
$ source .venv/bin/activate

# Install Python requirements
$ pip install -r requirements.txt

```

## Docker Container for Ansible Testing and Development

The docker container approach for development can be used to ensure that everybody is using the same development environment while still being flexible enough to use the repo you are making changes in. You can inspect the Dockerfile to see what packages have been installed.
The container will mount the current working directory, so you can work with your local files.

The ansible version is passed in with the docker build command using ***ANSIBLE*** variable.  If the ***ANSIBLE*** variable is not used the Dockerfile will by default set the ansible version to 2.9.2

Before you can use a container, you must install Docker CE on your workstation: https://www.docker.com/products/docker-desktop

### Build Docker Container

In addition to the `Dockerfile`, a `Makefile` is provided to help provision the container a single step. A user can pass the ansible version number to make and alter the default ansible-version number.  This allows a user to setup multiple containers running differing versions of ansible.

```shell
make build                        # Use default version of Ansible
make build ANSIBLE_VERSION=2.9.5  # Explicitly set Ansible version to 2.9.5

docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ansible_avd         2.9.6               5291937a2214        33 minutes ago      795MB
ansible_avd         2.9.5               27f648c4c249        46 hours ago        912MB
```

### Run Docker Container

```shell
make run                        # Use default version of Ansible
make run ANSIBLE_VERSION=2.9.5  # Explicitly set Ansible version to 2.9.5

docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
e682058d7dae        ansible_avd:2.9.5   "/bin/sh"           6 seconds ago       Up 5 seconds                            ansible_avd_2.9.5
540a8e778907        ansible_avd:2.9.6   "/bin/sh"           38 seconds ago      Up 37 seconds                           ansible_avd_2.9.6
```

### Stop Docker Container

Another make target (clean) has been created to stop and remove the container once the user is finished with it.

```shell
make clean                       # Clean default version of Ansible
make clean ANSIBLE_VERSION=2.9.5 # Explicitly clean Ansible version to 2.9.5

docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

## Getting started Script

### Step by step installation process

```shell
mkdir git_projects
cd git_projects
git clone https://github.com/aristanetworks/ansible-avd.git
git clone https://github.com/aristanetworks/ansible-cvp.git
git clone https://github.com/aristanetworks/netdevops-examples.git
cp ansible-avd/development/* ./
make build
make run
```

### One liner installation

```shell
$ sh -c "$(curl -fsSL https://raw.githubusercontent.com/aristanetworks/ansible-avd/master/development/install.sh)"
```
