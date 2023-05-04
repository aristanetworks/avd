This molecule scenario will not generate any configs or device documentation.

This molecule scenario is only intended to test the new eos_designs data model
with lists of dictionaries instead of nested dictionaries.

To prevent the automatic conversion, this molecule scenario run with the environment
variable "AVD_DISABLE_CONVERT_DICTS=TRUE" which disables the conversion.
Until eos_designs _output_ has been changed to lists of dictionaries, we can not run
eos_cli_config_gen role, since it would also pick up the environment variable, hence
disabling conversion.
