def offerOperations():
    print("Select an operation:")
    operation = 0
    error_msg = "That is not a valid selection. Please select from the following operations:"
    while not operation in range(1,8):
        operation = input('''
        1 : add
        2 : subtract
        3 : multiply
        4 : divide
        5 : exponentiation
        6 : modulus
        7 : exit

        ''')
        try:
            operation = int(operation)
            if operation in range(1,8):
                return operation
            else:
                print(error_msg)
        except:
            print(error_msg)