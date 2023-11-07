<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD Dev Containers Overview

> WARNING: AVD Dev Containers are currently in the early preview phase and not officially supported for any production cases.
> They can be still very useful for development and testing. Please report any issues and optimization suggestions.

## Why Dev Containers

Building a functional Ansible environment can be a challenging task. A manually created Ansible environment can be broken due to number of reasons:

- Problems with Python and Ansible versions
- Broken dependencies
- Interpreter path issues
- Inconsistent Ansible configuration files
- etc.

Containers can provide a simple and portable way to build a functional and portable Ansible environment. [Dev Containers](https://containers.dev) bring that to the next level by simplifying container build process and extending the functionality. The [Dev Container Specification](https://github.com/devcontainers/spec) was started by Microsoft and has strong community support. Essentially Dev Containers are powered by following:

- [Prebuilt images](https://github.com/devcontainers/images)
- [Features](https://containers.dev/features)

Dev containers can be run locally or remotely, in a private or public cloud, in a variety of [supporting tools and editors](https://containers.dev/supporting).

## AVD Dev Container Variants

The AVD repository provides a number of pre-build dev container images for various use cases:

- **base** - image that is used to build other variants. It is not intended for a direct use.
- **dev** - an image created for AVD contributors and to support quick testing of AVD branches.
- **universal** - an image with pre-installed AVD collection that can be used to build and deploy AVD configuration using a specific AVD version.

All images are based on [Python Slim](https://hub.docker.com/_/python) with some additional features and extensions pre-installed.

## How to Use Dev Containers

Currently the only supported option is using [VSCode](https://code.visualstudio.com/) to start a dev container.

To start using a dev container:

- Install [VScode Dev Containers extension](https://code.visualstudio.com/docs/devcontainers/tutorial)
- Add `.devcontainer/devcontainer.json` to your AVD repository (check examples below for possible dev container definitions).
- Open VSCode command pallette and pick `Dev Containers: Rebuild and Reopen in Container`
- Wait until the build will finish and enjoy running AVD in a container.

If you want to use specific AVD release, use following `devcontainer.json`:

```json
{
    "name": "AVD Universal",
    "image": "ghcr.io/aristanetworks/ansible-avd/universal:python3.11-avd-v4.4.0"
}
```

For AVD contributors following configuration is recommended:

```json
{
    "name": "AVD Development",
    "image": "ghcr.io/aristanetworks/ansible-avd/dev:python3.11",
    "mounts": [
        "source=${localWorkspaceFolder}/ansible_collections/arista/avd,target=/home/avd/.ansible/collections/ansible_collections/arista/avd,type=bind"
    ],
    // run entrypoint script manually as it's ignored by dev container CLI otherwise
    // the dev entrypoint is used to install ansible collections and requirements, as they are not included with the dev version
    // true is required to exit "onCreateCommand" without entering ZSH
    "onCreateCommand": "/bin/entrypoint.sh true"
}
```

If you want to test specific AVD branch or fork without making any changes, use following `devcontainer.json`:

```json
{
    "name": "AVD Development",
    "image": "ghcr.io/aristanetworks/ansible-avd/dev:python3.11",
    "containerEnv": {
        "AVD_GITHUB_REPO": "aristanetworks/ansible-avd",
        "AVD_BRANCH_NAME": "devel"
    },
    // run entrypoint script manually as it's ignored by dev container CLI otherwise
    // the dev entrypoint is used to install ansible collections and requirements, as they are not included with the dev version
    // true is required to exit "onCreateCommand" without entering ZSH
    "onCreateCommand": "/bin/entrypoint.sh true"
}
```

> NOTE: Do not forget to adjust the parameters like AVD version according to you use case.
