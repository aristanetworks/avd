.. _yaml_templates_to_facts:

yaml_templates_to_facts
+++++++++++++++++++++++
Set facts from YAML via Jinja2 templates


.. contents::
   :local:
   :depth: 2


Synopsis
--------


Set facts from YAML produced by Jinja2 templates


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
    <td>debug<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>Output list &#x27;avd_yaml_templates_to_facts_debug&#x27; with timestamps of each performed action.</div>
    </td>
    </tr>

    <tr>
    <td>dest<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Destination path. If set, the output facts will also be written to this path.
    Autodetects data format based on file suffix. &#x27;.yml&#x27;, &#x27;.yaml&#x27; -&gt; YAML, default -&gt; JSON
    </div>
    </td>
    </tr>

    <tr>
    <td>root_key<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>Root key under which the facts will be defined. If not set the facts well be set directly on root level.</div>
    </td>
    </tr>

    <tr>
    <td>template_output<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>If true the output data will be run through another jinja2 rendering before returning.
    This is to resolve any input values with inline jinja using variables/facts set by the input templates.
    </div>
    </td>
    </tr>

    <tr>
    <td rowspan="2">templates<br/><div style="font-size: small;"></div></td>
    <td>list</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>List of dicts for Jinja templates to be run.</div>
    </tr>

    <tr>
    <td colspan="5">
        <table border=1 cellpadding=4>
        <caption><b>Dictionary object templates</b></caption>

        <tr>
        <th class="head">parameter</th>
        <th class="head">type</th>
        <th class="head">required</th>
        <th class="head">default</th>
        <th class="head">choices</th>
        <th class="head">comments</th>
        </tr>

        <tr>
        <td>template<br/><div style="font-size: small;"></div></td>
        <td>str</td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Template file.
    Either template or python_module must be set.
    </div>
        </td>
        </tr>

        <tr>
        <td>python_module<br/><div style="font-size: small;"></div></td>
        <td>str</td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Python module to import
    Either template or python_module must be set.
    </div>
        </td>
        </tr>

        <tr>
        <td>python_class_name<br/><div style="font-size: small;"></div></td>
        <td>str</td>
        <td>no</td>
        <td>AvdStructuredConfig</td>
        <td></td>
        <td>
        <div>Name of Python Class to import
    </div>
        </td>
        </tr>

        <tr>
        <td>options<br/><div style="font-size: small;"></div></td>
        <td>dict</td>
        <td>no</td>
        <td></td>
        <td></td>
        <td>
        <div>Template options</div>
        </td>
        </tr>

        </table>

    </td>
    </tr>
    </td>
    </tr>

    </table>
    </br>

.. _yaml_templates_to_facts-examples-label:

Examples:
---------

::
    
    # tasks file for configlet_build_config
    - name: Generate device configuration in structured format
      yaml_templates_to_facts:
        root_key: structured_config
        templates:
          - python_module: "ansible_collections.arista.avd.roles.eos_designs.python_modules.base"
            python_class_name: "AvdStructuredConfig"
          - template: "mlag/main.j2"
          - template: "designs/underlay/main.j2"
          - template: "designs/overlay/main.j2"
          - template: "l3_edge/main.j2"
          - template: "designs/network_services/main.j2"
          - template: "connected_endpoints/main.j2"
          - template: "custom-structured-configuration-from-var.j2"
            options:
              list_merge: "{{ custom_structured_configuration_list_merge }}"
              strip_empty_keys: false
      check_mode: no
      changed_when: False



Author
~~~~~~

* EMEA AS Team (@aristanetworks)


