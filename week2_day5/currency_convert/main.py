import requests
from currency_table import get_currency_table

def get_exchange_rate(source_currency, target_currency):

    API_URL = "https://open.er-api.com/v6/latest/"

    currency_dic = get_currency_table()

    try:

        source_currency_name = currency_dic[source_currency]
        target_currency_name = currency_dic[target_currency]

    except KeyError:

        raise KeyError(f"Currency Codes invalid for either {source_currency} or {target_currency}.  One or both do not exist in the dictionary")

    REQUEST_URL = API_URL + source_currency

    try:
        exchange_data = {}
        rates_dict = {}
        response = requests.get(REQUEST_URL)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        exchange_data = response.json()
        rates_dict = exchange_data["rates"]
        # print(exchange_data)
        exchange_rate = get_rate(rates_dict, target_currency)
        print(f"The exchange rate from the {source_currency_name} to the {target_currency_name} is {exchange_rate} \n")
        return(exchange_rate)
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"
    
   
    
def get_rate(rates_dict, target_currency):
    exchange_rate = rates_dict[target_currency]
    return exchange_rate

def convert_currency(amount, source_currency, target_currency):

    currency_dic = get_currency_table()
    source_more_than_one = ""
    target_more_than_one = ""

    if amount > 1:
        source_more_than_one = "s"
    

    try:
        source_currency_name = currency_dic[source_currency]
        target_currency_name = currency_dic[target_currency]
    except KeyError:

        raise KeyError(f"Currency Codes invalid for either {source_currency} or {target_currency}.  One or both do not exist in the dictionary")

    exchange_rate = float(get_exchange_rate(source_currency, target_currency))

    total_amount = amount * exchange_rate

    if total_amount > 1:
        target_more_than_one = "s"

    print(f"{amount} {source_currency_name}{source_more_than_one} is equal to {total_amount} {target_currency_name}{target_more_than_one} \n")

    return total_amount
    

print(get_exchange_rate("USD", "BHD"))

print(convert_currency(853, "BRL", "PEN"))