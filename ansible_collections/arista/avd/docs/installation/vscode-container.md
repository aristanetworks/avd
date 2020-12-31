# Setup Ansible AVD with VSCode container

Arista AVD provides an easy way to setup a lab or demo environment by using a pre-configured [VScode container](https://github.com/arista-netdevops-community/docker-avd-vscode) with a web interface to connect and edit files.

This container can be leveraged in different ways like demo, remote lab, training sessions, development solution, ... In this page we will focus only on how-to play with AVD demo content.

## VScode container overview

This container is based on a [AVD base image](https://hub.docker.com/repository/docker/avdteam/base) with an installation of VScode server using [code-server](https://github.com/cdr/code-server/) implementation.

This container comes with a set of options available to let you customize your own environment:

### Generic settings

- __`AVD_MODE`__: If set to `demo`, container will install AVD content to test it from `get.avd.sh`. (Supported mode: `['demo', 'toi']`)
- __`AVD_PASSWORD`__: Allow user to set a password to use for VScode authentication. If not set, access is not protected by any password.
- __`AVD_GIT_USER`__: Username to configure in `.gitconfig` file.
- __`AVD_GIT_EMAIL`__: Email to configure in `.gitconfig` file.
- __`AVD_USER_EXTENSIONS_FILE`__: Allow user to installed additional VScode extensions
- __`AVD_USER_REPOS`__: Path to a text file in your container with a list of repository to clone (1 repository per line)
- __`AVD_USER_SCRIPT`__: Path to a shell script to execute during entrypoint execution.

### User settings

These settings must be used to mount and edit file from your physical host.

- __`AVD_UID`__: set uid for avd user in container.
- __`AVD_GID`__: set gid for avd user in container.

Container also comes with docker installed and in case you want to run docker from your container, you can expose your local docker socket from your host to your container:

__Docker Socket on Linux / Macos__

```bash
-v /var/run/docker.sock:/var/run/docker.sock
```

__Docker Socket on Windows__

```bash
-v //var/run/docker.sock:/var/run/docker.sock
```

## Requirements

To run this container, few requirements are expected:

- Docker installed on a host: laptop, VM, server or anything that run docker
- Git configured with at least username and email

```bash
# Set your user name to display in git commit
$ git config --global user.name "John Doe"

# Set your email address to use in git commit
$ git config --global user.email johndoe@example.com
```

## Get AVD demo in VSCode

We will ask container to automatically install the following content in your container:

- Ansible Arista Validated Design collection using GIT (devel) version.
- Ansible Arista Cloudvision collection using GIT (devel) version.
- AVD with Cloudvision demo repository

!!! note Customize your exposed port
    Container will listen on port `8080` but it can be changed accordingly by using docker cli

```bash
docker run --rm -it -d \
    -e AVD_MODE=demo \
    -e AVD_GIT_USER="$(git config --get user.name)" \
    -e AVD_GIT_EMAIL="$(git config --get user.email)" \
    -p 8080:8080 \
    avdteam/vscode:latest
```

!!! warning Storage management
    In this setup, container will be destroyed after you stop it. And because we do not share any volume, all changes will be lost.
