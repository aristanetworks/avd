=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  | AVD supports 2 different data models for community lists:<br><br>- The legacy `community_lists` data model that can be used for compatibility with the existing deployments.<br>- The improved `ip_community_lists` data model.<br><br>Both data models can coexist without conflicts, as different keys are used: `community_lists` vs `ip_community_lists`.<br>Community list names must be unique.<br><br>The improved data model has a better design documented below:<br><br>communities and regexp MUST not be configured together in the same entry<br>possible community strings are (case insensitive):<br><br>- GSHUT<br>- internet<br>- local-as<br>- no-advertise<br>- no-export<br>- <1-4294967040><br>- aa:nn<br> |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "ip_community_lists.[].name") | String | Required, Unique |  |  | IP Community-list Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_community_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- action</samp>](## "ip_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- permit<br>- deny |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "ip_community_lists.[].entries.[].communities") | List, items: String |  |  |  | If defined, a standard community-list will be configured |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "ip_community_lists.[].entries.[].communities.[].&lt;str&gt;") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression<br>If defined, a regex community-list will be configured |

=== "YAML"

    ```yaml
    ip_community_lists:
      - name: <str>
        entries:
          - action: <str>
            communities:
              - <str>
            regexp: <str>
    ```
