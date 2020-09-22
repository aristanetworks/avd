# configlet\_build\_config

Build arista.cvp.configlet configuration.

Module added in version 2.9

<div class="contents" data-local="" data-depth="2">

</div>

## Synopsis

Build configuration to publish configlets on Cloudvision.

## Module-specific Options

The following options may be specified for this module:

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
    <div>File extensio to look for.</div>
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

## Examples:

    # tasks file for cvp_configlet_upload
    - name: generate intented variables
      tags: [build, provision]
      configlet_build_config:
        configlet_dir: '{{ configlet_dir }}'
        configlet_prefix: '{{ configlets_prefix }}'
        configlet_extension: '{{configlet_extension}}'

### Author

  - EMEA AS Team (@aristanetworks)

### Status

This module is flagged as **preview** which means that it is not
guaranteed to have a backwards compatible interface.
