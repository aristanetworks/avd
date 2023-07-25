# arista.avd.global_vars

Variable plugins to allow loading global\_vars with less precedence than group\_vars or host\_vars

## Synopsis

Loads variables from variable files specified in ansible\.cfg or in the environment variable\.

Assign the loaded variables to the \'all\' inventory group\.

Files are restricted by extension to one of \.yaml\, \.json\, \.yml or no extension\.

Hidden files \(starting with \'\.\'\) and backup files \(ending with \'\~\'\) files are ignored\.

Only applies to inventory sources that are existing paths\.

## Requirements

The below requirements are needed on the host that executes this module.

- This plugin should run at the \`inventory\` stage \(default\) before all other variable plugins\, to inject the variables before any group and host vars\.

## Parameters

  paths (True, list, None)
    List of relative paths\, relative to the inventory file\.
    If path is a directory\, all the valid files inside are loaded in alphabetical order\.
    If the environment variable is set\, it takes precedence over ansible\.cfg\.

  stage (optional, any, inventory)
    The stage during which executing the plugin\. It could be \'inventory\' or \'task\'
    Given the expected usage of this plugin at the beginning of the run\. It is hardcoded to \'inventory\'

  _valid_extensions (optional, list, ['.yml', '.yaml', '.json'])
    Check all of these extensions when looking for \'variable\' files which should be YAML or JSON or vaulted versions of these\.
    This affects vars\_files\, include\_vars\, inventory and vars plugins among others\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
