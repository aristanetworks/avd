=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_password</samp>](## "enable_password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hash_algorithm</samp>](## "enable_password.hash_algorithm") | String |  |  | Valid Values:<br>- md5<br>- sha512 |  |
    | [<samp>&nbsp;&nbsp;key</samp>](## "enable_password.key") | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device. |

=== "YAML"

    ```yaml
    enable_password:
      hash_algorithm: <str>
      key: <str>
    ```
