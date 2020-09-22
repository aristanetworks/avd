# Development Tips & Tricks

## Overview

Two methods can be used get Ansible up and running quickly with all the requirements to leverage ansible-avd.
A Python Virtual Environment or Docker container.

The best way to use the development files, is to copy them to the root directory where you have your repositories cloned.
For example, see the file/folder structure below.

```shell
├── git_projects
│   ├── ansible-avd
│   ├── ansible-cvp
│   ├── netdevops-examples
|   ├── <YOUR OWN TESTING REPOSITORY>
│   ├── Makefile
```

## Build local environment

Please refer to [Setup environment page](./setup-environement.md)

Once installed, use `dev-start` command to bring up all the required containers:

- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) for AVD documentation listening on port `localhost:8000`
- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) or CVP documentation listening on port `localhost:8001`
- An [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) with a pseudo terminal connected to shell for ansible execution

## Docker things

he docker container approach for development can be used to ensure that everybody is using the same development environment while still being flexible enough to use the repo you are making changes in. You can inspect the Dockerfile to see what packages have been installed.
The container will mount the current working directory, so you can work with your local files.

The ansible version is passed in with the docker build command using **`ANSIBLE_VERSION`** variable.  If the ***ANSIBLE*** variable is not used the Dockerfile will by default set the ansible version to describe in AVD requirements.

Before you can use a container, you must install [__Docker CE__](https://www.docker.com/products/docker-desktop) and [__docker-compose__](https://docs.docker.com/compose/) on your workstation.

Since docker image is now automatically published on [__docker-hub__](https://hub.docker.com/repository/docker/avdteam/base), a dedicated repository is available on [__Arista Netdevops Community__](https://github.com/arista-netdevops-community/docker-avd-base).

```shell
# Start development stack
$ make dev-start
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

[`pre-commit`](https://github.com/aristanetworks/ansible-avd/blob/devel/.pre-commit-config.yaml) can run standard hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

Repository implements following hooks:

- `trailing-whitespace`: Fix trailing whitespace. if found, commit is stopped and you must run commit process again.
- `end-of-file-fixer`: Like `trailing-whitespace`, this hook fix wrong end of file and stop your commit.
- `check-yaml`: Check all YAML files ares valid
- `check-added-large-files`: Check if there is no large file included in repository
- `check-merge-conflict`: Validate there is no `MERGE` syntax related to a invalid merge process.
- `pylint`: Run python linting with settings defined in [`pylintrc`](https://github.com/aristanetworks/ansible-avd/blob/devel/pylintrc)
- `yamllint`: Validate all YAML files using configuration from [`yamllintrc`](https://github.com/aristanetworks/ansible-avd/blob/devel/.github/yamllintrc)
- `ansible-lint`: Validate yaml files are valid against ansible rules.

#### Installation

`pre-commit` is part of [__development requirememnts__](https://github.com/aristanetworks/ansible-avd/blob/devel/development/requirements-dev.txt). To install, run `pip command` in __ansible-avd__ folder:

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

Command will automatically detect changed files using git status and run tests according their type.

> This process is also implemented in project CI to ensure code quality and compliance with ansible development process.

### Configure git hook

To automatically run tests when running a commit, configure your repository whit command:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

To remove installation, use `uninstall` option.

### Check 404 links

To validate documentation, you should check for _not found_ links in your local version of the documentation. This test requires to run mkdocs container as explained in [installation documentation](./setup-environement.md).

In a shell, run the following make command. It starts a container in AVD documentation network and leverage [`muffet`](https://github.com/raviqqe/muffet) tool to check 404 HTTP code:

```shell
$ check-avd-404
docker run --network container:webdoc_avd raviqqe/muffet \
    http://127.0.0.1:8000 \
    -e ".*fonts.gstatic.com.*" \
    -e ".*edit.*" \
    -f --limit-redirections=3 \
    --timeout=60
http://127.0.0.1:8000/docs/installation/development/
        404     http://127.0.0.1:8000/docs/installation/development/setup-environement2.md
make: *** [check-avd-404] Error 1
```

> This process is also implemented in project CI to protect documentation against dead links.
