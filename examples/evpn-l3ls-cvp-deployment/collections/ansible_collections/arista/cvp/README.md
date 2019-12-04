# Ansible Modules for Arista CloudVision Platform

## About

[Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system through [CloudVision platform (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision). This roles includes a set of ansible modules that perform specific configuration tasks on CVP server. These tasks include: collecting facts, managing configlets, containers, build provisionning topology and running tasks. For installation, you can refer to [specific section](#git-installation) of this readme.

## Modules overview

This repository provides content for Ansible's collection __arista.cvp__ with following content:

- __arista.cvp.cv_facts__ - Collect CVP facts from server like list of containers, devices, configlet and tasks.
- __arista.cvp.cv_configlet__] -  Manage configlet configured on CVP.
- __arista.cvp.cv_container__ -  Manage container topology and attach configlet and devices to containers.
- __arista.cvp.cv_device__ - Manage devices configured on CVP
- __arista.cvp.cv_task__ - Run tasks created on CVP.

This collection supports CVP version `2018.2.x` and `2019.1.x`

## License

Project is published under [Apache License](LICENSE).

## Ask a question

Support for this `arista.cvp` collection is provided by the community directly in this repository. Easiest way to get support is to open [an issue](https://github.com/aristanetworks/ansible-cvp/issues).

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we’ll be able to merge it.

You can also open an [issue](https://github.com/aristanetworks/ansible-cvp/issues) to report any problem or to submit enhancement.

A more complete [guide for contribution](https://github.com/aristanetworks/ansible-cvp/contributing.md) is available in the repository
