import requests
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NASA_API_KEY")

# pip install python-dotenv


# https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY

# my_request = requests.get("https://api.nasa.gov/planetary/apod?api_key=DRmrvSEjggbV0PgSlJ44057kSQFFvnvnGJ6y1fkE")
# my_request = requests.get(f"{API_URL}?api_key={api_key}")

# print(my_request.json())


def get_nasa_apod(api_key):

    API_URL = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        apod_data = response.json()

        return apod_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

apod_data = get_nasa_apod(api_key)
print(apod_data)

# # open the apod image in a browser
# import webbrowser

# webbrowser.open(apod_data['url'])








# if 'error' in get_nasa_apod(api_key):
#     print("An error occurred")
# else:
    # print(f"Today's NASA APOD is: {get_nasa_apod(api_key)['title']}")
    # print(f"Title: {apod_data[0].get('title')}")
    # print(f"Date: {apod_data['date']}")
    # print(f"Explanation: {apod_data['explanation']}")
    # print(f"URL: {apod_data['url']}")







# print(get_nasa_apod(api_key))