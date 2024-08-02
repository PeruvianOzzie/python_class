sales_data = [
    {"product_name": "Product A", "units_sold": 10, "price_per_unit": 15.0},
    {"product_name": "Product B", "units_sold": 5, "price_per_unit": 30.0},
    {"product_name": "Product C", "units_sold": 8, "price_per_unit": 12.5},
    {"product_name": "Product D", "units_sold": 15, "price_per_unit": 10.0},
]

# Given is a list of dictionaries containing sales data

# 1. Calculate the total sales foe each product (units_sold * price_per_unit)#

def calculate_total_sales_per_product(sales_data):

    total_sales_per_product = 0
    for product in sales_data:
        total_sales_per_product = product["units_sold"] * product["price_per_unit"]
        product["total_sales"] = total_sales_per_product

    return(sales_data)


# 2. Determine the product with the highest sales
def product_with_highest_sale(sales_data):
    unsorted_products = {}
    for product in sales_data:
        unsorted_products[product["product_name"]] = product["total_sales"]


    n = 1
    # Sorting by values
    top_n = dict(sorted(unsorted_products.items(), key=lambda item: item[1], reverse=True)[:n])

    return(top_n)

# 3. Determine the product with the lowest sales
def product_with_lowest_sale(sales_data):

    unsorted_products = {}
    for product in sales_data:
        unsorted_products[product["product_name"]] = product["total_sales"]


    n = 1
    # Sorting by values
    bottom_n = dict(sorted(unsorted_products.items(), key=lambda item: item[1])[:n])

    return(bottom_n)
    


# 4. Calculate the total sales for all products
def total_sales(sales_data):
    pass

# 5. Print a summary report with the total sales for each product, the product with the highest sales, the total revenue
def summary_report(sales_data):
    pass

updated_sales_data = calculate_total_sales_per_product(sales_data)
print(f"The sales data per product has been updated: {updated_sales_data} \n")


lowest_sale_item = product_with_lowest_sale(updated_sales_data)
item_name = list(lowest_sale_item.keys())[0]
item_sales = lowest_sale_item[item_name]
print(f"the product witht he lowest sale item is: {item_name} with total sales of {item_sales}\n")

highest_sale_item = product_with_highest_sale(updated_sales_data)
item_name = list(lowest_sale_item.keys())[0]
item_sales = lowest_sale_item[item_name]
print(f"the product witht he highest sale item is: {item_name} with total sales of {item_sales}\n")
