def ret_order():

    return_order = []

    orders = [
        {"order_id": 1, "customer_name": "Bob", "total_amount": 250.00, "status": "completed"},
        {"order_id": 2, "customer_name": "Alice", "total_amount": 150.00, "status": "pending"},
        {"order_id": 3, "customer_name": "Charlie", "total_amount": 350.00, "status": "completed"},
        {"order_id": 4, "customer_name": "Davis", "total_amount": 100.00, "status": "shipped"},
    ]

    # total_amount >= 200 and status == "completed"

    for order in orders:
        if order["total_amount"] >= 200 and order["status"] == "completed":
            return_order.append(order)

    return return_order

print(ret_order())

        


