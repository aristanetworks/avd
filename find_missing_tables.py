# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import argparse
import glob
import sys

"""
Help on find_missing_tables.py:

DESCRIPTION
    Script to catch schema tables not covered in docs.
    ==================================================

    Checks if table files are added as snips in relevant role docs. Uses argparse to call in CLI with 3 arguments:
        - Glob for table files -> glob
        - Glob for md files, ie. the role docs -> glob
        - Start of relative path to role doc -> Default datatype of argparse arguments: str. For the use in the avd system, the argument: "roles", should be used as standard

        Using these 3 arguments the script calls the functions check_files_in_markdown(table_files, md_files)
        and returns the set with the table_files not covered in the role docs

        Can take any number of table_files and any number of role docs, and checks all md_files for all of the table files.

        Adds all table_files to a set, uses the function "make_path_relative" with the argument p__path_root to match the format of the paths from the table files
        to the format of the table files in the role docs. The .find() returns the first instance of the argument in the path string,
        so this solution even works for strings containing the directory name multiple times

        checks role docs for the snip string, and adds the table_files to the md_file_set, containing all the table files from the role docs already, and then returns the difference set
        containing the table files in the table_files set but not in the md_file_set.
"""

parser = argparse.ArgumentParser()

parser.add_argument("-t" "table_file_glob", type=glob.glob, nargs="*", help="The glob for the table file")
parser.add_argument(
    "-m" "--md_file_glob",
    type=glob.glob,
    nargs="*",
    help="The glob for the markdown file",
)
parser.add_argument(
    "-p" "--path_root",
    nargs="*",
    help="The start of the relative path of the md files, ie. the place in the table path from where to cut down to match",
)

args = parser.parse_args()

root_path = args.p__path_root[0]

md_files = list(*args.n__md_file_glob)

table_files = set(*args.table_file_glob)


def make_path_relative(path: str):
    index = path.find(f"{root_path}")
    if index != -1:
        relative_path = path[index:].replace("\\", "/")
        return relative_path
    else:
        return path


def check_files_in_markdown(table_files: set, md_files: list):
    md_file_set = set()
    for md_file in md_files:
        with open(md_file, "r") as f:
            md_lines = f.readlines()
            flag = False
            for line in md_lines:
                if line.strip() == "--8<--":
                    flag = not flag
                elif flag:
                    md_file_set.add(line.strip())

    for table_file in table_files:
        table_files.discard(table_file)
        table_files.add(make_path_relative(table_file))
    return table_files.difference(md_file_set)


print(check_files_in_markdown(table_files, md_files))

if len(check_files_in_markdown(table_files, md_files)) == 0:
    sys.exit(0)
else:
    sys.exit(1)
