# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# strings are immutable


# Mutable and Immutable

# greet = "hello"

# print(greet + "is immutable")
# print([] + [123] + [123])  # mutable

# # sep in print
# print("Http", "google", "search", sep="-->")

# #end in print
# print("Hello", end=".")  # end is used to print the output in the same line

# String Formatting

# name = "Jay"

# print("Hello, " + name)  # normal concatenation
# print(f"Hello, {name}, how are you doing today?")  # f-string

# quote = 'To be or not to be'

# print(len(quote))  # length of the string (function)

# print(quote.upper())  # upper case (method)

# quoteU = quote.upper()


# # is is comparing the memory location of the objects (based on identity)
# print(quoteU is quote)  # False

# # == is comparing objects based on their values
# print(quoteU == quote)  # False


# strings
# len()   str()   .upper()   .lower()


# quote = 'To be or not to be'

# # find

# print(quote.find('T'))  # returns the index of the first occurence of the substring

# print(quote.replace('be', 'me'))  # replaces the substring with another substring

# Pig latin problem
# if the word starts with a vowel, add 'ay' to the end
# python -> ythonpay

# when you are dealing with string data in python
# clean your data before you start processing it
# remove any leading or trailing white spaces

# strip() method removes any leading or trailing white spaces