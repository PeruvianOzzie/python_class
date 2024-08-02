def id_assigner(list_of_names):
    names_dict = {}
    for index, name in enumerate(list_of_names):
        names_dict[index + 1] = name

    return names_dict