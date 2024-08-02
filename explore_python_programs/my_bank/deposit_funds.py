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