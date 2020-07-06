# Installation using GIT

## Build & install collection from git

In this approach, an ansible collection package is built from current git version and installed locally.

### Clone repository

```shell
$ git clone https://github.com/aristanetworks/ansible-avd.git
$ cd ansible-avd
```

### Build and install collection

```shell
$ ansible-galaxy collection build --force ansible_collections/arista/avd
$ ansible-galaxy collection install arista-avd-<VERSION>.tar.gz
```

## Use Git as source of collection

In this setup, git repository will be used by ansible as collection. It is useful when working on feature development as we can change git branch and test code lively.

### Clone repository

```shell
# Clone repository
$ git clone https://github.com/aristanetworks/ansible-avd.git

# Move to git folder
cd ansible-avd
```

### Install python virtual-environment

```shell
# Install virtualenv if not part of your system
$ python -m pip3 install virtualenv
```

### Create virtual environment

```shell
# Create a virtual env named .venv
$ virtualenv --no-site-packages -p $(which python3) .venv

# Activate virtualenv
$ source .venv/bin/activate
```

### Install collection requirements

```shell
# Install repsoitory requirements
$ pip install -r development/requirements.txt
```

### Update your ansible.cfg

In your project, update your `ansible.cfg` file to point __collection_paths__ to your local version of ansible-avd

```shell
# Get your current location
$ pwd
/path/to/ansible/avd/collection_repository

# Update your ansible.cfg
$ vim ansible.cfg
collections_paths = /path/to/ansible/avd/collection_repository
```
