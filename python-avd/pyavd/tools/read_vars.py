from json import JSONDecodeError
from json import loads as json_loads
from sys import stdin

from yaml import unsafe_load as yaml_load


def read_vars(filename):
    if filename == "/dev/stdin" and stdin.isatty():
        print("Write variables in YAML or JSON format and end with ctrl+d to exit")
    with open(filename, "r", encoding="UTF-8") as file:
        data = file.read()

    try:
        return json_loads(data)
    except JSONDecodeError:
        pass

    return yaml_load(data) or {}
