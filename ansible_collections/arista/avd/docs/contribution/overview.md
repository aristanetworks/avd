# Arista Validated Design (AVD) Development

Arista Validated Design (AVD) is maintained as a [GitHub project](https://github.com/aristanetworks/ansible-avd) under the Apache 2 license. Users are encouraged to submit GitHub issues for feature requests and bug reports.

## Governance

Arista Validated Design (AVD) is a community-based Free Open Source Software (FOSS) project sponsored by [Arista Networks](https://www.arista.com/). [Arista Networks](https://www.arista.com/) supports Ansible for managing devices running the EOS operating system natively through eapi or [CloudVision Portal (CVP)](https://www.arista.com/en/products/eos/eos-cloudvision). This collection includes a set of ansible roles and modules to help kick-start your automation with Arista. The various roles and templates provided are designed to be customized and extended to your needs!

The Arista Validated Design (AVD) Core Team is responsible for the direction and execution of the code that gets committed to the project.

The following individuals are on the Arista Validated Design (AVD) Core Team:

* Carl Buchmann (@carlbuchmann)
* Claus Holbech (@ClausHolbechArista)
* Angelique Philipps (@aphillipps)
* Thomas Grimonet (@titom73)

## Contributing

We welcome many forms of contributions to Arista Validated Design (AVD).  While we understand most contributions will commonly come from ansible power-users, we encourage others to contribute in the form of docs, tutorials, and user guides.  If you have other ideas for contributing, don't hesitate to open an issue or have a discussion in one of the forums below.

### Communication

Communication among the contributors should always occur via public channels.
The following outlines the best ways to communicate and engage on all things Arista Validated Design (AVD):

#### Slack

* [**#ansible | #arista** on Network to Code Slack](http://slack.networktocode.com/) - Good for quick chats. Avoid any discussion that might need to be referenced later on, as the chat history is not retained long.

#### GitHub

* [GitHub issues](https://github.com/aristanetworks/ansible-avd/issues) - All feature requests, bug reports, and other substantial changes should be documented in an issue.
* [GitHub discussions](https://github.com/aristanetworks/ansible-avd/discussions) - The preferred forum for general discussion and support issues. Ideal for shaping a feature request prior to submitting an issue.

GitHub's discussions are the best place to get help or propose rough ideas for new functionality. Their integration with GitHub allows for easily cross-referencing and converting posts to issues as needed. There are several categories for discussions:

* **General** - General community discussion.
* **Ideas** - Ideas for new functionality that isn't ready for a formal feature request.
* **Q&A** - Request help with installing or using Arista Validated Design (AVD).

### Deprecation Policy

The deprecation policy will be such that there will be at least one release that makes users aware of a feature that will be deprecated in the next release.

### Versioning

Semantic Versioning ([SemVer](https://semver.org/)) is used for Arista Validated Design (AVD) versioning.

### Contributor Workflow

The following documents the lifecycle of work within Arista Validated Design (AVD):

1. Open/request a feature enhancement or file a bug
  a. If bug, see [here](#reporting-bugs)
  b. If feature request or enhancement, continue.
2. Open a GitHub Issue
  a. The issue will be reviewed. Based on the request, it will get labeled as  `current`, `near-term`, `future`.
  b. It will likely only stay in _current_ if it is trivial and quick work.
  c. If it gets labeled as _future_, the issue will be closed in the next batch of issues that get migrated and converted to GitHub discussions.

If you follow these steps, there **will** be a GitHub Issue opened prior to submitting a Pull Request (PR).  However, we're quite aware that a PR may come in without ever being discussed in an Issue or Discussion.  While we do not advocate for this, you should be aware of the process that will be followed for those circumstances.

Should this happen and if you followed the project guidelines, have sample tests, code quality, you will first be acknowledged for your work.  So, thank you in advance! After that, the PR will be quickly reviewed to ensure that it makes sense as a contribution to the project, and to gauge the work effort or issues with merging into _devel_.  If the effort required by the core team isn't trivial, it'll likely still be a few weeks before it gets thoroughly reviewed and merged. It will just depend on the current backlog.

### Contributing to Arista Validated Design (AVD)

#### Reporting Bugs

* First, ensure that you're running the [latest stable version](https://github.com/aristanetworks/ansible-avd/releases) of Arista Validated Design (AVD). If you're running an older version, it's possible that the bug has already been fixed.

* Next, check the GitHub [issues list](https://github.com/aristanetworks/ansible-avd/issues) to see if the bug you've found has already been reported. If you think you may be experiencing a reported issue that hasn't already been resolved, please click "add a reaction" in the top right corner of the issue and add a thumbs up (+1). You might also want to add a comment describing how it's affecting your installation. This will allow us to prioritize bugs based on how many users are affected.

* When submitting an issue, please be as descriptive as possible. Be sure to
provide all information request in the issue template, including:

  * The environment in which Arista Validated Design (AVD) is running
  * The exact steps that can be taken to reproduce the issue
  * Expected and observed behavior
  * Any error messages generated
  * Screenshots (if applicable)

* Please avoid prepending any sort of tag (e.g. "[Bug]") to the issue title. The issue will be reviewed by a maintainer after submission and the appropriate labels will be applied for categorization.

* Keep in mind that bugs are prioritized based on their severity and how much work is required to resolve them. It may take some time for someone to address your issue.

#### Feature Requests

* First, check the GitHub [issues list](https://github.com/aristanetworks/ansible-avd/issues) and [Discussions](https://github.com/aristanetworks/ansible-avd/discussions) to see if the feature you're requesting is already listed.  If the feature you'd like to see has already been requested and is open, click "add a reaction" in the top right corner of the issue and add a thumbs up (+1). This ensures that the issue has a better chance of receiving attention. Also feel free to add a comment with any additional justification for the feature. (However, note that comments with no substance other than a "+1" will be deleted. Please use GitHub's reactions feature to indicate your support.)

* Before filing a new feature request, consider starting with a GitHub Discussion. Feedback you receive there will help validate and shape the proposed feature before filing a formal issue. If the feature request does not get accepted into the _current_ or _near term_ backlog, it will get converted to a Discussion anyway.

* Good feature requests are very narrowly defined. Be sure to thoroughly describe the functionality and data model(s) being proposed. The more effort you put into writing a feature request, the better its chance is of being implemented. Overly broad feature requests will be closed.

* When submitting a feature request on GitHub, be sure to include all information requested by the issue template, including:

  * A detailed description of the proposed functionality
  * A use case for the feature; who would use it and what value it would add to Arista Validated Design (AVD)
  * A rough description of changes necessary to the database schema (if applicable)
  * Any third-party libraries or other resources which would be involved
  * Please avoid prepending any sort of tag (e.g. "[Feature]") to the issue title.

The issue will be reviewed by a moderator after submission and the appropriate labels will be applied for categorization.

#### Submitting Pull Requests

* If you're interested in contributing to Arista Validated Design (AVD), be sure to check out our [getting started](getting-started.html) documentation for tips on setting up your development environment.

* It is recommended to open an issue **before** starting work on a pull request, and discuss your idea with the Arista Validated Design (AVD) maintainers before beginning work. This will help prevent wasting time on something that might we might not be able to implement. When suggesting a new feature, also make sure it won't conflict with any work that's already in progress.

* Once you've opened or identified an issue you'd like to work on, ask that it be assigned to you so that others are aware it's being worked on. A maintainer will then mark the issue as "accepted."

* All new functionality must include relevant tests where applicable.

* When submitting a pull request, please be sure to work off of the `devel` branch, rather than `releases/*`. The `devel` branch is used for ongoing development, while `releases/*` is used for tagging stable releases.

* In most cases, it is not necessary to add a changelog entry: A maintainer will take care of this when the PR is merged. (This helps avoid merge conflicts resulting from multiple PRs being submitted simultaneously.)

* All code submissions should meet the following criteria (CI will enforce these checks):

  * Jinja2 templates follow our [guidelines](style-guide.html).
  * Molecule is updated with data covering your fix.
  * Molecule artifacts are updated with your coverage.
  * Python syntax is valid.
  * All unit tests pass successfully.
  * PEP 8 compliance is enforced, with the exception that lines may be greater than 80 characters in length.

* A PR can be opened before all the work is complete. In this situation, PR state should be set to __draft__. All PR marked as ready for review (i.e. not in draft) will be reviewed by the maintainer team.

* To automate release-notes creation and make filtering process easier, it is strongly recommended to use [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/#summary) syntax at least for PR title. Scope should be module or role updated. As a reminder, the list below provides all supported commit types and scopes:

  * __Types__:

    * `Feat`: Create a capability e.g. feature, test, dependency.
    * `Fix`: Fix an issue e.g. bug, typo, accident, misstatement.
    * `Cut`: Remove a capability e.g. feature, test, dependency.
    * `Doc`: Refactor of documentation, e.g. help files.
    * `CI`: Update CI components, e.g. molecule files or Github Actions.
    * `Start`: Begin doing something; e.g. create a feature flag.
    * `Stop`: End doing something; e.g. remove a feature flag.
    * `Bump`: Increase the version of something e.g. dependency.
    * `Test`: Add or refactor anything regarding test, e.g add a new testCases.
    * `Make`: Change the build process, or tooling, or infra.
    * `Refactor`: A code change that MUST be just a refactoring.
    * `Reformat`: Refactor of formatting, e.g. omit whitespace.
    * `Optimize`: Refactor of performance, e.g. speed up code.
    * `License`: Edits regarding licensing; no production code change.
    * `Revert`: Change back to the previous commit

  * __Scopes__:

    * `{{ role_name }}`: AVD role impacted by PR. __Required__ for `Feat`, `Cut` and `Fix` types
    * `plugins`: To use when AVD plugin is impacted by PR. __Required__ for `Feat`, `Cut` and `Fix` types
    * `requirements`: To use when using `Bump` type and when any AVD requirement is updated
    * `mkdoc`: represents generic documentation published on www.avd.sh
    * `contribution`: documentation related to contribution
    * `how-to`: documentation in the How to section of avd
    * `actions`: represents Github Actions update
    * `molecule`: represents Molecule CI update
    * `ansible`: For any ansible information update like galaxy.yml or ansible requirements
    * `github`: For any content related to Github processes

!!! info "Scopes"
    Scope is an optional field and can be ignore safely if your PR covers an undefined scope.

## Project Structure

All development of the current AVD release occurs in the `devel` branch; releases are packaged from the `releases/*` branches. A `releases/v*` branch should _always_ represent a stable release in its entirety, such that installing AVD by either downloading a packaged release or cloning the `releases/v*` branch provides the same code base.
