## "Wildcard Keyed Dict" to "List of Dicts" Data model migration

<!-- Use this PR Title: Refactor(eos_cli_config_gen): Wildcard dict to list for `< data_model_key >` -->

## Data model key

`< data_model_key >`

## Checklist

### Contributor Checklist

- [ ] Update `README_v4.0.md` with new data model
- [ ] Update all `host_vars` under molecule scenario `eos_cli_config_gen_v4.0` with new data model
- [ ] Update `templates/eos/< template >.j2` and `templates/documentation/< template >.j2`:
  - [ ] Add `arista.avd.convert_dicts('<primary key>')` filter for loops previously using wildcard keys
  - [ ] Update `arista.avd.natural_sort('<primary key>')` to sort on the primary key (if applicable)
- [ ] Run molecule `cd ansible_collections/arista/avd/molecule ; make cli-4.0-schema`
  - [ ] Verify no changes to generated configs/docs

### Reviewer Checklist

- Reviewer 1:
  - [ ] Verify data model changes
  - [ ] Verify that all molecule `host_vars` under `eos_cli_config_gen_v4.0` has been updated to the new data model
  - [ ] Verify no changes to configs/docs on any molecule scenario
  - [ ] Verify that CI pass

- Reviewer 2:
  - [ ] Verify data model changes
  - [ ] Verify that all molecule `host_vars` under `eos_cli_config_gen_v4.0` has been updated to the new data model
  - [ ] Verify no changes to configs/docs on any molecule scenario
  - [ ] Verify that CI pass
