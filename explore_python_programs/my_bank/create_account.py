from random import randint

def create_account(bank_dictionary):

    empty_bank_portfolio = False
    if not bank_dictionary:
        print("Our banks first customer!!!.  Welcome! ")
        empty_bank_portfolio = True

    duplicate_accnt = True

    initial_deposit = input("How much would you like to deposit in your new account? ")

    initial_deposit = float(initial_deposit)
    if initial_deposit <= 0:
        print("You cannot open an account with a negative or zero dollars for deposit")
        return
    

    while duplicate_accnt:
        account_number =  str(randint(1000, 2000))

        if empty_bank_portfolio:
            bank_dictionary[account_number] = initial_deposit
            duplicate_accnt = False
            print(f"Account number: {account_number} was successfully created.")
        else:
            if None == bank_dictionary.get(account_number):
                bank_dictionary[account_number] = initial_deposit
                duplicate_accnt = False
                print(f"Account number: {account_number} was successfully created.")
            else:
                continue     
    return