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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].interval") | Integer |  |  | Min: 2<br>Max: 1440 | Run the command every N minutes (standalone, no start time).<br>Mutually exclusive with `at` and `now`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;at</samp>](## "schedule.jobs.[].at") | Dictionary |  |  |  | Schedule job at a specific time, optionally on a specific date.<br>Mutually exclusive with `interval` (standalone) and `now`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "schedule.jobs.[].at.time") | String | Required |  |  | Start time in HH:MM:SS format. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date</samp>](## "schedule.jobs.[].at.date") | String |  |  |  | Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;once</samp>](## "schedule.jobs.[].at.once") | Boolean |  |  |  | Run the command a single time at the given time/date.<br>Mutually exclusive with `at.interval`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].at.interval") | Integer |  |  | Min: 2<br>Max: 1440 | Set interval for CLI command execution.<br>Mutually exclusive with `at.once`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;now</samp>](## "schedule.jobs.[].now") | Dictionary |  |  |  | Start the schedule immediately and repeat at the given interval.<br>Mutually exclusive with `interval` and `at`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].now.interval") | Integer | Required |  | Min: 2<br>Max: 1440 | Set interval for CLI command execution. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "schedule.jobs.[].timeout") | Integer |  |  | Min: 1<br>Max: 480 | Job timeout in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_log_files</samp>](## "schedule.jobs.[].max_log_files") | Integer |  |  | Min: 0<br>Max: 10000 | Maximum number of log files to retain. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging_verbose</samp>](## "schedule.jobs.[].logging_verbose") | Boolean |  |  |  | Enable verbose logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loglocation</samp>](## "schedule.jobs.[].loglocation") | String |  |  |  | Log file location path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_total_size</samp>](## "schedule.jobs.[].max_total_size") | String |  |  |  | Maximum total size of log files. |
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
          # Mutually exclusive with `at` and `now`.
          interval: <int; 2-1440>

          # Schedule job at a specific time, optionally on a specific date.
          # Mutually exclusive with `interval` (standalone) and `now`.
          at:

            # Start time in HH:MM:SS format.
            time: <str; required>

            # Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd.
            date: <str>

            # Run the command a single time at the given time/date.
            # Mutually exclusive with `at.interval`.
            once: <bool>

            # Set interval for CLI command execution.
            # Mutually exclusive with `at.once`.
            interval: <int; 2-1440>

          # Start the schedule immediately and repeat at the given interval.
          # Mutually exclusive with `interval` and `at`.
          now:

            # Set interval for CLI command execution.
            interval: <int; 2-1440; required>

          # Job timeout in seconds.
          timeout: <int; 1-480>

          # Maximum number of log files to retain.
          max_log_files: <int; 0-10000>

          # Enable verbose logging.
          logging_verbose: <bool>

          # Log file location path.
          loglocation: <str>

          # Maximum total size of log files.
          max_total_size: <str>

          # EOS CLI command to execute.
          command: <str; required>
    ```
