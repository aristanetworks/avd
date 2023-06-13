# Changelog

Prepare changelog fragments and place them in `changelogs/fragments/` folder. Copy PR titles from GitHub Release Notes (auto generated) and search/replace to make the formatting fit.
Check a previous fragments_backup for example.

To generate changelog (Note this can only be done once, since it will remove the fragments file - make sure to copy it to fragments_backup first):

```shell
cd ansible_collections/arista/avd/
antsibull-changelog release
```

## Documentation

- [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst)
- [categories]https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelogs.rst#changelog-fragment-categories
