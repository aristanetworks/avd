# .verify_requirements

Verify Python requirements when running AVD

## Synopsis

The \`arista\.avd\.verify\_requirements\` module is an Ansible Action Plugin providing the following capabilities \- Display the current running version of the collection \- Given a list of python requirements\, verify if the installed libraries match these requirements \- Validate the ansible version against collection requirements \- Validate the collection requirements against the collection requirements \- Validate the running python version

## Parameters

  requirements (True, list, None)
    \- List of strings of python requirements with pip file syntax\.

  avd_ignore_requirements (False, bool, False)
    \- Boolean\, if set to True\, the play does not stop if any requirement error is detected\.

## Examples

```yaml

    - name: Verify collection requirements
      arista.avd.verify_requirements:
        requirements:
          - Jinja2 >= 2.9
          - paramiko == 2.7.1
      check_mode: false
      run_once: true

```

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
