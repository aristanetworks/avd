<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>custom_templates</samp>](## "custom_templates") | List, items: String |  |  |  | - Custom templates can be added below the playbook directory.<br>- If a location above the directory is desired, a symbolic link can be used.<br>- Example under the `playbooks` directory create symbolic link with the following command:<br><br>  ```bash<br>  ln -s ../../shared_repo/custom_avd_templates/ ./custom_avd_templates<br>  ```<br><br>- The output will be rendered at the end of the configuration.<br>- The order of custom templates in the list can be important if they overlap.<br>- It is recommended to use a `!` delimiter at the top of each custom template.<br><br>Add `custom_templates` to group/host variables:<br> |
    | [<samp>&nbsp;&nbsp;- &lt;str&gt;</samp>](## "custom_templates.[].&lt;str&gt;") | String |  |  |  | Template relative path below playbook directory |

=== "YAML"

    ```yaml
    custom_templates:
      - <str>
    ```
