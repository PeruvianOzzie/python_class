from random import randint
def bank_operations():

    bank_dictionary = {}

    while True:
        selected_action = input('''
                        What Banking operation would you like to perform?
                        1 : Create Account
                        2 : Deposit Funds
                        3 : Withdraw Funds
                        4 : Check Balances
                        5 : exit
                        ''')
        try:
            selected_action = int(selected_action)
            if selected_action not in range(1,6):
                print("Operation selected not in rage of valid operations")
                continue
        
        except:
            print("Unknown operation error")

        if selected_action == 1:
            create_account(bank_dictionary)

        if selected_action == 2:
            deposit_funds(bank_dictionary)

        if selected_action == 3:
            withdraw_funds(bank_dictionary)

        if selected_action == 4:
            check_balance(bank_dictionary)

        if selected_action == 5:
            print("Bye!...")
            break

        again = input("Do you want to perform another operation? Y - N ") 

        if again == "Y" or again == "y":
            continue
        elif again == "N" or again == "n":
            print("Bye!...")
            break
        else:
            break

        

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


def deposit_funds(bank_dictionary):

    successful_transaction = False

    while not successful_transaction:
        account_number = input("What is your account number? ")
        account_number = str(account_number)
        if None == bank_dictionary.get(account_number):
            print("Account does not exist in our current portfolio")
            continue_op = input("Do you want to try again? ")
            if "Y" == continue_op or "y" == continue_op:
                continue
            else:
                print("Canceling Operation....")
                successful_transaction = True
        else:
            deposit_amount = input("How much would you like to deposit? ")
            deposit_amount = float(deposit_amount)
            if deposit_amount <= 0:
                print("You cannot deposit an account with a negative or zero dollars")
                print("Canceling Operation....")
                successful_transaction = True
            else:
                new_balance = deposit_amount + bank_dictionary[account_number]
                bank_dictionary[account_number] = new_balance
                successful_transaction = True
                print(f"deposit amount of {deposit_amount} was added to your account.  New balance: {new_balance}")

    return

def withdraw_funds(bank_dictionary):

    successful_transaction = False

    while not successful_transaction:
        account_number = input("What is your account number? ")
        account_number = str(account_number)
        if None == bank_dictionary.get(account_number):
            print("Account does not exist in our current portfolio")
            continue_op = input("Do you want to try again? ")
            if "Y" == continue_op or "y" == continue_op:
                continue
            else:
                print("Canceling Operation....")
                successful_transaction = True
        else:
            withdrawal_amount = input("How much would you like to withdraw? ")
            withdrawal_amount = float(withdrawal_amount)
            if withdrawal_amount <= 0:
                print("You cannot withdraw an account with a negative or zero dollars")
                print("Canceling Operation....")
                successful_transaction = True
            else:
                existing_balance = bank_dictionary[account_number]
                if withdrawal_amount > existing_balance:
                    print("You cannot withdraw an larger than existing funds")
                    print("Canceling Operation....")
                    successful_transaction = True
                else:
                    new_balance = bank_dictionary[account_number] - withdrawal_amount
                    bank_dictionary[account_number] = new_balance
                    successful_transaction = True
                    print(f"withdrawal amount of {withdrawal_amount} was subtracted form  your account.  New balance: {new_balance}")

    return



def check_balance(bank_dictionary):
    
    successful_transaction = False

    while not successful_transaction:
        account_number = input("What is your account number? ")
        account_number = str(account_number)
        account_balance = bank_dictionary.get(account_number)
        if None == account_balance:
            print("Account does not exist in our current portfolio")
            continue_op = input("Do you want to try again? ")
            if "Y" == continue_op or "y" == continue_op:
                continue
            else:
                print("Canceling Operation....")
                successful_transaction = True
        else:
            print(f"The current balnance on account {account_number} is {account_balance}")
            successful_transaction = True
    return

print(bank_operations())
