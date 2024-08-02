#def divide(x, y):
#     if float(y) == 0:
#         return '', "Cannot divide by zero"
#     else:
#         return float(x) / float(y), ''


class DivisionError(Exception):
    pass


def divide_numbers(numerator, denominator):
    try:
        if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
            raise TypeError("Numerator and denominator must be numbers")

        if denominator == 0:
            raise DivisionError("Denominator cannot be zero")

        result = numerator / denominator
        return result

    except DivisionError as e:
        return str(e)
    except Exception as e:
        return str(e)

# # result = divide_numbers("10", 10)
# # print(result)

# result = divide_numbers(10, 2)
# print(result)