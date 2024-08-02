import math
import random
from random import randint

# def is_palindrome(word):
#     reversed_w = "'
#     reversed_w = reversed_w.join(reversed(word))

#     # return ''.join(reversed(word))
#     return reversed_w

# print(is_palindrome("Oscar"))

def is_divisible_by_3(number):
    
    result1 = number % 5
    result2 = number % 3
    
    if result1 == 0 and result2 == 0:
        return "fizzbuzz"
    elif result1 == 0:
        return "buzz"
    elif result2 == 0:
        return "fizz"
    else:
        return number
    
    
print(is_divisible_by_3(6))

def can_make_pasta(ingredients):

    right_ingredients = ["flour", "eggs", "oil"]
    ingredient_count = 0

    for ingredient in right_ingredients:
        for incoming_in in ingredients:
            if ingredient == incoming_in:
                ingredient_count += 1
    
    if ingredient_count == 3:
        return True
    else:
        return False


print(can_make_pasta(['salt', 'flour', 'oil']))

def is_inside_bounds(x, y):
    print(x, y)
    x_is_inside = False
    y_is_inside = False
    
    if x >= 0 and x <= 10:
        x_is_inside = True
    
    if y >= 0 and y <= 10:
        y_is_inside = True
        
    return x and y

print(is_inside_bounds(5, 11))

def is_inside_bounds(x, y, rect_x, rect_y, rect_width, rect_height):
    print(x, y, rect_x, rect_y, rect_width, rect_height)
    x_flag = False
    y_flag = False
    rect_x_flag = False
    rect_y_flag = False

    
    if x >= rect_x:
        x_flag = True
    
    if y >= rect_y:
        y_flag = True

    if x <= rect_x + rect_width:
        rect_x_flag = True
    
    if y <= rect_y + rect_height:
        rect_y_flag = True
        
    return x_flag and y_flag and rect_x_flag and rect_y_flag

print(is_inside_bounds(5, 5, 2, 3, 4, 4))

def has_quorum(attendees_list, members_list):
    attendees = len(attendees_list)
    members = len(members_list)

    attendance = attendees/members

    if attendance >= 0.5:
        return True
    else:
        return False

print(has_quorum(['Noor'], ['Basia', 'Noor', 'Laila', 'Talia', 'Zahara']))

def gear_for_day(is_workday, is_sunny):
    gear_list = []

    if not is_sunny and is_workday:
        gear_list.append("umbrella")
    
    if is_workday:
        gear_list.append("laptop")
    
    if not is_workday:
        gear_list.append("surfboard")

    return gear_list

print(gear_for_day(True, False))

def calculate_average(values):

    return sum(values)/len(values)
    print(values)
    pass

def calculate_grade(values):
    print(values)
    
    grade = 0
    
    if len(values) > 0:
        grade = (sum(values)/len(values))
    else:
        return None
    
    
    if grade >= 90:
        return "A"
    if grade >= 80 and grade < 90:
        return "B"
    if grade >= 70 and grade < 80:
        return "C"
    if grade >= 60 and grade < 70:
        return "D"
    if grade < 60:
        return "F"
    
print(calculate_grade([99, 80, 99, 80, 99, 80]))

def remove_duplicate_letters(s):
    print(s)
    unique = []
    return_string = ""

    for value in s:
        # if s.count(value) > 1:
        if value not in unique: 
            unique.append(value)

    # print(unique)
    
    if len(unique) > 0:
        return_string = return_string.join(unique)
    else:
        return_string = ""
    
    # print(return_string)
    
    return return_string

print(remove_duplicate_letters("akdlsidjalfkajdladksj"))

def sum_of_squares(values):
    if len(values) == 0:
        return None
    
    sum_of_all_fears = 0 
    
    for value in values:
        sum_of_all_fears += value ** 2 

    return sum_of_all_fears



print(sum_of_squares([2,4,6]))

def sum_of_first_n_numbers(limit):
    
    if limit < 0:
        return None
    
    numbers_lst = list(range(limit))
    added_nums = sum(numbers_lst)
    
    return added_nums

print(sum_of_first_n_numbers(3))

def sum_of_first_n_even_numbers(n):
    
    if n < 0:
        return None
    
    numbers_lst = list(range(0, (n * 2), 2))
    added_nums = sum(numbers_lst)
    
    return added_nums

print(sum_of_first_n_even_numbers(10))


def reverse_dictionary(dictionary):
    reversed_dict = {}
    for key, value in dictionary.items():
        if value not in reversed_dict:
            reversed_dict[value] = key
        else:
            reversed_dict[value].append(key)
    return reversed_dict

print(reverse_dictionary({'key1': 1, 'key2': 2, 'key3': 100}))


def add_csv_lines(csv_lines):

    returnList = []
    

    for line in csv_lines:
        print(line.split(","))
        tempList = list(line.split(","))
        for item in tempList:
            tempList[tempList.index(item)] = int(item)
        returnList.append(sum(tempList))

    return returnList

print(add_csv_lines(['1,2,10', '3', '100,1,3']))

def pairwise_add(list1, list2):

    returnList = []

    for line in range(len(list1)):
        returnList.append(list1[line] + list2[line])

    return returnList
    
print(pairwise_add([3, 1, 1000], [8, 1010, 9]))

def find_indexes(search_list, search_term):
    
    return_list = []
    index_count = 0 

    for list in search_list:
        if list == search_term:
            return_list.append(index_count)
        index_count += 1

    return return_list

