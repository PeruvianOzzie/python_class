# daily_temps = [61.2, 59.0, 59.4, 58.9, 60.1, 55.3, 55.6]

# print(sum(daily_temps) / len(daily_temps))

# lst = [5, 4, 9, 3, 1, 0]
# sorted(lst)
# print(lst)

# lst = [5, 4, 9, 3, 1, 0]
# print(list(reversed(lst)))
# bool_list = [False, False, False, False, False]
# print(any(bool_list))

# a = 10
# n = 20

# num_list = list(range(a, n))
# print(any(num_list))

# # Do not change this line of code
# even_nums = []
# even_idx = []
# count = 0


# # Do not change this line of code
# iteration_list = list(range(1, 1000, 3))
# print(iteration_list)

# for i in iteration_list:
#     if i % 2 == 0:
#         count += 1
#         even_nums.append(i)
#         even_idx.append(count)

# print(even_nums)

# don't change these lists
# lst1 = list(range(0, 100, 4))
# lst2 = list(range(1, 51, 2))
# lst3 = list(range(-100, 0, 4))

# # write your code below
# output_lst = []
# for first in lst1:
#     for second in lst2:
#         for third in lst3:
#             output_lst.append(first + second + third)
#             break

# print(output_lst)

my_list = list(range(1, 101))
for idx, num in enumerate(my_list):
    print(f"index is {idx} divided by number: {num}")
    print(idx / num)