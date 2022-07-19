# Setup Ansible AVD with VSCode container

Arista AVD provides an easy way to set up a lab or demo environment using a pre-configured [VScode container](https://github.com/arista-netdevops-community/docker-avd-vscode) with a web interface to connect and edit files.

We can leverage this container in different ways like a demo, remote lab, training sessions, or development solution. However, on this page, we will focus only on how to play with AVD demo content.

## VScode container overview

This container is based on a [AVD base image](https://hub.docker.com/repository/docker/avdteam/base) with an installation of VScode server using [code-server](https://github.com/cdr/code-server/) implementation.

This container comes with a set of options available to let you customize your environment:

### Generic settings

- __`AVD_MODE`__: If set to `demo`, container will install AVD content to test it from `get.avd.sh`. (Supported mode: `['demo', 'toi']`).
- __`AVD_PASSWORD`__: Allow user to set a password for VScode authentication. If not set, access isn't protected by any password.
- __`AVD_GIT_USER`__: Username to configure in `.gitconfig` file.
- __`AVD_GIT_EMAIL`__: Email to configure in `.gitconfig` file.
- __`AVD_USER_EXTENSIONS_FILE`__: Allow user to install additional VScode extensions.
- __`AVD_USER_REPOS`__: Path to a text file in your container with a list of repository to clone (one repository per line).
- __`AVD_USER_SCRIPT`__: Path to a shell script to execute during entrypoint execution.

### User settings

These settings must be used to mount and edit file from your physical host.

- __`AVD_UID`__: Set uid for AVD user in container.
- __`AVD_GID`__: Set gid for AVD user in container.

The container also comes with Docker installed, and in case you want to run Docker from your container, you can expose your local Docker socket from your host to your container:

## Requirements

To run this container, few requirements are expected:

- Docker [installed on a host](https://docs.docker.com/get-docker/): laptop, VM, server, or anything that runs Docker
- Git configured with at least username and email

```bash
# Set your user name to display in git commit
$ git config --global user.name "John Doe"

# Set your email address to use in git commit
$ git config --global user.email johndoe@example.com
```

## Get AVD demo in VSCode

We will ask the container to install the following content in your container automatically:

- Ansible Arista Validated Design collection using Git (devel) version.
- Ansible Arista CloudVision collection using Git (devel) version.
- AVD with CloudVision demo repository

!!! note Customize your exposed port
    The container will listen on port `8080`, but we can be change it accordingly by using Docker CLI

```bash
docker run --rm -it -d \
    -e AVD_MODE=demo \
    -e AVD_GIT_USER="$(git config --get user.name)" \
    -e AVD_GIT_EMAIL="$(git config --get user.email)" \
    -p 8080:8080 \
    avdteam/vscode:latest
```

!!! warning Storage management
    In this setup, the container will be destroyed after you stop it. Since we don't share any volumes, all changes will be lost.

Once your container is started, confirm with the following Docker command:

```bash
$ docker ps
CONTAINER ID   IMAGE                   COMMAND                  CREATED          STATUS          PORTS                    NAMES
0fd39cc2dd3d   avdteam/vscode:latest   "/bin/entrypoint.sh"     10 seconds ago   Up 9 seconds    0.0.0.0:8080->8080/tcp   inspiring_germain
```

You should be able to connect to your VSCode instance using your favorite browser with the following URL:

```bash
http://<IP ADDR of DOCKER Machine>:8080/?folder=/home/avd/arista-ansible
```

![VSCode demo Overview](../_media/vscode-container-demo-overview.png)

## Customize your container

Once you run your first AVD demo, you may want to not use non-volatile storage or install your repositories.

### Mount your local folder

The first option is to mount one of your local folders to save your work from your container. Considering your local folder is empty, you can add this line to your Docker CLI:

```bash
-v ${PWD}/:/home/avd/arista-ansible
```

Complete CLI example below:

```bash
docker run --rm -it -d \
    -e AVD_GIT_USER="$(git config --get user.name)" \
    -e AVD_GIT_EMAIL="$(git config --get user.email)" \
    -v ${PWD}/:/home/avd/arista-ansible \
    -p 8080:8080 \
    avdteam/vscode:latest
```

### Install additional repositories

Now, you want to ship your own demo in your container with Git clone instead of local file sharing, you can leverage the following option: __`AVD_USER_REPOS`__

```bash
docker run --rm -it -d \
    -e AVD_GIT_USER="$(git config --get user.name)" \
    -e AVD_GIT_EMAIL="$(git config --get user.email)" \
    -e AVD_USER_REPOS=/home/avd/arista-ansible/my_repos.txt \
    -v ${PWD}/:/home/avd/arista-ansible \
    -p 8080:8080 \
    avdteam/vscode:latest
```

And then your [`my_repos.txt`](https://github.com/arista-netdevops-community/docker-avd-vscode/blob/master/tests/user-repos.txt) file should be like:

```text
https://github.com/aristanetworks/ansible-avd.git
https://github.com/aristanetworks/ansible-cvp.git
```

!!! note Repository file path
    By default, Docker can't load a file from your host. The path you provide in `AVD_USER_REPOS` must be configured using a shared volume.

For more details and options, you can check our repository for this container: __[arista-netdevops-community/docker-avd-vscode](https://github.com/arista-netdevops-community/docker-avd-vscode)__