print(find_indexes([100, 9, 100, 100, 9, 100], 100))

def translate(key_list, dictionary):
    
    return_list = []

    for key in key_list:
        temp_key = dictionary.get(key)
        if temp_key == None:
            return_list.append(None)
        else:
            return_list.append(temp_key)

    return return_list

print(translate(['one', 'one', 'two', 'three', 'two'], {'one': 1, 'two': 2}))

def make_sentences(subjects, verbs, objects):

    sentence = None
    return_list = []

    for subject in subjects:
        for verb in verbs:
            for object in objects:
                sentence = subject + " " + verb + " " + object
                return_list.append(sentence)

    return return_list


print(make_sentences(['I', 'You'], ['play', 'watch'], ['chess', 'cards']))

def check_password(password):
    
    lower_flag = False
    upper_flag = False
    digit_flag = False
    spec_flag = False
    len_flag = False
   

    for item in password:
        if item.islower():
            lower_flag = True
            continue
        if item.isupper():
            upper_flag = True
            continue
        if item.isdigit():
            digit_flag = True
            continue
        if item == "$" or item == "!" or item == "@":
            spec_flag = True
            continue

    if len(password) >= 6 and len(password) <= 12:
        len_flag = True
    
    return lower_flag and upper_flag and digit_flag and spec_flag and len_flag
        

print(check_password("A0z@abcabcabcabcabcabc"))

def count_word_frequencies(sentence):

    return_dic = {}
    temp_list = list(sentence.split(" "))

    for item in temp_list:
        if item == "":
            continue
        if return_dic.get(item) is not None:
            return_dic[item] = return_dic.get(item) + 1
        else:
            return_dic[item] = 1

    return return_dic

print(count_word_frequencies(""))

def halve_the_list(input_list):

    even_list = 0
    extra_item = 0

    even_list = int(len(input_list)/2)
    extra_item = len(input_list)%2


    temp_list = []
    return_list = []

    for item in range(even_list + extra_item):
        temp_list.append(input_list[item])

    return_list.append(temp_list)
    temp_list = []

    for item in range(even_list):
        temp_list.append(input_list[even_list + extra_item])
        even_list += 1
    
    return_list.append(temp_list)
    temp_list = []

    return return_list

print(halve_the_list([1, 2, 3, 4, 5]))

def generate_lottery_numbers(): 
    
    return_list = []
    random_num = 0

    while len(return_list) < 6:
        random_num = randint(1, 40)
        if random_num not in return_list:
            return_list.append(random_num)
    
    return return_list

print(generate_lottery_numbers())


def sum_fraction_sequence(a_number):

    total_sum = 0
    current_index = 1
    
    for a in range(a_number):
        total_sum = total_sum + (current_index / (current_index+1))
        current_index += 1
    
    return total_sum

print(sum_fraction_sequence(1))
        
def group_cities_by_state(cities_list):

    return_dic = {}

    for city in cities_list:
        city_state = list(city.split(", "))
        if return_dic.get(city_state[1]) is not None:
            check1 = return_dic.get(city_state[1])
            check1.append(city_state[0])
            return_dic[city_state[1]] = check1
        else:
            temp_city_list = []
            temp_city_list.append(city_state[0])
            return_dic[city_state[1]] = temp_city_list
        



    return(return_dic)
print(group_cities_by_state(['Seattle, WA', 'Olympia, WA', 'Topeka, KS', 'Wichita, KS']))

def specific_random():

    ramdon_list = list(range(10,500+1))

    new_list = []

    for x in ramdon_list:
        if x % 5 == 0 and x % 7 == 0 : 
            new_list.append(x)


    return random.choice(new_list)
        


print(specific_random())

def only_odds(input_numb):

    return_list = []

    for numb in input_numb:
        if numb % 2 != 0:
            return_list.append(numb)
    
    return return_list


print(only_odds([11, 13, 21, 31, 9, 5]))

def remove_duplicates(input_val):

    unique = []

    for value in input_val:
        if value not in unique: 
                unique.append(value)

print(remove_duplicates([1, 3, 3, 3, 3, 1, 12, 1, 2, 3, 3, 1, 2]))

def basic_calculator(left, op, right):
    
    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right
    
def shift_letters(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    word_list = list(word)
    return_string = ""

    for letter in word_list:
        upper_flag = False
        if letter.isupper():
            upper_flag = True
            letter = letter.lower()

        if letter == "z":
            letter_location = 0
        else:
            letter_location = alphabet.index(letter) + 1
        
        letter_to_add = alphabet[letter_location]


        if upper_flag:
            letter_to_add = letter_to_add.upper()

        return_string = return_string + letter_to_add

    return return_string

print(shift_letters(""))


# def temperature_differences(highs, lows):

#      returnList = []

#     for line in range(len(highs)):
#         returnList.append(highs[line] - lows[line])

#     return returnList

def biggest_gap(numbers_lst):

    biggest_gap = 0
    for index, number in enumerate(numbers_lst):

        if index < len(numbers_lst) - 1:
            sec_number_index = numbers_lst.index(number)


            sec_number = numbers_lst[sec_number_index + 1]

            if biggest_gap < abs(number - sec_number):
                biggest_gap = abs(number - sec_number)

    return biggest_gap

print(biggest_gap([12, 13, 100, 0, 10, 200]))

