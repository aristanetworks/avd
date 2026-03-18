<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>validation_profiles</samp>](## "validation_profiles") | List, items: Dictionary |  |  |  | List of validation profiles defining hardware, logging, and fabric-related validation rules.<br>Validation profiles can be referenced from node definitions (for example under `l3leaf.nodes[].validation_profile`) and support single-level inheritance using `parent_profile`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "validation_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "validation_profiles.[].parent_profile") | String |  |  |  | Inherit settings from a parent profile defined under `validation_profiles`.<br>Max one level of profile inheritance: profile -> parent_profile |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "validation_profiles.[].hardware") | Dictionary |  |  |  | Hardware validation thresholds for the device.<br>These settings are only applied when `platform_settings/custom_platform_settings[].feature_support.hardware_validation` is set to `true`.<br>If hardware validation is disabled, all hardware validation checks are skipped and the keys under this section are ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_power_supplies</samp>](## "validation_profiles.[].hardware.min_power_supplies") | Integer |  |  |  | Minimum number of power supplies required for the device. Set to 0 to skip validation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_fans</samp>](## "validation_profiles.[].hardware.min_fans") | Integer |  |  |  | Minimum number of fans required for the device. Set to 0 to skip validation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_supervisors</samp>](## "validation_profiles.[].hardware.min_supervisors") | Integer |  |  |  | Minimum number of supervisor modules required for the device. Set to 0 to skip validation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_line_cards</samp>](## "validation_profiles.[].hardware.min_line_cards") | Integer |  |  |  | Minimum number of line cards required for the device. Set to 0 to skip validation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_fabric_cards</samp>](## "validation_profiles.[].hardware.min_fabric_cards") | Integer |  |  |  | Minimum number of fabric cards required for the device. Set to 0 to skip validation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transceiver_manufacturers</samp>](## "validation_profiles.[].hardware.transceiver_manufacturers") | List, items: String |  | See (+) on YAML tab |  | List of approved transceiver manufacturers for the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "validation_profiles.[].hardware.transceiver_manufacturers.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "validation_profiles.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;validate_no_errors_period</samp>](## "validation_profiles.[].logging.validate_no_errors_period") | Integer |  |  |  | Threshold (in minutes) defining how far back to check the logging buffer for error-level logs during the validation performed by the `anta_runner` role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclude_as_extra_fabric_validation_target</samp>](## "validation_profiles.[].exclude_as_extra_fabric_validation_target") | Boolean |  | `False` |  | Exclude this node from being used as a destination target from other fabric devices in the extra fabric validation tests performed by the `anta_runner` role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "validation_profiles.[].interfaces") | Dictionary |  |  |  | Interface validation settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;errdisable</samp>](## "validation_profiles.[].interfaces.errdisable") | Dictionary |  |  |  | Settings for the VerifyInterfaceErrDisabled test. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;avd_managed_only</samp>](## "validation_profiles.[].interfaces.errdisable.avd_managed_only") | Boolean |  | `False` |  | When true, only validate interfaces defined in the device structured configuration.<br>When false, validate all interfaces on the device. |

=== "YAML"

    ```yaml
    # List of validation profiles defining hardware, logging, and fabric-related validation rules.
    # Validation profiles can be referenced from node definitions (for example under `l3leaf.nodes[].validation_profile`) and support single-level inheritance using `parent_profile`.
    validation_profiles:
      - name: <str; required; unique>

        # Inherit settings from a parent profile defined under `validation_profiles`.
        # Max one level of profile inheritance: profile -> parent_profile
        parent_profile: <str>

        # Hardware validation thresholds for the device.
        # These settings are only applied when `platform_settings/custom_platform_settings[].feature_support.hardware_validation` is set to `true`.
        # If hardware validation is disabled, all hardware validation checks are skipped and the keys under this section are ignored.
        hardware:

          # Minimum number of power supplies required for the device. Set to 0 to skip validation.
          min_power_supplies: <int>

          # Minimum number of fans required for the device. Set to 0 to skip validation.
          min_fans: <int>

          # Minimum number of supervisor modules required for the device. Set to 0 to skip validation.
          min_supervisors: <int>

          # Minimum number of line cards required for the device. Set to 0 to skip validation.
          min_line_cards: <int>

          # Minimum number of fabric cards required for the device. Set to 0 to skip validation.
          min_fabric_cards: <int>

          # List of approved transceiver manufacturers for the device.
          transceiver_manufacturers: # (1)!
            - <str>
        logging:

          # Threshold (in minutes) defining how far back to check the logging buffer for error-level logs during the validation performed by the `anta_runner` role.
          validate_no_errors_period: <int>

        # Exclude this node from being used as a destination target from other fabric devices in the extra fabric validation tests performed by the `anta_runner` role.
        exclude_as_extra_fabric_validation_target: <bool; default=False>

        # Interface validation settings.
        interfaces:

          # Settings for the VerifyInterfaceErrDisabled test.
          errdisable:

            # When true, only validate interfaces defined in the device structured configuration.
            # When false, validate all interfaces on the device.
            avd_managed_only: <bool; default=False>
    ```

    1. Default Value

        ```yaml
        transceiver_manufacturers:
        - Arista Networks
        - Arastra, Inc.
        ```
