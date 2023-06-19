# Role configuration

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Input Variables Validation settings

--8<--
roles/eos_designs/docs/tables/role-input-validation.md
--8<--

## Documentation output settings

The `documentation_output` settings can be leveraged to control documentation generation. This can be useful
if for instance the project has thousands of endpoints, to be able to disable fabric-wide connected endpoints documentation.

--8<--
roles/eos_designs/docs/tables/role-documentation-output-settings.md
--8<--

## Custom Templates

--8<--
roles/eos_designs/docs/tables/role-custom-templates.md
--8<--

## CloudVision Tags

By default, `eos_designs` will not generate the CloudVision Tags. To enable this feature, the `avd_generate_cloudvision_tags` needs to be set to `True`.
This can be set in the host/group vars to influence all or some of the devices. Alternatively it can be set in the playbook.

!!! tip
        **Refer to the [how-to](./how-to/cloudvision-tags.md) documentation for more details.**

--8<--
roles/eos_designs/docs/tables/role-input-cloudvision-tags.md
--8<--
