#source ./my_env/bin/activate
import sys

import calendar

# sys is a module that provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.
print(sys.path)


# import module
print(calendar)
# print(sys.modules)
print(sys.path)
print(calendar.month(2021, 1))

print(calendar.isleap(2021))


# import with an alias
import calendar as cal

# import module as alias
print(cal)
print(cal.month(2021, 1))

print(cal.isleap(2021))


# from-import statement

# from calendar import month, isleap
print(sys.modules["calendar"].__dir__())

print(month)
print(isleap(2021))

print(month(2021, 1))
print(isleap(2021))