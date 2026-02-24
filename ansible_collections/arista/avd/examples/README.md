---
title: How to use AVD examples  # This title is used for search results
link: https://avd.arista.com/stable/ansible_collections/arista/avd/examples/index.html
---
<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# How to use AVD examples

## Introduction

Examples include simple inventories showing how to build common network designs with AVD. AVD examples cover essential deployment aspects; however, they may be missing some fine-tuning required for a production network. Use them for inspiration, but avoid copying AVD examples into your production inventory until you fully understand how they work.

You can use AVD examples in 2 different ways:

- As an interactive lab (AVD playground).
- As a reference inventory only, without supporting lab.

## AVD Playground

AVD playground is an interactive, Cloud-based lab environment sponsored by Arista. To get started, simply sign in at [labs.arista.com](https://labs.arista.com/) and click the button below to launch the lab.

[Start AVD Playground :octicons-play-16:](https://labs.arista.com/launch?lab_type=avd-playground&origin=tech-lib){ .md-button .md-button--primary target=_blank}

Once the playground is ready to use, use the interactive menu at the bottom of the [code-server](https://github.com/coder/code-server) UI to pick the AVD release and the example you want to test. Some examples and older AVD releases may not include lab definitions; in that case, the lab selector menu will prompt you to choose a different option. Please select 6.0.0 releases or newer.

!!! tip

    If you don't see the "Start AVD Playground" button on the guide corresponding to a specific example, this example is not supported in AVD Playground. If this is the case, select a different one.

Once you select an example supported by a lab definition, it will be extracted to the code-server workspace. Open a new terminal and type `make start` to start the lab.

!!! note

    Due to infrastructure costs and security protocols, AVD Playgrounds are exclusively available to registered Arista customers with an active support contract.
    Users are expected to adhere to the EULA terms accepted during registration and use the environment for its intended professional purposes.
    If you do not currently have the required access level, please contact your Arista account team.

For additional documentation regarding AVD playgrounds and other community labs check [aclabs.arista.com](https://aclabs.arista.com/). The corresponding [GitHub repository](https://github.com/aristanetworks/aclabs) is used to build container images powering AVD playgrounds.

AVD playground lab files are available for [download on aclabs.arista.com](https://aristanetworks.github.io/aclabs/lab_archives/avd-playground.tar.gz). The download option is for skilled users only that can manage the environment without extra support.

## AVD as Reference Inventory

If you don't have access to AVD playgrounds, simply build a working Ansible environment with the AVD collection installed to start testing examples.
You can build an AVD environment by installing all requirements on a dedicated VM or inside a virtual environment. Please refer to the [installation](../../../../docs/installation/collection-installation.md) section for the details.
Alternatively, you can use the [AVD universal container images](../../../../docs/containers/overview.md) to quickly spin up a working AVD environment.
Once the environment is ready, you can extract all examples with:

```shell
ansible-playbook arista.avd.install_examples
```

Alternatively, you can copy a specific example to your current directory:

```shell
cp -r /home/${USER}/.ansible/collections/ansible_collections/arista/avd/examples/<example-name>/* .
```

!!! info

    `/home/${USER}/.ansible/collections/ansible_collections/arista/avd/examples` is the default Ansible path to the AVD collection. It may differ if your environment is not using the default path.

Once the example is copied to your working directory / container workspace, simply start playing with the inventory. For example, change a few variables, run the `ansible-playbook build.yml` command and check the diff in configurations and documentation.
