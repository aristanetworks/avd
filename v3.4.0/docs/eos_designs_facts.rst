.. _eos_designs_facts:

eos_designs_facts
+++++++++++++++++
Set eos_designs facts

Module added in version 3.5.0



.. contents::
   :local:
   :depth: 2


Synopsis
--------


The `arista.avd.eos_designs_facts` module is an Ansible Action Plugin providing the following capabilities
Set `avd_switch_facts` fact containing both `switch` facts per host.
Set `avd_topology_peers` fact containing list of downlink switches per host. This list is built based on the `uplink_switches` from all other hosts.
Set `avd_overlay_peers` fact containing list of EVPN or MPLS overlay peers per host. This list is built based on the `evpn_route_servers` and `mpls_route_reflectors` from all other hosts.
The plugin is designed to `run_once`. With this, Ansible will set the same facts on all devices, so all devices can lookup values of any other device without using the slower `hostvars`.
The facts can also be copied to the "root" `switch` in a task run per-device (see example below)
The module is used in `arista.avd.eos_designs` to set facts for devices, which are then used by jinja templates in `arista.avd.eos_designs` to generate the `structured_configuration`.


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
    <td>avd_switch_facts<br/><div style="font-size: small;"></div></td>
    <td>bool</td>
    <td>no</td>
    <td></td>
    <td><ul><li>yes</li><li>no</li></ul></td>
    <td>
        <div>- Calculate and set &#x27;avd_switch_facts.&lt;devices&gt;.switch&#x27;, &#x27;avd_overlay_peers&#x27; and &#x27;avd_topology_peers&#x27; facts
    </div>
    </td>
    </tr>

    </table>
    </br>

.. _eos_designs_facts-examples-label:

Examples:
---------

::
    
    - name: Set eos_designs facts
      tags: [build, provision, facts]
      arista.avd.eos_designs_facts:
        avd_switch_facts: True
      check_mode: False
      run_once: True



Author
~~~~~~

* Arista Ansible Team (@aristanetworks)


