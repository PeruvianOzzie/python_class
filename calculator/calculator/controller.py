from operation import offerOperations
from operand import getOperand
from calculator import calculate

def welcome():
    print("                                                                                     \n"
        + "------------------------------------------------------------------------------------\n"
        + "                                SIMPLE CALCULATOR                                   \n"
        + "------------------------------------------------------------------------------------")

def farewell():
    print("                                                                                     \n"
        + "------------------------------------------------------------------------------------\n"
        + "                            THANK YOU FOR USING OUR APP                             \n"
        + "------------------------------------------------------------------------------------")

def controller():
    welcome()

    symbols = {
        '1' : '+',
        '2' : '-',
        '3' : 'x',
        '4' : '/',
        '5' : '^',
        '6' : 'mod'
    }
    operation = 0
    while(not operation == 7):
        operation = offerOperations()
        if operation == 7:
            farewell()
            continue
        u_left, left = getOperand("first")
        u_right, right = getOperand("second")

        print(f'''
              
        {u_left} {symbols[str(operation)]} {u_right} = {calculate(left, right, operation)}
            
              ''')

controller()