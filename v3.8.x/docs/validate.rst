.. _validate:

validate
++++++++
Validate input data according to Schema

Module added in version 3.7.0



.. contents::
   :local:
   :depth: 2


Synopsis
--------


The `arista.avd.validate` Action Plugin validates the input variables according to the supplied Schema
This is used in `arista.avd.eos_designs` and `arista.avd.eos_cli_config_gen`.
The Action Plugin supports different modes, to either block the playbook or just warn the user.


.. _module-specific-options-label:

Module-specific Options
-----------------------
The following options may be specified for this module:

.. raw:: html

    <table border=1 cellpadding=4>

    <tr>
    <th class="head">parameter</th>
    <th class="head">type</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>

    <tr>
    <td>conversion_mode<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>debug</td>
    <td><ul><li>warning</li><li>info</li><li>debug</li><li>disabled</li></ul></td>
    <td>
        <div>Run data conversion in either &quot;warning&quot;, &quot;info&quot;, &quot;debug&quot; or &quot;disabled&quot; mode.</div>
        <div>Conversion will perform type conversion of input variables as defined in the schema.</div>
        <div>Conversion is intended to help the user to identify minor issues with the input data, while still allowing the data to be validated.</div>
        <div>During conversion, messages will generated with information about the host(s) and key(s) which required conversion.</div>
        <div>conversion_mode:disabled means that conversion will not run.</div>
        <div>conversion_mode:warning will produce warning messages.</div>
        <div>conversion_mode:info will produce regular log messages.</div>
        <div>conversion_mode:debug will produce hidden messages viewable with -v.</div>
        <div>The converted data is set as facts which can be seen with -v, but is more readable with -vvv.</div>
    </td>
    </tr>

    <tr>
    <td>schema<br/><div style="font-size: small;"></div></td>
    <td>dict</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Schema conforming to &quot;AVD Meta Schema&quot;</div>
    </td>
    </tr>

    <tr>
    <td>validation_mode<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>warning</td>
    <td><ul><li>error</li><li>warning</li><li>info</li><li>debug</li><li>disabled</li></ul></td>
    <td>
        <div>Run validation in either &quot;error&quot;, &quot;warning&quot;, &quot;info&quot;, &quot;debug&quot; or &quot;disabled&quot; mode.</div>
        <div>Validation will validate the input variables according to the schema.</div>
        <div>During validation, messages will generated with information about the host(s) and key(s) which failed validation.</div>
        <div>validation_mode:disabled means that validation will not run.</div>
        <div>validation_mode:error will produce error messages and fail the task.</div>
        <div>validation_mode:warning will produce warning messages.</div>
        <div>validation_mode:info will produce regular log messages.</div>
        <div>validation_mode:debug will produce hidden messages viewable with -v.</div>
    </td>
    </tr>

    </table>
    </br>

.. _validate-examples-label:

Examples:
---------

::
    
    - name: Validate input vars according to AVD eos_designs schema
      tags: [validate]
      arista.avd.validate:
        schema: "{{ lookup('ansible.builtin.file', role_schema_path) | from_yaml }}"
        conversion_mode: "{{ avd_data_conversion_mode }}"
        validation_mode: "{{ avd_data_validation_mode }}"
      delegate_to: localhost



Author
~~~~~~

* Arista Ansible Team (@aristanetworks)


