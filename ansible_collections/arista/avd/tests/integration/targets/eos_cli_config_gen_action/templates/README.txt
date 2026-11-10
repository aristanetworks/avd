These files are needed because the integration tests are implemented like roles and the action plugin
`eos_cli_config_gen` is called directly here.
The action plugin uses a relative path to the jinja templates used when rendering custom templates.
