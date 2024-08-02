def basic_calculator():

    while True:
        left = input("Enter the left side of the operation: ")
        right = input("Enter the right side of the operation: ")
        operator = input("Enter the operator to perform operation: ")
        try:
            left = float(left)
            right = float(right)
        except:
            print("Error casting input information to float")
            break

        if operator == "+":
            print(f"the result of addition {summation(left, right)}")
        
        if operator == "-":
            print(f"the result of subtraction {subtraction(left, right)}")

        if operator == "*":
            print(f"the result of multiplication {multiplication(left, right)}")
        
        if operator == "/":
            print(f"the result of division {division(left, right)}")

        if operator == "**":
            print(f"the result of exponentiation {exponentiation(left, right)}")

        again = input("Do you want to perform another operation? Y - N") 

        if again == "Y":
            continue
        elif again == "N":
            break

def multiplication(left, right):

    result = left * right
    return isfloatorint(result)

def division(left, right):
    try:
        result = left / right
        return isfloatorint(result)
    except: 
        print("divide by 0 error")

def summation(left, right):
    result = left + right
    return isfloatorint(result)

def subtraction(left, right):
    result = left - right
    return isfloatorint(result)

def isfloatorint(number):
    if number.is_integer():
        number = int(number)
    
    return number

def exponentiation(left, right):
    try:
        result = pow(left, right)
        return isfloatorint(result)
    except:
        print("Exponentiation error")


print(basic_calculator())