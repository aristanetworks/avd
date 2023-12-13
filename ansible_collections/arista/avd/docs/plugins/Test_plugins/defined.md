---
# This title is used for search results
title: arista.avd.defined
---
<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# defined

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.defined` when using this plugin.

Test if the value is not <code>Undefined</code> or <code>None</code>.

## Synopsis

The arista.avd.defined test returns <code>False</code> if the passed value is <code>Undefined</code> or <code>None</code>. Else it will return <code>True</code>.

The arista.avd.defined test also accepts an optional <em>test\_value</em> argument to test if the value equals this.

The optional <em>var\_type</em> argument can also be used to test if the variable is of the expected type.

Optionally, the test can emit warnings or errors if the test fails.

Compared to the built\-in <code>is defined</code> test, this test will also test for <code>None</code> and can even test for a specific value or class.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| _input | any | True | None |  | Value to test |
| test_value | any | optional | None |  | Value to match for in addition to defined and not none |
| var_type | string | optional | None | Valid values:<br>- <code>float</code><br>- <code>int</code><br>- <code>str</code><br>- <code>list</code><br>- <code>dict</code><br>- <code>tuple</code><br>- <code>bool</code> | Type or Class to test for |
| fail_action | string | optional | None | Valid values:<br>- <code>warning</code><br>- <code>error</code> | Optional action if a test fails to emit a Warning or Error |
| var_name | string | optional | None |  | Optional string to use as a variable name in warning or error messages |

## Examples

```yaml
# Test if "my_var" is defined and not none:
is_defined_and_not_none: "{{ my_var is arista.avd.defined }}"

# Test if "my_var" is defined, not none and has value "something"
is_defined_and_set_to_something: "{{ my_var is arista.avd.defined('something') }}"

# Test if "my_var" is defined and if not print a warning message with the variable name
test_result: "{{ my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' }}"
# Output >>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | boolean | Returns <code>False</code> if the passed value is <code>Undefined</code> or <code>None</code> or if any of the optional checks fail. Otherwise <code>True</code>. |

## Authors

- Arista Ansible Team (@aristanetworks)
