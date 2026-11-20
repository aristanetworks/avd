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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "schedule.jobs.[].name") | String | Required, Unique |  | Pattern: `(?!config)(?!summary$)[a-z0-9_-]+` | Schedule job name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "schedule.jobs.[].interval") | Integer |  |  | Min: 2<br>Max: 1440 | Interval in minutes. Used as the standalone interval when `at` is not set,<br>or as the recurring interval when combined with `at` and `at.once` is not True. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;at</samp>](## "schedule.jobs.[].at") | Dictionary |  |  |  | Schedule job at a specific time on a specific date. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time</samp>](## "schedule.jobs.[].at.time") | String | Required |  |  | Start time in HH:MM:SS format. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date</samp>](## "schedule.jobs.[].at.date") | String | Required |  |  | Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;once</samp>](## "schedule.jobs.[].at.once") | Boolean |  |  |  | Run the command a single time at the given time/date.<br>Mutually exclusive with `interval`. `once` takes precedence if both are set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "schedule.jobs.[].timeout") | Integer |  |  | Min: 1<br>Max: 480 | Job timeout in minutes for CLI command execution. Must be less than the job interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_log_files</samp>](## "schedule.jobs.[].max_log_files") | Integer | Required |  | Min: 0<br>Max: 10000 | Maximum number of log files to retain. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging_verbose</samp>](## "schedule.jobs.[].logging_verbose") | Boolean |  |  |  | Enable verbose logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loglocation</samp>](## "schedule.jobs.[].loglocation") | String |  |  |  | Log file location path (e.g. flash:/schedule/logs). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_total_size</samp>](## "schedule.jobs.[].max_total_size") | String |  |  |  | Maximum total size of log files (e.g. 110m, 1g).<br>Supported suffixes: b (bytes, default), k (kilobytes), m (megabytes), g (gigabytes). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;compression</samp>](## "schedule.jobs.[].compression") | String |  |  | Valid Values:<br>- <code>gzip</code><br>- <code>bzip2</code><br>- <code>xz</code> | Compression algorithm for log files. |
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

          # Interval in minutes. Used as the standalone interval when `at` is not set,
          # or as the recurring interval when combined with `at` and `at.once` is not True.
          interval: <int; 2-1440>

          # Schedule job at a specific time on a specific date.
          at:

            # Start time in HH:MM:SS format.
            time: <str; required>

            # Start date. Supported formats: mm/dd/yyyy or yyyy-mm-dd.
            date: <str; required>

            # Run the command a single time at the given time/date.
            # Mutually exclusive with `interval`. `once` takes precedence if both are set.
            once: <bool>

          # Job timeout in minutes for CLI command execution. Must be less than the job interval.
          timeout: <int; 1-480>

          # Maximum number of log files to retain.
          max_log_files: <int; 0-10000; required>

          # Enable verbose logging.
          logging_verbose: <bool>

          # Log file location path (e.g. flash:/schedule/logs).
          loglocation: <str>

          # Maximum total size of log files (e.g. 110m, 1g).
          # Supported suffixes: b (bytes, default), k (kilobytes), m (megabytes), g (gigabytes).
          max_total_size: <str>

          # Compression algorithm for log files.
          compression: <str; "gzip" | "bzip2" | "xz">

          # EOS CLI command to execute.
          command: <str; required>
    ```
