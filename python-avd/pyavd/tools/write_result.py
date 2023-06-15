def write_result(filename, result):
    mode = "w+"
    if filename == "/dev/stdout":
        mode = "w"

    with open(filename, mode, encoding="UTF-8") as file:
        file.write(result)
