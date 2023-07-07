# Role configuration

Role configuration settings can be set either as regular inventory variables or directly as task_vars on the `import_role` task.

## Input Variables Validation settings

--avdschema--
eos_designs:role-input-validation
--avdschema--

## Documentation output settings

The `documentation_output` settings can be leveraged to control documentation generation. This can be useful
if for instance the project has thousands of endpoints, to be able to disable fabric-wide connected endpoints documentation.

--avdschema--
eos_designs:role-documentation-output-settings
--avdschema--

## Custom Templates

--avdschema--
eos_designs:role-custom-templates
--avdschema--
