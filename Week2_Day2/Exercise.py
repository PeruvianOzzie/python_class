# Add new item to a list after a specified item
# Task: Add item 7000 after 6000 in the following list

# Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

for inner_item1 in list1:
    second_list = []
    if list == type(inner_item1):
        for inner_item2 in inner_item1:
            if list == type(inner_item2):
                inner_item2.append(7000)


print(list1)


    

# Expected output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]