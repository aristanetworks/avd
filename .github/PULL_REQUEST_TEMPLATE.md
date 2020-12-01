<!-- All PR should follow this template to allow a clean and transparent review -->
## Change Summary
<!--- Provide a general summary of your changes in the Title above -->

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Code style update (formatting, renaming)
- [ ] Refactoring (no functional changes)
- [ ] Documentation content changes
- [ ] Other (please describe):

## Related Issue(s)
<!-- If PR is linked to one or more issues, please list issues below -->
<!--- HINT: Include "Fixes #nnn" if you are fixing an existing issue -->

## Component(s) name

## Proposed changes
<!--- Describe your changes in detail -->

## How to test
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
- [ ] I have read the [**CONTRIBUTING**](https://www.avd.sh/docs/contributing/) document.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
- [ ] All new and existing tests passed ([`pre-commit`](https://www.avd.sh/docs/installation/development/#python-virtual-environment), `make linting` and `make sanity-lint`).
- [ ] I have updated [molecule CI](https://github.com/aristanetworks/ansible-avd/tree/devel/ansible_collections/arista/avd/molecule) testing accordingly
