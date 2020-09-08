# Requirements

## Arista EOS version

- EOS __4.21.8M__ or later
- Roles validated with eAPI transport -> `ansible_connection: httpapi`

## Python

- Python __3.6.8__ or later

## Supported Ansible Versions

- ansible 2.9.2 or later

## Additional Python Libraries required

- [Jinja2](https://pypi.org/project/Jinja2/)  `2.10.3`
- [netaddr](https://pypi.org/project/netaddr/) `0.7.19`
- [requests](https://pypi.org/project/requests/) `2.22.0`
- [treelib](https://pypi.org/project/treelib/) `1.5.5`
- [cvprac](https://github.com/aristanetworks/cvprac) `1.0.4`

### Python requirements installation

In a shell, run following command:

```shell
$ pip3 install -r development/requirements.txt
```

[`requirements.txt`](https://github.com/aristanetworks/ansible-avd/blob/devel/development/requirements.txt) has the following content:

```text
ansible==2.9.6
netaddr==0.7.19
Jinja2==2.10.3
requests==2.22.0
treelib==1.5.5
cvprac==1.0.4
```

> Depending of your operating system settings, `pip3` might be replaced by `pip`.

## Ansible runner requirements

A optional docker container is available with all the requirements already installed. To use this container, Docker must be installed on your ansible runner.

To install Docker on your system, you can refer to the following page: [Docker installation step by step](https://docs.docker.com/engine/installation/)

Or if you prefer you can run this oneLiner installation script:

```shell
$ curl -fsSL get.docker.com | sh
```

In addition, docker-compose should be consider as easy setup leverage this tool to run a stack of containers: https://docs.docker.com/compose/install/
