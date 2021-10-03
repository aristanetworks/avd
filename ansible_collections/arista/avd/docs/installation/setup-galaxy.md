# Collection installation via ansible-galaxy

## Install from Ansible Galaxy

__arista.avd__ collection is available on [Ansible Galaxy](https://galaxy.ansible.com/arista/avd) server and can be automatically installed on your system.

### Latest version

```shell
$ ansible-galaxy collection install arista.avd
```

### Install a specific version

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

### Use ansible requirements file

This approach gives you option to use arista.avd directly from github or via ansible galaxy.

#### Set arista.avd from github

The `version` knob supports any [branch](https://github.com/aristanetworks/ansible-avd/branches) available on github and also any [tag or version](https://github.com/aristanetworks/ansible-avd/releases) available in the repository

```yaml
collections:
  - name: https://github.com/aristanetworks/ansible-avd.git#ansible_collections/arista/avd
    type: git
    version: devel
```

#### Set arista.avd from ansible-galaxy

The `version` knob supports any [tag or version](https://galaxy.ansible.com/arista/avd) available in ansible-galaxy servers.

```yaml
collections:
  - name: arista.avd
    version: 3.0.0-rc2
```

#### Install required collection

With ansible requirements file, you can install all required collections with the following commands

```bash
➜  ~ ansible-galaxy collection install -r requirements.yml
Starting galaxy collection install process
Process install dependency map
Cloning into '/home/avd/.ansible/tmp/ansible-local-2741xjxm4bv/tmp07wpis9v/avd-ci-testrgl6qy3w'...
remote: Enumerating objects: 1945, done.
remote: Counting objects: 100% (1945/1945), done.
remote: Compressing objects: 100% (975/975), done.
remote: Total 1945 (delta 895), reused 1921 (delta 871), pack-reused 0
Receiving objects: 100% (1945/1945), 3.44 MiB | 2.72 MiB/s, done.
Resolving deltas: 100% (895/895), done.
Already on 'main'
Your branch is up to date with 'origin/main'.
Starting collection install process
Installing 'arista.avd:*' to '/home/avd/.ansible/collections/ansible_collections/arista/avd'
[...]
➜  ~ ansible-galaxy collection list

# /home/avd/.ansible/collections/ansible_collections
Collection        Version
----------------- -------
ansible.netcommon 2.4.0
ansible.utils     2.4.1
arista.cvp        3.2.0
arista.eos        3.1.0
arista.avd       *
```

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
