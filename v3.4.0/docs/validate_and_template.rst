.. _validate_and_template:

validate_and_template
+++++++++++++++++++++
Validate input data according to Schema, render Jinja2 template and write result to a file.

Module added in version 3.8.0



.. contents::
   :local:
   :depth: 2


Synopsis
--------


The `arista.avd.validate_and_template` Action Plugin performs data conversions and validation according to the supplied Schema.
The converted data is then used to render a Jinja2 template and writing the result to a file.
The Action Plugin supports different modes for conversion and validation, to either block the playbook or just warn the user if
the input data is not valid.
For Markdown files the plugin can also run md_toc on the output before writing to the file.


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
    <td>add_md_toc<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Run md_toc on the output before writing to the file.</div>
    </td>
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
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Destination path. The rendered template will be written to this file</div>
    </td>
    </tr>

    <tr>
    <td>md_toc_skip_lines<br/><div style="font-size: small;"></div></td>
    <td>int</td>
    <td>no</td>
    <td>0</td>
    <td></td>
    <td>
        <div>Pass this value as skip_lines to add_md_toc.</div>
    </td>
    </tr>

    <tr>
    <td>mode<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>File mode for dest file.</div>
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
    <td>template<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Path to Jinja2 Template file</div>
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

.. _validate_and_template-examples-label:

Examples:
---------

::
    
    - name: Generate device documentation
      tags: [build, provision, documentation]
      arista.avd.validate_and_template:
        template: "eos-device-documentation.j2"
        dest: "{{ devices_dir }}/{{ inventory_hostname }}.md"
        mode: 0664
        schema: "{{ lookup('ansible.builtin.file', role_schema_path) | from_yaml }}"
        conversion_mode: "{{ avd_data_conversion_mode }}"
        validation_mode: "{{ avd_data_validation_mode }}"
        add_md_toc: true
        md_toc_skip_lines: 3
      delegate_to: localhost
      when: generate_device_documentation | arista.avd.default(true)



Author
~~~~~~

* Arista Ansible Team (@aristanetworks)


