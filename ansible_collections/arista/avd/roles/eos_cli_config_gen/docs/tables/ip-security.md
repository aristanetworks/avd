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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_security.ike_policies.[].name") | String | Required, Unique |  |  | Policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_id</samp>](## "ip_security.ike_policies.[].local_id") | String |  |  |  | Local IKE Identification.<br>Can be an IPv4 or an IPv6 address.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ike_lifetime</samp>](## "ip_security.ike_policies.[].ike_lifetime") | Integer |  |  | Min: 1<br>Max: 24 | IKE lifetime in hours. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "ip_security.ike_policies.[].encryption") | String |  |  | Valid Values:<br>- <code>3des</code><br>- <code>aes128</code><br>- <code>aes256</code> | IKE encryption algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dh_group</samp>](## "ip_security.ike_policies.[].dh_group") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>5</code><br>- <code>14</code><br>- <code>15</code><br>- <code>16</code><br>- <code>17</code><br>- <code>20</code><br>- <code>21</code><br>- <code>24</code> | Diffie-Hellman group for the key exchange. |
    | [<samp>&nbsp;&nbsp;sa_policies</samp>](## "ip_security.sa_policies") | List, items: Dictionary |  |  |  | Security Association policies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_security.sa_policies.[].name") | String | Required, Unique |  |  | Name of the SA policy. The "null" value is deprecated and will be removed in AVD 5.0.0 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;esp</samp>](## "ip_security.sa_policies.[].esp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;integrity</samp>](## "ip_security.sa_policies.[].esp.integrity") | String |  |  | Valid Values:<br>- <code>disabled</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>null</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encryption</samp>](## "ip_security.sa_policies.[].esp.encryption") | String |  |  | Valid Values:<br>- <code>disabled</code><br>- <code>aes128</code><br>- <code>aes128gcm128</code><br>- <code>aes128gcm64</code><br>- <code>aes256</code><br>- <code>aes256gcm256</code><br>- <code>null</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pfs_dh_group</samp>](## "ip_security.sa_policies.[].pfs_dh_group") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>5</code><br>- <code>14</code><br>- <code>15</code><br>- <code>16</code><br>- <code>17</code><br>- <code>20</code><br>- <code>21</code><br>- <code>24</code> |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "ip_security.profiles") | List, items: Dictionary |  |  |  | IPSec profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_security.profiles.[].name") | String | Required, Unique |  |  | Name of the IPsec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ike_policy</samp>](## "ip_security.profiles.[].ike_policy") | String |  |  |  | Name of the IKE policy to use in this profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_policy</samp>](## "ip_security.profiles.[].sa_policy") | String |  |  |  | Name of the Security Association to use in this profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection</samp>](## "ip_security.profiles.[].connection") | String |  |  | Valid Values:<br>- <code>add</code><br>- <code>start</code><br>- <code>route</code> | IPsec connection (Initiator/Responder/Dynamic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "ip_security.profiles.[].shared_key") | String |  |  |  | Encrypted password - only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dpd</samp>](## "ip_security.profiles.[].dpd") | Dictionary |  |  |  | Dead Peer Detection. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ip_security.profiles.[].dpd.interval") | Integer | Required |  | Min: 2<br>Max: 3600 | Interval (in seconds) between keep-alive messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "ip_security.profiles.[].dpd.time") | Integer | Required |  | Min: 10<br>Max: 3600 | Time (in seconds) after which the action is applied. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_security.profiles.[].dpd.action") | String | Required |  | Valid Values:<br>- <code>clear</code><br>- <code>hold</code><br>- <code>restart</code> | Action to apply<br><br>* 'clear': Delete all connections<br>* 'hold': Re-negotiate connection on demand<br>* 'restart': Restart connection immediately<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ip_security.profiles.[].mode") | String |  |  | Valid Values:<br>- <code>transport</code><br>- <code>tunnel</code> | Ipsec mode type. |
    | [<samp>&nbsp;&nbsp;key_controller</samp>](## "ip_security.key_controller") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_security.key_controller.profile") | String |  |  |  | IPsec profile name to use. |

=== "YAML"

    ```yaml
    ip_security:

      # Internet Security Association and Key Mgmt Protocol.
      ike_policies:

          # Policy name.
        - name: <str; required; unique>

          # Local IKE Identification.
          # Can be an IPv4 or an IPv6 address.
          local_id: <str>

          # IKE lifetime in hours.
          ike_lifetime: <int; 1-24>

          # IKE encryption algorithm.
          encryption: <str; "3des" | "aes128" | "aes256">

          # Diffie-Hellman group for the key exchange.
          dh_group: <int; 1 | 2 | 5 | 14 | 15 | 16 | 17 | 20 | 21 | 24>

      # Security Association policies.
      sa_policies:

          # Name of the SA policy. The "null" value is deprecated and will be removed in AVD 5.0.0
        - name: <str; required; unique>
          esp:
            integrity: <str; "disabled" | "sha1" | "sha256" | "null">
            encryption: <str; "disabled" | "aes128" | "aes128gcm128" | "aes128gcm64" | "aes256" | "aes256gcm256" | "null">
          pfs_dh_group: <int; 1 | 2 | 5 | 14 | 15 | 16 | 17 | 20 | 21 | 24>

      # IPSec profiles.
      profiles:

          # Name of the IPsec profile.
        - name: <str; required; unique>

          # Name of the IKE policy to use in this profile.
          ike_policy: <str>

          # Name of the Security Association to use in this profile.
          sa_policy: <str>

          # IPsec connection (Initiator/Responder/Dynamic).
          connection: <str; "add" | "start" | "route">

          # Encrypted password - only type 7 supported.
          shared_key: <str>

          # Dead Peer Detection.
          dpd:

            # Interval (in seconds) between keep-alive messages.
            interval: <int; 2-3600; required>

            # Time (in seconds) after which the action is applied.
            time: <int; 10-3600; required>

            # Action to apply

            # * 'clear': Delete all connections
            # * 'hold': Re-negotiate connection on demand
            # * 'restart': Restart connection immediately
            action: <str; "clear" | "hold" | "restart"; required>

          # Ipsec mode type.
          mode: <str; "transport" | "tunnel">
      key_controller:

        # IPsec profile name to use.
        profile: <str>
    ```
