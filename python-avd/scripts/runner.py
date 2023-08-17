#!/usr/bin/env python3
# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import argparse
from sys import path

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, ".")

from pyavd.tools.multiprocess_runners import run_eos_cli_config_gen, run_eos_designs_facts, run_eos_designs_structured_configs
from pyavd.tools.template_var_files import run_template_var_files


def main():
    parser = argparse.ArgumentParser(
        prog="Runner",
        description="Run AVD Components like eos_cli_config_gen for multiple devices",
        epilog="See https://avd.sh/en/stable/ for details on supported variables",
    )
    parser.add_argument(
        "--eos_designs_facts",
        "-1",
        help=(
            "Run eos_designs_facts. Vars are read from dir set in --device_varfiles combined with any --common_varfile."
            " Facts are written to file set in --factfile if the option is set."
        ),
        action="count",
        default=0,
    )
    parser.add_argument(
        "--eos_designs_structured_configs",
        "-2",
        help=(
            "Run eos_designs_structured_configs. Vars are read from dir set in --device_varfiles combined with any --common_varfile"
            " and factsfile. Structured Configs are written to dir set in --struct_cfgfiles."
        ),
        action="count",
        default=0,
    )
    parser.add_argument(
        "--eos_cli_config_gen",
        "-3",
        help=(
            "Run eos_cli_config_gen. Vars are read from dir set in --struct_cfgfiles combined with --device_varfiles combined with any --common_struct_cfgfile."
            " Configs are written to dir set in --cfgfiles if the option is set."
            " Documentation markdown files are written to dir set in --docfiles if the option is set."
        ),
        action="count",
        default=0,
    )
    parser.add_argument(
        "--device_varfiles",
        "-g",
        help=(
            "Glob covering paths to YAML or JSON Files where device variables are read from."
            " Files matched by the glob will be iterated over,"
            " and the filename will decide the hostname of each device."
            " Data will be deepmerged on top of common_vars."
            " NOTE: Remember to enclose the glob in single quotes to avoid shell from expanding it."
        ),
    )
    parser.add_argument(
        "--common_varfile",
        "-e",
        help=(
            "YAML or JSON File where common variables are read from."
            " Multiple files can be added by repeating the argument."
            " Data will be deepmerged in the order of the common_varfile arguments."
        ),
        action="append",
    )
    parser.add_argument(
        "--factsfile",
        "-f",
        help="Destination YAML file for storing AVD Facts",
    )
    parser.add_argument(
        "--struct_cfgfiles",
        "-s",
        help=(
            "Source/Destination directory for device structured configuration files Filenames will be <hostname>.yml"
            " Will be used as input for eos_cli_config_gen and output for eos_designs"
        ),
    )
    parser.add_argument(
        "--common_struct_cfgfile",
        "-t",
        help=(
            "YAML or JSON File where common structured_config are read from."
            " Multiple files can be added by repeating the argument."
            " Data will be deepmerged in the order of the common_struct_cfgfiles arguments."
        ),
        action="append",
        default=[],
    )
    parser.add_argument(
        "--cfgfiles",
        "-c",
        help="Destination directory for device configuration files Filenames will be <hostname>.cfg",
    )
    parser.add_argument(
        "--docfiles",
        "-d",
        help="Destination directory for device documentation files Filenames will be <hostname>.md",
    )
    parser.add_argument(
        "--template_vars",
        "-j",
        help=(
            "Run Jinja2 templating on the var files given in --device_varfiles and --common_varfile."
            " All vars will be loaded first and then each file will be templated with all vars and"
            " the result is written in the file again."
            " NOTE: This can be destructive on the files in case of errors"
        ),
        action="count",
        default=0,
    )

    args = parser.parse_args()

    if args.template_vars:
        run_template_var_files(args.common_varfile, args.device_varfiles)

    if args.eos_designs_facts:
        run_eos_designs_facts(args.common_varfile, args.device_varfiles, args.factsfile)

    if args.eos_designs_structured_configs:
        run_eos_designs_structured_configs(
            args.common_varfile,
            args.factsfile,
            args.device_varfiles,
            args.struct_cfgfiles,
        )

    if args.eos_cli_config_gen:
        run_eos_cli_config_gen(
            args.common_struct_cfgfile,
            args.device_varfiles,
            args.struct_cfgfiles,
            args.cfgfiles,
            args.docfiles,
        )


if __name__ == "__main__":
    main()
