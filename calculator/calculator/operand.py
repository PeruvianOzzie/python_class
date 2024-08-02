def getOperand(ordinal):
    user_value = input(f"Enter the {ordinal} number on which to be operated: ")

    while True:
        try:
            op = float(user_value)
            return user_value, op
        except:
            user_value = input("That is not a valid number. Please enter a numerical value: ")