<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# AVD CI Notes

This file captures maintainer-facing CI decisions and implementation notes.

## autofix.ci and generated files

AVD uses pre-commit hooks to regenerate schemas, generated Python classes, and schema documentation tables. Some of these generated files are intentionally marked as non-mergeable in committed `.gitattributes` to keep normal Git behavior explicit and avoid noisy generated-file merges for contributors.

`autofix-ci/action` has a different constraint. On pull requests, the action commits any changes created by pre-commit, fetches the real PR head, checks it out, and runs:

```shell
git cherry-pick --no-commit <autofix-commit>
```

If a generated file is changed by both the PR head and the autofix commit, Git can fail the cherry-pick with a binary-style conflict because the committed attributes include `-merge`.

The autofix workflow configures a local-only merge driver to handle this case. It writes generated-file attributes to `.git/info/attributes` and configures `merge.generated-autofix` in the local checkout. This does not change committed `.gitattributes`, does not require contributor Git configuration, and does not affect local developer behavior.

The generated paths are discovered from `python-avd/schema_tools/constants.py`, using the same `SCHEMAS` registry used by the schema builder. If generated schema or table paths move, update the schema tooling registry; the autofix workflow should follow that move automatically.

### Strategy options

The selected strategy is **default checkout plus CI-local merge driver**.

- Keeps the standard `actions/checkout` behavior for pull requests, so autofix runs against GitHub's PR merge result.
- Preserves validation against the effective merge with `devel`.
- Resolves generated edit/edit conflicts during `autofix-ci/action`'s cherry-pick.
- Keeps contributor local Git behavior unchanged.

The rejected alternative was **PR-head checkout plus CI-local merge driver**.

- This would make the autofix commit a direct child of the PR head and reduce cherry-pick conflicts.
- It would also stop the autofix pass from validating the merged result with latest `devel`, which is a broader semantic change than needed.

The fallback alternative is **no schema/docs autofix**.

- This is the safest Git behavior.
- It requires contributors, maintainers, or another automation path to push regenerated schema and documentation outputs.
- It does not support moving the schema-generation pre-commit hook fully to autofix.ci.

### Known limitations

The CI-local merge driver is intended for generated edit/edit conflicts. It does not reliably solve generated file moves or modify/delete conflicts. For schema or table moves, prefer committing regenerated outputs explicitly in the PR, or expect maintainer intervention.

Contributors should still run pre-commit locally and commit generated outputs when possible. The autofix workflow is a compatibility layer, not the source of truth for generated artifacts.
