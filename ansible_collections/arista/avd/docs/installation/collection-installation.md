# Collection installation

These instructions are for regular users to install via Ansible Galaxy. To setup a development environment use [these](../contribution/setup-environment.md) instructions.

__arista.avd__ can also be consumed using the ["AVD All-in-one" container](https://github.com/arista-netdevops-community/avd-all-in-one-container).

## Install from Ansible Galaxy

__arista.avd__ collection is available on [Ansible Galaxy](https://galaxy.ansible.com/arista/avd) server and can be automatically installed on your system.

Make sure to install [Python requirements](requirements.md#additional-python-libraries-required) afterwards.

### Latest version

```shell
$ ansible-galaxy collection install arista.avd
```

!!! warning
    If you have an `ansible.cfg` file in the directory where you run `ansible-galaxy`, it may affect the directory under which the collection and dependencies will be installed.

### Install a specific version

```shell
$ ansible-galaxy collection install arista.avd:==3.0.0
```

You can specify multiple range identifiers which are split by ,. You can use the following range identifiers:

- `*`: Any version, this is the default used when no range specified is set.
- `!=`: Version is not equal to the one specified.
- `==`: Version must be the one specified.
- `>=`: Version is greater than or equal to the one specified.
- `>`: Version is greater than the one specified.
- `<=`: Version is less than or equal to the one specified.
- `<`: Version is less than the one specified.

### Install latest `devel` version from AVD GitHub

```shell
$ ansible-galaxy collection install git+https://github.com/aristanetworks/ansible-avd.git#/ansible_collections/arista/avd/,devel
```

!!! note
    Collection dependencies like `ansible-cvp` will be installed from ansible-galaxy unless installed first using similar github source.

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

You can use `-U` to upgrade to a new version for any installed collection:

```shell
$ ansible-galaxy collection install -U arista.avd
Process install dependency map
Starting collection install process
Installing 'arista.avd:3.0.0' to '/root/.ansible/collections/ansible_collections/arista/avd'
```

## Ansible resources

You can find some additional information about how to use ansible's collections on the following Ansible pages:

- [Ansible collection user guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
