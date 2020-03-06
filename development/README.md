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

### Start Docker Container

In addition to the `Dockerfile`, a `Makefile` is provided to help provision the container a single step. A user can pass the ansible version number to make and alter the default ansible-version number.  This allows a user to setup multiple containers running differing versions of ansible.

```shell
make                        # Use default version of Ansible
make ANSIBLE_VERSION=2.9.5  # Explicitly set Ansible version to 2.9.5

docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
43e8e095e1f5        ansible_avd:2.9.5   "/bin/sh"           26 seconds ago       Up 25 seconds                           ansible_avd_2.9.5
3ee4c555bca5        ansible_avd:2.9.2   "/bin/sh"           About a minute ago   Up About a minute                       ansible_avd_2.9.2

```

### Stop Docker Container

Another make target (clean) has been created to stop and remove the container once the user is finished with it.

```shell
make clean                       # Clean default version of Ansible
make ANSIBLE_VERSION=2.9.5 clean # Explicitly clean Ansible version to 2.9.5

docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
