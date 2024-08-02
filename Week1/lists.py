# lists in python
# lists are mutable

amazong_cart = ['notebooks', 'sunglasses', 'toys', 'grapes', 'lights']

# print(amazong_cart[0])  # indexing

# amazong_cart[0] = 'laptop'  # reassigning
# print(amazong_cart)


# slicing in lists
# print(amazong_cart[0:3])  # slicing
# print(amazong_cart[0::2])  # slicing with step
# print(amazong_cart[::-1])  # reverse the list returns new list

# # print(amazong_cart[::])
# new_cart = amazong_cart[::]
# print(new_cart is amazong_cart)  # False

# slicing syntax
# list[initial:End:IndexJump]


# .append() method
# it modifies the original list
# it does not return anything
# it only adds 1 item at a time to the end of the list
# amazong_cart.append('laptop')
# print(amazong_cart)


# # if you want to add more than one element in a list
# # use .extend() method
# # it modifies the original list
# # it does not return anything
# amazong_cart.extend(['table', 'chair'])
# print(amazong_cart)


# # .insert() method
# # it modifies the original list
# # it does not return anything
# # it takes two arguments
# # 1st argument is the index where you want to insert the element
# # 2nd argument is the element you want to insert


# .clear() method   # it clears the list


# .remove() method
# it removes the first occurence of the element from the list
# it modifies the original list
# it does not return anything
# amazong_cart.remove('toys')

# .pop() method - it removes the last element from the list
# it modifies the original list
# it returns the element that is removed from the list

# popped_item = amazong_cart.pop()
# print(popped_item)

# destructuring
# or list unpacking

a, b, c, *other,  d, = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)

print(range(0,11))