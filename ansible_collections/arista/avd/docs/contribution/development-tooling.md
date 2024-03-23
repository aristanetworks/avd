<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Development Tooling

## Makefile
<!-- TO DO - update!!! -->

## Pre-commit hook

[pre-commit](https://github.com/aristanetworks/avd/blob/devel/.pre-commit-config.yaml) can run standard hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. Pointing these issues out before code review allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

Repository implements the following hooks:

- `trailing-whitespace`: Fix trailing whitespace. If found, the commit is stopped, and you must rerun the commit process.
- `end-of-file-fixer`: Like `trailing-whitespace`, this hook fixes the wrong end of the file and stops your commit.
- `check-yaml`: Checks that all YAML files are valid.
- `check-added-large-files`: Check if no large file is included in the repository.
- `check-merge-conflict`: Validate there is no `MERGE` syntax related to an invalid merge process.
- `pylint`: Run Python linting with settings defined in [pylintrc](https://github.com/aristanetworks/avd/blob/devel/pylintrc).
- `yamllint`: Validate all YAML files using configuration from [yamllintrc](https://github.com/aristanetworks/avd/blob/devel/.github/yamllintrc).
- `ansible-lint`: Validate YAML files with Ansible proven practices, patters, and behaviors.
- `Flake8`: Style guide enforcement for Python code base.
- `markdownlint-cli`: Validates markdown files for common errors as referenced [here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md).

### Installation

`pre-commit` is part of [**development requirements**](https://github.com/aristanetworks/avd/blob/devel/development/requirements-dev.txt). To install, run `pip command` in **avd** folder:

```shell
$ pip install -r development/requirements-dev.txt
...
```

### Run pre-commit manually

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
