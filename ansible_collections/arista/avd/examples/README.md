---
title: How to use AVD examples  # This title is used for search results
link: https://avd.arista.com/stable/ansible_collections/arista/avd/examples/index.html
---
<!--
  ~ Copyright (c) 2025-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# How to use AVD examples

## Introduction

Examples are simple inventories showing how to build common network designs with AVD.
AVD examples are covering all essential deployments aspects, however they may miss some fine tuning required for production network. Use them as an inspiration, but avoid copy-pasting AVD examples to your prod inventory until you fully understand how they work. Be mindful to your production network to keep it healthy.

You can use AVD examples in 2 different ways:

- As an interactive lab (AVD playground)
- As a reference inventory only, without supporting lab

Some AVD examples are also augmented with guides explaining how they work. However the most important part of every example is the inventory. Labs and guides are optional.

## AVD Playground

## AVD as Reference Inventory

If you don't have access to AVD playgrounds, it's enough to build a working Ansible environment with AVD collection installed to start testing examples.
You can build an AVD environment by installing all requirements on a dedicated VM or inside a virtual environment / uv. Please refer to the installation section for the details.
Alternatively you can use AVD universal container images to spin a working AVD environmet quickly.
Once the environment is ready, you can extract all examples with:

```shell
ansible-playbook arista.avd.install_examples
```

Alternatively you can copy specific example to your current directory:

```shell
cp -r /home/${USER}/.ansible/collections/ansible_collections/arista/avd/examples/<example-name>/* .
```

`/home/${USER}/.ansible/collections/ansible_collections/arista/avd/examples` is the default Ansible path to AVD collection. It can be different if your environment is not using the default path.

Once the example is copied to your working directory / container workspace - simply start playing with the inventory. For example, change a few variables, run `ansible-playbook build.yml` command and check the diff in configurations and documentation.
