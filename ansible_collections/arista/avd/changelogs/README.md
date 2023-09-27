<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Changelog

- Update galaxy.yml with the target version
- Prepare changelog fragments and place them in `changelogs/fragments/` folder. Copy PR titles from GitHub Release Notes (auto
  generated) and search/replace to make the formatting fit.
  - Check a previous fragments_backup for example.
  - In IDE use regex based search/replace
    - Search:

      ```re
      [*-] (.*)[:-] (.*) by @.+ in (.*)$
      ```

    - Replace (vscode syntax):

      ```re
      $1 - $2 ($3)
      ```

    - converts

      ```md
      * Fix(eos_designs): Fix schema for BGP peers to allow shutdown key by @ClausHolbechArista in https://github.com/aristanetworks/ansible-avd/pull/3100
      ```

    - to

      ```md
      - Fix(eos_designs) - Fix schema for BGP peers to allow shutdown key (https://github.com/aristanetworks/ansible-avd/pull/3100)
      ```

- Copy the fragment to `changelogs/fragments_backup` *before* generating the changelog
- Generate changelog (Note this can only be done once, since it will remove the fragments file - make sure to copy it to fragments_backup first):

  ```shell
  cd ansible_collections/arista/avd/
  antsibull-changelog release
  ```

## Documentation

- [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst)
- [categories]https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst#changelog-fragment-categories
