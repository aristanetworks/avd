<!--
  ~ Copyright (c) 2026 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>schedule</samp>](## "schedule") | Dictionary |  |  |  | Configuration of EOS scheduled jobs. |
    | [<samp>&nbsp;&nbsp;config</samp>](## "schedule.config") | Dictionary |  |  |  | Global schedule configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_concurrent_jobs</samp>](## "schedule.config.max_concurrent_jobs") | Integer |  |  | Min: 1<br>Max: 4 | Maximum number of concurrent scheduled jobs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prepend_hostname_logfile</samp>](## "schedule.config.prepend_hostname_logfile") | Boolean |  |  |  | Prepend hostname to the log file name. |
    | [<samp>&nbsp;&nbsp;jobs</samp>](## "schedule.jobs") | List, items: Dictionary |  |  |  | List of schedule jobs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "schedule.jobs.[].name") | String | Required, Unique |  |  | Schedule job name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].interval") | Integer |  |  | Min: 2<br>Max: 1440 | Run the command every N minutes (standalone, no start time).<br>Mutually exclusive with `at` and `now_interval`. Takes precedence over both if multiple are set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;at</samp>](## "schedule.jobs.[].at") | Dictionary |  |  |  | Schedule job at a specific time, optionally on a specific date.<br>Mutually exclusive with `interval` (standalone) and `now_interval`.<br>Takes precedence over `now_interval` if both are set. Ignored if `interval` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "schedule.jobs.[].at.time") | String | Required |  |  | Start time in HH:MM:SS format. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date</samp>](## "schedule.jobs.[].at.date") | String |  |  |  | Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;once</samp>](## "schedule.jobs.[].at.once") | Boolean |  |  |  | Run the command a single time at the given time/date.<br>Mutually exclusive with `at.interval`. Takes precedence over `at.interval` if both are set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].at.interval") | Integer |  |  | Min: 2<br>Max: 1440 | Set interval.<br>Mutually exclusive with `at.once`. `at.once` takes precedence if both are set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;now_interval</samp>](## "schedule.jobs.[].now_interval") | Integer |  |  | Min: 2<br>Max: 1440 | Start the schedule immediately and repeat every N minutes.<br>Mutually exclusive with `interval` and `at`. `interval` or `at` take precedence if they are set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "schedule.jobs.[].timeout") | Integer |  |  | Min: 1<br>Max: 480 | Job timeout. Must be less than the job interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_log_files</samp>](## "schedule.jobs.[].max_log_files") | Integer | Required |  | Min: 0<br>Max: 10000 | Maximum number of log files to retain. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging_verbose</samp>](## "schedule.jobs.[].logging_verbose") | Boolean |  |  |  | Enable verbose logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loglocation</samp>](## "schedule.jobs.[].loglocation") | String |  |  |  | Log file location path (e.g. flash:/schedule/logs). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_total_size</samp>](## "schedule.jobs.[].max_total_size") | String |  |  |  | Maximum total size of log files (e.g. 110m, 1g).<br>Supported suffixes: k (kilobytes), m (megabytes), g (gigabytes). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;command</samp>](## "schedule.jobs.[].command") | String | Required |  |  | EOS CLI command to execute. |

=== "YAML"

    ```yaml
    # Configuration of EOS scheduled jobs.
    schedule:

      # Global schedule configuration.
      config:

        # Maximum number of concurrent scheduled jobs.
        max_concurrent_jobs: <int; 1-4>

        # Prepend hostname to the log file name.
        prepend_hostname_logfile: <bool>

      # List of schedule jobs.
      jobs:

          # Schedule job name.
        - name: <str; required; unique>

          # Run the command every N minutes (standalone, no start time).
          # Mutually exclusive with `at` and `now_interval`. Takes precedence over both if multiple are set.
          interval: <int; 2-1440>

          # Schedule job at a specific time, optionally on a specific date.
          # Mutually exclusive with `interval` (standalone) and `now_interval`.
          # Takes precedence over `now_interval` if both are set. Ignored if `interval` is set.
          at:

            # Start time in HH:MM:SS format.
            time: <str; required>

            # Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd.
            date: <str>

            # Run the command a single time at the given time/date.
            # Mutually exclusive with `at.interval`. Takes precedence over `at.interval` if both are set.
            once: <bool>

            # Set interval.
            # Mutually exclusive with `at.once`. `at.once` takes precedence if both are set.
            interval: <int; 2-1440>

          # Start the schedule immediately and repeat every N minutes.
          # Mutually exclusive with `interval` and `at`. `interval` or `at` take precedence if they are set.
          now_interval: <int; 2-1440>

          # Job timeout. Must be less than the job interval.
          timeout: <int; 1-480>

          # Maximum number of log files to retain.
          max_log_files: <int; 0-10000; required>

          # Enable verbose logging.
          logging_verbose: <bool>

          # Log file location path (e.g. flash:/schedule/logs).
          loglocation: <str>

          # Maximum total size of log files (e.g. 110m, 1g).
          # Supported suffixes: k (kilobytes), m (megabytes), g (gigabytes).
          max_total_size: <str>

          # EOS CLI command to execute.
          command: <str; required>
    ```
