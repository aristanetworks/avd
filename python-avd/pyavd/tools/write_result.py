import yaml


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def write_result(filename, result):
    mode = "w+"
    if filename == "/dev/stdout":
        mode = "w"

    with open(filename, mode, encoding="UTF-8") as file:
        file.write(result)


def write_yaml_result(filename, data):
    write_result(filename, yaml.dump(data, Dumper=NoAliasDumper, sort_keys=False, width=130))
