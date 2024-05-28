<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Development Tooling

- To assist the AVD development community, we provide guidance to develop with two primary methods: VSCode dev containers or local Python environment.
- You may choose your also choose your own development methodology, however we may not be able to provide assistance in a timely manner.
- Please report any issues and optimization suggestions regarding the development workflow via [Github discussions board](https://github.com/aristanetworks/avd/discussions).

## Development environments

### VSCode Containers

- To facilitate onboarding of development the AVD project builds [Dev Containers](../containers/overview.md) with all the required tools to get started.
- Before you can leverage the Dev Container ensure to have [Docker](https://docs.docker.com/engine/install/) and [Visual Studio Code](https://code.visualstudio.com/) installed.
- Follow the instruction to customize a and leverage the [AVD Dev Container](../containers/overview.md#how-to-use-dev-containers)

### Python Environments

Developing with you local Python environment requires you to configure and install the AVD project development tools and dependencies.
In additional to Ansible collection [requirements](../installation/collection-installation.md), your development environment must support the following tools: Git, Make, Docker and [Python development requirements](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/requirements-dev.txt)

Recommend steps with Python virtual environment:

1. Create and activate a Python virtual environment.
2. Clone the AVD repository.
3. Install Python requirements located in the AVD repository: [requirements-dev.txt](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/requirements-dev.txt) and [requirements.txt](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/requirements.txt).
4. Configure pre-commit git hook, to automatically run pre-commit (optional, highly recommended!).

```shell
python -m venv avd-development
source avd-development/bin/activate
git clone https://github.com/aristanetworks/avd.git
cd avd
pip install -r ansible_collections/arista/avd/requirements-dev.txt
pip install -r ansible_collections/arista/avd/requirements.txt
pre-commit install
```

## Pre-commit

[pre-commit](https://github.com/aristanetworks/avd/blob/devel/.pre-commit-config.yaml) can run standard hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. Pointing these issues out before code review allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.
Additionally the AVD project leverages pre-commit hooks to build and update the AVD schemas and documentation artifacts.

The AVD repository implements the following hooks:

- `trailing-whitespace`: Fix trailing whitespace.
- `end-of-file-fixer`: Fixes the wrong end of the file and stops your commit.
- `check-added-large-files`: Check if no large file is included in the repository.
- `check-merge-conflict`: Validate there is no `MERGE` syntax related to an invalid merge process.
- `insert-license`: Check and insert license on Python, YAML, Jinja2 and Markdown files.
- `isort`: Check for changes when running isort on all python files.
- `black`: Check for changes when running Black on all python files.
- `flake8`: Check for Flake8 errors on Python files.
- `pylint`: Run Python linting with settings defined in [pylintrc](https://github.com/aristanetworks/avd/blob/devel/pylintrc).
- `yamllint`: Validate all YAML files using configuration from [yamllintrc](https://github.com/aristanetworks/avd/blob/devel/.github/yamllintrc).
- `j2lint`: Check for Linting errors on Jinja2 files [j2lint](https://github.com/aristanetworks/j2lint).
- `codespell`: Check for common misspellings in text files.
- `docs-plugin-modules`: Build documentation for collection modules and action plugins.
- `docs-plugin-filter`: Build documentation for collection filter plugins.
- `docs-plugin-lookup`: Build documentation for collection lookup plugins.
- `docs-plugin-test`: Build documentation for collection test plugins.
- `docs-plugin-vars`: Build documentation for collection var plugins.
- `schemas`: Build AVD schemas and documentation from schema fragments.
- `markdownlint`: Validates markdown files for common errors as referenced [here](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md).

### Run pre-commit manually

To run `pre-commit` manually before you commit, use this command:

```shell
# Run pre-commit hooks on all staged files. The command will automatically detect changed files using `git status` and run tests according to their type.
pre-commit run
# Run pre-commit hooks on all un-staged and staged files.
pre-commit run --all
# Run specific pre-commit schemas hook on all un-staged and staged files.
pre-commit run schemas --all
```

!!! note
    This process is also implemented in project CI to ensure code quality and compliance.

## Molecule

- [Molecule](https://ansible.readthedocs.io/projects/molecule/) project is designed to aid in the development and testing of Ansible roles.
- The AVD project leverages Molecule for:
  - Static integration test on the following Ansible roles:
    - `eos_designs`
    - `eos_cli_config_gen`
    - `eos_validate_state`
    - `eos_config_deploy_cvp`
    - `dhcp_provisionner`
  - End-to-end systems integration tests on the following CloudVision role and module:
    - `cv_deploy`
    - `cv_workflow`
- The molecule scenarios are located under the [molecule directory](https://github.com/aristanetworks/avd/tree/devel/ansible_collections/arista/avd/molecule) at the root of the collection.
  - The directory name is the molecule `--scenario-name` leveraged when executing Molecule, i.e: `eos_cli_config_gen`, `eos_designs_unit_tests`.

### Makefile method

To run the Molecule tests locally to generate the new expected configuration and documentation leverage Makefile located in the `ansible_collections/arista/avd/molecule` directory.

The Makefile supports the following targets:

- `help`: Display available make target and descriptions.
- `converge`: Execute molecule "converge" sequence. Specify scenario name (default: eos_cli_config_gen) with MOLECULE= and Ansible options (default none) with ANSIBLE_OPTIONS=.
- `test`: Execute molecule "test" sequence. Specify scenario name (default: eos_cli_config_gen) with MOLECULE= and Ansible options (default none) with ANSIBLE_OPTIONS=.
- `refresh-facts`: Run all "eos_designs" and "eos_cli_config_gen" [molecule scenarios](https://github.com/aristanetworks/avd/blob/devel/ansible_collections/arista/avd/molecule/MOLECULE_SCENARIOS.txt).
- `commit-facts`: Commit updated facts for CI with the following message: 'CI(molecule): Update Molecule artifacts'.
- `sync-facts`: Run `refresh-facts` and `commit-facts` to update all CI artifacts.
- `cleanup`: Execute molecule "cleanup" sequence on all scenarios located in the molecule directory.

!!! info
    `make refresh-facts` can be useful when your change common template or structured configuration output.
    Note that it will take significant amount of local resources and can take several minutes/hours to execute.

In the majority of new features or bug fixes, the process is the following:

1. Update scenario inventory when required. It is ok to extend an existing host to cover a new test. When in doubt consult with a maintainer.
2. Update group and or host variables in the scenario and ensure to cover all use case of the feature.
3. Run `make converge` target within the molecule directory to generate artifacts. Examples:

    ```shell
    # Run eos_designs_unit_tests scenario to generate artifacts
    make converge MOLECULE=eos_designs_unit_tests
    # Run eos_designs_unit_tests scenario with verbosity `-vvv` and limit `--limit DC1-SPINE1`
    make converge MOLECULE=eos_designs_unit_tests ANSIBLE_OPTIONS="-vvv --limit DC1-SPINE1"
    #Run eos_cli_config_gen scenario with limit
    make converge ANSIBLE_OPTIONS="--limit logging"
    ```

4. Review generated artifacts and test results on an EOS device to confirm syntax and working configuration.
5. Commit artifacts with `make commit-facts`.

!!! info
    Molecule scenario are also executed in project CI to ensure code quality and compliance and tested against various ansible-core versions.

### CLI syntax

You may also run Molecule by leveraging its CLI syntax directly from the root of the collection path: `ansible_collections/arista/avd/`.

Examples:

```shell
# Run eos_cli_config_gen scenario
molecule converge -s eos_cli_config_gen
# Run eos_cli_config_gen scenario limiting to "logging" host only
molecule converge -s eos_cli_config_gen -- --limit logging
# Run eos_designs)unit_test scenario with verbosity
molecule converge -s eos_designs_unit_tests -- -vvv
```

## Pytest
<!---To Do -->
