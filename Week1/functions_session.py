def say_whatUP(name, emoji):
    print(name, emoji)
    print(f'What up {name} {emoji}')
    print('What up '+ name + ' ' + emoji)


# say_whatUP('John', '🤣')


some_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n']

another_list = ["Party", "Laptop", "Party", "hello"]

whole_other_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n', "Party", "Laptop", "Party", "hello"]

a_list = ["1", "2", "3"]

def check_duplicates(any_list):
    duplicates = []
# check for duplicates in list and return a new list with duplicates
    for value in any_list:
    # print("all my values in any_list", value)
        if any_list.count(value) > 1:
        # print(value)
         if value not in duplicates: # to avoid duplicates in duplicates list
            duplicates.append(value)
            # print(duplicates)

    print(duplicates)
    return duplicates


check_duplicates(a_list)