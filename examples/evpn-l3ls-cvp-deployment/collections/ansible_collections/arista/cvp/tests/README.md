# Ansible CVP test environment

## About

This directory contains all the material to run basic test during development of modules. Please consider this content as unstable and not production grade.

## Run tests

> This section does not cover how to build a development environment

1. Run test per module:

In this command only a subset of build playbook will be executed, mainly to validate one module execution:

```
$ make ANSIBLE_TAG=<YOUR MODULE NAME> unit
```

__ANSIBLE_TAG__ supports following options:
- _container_
- _device_
- _configlet_

2. Run all tests:

In this command all part of the playbook are executed to build a topology

```
$ make run
```

3. Revert topology

This command executes a playbook to revert topology to a single container (`staging`) with all devices and unbind configlets from devices.

```
$ make reset
```

## Makefile options

All these commands support an option to select target:

__ANSIBLE_TARGET__ supports following options:
- _cvp_2018_
- _cvp_2019_

