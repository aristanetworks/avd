# Requirements

## Arista EOS version

- EOS __4.21.8M__ or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista Cloudvision

If you leverage [Cloudvision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [Cloudvision ansible collection](https://cvp.avd.sh/)

## Python

- Python __3.6.8__ or later

## Supported Ansible Versions

- ansible __2.10.7__ or later
- previous ansible version not supported as avd is shipped as an [ansible collection](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)

## Additional Python Libraries required

- netaddr `0.7.19`
- Jinja2 `2.11.3`
- treelib `1.5.5`
- cvprac `1.0.5`
- paramiko `2.7.1`
- jsonschema `3.2.0`
- requests `2.25.1`
- PyYAML `5.4.1`
- md-toc `7.1.0`

### Python requirements installation

In a shell, run following command:

```shell
$ pip3 install -r ansible_collections/arista/avd/requirements.txt
```

[`requirements.txt`](https://github.com/aristanetworks/ansible-avd/blob/devel/ansible_collections/arista/avd/requirements.txt) has the following content:

```text
netaddr==0.7.19
Jinja2==2.11.3
treelib==1.5.5
cvprac==1.0.5
paramiko==2.7.1
jsonschema==3.2.0
requests==2.25.1
PyYAML==5.4.1
md-toc==7.1.0

```

!!! warning
    Depending of your operating system settings, `pip3` might be replaced by `pip`.

## Ansible runner requirements

A optional docker container is available with all the requirements already installed. To use this container, Docker must be installed on your ansible runner.

To install Docker on your system, you can refer to the following page: [Docker installation step by step](https://docs.docker.com/engine/installation/)

Or if you prefer you can run this oneLiner installation script:

```shell
$ curl -fsSL get.docker.com | sh
```

In addition, docker-compose should be considered to run a stack of containers: https://docs.docker.com/compose/install/
