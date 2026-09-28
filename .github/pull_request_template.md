## Change Summary

<!-- Enter short PR description -->

## Related Issue(s)

Fixes #<ISSUE ID>

## Component(s) name

`arista.avd.<role-name>`

## Proposed changes
<!--- Describe your changes in detail -->
<!--- Describe data model implemented for new features -->

## How to test
<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, and the tests you ran to -->

## Checklist

### User Checklist

<!-- Add your own checklist using MD syntax and by replacing N/A -->
- N/A

### Repository Checklist

<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- If you're unsure about any of these, don't hesitate to ask. We're here to help! -->
- [ ] My code has been rebased from devel before I start

#### Schema Explorer changes (complete when touching `tools/schema-explorer/` or `tools/schema_explorer_markdown.py`)

- [ ] No new backend or remote runtime service
- [ ] No unescaped schema-derived HTML rendering
- [ ] Runtime assets are same-origin or explicitly reviewed
- [ ] Generated public artifacts remain allowlisted (`mkdocs_hook.py`)
- [ ] `make schema-explorer-check` passed (or CI equivalent)
- [ ] I have read the [**CONTRIBUTING**](https://avd.arista.com/stable/docs/contribution/overview.html) document.
- [ ] My change requires a change to the documentation and documentation have been updated accordingly.
- [ ] I have updated [molecule CI](https://github.com/aristanetworks/avd/tree/devel/ansible_collections/arista/avd/extensions/molecule) testing accordingly. (check the box if not applicable)
