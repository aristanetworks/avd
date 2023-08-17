<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

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
