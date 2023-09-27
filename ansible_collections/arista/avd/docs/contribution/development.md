<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Development Tips & Tricks

## Overview

Two methods can be used to get Ansible up and running quickly with all the requirements to leverage ansible-avd: a Python Virtual Environment or a Docker container.

The best way to use the development files is to copy them to the root directory where your repositories are cloned. For example, see the file/folder structure below.

```shell
├── git_projects
│   ├── ansible-avd
│   ├── ansible-cvp
│   ├── netdevops-examples
|   ├── <YOUR OWN TESTING REPOSITORY>
│   ├── Makefile
```

## Build a local environment

Please refer to [Setup environment page](./setup-environment.md)

Once installed, use `dev-start` command to bring up all the required containers:

- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) for AVD documentation listening on port `localhost:8000`
- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) or CVP documentation listening on port `localhost:8001`
- An [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) with a pseudo-terminal connected to a shell for Ansible execution

## Docker tips

The Docker container approach for development can be used to ensure that everybody is using the same development environment while still being flexible enough to use the repository you are making changes to. You can inspect the Dockerfile to see what packages have been installed. The container will mount the current working directory so that you can work with your local files.

The Ansible version is passed in with the Docker build command using the **`ANSIBLE_VERSION`** variable. If the variable isn't defined, the Dockerfile will, by default, set the Ansible version to what's specified in the AVD requirements.

Before you can use a container, you must install [**Docker CE**](https://www.docker.com/products/docker-desktop) and [**docker-compose**](https://docs.docker.com/compose/) on your workstation.

Since the AVD Docker image is now automatically published on [**docker-hub**](https://hub.docker.com/repository/docker/avdteam/base), a dedicated repository is available on [**Arista NetDevOps Community**](https://github.com/arista-netdevops-community/docker-avd-base).

```shell
# Start development stack
$ make start
docker-compose -f ansible-avd/development/docker-compose.yml up -d
Recreating development_ansible_1    ... done
Recreating development_webdoc_cvp_1 ... done
Recreating development_webdoc_avd_1 ... done

# List containers started with stack
$ docker-compose -f ansible-avd/development/docker-compose.yml ps
        Name                       Command               State           Ports
-----------------------------------------------------------------------------
ansible_avd   /bin/sh -c while true; do  ...   Up
webdoc_avd    sh -c pip install -r ansib ...   Up      0.0.0.0:8000->8000/tcp
webdoc_cvp    sh -c pip install -r ansib ...   Up      0.0.0.0:8001->8000/tcp

# Get a shell with ansible (if not in shell from previous command)
$ make dev-run
docker-compose -f ansible-avd/development/docker-compose.yml exec ansible zsh
Agent pid 52
➜  /projects

# Test MKDOCS access (outside of development container)
$ curl -s http://127.0.0.1:8000 | head -n 10
<!doctype html>
<html lang="en" class="no-js">
  <head>

      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">

# Stop development stack
$ make dev-stop
docker-compose -f ansible-avd/development/docker-compose.yml kill &&\
        docker-compose -f ansible-avd/development/docker-compose.yml rm -f
Killing development_ansible_1 ... done
Killing development_webdoc_1  ... done
Going to remove development_ansible_1, development_webdoc_1
Removing development_ansible_1 ... done
Removing development_webdoc_1  ... done
```

## Development tools

### Pre-commit hook

[pre-commit](https://github.com/aristanetworks/ansible-avd/blob/devel/.pre-commit-config.yaml) can run standard hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. Pointing these issues out before code review allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

Repository implements the following hooks:

- `trailing-whitespace`: Fix trailing whitespace. If found, the commit is stopped, and you must rerun the commit process.
- `end-of-file-fixer`: Like `trailing-whitespace`, this hook fixes the wrong end of the file and stops your commit.
- `check-yaml`: Checks that all YAML files are valid.
- `check-added-large-files`: Check if no large file is included in the repository.
- `check-merge-conflict`: Validate there is no `MERGE` syntax related to an invalid merge process.
- `pylint`: Run Python linting with settings defined in [pylintrc](https://github.com/aristanetworks/ansible-avd/blob/devel/pylintrc).
- `yamllint`: Validate all YAML files using configuration from [yamllintrc](https://github.com/aristanetworks/ansible-avd/blob/devel/.github/yamllintrc).
- `ansible-lint`: Validate YAML files with Ansible proven practices, patters, and behaviors.
- `Flake8`: Style guide enforcement for Python code base.
- `markdownlint-cli`: Validates markdown files for common errors as referenced [here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md).

#### Installation

`pre-commit` is part of [**development requirements**](https://github.com/aristanetworks/ansible-avd/blob/devel/development/requirements-dev.txt). To install, run `pip command` in **ansible-avd** folder:

```shell
$ pip install -r development/requirements-dev.txt
...
```

#### Run pre-commit manually

To run `pre-commit` manually before your commit, use this command:

```shell
pre-commit run
[WARNING] Unstaged files detected.

[INFO] Stashing unstaged files to /Users/xxx/.cache/pre-commit/patch1590742434.

Trim Trailing Whitespace.............................(no files to check)Skipped
Fix End of Files.....................................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Check for added large files..........................(no files to check)Skipped
Check for merge conflicts............................(no files to check)Skipped
Check for Linting error on Python files..............(no files to check)Skipped
Check for Linting error on YAML files................(no files to check)Skipped
Check for ansible-lint errors............................................Passed

[INFO] Restored changes from /Users/xxx/.cache/pre-commit/patch1590742434.
```

The command will automatically detect changed files using `git status` and run tests according to their type.

!!! note
    This process is also implemented in project CI to ensure code quality and compliance with the Ansible development process.

### Configure Git hook

To automatically run tests when running a commit, configure your repository with the following command:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

To remove the installation, use the `uninstall` option.

### Check 404 links

To validate documentation, you should check for *not found* links in your local version of the documentation. This test requires running the mkdocs container as explained in [installation documentation](./setup-environment.md).

In a shell, run the following make command. It starts a container in the AVD documentation network and leverages [`muffet`](https://github.com/raviqqe/muffet) tool to check for any 404 HTTP codes:

```shell
$ check-avd-404
docker run --network container:webdoc_avd raviqqe/muffet \
    http://127.0.0.1:8000 \
    -e ".*fonts.gstatic.com.*" \
    -e ".*edit.*" \
    -f --limit-redirections=3 \
    --timeout=60
http://127.0.0.1:8000/docs/installation/development/
        404     http://127.0.0.1:8000/docs/installation/development/setup-environment2.md
make: *** [check-avd-404] Error 1
```

> This process is also implemented in project CI to protect documentation against dead links.
