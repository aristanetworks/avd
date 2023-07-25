# arista.avd.defined

Test if the value is not <code>Undefined</code> or <code>None</code>\.

## Synopsis

The arista\.avd\.defined test returns <code>False</code> if the passed value is <code>Undefined</code> or <code>None</code>\. Else it will return <code>True</code>\.

The arista\.avd\.defined test also accepts an optional <em>test\_value</em> argument to test if the value equals this\.

The optional <em>var\_type</em> argument can also be used to test if the variable is of the expected type\.

Optionally the test can emit warnings or errors if the test fails\.

Compared to the builtin <code>is defined</code> test\, this test will also test for <code>None</code> and can even test for a specific value or class\.

## Parameters

  _input (True, any, None)
    Value to test

  test_value (optional, any, None)
    Value to match for in addition to defined and not none

  var_type (optional, string, None)
    Type or Class to test for

  fail_action (optional, string, None)
    Optional action if test fails to emit a Warning or Error

  var_name (optional, string, None)
    Optional string to use as variable name in warning or error messages

## Examples

```yaml
# Test if "my_var" is defined and not none:
{% if my_var is arista.avd.defined %}
...
{% endif %}

# Test if "my_var" is defined, not none and has value "something"
{% if my_var is arista.avd.defined("something") %}
...
{% endif %}

# Test if "my_var" is defined and if not print a warning message with the variable name
{% if my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' %}
...
{% endif %}
# >>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!
```

## Return Values

  _value (, boolean, )
    Returns <code>False</code> if the passed value is <code>Undefined</code> or <code>None</code> or if any of the optional checks fail\. Otherwise <code>True</code>\.

## Status

## Authors

- Arista Ansible Team (@aristanetworks)
