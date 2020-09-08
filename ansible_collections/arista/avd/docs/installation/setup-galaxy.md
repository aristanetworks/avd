# Collection installation via ansible-galaxy

## Install from Ansible Galaxy

__arista.avd__ collection is available on [Ansible Galaxy](https://galaxy.ansible.com/arista/avd) server and can be automatically installed on your system.

### Latest version

```shell
$ ansible-galaxy collection install arista.avd
```

### Install specific version

```shell
$ ansible-galaxy collection install arista.avd:==1.0.2
```

You can specify multiple range identifiers which are split by ,. You can use the following range identifiers:

- `*`: Any version, this is the default used when no range specified is set.
- `!=`: Version is not equal to the one specified.
- `==`: Version must be the one specified.
- `>=`: Version is greater than or equal to the one specified.
- `>`: Version is greater than the one specified.
- `<=`: Version is less than or equal to the one specified.
- `<`: Version is less than the one specified.

### Install in specific directory

If you want to install collection in a specific directory part of your project, you can call `ansible-galaxy` and update your `ansible.cfg`

```shell
# Install collection under ${PWD/collections/}
$ ansible-galaxy collection install arista.avd -p collections/

# Update ansible.cfg file
$ vim ansible.cfg
collections_paths = ${PWD}/collections:~/.ansible/collections:/usr/share/ansible/collections
```

### Upgrade installed AVD collection

You can use `-f` to force installation of a new version for any installed collection:

```shell
$ ansible-galaxy collection install -f arista.avd
Process install dependency map
Starting collection install process
Installing 'arista.avd:1.0.2' to '/root/.ansible/collections/ansible_collections/arista/avd'
```

> Note: Ansible community is discussing option to implement specific triggers to support upgrade under [issue #65699](https://github.com/ansible/ansible/issues/65699)

## Ansible resources

You can find some additional information about how to use ansible's collections on the following Ansible pages:

- [Ansible collection user guide](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
