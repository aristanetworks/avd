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

- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) for AVD documentation listening on port `8000`
- An [mkdoc](https://hub.docker.com/repository/docker/titom73/mkdocs) or AVD documentation listening on port `8001`
- An [AVD runner](https://hub.docker.com/repository/docker/avdteam/base) with a pseudo terminal connected to shell for ansible execution

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

### Configure git hook

To automatically run tests when running a commit, configure your repository whit command:

```shell
$ pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

To remove installation, use `uninstall` option.
