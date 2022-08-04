# Installation using Git

Using Git as source of collection in Ansible provides an easy way to implement all the changes once they're part of the development branch without waiting for a new tagged version shipped to ansible-galaxy.

## Use Git as source of collection

In this setup, Git repository will be used by Ansible as collection. It's useful when working on feature development as we can change Git branch and test code live.

### Get repository locally

```shell
# Clone repository
git clone https://github.com/aristanetworks/ansible-avd.git

# Move to git folder
cd ansible-avd
```

### Update your `ansible.cfg`

In your project, update your `ansible.cfg` file to point __collection_paths__ to your local version of ansible-avd

- Get full path to your newly cloned AVD repository.

```shell
# Get your current location
$ pwd
/path/to/ansible/avd/collection_repository
```

- Configure your project to use AVD repository as source of collections:

```ini
# Update your ansible.cfg in your playbook project
# $ vim ansible.cfg
[default]
...
collections_paths = /path/to/ansible/avd/collection_repository
...
```

## Build & install collection from Git

In this approach, an Ansible collection package is built from current Git version and installed locally.

### Clone repository

```shell
git clone https://github.com/aristanetworks/ansible-avd.git
cd ansible-avd
```

### Build and install collection

This section should be used only to test collection packaging and to create an offline package to ship on your internal resources if required.

```shell
ansible-galaxy collection build --force ansible_collections/arista/avd
ansible-galaxy collection install arista-avd-<VERSION>.tar.gz
```
