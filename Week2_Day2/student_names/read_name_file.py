def read_name_from_file(file_name):
    names = []
    with open(file_name) as file:
        for line in file:
            # print(line.strip())
            stripped_line = line.strip()
            if stripped_line:
                names.append(stripped_line)
    return names
