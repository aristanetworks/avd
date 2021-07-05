# Requirements

## Arista EOS version

- EOS __4.21.8M__ or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Arista Cloudvision

If you leverage [Cloudvision](https://www.arista.com/en/products/eos/eos-cloudvision) deployment with AVD, your CV instance must be supported by [Cloudvision ansible collection](https://cvp.avd.sh/)

## Python

- Python __3.6.8__ or later

## Supported Ansible Versions

- ansible __2.10.0__ or later

## Additional Python Libraries required

- netaddr
- Jinja2
- treelib
- cvprac
- paramiko
- jsonschema
- requests
- PyYAML
- md-toc

### Python requirements installation

In a shell, run the following command:

```shell
$ pip3 install -r ansible_collections/arista/avd/requirements.txt
```

```pip
--8<--
requirements.txt
--8<--
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
