<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Getting Started

## Branches

- Current development branch: **`devel`**
- Branch namespace for release & development: `releases/<release_id>`

## Pull requests

- **Before** you start working on a pull request, open an issue and discuss your ideas with the **ansible-avd** maintainers. This will help prevent wasting time on something we might be unable to implement. When suggesting a new feature, ensure it will be consistent with all work already in progress.

- Any pull request which *doesn't* relate to an accepted issue will not be approved.

- All major new functionality must include relevant molecule tests where applicable.

- When submitting a pull request, please rebase from the `devel` branch rather than a release branch:`releases/*`. This is because the `devel` branch is used for ongoing development, while `releases/*` are used for tagging new stable releases.

- All code submissions should meet the following criteria (CI will enforce these checks):

  - YAML syntax is valid
  - Python syntax is valid
  - All tests pass when run with `make sanity`
  - PEP 8 compliance is enforced, with the exception that lines may be greater than 80 characters in length

Adhering to the following process is the best way to get your work merged:

- [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) the repository, clone your fork, and configure the remotes:

  ```bash
  # Clone your fork of the repo into the current directory
  git clone https://github.com/<your-username>/ansible-avd

  # Navigate to the newly cloned directory
  cd ansible-avd

  # Assign the original repo to a remote called "upstream"
  git remote add upstream https://github.com/aristanetworks/ansible-avd.git
  ```

- If you cloned a while ago, get the latest changes from upstream:

  ```bash
  git checkout devel
  git pull upstream devel
  ```

- Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:

  ```bash
  git checkout -b <topic-branch-name>
  ```

- Commit your changes in logical chunks. Please adhere to these [Git commit message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html), or your code will unlikely be merged into the main project. Use Git's [git rebase](https://docs.github.com/en/get-started/using-git/about-git-rebase) feature to tidy up your commits before making them public.

- Locally merge (or rebase) the upstream development branch into your topic branch:

  ```bash
  git pull [--rebase] upstream <dev-branch>
  ```

- Push your topic branch up to your fork:

  ```bash
  git push origin <topic-branch-name>
  ```

- [Open a Pull Request](https://github.com/aristanetworks/ansible-avd/pulls) with a clear title, description, and following the template.
