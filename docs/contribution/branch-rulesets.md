<!--
  ~ Copyright (c) 2023-2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Branch Rulesets and Pull Request Approvals

This page describes the branch rulesets downloaded from `aristanetworks/avd` on **2026-11-24**.
The default branch at capture time was **`devel`**, not `main`.
The downloaded rulesets include changes through **10:03:33 UTC**, as recorded in their `updated_at` fields.
GitHub settings can change independently of this documentation; consult the [live rulesets](https://github.com/aristanetworks/avd/rules) for the current policy.
These are repository branch rulesets, not rules for branches in contributors' forks.

## Sources and Scope

The [ruleset index](branch-rulesets/rulesets.json) and full API responses below preserve the downloaded settings, including bypass actors and timestamps.
The responses are read-only snapshots, not configuration managed or applied by this repository.
In particular, `current_user_can_bypass` describes the account that downloaded the response, not every contributor's permissions.

| Ruleset | Full API response | Branch selection | Enforcement |
| --- | --- | --- | --- |
| [Do not allow new branches](https://github.com/aristanetworks/avd/rules/651945) | [651945.json](branch-rulesets/651945.json) | All branches except `devel` and `releases/**/*` | Active |
| [Do not delete or force push protected branches](https://github.com/aristanetworks/avd/rules/8322346) | [8322346.json](branch-rulesets/8322346.json) | Default branch and `releases/**/*` | Active |
| [Old release branches PRs](https://github.com/aristanetworks/avd/rules/27972713) | [27972713.json](branch-rulesets/27972713.json) | `releases/*` | Active |
| [PR-Approval](https://github.com/aristanetworks/avd/rules/27971823) | [27971823.json](branch-rulesets/27971823.json) | Default branch and exactly `releases/v5.7.x` | Active |

The API stores literal branch names and patterns with the prefix `refs/heads/`.
`~ALL` selects all branches; `~DEFAULT_BRANCH` follows the repository's default branch if it changes.
Branch selection uses GitHub's `fnmatch` rules: `releases/*` matches one component after `releases/`, while `releases/**/*` also covers deeper paths.
The name "Old release branches PRs" does not impose a version or age condition: it also matches `releases/v6.0.x`.

Matching rulesets apply together. Bypassing one ruleset does not bypass another, and a less restrictive matching ruleset does not relax a stricter one.

| Example branch | Applicable rulesets |
| --- | --- |
| `devel` | Do not delete or force push protected branches; PR-Approval |
| `releases/v5.7.x` | Do not delete or force push protected branches; Old release branches PRs; PR-Approval |
| `releases/v6.0.x` | Do not delete or force push protected branches; Old release branches PRs |
| `releases/archive/v5.7.x` | Do not delete or force push protected branches |
| `documentation`, `feature/example`, or `main` | Do not allow new branches |

The effective-rules API was checked for `devel`, `releases/v5.7.x`, and `releases/v6.0.x` and confirmed the combinations above.
The nested-release and other-name examples follow the configured patterns; they are not results of live push tests.
Only "Do not delete or force push protected branches" applies to nested release names: it blocks deletion and force pushes, without imposing PR requirements or a creation restriction.

## Branch Creation and Updates

### Do not allow new branches

For matching branches, this ruleset:

- Restricts branch creation to its bypass actors (`creation`).
- Blocks force pushes (`non_fast_forward`).
- Restricts updates to its bypass actors (`update`), including updates to already existing matching branches.
- Requires the branch name **not** to start with the literal text `.*` (`branch_name_pattern`, `operator: starts_with`, `negate: true`).
  This is a literal prefix condition, not a regular expression matching every name.

The `devel` and `releases/**/*` exclusions apply to this entire ruleset.
It contains no deletion restriction.
The creation restriction is why contributors use branches in personal forks.

Two GitHub Apps can always bypass this ruleset: Renovate (integration ID `2740`) and integration ID `262318`.
The name of integration `262318` was not resolved during capture; its numeric identity is preserved rather than guessed.

### Do not delete or force push protected branches

For the default branch and all matching release branches, this ruleset:

- Restricts deletion (`deletion`).
- Blocks force pushes (`non_fast_forward`).

**Its bypass list is empty.** There is no explicit exception here for maintainers, admins, Renovate, or integration `262318`.
The `avd-admins` and app exceptions in the PR ruleset below do not grant bypass of this ruleset.
It contains no `update` restriction: ordinary updates remain subject to the applicable PR requirements.
No live push, deletion, or merge was attempted.

## Pull Request Approval Policy

### Default branch and releases/v5.7.x

`PR-Approval` requires **two approving reviews overall**, with these additional team requirements for all files (`file_patterns: ["*"]`):

| Team | Team ID | Minimum team approvals | Repository access verified at capture |
| --- | --- | --- | --- |
| `@aristanetworks/avd-developers` | `5615379` | 2 | Write |
| `@aristanetworks/avd-maintainers` | `7565600` | 1 | Maintain |

The membership lists checked at capture time showed that every maintainer, including every member of `avd-admins`, was also in `avd-developers`.
`avd-admins` is a child team of `avd-maintainers`; `avd-maintainers` is not a child team of `avd-developers`.
The developer overlap therefore depends on membership being maintained, rather than that parent-child relationship.

With this overlap, a maintainer's approval contributes to both team requirements.
The required combination is **one maintainer and either one other developer or one other maintainer**.
The developer minimum is two because setting it to one would let a single maintainer satisfy both team minima and an unrelated reviewer with Write access supply the second overall approval.
Repository roles alone do not establish team membership: an admin outside these teams does not satisfy their team requirements by virtue of being an admin.

| Distinct eligible reviewers | Maintainers (minimum 1) | Developers (minimum 2) | Ordinary approval counts satisfied? |
| --- | --- | --- | --- |
| 1 maintainer + 1 developer outside the maintainer team | 1 | 2 | Yes |
| 2 maintainers, including admins who belong to both teams | 2 | 2 | Yes |
| 2 developers outside the maintainer team | 0 | 2 | No |
| 1 maintainer + 1 Write collaborator outside both teams | 1 | 1 | No |
| 1 reviewer alone | At most 1 | At most 1 | No |

This table describes approval counts, not overall merge eligibility or bypass behavior.
It assumes reviewers are eligible to approve, their approvals count, and the verified team overlap still holds.
The overlap interpretation follows the independent team minima; no controlled live PR experiment was performed.

The pull request rule also sets:

| Setting | Value and effect |
| --- | --- |
| Require code owner review | Enabled. Changes to owned files require an eligible code owner's approval. |
| Dismiss stale approvals on push | Disabled. A new push does not automatically dismiss prior approvals under this setting. |
| Require approval of the most recent reviewable push | Enabled. Someone other than its pusher must approve that push; an existing reviewer can reapprove. |
| Require review thread resolution | Enabled. Review conversations must be resolved. |
| Restrict review dismissal | Disabled, with no allowed-actor list. This ruleset adds no special dismissal restriction; GitHub's normal permissions still apply. |
| Extra approval for unattributed changes | Enabled. GitHub requires one additional approval for a Copilot PR opened under its own identity without attribution to a person: three overall rather than two. |
| Allowed merge methods | Squash only. |

PR authors cannot approve their own PRs.
For a maintainer author, the ordinary approval counts require another maintainer plus another developer or maintainer, all distinct from the author.
An approval after the latest reviewable push must also meet the separate latest-push condition.

### Code owners and review requests

At the captured revision, [`.github/CODEOWNERS`](https://github.com/aristanetworks/avd/blob/7bb3151de8/.github/CODEOWNERS) contains:

```text
*   @aristanetworks/avd-developers @aristanetworks/avd-maintainers
```

This lists both teams as owners of every file.
GitHub automatically requests code owner reviews when a PR is opened ready for review or a draft becomes ready, subject to team review-assignment settings.
It does not automatically request reviews merely because a draft PR is opened, nor does it necessarily request every individual member of either team.
GitHub uses the `CODEOWNERS` file from the PR's base branch, so release branches may have different ownership rules.

When multiple code owners share a matching entry, an approval from any one of them satisfies the code owner requirement.
The separate team requirements in `PR-Approval` impose the maintainer minimum and two-developer minimum; the `CODEOWNERS` entry alone does not require approval from both teams.

### Other single-component release branches

`Old release branches PRs` applies to every `releases/*` branch and has these settings:

- Branch creation is restricted, with `avd-admins` as its only bypass actor (`always` mode).
- Two approving reviews are required overall, with **no team-specific required reviewers**.
- Code owner review and resolved review threads are required.
- Automatic dismissal of stale approvals and approval of the most recent reviewable push are disabled.
- Review dismissal restrictions are disabled, with an empty allowed-actor list.
- The additional approval for unattributed Copilot PRs is enabled, bringing their overall requirement to three.
- Merge, squash, and rebase are allowed by this ruleset, subject to repository settings and other applicable rulesets.
- Required status checks are configured as strict (`strict_required_status_checks_policy: true`) and enforce on creation (`do_not_enforce_on_create: false`), but the check list is empty.
  This ruleset names no required CI checks; an empty list does not mean that all CI jobs are required.

For `releases/v5.7.x`, `PR-Approval` applies as well: the combined policy still requires the team minima, approval after the latest push, squash merging, the named checks, and the merge queue.
The two rulesets' two-review requirements do not add up to four reviews.
For `releases/v6.0.x` and other single-component release names, the old-release ruleset supplies no team quotas, latest-push approval condition, or merge queue requirement.
The separate deletion and force-push restrictions still apply.

## Required Checks and Merge Queue

`PR-Approval` names exactly these required checks, both bound to the GitHub Actions app (integration ID `15368`):

- `required-checks`
- `Autofix - run pre-commit`

`strict_required_status_checks_policy: true` enables the up-to-date requirement.
`do_not_enforce_on_create: true` skips these check requirements for branch creation; it does not exempt subsequent updates or merges.
The merge queue validates queued changes against the current target branch and preceding queued changes.
The workflows in `.github/workflows/pull-request-management.yml` and `.github/workflows/pull-request-autofix.yml` handle `merge_group` events.

| Merge queue parameter | Captured value | Meaning |
| --- | --- | --- |
| `merge_method` | `SQUASH` | Squash merge queued PRs. |
| `max_entries_to_build` | `5` | At most five queue entries request builds concurrently. |
| `min_entries_to_merge` | `1` | Minimum merge group size is one PR. |
| `max_entries_to_merge` | `5` | Merge at most five PRs in a group. |
| `min_entries_to_merge_wait_minutes` | `5` | Maximum wait to reach the minimum group size; with a minimum of one, this does not impose a five-minute wait on every PR. |
| `grouping_strategy` | `ALLGREEN` | Every entry in a merge group must pass required checks. |
| `check_response_timeout_minutes` | `60` | A required check without a conclusion after 60 minutes is treated as failed. |

## Bypass Permissions

`always` permits bypass for direct operations as well as through PRs; `pull_request` permits bypass only through a pull request.
These permissions apply only to the named ruleset.

| Ruleset | Actors allowed to bypass |
| --- | --- |
| Do not allow new branches | Renovate (`Integration`, `2740`, `always`); unresolved app (`Integration`, `262318`, `always`) |
| Do not delete or force push protected branches | None |
| Old release branches PRs | `avd-admins` (`Team`, `14205968`, `always`) |
| PR-Approval | `avd-admins` (`Team`, `14205968`, `pull_request`); unresolved app (`Integration`, `262318`, `always`) |

For example, membership in `avd-admins` grants bypass of `PR-Approval` only through PRs and of `Old release branches PRs` in always mode.
It does not grant bypass of protected-branch deletion or force-push restrictions, or of the general branch creation and update restrictions.
Renovate's exception in the new-branch ruleset does not grant it an exception from the PR ruleset.

## Refreshing and Verifying the Snapshot

Download the index first, then download each ruleset ID it returns; new rulesets may have been added since this capture.
For example, from the repository root:

```bash
gh api repos/aristanetworks/avd/rulesets --paginate > docs/contribution/branch-rulesets/rulesets.json
gh api repos/aristanetworks/avd/rulesets/27971823 > docs/contribution/branch-rulesets/27971823.json
```

Repeat the second command for every ID in the current index.
The committed JSON is indented for readability; no response fields have been removed.
To inspect all effective rules for a branch, including overlapping rulesets:

```bash
gh api repos/aristanetworks/avd/rules/branches/devel
gh api repos/aristanetworks/avd/rules/branches/releases%2Fv5.7.x
gh api repos/aristanetworks/avd/rules/branches/releases%2Fv6.0.x
```

Recheck the default branch, team IDs, repository access, team membership overlap, and each target branch's `CODEOWNERS` when refreshing this explanation.
The snapshot does not establish every other possible merge condition, such as legacy branch protection, repository-wide merge-method settings, or the state of an individual PR.

GitHub references:

- [Available rules for rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [About rulesets and overlapping rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Creating rulesets and branch patterns](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository)
- [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
