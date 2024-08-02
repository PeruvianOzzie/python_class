def cash_on_hand(expenses):
   
    total_bal = 0
    # expenses_lst = list(expenses)

    for expense in expenses:
        total_bal += 30
        total_bal = total_bal - expense

    return total_bal 

print(cash_on_hand([28, 10, 35, 18, 23, 22, 9, 21, 17, 40]))  
