<!--
  ~ Copyright (c) 2023 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_security</samp>](## "ip_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ike_policies</samp>](## "ip_security.ike_policies") | List, items: Dictionary |  |  |  | Internet Security Association and Key Mgmt Protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_security.ike_policies.[].name") | String | Required, Unique |  |  | Policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_id</samp>](## "ip_security.ike_policies.[].local_id") | String |  |  |  | Local IKE Identification.<br>Can be an IPv4 or an IPv6 address.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ike_lifetime</samp>](## "ip_security.ike_policies.[].ike_lifetime") | Integer |  |  | Min: 1<br>Max: 24 | IKE lifetime in hours. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "ip_security.ike_policies.[].encryption") | String |  |  | Valid Values:<br>- disabled<br>- 3des<br>- aes128<br>- aes256 | Local IKE Identification.<br>Can be an IPv4 or an IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dh_group</samp>](## "ip_security.ike_policies.[].dh_group") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 5<br>- 14<br>- 15<br>- 16<br>- 17<br>- 20<br>- 21<br>- 24 | Diffie-Hellman group for the key exchange. |
    | [<samp>&nbsp;&nbsp;sa_policies</samp>](## "ip_security.sa_policies") | List, items: Dictionary |  |  |  | Security Association policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_security.sa_policies.[].name") | String | Required, Unique |  |  | Name of the SA policy. The "null" value is deprecated and will be removed in AVD 5.0.0 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esp</samp>](## "ip_security.sa_policies.[].esp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integrity</samp>](## "ip_security.sa_policies.[].esp.integrity") | String |  |  | Valid Values:<br>- disabled<br>- sha1<br>- sha256<br>- null |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "ip_security.sa_policies.[].esp.encryption") | String |  |  | Valid Values:<br>- disabled<br>- aes128<br>- aes128gcm128<br>- aes128gcm64<br>- aes256<br>- aes256gcm256<br>- null |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pfs_dh_group</samp>](## "ip_security.sa_policies.[].pfs_dh_group") | Integer |  |  | Valid Values:<br>- 1<br>- 2<br>- 5<br>- 14<br>- 15<br>- 16<br>- 17<br>- 20<br>- 21<br>- 24 |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "ip_security.profiles") | List, items: Dictionary |  |  |  | IPSec profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "ip_security.profiles.[].name") | String | Required, Unique |  |  | Name of the IPsec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ike_policy</samp>](## "ip_security.profiles.[].ike_policy") | String |  |  |  | Name of the IKE policy to use in this profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_policy</samp>](## "ip_security.profiles.[].sa_policy") | String |  |  |  | Name of the Security Association to use in this profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection</samp>](## "ip_security.profiles.[].connection") | String |  |  | Valid Values:<br>- add<br>- start<br>- route | IPsec connection (Initiator/Responder/Dynamic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "ip_security.profiles.[].shared_key") | String |  |  |  | Encrypted password - only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dpd</samp>](## "ip_security.profiles.[].dpd") | Dictionary |  |  |  | Dead Peer Detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ip_security.profiles.[].dpd.interval") | Integer | Required |  | Min: 2<br>Max: 3600 | Interval (in seconds) between keep-alive messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "ip_security.profiles.[].dpd.time") | Integer | Required |  | Min: 10<br>Max: 3600 | Time (in seconds) after which the action is applied. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_security.profiles.[].dpd.action") | String | Required |  | Valid Values:<br>- clear<br>- hold<br>- restart | Action to apply<br><br>* 'clear': Delete all connections<br>* 'hold': Re-negotiate connection on demand<br>* 'restart': Restart connection immediately<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ip_security.profiles.[].mode") | String |  |  | Valid Values:<br>- transport<br>- tunnel | Ipsec mode type. |
    | [<samp>&nbsp;&nbsp;key_controller</samp>](## "ip_security.key_controller") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_security.key_controller.profile") | String |  |  |  | IPsec profile name to use. |

=== "YAML"

    ```yaml
    ip_security:
      ike_policies:
        - name: <str>
          local_id: <str>
          ike_lifetime: <int>
          encryption: <str>
          dh_group: <int>
      sa_policies:
        - name: <str>
          esp:
            integrity: <str>
            encryption: <str>
          pfs_dh_group: <int>
      profiles:
        - name: <str>
          ike_policy: <str>
          sa_policy: <str>
          connection: <str>
          shared_key: <str>
          dpd:
            interval: <int>
            time: <int>
            action: <str>
          mode: <str>
      key_controller:
        profile: <str>
    ```
