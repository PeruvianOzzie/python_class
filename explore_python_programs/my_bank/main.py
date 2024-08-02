import create_account
import deposit_funds
import withdraw_funds
import check_balance

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
            create_account.create_account(bank_dictionary)

        if selected_action == 2:
            deposit_funds.deposit_funds(bank_dictionary)

        if selected_action == 3:
            withdraw_funds.withdraw_funds(bank_dictionary)

        if selected_action == 4:
            check_balance.check_balance(bank_dictionary)

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


print(bank_operations())
