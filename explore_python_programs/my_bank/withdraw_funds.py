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
