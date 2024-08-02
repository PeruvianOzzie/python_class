import requests
import os
import shutil

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NASA_API_KEY")
sol = "1000"
camera = "rhaz"

def get_rover_pictures(api_key, sol, camera):

    API_URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

    params = {
        "sol": sol,
        "camera": camera,
        "api_key": api_key
    }

    try:
        response = requests.get(API_URL, params=params)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        rover_data = response.json()

        return rover_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"

rover_picture_data = get_rover_pictures(api_key, sol, camera)

print(rover_picture_data)

photos_lst = rover_picture_data["photos"]
new_photos_dic = {}

print("listing photos now: \n")
for photo in photos_lst:
    split_uri = []
    split_uri = photo["img_src"].split("/")
    new_photos_dic[split_uri[-1]] = photo["img_src"]
    
print(new_photos_dic)

for key in new_photos_dic.keys():
    response = requests.get(new_photos_dic[key], stream=True)

    if response.status_code == 200:
        with open(key, "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
            print(f"file {key} was successfully saved")
    else:
        print(f"unable to save file: {key}")




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