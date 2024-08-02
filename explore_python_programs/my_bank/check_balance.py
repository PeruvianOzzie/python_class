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