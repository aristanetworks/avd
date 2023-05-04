.. _configlet_build_config:

configlet_build_config
++++++++++++++++++++++
Build arista.cvp.configlet configuration.


.. contents::
   :local:
   :depth: 2


Synopsis
--------


Build configuration to publish configlets to Cloudvision.


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
    <td>configlet_dir<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Directory where configlets are located.</div>
    </td>
    </tr>

    <tr>
    <td>configlet_extension<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td>conf</td>
    <td></td>
    <td>
        <div>File extension to look for.</div>
    </td>
    </tr>

    <tr>
    <td>configlet_prefix<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>yes</td>
    <td></td>
    <td></td>
    <td>
        <div>Prefix to append on configlet.</div>
    </td>
    </tr>

    <tr>
    <td>destination<br/><div style="font-size: small;"></div></td>
    <td>str</td>
    <td>no</td>
    <td></td>
    <td></td>
    <td>
        <div>File where to save information.</div>
    </td>
    </tr>

    </table>
    </br>

.. _configlet_build_config-examples-label:

Examples:
---------

::
    
    # tasks file for configlet_build_config
    - name: generate intended variables
      tags: [build, provision]
      configlet_build_config:
        configlet_dir: '/path/to/configlets/folder/'
        configlet_prefix: 'AVD_'
        configlet_extension: 'cfg'



Author
~~~~~~

* EMEA AS Team (@aristanetworks)


